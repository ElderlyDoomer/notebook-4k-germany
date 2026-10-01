"""Фотографии ноутбуков: photos/<id>/01.jpg … 05.jpg, thumb.jpg, sources.txt и общий photos/index.json.

Каждый ноутбук — своя папка с именем = id из data/laptops.json, поэтому снимки не путаются.

  python3 page/photos.py icecat <id> <Brand> <P/N>          # галерея и характеристики из открытого Icecat
  python3 page/photos.py urls <id> <url1> [<url2> …]         # свои ссылки (сайт производителя, магазин)
  python3 page/photos.py index                               # пересобрать photos/index.json по папкам

Icecat-характеристики (вес, батарея, порты, гарантия) сохраняются в photos/<id>/icecat-specs.json.
"""
import io
import json
import pathlib
import sys
import urllib.parse
import urllib.request

from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent.parent
PHOTOS = ROOT / "photos"
MAX_IMAGES, MAX_SIDE, THUMB_SIDE = 5, 1200, 360
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0 Safari/537.36"}


def fetch(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=40) as r:
        return r.read()


def to_jpeg(raw, side):
    img = Image.open(io.BytesIO(raw))
    if img.mode in ("RGBA", "LA", "P"):
        img = img.convert("RGBA")
        bg = Image.new("RGB", img.size, (255, 255, 255))
        bg.paste(img, mask=img.split()[-1])
        img = bg
    img = img.convert("RGB")
    img.thumbnail((side, side))
    out = io.BytesIO()
    img.save(out, "JPEG", quality=82, optimize=True, progressive=True)
    return out.getvalue()


def save(laptop_id, urls, origin=""):
    folder = PHOTOS / laptop_id
    folder.mkdir(parents=True, exist_ok=True)
    for old in folder.glob("[0-9][0-9].jpg"):
        old.unlink()
    kept, lines = 0, []
    for url in urls:
        if kept >= MAX_IMAGES:
            break
        try:
            raw = fetch(url)
            big = to_jpeg(raw, MAX_SIDE)
        except Exception as exc:  # битая ссылка или не картинка — пропускаем, но пишем в sources.txt
            lines.append(f"ПРОПУЩЕНО {url} — {exc}")
            continue
        kept += 1
        (folder / f"{kept:02d}.jpg").write_bytes(big)
        if kept == 1:
            (folder / "thumb.jpg").write_bytes(to_jpeg(raw, THUMB_SIDE))
        lines.append(f"{kept:02d}.jpg ← {url}")
    head = [f"Ноутбук: {laptop_id}", f"Откуда: {origin}" if origin else "", ""]
    (folder / "sources.txt").write_text("\n".join([h for h in head if h is not None] + lines) + "\n", encoding="utf-8")
    print(f"{laptop_id}: сохранено {kept} фото")
    return kept


def icecat(laptop_id, brand, pn):
    q = urllib.parse.urlencode({"UserName": "openIcecat-live", "Language": "de", "Brand": brand, "ProductCode": pn})
    page = f"https://live.icecat.biz/api?{q}"
    data = json.loads(fetch(page)).get("data") or {}
    gallery = [g.get("Pic") for g in data.get("Gallery") or [] if g.get("Pic")]
    main = (data.get("Image") or {}).get("HighPic")
    urls = list(dict.fromkeys(([main] if main else []) + gallery))
    if not urls:
        print(f"{laptop_id}: в Icecat нет фото ({brand} {pn})")
        return 0
    specs = {}
    for group in data.get("FeaturesGroups") or []:
        for f in group.get("Features") or []:
            name = ((f.get("Feature") or {}).get("Name") or {}).get("Value")
            if name:
                specs[name] = f.get("PresentationValue")
    folder = PHOTOS / laptop_id
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "icecat-specs.json").write_text(json.dumps({"source": page, "specs": specs}, ensure_ascii=False, indent=1), encoding="utf-8")
    return save(laptop_id, urls, origin=f"Icecat {brand} {pn} — {page}")


def index():
    idx = {}
    for folder in sorted(p for p in PHOTOS.iterdir() if p.is_dir()):
        files = sorted(f.name for f in folder.glob("[0-9][0-9].jpg"))
        if files:
            idx[folder.name] = {"files": files, "thumb": "thumb.jpg" if (folder / "thumb.jpg").exists() else files[0]}
    (PHOTOS / "index.json").write_text(json.dumps(idx, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"photos/index.json: {len(idx)} ноутбуков с фото")


if __name__ == "__main__":
    cmd, *rest = sys.argv[1:] or ["index"]
    if cmd == "icecat":
        icecat(*rest[:3])
    elif cmd == "urls":
        save(rest[0], rest[1:], origin="ссылки вручную")
    index()
