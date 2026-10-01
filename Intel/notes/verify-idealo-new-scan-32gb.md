# Проверка новых SKU из скана idealo 32 ГБ (по даташитам)

_30.09.2026, локальная сессия. Цены и история сняты на idealo.de в Chrome пользователя сегодня. Даташиты скачаны curl'ом (IP в Германии); geizhals (защита Cloudflare) открыт в Chrome._
_Источник SKU — `notes/idealo-scan-intel-32gb.md`. Цена планки (если понадобится) — из `notes/idealo-sku-other.md`: DDR5-5600 16 ГБ 206,80–248,89 €._

## Итог коротко

1. **Ни один из 4 SKU не стал top-candidate.**
2. **HP OmniBook 7 AI 16-ay0770ng `BM9T4EA#ABD` (979,30 €) — память распаяна** (32 ГБ DDR5-5600 «integriert», слотов нет). Это **B-список**.
   Внутри B-списка он лучший: Arrow Lake-H 255H + Arc 140T, TB4, 70 Втч, продаёт hp.com. Он дешевле и сильнее, чем `NX.JCJEG.00K` (№5 в REPORT, 999 €, маркетплейс).
   Главный риск — HEVC: у потребительской линейки OmniBook 7 уже есть задокументированный случай, когда аппаратный HEVC недоступен.
3. **Acer Aspire Go 15 AG15-71P-75W4 `NX.J4GEG.00D` — 2×16 SO-DIMM подтверждено** (даташит Acer + Icecat). Формально подходит (candidate), но хуже №1 `83HS00BLGE`:
   тот же i7-13620H, экран 15,6" 16:9, продаётся только на маркетплейсе, у Acer повышенный риск с HEVC.
4. **Acer Aspire 15 A15-51M-919A `NX.JCJEG.00T` — распайка LPDDR5** (даташит Acer). Idealo и Icecat пишут «DDR5» — это ошибка. B-список, дороже `00K`.
5. **A15-51M-94GX — P/N и даташит найти не удалось.** По платформе почти наверняка распайка. Продаётся только на маркетплейсе и не лучше `00K`.
6. **Попутно закрыта зацепка из скана 16 ГБ:** у HP 16-ay0750ng (`BM9T3EA`) 16 ГБ распаяны, максимум 16 ГБ → **reject**. Вариант «+ планка» невозможен.

## Таблица

| SKU · P/N | Память (источник) | CPU | HEVC | Цена idealo 30.09.2026 | Итог | Вердикт |
|---|---|---|---|---|---|---|
| HP OmniBook 7 AI 16-ay0770ng · `BM9T4EA#ABD` | **32 ГБ DDR5-5600 распайка, слотов нет**: HP Store — «32 GB DDR5-5600 MT/s (integriert)», «Layout des Speichers: Integriert»; Icecat — «Memory Formfaktor: On-board», максимум 32 ГБ; MSG HP — у 255H «DDR5-5600 (not accessible or upgradeable)» | Core Ultra 7 255H, **Arrow Lake-H** (idealo: «Prozessor Codename Arrow Lake-H») — современный ✔ | **риск**: QuickSpecs у потребительских HP нет; в MSG, HP Store и Icecat про HEVC ничего нет; на форуме HP — HEVC HW недоступен на OmniBook 7 Aero 13 (13-bg1000, AMD) | **979,30 €** — hp.com (DE), обычный магазин, возврат 14 дней, доставка до 10.10; других продавцов нет · [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/206602335_-omnibook-7-ai-16-ay0770ng-hp.html) | 979,30 € (зарядка 100 Вт USB-C в комплекте) | **b-list** (лучший в B) |
| Acer Aspire Go 15 AG15-71P-75W4 · `NX.J4GEG.00D` | **2×16 ГБ DDR5 SO-DIMM**, максимум 32 ГБ: даташит Acer — «Arbeitsspeicherbelegung 2 x 16 GB DDR5 RAM», «Bis zu 32 GB (2x 16 GB soDIMM)»; Icecat — «2 x 16 GB», «2x SO-DIMM» | i7-13620H, **Raptor Lake-H** (idealo), UHD 64 EU; не ловушка, но кремний 2023 года, нет кодирования AV1 — как у №1 | **повышенный риск (Acer)**: в даташите про HEVC ничего нет; Acer с 06.2026 продаёт в DE часть моделей «без HEVC» | **979,00 €** — только Galaxus Marktplatzhändler, возврат 30 дней · [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/206147182_-aspire-go-15-ag15-71p-75w4-acer.html) | 979,00 € (зарядка USB-C 65 Вт в комплекте) | **candidate** (хуже №1–3 REPORT) |
| Acer Aspire 15 A15-51M-94GX · P/N не найден | **не удалось подтвердить по SKU**. По платформе — распайка: у всех 5 известных SKU A15-51M (`NX.JCJEG.00A/.00B/.00C/.00K/.00T`) LPDDR5 (даташиты Acer у `.00K` и `.00T`, Icecat у `.00A/.00B/.00C`); Acer рекламирует платформу как «SpeedBoost LPDDR5» | i9-13900H, Raptor Lake-H (в карточке idealo кодового имени нет), Iris Xe 96 EU | повышенный риск (Acer) | **999,00 €** — только euronics.de, маркетплейс · [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/208669537_-aspire-15-a15-51m-94gx-acer.html) | 999,00 € (у A15-51M зарядка 90 Вт в комплекте — по даташитам `.00K`/`.00T`; для этого SKU не проверено) | **unclear** (скорее всего b-list; не лучше `.00K`) |
| Acer Aspire 15 A15-51M-919A · `NX.JCJEG.00T` | **32 ГБ LPDDR5 распайка**: даташит Acer (DE и EN, 04.11.2025) — «Onboard-RAM (nicht austauschbar oder erweiterbar)». ⚠️ Icecat («DDR5-SDRAM, max. 96 GB») и idealo («DDR5») ошибаются | i9-13900H, Raptor Lake-H, Iris Xe 96 EU | повышенный риск (Acer); в даташите про HEVC ничего нет | **1044,10 €** — e-tec.at (DE), обычный магазин, срок возврата idealo не показывает; 0815.eu — 1099,00 € (возврат 30 дней) · [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/208438558_-aspire-15-a15-51m-919a-acer.html) | 1044,10 € (зарядка 90 Вт в комплекте) | **b-list** (хуже `.00K` и HP) |

Планка никому не нужна: у всех четырёх 32 ГБ с завода, у трёх из них добавить память нельзя.

## История цен на idealo (6 мес., `/price-chart/.../history?period=6M`, снято 30.09.2026)

| SKU | Точек в истории | Минимум | ≤ 1100 € | Макс. |
|---|---|---|---|---|
| HP 16-ay0770ng | 76 | **979,30 € — сегодня** (такая же цена держалась с 27.08) | 11 из 76 точек | 1599,00 € |
| AG15-71P-75W4 | 15 | 979,00 € (цена не менялась с 30.03) | 15 из 15 | 979,00 € |
| A15-51M-94GX | 185 | 897,00 € (27.08) | 185 из 185 | 999,95 € |
| A15-51M-919A | 78 | 909,00 € (20.04) | 76 из 78 | 1450,71 € |

Сегодня API истории отвечал 200; в скане 32 ГБ он отдавал 404. Точки есть только за дни, когда были предложения.

## Пометки по каждому SKU

### HP OmniBook 7 AI 16-ay0770ng — `BM9T4EA#ABD`
- **Память:** MSG HP (Second Edition, 12.2025, табл. 1-1) описывает три варианта памяти в серии 16-ay0 / 16-az0 / 16-bh0:
  - «DDR5-5200 (accessible and upgradeable)» — 16×2 / 12×2 / 8×2. Это 16-az0xxx (Core 5/7 2xxH, см. ниже);
  - «DDR5-5600 (not accessible or upgradeable) … (255H processors/RTX 4050 graphics): 32 GB, 16 GB»;
  - LPDDR5X — у Panther Lake (16-bh0).

  В той же MSG есть модули SO-DIMM (16 ГБ `N77399-005` = SODIMM DDR5-5600). Поэтому одна MSG не доказывает распайку.
  Решают HP Store («integriert») и Icecat («On-board», максимум 32 ГБ). **Итог: распайка, 32 ГБ навсегда.** Двухканал есть: без него HP не указывала бы Arc 140T.
- **Прочее (HP Store, Icecat):**
  - экран 16" WUXGA; в MSG у этой матрицы 300 нит, sRGB 62,5 %, 60 Гц;
  - порты: 1× TB4 / USB4, 1× USB-C 10 Гбит/с, HDMI 2.1, 2× USB-A (10 и 5 Гбит/с);
  - Wi-Fi 7 BE201, 70 Втч, 1,91 кг, зарядка USB-C 100 Вт;
  - гарантия 2 года (отправка в сервис);
  - SSD M.2 2280; в MSG есть «Secondary SSD», но есть ли второй слот у этого SKU — не проверено.
- **HEVC:** QuickSpecs для потребительских HP нет. На форуме HP (04.07.2025) владелец OmniBook 7 Aero 13-bg1000 (`B4NF1AV`, AMD) пишет: в DXVA Checker нет декодера HEVC, кодирование HEVC тоже недоступно.
  Это та же потребительская линейка OmniBook 7, но другая модель и AMD. **Считать «риск»**: проверить DXVA Checker в течение 14 дней на возврат (hp.com даёт только 14).
- **Сравнение с REPORT:** в B-списке (распайка) сейчас `NX.JCJEG.00K` — i9-13900H, 999 € только на маркетплейсе Amazon.
  HP дешевле на ~20 €, CPU новее (есть кодирование AV1, Arc, NPU), больше аккумулятор, продаёт обычный магазин. Ремонт хуже, чем у №1 (память не расширить).
  Top-candidate не ставлю по правилам: распайка; кроме того, риск HEVC у HP.

### Acer Aspire Go 15 AG15-71P-75W4 — `NX.J4GEG.00D`
- **Даташит Acer (24.03.2025):**
  - 15,6" FHD IPS 16:9, матовый;
  - 2× USB-C Gen 2, 2× USB-A Gen 1, HDMI 2.1; нет Thunderbolt, кардридера и подсветки клавиатуры;
  - Wi-Fi 6, 53 Втч, зарядка USB-C 65 Вт, 1,8 кг;
  - гарантия 2 года (Einsende-Service).
- EAN 4711121785085. Idealo: «Prozessor Codename Raptor Lake-H», зарядка 65 Вт.
- Почему не top-candidate:
  - тот же CPU, что у №1 `83HS00BLGE` (995 €), но экран 15,6" 16:9 вместо 16" 16:10;
  - продаётся только на маркетплейсе, у Acer риск с HEVC;
  - за 849 € есть `NX.JS9EG.005` (i9-13900H, 2×16, 16", 120 Гц — см. скан 32 ГБ).

### Acer Aspire 15 A15-51M-94GX — P/N не найден
- **Где искал:**
  - карточка idealo — P/N и EAN нет;
  - Icecat — перебрал `NX.JCJEG.000–04Z`, нашлись только `.00A/.00B/.00C/.00K/.00T`;
  - geizhals — по «A15-51M-94GX» ничего нет;
  - acer.com/de-de — поиск ничего не дал;
  - Galaxus — нет;
  - cosse.de — «nicht mehr verfügbar»; techniklieben.de — 404;
  - euronics.de и DuckDuckGo — капча, не проходил.
- Вывод по платформе — распайка LPDDR5 (см. таблицу). Если нужен A15-51M, то `.00K` (999 €, даташит подтверждён) — ровно то же самое.

### Acer Aspire 15 A15-51M-919A — `NX.JCJEG.00T`
- **Даташит Acer (04.11.2025):**
  - 32 ГБ LPDDR5 onboard;
  - 1× USB4 / TB4, HDMI 2.1, 2× USB-A Gen 1;
  - зарядка 90 Вт, 1,77 кг, Iris Xe.
- То же, что `.00K`, но на 45 € дороже. Смысл брать его есть, только если у `.00K` пропадёт единственный продавец (Amazon MP), а цена `.00T` упадёт к минимуму (909 €).

## Попутно: другие HP OmniBook 7 16 (из блока «Variante» на idealo)

| SKU | Память (Icecat / HP Store) | CPU | Цена | Вердикт |
|---|---|---|---|---|
| 16-ay0750ng `BM9T3EA` | **16 ГБ DDR5-5600 распайка**, максимум 16 (Icecat «On-board»; HP Store «integriert») | Core Ultra 5 225H (Arrow Lake-H) | 755,15 € hp.com ([idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/206602486_-omnibook-7-ai-16-ay0750ng-hp.html), данные скана 16 ГБ) | **reject**: 16 ГБ распайки без слота; зацепку «+ планка» из `idealo-scan-intel-16gb-gpu.md` закрываю |
| 16-az0770ng `BM9T5EA` | 2×8 ГБ SO-DIMM, 512 ГБ (Icecat) | Core 7 240H (= i7-13620H, Raptor Lake-H) | не проверял | **reject** (2×8, 512 ГБ) |
| 16-az0750ng `BM8S7EA` | 2×8 ГБ DDR5-5200 SO-DIMM, 512 ГБ (Icecat) | Core 5 210H (= i5-13420H) | ab 689 € ([idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/206602519_-omnibook-7-16-az0750ng-hp.html)) | **reject** |

У серии 16-az0 память в SO-DIMM (MSG: «DDR5-5200 accessible and upgradeable», до 16×2). Но розничного SKU az0 с 2×16 и 1 ТБ в Германии не видел; отдельно не искал.

## Источники

- Idealo, карточки (30.09.2026, Chrome пользователя):
  [HP 16-ay0770ng](https://www.idealo.de/preisvergleich/OffersOfProduct/206602335_-omnibook-7-ai-16-ay0770ng-hp.html),
  [AG15-71P-75W4](https://www.idealo.de/preisvergleich/OffersOfProduct/206147182_-aspire-go-15-ag15-71p-75w4-acer.html),
  [A15-51M-94GX](https://www.idealo.de/preisvergleich/OffersOfProduct/208669537_-aspire-15-a15-51m-94gx-acer.html),
  [A15-51M-919A](https://www.idealo.de/preisvergleich/OffersOfProduct/208438558_-aspire-15-a15-51m-919a-acer.html).
- HP:
  - [HP Store DE, BM9T4EA#ABD](https://www.hp.com/de-de/shop/products/laptops/hp-omnibook-7-ai-16-ay0770ng-bm9t4ea-abd);
  - [HP Store DE, BM9T3EA#ABD](https://www.hp.com/de-de/shop/products/laptops/hp-omnibook-7-ai-16-ay0750ng-bm9t3ea-abd);
  - [MSG OmniBook 7 16 (16-ay0 / 16-az0 / 16-bh0), 2nd Ed. 12.2025](https://kaas.hpcloud.hp.com/pdf-public/pdf_12123979_en-US-1.pdf) — табл. 1-1 «Memory», табл. 6-2 «Memory modules»;
  - [форум HP — HEVC HW недоступен, OmniBook 7 Aero 13-bg1000](https://h30434.www3.hp.com/t5/Notebook-Video-Display-and-Touch/H265-HEVC-HW-encoder-and-decoder-not-available/td-p/9431209).
- Icecat (open):
  [BM9T4EA](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=HP&ProductCode=BM9T4EA),
  [BM9T3EA](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=HP&ProductCode=BM9T3EA),
  [BM9T5EA](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=HP&ProductCode=BM9T5EA),
  [BM8S7EA](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=HP&ProductCode=BM8S7EA),
  [NX.J4GEG.00D](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Acer&ProductCode=NX.J4GEG.00D),
  [NX.JCJEG.00T](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Acer&ProductCode=NX.JCJEG.00T) (ошибочно «DDR5»).
- Даташиты Acer (через geizhals):
  - [AG15-71P-75W4 / NX.J4GEG.00D, 24.03.2025](https://gzhls.at/blob/ldb/a/2/2/9/ad704a2f9608740ddce65127af6e3ba50df3.pdf);
  - [A15-51M-919A / NX.JCJEG.00T, DE](https://gzhls.at/blob/ldb/f/e/a/f/3f4a7dfc249f6b5a0d6ada562ae92611f6aa.pdf) и [EN](https://gzhls.at/blob/ldb/8/8/5/6/cea4e7ebc4d73467ee018b2b83221b6d9a60.pdf), 04.11.2025;
  - [A15-51M-93FG / NX.JCJEG.00K](https://gzhls.at/blob/ldb/f/8/5/3/b873a5475a7371afc0807af2980cd97d7e77.pdf).
- Acer ME, A15-51M-94UX `NX.JCJEM.003` (платформа, «SpeedBoost LPDDR5») — [acer.com/ae-en](https://www.acer.com/ae-en/laptops/aspire/aspire-intel/pdp/NX.JCJEM.003).
- CPU — `notes/intel-cpu.md` (255H — «современный ✔»; 13620H/13900H — Raptor Lake-H, «старый кремний»). HEVC — `notes/hevc-audit.md` (HP потребительские — риск; Acer — повышенный риск).
