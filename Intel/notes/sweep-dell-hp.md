# Добор: Dell и HP (Intel, 15–16", 1 ТБ, 32 ГБ двухканал)

_2026-09-30, облачная сессия. Цены — billiger.de (предложения магазинов + график за 6 мес.), dell.com/de, сниппеты поиска. «Из облака — перепроверить на idealo»._
_Раскладка памяти — HP QuickSpecs и Maintenance & Service Guide (MSG), Dell Owner's Manual, Icecat (данные производителя, не даташит)._
_Что уже есть в `candidates-lenovo-hp-dell.md`, не повторяю, если нет новых фактов._

## Вывод

1. **HP 15-fd1555ng — CU7G6EA#ABD — единственная новая находка у Dell/HP в бюджете.**
   Core Ultra 5 125H (Meteor Lake-H, Arc), **1×24 ГБ DDR5-5600 SO-DIMM + свободный второй слот**, 1 ТБ, 15,6" FHD IPS, 300 нит, 62,5 % sRGB. Цена **783,17 €**.
   С планкой 16 ГБ: **~1027 €** (Crucial CT16G56C46S5 — 243,90 € сейчас на billiger) или 943–1043 € при планке за 160–260 €.
   Получится 40 ГБ (24+16): двухканал на 32 ГБ. Это аналог Lenovo 83V70077GE, только на ~80 € дешевле, с экраном 15,6" и батареей 41 Втч.
   **HEVC — не проверено, есть риск** (см. таблицу HEVC). → проверено в браузере 30.09.2026: (п. 5.3) Сообщений по ProBook 4 G1iR, 250/250R G10, HP 15-fd1, Pavilion 16, OmniBook 5 16 и X Flip 16 нет; у free-codecs источников нет. Новое: потребительский HP OmniBook 7 Aero 13 (AMD) — DXVA без HEVC (форум HP, 04.07.2025) ([h30434.www3.hp.com](https://h30434.www3.hp.com/t5/Notebook-Video-Display-and-Touch/H265-HEVC-HW-encoder-and-decoder-not-available/td-p/9431209)).
2. **Dell: подходящих SKU нет.** Ни одного Intel + 1 ТБ + (2×16 / 16 + свободный слот / 32 распайкой) дешевле ~1500 €. Причины:
   - Dell Pro 15 Essential — **один слот, максимум 16 ГБ** (новый факт, по мануалу Dell);
   - Dell 16 DC16250/DC16251 — 16 ГБ бывает только как 2×8;
   - всё с 32 ГБ + 1 ТБ стоит от 1515 €;
   - dell.de сам дорогой: Dell 16 DC16250 с Core 5 120U, 2×8 ГБ и 512 ГБ — 1099,56 €.
3. **Бизнес-HP с отключённым HEVC, подтверждено по QuickSpecs (свежие версии):**
   - ProBook 4 G1i 16;
   - ProBook 460 G11;
   - **EliteBook 6 G1i 16** (v16, 23.09.2026);
   - **EliteBook 660 G11** (v25, 15.09.2026).

   **Новое:** у **ProBook 4 G2i 16** (Panther Lake, 2026) в QuickSpecs написано: «Hardware Acceleration HEVC (H.265) CODEC is an optional feature and must be configured at purchase». Значит, HEVC у него — платная опция при заказе. Есть ли она в розничных SKU, неизвестно.
4. **HP OmniBook 5 16 (16-af1xxx, 16-ba1xxx) и Pavilion 16 (16-af0xxx) — память распаяна** (LPDDR5/5X, MSG HP).
   SKU с 16 ГБ не годятся. Немецких SKU с 32 ГБ + 1 ТБ дешевле ~1860 € не нашёл.
5. **Ловушки HP по памяти:**
   - HP 15-fd1059ng, 15-fd1356ng, 15-fd0730ng, 15-fd0673ng — 2×8 ГБ DDR4 (Icecat);
   - у HP 15-fd2xxx (Core Ultra 225U/255U) 16 ГБ бывает только как 2×8 (MSG).

## HEVC по семействам (Dell/HP)

| Семейство | HEVC | Источник |
|---|---|---|
| HP ProBook 4 G1i 16 | **отключён** — «Hardware acceleration for CODEC H.265/HEVC … is disabled on this platform» | [QuickSpecs c09102587 v11, 23.04.2026](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09102587) |
| HP ProBook 460 G11 | **отключён** (та же фраза) | QuickSpecs c08915560 v11, 16.09.2025 — [копия PDF у Ars](https://cdn.arstechnica.net/wp-content/uploads/2025/11/ProBook-460-G11.pdf) |
| HP EliteBook 6 G1i 16 | **отключён** | [QuickSpecs c09100636 v16, 23.09.2026](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09100636) |
| HP EliteBook 660 G11 | **отключён** | [QuickSpecs c08915794 v25, 15.09.2026](https://www8.hp.com/h20195/V2/GetPDF.aspx/c08915794) |
| HP ProBook 4 G2i 16 (2026) | **опция при заказе** («optional feature and must be configured at purchase»); у розничных SKU — не проверено | [QuickSpecs c09231091 v11, 24.08.2026](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09231091) → проверено в браузере 30.09.2026: (п. 5.1) По открытым данным не узнать: QuickSpecs G2i — «optional feature and must be configured at purchase», номера опции нет; в даташите E04G3ET, на страницах HP и в PartSurfer про HEVC ни слова. Спросить HP или продавца либо проверить экземпляр (линейка и так отброшена) ([hp.com](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09231091)). |
| HP ProBook 4 G1iR 16 (Core 1xxU / i5-1334U) | в QuickSpecs фразы нет → не проверено | [QuickSpecs c09119776 v10](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09119776) → проверено в браузере 30.09.2026: (п. 5.3) см. строку 13 ([h30434.www3.hp.com](https://h30434.www3.hp.com/t5/Notebook-Video-Display-and-Touch/H265-HEVC-HW-encoder-and-decoder-not-available/td-p/9431209)). |
| HP 250 G10 / 250R G10 | в QuickSpecs фразы нет → не проверено. HP публично назвал отключённым «200 Series **G9**» ([Ars](https://arstechnica.com/gadgets/2025/11/hp-and-dell-disable-hevc-support-built-into-their-laptops-cpus/)) | [250 G10 c08479496 v9](https://www8.hp.com/h20195/V2/GetPDF.aspx/c08479496), [250R G10 c09053764 v8](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09053764) → проверено в браузере 30.09.2026: (п. 5.3) см. строку 13 ([h30434.www3.hp.com](https://h30434.www3.hp.com/t5/Notebook-Video-Display-and-Touch/H265-HEVC-HW-encoder-and-decoder-not-available/td-p/9431209)). |
| HP 15-fd1xxx (потребительский) | в MSG оговорки нет («HD decode, DX12, and HDMI»). free-codecs.com (02.01.2026) пишет, что затронуты «HP Pavilion and HP 15 budget consumer lines», но **без источников** → **не проверено, риск** | [MSG P80783-001](https://kaas.hpcloud.hp.com/pdf-public/pdf_12998862_en-US-1.pdf), [free-codecs](https://www.free-codecs.com/news/hp-and-dell-quietly-remove-hevc-support.htm) → проверено в браузере 30.09.2026: (п. 5.3) см. строку 13 ([h30434.www3.hp.com](https://h30434.www3.hp.com/t5/Notebook-Video-Display-and-Touch/H265-HEVC-HW-encoder-and-decoder-not-available/td-p/9431209)). |
| HP OmniBook 5 16 / Pavilion 16 | не проверено (к тому же память распаяна) | [MSG OmniBook 5 16 / Pavilion 16](https://kaas.hpcloud.hp.com/pdf-public/pdf_10220266_en-US-1.pdf) → проверено в браузере 30.09.2026: (п. 5.3) см. строку 13 ([h30434.www3.hp.com](https://h30434.www3.hp.com/t5/Notebook-Video-Display-and-Touch/H265-HEVC-HW-encoder-and-decoder-not-available/td-p/9431209)). |
| Dell (Dell 16, Dell Pro, Dell Pro Essential, Latitude, Inspiron) | **риск.** Dell: HEVC есть на конфигурациях с дискреткой, 4K-экраном, Dolby Vision или CyberLink; остальные «may not include the required HEVC codec components». Списка моделей нет. Dell 16 Plus 2-in-1 — аппаратный HEVC отключён (Ars) | [Dell KB 000222670, изм. 11.09.2026](https://www.dell.com/support/kbdoc/en-bs/000222670/how-to-identify-if-you-cannot-view-4k-video-content-due-to-a-hevc-codec), [Ars](https://arstechnica.com/gadgets/2025/11/hp-and-dell-disable-hevc-support-built-into-their-laptops-cpus/) |

Как отключают: по разбору devinthreethousand (21.11.2025), HEVC блокируют в ACPI-таблицах прошивки (UEFI/BIOS).
Под Linux тот же ноутбук декодирует — [substack](https://devinthreethousand.substack.com/p/hevc-hardware-support-being-removed). Для Windows это значит, что декодер не видят все программы, включая монтажные (моё заключение, не проверено тестом).
Проверка — DXVA Checker на витринном образце или в первые 14 дней после покупки (право на возврат).

---

## Кандидат

### HP 15-fd1555ng — CU7G6EA#ABD («24 ГБ + свободный слот»)
- **Проверка.** Даташит ✅: [HP MSG 15-fd1xxx, P80783-001, 09/2025](https://kaas.hpcloud.hp.com/pdf-public/pdf_12998862_en-US-1.pdf) — серия. SKU ✅: Icecat, код CU7G6EA, [по EAN 0199764524645](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&GTIN=0199764524645). Цена ✅: billiger.
- **CPU:** Core Ultra 5 125H — 14 ядер (4P+8E+2LPE), 28 Вт. Meteor Lake-H (Core Ultra Series 1) — не ребренд. iGPU Arc включается только при двухканале.
- **ОЗУ:** 24 ГБ = **1×24 ГБ DDR5-5600 SO-DIMM** (Icecat: «Speicherlayout 1 x 24 GB»; billiger: «Anzahl Arbeitsspeichermodule 1»).
  - MSG: «DDR5-5600, dual channel support (Ultra processors)», в списке конфигураций есть «24 GB (1 × 24 GB)» и «32 GB (2 × 16 GB)». Значит, слотов два, и в этом SKU **один свободен**.
  - HP пишет «Supports up to 32 GB». 24+16 = 40 ГБ — **вне списка HP** (сам Meteor Lake-H поддерживает больше; не проверено).
  - Вариант строго в рамках HP — комплект 2×16 (Crucial CT2K16G56C46S5, 479,99 € — [billiger](https://www.billiger.de/products/4312168486-crucial-ddr5-5600-32gb-kit-2x16gb-so-dimm-cl46-ct2k16g56c46s5)). Итог ~1263 € — выше потолка.
- **SSD:** 1 ТБ M.2 2280 PCIe NVMe. Слот M.2 один (MSG: только «Primary storage»).
- **Экран:** 15,6", 1920×1080, IPS, антиблик, **300 нит, 62,5 % sRGB**, 60 Гц, без сенсора (Icecat).
  В MSG панель «62.5% sRGB, 300 nits» указана как сенсорная (TOP) — точную матрицу SKU не проверял.
- **Порты (MSG + Icecat):**
  - 1× USB-C 10 Гбит/с (PD, **DP 1.4b до 4K/60**);
  - 2× USB-A 5 Гбит/с;
  - **HDMI 1.4b — только 1080p/60**;
  - Thunderbolt, RJ45, SD-ридера — нет;
  - Wi-Fi 6.
- **Батарея и вес:** 41 Втч; 1,59 кг (Icecat). Клавиатура с цифровым блоком; подсветка у этого SKU — не проверено. → проверено в браузере 30.09.2026: (п. 4.12) HP 15-fd1555ng: второго M.2 нет и подсветки нет (PartSurfer CU7G6EA — один SSD, клавиатура P26463-041 без подсветки; в сервис-мануале только «Primary storage») ([partsurfer.hp.com](https://partsurfer.hp.com/?searchtext=CU7G6EA)).
- **ОС:** Windows 11 Home. Гарантия производителя 1 год (1/1/0), плюс 2 года гарантии продавца по закону (Gewährleistung).
- **Цена:** **783,17 €** (TECHNIKdirekt), далее JACOB 785,03, Heinzsoft 814,00, Kaufland 821,08, Galaxus 847,83; всего 15 предложений.
  За 6 мес. (02.04–30.09.2026): мин. **737,21 €** (23.08), макс. 799 €. [billiger.de](https://www.billiger.de/products/5549038366-hp-15-fd1555ng-intel-core-ultra-5-125h-24-gb-ram-1-tb-ssd-win11-home-natural-silver), 30.09.2026.
  Сниппет geizhals: «ab € 799,00 (2026)» — [geizhals](https://geizhals.de/hp-laptop-15-fd1555ng-cu7g6ea-abd-a3716076.html). «Из облака — перепроверить на idealo».
- **Итог с планкой 16 ГБ:** 783,17 + 243,90 (Crucial CT16G56C46S5, [billiger](https://www.billiger.de/products/4309462977-crucial-ddr5-5600-16gb-modul-1x16gb-so-dimm-cl46-ct16g56c46s5)) = **1027,07 €**.
  Планка 24 ГБ (48 ГБ симметрично): CT24G56C46S5 — 364 € ([billiger](https://www.billiger.de/pricelist/4518013529-crucial-ddr5-5600-24gb-modul-1x24gb-so-dimm-cl46-ct24g56c46s5)); итог 1147 € — выше потолка.
- **HEVC:** **не проверено.** В MSG оговорки нет, но есть неподтверждённое сообщение про «HP 15». Перед покупкой проверить в DXVA Checker или покупать там, где легко вернуть. → проверено в браузере 30.09.2026: (п. 5.3) см. строку 13 ([h30434.www3.hp.com](https://h30434.www3.hp.com/t5/Notebook-Video-Display-and-Touch/H265-HEVC-HW-encoder-and-decoder-not-available/td-p/9431209)).
- **Минусы:**
  - экран 62,5 % sRGB — для цветокоррекции нужен внешний монитор (через USB-C, 4K/60);
  - батарея 41 Втч;
  - HDMI 1.4b;
  - корпус бюджетный пластиковый;
  - HP сам не заявляет, что ОЗУ меняет пользователь (для потребительских моделей в MSG есть процедура замены).

---

## Почти подходит / наблюдать

### HP ProBook 4 G1i 16 — C7SR2ES (новый факт: цена опускалась ниже 1100 €) — HEVC ОТКЛЮЧЁН
- Уже есть в `candidates-lenovo-hp-dell.md`. Новое — история цены: за 6 мес. минимум **1060,32 € (09.09.2026)**, сейчас **1199,00 €** (notebooksbilliger), Galaxus 1207,99; 7 предложений — [billiger](https://www.billiger.de/products/5406906475-hp-probook-4-g1i-16-intel-core-ultra-5-225h-32-gb-ram-1-tb-ssd-c7sr2es).
- Core Ultra 5 225H (Arrow Lake-H). 32 ГБ по QuickSpecs бывает только как 2×16 (для SKU не подтверждено). 1 ТБ, 48 Втч (billiger). → проверено в браузере 30.09.2026: (п. 4.15) ProBook 4 G1i 16 C7SR2ES: 2×16 (PartSurfer, geizhals), один SSD 1 ТБ 2280; экран 300 нит, 62,5 % sRGB (geizhals); клавиатура DE с подсветкой; гарантия 1 год ([partsurfer.hp.com](https://partsurfer.hp.com/?searchtext=C7SR2ES)).
- **HEVC отключён** ([QuickSpecs c09102587](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09102587)) → для монтажа не рекомендую, даже по 1060 €.

### HP 15-fd0068ng — D46JPEA#ABD (дёшево, но слот и HEVC не проверены)
- Core 5 120U — Raptor Lake-U refresh (2P+8E), **ловушка по поколению**. iGPU Intel Graphics; декод HEVC 4:2:2 10 бит есть у любого Intel 11+ (см. intel-cpu.md).
- ОЗУ: **1×16 ГБ DDR5-5200 SO-DIMM** (Icecat [по EAN 0199896683265](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&GTIN=0199896683265); billiger: «1 модуль»).
  **Есть ли второй слот — не проверено.** Icecat и billiger пишут «max 16 GB». В MSG 15-fd0xxx (N33165-001, 03/2023, [PDF](https://kaas.hpcloud.hp.com/pdf-public/pdf_7525191_en-US-1.pdf)) версии с Core 5 120U и DDR5 нет вовсе. → проверено в браузере 30.09.2026: (п. 4.13) HP 15-fd0068ng D46JPEA: слот, скорее всего, один (geizhals «1 Slot gesamt», Icecat «max 16 GB»); платы нет в сервис-мануалах; официально не подтверждено. Из кандидатов убрать ([geizhals.de](https://geizhals.de/hp-laptop-15-fd0068ng-d46jpea-abd-a3755767.html)).
- Экран 15,6" FHD, **250 нит**, 62,5 % sRGB; 1 ТБ; FreeDOS.
- Цена **570,68 €** (JACOB), Galaxus 592,96; 6 мес.: 519–749 € — [billiger](https://www.billiger.de/products/5586702164-hp-15-fd0068ng-intel-core-5-120u-16-gb-ram-1-tb-ssd-freedos-natural-silver).
  Если второй слот есть: **+243,90 € = ~815 €**.
- Вывод: слабый CPU и тусклый экран. Брать только если нужен минимум денег и продавец подтвердит второй слот DDR5.

---

## Отброшено — Dell

| SKU / модель | Что не так | Источник |
|---|---|---|
| **Dell Pro 15 Essential PV15250, i7-1355U, 16 ГБ, 1 ТБ — GYXJD** (EAN 5397184978221), 833,24 € (6 мес. мин. 616,50 €) | **1 слот SO-DIMM, максимум 16 ГБ** (мануал Dell: «Maximum 16 GB», модули 8 или 16 ГБ). Icecat: «1 x 16 GB». Двухканал с 32 ГБ невозможен. Экран 250 нит, 45 % NTSC, HDMI 1.4 | [Dell manual PV15250 — Memory](https://www.dell.com/support/manuals/en-tt/dell-pro-pv15250-laptop/dell-pro-essential-15-pv15250-laptop-om/memory?guid=guid-c921bbbc-3ad1-44dc-a91c-799f02c95f51), [Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&GTIN=5397184978221), [billiger](https://www.billiger.de/products/5406536869-dell-pro-15-essential-pv15250-15-6-intel-core-i7-1355u-16-gb-ram-1-tb-ssd-win11-pro-schwarz) |
| Dell Pro 15 Essential PV15250 i5-1334U 16/1 ТБ — 748,09 € (1 предложение) | то же: 1 слот, максимум 16 ГБ | [billiger](https://www.billiger.de/pricelist/5538563812-dell-pro-15-essential-pv15250-15-6-intel-core-i5-1334u-16-gb-ram-1-tb-ssd-win11-home-schwarz) |
| Dell 16 DC16250 (Core 5 120U / Core 7 150U) | 2 SO-DIMM, но 16 ГБ **только 2×8** (24 = 16+8, 32 = 2×16). 16/1 ТБ — от 1144,67 € (Kaufland). На dell.de: Core 5 120U, 2×8, 512 ГБ — 1099,56 € | мануал DC16250 — по сниппету поиска ([Dell](https://www.dell.com/support/manuals/en-uk/dell-dc16250-laptop/dell_16_dc16250_owners_manual/memory?guid=guid-e9d2ea83-38a4-431d-803c-96d63c1dbc34&lang=en-us)), [dell.de](https://www.dell.com/de-de/shop/laptops/spd/dell16laptopdc16250) |
| Dell 16 DC16251 | те же конфигурации памяти (2×8 / 16+8 / 2×16), максимум 32 ГБ. 32/1 ТБ Core 7 — 1515,61 € (Kaufland); dell.de — от 1510,11 € | [Dell manual DC16251](https://www.dell.com/support/manuals/en-ie/dell-dc16251-laptop/dell_16_dc16251_owners_manual/memory?guid=guid-e9d2ea83-38a4-431d-803c-96d63c1dbc34&lang=en-us), [dell.de](https://www.dell.com/de-de/shop/laptops/scr/laptops) |
| Dell 16 Plus DB16250 | Lunar Lake, LPDDR5x на корпусе CPU (16 или 32 ГБ, распайка). 32/1 ТБ Ultra 7 258V — 2653,99 € (Techinn); dell.de — от 2244,34 € | [Dell manual DB16250](https://www.dell.com/support/manuals/en-us/dell-db16250-laptop/dell-16-plus-db16250_om/memory?guid=guid-05867936-5f4f-49a0-aba0-bdb592fd6959&lang=en-us) |
| Dell Pro 16 PC16250 (Ultra 5 225U/235U, Ultra 7 255U/265U) | 2 SO-DIMM, 1×16 бывает, максимум 64 ГБ. Но с 1 ТБ в продаже только 32 ГБ за 2175,99 € и дороже (Kaufland). Дешевле всего 16/512 — 860,72 €, 512 ГБ не проходят. dell.de — от 1770,72 € | [Dell manual PC16250](https://www.dell.com/support/manuals/en-us/dell-pro-pc16250-laptop/dell-pro-16-pc16250-owners-manual/memory?guid=guid-a016b804-d53e-4db1-9941-cd813093e800&lang=en-us), [billiger поиск](https://www.billiger.de/search?searchstring=Dell+Pro+16+PC16250+1+TB) |
| Dell Pro 16 Plus PB16250 | 32/1 ТБ Ultra 7 — от 2932,99 € (Kaufland). T17XR (32/512, 1048,50 €) — уже в candidates, 512 ГБ | billiger |
| Dell Pro 16 Essential PV16250 | на billiger нет ни одного SKU с 1 ТБ (есть только Pro 14/15 Essential) | [billiger](https://www.billiger.de/search?searchstring=PV16250) |
| Dell 15 DC15250 | с 1 ТБ не продаётся. i7-1355U 16/512 — 829 €, i5-1334U 16/512 — 549 € | [billiger](https://www.billiger.de/search?searchstring=DC15250) |
| Dell Inspiron 3530 **WCDJC** (i7-1355U, 16 ГБ, 1 ТБ) — 949 € (OTTO) | 2×8 DDR4 (Icecat); экран 250 нит, 45 % | [Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=DELL&ProductCode=WCDJC) |
| Latitude 3550 / 5550 / 3560 / 5560, Vostro 16 | новых SKU с 1 ТБ в продаже нет. 3550 — только 8/512 (Saturn, 899 €) и 16/512 (OTTO, 1099 €). Предложения «Laptop Dell Latitude 5550 … 32 GB 1 TB» за 1119 € на Kaufland — у продавца, торгующего восстановленными Latitude, статус «новый» не подтверждён. 3560/5560 в продаже не нашёл | billiger |

## Отброшено — HP

| SKU / модель | Что не так | Источник |
|---|---|---|
| ProBook 4 G1i 16 **D74TZES** (Ultra 5 225U, 24 ГБ, 1 ТБ, FreeDOS) — 999 € (NBB) | **HEVC отключён**; раскладка 24 ГБ (1×24 или 2×12) не проверена. Даже при 1×24 с планкой — ~1240 € | [billiger](https://www.billiger.de/pricelist/5953673057-hp-probook-4-g1i-16-intel-core-ultra-5-225u-24-gb-ram-1-tb-ssd-freedos-d74tzes) |
| ProBook 4 G1i 16 **D74TYES** (225H, 24/1 ТБ) и **D74V6ES** (255H, 24/1 ТБ) — по 1099 € | HEVC отключён; раскладка не проверена; с планкой выше 1300 € | [billiger D74V6ES](https://www.billiger.de/pricelist/5825538254-hp-probook-4-g1i-16-intel-core-ultra-7-255h-24-gb-ram-1-tb-ssd-d74v6es) |
| ProBook 4 G1i 16 **C7SR8ES** (255H, 16/1 ТБ) — 1129 € | HEVC отключён; с планкой выше 1300 € | [billiger](https://www.billiger.de/products/5406906492-hp-probook-4-g1i-16-intel-core-ultra-7-255h-16-gb-ram-1-tb-ssd-c7sr8es) |
| «ProBook 4 G1i 16 CB4M4EA» (billiger) | по Icecat это **14"**, 2×8 — ошибка в названии карточки | [Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=HP&ProductCode=CB4M4EA) |
| ProBook 460 G11 **B2MK5ES** (Ultra 5 125U, 16/1 ТБ) — 999,01 € (6 мес. мин. 789,19 €) | 1×16 (Icecat) + свободный слот, но **HEVC отключён**; с планкой ~1243 € | [billiger](https://www.billiger.de/pricelist/5165737379-hp-probook-460-g11-intel-core-ultra-5-125u-16-gb-ram-1-tb-ssd-win11-pro-b2mk5es) |
| ProBook 460 G11 B2MK4ES (155H, 32/1 ТБ) — 1319 €; «D05D3ES#ABD 89378/89383» — сборки магазина | HEVC отключён; дорого или «aufgerüstet» | billiger |
| EliteBook 6 G1i 16 (32/1 ТБ) — 1995–2099 € | HEVC отключён (QuickSpecs v16); дорого; 32 ГБ бывает и 1×32 | [QuickSpecs](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09100636) |
| EliteBook 660 G11 | HEVC отключён (QuickSpecs v25); с 1 ТБ не продаётся (есть 8/256, 16/512 за ~1030–1040 €) | [QuickSpecs](https://www8.hp.com/h20195/V2/GetPDF.aspx/c08915794) |
| ProBook 4 G2i 16 / EliteBook 6 G2i 16 с «Intel Core 5 320 / Core 7 350» | Core 5/7 3xx без «Ultra» — **Wildcat Lake, один канал памяти** (ловушка, intel-cpu.md). Дорого: ProBook 4 G2i 16 E04G3ET 32/1 ТБ — 1955 €, EliteBook 6 G2i 16 E02DGET — 1436,27 € | billiger |
| HP OmniBook 5 16-af1655ng (C53MFEA, Ultra 5 225U, 16/1 ТБ, OLED) — 869 € | **16 ГБ LPDDR5x распаяно** (Icecat + MSG) | [MSG](https://kaas.hpcloud.hp.com/pdf-public/pdf_10220266_en-US-1.pdf) |
| HP Pavilion 16-af0652ng (B04YHEA, Ultra 5 125U, 16/1 ТБ, OLED 2K 120 Гц) — 939 € | 16 ГБ LPDDR5x распаяно | [MSG](https://kaas.hpcloud.hp.com/pdf-public/pdf_10220266_en-US-1.pdf), Icecat |
| HP OmniBook 5 16 с 32 ГБ (16-af1004nc, чешский SKU) | распайка; 1862,57 € | billiger |
| HP OmniBook 7 16 (Intel) | Intel-версий 16" на billiger нет. Есть OmniBook 7 **17** (17,3" — вне диапазона экрана) | billiger |
| HP OmniBook X Flip 16-as0177ng / as0373ngx (258V, 32/1 ТБ распайка) — 1399 € | B-список, но выше 1200 € | [billiger](https://www.billiger.de/products/5308050354-hp-omnibook-x-flip-16-as0177ng-intel-core-ultra-7-258v-32-gb-ram-1-tb-ssd) |
| HP Envy x360 16-ac0655ng (125U, 16/1 ТБ) — 1049 €; Envy 16-h1375ng — 1499 € (Kaufland) | распайка 16 ГБ / дорого | billiger |
| HP 15-fd1059ng (**C6RF2EA**), 15-fd1356ng (**C8JE1EA**) — Core 5 120U, 16/1 ТБ | **2×8 DDR4** (Icecat) | Icecat по EAN 0199642082335 / 0199642395015 |
| HP 15-fd0730ng (**BU9R3EA**, i5-1334U), 15-fd0673ng (**C94P4EA**, i7-1355U) — 16/1 ТБ, 667–790 € | **2×8 DDR4** (Icecat); у 15-fd0xxx с 13xxU максимум 16 ГБ (MSG N33165) | Icecat, [MSG](https://kaas.hpcloud.hp.com/pdf-public/pdf_7525191_en-US-1.pdf) |
| HP 15-fd2xxx (Ultra 5 225U / 7 255U) | 16 ГБ DDR5 только 2×8 (MSG); с 1 ТБ в продаже нет | [MSG](https://kaas.hpcloud.hp.com/pdf-public/pdf_11954528_en-US-1.pdf) |
| HP 250R G10 (Core 5 120U, 8/1 ТБ) — 629 € | 1×8. До 2×16 нужен комплект 2×16 (~480 €). HP: слоты «customer non-accessible». Предложения на Kaufland с 32–128 ГБ — сборки магазина. Ловушка по CPU | [QuickSpecs](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09053764), [billiger](https://www.billiger.de/pricelist/5859885897-hp-250r-g10-15-6-intel-core-5-120u-8-gb-ram-1-tb-ssd-win-11-pro-grau) |
| HP 250 G10 (i7-1355U) «32 GB DDR4 1 TB» — 1039,90 € (Amazon/Kaufland) | сборки магазина, не заводская конфигурация; DDR4; Raptor Lake-U | billiger |
| HP 255 G10/G11 | только AMD | — |
| HP 17 / OmniBook 3 17 / OmniBook 7 17 | 17,3" — вне диапазона | — |

## Как искал

- billiger.de: поиск по семействам и кодам моделей (DC15250, DC16250, DB16250, PV15250, PV16250, PC16250, PB16250, Latitude 3550/5550, Vostro 16, Inspiron 16, HP 15-fd0/1/2, OmniBook 3/5/7 16, Pavilion 16, ProBook 460 G11 / 4 G1i / 4 G1iR / 4 G2i 16, EliteBook 660 G11 / 6 G1i / 6 G2i 16, HP 250/250R G10, Envy 16), фильтр «Notebooks», сортировка по цене. Страницы товаров — EAN, предложения, график за 6 мес.
- Раскладка: Icecat по EAN или коду; HP MSG (kaas.hpcloud.hp.com); HP QuickSpecs (www8.hp.com/h20195); Dell Owner's Manual (dell.com/support/manuals — через WebFetch, прямой curl получает 403).
- Недоступно из облака: support.hp.com и hp.com/us-en (сброс соединения / 503), форум HP (403). В HP Store DE нет ни CU7G6EA, ни D46JPEA.
