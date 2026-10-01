# Доп. скан idealo без фильтра производителя CPU (AMD, 15–16")

_30.09.2026, ~13:40–14:30, Chrome пользователя, своя вкладка. Выдачи сняты `fetch` + разбор HTML страниц категории (те же страницы, что видит браузер), сортировка по цене, все страницы до потолка. Капчи не было._
_Цель — поймать карточки, которые выпали из [`market-amd.md`](market-amd.md): у части карточек нет поля «Prozessorhersteller», фильтр AMD их не показывает._
_Статус: готово (30.09.2026, ~14:30)._

## Итог коротко

1. **Фильтр AMD действительно теряет карточки**, но в классе 32 ГБ / 1 ТБ / 15–16" ≤ 1150 € он не потерял ничего подходящего. Потери — в 16 ГБ (30 AMD-карточек до 850 €) и 32/512 ГБ (4 карточки), почти всё — старые CPU, Mendocino или распайка.
2. **Главная новость — `83HY008CGE`** (IdeaPad Slim 5 16AKP10, **Ryzen AI 7 350 Zen 5, 2×16 SO-DIMM, 1 ТБ, второй M.2**): утром было только б/у, сейчас есть новое предложение **1059,99 €** — но **только Kaufland-маркетплейс** (продаёт expert), возврат 14 дн. Первый Zen 5 с 2×16 в бюджете. [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/209439304.html)
3. **Новый вариант «+ SSD»: `83HU004KGE`** (IdeaPad Slim 5 16ARP10, R5 7535HS, 2×16, 512 ГБ + свободный M.2 2280, без зарядки) — 776,90 € → с SSD 1 ТБ и зарядкой **941,82 €**. Дешевле `21MW00AYGE` (998,99 €) на ~57 € при том же CPU. [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/210287882.html)
4. **«+ планка» — только HP 255R G10 `CJ5Q2EA`/`CJ5Q1EA`** (1×16 + свободный слот по Icecat): 605 € → с планкой **853,89 €**. Но CPU U-серии Zen 3+, HEVC у HP — риск, HP пишет «slots customer non-accessible», один магазин.
5. `21MW009MGE` (ThinkBook 16 G7 ARP, 2×16, 512 ГБ) + SSD = 1091,89 € — укладывается, но хуже `21MW00AYGE` (998,99 € с 1 ТБ). Прочие новые — reject (HEVC выкл., старый CPU, нет второго M.2, 2×8, распайка).
6. Цены сдвинулись с утра: `21KK0074GE` — 1149 € (было 999), `NX.DL5EG.002` — 999 € (было 986,51), `21UT004QGE` — 1066,82 €.

## Фильтры (id idealo, категория 3751)

| Фильтр | id | Как нашёл |
|---|---|---|
| AMD / 16 Zoll / 15 Zoll / 1 TB SSD / 32 GB / 16 GB | 848110 / 1568565 / 699493 / 2682401 / 7612877 / 7612874 | `idealo-howto.md`, `market-amd.md` |
| **512 GB SSD** | **2682416** | клик по фильтру, заголовок «… 512 GB SSD-Speicher» |
| Prozessor Codename: Gorgon Point / Hawk Point / Hawk Point-HS / Hawk Point-U / Krackan Point / Phoenix / Rembrandt H / Rembrandt R / Rembrandt U / Strix Point / Strix Point-HX | 107335564 / 107335565 / 107335566 / 107335567 / 107335572 / 107335580 / 107335589 / 107335590 / 107335591 / 107335595 / 107335596 | перебор `3751F<id>.html`, id → `<title>` |
| прочие AMD-кодовые имена (для справки) | Barcelo 107335549, Barcelo-R 107335550, Cezanne H/U 107335553/554, Dragon Range 107335559, Dragon Range-HX 107335560, Fire Range 107335561, Lucienne U 107335573, Mendocino 107335575, Renoir 107335592, Strix Halo 107335594 | то же |

- Размер страницы выдачи — 36 карточек; страница N — `3751I16-<15×(N−1)>F….html` (как в `idealo-howto.md`).

## Проход 1 — 32 ГБ + 1 ТБ, без фильтра Intel/AMD, до 1150 €

Выдачи (30.09.2026): [16 Zoll](https://www.idealo.de/preisvergleich/ProductCategory/3751F1568565-2682401-7612877.html?sortKey=minPrice) — 72 карточки на 2 стр. (до 1278 €), [15 Zoll](https://www.idealo.de/preisvergleich/ProductCategory/3751F699493-2682401-7612877.html?sortKey=minPrice) — 72 карточки на 2 стр. (до 1169 €). AMD отобраны по названию CPU.

| pid · модель · P/N | CPU | ab, € · предл. | Статус |
|---|---|---|---|
| 207280344 IdeaPad Slim 5 16 `83HY0061GE` | AI 5 340 | 877 · только б/у | уже в market-amd |
| 208030540 HP ProBook 4 G1a 16 `C7SP9ES` | R5 230 | 899 · 8 | уже в market-amd (HEVC выкл.) |
| **206577198 HP EliteBook 665 G11 `8Z719AV`** | R7 PRO 7735U | 949 · 4 | **новая**, reject: HEVC выкл. (см. ниже) |
| 207875978 Acer Aspire 16 AI `A16-61M-R583` | AI 7 350 | 983,33 · только б/у | уже в market-amd |
| 207306483 ThinkBook 16 G7 `21MW00AYGE` | R5 7535HS | 998,99 · 314 | уже в market-amd / brands-amd |
| 211778543 Acer Swift Air 16 `NX.DL5EG.002` | AI 5 330 | 999 (было 986,51) · 7 | уже в market-amd (распайка) |
| 209439304 IdeaPad Slim 5 16 `83HY008CGE` | AI 7 350 | **1059,99 · появилось новое предложение** (утром было только б/у) | P/N уже в market-amd, **статус новый → карточка ниже** |
| 209122445 ThinkBook 16 G9 `21UT004QGE` | R5 220 | 1066,82 · 39 | уже в market-amd |
| 208031586 Acer Aspire 16 AI `A16-61M-R8T1` | AI 7 350 | 1080,25 · 17 | уже в market-amd (распайка) |
| 207306221 ThinkBook 16 G7 `21MW007VGE` | R7 7735HS | 1080,62 · 335 | уже в market-amd |
| 203811127 ThinkBook 16 G6 `21KK0074GE` | R7 7730U | **1149 · 18** (утром 999 у electronic4you) | уже в market-amd; сейчас выше потолка |
| 207390560 HP OmniBook 5 16 `16-ag1477ng` | AI 7 350 | 1105,36 · только б/у | уже в market-amd |
| 208030541 HP ProBook 4 G1a 16 `C7SQ0ES` | R5 230 | 1129 · 8 | уже в market-amd (HEVC выкл.) |
| 207341402 HP Omen 16-ap `C2VM8EA` | R9 8940HX + RTX 5070 | 1129 · только б/у | уже в candidates-gpu |
| 210080645 HP OmniBook 3 16 `16-bv0074ng` | AI 7 445 | 1130,23 · 1 | уже в brands-amd; выше потолка |
| 207096771 ThinkPad E16 G3 `21ST004GGE` | R5 220 | 1149 · 119 | уже в market-amd (1×32) |
| 209373389 Acer Swift Air 16 `SFA16-61M-R559` | AI 7 350 | 1149 · 11 | уже в market-amd (распайка) |
| **15":** 213603044 «Lenovo IdeaPad 1 15,6" … Ryzen 5 7520U, 8GB RAM, 256GB (15AMN7)» | R5 7520U (Mendocino) | 648,38 · 1 (Amazon МП) | **новая**, reject: в названии 8 ГБ / 256 ГБ (фильтр idealo врёт), Mendocino — LPDDR5 максимум 16 ГБ ([amd-cpu.md](amd-cpu.md)) |
| 203893377 / 203893407 CSL R'Evolve C15 `90608` / `90610` | R5 5500U | 659 / 709 | уже в market-amd |
| **211709177 Acer Aspire Go 15 `AG15-42P-R3HH`** | R7 5825U (Barcelo, Zen 3) | 699 · 2 | **новая**, reject: CPU 2022 г. (см. ниже) |
| 208529022 Acer Aspire Go 15 `AG15-42P-R5ZD` | R7 5825U | 729 · 1 | уже в market-amd |
| 208438555 HP OmniBook 3 `15-fn0278ng` | AI 7 350 | 767 · только б/у | новая, reject: только б/у |
| 205898880 HP 255 G10 «884420874911» / 207229437 HP 15 «4260260631727» | R5 7530U | 919 / 929 | уже в market-amd (сборки продавца) |
| 207948312 HP 15-fc0677ng `C8TT7EA` | R7 7730U | 923,30 · 9 | уже в market-amd |
| 212191488 ASUS ExpertBook BM1 «4718017633086» | R7 170 | 1119 · 2 | уже в brands-amd / candidates-other-brands (BM1503); выше потолка |

**Итог прохода 1:** фильтр AMD в утреннем скане ничего подходящего не потерял. Новых подходящих карточек нет; главное изменение — у `83HY008CGE` (Zen 5, 2×16) появилось новое предложение за 1059,99 €.

## Проход 2 — 16 ГБ + 1 ТБ, 15/16", до 850 € (кандидаты «+ планка»)

Выдачи: [с фильтром AMD](https://www.idealo.de/preisvergleich/ProductCategory/3751F699493-848110-1568565-2682401-7612874.html?sortKey=minPrice) — 72 карточки на 2 стр.; [без фильтра AMD](https://www.idealo.de/preisvergleich/ProductCategory/3751F699493-1568565-2682401-7612874.html?sortKey=minPrice) — 180 карточек на 5 стр. **Без фильтра нашлось ещё 30 AMD-карточек до 850 €** — фильтр их теряет.

Отбор «+ планка» — только линейки, где вероятно 1×16 + свободный слот или 16 распайки + слот. Остальное отброшено по линейке:

| Карточки (pid · P/N) | CPU | ab, € | Почему не «+ планка» / статус |
|---|---|---|---|
| **208126554 HP 255 G10 `CJ5Q2EA`**, **208126364 `CJ5Q1EA`** | R5 7535U (Rembrandt-R) | 599 | уже в market-amd («не проверено») → **проверено: 1×16 + свободный слот** (Icecat) — карточка ниже, список «+ планка» |
| 209172185 Vivobook 16 `M1607GA-MB020W`, **209172188 «ASUS Vivobook 16 M1607 2026»** | AI 7 445 | 799 | уже в candidates-other-brands (16 распайка + слот); 209172188 — **дубль карточки**: оба предложения (NBB, nullprozentshop) называются `M1607GA-MB020W` |
| 206751394 Vivobook S16 `M3607HA-RP017W` | R7 260 | 819 | уже в candidates-other-brands (16 распайка + слот, 1067,89 € с планкой) |
| 208069128 `83HY006XGE`, **213186337 `83HY009NGE`** (IdeaPad Slim 5 16AKP10) | AI 5 330 | 796,39 / 848 | 2×8 — `83HY009NGE`: «2x 8GB SODIMM DDR5-5600» ([PSREF](https://psref.lenovo.com/Detail/IdeaPad/IdeaPad_Slim_5_16AKP10?M=83HY009NGE)); менять обе |
| **208471339 `83KU002JGE`** (IdeaPad 5 2-in-1 16AKP10) | AI 5 340 | 822,12 | «16GB Soldered LPDDR5X-7500 … not upgradable» ([PSREF](https://psref.lenovo.com/Detail/IdeaPad/IdeaPad_5_2_in_1_16AKP10?M=83KU002JGE)) |
| **210264011 `83S2003GGE`** (IdeaPad Slim 5a 16AGP11) | AI 5 430 | 849 | уже в brands-amd: 2×8 |
| IdeaPad Slim 3 ARP10: **`83K800CGGE`, `83K800GQGE`, `83K800A2GE`, `83K800ENGE`, `83K700UEGE`, `83K700SSGE`**; `83K700ENGE`, `83K8006EGE` | R5 150 / R7 170 / 7535HS / 7735HS | 666–849 | «8 распайки + 1 SO-DIMM, максимум 24 ГБ» у платформы ([PSREF 16ARP10](https://psref.lenovo.com/Detail/IdeaPad/IdeaPad_Slim_3_16ARP10?M=83K8006EGE), см. market-amd) — 32 ГБ невозможно |
| IdeaPad Slim 3 ABR8 `82XR009WGE`, `82XR0094GE`, `82XM008AGE`, **`82XM00FHGE`**, **«0199275164224»** | 7730U / 7430U / 5825U | 699–849 | распайка DDR4 без слота (PSREF ABR8, см. market-amd) |
| **210612660 / 213088511 / 208996010 Vivobook 16 OLED `M1605NAQ-MB007W` / `-MB226W` / `-MB029W`** | R7 170 / R5 150 | 629–679 | уже в candidates-other-brands: 8 on board + слот, максимум 24 ГБ |
| Mendocino: HP 15-fc0554ng, 15-fc0655ng, **HP 15 `BU7J0EA`**, **OmniBook 3 16 `16-by0656ng`** (R5 40), **IdeaPad Slim 3 15 `82XQ019TGE`** (R5 40) | 7520U / Ryzen 5 40 | 395–779 | Mendocino — LPDDR5 распайка, максимум 16 ГБ ([amd-cpu.md](amd-cpu.md), [brands-amd.md](brands-amd.md)) |
| Zen 2 / Zen 3 (2020–2022): CSL C15 `90592`/`90594`, Acer Aspire 3 `A315-44P-R0TB`, HP 15s-eq3078ng / eq2677ng / eq2679ng, **Acer Aspire Lite 15 `AL15-45P-R15P`**, **Ninkear A15 Pro**, **Medion Avantum 15 E1 `30039298`** (16 ГБ-вариант), HP 255 G10 «4262425498749», HP 15 «4260260631697» | 5500U / 5700U / 5825U / 7430U / 7530U | 528–789 | старый CPU (Vega, без AV1); сборки продавца по EAN — не заводской SKU |
| **213560240 Ankermann RX16** | R9 6900HX | 639 · 1 | неизвестный бренд, один продавец, CPU 2022 г. — reject |
| HP 15-fc0680ng / 0676ng / 0075ng, OmniBook 3 15-fn0655ng / 0653ng | 7730U / AI 5 340 / 330 | 655–729 | уже в market-amd |

## Проход 3 — 32 ГБ + 512 ГБ, 15/16", до 1000 € (кандидаты «+ SSD 1 ТБ во второй M.2»)

Выдачи: [с фильтром AMD](https://www.idealo.de/preisvergleich/ProductCategory/3751F699493-848110-1568565-2682416-7612877.html?sortKey=minPrice) — 16 карточек; [без фильтра AMD](https://www.idealo.de/preisvergleich/ProductCategory/3751F699493-1568565-2682416-7612877.html?sortKey=minPrice) — 36 (1 стр. до потолка). Без фильтра AMD нашлось ещё 4 AMD-карточки.

| pid · модель · P/N | CPU | ab, € | Второй M.2 (даташит) | Статус |
|---|---|---|---|---|
| 207229438 HP 15 «4260260631710» | R5 7530U | 869 | — | сборка продавца по EAN — reject |
| 209122443 ThinkBook 16 G9 `21UT004EGE` | R5 220 | 894 · 7 | есть (PSREF) | уже в market-amd; + SSD 142,89 = **1036,89 €** |
| **206598202 ThinkBook 16 G7 `21MW009MGE`** | R5 7535HS | 949 · 11 | **есть**: «Two M.2 2280 PCIe 4.0 x4 slots» | **новая → карточка ниже** |
| 214137501 HP EliteBook 8 G1a 16 `CN0Q3EC` | R5 230 | 999 · 1 | не проверено | уже в hevc-amd; 999 + 142,89 = 1141,89 € > 1100 — reject |
| **208441340 HP 15-fc0063ng**, **208408777 HP 15-fc0065ng `CA8S1EA`** | R5 7430U (Barcelo-R, Zen 3) | 688 (Kaufland МП) / 699 | не проверено; Icecat `CA8S1EA`: память «On-board», раскладка «Not available» | новые, reject: CPU 2022 г. (Vega), второй M.2 не подтверждён |
| **209094412 Lenovo V15 G6 ARP `83UU001LGE`** | R5 150 (Rembrandt, Zen 3+) | 759 · 20 | **нет**: «One M.2 2280 PCIe 4.0 x4 slot» ([PSREF](https://psref.lenovo.com/Detail/Lenovo/Lenovo_V15_G6_ARP?M=83UU001LGE)) | новая, reject: второго M.2 нет (2×16 DDR5-4800 есть) |
| **210287882 IdeaPad Slim 5 16ARP10 `83HU004KGE`** | R5 7535HS | 776,90 · 5 | **есть**: «One M.2 2242 … One M.2 2280 PCIe 4.0 x4» | **новая → карточка ниже** |

## Проход 4 — фильтр «Prozessor Codename» + 32 ГБ

- [15/16" + 32 ГБ + Gorgon / Hawk Point (+HS, -U) / Krackan / Phoenix / Rembrandt H/R/U / Strix Point, без фильтра SSD](https://www.idealo.de/preisvergleich/ProductCategory/3751F699493-1568565-7612877-107335564-107335565-107335566-107335567-107335572-107335580-107335589-107335590-107335591-107335595.html?sortKey=minPrice) — 36 карточек до потолка: **новых относительно проходов 1–3 нет**.
- [То же без фильтра размера](https://www.idealo.de/preisvergleich/ProductCategory/3751F7612877-107335564-107335565-107335566-107335567-107335572-107335580-107335589-107335590-107335591-107335595.html?sortKey=minPrice) — новые только 13–14" и 18" (EliteBook 835 G10, ThinkBook 14 G7/G9, ThinkPad E14 G7, ProBook 4 G1a 14, Vivobook 18 M1807GA, OmniBook 7 Aero 13 и др.) — вне 15–16".
- Вывод: у карточек 15–16" без поля «Prozessorhersteller» кодовое имя тоже есть не всегда, но всё, что ловит фильтр кодовых имён, уже поймали проходы 1–3.

## Цены докупки (idealo, 30.09.2026, цена с доставкой)

| Что | Цена | Магазин · возврат | Карточка | Мин. за год (API) |
|---|---|---|---|---|
| **SSD Kingston NV3 1 ТБ** (расчётная) | **142,89 €** | alternate.de, 14 дн.; x-kom.de 146,89; computeruniverse / cyberport 149,83 (30 дн.) | [204697967](https://www.idealo.de/preisvergleich/OffersOfProduct/204697967.html) | 42,00 € (01.10.2025) |
| SSD WD Blue SN5000 1 ТБ | 171,00 € | galaxus.de, 30 дн. | [204448902](https://www.idealo.de/preisvergleich/OffersOfProduct/204448902.html) | 54,61 € |
| SSD Crucial P310 1 ТБ (2280) | 174,89 € | alza.de, 30 дн. | [204799641](https://www.idealo.de/preisvergleich/OffersOfProduct/204799641.html) | 56,69 € |
| SSD Samsung 990 EVO Plus 1 ТБ | 194,99 € | notebooksbilliger.de, 30 дн. (ab 189,00) | [204850856](https://www.idealo.de/preisvergleich/OffersOfProduct/204850856.html) | 63,03 € |
| Зарядка Lenovo 65W USB-C `4X20M26272` | 22,03 € (computeruniverse.net); 22,55 € (cyberport.de, 30 дн.) | | [5584731](https://www.idealo.de/preisvergleich/OffersOfProduct/5584731.html) | 17,90 € |
| Планка DDR5-5600 16 ГБ Crucial `CT16G56C46S5` | 248,89 € (alza.de) — как в [candidates-other-brands.md](candidates-other-brands.md) | | [202284828](https://www.idealo.de/preisvergleich/OffersOfProduct/202284828_-16gb-ddr5-5600-cl46-ct16g56c46s5-crucial.html) | — |

SSD за год подорожали в 2,5–3,4 раза (NV3: 42 → 143 €).

## Карточки новых находок (в пределах потолка)

HEVC у Lenovo: в PSREF AMD-платформ Lenovo отключений HEVC не найдено ([hevc-amd.md](hevc-amd.md), п. 7) — проверить DXVA Checker в срок возврата.

### 1. IdeaPad Slim 5 16AKP10 — `83HY008CGE` · **1059,99 €** · список A (2×16 с завода) — **Zen 5 в бюджете, но только маркетплейс**

| Поле | Значение | Источник |
|---|---|---|
| CPU | Ryzen AI 7 350 (8C/16T), Krackan Point (Zen 5 + Zen 5c), Radeon 860M | [PSREF](https://psref.lenovo.com/Detail/IdeaPad/IdeaPad_Slim_5_16AKP10?M=83HY008CGE); idealo «Prozessor Codename Krackan Point» |
| Память | **2× 16 ГБ SODIMM DDR5-5600**, «Two DDR5 SODIMM slots, dual-channel capable», максимум 32 ГБ | PSREF ([PDF](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=83HY008CGE&country_code=)) |
| SSD | 1 ТБ M.2 2242 PCIe 4.0 x4; **два слота M.2** (2242 + 2280, оба PCIe 4.0 x4) | PSREF |
| Экран | 16" WUXGA IPS 300 нит, 45 % NTSC, 60 Гц | PSREF |
| Порты | 2× USB-A 5 Гбит/с, 2× USB-C 10 Гбит/с (PD 65–100 Вт, DP 1.4), HDMI 2.1 (4K60), microSD; USB4 нет, Ethernet нет | PSREF |
| Вес · батарея · БП | ~1,85 кг · 60 Втч · 65 Вт USB-C **в комплекте** | PSREF |
| ОС · гарантия | Windows 11 Home · 2 года (курьер / carry-in), батарея 1 год | PSREF |
| HEVC | отключений у Lenovo не найдено | hevc-amd.md |
| Цена | **1059,99 €** с доставкой — **kaufland.de, маркетплейс, «Verkauf durch: expertDeutschland»**, возврат 14 дн., доставка до 06.10. Единственное новое предложение; б/у и B-Ware — от 949 € | [idealo 209439304](https://www.idealo.de/preisvergleich/OffersOfProduct/209439304.html), «Daten vom 30.09.2026 12:37» |
| История (1 год, API) | карточка с 13.02.2026, 179 точек; **минимум 896,28 € (23.02.2026)**, средняя 952,23 €, максимум 1059,99 € (сегодня); все 179 дней ≤ 1100 € | `/price-chart/…/209439304/history?period=1Y` |
| Итог | **1059,99 €**, докупать ничего не нужно | — |
| Минусы | только маркетплейс (продавец — expert через Kaufland); экран 45 % NTSC; USB4 нет | — |

### 2. HP 255R G10 — `CJ5Q2EA` (Win 11 Pro) / `CJ5Q1EA` (FreeDOS) · 605,00 € + планка = **853,89 €** · список «+ планка» (1×16 + свободный слот)

| Поле | Значение | Источник |
|---|---|---|
| Модель | idealo называет «HP 255 G10», Icecat и QuickSpecs — **HP 255R G10** | [Icecat CJ5Q2EA](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=HP&ProductCode=CJ5Q2EA), [Icecat CJ5Q1EA](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=HP&ProductCode=CJ5Q1EA) |
| CPU | Ryzen 5 7535U (6C/12T), Rembrandt-R (Zen 3+, 2023), Radeon 660M. ⚠️ У `CJ5Q1EA` в названии единственного предложения — «7530U», Icecat — 7535U | Icecat; [QuickSpecs c09053765](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09053765) |
| Память | **1× 16 ГБ DDR5-4800 SO-DIMM, 2 слота SO-DIMM** (Icecat: «Speicherlayout 1 x 16 GB», «2x SO-DIMM»). QuickSpecs: «2 SODIMM», «Support Dual Channel Memory», «System runs at 4800», максимум 32 ГБ. ⚠️ Там же: **«All slots are customer non-accessible / non-upgradeable»** — HP не считает память пользовательской деталью | Icecat; QuickSpecs v7 (06.03.2026), с. 7 |
| SSD | 1 ТБ M.2 2280 PCIe NVMe; второй M.2 — не указан | Icecat; QuickSpecs |
| Экран | 15,6" FHD IPS (варианты 250/300 нит, 45 % NTSC; у SKU какой — не проверено) | QuickSpecs |
| Порты | 2× USB-A 5 Гбит/с, 1× USB-C 10 Гбит/с (DP, PD), HDMI 1.4b | Icecat |
| Вес · батарея · БП | 1,66 кг · 41 Втч · 65 Вт USB-C в комплекте | Icecat; QuickSpecs |
| Гарантия | 1 год (1/1/0) | Icecat |
| HEVC | в QuickSpecs фразы про HEVC нет («Support HD decode, DX12, HDMI 1.4b») → **риск** (политика HP, [hevc-amd.md](hevc-amd.md)) | QuickSpecs |
| Цена | **605,00 €** с доставкой — asaboshisystems.de, обычный магазин, срок возврата idealo не показывает; **одно предложение** на каждой карточке | [idealo 208126554 (CJ5Q2EA)](https://www.idealo.de/preisvergleich/OffersOfProduct/208126554.html), [idealo 208126364 (CJ5Q1EA)](https://www.idealo.de/preisvergleich/OffersOfProduct/208126364.html) |
| История (1 год) | CJ5Q2EA: с 24.10.2025, 27 точек, минимум 548,99 € (28.11.2025), максимум 999,95 €; CJ5Q1EA: минимум 499,00 € (23.11.2025) | API idealo |
| Итог | 605,00 + 248,89 (Crucial DDR5-5600, заработает на 4800) = **853,89 €**; с Kingston 187,56 € (маркетплейс) — 792,56 € | расчёт |
| Минусы | CPU U-серии Zen 3+, iGPU RDNA 2 (maintenance mode, [amd-cpu.md](amd-cpu.md)); 41 Втч; HDMI 1.4b; HEVC — риск; HP запрещает апгрейд памяти пользователю; один магазин | — |

### 3. IdeaPad Slim 5 16ARP10 — `83HU004KGE` · 776,90 € + SSD + зарядка = **941,82 €** · список «+ SSD» (2×16, 512 ГБ, второй M.2 свободен)

| Поле | Значение | Источник |
|---|---|---|
| CPU | Ryzen 5 7535HS (6C/12T), Rembrandt-R (Zen 3+), Radeon 660M | [PSREF](https://psref.lenovo.com/Detail/IdeaPad/IdeaPad_Slim_5_16ARP10?M=83HU004KGE) ([PDF](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=83HU004KGE&country_code=)) |
| Память | **2× 16 ГБ SODIMM DDR5-4800**, два слота, двухканал; максимум «Up to 32GB DDR5-4800 offering» | PSREF |
| SSD | 512 ГБ M.2 2242 PCIe 4.0 x4; **«Two M.2 slots • One M.2 2242 … • One M.2 2280 PCIe 4.0 x4»** → 1 ТБ ставится во второй слот 2280 | PSREF |
| Экран | 16" WUXGA IPS 300 нит, 45 % NTSC | PSREF |
| Порты | 2× USB-A 5 Гбит/с, 2× USB-C **5 Гбит/с** (PD 65–100 Вт, DP 1.4), HDMI 2.1, microSD | PSREF |
| Вес · батарея · БП | ~1,85 кг · 60 Втч · **без блока питания** («No Power Adapter») | PSREF |
| ОС · гарантия | Windows 11 Home · 2 года (курьер / carry-in), батарея 1 год | PSREF |
| Цена | **776,90 €** — technik-brandenburg.de, обычный магазин, срок возврата idealo не показывает; дальше expert-technomarkt.de / boomstore.de 799,00, expert.de 799,00 (возврат 14 дн.). 5 предложений | [idealo 210287882](https://www.idealo.de/preisvergleich/OffersOfProduct/210287882.html) |
| История (1 год) | с 07.05.2026, 125 точек; минимум 699,00 € (20.05.2026), средняя 769,45 €, максимум 831 € | API idealo |
| Итог | 776,90 + 142,89 (Kingston NV3 1 ТБ) + 22,03 (Lenovo 65W USB-C) = **941,82 €** (с зарядкой у cyberport 22,55 € — 942,34 €); диск 1,5 ТБ | расчёт |
| Минусы | CPU Zen 3+ (2023), iGPU RDNA 2; USB-C только 5 Гбит/с; нет зарядки в комплекте; «1 ТБ с завода» не выполнен | — |

### 4. ThinkBook 16 G7 ARP — `21MW009MGE` · 949,00 € + SSD = **1091,89 €** · список «+ SSD» (2×16, 512 ГБ, второй M.2 свободен)

| Поле | Значение | Источник |
|---|---|---|
| CPU | Ryzen 5 7535HS, Rembrandt-R (Zen 3+), Radeon 660M | [PSREF](https://psref.lenovo.com/Detail/ThinkBook/ThinkBook_16_G7_ARP?M=21MW009MGE) ([PDF](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=21MW009MGE&country_code=)); idealo «Rembrandt R» |
| Память | **2× 16 ГБ SODIMM DDR5-4800**, два слота, до 64 ГБ | PSREF |
| SSD | 512 ГБ M.2 2242 PCIe 4.0 x4; **«Two M.2 2280 PCIe 4.0 x4 slots»**, до 2 ТБ каждый | PSREF |
| Экран | 16" WUXGA IPS 300 нит, 45 % NTSC | PSREF |
| Порты | 2× USB-A 5 Гбит/с, 1× USB-C 10 Гбит/с, **1× USB4 40 Гбит/с**, HDMI 2.1, SD-кардридер | PSREF |
| Вес · батарея · БП | от 1,7 кг · 45 Втч · 65 Вт USB-C в комплекте | PSREF |
| ОС · гарантия | Windows 11 Pro · 1 год (курьер / carry-in) + «1Y Premier» | PSREF |
| Цена | **949,00 €** — easynotebooks.de (возврат 14 дн.); notebook.de 949,01 (14 дн.); notebooksbilliger.de 1007,99 (30 дн.). 11 предложений | [idealo 206598202](https://www.idealo.de/preisvergleich/OffersOfProduct/206598202.html) |
| История (1 год) | с 30.09.2025, 366 точек; **минимум 672,26 € (23.10.2025)**, средняя 819,41 €, максимум 949 € (сейчас) | API idealo |
| Итог | 949,00 + 142,89 = **1091,89 €** (1,5 ТБ) | расчёт |
| Вывод | **хуже `21MW00AYGE`** (тот же ноутбук и CPU, 1 ТБ с завода) — 998,99 € ([market-amd.md](market-amd.md)); смысл только ради 1,5 ТБ | — |

### 5. Отброшенные новые (коротко)

| P/N | Цена idealo | Почему reject | Источник |
|---|---|---|---|
| HP EliteBook 665 G11 `8Z719AV` (R7 PRO 7735U, 32/1 ТБ) | 949,00 € — novendu.de (обычный магазин); Kaufland МП 949; eBay МП 949 · [idealo 206577198](https://www.idealo.de/preisvergleich/OffersOfProduct/206577198.html); за год минимум 949 € (23.07.2026) | **HEVC отключён** у всей платформы (QuickSpecs c08927104, см. [hevc-amd.md](hevc-amd.md)); `…AV` — базовый номер CTO, раскладку 32 ГБ по SKU не проверял (Icecat: 404) | hevc-amd.md |
| Acer Aspire Go 15 `AG15-42P-R3HH` (R7 5825U, 32/1 ТБ) | 707,99 € — notebooksbilliger.de (30 дн.); nullprozentshop 706,99 · [idealo 211709177](https://www.idealo.de/preisvergleich/OffersOfProduct/211709177.html); минимум за год 649 € (16.09.2026) | CPU Barcelo (Zen 3, 2022, Vega) — не «актуальная архитектура»; раскладка — **не проверено** (Icecat по модели — 404; у серии с завода 1×8, макс. 32 — [brands-amd.md](brands-amd.md)); Acer — риск HEVC | — |
| Lenovo V15 G6 ARP `83UU001LGE` (R5 150, 2×16, 512 ГБ) | 759,00 € — aitek.de; galaxus.de 789,95 (30 дн.) · [idealo 209094412](https://www.idealo.de/preisvergleich/OffersOfProduct/209094412.html); минимум 712,52 € (10.08.2026) | **второго M.2 нет** («One M.2 2280 slot»); 1 ТБ только заменой диска; HDMI 1.4b, USB-C 10 Гбит/с с DP 1.2 | [PSREF](https://psref.lenovo.com/Detail/Lenovo/Lenovo_V15_G6_ARP?M=83UU001LGE) |
| HP 15-fc0063ng / 15-fc0065ng `CA8S1EA` (R5 7430U, 32/512) | 688,00 € (Kaufland МП) / 707,99 € (electronic4you.de) · [208441340](https://www.idealo.de/preisvergleich/OffersOfProduct/208441340.html), [208408777](https://www.idealo.de/preisvergleich/OffersOfProduct/208408777.html) | CPU Barcelo-R (Zen 3, Vega); Icecat `CA8S1EA`: DDR4 «On-board», раскладка «Not available»; второй M.2 — не проверено | [Icecat CA8S1EA](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=HP&ProductCode=CA8S1EA) |
| Lenovo IdeaPad 1 15AMN7 (idealo 213603044) | 648,38 € — Amazon МП, 1 предложение | название: 8 ГБ / 256 ГБ — фильтр 32/1 ТБ ошибочен; Mendocino | [idealo 213603044](https://www.idealo.de/preisvergleich/OffersOfProduct/213603044.html) |
| HP OmniBook 3 `15-fn0278ng` (AI 7 350) | 767 € — только б/у | не новый | [idealo 208438555](https://www.idealo.de/preisvergleich/OffersOfProduct/208438555.html) |
| IdeaPad Slim 5 16AKP10 `83HY009NGE` (AI 5 330) | 848 € · 13 | 2×8 + слабый CPU (4 ядра) | [PSREF](https://psref.lenovo.com/Detail/IdeaPad/IdeaPad_Slim_5_16AKP10?M=83HY009NGE), [idealo 213186337](https://www.idealo.de/preisvergleich/OffersOfProduct/213186337.html) |
| IdeaPad 5 2-in-1 16AKP10 `83KU002JGE` (AI 5 340) | 822,12 € · 23 | 16 ГБ распайка, не расширить | [PSREF](https://psref.lenovo.com/Detail/IdeaPad/IdeaPad_5_2_in_1_16AKP10?M=83KU002JGE), [idealo 208471339](https://www.idealo.de/preisvergleich/OffersOfProduct/208471339.html) |

## Списки по итогам скана

| Список | P/N | Итог, € | Карточка idealo |
|---|---|---|---|
| A (2×16 с завода) | `83HY008CGE` IdeaPad Slim 5 16AKP10, AI 7 350 | 1059,99 (Kaufland МП, продавец expert) | [209439304](https://www.idealo.de/preisvergleich/OffersOfProduct/209439304.html) |
| «+ SSD 1 ТБ» (условный) | `83HU004KGE` IdeaPad Slim 5 16ARP10, R5 7535HS | 941,82 (776,90 + NV3 142,89 + зарядка 22,03) | [210287882](https://www.idealo.de/preisvergleich/OffersOfProduct/210287882.html) |
| «+ SSD 1 ТБ» (условный) | `21MW009MGE` ThinkBook 16 G7 ARP, R5 7535HS | 1091,89 (949 + 142,89) | [206598202](https://www.idealo.de/preisvergleich/OffersOfProduct/206598202.html) |
| «+ SSD 1 ТБ» (уже известен) | `21UT004EGE` ThinkBook 16 G9 AHP, R5 220 | 1036,89 (894 + 142,89) | [209122443](https://www.idealo.de/preisvergleich/OffersOfProduct/209122443.html) |
| «+ планка» (1×16 + слот) | `CJ5Q2EA` / `CJ5Q1EA` HP 255R G10, R5 7535U | 853,89 (605 + 248,89) | [208126554](https://www.idealo.de/preisvergleich/OffersOfProduct/208126554.html) / [208126364](https://www.idealo.de/preisvergleich/OffersOfProduct/208126364.html) |

## Контроль

- Текстовый поиск по категории «Ryzen 32GB» и «Ryzen 32 GB 1TB» ([пример](https://www.idealo.de/preisvergleich/ProductCategory/3751.html?q=Ryzen%2032%20GB%201TB&sortKey=minPrice)) — выдача забита б/у-предложениями (EliteBook 745 G6, Latitude 5495 и т. п.) и сборками продавцов; новых 15–16" AMD с 32 ГБ до потолка не дал. Попались HP 255R G10 `CU0R4ES` (16/512, 519,90 €) и `D30YSES` (24/512, 609 €) — вне критериев (512 ГБ, один M.2 не подтверждён / 24 ГБ).
- Кодовые имена во всех найденных SKU сверены с полем idealo «Prozessor Codename» и [amd-cpu.md](amd-cpu.md).

## Что не проверено

- Срок возврата у technik-brandenburg.de (`83HU004KGE`), asaboshisystems.de (`CJ5Q2EA`), aitek.de (`83UU001LGE`) — idealo не показывает.
- Какая матрица (250 или 300 нит) у `CJ5Q2EA` / `CJ5Q1EA`; CPU у `CJ5Q1EA` (Icecat — 7535U, предложение — 7530U); есть ли второй M.2 у HP 255R G10.
- Раскладка памяти `AG15-42P-R3HH` (Icecat по модели — 404) и `8Z719AV` (номер CTO) — оба отброшены по другим причинам.
- HEVC на конкретных экземплярах Lenovo — только по отсутствию отключений в PSREF; проверка DXVA Checker — в срок возврата.

## Источники

- idealo.de, Chrome пользователя, 30.09.2026: выдачи и карточки — ссылки в таблицах выше; история цен — `https://www.idealo.de/price-chart/sites/1/products/<pid>/history?period=1Y`.
- Lenovo PSREF (PDF-экспорт): [83HY008CGE](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=83HY008CGE&country_code=), [83HU004KGE](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=83HU004KGE&country_code=), [21MW009MGE](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=21MW009MGE&country_code=), [83UU001LGE](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=83UU001LGE&country_code=), [83HY009NGE](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=83HY009NGE&country_code=), [83KU002JGE](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=83KU002JGE&country_code=).
- HP: [QuickSpecs HP 255R G10, c09053765 v7 (06.03.2026)](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09053765); EliteBook 665 G11 — QuickSpecs c08927104 через [hevc-amd.md](hevc-amd.md).
- Icecat open: [CJ5Q2EA](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=HP&ProductCode=CJ5Q2EA), [CJ5Q1EA](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=HP&ProductCode=CJ5Q1EA), [CA8S1EA](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=HP&ProductCode=CA8S1EA).
- Проект: [market-amd.md](market-amd.md), [brands-amd.md](brands-amd.md), [hevc-amd.md](hevc-amd.md), [amd-cpu.md](amd-cpu.md), [candidates-other-brands.md](candidates-other-brands.md), [candidates-gpu.md](candidates-gpu.md).
