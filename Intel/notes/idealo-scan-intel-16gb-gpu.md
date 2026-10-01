# Скан idealo: Intel 15–16" с 16/24 ГБ (+ планка) и с видеокартой ≥ 8 ГБ

_30.09.2026, локальная сессия, Chrome пользователя (своя вкладка). Все цены — с idealo.de, «с доставкой» = «inkl. Versand» из карточки._
_Капчи не было. Примерно после 20-й открытой карточки API истории цен idealo (`/price-chart/.../history`) начал отвечать 404 — даже на собственный запрос страницы. Поэтому история цен есть у всех карточек части B, а у карточек части A её нет._

## Фильтры (проверено по document.title)

| Что | id |
|---|---|
| Intel | 107335535 |
| SSD 1 ТБ | 2682401 |
| 15 Zoll / 16 Zoll | 699493 / 1568565 |
| RAM 16 / 24 / 32 GB | 7612874 / 7612876 / 7612877 |
| RTX 4060, 5050, 5060, 5070 | 104023766, 106697019, 106745465, 106843055 (выбраны все четыре; какой id к какой карте — не разбирал) |

- **A** (16 или 24 ГБ, 1 ТБ, 15/16", Intel), всего 388 товаров: [стр. 1](https://www.idealo.de/preisvergleich/ProductCategory/3751F699493-1568565-2682401-7612874-7612876-107335535.html?sortKey=minPrice), [стр. 2](https://www.idealo.de/preisvergleich/ProductCategory/3751F699493-1568565-2682401-7612874-7612876-107335535I16-15.html?sortKey=minPrice) (749,00 → 879,95 €). Потолок 850 € пройден на стр. 2. Страницы нумеруются так: `I16-15` — вторая, `I16-30` — третья, по 36 товаров на странице.
- **B** (RTX 4060/5050/5060/5070, 16/24/32 ГБ, 1 ТБ, 15/16", Intel), всего 179 товаров: [стр. 1](https://www.idealo.de/preisvergleich/ProductCategory/3751F699493-1568565-2682401-7612874-7612876-7612877-104023766-106697019-106745465-106843055-107335535.html?sortKey=minPrice) (899 → 1409 €). Потолок 1250 € пройден на стр. 1.
- **B без фильтра по ОЗУ**, 204 товара: [стр. 1](https://www.idealo.de/preisvergleich/ProductCategory/3751F699493-1568565-2682401-104023766-106697019-106745465-106843055-107335535.html?sortKey=minPrice). До 1250 € добавились только два MSI Cyborg 15 с 8 ГБ (см. «Отсеяно»).

Цены планок на idealo (для расчёта итога):
- DDR5-5600 16 ГБ Kingston KVR56S46BS8-16 — **187,56 €**, но это единственное предложение, и оно на маркетплейсе Galaxus (возврат 30 дней) — [карточка](https://www.idealo.de/preisvergleich/OffersOfProduct/213624753_-valueram-16gb-ddr5-5600mhz-cl46-so-dimm-on-die-ecc-kvr56s46bs8-16-kingston.html).
- DDR4-3200 16 ГБ Samsung M471A2K43DB1-CWE — 97,50 € (eBay), 129 € (Amazon Marketplace), 135,80 € (Kaufland). Все три предложения — маркетплейсы, обычного магазина в карточке нет — [карточка](https://www.idealo.de/preisvergleich/OffersOfProduct/201545973_-16gb-ddr4-3200-m471a2k43db1-cwe-samsung.html).
- Итог ниже считаю в диапазоне: DDR5 +188…244 € (нижняя граница — маркетплейс, верхняя — ~244 € из задачи), DDR4 +98…136 €.

## A. 16/24 ГБ + 1 ТБ, до 850 € — процессоры не хуже Raptor Lake-H / Meteor Lake-H / Arrow Lake

«Лучшая цена» — у обычного магазина, с доставкой. МП — маркетплейс. Возврат — в днях. «ab» — цена из списка категории, если карточку не открывал.

| Модель · P/N | CPU (Codename на idealo) | ОЗУ | Экран | Лучшая цена · магазин | Раскладка / вывод | В notes |
|---|---|---|---|---|---|---|
| **HP OmniBook 7 AI 16 · 16-ay0750ng** | Core Ultra 5 225H (**Arrow Lake-H**; своей карточки у товара нет, codename из idealo недоступен) | 16 ГБ | 16" WUXGA, Arc 130T | **755,15 €** · hp.com (DE), возврат 14, доставка до 10.10 — [карточка серии](https://www.idealo.de/preisvergleich/OffersOfProduct/206602371_-omnibook-7-ai-16-hp.html) | **НОВОЕ.** Раскладка неизвестна. Если 1×16 + свободный слот: **≈ 943–999 €** → в бюджете, и это Arrow Lake-H. **Проверить даташит HP** | нет (в sweep-dell-hp: «Intel-версий 16" на billiger нет») |
| HP 15-fd1555ng · CU7G6EA | Core Ultra 5 125H (Meteor Lake) | 24 ГБ DDR5 | 15,6" FHD, Arc | **783,17 €** · easynotebooks (14) / technikdirekt; 783,18 € notebook.de — [карточка](https://www.idealo.de/preisvergleich/OffersOfProduct/209321225_-15-fd1555ng-hp.html) | 1×24 + слот (notes). +16 ГБ: ≈ 971–1027 €. Цена совпала с REPORT | REPORT №4 |
| ASUS Vivobook 15 OLED · X1505VA-MA884W | i9-13900H (Raptor Lake-H) | 16 ГБ | 15,6" 2880×1620 OLED (120 Гц — по названию предложения) | **807,99 €** · notebooksbilliger (30); 806,99 € nullprozentshop — [карточка](https://www.idealo.de/preisvergleich/OffersOfProduct/207200981_-vivobook-15-oled-x1505va-ma884w-asus.html) | P/N новый. У семейства по Icecat максимум 16 ГБ (SKU M014X0). Если здесь 16 распайка + свободный слот DDR4 → ≈ 906–944 € за 32 ГБ двухканал (B-список). **Проверить даташит** | семейство (sweep-asus-acer-msi-medion) |
| Lenovo V15 G5 · 83GW00A9GE | i5-13420H (Raptor Lake-H) | 16 ГБ | 15,6" FHD | **598,98 €** · easynotebooks (14); 607,99 € NBB (30) — [карточка](https://www.idealo.de/preisvergleich/OffersOfProduct/208744735.html) | «1 из 2» по магазину (notes). +планка: ≈ 787–843 €. Цена совпала | REPORT (условный) |
| Lenovo IdeaPad Slim 3 15IRH10 · 83K100G1GE | i5-13420H (Raptor Lake-H) | 16 ГБ DDR5 | 15,3" WUXGA | **679,95 €** · expert (14); Kaufland МП 631,71 € — [карточка](https://www.idealo.de/preisvergleich/OffersOfProduct/207280341_-ideapad-slim-3-15-83k100g1ge-lenovo.html) | Платформа 15IRH10: распайка + 1 слот (по notes для 83K1002RGE) → 2×16 не собрать | P/N новый, платформа известна |
| IdeaPad Slim 3 15 · 83K1002TGE | i7-13620H | 16 ГБ | 15,3" WUXGA | ab 749,00 € (6 предл., карточку не открывал) | Платформа 15IRH10 → нет | P/N новый |
| IdeaPad Slim 3 15 G10 · 83K100YWSP | i7-13620H | 16 ГБ | 15,3" | 719,47 € (1 предл., не открывал) | Испанская версия (SP) и платформа 15IRH10 → нет | нет |
| IdeaPad Slim 3 15 · 83K1002RGE | i5-13420H | 16 ГБ | 15,3" | ab 638,06 € | 8 распайка + 8, один слот → нет | sweep-16gb |
| IdeaPad Slim 3 16 · 83K2008PGE / 83K200A1GE | i5-13420H | 16 ГБ | 16" WUXGA | ab 687,73 € / ab 699 € | Один слот → нет | sweep-16gb, candidates-lenovo |
| Lenovo V15 G4 · 83A100JFGE | i5-13420H | 16 ГБ | 15,6" FHD | ab 701 € (2 предл.) | V15 G4: DDR4, распайка / один слот (notes) → нет | sweep-lenovo |
| IdeaPad Slim 5 16 · 83HS00AAGE | i7-13620H | 16 ГБ | 16" | ab 799 € | 2×8 → нет | candidates-lenovo |
| ASUS Vivobook S16 · S3607VA-RP142W | Core 7 240H | 16 ГБ | 16" | ab 799 € | 8 + 8, максимум 16 ГБ → нет | candidates-other |
| Сборки продавцов с i5-13420H / i5-12500H без заводского P/N: V15 G4 196804728483 (648 €), 7427307800820 (709 €), A-1042 (24 ГБ, 739 €), 4262490581452 (849 €), 12500-16-1000 (849 €); V15 G5 T-LM-V15G5-C513-16-T1-W (819 €); IdeaPad 3 15 4262425494383 (i5-12500H, 739 €) | — | 16/24 ГБ | 15,6" | ab-цены из списка | Не заводские конфигурации → не рассматриваю | sweep-lenovo (сборки) |

Чуть выше потолка A:
- Lenovo IdeaPad Slim 5 16IRH10R 83J10065GE (Core 5 210H, Raptor Lake-H Refresh, 24 ГБ) — 865,99 € · expert, возврат 14 — [карточка](https://www.idealo.de/preisvergleich/OffersOfProduct/207280346.html). По notes это 2×12 → не подходит.
- Medion E15443 MD62718 (Core Ultra 7 155H, Meteor Lake, 16 ГБ) — 895,88 €, только euronics (маркетплейс) — [карточка](https://www.idealo.de/preisvergleich/OffersOfProduct/205864759_-e15443-md62718-medion.html). Раскладка неизвестна. С планкой ≈ 1084–1140 €. Родственный MD62621 — 512 ГБ.

## A. Остальные товары до 850 € — не подходят по процессору или памяти

| Модель · P/N | CPU | ab-цена | Причина |
|---|---|---|---|
| CSL R'Evolve C15 V3 90008 / 90026; C15 v4 92324 / 92348 | N200 / N100 | 435,99 / 484,94 / 519 / 569 € | Серия N: один канал памяти |
| HP 15-fd1059ng; HP 15-fd1356ng | Core 5 120U | 549 / 699 € | Переименованный Raptor Lake-U, 2×8 DDR4 (notes) |
| CSL R'Evolve C16 92677 / 92701 | i5-1235U | 639 / 689 € | U-серия 12-го поколения |
| Lenovo IdeaPad 3 15 82H802KGGE | i5-1135G7 | 640 € | 11-е поколение |
| ASUS Vivobook 16X X1605VA-MB2306W | Core 5 120U | 647 € | Максимум 16 ГБ (notes) |
| HP 15-fd0730ng / 15-fd0656ng / 15-fd0079ns (ES) | i5-1334U | 649 / 799 / 781,92 € | U-серия, 2×8 DDR4 (notes) |
| HP 250 G10 8D404ES-16G-1T-W11P, 4262490584392, 853S0ES-16G-1T-W11P, 7427307801513, 195122538941 | i5-1335U / i5-1334U / i7-1355U | 689–849,90 € | Сборки продавцов, U-серия |
| HP 15-fc0673ng | i7-1355U | 749 € | U-серия |
| Acer Aspire 3 A315-59-576H | i5-1235U | 749,99 € | 2×8 DDR4 (notes) |
| HP OmniBook X Flip 16 D5ZM1EA | Core Ultra 5 226V | 779 € | Lunar Lake: память распаяна |
| Acer Aspire Go 15 AG15-72P-50QJ | Core 5 120U | 799 € | Ловушка по процессору |
| Wortmann TERRA MOBILE 1517 1220796 / 1516 1220844 | i5-1235U / i5-1334U | 799,90 / 818,61 € | U-серия. У 1220844 — 1×16 + слот DDR4, он уже в notes |
| Dell Pro 15 Essential GYXJD | i7-1355U | 833,24 € | Максимум 16 ГБ (notes) |
| Lenovo V15 G4 725844015873; ASUS Vivobook X1605 4262490589724; Lenovo V15 4262490582329 | i5-1235U / i3-1315U / Celeron N4500 | по 849 € | Сборки продавцов, слабый CPU |
| Б/у (пропущены): MacBook Pro MLH52D/A, MVVK2, MVVM2; Lenovo 83EM00D6SP, 83ES001AGE; Medion MD62501, E15443 30039333, E16433 MD62698; Acer SFX16-52G-77KY; ThinkPad E15 4262395173530; IdeaPad Slim 5 16 198155976339; Vivobook 16X X1605VA-MB2291W; Vivobook 16 X1607QA-MB054W; Surface Book 2; HP 250 G10 195122536756 | — | 292,99–849,90 € | Б/у |

## B. Видеокарта ≥ 8 ГБ + 1 ТБ, до 1250 €

Строки отсортированы по «ab»-цене idealo. «Мин. 6 мес.» и «дней ≤ 1100 из 182» — дневной минимум idealo по графику.

| Модель · P/N | CPU (Codename на idealo) | ОЗУ | Экран | GPU | Лучшая цена · магазин | МП / условные | Мин. 6 мес. · дней ≤ 1100 | Итог / раскладка | В notes |
|---|---|---|---|---|---|---|---|---|---|
| Monsternotebook Tulpar T5 V23.4 | i7-12700H (**Alder Lake-P**) | 16 ГБ DDR4 | 15,6" FHD 144 Гц | RTX 4060 | **не найдено у обычного магазина** | Amazon Marketplace 899,00 € — [карточка](https://www.idealo.de/preisvergleich/OffersOfProduct/206080042.html) | 787 € (07.10.2025, 1 год) · 49 | Раскладка неизвестна. Если 1×16 + слот DDR4: ≈ 997–1035 €. Но продаёт только маркетплейс, CPU 12-го поколения, RTX 40 без декодирования 4:2:2 | нет |
| Medion Erazer Scout 15 E1 · 30039767 | i5-13420H (Raptor Lake-H) | 16 ГБ | 15,6" FHD 144 Гц, FreeDOS | RTX 5050 | **1006,99 €** · nullprozentshop; **1007,99 €** · NBB (30) — [карточка](https://www.idealo.de/preisvergleich/OffersOfProduct/207120029_-scout-15-e1-medion.html) | heinzsoft 1073,90 € (условная); Amazon МП 1123,76 €; Galaxus МП 1133 €; Kaufland 1154,54 € | 888,17 € (04.06) · 181 | Раскладка неизвестна (у родни 2×8). 1×16 + слот: ≈ 1195–1251 €; 2×8: ≈ 1480 € | candidates-gpu |
| ASUS V16 · V3607VM-RP011 | Core 7 240H (Raptor Lake-H Refresh) | 16 ГБ DDR5 | 16" 1920×1200 144 Гц, без ОС | RTX 5060 | **1071,39 €** · Amazon (14) — [карточка](https://www.idealo.de/preisvergleich/OffersOfProduct/210621618_-v16-v3607vm-rp011-asus.html) | — | 997,74 € (19.06) · 43 | **Испанская QWERTY** (в названии предложения). Раскладка памяти неизвестна | candidates-gpu |
| Gigabyte Gaming A16 · CTHI3DE894SH | i7-13620H (Raptor Lake-H) | 16 ГБ DDR5 | 16" 1920×1200 165 Гц | RTX 5050 | **1115,54 €** · otto (30); 1206,99 € Alternate (14); 1207,99 € NBB (30) — [карточка](https://www.idealo.de/preisvergleich/OffersOfProduct/206981765_-gaming-a16-cthi3de894sh-gigabyte.html) | otto МП 1229,99 €; eBay 1269,99 € | 1027,20 € (01.07) · 151; за год — 831,09 € | Вероятно 1×16 + слот, как у CVHI (не проверено). При 1027 € итог ≈ 1215–1271 € | verify-hp-asus… (упомянут) |
| Lenovo LOQ Essential 15IRX11 · **83SC000EGE** | i5-13450HX (Raptor Lake) | 16 ГБ DDR5 | 15,6" FHD | RTX 5060 | **1111,00 €** · berlet — [карточка](https://www.idealo.de/preisvergleich/OffersOfProduct/207948304.html) | euronics МП 1111 €; Amazon МП 1194,98 € | 974,95 € (01.07) · 123; за год — 888 € | Близнец 0026GE: 1×16 + слот, RTX 5060 65 Вт (PSREF для 0026GE; для 000E не проверено). ≈ 1299–1355 € | P/N новый |
| Lenovo LOQ Essential 15IRX11 · 83SC0026GE | i5-13450HX (Raptor Lake) | 16 ГБ DDR5 | 15,6" FHD | RTX 5060 (65 Вт) | **1117,99 €** · expert (14) — [карточка](https://www.idealo.de/preisvergleich/OffersOfProduct/207948303_-loq-essential-15-83sc0026ge-lenovo.html) | Kaufland 1163,86 €; eBay 1169,99 € | 999,00 € (22.06) · 84 (последний раз 31.07) | 1×16 + слот (PSREF). ≈ 1306–1362 € | candidates-gpu |
| MSI Katana 15 · B13VFK-081 | i7-13620H (Raptor Lake-H) | 16 ГБ | 15,6" FHD 144 Гц | RTX 4060 | **1199,00 €** · easynotebooks (14); 1199,01 € notebook.de — [карточка](https://www.idealo.de/preisvergleich/OffersOfProduct/202303564.html) | МП от 1372,86 € | 1199 € · 0 | RTX 40 — нет декодирования 4:2:2. Раскладка неизвестна | нет |
| Acer Nitro V15 · ANV15-52-50S2 (NH.QZ9EG.002) | i5-13420H (Raptor Lake-H) | 16 ГБ | 15,6" FHD 165 Гц | RTX 5050 | **1205,10 €** · Galaxus (30); 1207,99 € NBB (30) — [карточка](https://www.idealo.de/preisvergleich/OffersOfProduct/206783922_-nitro-v15-anv15-52-50s2-acer.html) | heinzsoft 1281,90 € (условная); eBay 1318,99 € | 998,99 € (22.08) · 155 (последний раз 25.09) | 2×8 DDR4 (notes) → комплект 2×16. Выше 1250 € | candidates-gpu |
| MSI Cyborg 15 · B2RWFKG-2380 | Core 7 240H (Raptor Lake-H Refresh) | 16 ГБ | 15,6" FHD 144 Гц | RTX 5060 | **1206,99 €** · nullprozentshop; 1207,99 € NBB (30) — [карточка](https://www.idealo.de/preisvergleich/OffersOfProduct/207207802.html) | eBay 1318,99 €; Kaufland 1773,99 € | 1199 € · 0 | У платформы 2×8 (NBC, notes) | P/N новый |
| Medion Erazer Deputy 15 P1 · **30039883** | Core 7 250H (codename на idealo не указан) | 16 ГБ DDR5 | 15,6" FHD 144 Гц | RTX 5060 | **1206,99 €** · nullprozentshop; 1207,99 € Galaxus / NBB (30); 1235,99 € Cyberport — [карточка](https://www.idealo.de/preisvergleich/OffersOfProduct/206756972_-erazer-deputy-15-p1-30039883-medion.html) | heinzsoft 1281,90 € (условная); Amazon МП 1347,28 € | 1079 € (02.04) · 10 (последний раз 01.07) | У платформы 2×8 (Medion, notes) | P/N новый |
| Gigabyte Gaming A16 · CVHI3DE894SH | i7-13620H (Raptor Lake-H) | 16 ГБ DDR5 | 16" 1920×1200 165 Гц | RTX 5060 | **1199,00 €** · Coolblue (30) — [карточка](https://www.idealo.de/preisvergleich/OffersOfProduct/206981767.html) | — | 1137 € (03.09) · 0; за год — 898,32 € | 1×16 + слот (notes). ≈ 1387–1443 € | candidates-gpu |
| **Acer Nitro V15 · ANV15-52-74JQ** | i7-13620H (Raptor Lake-H) | **32 ГБ** | 15,6" FHD | RTX 5050, 8 ГБ GDDR7 | **1199,00 €** · acer.com/de-de — это **цена с ваучером** («Preis inkl. Gutschein»), других предложений нет — [карточка](https://www.idealo.de/preisvergleich/OffersOfProduct/206982073_-nitro-v15-anv15-52-74jq-acer.html) | — | за год: минимум 1199 € (10.11.2025), в среднем 1332,61 €, максимум 1399 € · 0 | **Это и есть «ANV15-52 с 32 ГБ» из notes**: теперь известен P/N. 2×16 или 1×32 — idealo не пишет; у платформы 2 слота DDR4 → вероятно 2×16. **Проверить даташит** | семейство (без P/N) |
| Monsternotebook Tulpar T6 V3.5 | i7-14700HX (Raptor Lake-HX Refresh) | 16 ГБ DDR5 | 16" 1920×1200 165 Гц | RTX 5060 | **1289,00 €** · tulparnotebook.de (30) — [карточка](https://www.idealo.de/preisvergleich/OffersOfProduct/207329994_-tulpar-t6-v3-5-monsternotebook.html) | Kaufland 1223,10 € (маркетплейс, условная); Amazon МП 1299 € | 1069 € (11.03) · 1 | У обычного магазина цена выше 1250 € | семейство (T6 V3.5.2) |
| Medion Erazer Deputy P60 (P60i) · MD62688 | i7-13620H (Raptor Lake-H) | 16 ГБ DDR4 | 15,6" FHD | RTX 4060 | **не найдено у обычного магазина** | euronics МП 1242,99 € — [карточка](https://www.idealo.de/preisvergleich/OffersOfProduct/204800555.html) | 1019,99 € (02.04) · 97 (последний раз 19.08) | RTX 40, раскладка неизвестна | нет |
| Medion Erazer Deputy 15 P1 · 30039869 | Core 5 210H (Raptor Lake-H Refresh) | 16 ГБ | 15,6" FHD 144 Гц, без ОС | RTX 5060 | **1244,70 €** · Galaxus (30); 1299,95 € medion.com (14); 1305,99 € Cyberport — [карточка](https://www.idealo.de/preisvergleich/OffersOfProduct/206756952_-erazer-deputy-15-p1-30039869-medion.html) | Kaufland 1369,55 € | 899 € (12.03) · 35 (последний раз 19.09) | 2×8 (Medion, notes) → комплект 2×16 ≈ 1720 € | candidates-gpu |

Второй листинг «Medion Scout 15 E1 30039767» (9 предложений, ab 999 €) — без собственной карточки, дубль первой строки.

### B. Отсеяно

| Что | Цена | Почему |
|---|---|---|
| MSI Cyborg 15 B2RWFKG-068 | 1079,10 € (Amazon, 14) — [карточка](https://www.idealo.de/preisvergleich/OffersOfProduct/206837107_-cyborg-15-b2rwfkg-068-msi.html) | **SSD 512 ГБ** по datasheet idealo. В candidates-gpu указан 1 ТБ (по billiger) — **расхождение** |
| Acer Nitro V15 ANV15-52-714T | 1119,53 € (Amazon МП) — [карточка](https://www.idealo.de/preisvergleich/OffersOfProduct/206936808_-nitro-v15-anv15-52-714t-acer.html) | 512 ГБ, DDR4 |
| MSI Katana 15 B13VFK-1877 | ab 1150,89 € | i5-13420H, 512 ГБ |
| Gigabyte Gaming A16 3VHK3DE894SH | ab 1099 € | AMD Ryzen 7 260 |
| MSI Cyborg 15 4711377237178 / 4711377653374 | 1229 € | 8 ГБ ОЗУ |
| Б/у: Gigabyte G5 KF5-H3DE554KH, G6 KF-H3DE854KH, Aorus 15 BKF-H3DE754SD | 1000,92 / 1099 / 1195,99 € | Б/у |

## Выводы: что нового по сравнению с REPORT.md и candidates-gpu.md

1. **Ветка с дискреткой: в пределах 1100 € с памятью по-прежнему пусто** (idealo подтверждает вывод облачной сессии).
   Формально укладывается только Tulpar T5 V23.4 (899 €, если окажется 1×16 + свободный слот DDR4). Но его продаёт только Amazon Marketplace, процессор Alder Lake-P, а RTX 4060 не декодирует 4:2:2 — не рекомендую.
2. **Acer «ANV15-52 с 32 ГБ за 1199 €» — это `ANV15-52-74JQ`.** На idealo его продаёт только acer.com, и 1199 € — цена с ваучером. За год дешевле 1199 € он не бывал (в среднем 1333 €). Раскладку 32 ГБ проверить по даташиту.
3. **Цены из candidates-gpu, перепроверенные на idealo:**
   - Nitro V15 50S2: сейчас 1205,10 € (Galaxus), а не «999 € у Cyberport». 22.08 падал до 998,99 €.
   - LOQ Essential 83SC0026GE: 1117,99 € (expert). Новый близнец 83SC000EGE — 1111 € (berlet).
   - Deputy 15 P1 30039869: 1244,70 € (Galaxus); у Cyberport 1305,99 €, а не 1139 €.
   - Scout 15 E1: 1006,99–1007,99 € — совпадает.
   - Gigabyte CVHI3DE894SH: 1199 € (Coolblue) — совпадает.
   - ASUS V16 V3607VM-RP011: 1071,39 € — совпадает, раскладка клавиатуры испанская.
   - Gigabyte CTHI3DE894SH (RTX 5050): 1115,54 € у otto. 151 день из 182 стоил ≤ 1100 €, за год минимум 831 €. Но с памятью всё равно выше 1100 €.
4. **Новые P/N с RTX до 1250 €** (все с 16 ГБ, в бюджет с памятью не проходят): MSI Katana 15 B13VFK-081 (RTX 4060, 1199 €), MSI Cyborg 15 B2RWFKG-2380 (1206,99 €), Medion Deputy 15 P1 30039883 (Core 7 250H, 1206,99 €), Medion Deputy P60 MD62688 (только маркетплейс), Tulpar T5 V23.4 (только маркетплейс).
5. **Расхождение:** у MSI Cyborg 15 B2RWFKG-068 idealo указывает 512 ГБ, а не 1 ТБ.
6. **Ветка «16 ГБ + планка», новое:**
   - **HP OmniBook 7 AI 16-ay0750ng** — Core Ultra 5 225H (**Arrow Lake-H**), 16 ГБ, 1 ТБ, 16" — 755,15 € на hp.com (возврат 14 дней). Если там 1×16 + свободный слот, итог ≈ 943–999 € — **лучший процессор в бюджете среди всех «+ планка»**. Приоритет №1 для проверки по даташиту HP (а также риск HEVC, как у всех HP).
   - ASUS Vivobook 15 OLED X1505VA-MA884W (i9-13900H, 2,8K OLED, 807,99 € у NBB) — проверить, не 16 ГБ ли распайки + свободный слот.
   - HP 15-fd1555ng (783,17 €) и V15 G5 83GW00A9GE (598,98 €) — цены из REPORT подтвердились.
7. **Планки:** на idealo DDR5 16 ГБ есть от 187,56 €, но только на маркетплейсе Galaxus; DDR4 16 ГБ — от 97,50 €, тоже только маркетплейсы. Цены у обычных магазинов для планок я не искал.
8. **Ограничения скана:** в фильтры не попадают карточки серий без характеристик (например, «HP OmniBook 7 AI 16», «MSI Katana 15 B13», «Lenovo LOQ 15 G10 2025»). Без собственной карточки остаются и листинги с одним предложением — у них нет истории цен. API истории примерно после 20 карточек отвечал 404.
