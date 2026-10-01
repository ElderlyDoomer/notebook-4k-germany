"""Снимок страницы в headless Chrome через CDP (временный профиль, Chrome пользователя не трогается).

  python3 shot.py WIDTH OUT.png [--url URL] [--js 'код до снимка'] [--eval 'выражение → stdout'] [--height H] [--clip-selector CSS]

--js выполняется до снимка (можно await); --eval печатает JSON результата.
Снимок — всей страницы (captureBeyondViewport) или только элемента --clip-selector.
"""
import argparse, asyncio, base64, json, os, shutil, subprocess, tempfile, time, urllib.request
import websockets

p = argparse.ArgumentParser()
p.add_argument("width", type=int); p.add_argument("out")
p.add_argument("--url", default="http://localhost:8765/page/laptops.html")
p.add_argument("--js", default=""); p.add_argument("--eval", default="")
p.add_argument("--height", type=int, default=900); p.add_argument("--clip-selector", default="")
p.add_argument("--dark", action="store_true")
a = p.parse_args()

prof = tempfile.mkdtemp(prefix="shot-")
port = 9300 + os.getpid() % 500
chrome = subprocess.Popen(["google-chrome-stable", "--headless=new", f"--remote-debugging-port={port}", f"--user-data-dir={prof}",
                           "--no-first-run", "--no-default-browser-check", "--hide-scrollbars", f"--window-size={a.width},{a.height}", "about:blank"],
                          stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

async def main():
    for _ in range(100):
        try:
            tabs = json.loads(urllib.request.urlopen(f"http://127.0.0.1:{port}/json").read()); break
        except Exception:
            time.sleep(0.1)
    ws_url = [t for t in tabs if t["type"] == "page"][0]["webSocketDebuggerUrl"]
    async with websockets.connect(ws_url, max_size=2**30) as ws:
        n = 0
        async def cmd(method, **params):
            nonlocal n; n += 1; my = n
            await ws.send(json.dumps({"id": my, "method": method, "params": params}))
            while True:
                m = json.loads(await ws.recv())
                if m.get("id") == my:
                    if "error" in m: raise RuntimeError(m["error"])
                    return m.get("result", {})
        await cmd("Emulation.setDeviceMetricsOverride", width=a.width, height=a.height, deviceScaleFactor=1, mobile=a.width < 600)
        if a.dark:
            await cmd("Emulation.setEmulatedMedia", features=[{"name": "prefers-color-scheme", "value": "dark"}])
        await cmd("Page.enable"); await cmd("Page.navigate", url=a.url)
        await asyncio.sleep(1.5)
        async def run(expr):
            r = await cmd("Runtime.evaluate", expression=f"(async()=>{{ {expr} }})()", awaitPromise=True, returnByValue=True)
            if r.get("exceptionDetails"): raise RuntimeError(r["exceptionDetails"])
            return r.get("result", {}).get("value")
        if a.js: await run(a.js)
        await asyncio.sleep(0.8)  # картинки lazy
        await run("for(const i of document.images){ i.loading='eager'; } await new Promise(r=>setTimeout(r,800));")
        if a.eval: print(json.dumps(await run("return (" + a.eval + ")"), ensure_ascii=False, indent=1))
        params = {"format": "png", "captureBeyondViewport": True}
        if a.clip_selector:
            box = await run(f"const r=document.querySelector({json.dumps(a.clip_selector)}).getBoundingClientRect(); return {{x:r.x+scrollX,y:r.y+scrollY,width:r.width,height:r.height}}")
            params["clip"] = {**box, "scale": 1}
        else:
            h = await run("return document.documentElement.scrollHeight")
            params["clip"] = {"x": 0, "y": 0, "width": a.width, "height": h, "scale": 1}
        shot = await cmd("Page.captureScreenshot", **params)
        open(a.out, "wb").write(base64.b64decode(shot["data"]))

try:
    asyncio.run(main())
finally:
    chrome.terminate(); chrome.wait(); shutil.rmtree(prof, ignore_errors=True)
print(a.out)
