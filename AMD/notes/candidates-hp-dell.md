# Кандидаты HP и Dell на AMD, 15–16" (30.09.2026)

_Локальная сессия, Chrome пользователя (idealo — своя вкладка, капчи не было, ничего не отправлял). Цены — idealo.de 30.09.2026, «итого» = цена с доставкой лучшего предложения. Раскладка памяти — HP PartSurfer (сервисный BOM по P/N), QuickSpecs, Icecat, Dell Owner's Manual / Setup and Specifications. Критерии и ловушки — `../CLAUDE.md`, HEVC — `hevc-amd.md`._

## Коротко

1. **У HP и Dell на AMD нет ни одного SKU, который проходит всё сразу:** HEVC включён, 32 ГБ в двухканале, 1 ТБ и итог ≤ 1100 €.
2. **Ближе всех — HP EliteBook 8 G1a 16 `CN0Q3EC`** (HEVC есть, Ryzen 5 230, 32 ГБ / 512 ГБ): 1005,00 € + SSD 1 ТБ 142,89 € = **1147,89 €**, то есть выше потолка на 48 €.
   - Второго M.2 нет, SSD придётся **менять**, а не добавлять.
   - Раскладка не подтверждена: в BOM PartSurfer есть и модуль 16 ГБ, и модуль 32 ГБ.
   - → список `watch-over-1100`.
3. **Формально проходит только HP 255R G10 `CU0R1ES`** (1×16 + свободный слот): 607,99 + 243,90 (планка) + 142,89 (SSD) = **994,78 €**.
   - Но CPU — Ryzen 7 7735U (Rembrandt‑R, Zen 3+ 2022 года).
   - HEVC: нет данных при высоком риске (у HP серия 200 G9 — выключен).
   - Экран 15,6" FHD, 300 нит, 45 % NTSC.
   - → условно, **не рекомендую**.
4. **Цена HEVC-ловушки:** ProBook 4 G1a 16 `C7SP9ES` — 2×16 (PartSurfer), 1 ТБ, **906,99 €**, была бы лучшей покупкой группы.
   - Аппаратный HEVC выключен.
   - Самый дешёвый HP с HEVC и 2×16 / 1 ТБ — EliteBook 8 G1a 16 `CT3V9ES` за **1599 €**. Разница — **+692 €**.
5. **Исправление к `hevc-amd.md`:** EliteBook 8 G1a 16 `CT3V8ES` (32/1 ТБ, 1299 €) по PartSurfer — **1×32** (в BOM только модуль 32 ГБ). `C67H1EA` — тоже 1×32.
6. **HP G2a (2026):** всё дороже потолка — от 1279,87 €; у EliteBook 6 G2a 16 и 8 G2a 16 память распаяна (PartSurfer: «MB … 16GB»).
   - Узнать по P/N, заказана ли опция HEVC, нельзя: в BOM PartSurfer такой позиции нет.
7. **Dell (AMD):** на idealo нет ни одного AMD-ноутбука Dell 15–16" с 32 ГБ дешевле 1605 €.
   - 16-ГБ Dell 16 DC16255 и Dell Pro 16 PC16255 — 1×16 + свободный слот (Icecat), но с SSD 512 ГБ итог > 1100 €.
   - HEVC по политике Dell считаем выключенным.
   - Inspiron 16 5645 и Dell Pro 16 Essential AMD новыми на idealo не продаются.

## Как искал

- **idealo, сканы категории «Notebooks» по бренду** (без фильтра производителя CPU, поэтому ловушка с полем «Prozessorhersteller» не действует), сортировка по цене:
  - HP (id фильтра **471889**) × 15"/16" × 32 ГБ, страницы 1–3, до ~1420 €: [стр. 1](https://www.idealo.de/preisvergleich/ProductCategory/3751F471889-699493-1568565-7612877.html?sortKey=minPrice), [стр. 2](https://www.idealo.de/preisvergleich/ProductCategory/3751I16-15F471889-699493-1568565-7612877.html?sortKey=minPrice), [стр. 3](https://www.idealo.de/preisvergleich/ProductCategory/3751I16-30F471889-699493-1568565-7612877.html?sortKey=minPrice);
  - Dell (id **471884**) × 15"/16" × 32 ГБ: [стр. 1](https://www.idealo.de/preisvergleich/ProductCategory/3751F471884-699493-1568565-7612877.html?sortKey=minPrice) — AMD только Pro 16 Plus, от 1605,99 €;
  - Dell × 15"/16" × 16 ГБ: [стр. 1](https://www.idealo.de/preisvergleich/ProductCategory/3751F471884-699493-1568565-7612874.html?sortKey=minPrice), [стр. 2](https://www.idealo.de/preisvergleich/ProductCategory/3751I16-15F471884-699493-1568565-7612874.html?sortKey=minPrice).
- **idealo, поиск по модели:** EliteBook 8 G1a 16, EliteBook 6 G1a 16, ProBook 4 G1a 16, ProBook 465 G11, EliteBook 665 G11, «HP G2a 16», OmniBook 5 16, OmniBook 7 16 AMD, Envy 16, Pavilion 16, HP 255 G10 / G11, Dell Inspiron 16 5645, Dell Pro 16 Essential, Dell 15 DC15255.
- **HP PartSurfer** — сервисный BOM конкретного P/N. UI: `https://partsurfer.hp.com/partsurfer/?searchtext=<P/N>`, API (отвечает и в curl): `https://partsurfer.hpcloud.hp.com/bff/proxy/get?input=/Search/GenericSearch/<P/N>/country/DE/usertype/EXT`.
  - Как читаю строки «SKO-SODIMM»:
    - 32 ГБ и в BOM только модуль 16 ГБ → **2×16**;
    - только модуль 32 ГБ → **1×32**;
    - 16 ГБ и модуль 16 ГБ → **1×16 + свободный слот**.
  - Модель поддерживает только такие наборы (QuickSpecs, раздел MEMORY), поэтому вывод однозначен. Исключение — BOM с модулями обоих размеров (у `CN0Q3EC`).
  - У потребительских HP BOM бывает не всегда (`C8TT7EA` — нет).
- **Цены докупки (idealo, 30.09.2026):**
  - SSD 1 ТБ NVMe M.2 2280 — Kingston NV3 `SNV3S/1000G`: ab 134,90 €, **142,89 € с доставкой** (alternate.de, возврат 14 дн.) или 149,83 € (computeruniverse / cyberport, 30 дн.) — [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/204697967.html). WD Blue SN5000 1 ТБ — 171,00 € (galaxus) — [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/204448902_-blue-sn5000-nvme-1tb-western-digital.html).
  - Планка DDR5-5600 16 ГБ — Crucial `CT16G56C46S5`: **243,90 €** (`market-amd.md`, §4, idealo 30.09).

## Списки

| Список | SKU | Итог, € | Почему |
|---|---|---|---|
| A-2x16 | — | — | В HP/Dell с HEVC и 2×16 / 1 ТБ дешевле 1100 € нет. Самый дешёвый — `CT3V9ES`, 1599 €. |
| B16-plus-stick | HP 255R G10 `CU0R1ES` (условно) | **994,78** | 1×16 + слот (PartSurfer), но Zen 3+ и высокий риск HEVC; нужны и планка, и SSD. |
| C-plus-ssd | — | — | `CN0Q3EC`: второго M.2 нет, SSD только менять, итог 1147,89 → watch. |
| B-soldered | — | — | OmniBook 3 16 `D46JVEA` — 1×32 (Icecat); OmniBook 5 16-ag1477ng — только б/у; Envy x360 16 AMD — 16 ГБ распайки. |
| watch-over-1100 | EliteBook 8 G1a 16 `CN0Q3EC` | 1147,89 | HEVC есть, 32/512; раскладка не подтверждена, надо спросить продавца «2×16?». |
| reject (HEVC) | ProBook 4 G1a 16, EliteBook 6 G1a 16, ProBook 465 G11, EliteBook 665 G11, все Dell | — | см. раздел «HEVC выключен» |
| reject (прочее) | HP 15-fc (Barcelo‑R), OmniBook 3 15 `BP1G1EA` (2×8), EliteBook 8 G1a 16 `CT3V8ES` / `C67H1EA` (1×32), `CT3V6ES` / `CT3V7ES` (24 ГБ), Dell 15 DC15255 (1 слот, макс. 16) | — | см. карточки |

## Карточки SKU

### 1. HP EliteBook 8 G1a 16 `CN0Q3EC` — watch-over-1100 (ближе всех к потолку с HEVC)

| Поле | Значение | Источник |
|---|---|---|
| CPU | Ryzen 5 230 (Hawk Point, Zen 4, 760M); в PartSurfer — «MB UMA R5 PRO 230» | [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/214137501_-elitebook-8-g1a-16-cn0q3ec-hp.html) («Prozessor Codename Hawk Point»), [PartSurfer](https://partsurfer.hp.com/partsurfer/?searchtext=CN0Q3EC) |
| Память | 32 ГБ, 2 SODIMM. **Раскладка не подтверждена:** в BOM PartSurfer есть и `N77399-001` «SODIMM 16GB DDR5 5600», и `N77400-001` «SODIMM 32GB DDR5 5600». Это DaaS-SKU с 8 вариантами локализации (ABD, ABF, ABZ …), так что может быть и 2×16, и 1×32. В Icecat SKU нет | [PartSurfer](https://partsurfer.hp.com/partsurfer/?searchtext=CN0Q3EC); QuickSpecs: «32GB (1 x 32 GB)» и «32GB (2 x 16 GB)» — оба варианта ([c09120200 v21](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09120200)) |
| SSD | 512 ГБ M.2 2280 (`N77392-001`). **Слот M.2 один**: «storage is unfortunately limited to a single M.2 2280 slot» | PartSurfer; [NBC](https://www.notebookcheck.net/HP-EliteBook-8-G1a-16-AI-laptop-review-Redesigned-inside-and-out.1103659.0.html) |
| HEVC | **есть**: «Hardware Acceleration HEVC (H.265) CODEC is supported» | [c09120200](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09120200), GRAPHICS |
| Экран, порты | 16" WUXGA; 2× Thunderbolt 4 40 Гбит/с (DP 2.1), USB-C 10 Гбит/с, USB-A 5 Гбит/с, HDMI 2.1 | QuickSpecs c09120200 |
| Вес, батарея, зарядка | 1,69 кг (idealo); 62 Втч; блок 65 Вт USB-C в BOM (idealo пишет 100 Вт) | PartSurfer, idealo |
| Цена | **999,00 € / 1005,00 € с доставкой**, asaboshisystems.de (Vorkasse, доставка до 02.10) — единственное предложение. Срок возврата в предложении не указан → законные 14 дней | [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/214137501_-elitebook-8-g1a-16-cn0q3ec-hp.html), 30.09.2026 |
| История | карточка с 17.09.2026, всё время 999 € | idealo API |
| Итог | 1005,00 + SSD 1 ТБ 142,89 = **1147,89 €** (> 1100). Если окажется 1×32 — не подходит вовсе | — |

### 2. HP 255R G10 `CU0R1ES` — B16-plus-stick, условно (не рекомендую)

| Поле | Значение | Источник |
|---|---|---|
| CPU | Ryzen 7 7735U — **Rembrandt‑R, Zen 3+ (2022)**, 680M; вердикт `amd-cpu.md`: «только если очень дёшево» | [PartSurfer](https://partsurfer.hp.com/partsurfer/?searchtext=CU0R1ES) («MB UMA R7 7735U 255R G10»), `amd-cpu.md` |
| Память | 16 ГБ = **1×16** SODIMM DDR5 (`N77399-005`) + свободный слот. Но HP пишет: «All slots are customer non-accessible / non-upgradeable», максимум «32GB DDR5-4800 (1 x 32GB)» | PartSurfer; [QuickSpecs c09053765 v7, 06.03.2026](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09053765) |
| SSD | 512 ГБ M.2 2280 → менять на 1 ТБ; второй M.2 — не проверено | PartSurfer |
| HEVC | в QuickSpecs только «Support HD decode, DX12, HDMI 1.4b» → **нет данных, риск высокий** (HP выключил HEVC в «200 Series G9»; G10 — наследник) | QuickSpecs; `hevc-amd.md`, §1.2 |
| Экран, порты | 15,6" FHD UWVA, 300 нит, 45 % NTSC (панель в BOM — «FHD AG LBL UWVA 300»); HDMI 1.4b, USB-C 10 Гбит/с, USB-A 5 Гбит/с | QuickSpecs, PartSurfer |
| Вес, зарядка | 1,66 кг (idealo); адаптер 45 Вт в BOM (idealo пишет 65 Вт); FreeDOS | PartSurfer, idealo |
| Цена | **607,99 €** с доставкой, notebooksbilliger.de (возврат 30 дн.); 606,99 € — nullprozentshop.de; 8 предложений | [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/210295290.html), 30.09.2026 |
| История | минимум за год 599 € (с 11.05.2026 цена не менялась); ≤ 1100 € все 140 дней с появления карточки | idealo API |
| Итог | 607,99 + 243,90 (16 ГБ DDR5; в паре заработает на 4800) + 142,89 (SSD 1 ТБ) = **994,78 €** | — |
| Соседи с той же раскладкой | `C99TJES` 649 € ([idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/209321475.html)), `C8TH1ES` 706,99 € ([idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/210295301.html)) — PartSurfer: 1×16 | — |

### 3. HP EliteBook 8 G1a 16 — остальные SKU (HEVC есть)

Все цены — idealo 30.09.2026, «ab» из выдачи; раскладка — по [PartSurfer](https://partsurfer.hp.com/partsurfer/?searchtext=CT3V8ES).

| P/N | CPU | ОЗУ / SSD | Раскладка | Цена, € (предл.) | Вердикт |
|---|---|---|---|---|---|
| `CT3V8ES` | R7 250 | 32 / 1 ТБ, FreeDOS | **1×32** (только модуль 32 ГБ) | 1299,00 (8); 1306,99 с доставкой — nullprozentshop, 1307,99 — NBB; минимум за год 1111 € (17.12.2025), за 182 дня ни одного дня ≤ 1100 — [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/208652377_-elitebook-8-g1a-16-ct3v8es-hp.html) | reject (1×32) |
| `CT3V9ES` | R7 250 | 32 / 1 ТБ, LTE | 2×16 | 1599,00 (9) — [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/208508534_-elitebook-8-g1a-16-ct3v9es-hp.html) | дорого; самый дешёвый HP с HEVC, 2×16 и 1 ТБ |
| `AD3F6ET` | R7 250 | 32 / 1 ТБ | 2×16 | 1625,00 (7) — [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/206525943_-elitebook-8-g1a-16-ad3f6et-hp.html) | дорого |
| `AD3F7ET` | R7 250 | 32 / 1 ТБ, LTE | 2×16 | 2128,00 (9) — [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/206703230.html) | дорого |
| `C67H1EA` | AI 7 PRO 350 | 32 / 1 ТБ | **1×32** | предложений нет — [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/211095794_-elitebook-8-g1a-16-c67h1ea-hp.html) | reject |
| `AD4J7ET#ABZ` | R5 230 | 16 / 512 | 1×16 + слот | предложений нет — [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/209369388_-elitebook-8-g1a-16-ad4j7et-abz-hp.html) | нет в продаже |
| `AD3F4ET` | R5 230 | 16 / 512, LTE | 1×16 + слот | 1199,00 (20) — [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/206703229_-elitebook-8-g1a-16-ad3f4et-hp.html) | 1199 + 243,90 + 142,89 = 1585,79 → reject |
| `AD3F3ET` / `AD3F5ET` | R5 230 / R7 250 | 16 / 512 | не проверено | 1275,85 / 1374,62 | reject (цена) |
| `CT3V7ES` / `CT3V6ES` | R5 230 | **24** / 512 | нет в PartSurfer; по QuickSpecs 24 ГБ = 2×12 | 969,00 / 999,00 (8) — [7ES](https://www.idealo.de/preisvergleich/OffersOfProduct/208508528_-elitebook-8-g1a-16-ct3v7es-hp.html), [6ES](https://www.idealo.de/preisvergleich/OffersOfProduct/208508530.html) | reject: до 32 ГБ — менять обе планки |

Карточка модели: [idealo 206525896](https://www.idealo.de/preisvergleich/OffersOfProduct/206525896_-elitebook-8-g1a-16-hp.html) — ab 969 €, 124 предложения.

### 4. HP G2a (2026) — HEVC «опция при заказе», всё дороже 1100 €

| Линейка | Мин. цена, € | Память | HEVC | Источник |
|---|---|---|---|---|
| EliteBook 8 G2a 16 | 1737,71 (`DL9U5ET`, AI 5 435, 16/512) | распайка: «MB UMA RAI5 435 16GB LPDDR5» | есть ([c09233498](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09233498)) | [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/211044941.html), [PartSurfer](https://partsurfer.hp.com/partsurfer/?searchtext=DL9U5ET) |
| EliteBook 6 G2a 16 | 1279,87 (`E02FSET`, R5 230, 16/512) | распайка: «MB UMA R5230 16GB» | опция при заказе ([c09236064](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09236064)) | [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/211713223.html), [PartSurfer](https://partsurfer.hp.com/partsurfer/?searchtext=E02FSET) |
| ProBook 4 G2a 16 | 1286,24 | не проверено | опция при заказе ([c09228216](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09228216)) | [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/210666938.html) |

**Как узнать опцию HEVC по P/N:** не нашёл способа.
- В BOM PartSurfer (`E02FSET`, `E02FWET`, `DL9U5ET`) позиции HEVC или кодека нет.
- На странице SKU на hp.com про HEVC ничего нет (`hevc-amd.md`, §1.2).
- Остаётся письменное подтверждение от продавца или HP либо проверка DXVA Checker в 14 дней на возврат.

### 5. HP, потребительские AMD

| Линейка | SKU (idealo) | Память (источник) | Цена, € | Вердикт |
|---|---|---|---|---|
| OmniBook 5 16 AMD | `16-ag1477ng` (AI 7 350, 32/1 ТБ) | распайка LPDDR5x (MSG, `brands-amd.md`) | **только б/у**, 2 предложения — [поиск](https://www.idealo.de/preisvergleich/MainSearchProductCategory.html?q=16-ag1477ng) | reject (не новый); в DE нет новых подходящих SKU (скан HP 32 ГБ) |
| OmniBook 7 16 AMD | — | MSG OmniBook 7 16 (16-ay0 / bh0 / az0) — только Intel | — | **в DE нет**: на idealo только OmniBook 7 Aero 13 AMD (13,3") — [поиск](https://www.idealo.de/preisvergleich/MainSearchProductCategory.html?q=HP+OmniBook+7+16+AMD+Ryzen) |
| OmniBook 3 16 AMD | `16-bv0074ng` = `D46JVEA` (AI 7 445, 32/1 ТБ) | **1×32** («Speicherlayout: 1 x 32 GB») — [Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=HP&ProductCode=D46JVEA); MSG: «Memory is not accessible or upgradeable» ([pdf_13159558](https://kaas.hpcloud.hp.com/pdf-public/pdf_13159558_en-US-1.pdf)) | 1130,23, только Amazon Marketplace; минимум за год 949 € (02.05.2026) — [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/210080645.html) | reject (1×32) |
| OmniBook 3 15 AMD | `15-fn0655ng` = `BP1G1EA` (AI 5 340, 16/1 ТБ) | **2×8**: Icecat «2 x 8 GB», PartSurfer «SODIMM 8GB» | 695,00 (euronics, маркетплейс); 728,48 — energeto.de; минимум за год 642,76 € (18.09.2026) — [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/206785231_-omnibook-3-15-fn0655ng-hp.html) | reject (2×8: +475 € за комплект → ~1170 €) |
| HP 15-fc (15,6") | `15-fc0063ng` R5 7430U 32/512 — 688,00 (13) [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/208441340.html); `15-fc0065ng` 32/512 — 699,00 (4) [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/208408777.html); `15-fc0677ng` = `C8TT7EA` R7 7730U 32/1 ТБ — 923,30 (9) [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/207948312.html) | DDR4-3200, «Speicherlayout: Not available» ([Icecat C8TT7EA](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=HP&ProductCode=C8TT7EA)); BOM в PartSurfer нет | см. слева | reject: **Barcelo‑R** (Zen 3 2021 года, Vega) — ловушка «старый CPU» (`amd-cpu.md`) |
| HP 255 G10 | от 371,27 — [карточка модели](https://www.idealo.de/preisvergleich/OffersOfProduct/202679861.html) | Mendocino 7x20U — LPDDR5 onboard (до 16); Barcelo‑R 7x30U — DDR4 ([c08479497](https://www8.hp.com/h20195/V2/GetPDF.aspx/c08479497)) | — | reject (ловушки CPU). «32 ГБ» бывает только в сборке продавца `884420874911` (919 €, не заводской SKU) |
| HP 255R G10 | `CU0R1ES` и соседи, см. карточку 2 | 1×16 + слот | 607,99 | условно |
| HP 255 G11 | — | — | — | **в DE нет**: поиск idealo «HP 255 G11» выдаёт только G10 / 255R G10 |
| Envy x360 16 AMD | `16-ad0675ng` 8840HS 16 ГБ — 899,00 [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/207778580.html); `16-ad0654ng` 8640HS — 899,99; `16-ad0177ng` — 1049 | распайка ([NBC](https://www.notebookcheck.net/HP-Envy-x360-2-in-1-16-review-Ryzen-7-8840HS-beats-Core-Ultra-7-155U.837856.0.html)); 32 ГБ AMD-версий в DE нет (скан HP 32 ГБ) | — | reject (16 ГБ распайки) |
| Pavilion 16 AMD | `16-ag0477ng` 8840U 16 ГБ — только б/у (829,99) | распайка ([NBC](https://www.notebookcheck.net/HP-Pavilion-16-review-Budget-AMD-CPU-in-a-stylish-laptop.959151.0.html)) | — | reject; новых нет |
| Victus / Omen | Omen 16-ap `C2VM8EA` (R9 8940HX) — 1129 € | — | — | группа gpu |

HEVC у потребительских HP на AMD не документируется. Известен случай с выключенным HEVC на OmniBook 7 Aero 13 AMD, поэтому риск считаю **высоким** (`hevc-amd.md`, §1.3).

### 6. Dell (AMD): память по мануалам, цены idealo

HEVC — по политике Dell: без дискретки, 4K, Dolby Vision или CyberLink **считать выключенным** (`hevc-amd.md`, §2). Поэтому все Dell ниже → reject, даже если подходят по памяти.

| Линейка | Память по мануалу | SKU на idealo (30.09) | Итог | Вердикт |
|---|---|---|---|---|
| **Dell 16 DC16255** | 2 SODIMM, максимум 32; 32 ГБ продаётся **только как 1×32**; 16 ГБ — 2×8 или 1×16; **один M.2 2230** ([Setup & Specs](https://dl.dell.com/content/manual20191269-dell-16-dc16255-p-setup-and-specifications.pdf?language=en-us)) | `450R1` R5 220 16/512 — 849,00 (10) [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/213117938.html), Icecat: **1×16** ([Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Dell&ProductCode=450R1)); `21W0X` R7 250 16/1 ТБ — 1119,00 (1) [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/211451969.html), раскладка не проверена (в Icecat нет) | 450R1: 849 + 243,90 + SSD 2230 1 ТБ (цена не снята, ≥ 143) ≈ 1236+; 21W0X: 1119 + 243,90 = 1362,90 | reject (цена + HEVC) |
| **Dell 15 DC15255** | 1 SODIMM DDR4 (7530U / 7730U) или LPDDR5x onboard (7520U), **максимум 16 ГБ** ([Owner's Manual](https://dl.dell.com/content/manual20023858-dell-15-dc15255-owner-s-manual.pdf?language=en-us)) | R5 7520U 8/512 — 597,81 [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/213273546.html) | — | reject (32 ГБ невозможно) |
| **Dell Pro 16 PC16255** | 2 SODIMM, до 64; есть 2×16 и 1×32; один M.2 2230 для SSD ([Owner's Manual](https://dl.dell.com/content/manual33305221-dell-pro-16-pc16255-owner-s-manual.pdf?language=en-us)) | 32 ГБ AMD на idealo нет. 16/512, у всех **1×16** по Icecat: `0JP8Y` R5 PRO 215 — 949,00 [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/206988416.html); `HT3DJ` R5 220 — 949,00 [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/206563355.html); `7693X` — 950,00; `DCNC3` — 961,48; `DFT4N` AI 5 PRO 340 — 1078,99 [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/206563352.html); `YXRKP` AI 5 340 — 1114,83 | 949 + 243,90 + SSD ≥ 143 ≈ 1336+ | reject (цена + HEVC) |
| Dell Pro 16 Plus PB16255 | распайка LPDDR5x («32 GB LPDDR…», [Icecat Y7X3K](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Dell&ProductCode=Y7X3K)) | `TY5FC` AI 7 350 — 1605,99; `5WY0N` — 1870,32; `Y7X3K` R5 PRO 230 32/1 ТБ — 1901,71 [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/209854641.html) | — | reject (цена) |
| **Dell Pro 16 Essential AMD** | модели нет на dell.com (`brands-amd.md`) | поиск idealo «Dell Pro 16 Essential» — AMD есть только у Pro 14 Essential (14", вне размера) и Pro 15 Essential — [поиск](https://www.idealo.de/preisvergleich/MainSearchProductCategory.html?q=Dell+Pro+16+Essential) | — | **в DE нет** |
| Dell Pro 15 Essential (15,6") | PV15255 (7320U / 7520U, Mendocino): onboard, максимум 16 ([Owner's Manual](https://dl.dell.com/content/manual33819502-dell-pro-15-essential-pv15255-owner-s-manual.pdf?language=en-us)). У версии 2026 с Ryzen 5 130 мануал не нашёл — не проверено | `P0NMK` R5 130 16/1 ТБ — 854,00 (24) [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/209951790.html); `6PFYT` 16/512 — 765,63; `1X1C9` — 801,99 | — | reject (HEVC; Rembrandt; раскладка не проверена) |
| **Inspiron 16 5645** | 2 SODIMM, есть «32 GB: 2 x 16 GB … dual-channel»; один M.2 2230 ([Owner's Manual](https://dl.dell.com/content/manual18275235-inspiron-16-5645-owner-s-manual.pdf?language=en-us)) | **в DE нет новых**: поиск idealo — только одна подозрительная карточка «Inspiron 5645 R7 8840U» за 2306,46 € и аксессуары — [поиск](https://www.idealo.de/preisvergleich/MainSearchProductCategory.html?q=Dell+Inspiron+16+5645) | — | в DE нет |

## HEVC выключен — не брать (цены, чтобы было видно, чего стоит ловушка)

Фраза «Hardware acceleration for CODEC H.265/HEVC … is disabled on this platform» есть в QuickSpecs: [ProBook 4 G1a 16 c09111176](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09111176), [EliteBook 6 G1a 16 c09111179](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09111179), [ProBook 465 G11 c08908497](https://www8.hp.com/h20195/V2/GetPDF.aspx/c08908497), [EliteBook 665 G11 c08927104](https://www8.hp.com/h20195/V2/GetPDF.aspx/c08927104) (`hevc-amd.md`, §1.2).

| Модель | P/N | CPU | ОЗУ / SSD | Раскладка (PartSurfer) | Цена idealo 30.09, € | Ссылка |
|---|---|---|---|---|---|---|
| ProBook 4 G1a 16 | **`C7SP9ES`** | R5 230 (Hawk Point) | 32 / 1 ТБ, FreeDOS | **2×16** | **906,99** nullprozentshop.de / 907,99 NBB (возврат 30 дн.) / 907,99 galaxus; минимум за год **699 €** (17.12.2025); ≤ 1100 € все 182 дня | [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/208030540_-probook-4-g1a-16-c7sp9es-hp.html) |
| ProBook 4 G1a 16 | `C65T9ES` | R5 230 | 32 / 512 | нет в PartSurfer | 1025,13 (1) | [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/207830984.html) |
| ProBook 4 G1a 16 | `C7SQ0ES` | R5 230 | 32 / 1 ТБ, W11 Pro | 2×16 | 1129,00 (8) | [карточка модели](https://www.idealo.de/preisvergleich/OffersOfProduct/208030487.html) |
| ProBook 4 G1a 16 | `AD2N2ET` | R7 250 | 32 / 1 ТБ | 2×16 | 1167,99 (29) | [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/206571932.html) |
| ProBook 4 G1a 16 | `C65TTES` / `C7SQ3ES` / `C7SQ4ES` | R7 250 | 32 / 1 ТБ | — | 1189,00 / 1199,00 / 1299,00 | [карточка модели](https://www.idealo.de/preisvergleich/OffersOfProduct/208030487.html) |
| ProBook 4 G1a 16, 16 ГБ | `C07P2ES` R3 210 — 599; `C7SP7ES` — 699; `C07P1ES` — 749; `C7SQ1ES` R7 — 777; `AD2N0ET` — 849; `C65TVES` R7 16/1 ТБ — 949 | | | | | [карточка модели](https://www.idealo.de/preisvergleich/OffersOfProduct/208030487.html) — ab 599, 651 предложение |
| EliteBook 6 G1a 16 | `AD3K1ET` | R7 250 | 32 / 1 ТБ | 2×16 | 1800,91 (27) | [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/206525611.html) |
| EliteBook 6 G1a 16 | `AD3J9ET` / `9M4J4AT` | R5 230 / R5 PRO 220 | 16 / 512 | — | 1103,14 / 1099,00 | [карточка модели](https://www.idealo.de/preisvergleich/OffersOfProduct/206525547.html) — ab 1099 |
| ProBook 465 G11 | — | 7x35U (Rembrandt‑R) | — | — | ab 1071,38, всего 2 предложения — модель уходит | [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/204307465.html) |
| EliteBook 665 G11 | `8Z719AV` (CTO) | R7 PRO 7735U | 32 / 1 ТБ | — | 949,00 (4) | [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/206577198.html) |
| EliteBook 665 G11 | модель | R7 PRO 7735U | 16/512 LTE, 32/512 | — | ab 899,00 (905,00 с доставкой); 32/512 — 949,00 | [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/204264280.html) |

**Во что обходится ловушка:**
- `C7SP9ES` (2×16, 1 ТБ, Zen 4) — **906,99 €**, ещё в декабре стоил 699 €.
- Та же память у HP с HEVC (EliteBook 8 G1a 16 `CT3V9ES`) — **1599 €**, то есть +692 €.
- Ближайшая альтернатива без ловушки — ThinkBook 16 G9 AHP `21UT004QGE` (~1068 €, `market-amd.md`), то есть +161 €.

## Что не проверено

- Раскладка `CN0Q3EC`: 2×16 или 1×32. PartSurfer неоднозначен, в Icecat SKU нет. Спросить у asaboshisystems.de до покупки.
- Второй M.2 у HP 255R G10 — в QuickSpecs не нашёл; для итога не важно, SSD считал заменой.
- Цена SSD M.2 **2230** 1 ТБ (для Dell) — не снимал: Dell и так выбыли по цене и HEVC.
- Dell Pro 15 Essential 2026 (Ryzen 5 130): мануал не найден, раскладка не проверена.
- MSG для HP 15-fc0xxx не нашёл: DuckDuckGo давал только MSG 15-fc1xxx (7x35HS) — [pdf_10660033](https://kaas.hpcloud.hp.com/pdf-public/pdf_10660033_en-US-1.pdf). Модель всё равно отсеяна по CPU.
