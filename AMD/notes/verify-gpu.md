## Проверка gpu (AMD + RTX)

_30.09.2026, локальная сессия, скептическая проверка [`candidates-gpu.md`](candidates-gpu.md). Цены и история — idealo.de в Chrome пользователя (своя вкладка, капчи не было). Память — gigabyte.com (спецификация серии GA63H) + Icecat open по GTIN + карточка Alternate. Обзоры — 3DNews, LaptopMedia, Notebookcheck (сборник)._
_Правило цены — новое (корневой [`CLAUDE.md`](../../CLAUDE.md), 30.09.2026): минимальная цена нового товара с доставкой у любого продавца, маркетплейсы включительно; б/у и цены с купоном не считаются._

### Вывод

1. **Gigabyte GAMING A16 `3VHK3DE894SH` — подтверждён, список «наблюдать» (> 1100 €).** Раскладка 1×16 DDR5 + свободный второй SO-DIMM подтверждена четырьмя источниками (gigabyte.com — 2 слота; Icecat и Alternate — «1 x 16 GB», «belegt 1»; обзор LaptopMedia — «second slot free»). CPU Ryzen 7 260 — Hawk Point, 8 × Zen 4, не урезан. RTX 5060 закрывает 4:2:2.
2. **Итог сейчас — 1286,56 €** (1099 € + планка Kingston 187,56 € на маркетплейсе Galaxus; с Crucial у обычного магазина — 1347,89 €). В бюджет 1100 € — только если ноутбук упадёт до **≤ 912 €**; такого за год не было (минимум 999 €, 28.10–31.12.2025; с января — не ниже 1079 €).
3. **Исправлено:** планка Crucial стоит 248,89 € с доставкой, а не 243,90; пороги пересчитаны по новому правилу цены (Kingston на маркетплейсе теперь считается); USB-C — это USB4 (Icecat/Alternate ошибаются); TGP RTX 5060 — 75 Вт (NBC), GPU урезан по мощности; 03–05.09.2026 цена была 1079 €.
4. **Экран слабый для цвета:** 60 % sRGB (3DNews), 52 % sRGB (LaptopMedia) — для цветокоррекции 4K нужен внешний монитор (есть USB4 с DP 1.4 и HDMI 2.1).
5. **Отброшенные — выборочно проверены 3 «обидных» (C2VM8EA, ANV16-42-R38V, 15-fb3051ng): у всех на idealo сейчас только б/у** («Für dieses Produkt sind zur Zeit nur Gebraucht-Angebote verfügbar»). Отброшены верно. Две причины в `candidates-gpu.md` («только маркетплейс» у 15-fb3357ng и 16-xd0674ng) по новому правилу не причина, но оба и так выше 1100 € с докупкой.
6. **Основной список, B-список и условный вариант «2×16 + 512 ГБ + SSD»: пусто** — подтверждаю вывод поиска.

### Сводная таблица (idealo, 30.09.2026)

| P/N | CPU (кодовое имя) | GPU | Память (источник) | SSD / M.2 | Цена сейчас · продавец | Мин. 1 год | Итог с планкой | Вердикт |
|---|---|---|---|---|---|---|---|---|
| Gigabyte GAMING A16 `3VHK3DE894SH` | Ryzen 7 260 (Hawk Point, 8 × Zen 4, 780M) — [amd.com](https://www.amd.com/en/products/processors/laptop/ryzen/200-series/amd-ryzen-7-260.html) | RTX 5060 8 ГБ, 75 Вт, MUX | **1×16 + свободный SO-DIMM** ✅ — [gigabyte.com](https://www.gigabyte.com/de/Laptop/GIGABYTE-GAMING-A16-GA63H/sp), [Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&GTIN=4719331766764), [Alternate](https://www.alternate.de/GIGABYTE/GAMING-A16-3VHK3DE894SH-Gaming-Notebook/html/product/100151262) | 1 ТБ Gen4 + свободный M.2 Gen4 x2 | **1099,00 €** coolblue.de (30 дней), также MediaMarkt, computeruniverse, Cyberport — [карточка](https://www.idealo.de/preisvergleich/OffersOfProduct/207329496_-gaming-a16-3vhk3de894sh-gigabyte.html) | 999 € (28.10.2025) | **1286,56 €** (Kingston, Galaxus МП) / 1347,89 € (Crucial, alza.de) | **подтверждено → наблюдать**: в бюджет при ≤ 912 € |

### Gigabyte GAMING A16 3VH — `3VHK3DE894SH` (GTIN 4719331766764)

**Вердикт: подтверждено (память, CPU, цена), список «наблюдать» (watch-over-1100) остаётся; исправлены итог с планкой, пороги, порты, TGP.**

- **Память — подтверждено (1×16 + свободный слот):**
  - gigabyte.com, колонка 3VH: «Up to 64GB DDR5 5600MHz», «2x SO-DIMM sockets for expansion», «1x PCIe Gen4x4 M.2 slot, 1x PCIe Gen4x2 M.2 slot», MUX Switch — [gigabyte.com GA63H/sp](https://www.gigabyte.com/de/Laptop/GIGABYTE-GAMING-A16-GA63H/sp). Раскладки конкретного SKU на сайте нет.
  - Icecat по GTIN: «Speicherlayout 1 x 16 GB», DDR5-5200, «2x SO-DIMM», max 64 ГБ, «Anzahl SSD installiert 1» — [Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&GTIN=4719331766764).
  - Alternate (карточка этого P/N): «2 Speicherbänke vorhanden, davon belegt 1 Speicherbank», DDR5-5600 — [alternate.de](https://www.alternate.de/GIGABYTE/GAMING-A16-3VHK3DE894SH-Gaming-Notebook/html/product/100151262).
  - Обзоры: LaptopMedia (GA63H) — «one of the slots is populated with a 16GB Crucial DDR5-5600 module, leaving the second slot free» — [LaptopMedia](https://laptopmedia.com/review/gigabyte-gaming-a16-ga63h-amd-review-stealthy-sleeper-with-record-battery-life/); 3DNews (3VH): 16 ГБ, советуют «ещё одну планку DDR5-5600 на 16 ГБ» — [3DNews](https://3dnews.ru/1132160/obzor-gigabyte-gaming-a16-3vh).
  - Частота: Icecat — 5200, gigabyte.com/Alternate/NBC — 5600. Не критично.
- **SSD:** 1 ТБ PCIe 4.0 (Icecat, Alternate); второй M.2 — Gen4 **x2** (gigabyte.com; LaptopMedia: «Second M.2 slot is limited to slower PCIe 4.0 x2»).
- **CPU — подтверждено:** Ryzen 7 260 — «Former Codename Hawk Point», Zen 4, 8 ядер/16 потоков, Radeon 780M, USB4 ×2 native — [amd.com](https://www.amd.com/en/products/processors/laptop/ryzen/200-series/amd-ryzen-7-260.html). Не урезан (= 8845HS, [`amd-cpu.md`](amd-cpu.md)). Для 4K — ок: CPU на уровне Core Ultra 7 155H, декодирование 4:2:2 — через RTX 5060.
- **Порты — исправлено:** USB-C — **USB4** (DP 1.4, PD 3.0) по gigabyte.com и 3DNews («полноценный разъём USB4»); Icecat и Alternate («USB-C 3.2 Gen 1, 5 Gbit/s») ошибаются. AMD: у Ryzen 7 260 два нативных USB4.
- **GPU:** RTX 5060 8 ГБ GDDR7, MUX. TGP: NBC — «75 W TDP» ([NBC 3VH](https://www.notebookcheck.net/Gigabyte-Gaming-A16-3VH.1188434.0.html)); 3DNews намерил 67–84 Вт на GPU в играх. Это **пониженный** TGP (у LOQ 15AHP10/11 и Legion 5 15AHP10 — 100–115 Вт по PSREF, см. [`candidates-gpu.md`](candidates-gpu.md)) — для NVDEC/NVENC не важно, для эффектов в Resolve — минус.
- **HEVC — риск низкий:** Gigabyte в списках отключений нет ([`hevc-amd.md`](hevc-amd.md)); RTX 5060 (Blackwell) декодирует H.264/HEVC 4:2:2 ([NVIDIA NVDEC](https://docs.nvidia.com/video-technologies/video-codec-sdk/13.0/nvdec-video-decoder-api-prog-guide/index.html)). Проверить DXVA Checker'ом в окно возврата.
- **Зарядка:** 150 Вт в комплекте (gigabyte.com; Icecat «AC-Netzadapter: Ja»; Alternate «150 Watt Netzteil»). Гарантия 2 года (Icecat).
- **Цена — idealo, 30.09.2026** ([карточка этого P/N](https://www.idealo.de/preisvergleich/OffersOfProduct/207329496_-gaming-a16-3vhk3de894sh-gigabyte.html)):

| Магазин | Цена с доставкой | Возврат | Доставка | Тип |
|---|---|---|---|---|
| coolblue.de | **1099,00 €** | 30 дней | до 01.10 | магазин |
| mediamarkt.de | 1099,00 € | 30 дней | до 01.10 | магазин |
| computeruniverse.net | 1099,00 € | 30 дней | до 05.10 | магазин |
| cyberport.de | 1099,00 € | 30 дней | до 05.10 | магазин |
| alternate.de | 1106,99 € | 14 дней | до 02.10 | магазин |
| eBay | 1099,00 € | 30 дней | — | МП, цена с купоном — не считается (и не дешевле) |
| otto.de | 1121,70 € | 30 дней | — | магазин |

- **История 1 год (API `/price-chart/…/207329496/history?period=1Y`):** мин. **999 €** (28.10–27.12.2025, ещё 29 и 31.12); с января — 1099–1545 €; 12.06–09.08.2026 — 1199 €; 10–25.08 — 1149; 26.08–05.09 — 1079–1099 (**1079 € 03–05.09.2026**); с 06.09 — 1099 €. ≤ 1100 € — 35 из последних 182 дней (подтверждено). ≤ 1062 € — последний раз 31.12.2025. ≤ 912 € — ни разу. Средняя за год — 1188,12 €. (Позже, ~14:00, API отвечал 404 на все товары — см. `idealo-howto.md`.)
- **Итог с планкой (idealo, 30.09.2026; правило: минимум у любого продавца, маркетплейс включительно):**
  - Kingston `KVR56S46BS8-16` — **187,56 €** с доставкой (одно предложение, Galaxus — маркетплейс, возврат 30 дней) — [карточка](https://www.idealo.de/preisvergleich/OffersOfProduct/213624753_-valueram-16gb-ddr5-5600mhz-cl46-so-dimm-on-die-ecc-kvr56s46bs8-16-kingston.html) → **1099 + 187,56 = 1286,56 €**.
  - Запасной вариант — Crucial `CT16G56C46S5`: 248,89 € с доставкой (alza.de, 30 дней; «ab 243,90» — без доставки) — [карточка](https://www.idealo.de/preisvergleich/OffersOfProduct/202284828_-16gb-ddr5-5600-cl46-ct16g56c46s5-crucial.html) → 1347,89 €. В категории SO-DIMM DDR5 16 ГБ дешевле Kingston нет (первая — Lenovo 4X71M23186, 199,90 €) — [категория](https://www.idealo.de/preisvergleich/ProductCategory/4552F102189756-102193939-102286859-107683716.html?sortKey=minPrice).
  - SSD и зарядку докупать не нужно (1 ТБ и 150 Вт в комплекте).
  - Пороги: в бюджет 1100 € — ноутбук ≤ **912 €** (с Crucial ≤ 851 €); в окно ≤ 1250 € — ≤ **1062 €** (с Crucial ≤ 1001 €). За год ≤ 912 € не было ни разу; ≤ 1062 € — только 28.10–31.12.2025 (999 €).
- **Известные проблемы (обзоры этой платформы GA63H):**
  - Экран WUXGA BOE NE160WUM-NX6: **60 % sRGB, 43 % DCI-P3**, 330 нит, контраст 1603:1, ΔE 4,74 (макс. 23,7) — [3DNews](https://3dnews.ru/1132160/obzor-gigabyte-gaming-a16-3vh); LaptopMedia — «very poor color coverage (52% sRGB)», без ШИМ. Для цветокоррекции 4K — только внешний монитор.
  - Шум под нагрузкой 47–50 дБА (3DNews); CPU до 90–94 °C (3DNews, LaptopMedia) — без сброса частот.
  - GPU урезан по мощности («Severely power-limited GPU» — LaptopMedia, тест с RTX 5070).
  - Плюсы: 2× SO-DIMM + 2× M.2, USB4, ~8 ч батареи (LaptopMedia), корпус без «геймерского» дизайна.
  - Intel-сестра GA6H у NBC: «засветка по краям», громкая — [NBC](https://www.notebookcheck.net/An-affordable-RTX-5070-laptop-Gigabyte-Gaming-A16-review.1072350.0.html). Собственного обзора NBC у AMD-версии нет (только сборник [GA63H](https://www.notebookcheck.net/Gigabyte-Gaming-A16-GA63H.1100671.0.html)).
- **Опровергнуто / поправлено в `candidates-gpu.md`:**
  - «Планка 243,90 €» — это цена без доставки; с доставкой 248,89 €. По новому правилу цены берём Kingston 187,56 € (Galaxus МП) → основной итог **1286,56 €** (у поиска — 1342,90 € основным).
  - Пороги «≤ 1006 € / ≤ 856 €» → **≤ 1062 € / ≤ 912 €** (с Kingston); с Crucial — ≤ 1001 € / ≤ 851 €.
  - Пропущено: 1079 € 03–05.09.2026 (минимум с января). TGP RTX 5060 — 75 Вт по NBC, а не «не указан».
  - Разночтение USB4 / USB 3.2 решено: USB4 (производитель + обзор 3DNews; у Ryzen 7 260 два нативных USB4 по amd.com).
  - Подтверждено без изменений: 1099 € у четырёх магазинов с возвратом 30 дней; минимум года 999 € (28.10.2025); 35 дней ≤ 1100 € из последних 182; средняя 1188 €.

### Отброшенные — выборочная проверка (3 самых «обидных»)

| P/N | Почему «обидно» | Проверка 30.09.2026 | Вердикт |
|---|---|---|---|
| HP Omen 16-ap `C2VM8EA` (R9 8940HX, 32 ГБ, 1 ТБ, RTX 5070) | единственный AMD + RTX 50 с 32 ГБ/1 ТБ около 1100 € | карточка: «Für dieses Produkt sind zur Zeit nur Gebraucht-Angebote verfügbar» — [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/207341402_-omen-16-ap-c2vm8ea-hp.html); поиск idealo «Omen 16-ap» — других 16-ap нет, семейство «Omen 16 2025» — ab 1279 € (с Intel). История — API 404, минимум новых 1399 € (14.11.2025) не перепроверен | **reject подтверждён** (только б/у) |
| Acer Nitro V 16 AI `ANV16-42-R38V` (R7 260, RTX 5060, 1 ТБ) | та же связка, что у Gigabyte, раньше бывал ≤ 1100 € | только б/у — [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/208996016_-nitro-v-16-ai-anv16-42-r38v-acer.html); история — API 404, «последний раз ≤ 1100 € 22.07.2026» не перепроверен | **reject подтверждён** |
| HP Victus 15 `15-fb3051ng` (R5 240, RTX 5050, 1 ТБ) | самый дешёвый с 1 ТБ (б/у 954 €) | только б/у — [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/207234462_-victus-15-fb3051ng-hp.html); вдобавок HP ограничивает Victus 15 16 ГБ ([MSG 15-fb3xxx](https://kaas.hpcloud.hp.com/pdf-public/pdf_11551834_en-US-1.pdf)) и риск HEVC у HP ([`hevc-amd.md`](hevc-amd.md)) | **reject подтверждён** |

- По новому правилу цены «только маркетплейс» — не причина отбрасывать. Это касается `15-fb3357ng` (920 € eBay) и `16-xd0674ng` (1285,99 € МП): итог у первого ≥ 920 + 142,89 (SSD) + 187,56 (планка) = 1250,45 € и HP-лимит 16 ГБ; второй — дороже 1250 € и RTX 4060. **Reject остаётся**, но по цене/памяти, а не из-за маркетплейса.

### Известные проблемы (сводно)

| Модель | Экран | Шум / нагрев | Прочее | Источник |
|---|---|---|---|---|
| Gigabyte GAMING A16 GA63H (3VH) | WUXGA IPS 165 Гц: 60 % sRGB, 43 % DCI-P3, 330 нит, ΔE 4,74; без ШИМ | 47–50 дБА под нагрузкой; CPU 90–94 °C, без троттлинга | RTX 5060 с TGP 75 Вт (урезан); второй M.2 — Gen4 x2; ~8 ч батареи; Intel-сестра — засветка по краям | [3DNews](https://3dnews.ru/1132160/obzor-gigabyte-gaming-a16-3vh), [LaptopMedia](https://laptopmedia.com/review/gigabyte-gaming-a16-ga63h-amd-review-stealthy-sleeper-with-record-battery-life/), [NBC 3VH](https://www.notebookcheck.net/Gigabyte-Gaming-A16-3VH.1188434.0.html), [NBC GA6H](https://www.notebookcheck.net/An-affordable-RTX-5070-laptop-Gigabyte-Gaming-A16-review.1072350.0.html) |

### Источники

- idealo (Chrome, 30.09.2026): [Gigabyte 3VHK3DE894SH](https://www.idealo.de/preisvergleich/OffersOfProduct/207329496_-gaming-a16-3vhk3de894sh-gigabyte.html), [Kingston KVR56S46BS8-16](https://www.idealo.de/preisvergleich/OffersOfProduct/213624753_-valueram-16gb-ddr5-5600mhz-cl46-so-dimm-on-die-ecc-kvr56s46bs8-16-kingston.html), [Crucial CT16G56C46S5](https://www.idealo.de/preisvergleich/OffersOfProduct/202284828_-16gb-ddr5-5600-cl46-ct16g56c46s5-crucial.html), [C2VM8EA](https://www.idealo.de/preisvergleich/OffersOfProduct/207341402_-omen-16-ap-c2vm8ea-hp.html), [ANV16-42-R38V](https://www.idealo.de/preisvergleich/OffersOfProduct/208996016_-nitro-v-16-ai-anv16-42-r38v-acer.html), [15-fb3051ng](https://www.idealo.de/preisvergleich/OffersOfProduct/207234462_-victus-15-fb3051ng-hp.html).
- Производитель и даташиты: [gigabyte.com GA63H](https://www.gigabyte.com/de/Laptop/GIGABYTE-GAMING-A16-GA63H/sp), [Icecat GTIN 4719331766764](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&GTIN=4719331766764), [amd.com Ryzen 7 260](https://www.amd.com/en/products/processors/laptop/ryzen/200-series/amd-ryzen-7-260.html), [Alternate 3VHK3DE894SH](https://www.alternate.de/GIGABYTE/GAMING-A16-3VHK3DE894SH-Gaming-Notebook/html/product/100151262).
- Обзоры: [3DNews 3VH](https://3dnews.ru/1132160/obzor-gigabyte-gaming-a16-3vh), [LaptopMedia GA63H](https://laptopmedia.com/review/gigabyte-gaming-a16-ga63h-amd-review-stealthy-sleeper-with-record-battery-life/), [NBC 3VH](https://www.notebookcheck.net/Gigabyte-Gaming-A16-3VH.1188434.0.html), [NBC GA63H](https://www.notebookcheck.net/Gigabyte-Gaming-A16-GA63H.1100671.0.html).
