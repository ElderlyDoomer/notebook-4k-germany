# Проверка новых SKU из скана idealo (scan-16gb-gpu) по даташитам

_30.09.2026, локальная сессия. Даташиты — curl (IP в Германии); цены и история — idealo.de в Chrome пользователя (своя вкладка, капчи не было)._

## Итог

- **HP OmniBook 7 AI 16-ay0750ng — reject.** 16 ГБ распаяны, слотов 0 — докупить планку нельзя. Три источника HP/Icecat сходятся.
- **Попутная находка: HP OmniBook 7 AI 16-ay0770ng (`BM9T4EA#ABD`) — B-список, и лучший в нём.** Core Ultra 7 255H (Arrow Lake-H), 32 ГБ DDR5-5600 распаяны, 1 ТБ, 16" — **979,30 €** на hp.com. Это на ~225 € дешевле ThinkPad E16 G3 `22AY004XGE` (REPORT №9), и процессор сильнее. Минусы: слабый экран и риск HEVC, как у всех HP.

## Таблица

| Модель · P/N | Память (источник) | CPU | HEVC | Цена idealo (30.09.2026) | Итог | Вердикт |
|---|---|---|---|---|---|---|
| HP OmniBook 7 AI 16-ay0750ng · `BM9T3EA#ABD` | **16 ГБ DDR5-5600 распаяны, слотов 0.** Даташит HP [c09154107](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09154107): «16 GB DDR5-5600 MT/s (integriert)», «Anzahl der benutzerzugänglichen Speichersteckplätze: 0». [HP Store DE](https://www.hp.com/de-de/shop/products/laptops/hp-omnibook-7-ai-16-ay0750ng-bm9t3ea-abd): «Layout des Speichers: Integriert». Icecat (`BM9T3EA`): «Memory Formfaktor: On-board», «RAM-Speicher maximal: 16 GB» | Core Ultra 5 225H, **Arrow Lake-H** (idealo «Prozessor Codename»). По `intel-cpu.md` — современный ✔ | Риск (потребительская линейка HP, см. ниже) | **755,15 €** · hp.com (DE), возврат 14 дней, единственное предложение — [карточка](https://www.idealo.de/preisvergleich/OffersOfProduct/206602486_-omnibook-7-ai-16-ay0750ng-hp.html). 6 мес.: мин. 755,15 € (с 27.08), средн. 1006,19 €, макс. 1199 € | Не собрать 32 ГБ | **reject** |
| _Попутно:_ HP OmniBook 7 AI 16-ay0770ng · `BM9T4EA#ABD` | **32 ГБ DDR5-5600 распаяны, слотов 0.** Даташит HP [c09154072](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09154072): «32 GB DDR5-5600 MT/s (integriert)», «…Speichersteckplätze: 0». [HP Store DE](https://www.hp.com/de-de/shop/products/laptops/hp-omnibook-7-ai-16-ay0770ng-bm9t4ea-abd): «Integriert». Icecat (`BM9T4EA`): «On-board», максимум 32 ГБ. Двухканальность косвенно подтверждает графика Arc 140T: Intel включает Arc только при ≥ 16 ГБ в двух каналах (`intel-cpu.md`, п. 11) | Core Ultra 7 255H, **Arrow Lake-H** (idealo) — лучший CPU в списке, как у `21SK007KGE` | Риск (потребительская линейка HP) | **979,30 €** · hp.com (DE), возврат 14 дней, единственное предложение — [карточка](https://www.idealo.de/preisvergleich/OffersOfProduct/206602335_-omnibook-7-ai-16-ay0770ng-hp.html). 6 мес.: мин. 979,30 € (с 27.08, это и есть текущая цена), средн. 1343,01 €, макс. 1599 € | 979,30 € (зарядка 100 Вт USB-C в комплекте) | **b-list** (распайка 32) |

Та же серия на idealo ([карточка серии](https://www.idealo.de/preisvergleich/OffersOfProduct/206602371_-omnibook-7-ai-16-hp.html)): 16-ay0775ng (255H, 32 ГБ, 2 ТБ, OLED) — от 1299 € на hp.com, выше потолка.

## Пометки

- **Ошибка скана:** в скане написано «своей карточки нет». Карточка у 16-ay0750ng есть — `206602486`, и в ней idealo указывает Codename «Arrow Lake-H».
- **Сервис-мануал HP** ([MSG 16-ay0xxx / 16-az0xxx / 16-bh0xxx](https://kaas.hpcloud.hp.com/pdf-public/pdf_12123979_en-US-1.pdf), 2-е изд., 12.2025): у платформы есть и SO-DIMM (DDR5-5200: 2×8, 2×12, 2×16), и распайка. Про DDR5-5600 сказано «not accessible or upgradeable… (255H processors/RTX 4050 graphics)».
  Среди запчастей есть системная плата «Core Ultra 5 225H and 32 GB system memory» (P57671-601). Розничных SKU с SO-DIMM на idealo в этой серии я не видел: у всех трёх — распайка или 32 ГБ.
- **Порты и прочее (даташиты c09154107 / c09154072, одинаковые):** Thunderbolt 4 40 Гбит/с, USB-C 10 Гбит/с, 2× USB-A, HDMI 2.1, 2 слота M.2 (второй свободен), 70 Втч, 1,91 кг, зарядка 100 Вт в комплекте, 2 года гарантии HP.
  Экран у обеих моделей один: 16" 1920×1200 IPS, 300 нит, **62,5 % sRGB** (тот же класс, что 45 % NTSC у IdeaPad/ThinkBook) — для цвета нужен внешний монитор.
- **HEVC:** в даташитах и MSG нет ни слова о HEVC. QuickSpecs у потребительских HP нет (`hevc-audit.md`).
  В той же потребительской линейке OmniBook есть жалоба пользователя: OmniBook 7 Aero 13-bg1000 (AMD) — DXVA Checker не показывает HEVC-декодер, кодирование HEVC тоже недоступно ([HP Community, 04.07.2025](https://h30434.www3.hp.com/t5/Notebook-Video-Display-and-Touch/H265-HEVC-HW-encoder-and-decoder-not-available/td-p/9431209), открыто в Chrome). Это другая платформа, на Intel-версиях не проверено.
  Итог: **риск повышенный**. Если брать 16-ay0770ng — в первые 14 дней проверить DXVA Checker (`HEVC_VLD_Main10`) и экспорт H.265 через Quick Sync.
- **Цены:** обе модели продаёт только hp.com (DE), предоплата (Vorkasse), возврат 14 дней. Других магазинов на idealo нет.

## Источники

- idealo (Chrome, 30.09.2026): [16-ay0750ng](https://www.idealo.de/preisvergleich/OffersOfProduct/206602486_-omnibook-7-ai-16-ay0750ng-hp.html), [16-ay0770ng](https://www.idealo.de/preisvergleich/OffersOfProduct/206602335_-omnibook-7-ai-16-ay0770ng-hp.html), [серия](https://www.idealo.de/preisvergleich/OffersOfProduct/206602371_-omnibook-7-ai-16-hp.html); история — `/price-chart/…/history?period=6M`.
- Даташиты HP: [c09154107](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09154107) (0750ng), [c09154072](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09154072) (0770ng).
- HP Store DE: [BM9T3EA](https://www.hp.com/de-de/shop/products/laptops/hp-omnibook-7-ai-16-ay0750ng-bm9t3ea-abd), [BM9T4EA](https://www.hp.com/de-de/shop/products/laptops/hp-omnibook-7-ai-16-ay0770ng-bm9t4ea-abd).
- Icecat (open): `https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=HP&ProductCode=BM9T3EA` и `…=BM9T4EA`. По «16-ay0750ng» и «BM9T3EA#ABD» Icecat ничего не находит.
- HP MSG: [pdf_12123979](https://kaas.hpcloud.hp.com/pdf-public/pdf_12123979_en-US-1.pdf).
- Обзора notebookcheck именно этих конфигураций не нашёл.
