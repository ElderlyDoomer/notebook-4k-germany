"""Собирает page/laptops.html: шаблон page/template.html + данные data/laptops.json
+ справочные таблицы производительности из AMD/notes/perf-tables.md.

Запуск: python3 page/build.py
"""
import html
import json
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
payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
page = (root / "page" / "template.html").read_text(encoding="utf-8").replace("__DATA__", payload)
out = root / "page" / "laptops.html"
out.write_text(page, encoding="utf-8")
print(f"{out}: {len(data.get('laptops', []))} ноутбуков, {len(data.get('brands', []))} брендов, "
      f"{len(data.get('reference', []))} справочных таблиц, фото у {sum(1 for x in data.get('laptops', []) if x.get('photos'))}, {len(page) // 1024} КБ")
