"""Собирает page/laptops.html: шаблон page/template.html + данные data/laptops.json
+ справочные таблицы производительности из AMD/notes/perf-tables.md.

Запуск: python3 page/build.py
"""
import html
import json
import math
import pathlib
import re

root = pathlib.Path(__file__).resolve().parent.parent


def inline_md(text):
    """Markdown в ячейке → безопасный HTML: ссылки, жирный, код; относительные ссылки — просто текст."""
    out, pos = [], 0
    for m in re.finditer(r"\[([^\]]+)\]\(([^)\s]+)\)", text):
        out.append(html.escape(text[pos:m.start()]))
        label, url = html.escape(m.group(1)), m.group(2)
        out.append(f'<a href="{html.escape(url)}" target="_blank" rel="noopener">{label}</a>' if url.startswith("http") else label)
        pos = m.end()
    out.append(html.escape(text[pos:]))
    s = "".join(out)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    return re.sub(r"`([^`]+)`", r"<code>\1</code>", s)


def md_tables(path):
    """Все таблицы Markdown файла с ближайшим заголовком над ними."""
    tables, title, lines = [], "", path.read_text(encoding="utf-8").splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("#"):
            title = line.lstrip("#").strip()
        if line.startswith("|") and i + 1 < len(lines) and re.match(r"^\|[\s:|-]+\|$", lines[i + 1].strip()):
            split = lambda row: [c.strip() for c in row.strip().strip("|").split("|")]
            headers, rows, i = split(line), [], i + 2
            while i < len(lines) and lines[i].startswith("|"):
                rows.append([inline_md(c) for c in split(lines[i])])
                i += 1
            tables.append({"title": title, "headers": [inline_md(h) for h in headers], "rows": rows})
            continue
        i += 1
    return tables


data = json.loads((root / "data" / "laptops.json").read_text(encoding="utf-8"))

def deep_merge(dst, src):
    for k, v in src.items():
        if isinstance(v, dict) and isinstance(dst.get(k), dict):
            deep_merge(dst[k], v)
        else:
            dst[k] = v


# Патчи data/patch-*.json накладываются по порядку имён: {"update": {id: поля}, "add": [...], "cash_guide": {...}, ...}
for patch_path in sorted((root / "data").glob("patch-*.json")):
    patch = json.loads(patch_path.read_text(encoding="utf-8"))
    by_id = {x.get("id") or x.get("pn"): x for x in data.get("laptops", [])}
    for key, fields in patch.get("update", {}).items():
        if key in by_id:
            deep_merge(by_id[key], fields)
        else:
            print(f"{patch_path.name}: нет ноутбука с id {key!r} — пропущен")
    data.setdefault("laptops", []).extend(patch.get("add", []))
    for key, value in patch.items():
        if key not in ("update", "add"):
            data[key] = value
# Сколько стоит довести память до 32 ГБ в двухканале: data/memory-upgrade.json (что докупить) × data/upgrade-prices.json (цены)
mu_path, up_path = root / "data" / "memory-upgrade.json", root / "data" / "upgrade-prices.json"
if mu_path.exists() and up_path.exists():
    mem_up = json.loads(mu_path.read_text(encoding="utf-8"))
    up = json.loads(up_path.read_text(encoding="utf-8"))
    data["upgrade_prices"] = up
    items = up.get("items", {})
    is_mem = re.compile(r"планк|DDR|RAM|памят|SO-DIMM", re.I)
    for x in data.get("laptops", []):
        m = mem_up.get(x.get("id"))
        if not m:
            continue
        m = dict(m)
        if not (x.get("memory") or {}).get("layout") and m.get("layout"):
            x.setdefault("memory", {})["layout"] = m["layout"]
        if m.get("possible") and m.get("buy"):
            def cost(kind):
                total = 0.0
                for b in m["buy"]:
                    offer = (items.get(b["what"]) or {}).get(kind)
                    if not offer or offer.get("eur") is None:
                        return None
                    total += float(offer["eur"]) * int(b.get("qty", 1))
                return round(total, 2)
            p = x.get("prices") or {}
            other = sum(float(a.get("eur") or 0) for a in p.get("addons") or [] if not is_mem.search(a.get("what", "")))
            for kind, base in (("any", p.get("any_eur")), ("cash", p.get("cash_eur"))):
                c = cost(kind)
                m["cost_" + kind] = c
                m["total_" + kind] = round(float(base) + other + c, 2) if base is not None and c is not None else None
        x["mem_upgrade"] = m
# Оценки «Цена» и «Средняя» — по единому правилу для всех (01.10.2026, после аудита):
# Цена — от суммы «до критериев»: ноутбук + докупка (prices.addons) + память до 32 ГБ в двухканале + SSD до 1 ТБ;
# наличная сумма, если наличные проверены, иначе любая оплата. 32 ГБ не набрать или нет цены нового → Цены нет,
# Средняя тогда не ставится (scores.n — по скольким оценкам посчитана).
def r05(v):
    return math.floor(v * 2 + 0.5 + 1e-9) / 2


def price_score(v):
    s = 10 if v <= 700 else 10 - (v - 700) / 100 if v <= 1000 else 7 - (v - 1000) / 50 if v <= 1100 else max(1, 5 - (v - 1100) / 50)
    return r05(s)


up_items = (data.get("upgrade_prices") or {}).get("items", {})
is_ssd = re.compile(r"\bSSD\b", re.I)
mem_word = re.compile(r"планк|DDR|RAM|памят|SO-DIMM", re.I)
for x in data.get("laptops", []):
    p, sc = x.setdefault("prices", {}), x.setdefault("scores", {})
    addons = p.get("addons") or []
    kind = "cash" if p.get("cash_eur") is not None else "any"
    base = p.get(kind + "_eur")
    crit, parts, reason = None, [], None
    if base is None:
        reason = "нет цены нового товара"
    else:
        crit = float(base) + sum(float(a.get("eur") or 0) for a in addons)
        mu = x.get("mem_upgrade") or {}
        if mu.get("possible") is False:
            crit, reason = None, "32 ГБ в двухканале не набрать"
        else:
            if mu.get("buy") and not any(mem_word.search(a.get("what", "")) for a in addons):
                c = mu.get("cost_" + kind) if mu.get("cost_" + kind) is not None else mu.get("cost_any")
                if c is not None:
                    crit += c
                    worst = "не подтвержд" in (mu.get("path") or "") or "не подтвержд" in (mu.get("layout") or "")
                    parts.append(["память до 32 ГБ" + (" (если раскладка худшая — не подтверждена)" if worst else ""), c])
            size = (x.get("ssd") or {}).get("size_gb")
            if size and float(size) < 900 and not any(is_ssd.search(a.get("what", "")) for a in addons):
                note = (x.get("ssd") or {}).get("note") or ""
                ssd_key = "ssd_2230_1tb" if "2230" in note and "2280" not in note else "ssd_2280_1tb"
                offer = (up_items.get(ssd_key) or {}).get(kind) or (up_items.get(ssd_key) or {}).get("any")
                if offer and offer.get("eur") is not None:
                    crit += float(offer["eur"])
                    parts.append(["SSD 1 ТБ", float(offer["eur"])])
    p["criteria_total"] = round(crit, 2) if crit is not None else None
    p["criteria_kind"], p["criteria_parts"], p["criteria_reason"] = kind, parts, reason
    sc["price"] = price_score(crit) if crit is not None else None
    marks = [sc.get(k) for k in ("problems", "repair", "price", "portability", "power")]
    vals = [float(m) for m in marks if m is not None]
    # без Цены Средняя не ставится: иначе ноутбук, которого нет в продаже, выглядел бы лучше
    sc["avg"] = r05(sum(vals) / len(vals)) if vals and sc["price"] is not None else None
    sc["n"] = len(vals)
# Видимые тексты — без внутренних кодов прежних отчётов (R1FY, R2R1, «Intel №1 до новых критериев» и т. п.)
SKIP_KEYS = {"id", "pn", "model", "url", "idealo_url", "shop_url", "specs_source", "source", "sources", "source_extra"}
def plain_text(s):
    s = re.sub(r"^(Intel|AMD) №(\d+) до новых критериев\.\s*", r"До требования к экрану был №\2 среди \1. ", s)
    s = re.sub(r"^(Intel|AMD) №(\d+) и прежний запасной\.\s*", r"До требования к экрану был №\2 среди \1 и запасным в итоге. ", s)
    s = re.sub(r"^Вариант к (Intel|AMD) №(\d+)", r"Вариант ноутбука, который до требования к экрану был №\2 среди \1", s)
    s = re.sub(r"Swift Air(?: 16)?(?: OLED)? R1FY", "Swift Air 16 (№2)", s)
    s = re.sub(r"(?<![\w-])R1FY(?![\w-])", "Swift Air 16 (№2)", s)
    s = re.sub(r"Aspire(?: 16 AI)?(?: OLED)? R2R1", "Aspire 16 AI OLED (NX.JP0EG.00Z)", s)
    s = re.sub(r"(?<![\w-])R2R1(?![\w-])", "Aspire 16 AI OLED (NX.JP0EG.00Z)", s)
    s = re.sub(r"\bв legacy\b", "в режиме поддержки", s)
    s = re.sub(r"\blegacy\b", "«только поддержка»", s)
    return s
def walk(v, key=""):
    if key in SKIP_KEYS:
        return v
    if isinstance(v, str):
        return plain_text(v)
    if isinstance(v, list):
        return [walk(i, key) for i in v]
    if isinstance(v, dict):
        return {k: walk(i, k) for k, i in v.items()}
    return v
data["laptops"] = [walk(x) for x in data.get("laptops", [])]
for k in ("cash_guide", "verdict_note", "chips"):
    if k in data:
        data[k] = walk(data[k])
# у ноутбуков «1×16 + слот» тоже показываем, сколько стоит довести до 32 ГБ (планка уже в докупке)
items0 = (data.get("upgrade_prices") or {}).get("items", {})
for x in data.get("laptops", []):
    lay0 = ((x.get("memory") or {}).get("layout") or "").lower().replace(" ", "")
    if x.get("mem_upgrade") or lay0 not in ("1x16+slot", "soldered16+slot"):
        continue
    kind_ram = "ddr4_16" if "DDR4" in ((x.get("memory") or {}).get("type") or "") else "ddr5_16"
    it = items0.get(kind_ram) or {}
    x["mem_upgrade"] = {"possible": True, "path": "докупить одну планку 16 ГБ во второй слот — будет 32 ГБ в двухканале", "buy": [{"what": kind_ram, "qty": 1}],
                        "cost_any": (it.get("any") or {}).get("eur"), "cost_cash": (it.get("cash") or {}).get("eur"), "auto": True}
photo_index = root / "photos" / "index.json"
if photo_index.exists():
    photos = json.loads(photo_index.read_text(encoding="utf-8"))
    for x in data.get("laptops", []):
        p = photos.get(x.get("id"))
        if p:
            x["photos"] = {"dir": f"../photos/{x['id']}/", "files": p["files"], "thumb": p["thumb"]}
perf = root / "AMD" / "notes" / "perf-tables.md"
if perf.exists():
    data["reference"] = md_tables(perf)
    for tbl in data["reference"]:
        if tbl["title"].startswith("1. Процессоры"):
            tbl["kind"] = "cpu"
        elif tbl["title"].startswith("2. Видеоядра"):
            tbl["kind"] = "gpu"
    # одинаковые заголовки («6. Разброс…» у процессоров и у видеоядер) и группы Puget без номера раздела
    seen = {}
    for tbl in data["reference"]:
        if tbl["title"].startswith(("Resolve Studio", "Premiere Pro")):
            tbl["title"] = "3. Puget: " + tbl["title"]
        seen[tbl["title"]] = seen.get(tbl["title"], 0) + 1
    for tbl in data["reference"]:
        if seen.get(tbl["title"], 0) > 1 and tbl["headers"]:
            tbl["title"] += " — " + re.sub(r"<[^>]+>", "", tbl["headers"][0]).strip()
chips = root / "data" / "chips.json"   # плюсы и минусы процессоров и видеоядер для справочника
if chips.exists():
    data["chips"] = json.loads(chips.read_text(encoding="utf-8"))
payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
page = (root / "page" / "template.html").read_text(encoding="utf-8").replace("__DATA__", payload)
out = root / "page" / "laptops.html"
out.write_text(page, encoding="utf-8")
print(f"{out}: {len(data.get('laptops', []))} ноутбуков, {len(data.get('brands', []))} брендов, "
      f"{len(data.get('reference', []))} справочных таблиц, фото у {sum(1 for x in data.get('laptops', []) if x.get('photos'))}, {len(page) // 1024} КБ")
