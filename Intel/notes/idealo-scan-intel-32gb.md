# idealo.de: широкий скан Intel · 32 ГБ · 1 ТБ · 15–16" — до 1250 €

_Проверено в Chrome пользователя 30.09.2026 (все цены — этой даты, «итог с доставкой»). Капчи не было._
_Карточка idealo: `https://www.idealo.de/preisvergleich/OffersOfProduct/<id>.html` (id — в последней колонке)._
_«МП» — маркетплейс (Kaufland, Amazon Marketplace, eBay, OTTO-/Galaxus-Marktplatzhändler, euronics-Marktplatz, metro). R30/R14 — срок возврата, если idealo его показывает._

## Итог коротко

1. **Новое и важное: HP OmniBook 7 AI 16-ay0770ng** — Core Ultra 7 255H (**Arrow Lake-H**), 32 ГБ, 1 ТБ, 16" WUXGA 300 нит, TB4, HDMI 2.1, 70 Втч —
   **979,30 €**, hp.com (DE), единственный продавец, возврат 14 дней, доставка до 10.10. В `notes/` и `REPORT.md` его нет
   (в `sweep-dell-hp.md`: «Intel-версий 16" на billiger нет»). **Раскладка памяти неизвестна** (распайка или SO-DIMM) и HEVC у потребительских HP не проверен — нужен даташит HP.
2. **Acer Aspire Go 16 `NX.JS9EG.005` (AG16-71P-97GF) сейчас 849,00 €** у technik-brandenburg.de (в REPORT — 899 €). У technowelt24 и expert — 899,00 €.
   Магазин маленький (5,0 ★, 33 отзыва), срок возврата idealo не показывает.
3. Новые SKU на Raptor Lake-H (i9-13900H / i7-13620H): AG15-71P-75W4 (979 €, только МП), A15-51M-94GX (999 €, только МП), A15-51M-919A `NX.JCJEG.00T` (1044,10 €).
   Лучше -97GF ни один не выглядит: тот же или слабее CPU, дороже, у A15-51M память, вероятно, распаяна.
4. **Core Ultra H + 2×16 SO-DIMM с завода + 1 ТБ за ≤ 1100 € на idealo не найдено.**
5. **Фильтры idealo теряют товары:** у `83HS00BLGE`, `MD600023`, `22AY004XGE`, `21UR005AGE` нет поля «Prozessorhersteller», поэтому фильтр Intel их не показывает.
   Я прошёл те же фильтры без Intel (скан B) и без RAM (скан C), чтобы их поймать.
6. **История цен не снята:** `/price-chart/sites/1/products/<id>/history` отвечал 404 на всех карточках, даже на собственный запрос страницы (блок графика пустой).
   Минимумы за полгода по idealo — «не найдено на idealo».

## Использованные URL фильтров

| Скан | Фильтры (id) | URL | Товаров | Пройдено страниц (до цены) |
|---|---|---|---|---|
| A | 15 Zoll + 16 Zoll + 1 TB + 32 GB + Intel | [3751F699493-1568565-2682401-7612877-107335535](https://www.idealo.de/preisvergleich/ProductCategory/3751F699493-1568565-2682401-7612877-107335535.html?sortKey=minPrice) | 592 | 1–2 (до 1297,73 €) |
| A0 | 1 TB + 32 GB + Intel (без размера) — сверка | [3751F2682401-7612877-107335535](https://www.idealo.de/preisvergleich/ProductCategory/3751F2682401-7612877-107335535.html?sortKey=minPrice) | 1110 | 1–4 (до 1313,89 €): новых 15–16" нет |
| B | 15 + 16 Zoll + 1 TB + 32 GB, **без Intel** (AMD/Apple/Snapdragon отсеял по тексту) | [3751F699493-1568565-2682401-7612877](https://www.idealo.de/preisvergleich/ProductCategory/3751F699493-1568565-2682401-7612877.html?sortKey=minPrice) | — | 1–5 (до 1281 €) |
| C | 15 + 16 Zoll + 1 TB + Intel, **без RAM** (искал карточки без поля RAM) | [3751F699493-1568565-2682401-107335535](https://www.idealo.de/preisvergleich/ProductCategory/3751F699493-1568565-2682401-107335535.html?sortKey=minPrice) | 1145 | 1–9 (до 1299 €) |

- id фильтров: **16 Zoll = 1568565**, **15 Zoll = 699493** (в заголовке иногда «15,6 Zoll»), Intel = 107335535, 32 GB = 7612877, 1 TB = 2682401.
- Пагинация: суффикс `I16-<15×(N−1)>` перед `.html`, например стр. 2 = `...107335535I16-15.html?sortKey=minPrice` (36 товаров на странице).
- Скан C дал только товары без 32 ГБ или б/у: Tarox Modula X16 (id 208069174, 1228,97 €, по оферте Core Ultra 5 125H, **16 ГБ**), OmniBook X Flip 16-as0773ng (б/у), Yoga Slim 7 15 83HM0069GE (б/у).

## 1. Процессор Raptor Lake-H и новее — новые, ≤ 1250 €

Отсортировано по цене. «Известен» — есть в `REPORT.md` или облачных заметках `notes/`.

| P/N | Модель | CPU (кодовое имя по idealo) | ОЗУ / SSD | Экран · GPU | Лучшая цена | Магазин · замечания | Известен | id |
|---|---|---|---|---|---|---|---|---|
| `MD600023` | Medion E15433 | i7-13620H (нет в карточке; Raptor Lake-H) | 32 DDR4 / 1 ТБ | 15,6" FHD · UHD | **699,97 €** | expert.de; МП kaufland 857,99 | да (REPORT, условный: раскладка не подтверждена) | 208688812 |
| `NX.JS9EG.005` | Acer Aspire Go 16 AG16-71P-97GF | i9-13900H (Raptor Lake-H) | 32 DDR5 / 1 ТБ | 16" WUXGA · Iris Xe | **849,00 €** | technik-brandenburg.de (33 отзыва); technowelt24 899, expert 899; МП kaufland 915,40 (R14), OTTO/expert 939,99 (R30) | да (REPORT №2: 899 €) | 209373295 |
| `NX.JS9EG.00C` | Acer Aspire Go 16 AG16-71P-95Q7 | i9-13900H (Raptor Lake-H) | 32 / 1 ТБ | 16" WUXGA (idealo: 120 Гц, даташит: 60 Гц) · Iris Xe | **906,99 €** | nullprozentshop.de; notebooksbilliger 907,99 (R30), Galaxus 907,99 (R30), JACOB 943,05 | да (REPORT №3) | 209220720 |
| `NX.JS9EG.00B` | Acer Aspire Go 16 AG16-71P-90SZ | i9-13900H (Raptor Lake-H) | 32 / 1 ТБ | 16" WUXGA 120 Гц · Iris Xe | **951,46 €** | easynotebooks.de (R14); notebook.de 951,47; МП euronics 953,99 | да | 209421477 |
| — | Acer Aspire Go 15 AG15-71P-75W4 | i7-13620H (Raptor Lake-H) | 32 / 1 ТБ | 15,6" FHD · UHD | 979,00 € (МП) | только Galaxus-Marktplatzhändler (R30) | **нет** | 206147182 |
| — (HP P/N на idealo нет) | **HP OmniBook 7 AI 16-ay0770ng** | **Core Ultra 7 255H (Arrow Lake-H)** | 32 (тип не указан) / 1 ТБ | 16" WUXGA 300 нит · Arc 140T; TB4, HDMI 2.1 | **979,30 €** | hp.com (DE), R14, доставка до 10.10; других продавцов нет | **нет** | 206602335 |
| `83HS00BLGE` | Lenovo IdeaPad Slim 5 16IRH10 | i7-13620H (нет в карточке; Raptor Lake-H) | 32 DDR5 / 1 ТБ | 16" WUXGA 300 нит · UHD | **995,00 €** | technowelt24.de, expert.de, expert-technomarkt.de; МП kaufland 989,05 (R14), eBay/expert 995,98 (R30) | да (REPORT №1) | 209881995 |
| `NX.JCJEG.00K` | Acer Aspire 15 A15-51M-93FG | i9-13900H (Raptor Lake-H) | 32 LPDDR5 распайка / 1 ТБ | 15,6" FHD · Iris Xe, TB4 | 1199,00 € (обычный магазин) | acer.com; **МП Amazon 999,00** («nur noch 6»); Galaxus-МП/Kaufland 1217 | да (REPORT №5) | 206565041 |
| — | Acer Aspire 15 A15-51M-94GX | i9-13900H (нет в карточке) | 32 «DDR5» (по idealo) / 1 ТБ | 15,6" FHD · Iris Xe, TB4 | 999,00 € (МП) | только euronics.de (Marktplatz) | **нет** | 208669537 |
| `NX.BMCEG.001` | Acer TravelMate P2 TMP215-75-G2-TCO-70VW | Core Ultra 7 155H (Meteor Lake) | 32 (**1×32** по notes) / 1 ТБ | 15,6" FHD · Arc | 1004,98 € | playox.de (R30); МП eBay 1050,92 | да (ловушка 1×32) | 207195151 |
| `NX.BMGEG.002` | Acer TravelMate P2 TMP215-75-G2-TCO-789W | Core Ultra 7 155H (Meteor Lake) | 32 DDR5 (**1×32** по notes) / 1 ТБ | 15,6" FHD · Arc | 1005,88 € | playox.de (R30); МП eBay 1051,10 | да (ловушка 1×32) | 209172103 |
| EAN 4049998792258 | ASUS ExpertBook P1 P1503CVA-S72336 | Core 5 210H (= i5-13420H, Raptor Lake-H) | 32 DDR5 / 1 ТБ — сборка one.de | 15,6" FHD 250 нит | 1009,99 € (МП) | только OTTO/one.de (R30) | да | 209554393 |
| `NX.JCJEG.00T` | Acer Aspire 15 A15-51M-919A | i9-13900H (нет в карточке) | 32 «DDR5» (по idealo) / 1 ТБ | 15,6" FHD · Iris Xe, TB4 | **1044,10 €** | e-tec.at (DE); 0815.eu 1099,00 (R30) | **нет** | 208438558 |
| `NX.JS9EG.009` | Acer Aspire Go 16 AG16-71P-96VZ | i9-13900H | 32 DDR5 / 1 ТБ | 16" WUXGA 120 Гц | 1069,00 € (МП) | только Amazon Marketplace | да | 207726539 |
| EAN 4049998799219 | ASUS Vivobook 16 X1607CA-MB120 | Core Ultra 7 255H (Arrow Lake-H) | 32 DDR5 = 16 распайка + 16 SO-DIMM, сборка one.de / 1 ТБ | 16" WUXGA 300 нит | 1069,99 € (МП) | только OTTO-Marktplatzhändler (R30) | да (B-список) | 213296258 |
| `NX.JS9EG.00A` | Acer Aspire Go 16 AG16-71P-952H | i9-13900H | 32 / 1 ТБ | 16" WUXGA 60 Гц | 1089,00 € (МП) | только Amazon Marketplace | да | 208008728 |
| `21SK0083GE` | Lenovo ThinkBook 16 G8 IAL | Core Ultra 5 225U (idealo: Arrow Lake-U) | 32 DDR5 / 1 ТБ | 16" WUXGA 300 нит · Graphics | **1122,00 €** | jb-computer.de (R30); МП eBay 1179,28 | да (REPORT №6) | 206151171 |
| `NX.JP1EG.007` | Acer Aspire 16 AI A16-52M-75LW | Core Ultra 7 258V (Lunar Lake) | 32 LPDDR5 распайка / 1 ТБ | 16" 2048×1280 120 Гц 500 нит · Arc 140V | 1146,86 € | electronis.de; МП Amazon 1143,00 | да | 207120152 |
| — | Acer Aspire 5 A515-58GM-50RV | i5-13420H (Raptor Lake-H) | 32 DDR4 / 1 ТБ | 15,6" FHD · **RTX 2050 4 ГБ** | 1169,10 € | joybuy.de (R30) | нет | 204987642 |
| `83SC0028SP` | Lenovo LOQ Essential 15 | i5-13450HX (нет в карточке) | 32 / 1 ТБ | 15,6" FHD 144 Гц · **RTX 5050** | 1181,86 € | Amazon (R14); «SP» — испанский SKU (раскладка?) | нет (серия есть в candidates-gpu) | 209617011 |
| — | Acer Nitro V15 ANV15-52-74JQ | i7-13620H (Raptor Lake-H) | 32 / 1 ТБ | 15,6" FHD · **RTX 5050 8 ГБ**, TB4 | 1199,00 € (условная) | acer.com, «Preis inkl. Gutschein» | нет (серия ANV15-52 есть) | 206982073 |
| — | Acer Aspire 15 A15-51M-95T2 | i9-13900H (Raptor Lake-H) | 32 LPDDR5 распайка / 1 ТБ | 15,6" FHD | 1199,00 € (МП) | только Amazon Marketplace | нет | 206565043 |
| `C7SR2ES#ABD` | HP ProBook 4 G1i 16 | Core Ultra 5 225H (Arrow Lake-H) | 32 / 1 ТБ | 16" WUXGA 400 нит · Arc 130T | 1207,99 € | notebooksbilliger (R30); МП eBay 1318,99 | да (**HEVC выключен**) | 208030552 |
| `21UR005AGE` | Lenovo ThinkBook 16 G9 | Core Ultra 5 325 (нет в карточке; Panther Lake) | 32 / 1 ТБ | 16" WUXGA 400 нит · Arc | 1209,80 € | klarsicht-it.de; МП Galaxus 1271 | да | 209497615 |
| `22AY004XGE` | Lenovo ThinkPad E16 Gen 3 | Core Ultra 5 228V (Lunar Lake) | 32 LPDDR5X распайка / 1 ТБ | 16" 2560×1600 120 Гц · Arc 130V | 1207,78 € (МП) | только Amazon Marketplace; обычный магазин — 1584,24 (techpointonline) | да (REPORT №9) | 209382346 |
| `22AY004VGE` | Lenovo ThinkPad E16 Gen 3 | Core Ultra 5 228V (Lunar Lake) | 32 LPDDR5X / 1 ТБ | 16" WUXGA 300 нит | 1242,62 € | galaxus.de (R30); МП Amazon 1447,81 | да | 209221694 |
| `21MS004SGE` | Lenovo ThinkBook 16 G7 IML | Core Ultra 5 125U (Meteor Lake) | 32 DDR5 / 1 ТБ | 16" WUXGA 300 нит | 1245,58 € (МП) | только Amazon Marketplace (французская оферта) | да | 204414891 |
| `21MA000RGE` | Lenovo ThinkPad E16 Gen 2 | Core Ultra 5 125U (Meteor Lake) | 32 / 1 ТБ | 16" WUXGA 300 нит | 1194,28 € (МП) | МП Amazon; обычный магазин — 1308,34 (techpointonline) | да | 204203147 |
| `NX.BLMEG.006` | Acer TravelMate P2 TMP215-55-G2-TCO-74DE | Core Ultra 7 255U (Arrow Lake-U) | 32 DDR5 / 1 ТБ | 15,6" FHD · Arc | 1253,90 € (ab 1249) | notebooksektor.de; МП eBay 1396 | нет (P/N) | 206829397 |
| — | HP OmniBook X Flip 16-as0000sl | Core Ultra 7 258V (Lunar Lake) | 32 распайка / 1 ТБ | 16" 1920×1200 · без ОС | 1029,99 € (МП) | только eBay; итальянский SKU, **QWERTY UK** | нет | 208950074 |
| — | Monsternotebook Tulpar A7 V16.2.1 | i7-13700HX | 32 DDR5 / 1 ТБ | idealo: 15,6", оферта: **17,3"** 144 Гц · RTX 5050 | 1115,10 € (МП) | только Kaufland | нет | 210008163 |

## 2. Слабые CPU (Raptor Lake-U, Core 5/7 1xxU, Alder Lake, N-серия, Celeron) — новые, ≤ 1250 €

Для монтажа 4K не годятся или сильно хуже вариантов из раздела 1. Большинство — сборки магазинов (CSL, Captiva, EAN-листинги с «+ MS Office»).

| P/N · модель | CPU (кодовое имя) | Цена | Магазин | Известен | id |
|---|---|---|---|---|---|
| CSL R'Evolve C15 v3 (EAN 4061474199696) | N200 (Alder Lake-N) | 489,89 € | otto.de (R30) | серия упоминается | 203482425 |
| CSL R'Evolve C15 v4 92332 | N100 (Alder Lake-N) | 623,90 € | csl-computer.de | нет | 205167946 |
| CSL R'Evolve C16 92685 | i5-1235U (Alder Lake-P), DDR4 | 651,52 € | otto.de (R30) | нет | 205776112 |
| CSL R'Evolve C15 v4 92356 | N100 | 673,90 € (МП Amazon 619) | csl-computer.de | нет | 205167950 |
| CSL R'Evolve C16 92709 | i5-1235U | 700,59 € | otto.de (R30) | нет | 205776124 |
| CSL R'Evolve C15 v3 (EAN 4061474199788) | N200 | 743,90 € | csl-computer.de | нет | 203482434 |
| Captiva Business/Office I10-0814GE | i5-1235U (Alder Lake-P) | 780,42 € | nexoc-store.de | да | 210052572 |
| Acer Aspire Go 15 AG15-72P-591H | Core 5 120U (Raptor Lake-U Refresh) | 799,00 € (МП) | Amazon Marketplace | нет | 209058647 |
| `NX.JTGEG.00P` Acer Aspire Go 16 AG16-71P-70RK | Core 7 150U (Raptor Lake-U Refresh) | 857,99 € | notebooksbilliger (R30) | да (ловушка) | 209225890 |
| Captiva Power Starter I81-316 / Business I10-0771GE | i7-1255U (Alder Lake-P) | 873,13 € | nexoc-store.de | I10-0771GE — да | 203818151, 210052561 |
| HP 250 G10 8D404ES-32G-1T-W11P (сборка) | i5-1335U (Raptor Lake-U) | 879,00 € (МП) | Kaufland | нет | 203505000 |
| Captiva Power Starter I81-317 | i7-1255U | 892,00 € | voelkner.de (R30) | да | 203818152 |
| Captiva Business/Office I10-0772GE | i7-1255U | 892,50 € | nexoc-store.de | нет | 210052562 |
| Acer Aspire Go 15 AG15-72P-73PW | Core 7 150U | 899,00 € | mediamarkt.de (R30) | нет | 210690819 |
| Medion E15443 30040188 | i5-1334U (Raptor Lake-U) | 905,95 € (МП) | Amazon Marketplace | да | 205982540 |
| Captiva Business/Office I10-0777GE | i7-1255U | 916,02 € | nexoc-store.de | да | 210052568 |
| Acer Aspire Go 16 AG16-71P-7607 | Core 7 150U | 939,64 € (МП euronics 937,64) | allesfuerzuhause.de | да | 213350111 |
| HP 250 G10 (EAN 0197192797228) | i7-1355U | 949,31 € (МП) | Amazon Marketplace | нет | 208144215 |
| HP 15 (EAN 4260260630454) | i7-1355U | 969,00 € (МП) | eBay | нет | 207229450 |
| Lenovo V15 G5 IRL T-LM-V15G5-C313-32-T1-W / S-LM-…-W / T-LM-…-WO / S-LM-…-WO (сборки, «RAM/SSD konfig.») | i3-1315U | 969,00 / 999,01 / 1019,00 / 1049,00 € (все МП) | eBay / metro / Galaxus / metro | нет | 208462810, 209449282, 208462814, 209449284 |
| Acer Aspire Go 16 (EAN 4711121259340 / 4711121259982) | i3-1305U | 1019,00 / 1069,00 € (МП) | Galaxus-Marktplatzhändler | нет | 211852746, 211852747 |
| HP 250 G10 853S0ES-32G-1T-W11P / EAN 7427307801544 (сборки) | i7-1355U | 1039,90 € (МП) | Kaufland | нет | 207104350, 205898399 |
| ASUS Vivobook X1605 (EAN 4262490589731, + Office; в оферте «Ryzen 5») | i3-1315U | 1049,00 € (МП) | Kaufland | нет | 207889689 |
| Lenovo V15 (EAN 4262490582312, + Office; в оферте N150) | Celeron N4500 | 1049,00 € (МП) | Kaufland | нет | 207229508 |
| HP 250 G10 I-HM-H25-V11-I5-32-T1-W (сборка) | i7-1355U | 1069,00 € (МП) | eBay | нет | 211271584 |
| Lenovo V15 G4 (EAN 725844015798, + Office) | i5-1235U | 1099,00 € (МП) | Kaufland | нет | 203757791 |
| HP 250 G10 (EAN 4260634442805, + Office; в оферте Core 7 150U) | i7-1355U | 1149,00 € (МП) | Kaufland | нет | 205898495 |
| Acer Aspire 15 A15-51M-73QW | Core 7 150U | 1149,00 € (МП) | Galaxus-Marktplatzhändler | нет | 204606417 |
| Acer Aspire Go 16 (EAN 4262555852534 = AG16-71P-353M + Office) | i3-1305U | 1149,00 € (МП) | Amazon Marketplace | нет | 211852801 |
| Captiva Power Starter I91-484UK / -735IT / -486UK / -734IT (UK/IT-раскладка) | i5-1335U / i7-1355U | 1174,43 € | otto.de (R30) | нет | 210010208, 208653180, 210010209, 208653179 |
| Captiva Business/Office I10-0707GE / -0708GE; Power Starter I91-104 / -099 | i5-1335U / i7-1355U | 1178,93 € | nexoc-store.de | нет | 210052533, 210052534, 206333980, 206333904 |
| Captiva Power Starter I91-667CH / -669CH (CH-раскладка) | i5-1335U | 1179,89 € | otto.de (R30) | нет | 210010239, 210010240 |
| Acer TravelMate P2 16 P216-51-G2-TCO-78RY | Core 7 150U | 1229,00 € | galaxus.de (R30) | серия есть | 205580568 |
| Dell Inspiron 15 3530 (EAN 4262490582831; в оферте «Asus X170 17,3"») | i5-1334U | 1249,00 € (МП) | OTTO-Marktplatzhändler | нет | 205730624 |

## 3. Сборки продавцов и листинги-мусор с «нормальным» CPU — не брать

| Модель | CPU | Цена | Почему не брать | id |
|---|---|---|---|---|
| Lenovo V15 G5 T-LM-V15G5-C513-32-T1-W / -WO | i5-13420H (Raptor Lake-H) | 1069 / 1119 € (МП Galaxus) | память доставлял продавец | 208035125, 208142963 |
| Lenovo V15 G4 (EAN 4262490581469) / V15 G4 12500-32-1000 | i5-13420H | 1099 € (МП Kaufland) / 1199 € (МП Galaxus) | сборка + MS Office | 207350936, 204953174 |
| ASUS ExpertBook P1503 (EAN 4262490589243) | i7-13620H | 1099 € (МП OTTO) | в оферте другой ноутбук (Vivobook 16, Ryzen 5 150) | 207283781 |
| HP EliteBook 860 G11 9G0A4ET | Core Ultra 7 155H | 1099 € (МП eBay) | в оферте EliteBook 840 G11 14" QWERTY; у EliteBook 6xx HEVC выключен | 204380277 |
| MSI Creator Z16P B12VE-464FR | i7-12650H + RTX 4050 | 1187,32 € (Amazon) | в оферте Creator M16 с 16 ГБ; французский SKU | 203269797 |
| «Lenovo IdeaPad 1i / 3i Chromebook / IdeaPad 15,6" Touch» | в карточке CU5 135U / 228V, в оферте Pentium N6000, Celeron, i5-1335U 24 ГБ | 438,60 / 474,05 / 959,92 / 1242 € (МП Amazon) | данные карточки не совпадают с офертой | 213600242, 213607401, 213607080, 213609930 |

Б/у (не рассматривал): IdeaPad Slim 5 16 83HS00BMGE (769 €), ThinkPad P15 G1, Surface Book 3, HP 250 G10 ×3, HP OmniBook 5 16-af1177ng, Acer Swift Go SFG16-71-78ZB,
HP Envy x360 16-ac0790ng, HP ProBook 460 G11 9C0H8EA, HP ZBook ×3, EliteBook 860 G9, Dell Precision 7560, Dell XPS 15 9510,
**ASUS Vivobook S16 S3607AA-SH013W** (Core Ultra 7 355, 1140 €, только б/у), Yoga Slim 7 15 83HM0069GE, OmniBook X Flip 16-as0773ng.

## Что проверить дальше (даташиты)

| Модель | Что выяснить | Почему |
|---|---|---|
| **HP OmniBook 7 AI 16-ay0770ng** (979,30 €) | раскладка памяти (распайка LPDDR5x или SO-DIMM 2×16), HP P/N, отключён ли HEVC | единственный Arrow Lake-H с 32/1 ТБ дешевле 1000 € у нормального магазина. Родственный 16-ay0750ng (Core Ultra 5 225H, 16 ГБ, 1 ТБ) — 755,15 € на hp.com ([id 206602486](https://www.idealo.de/preisvergleich/OffersOfProduct/206602486.html)); если там 1×16 + слот — ещё один вариант «+ планка» (его нашёл и скан 16 ГБ) |
| Acer Aspire Go 15 AG15-71P-75W4 (979 €, МП) | P/N NX…, раскладка памяти | новый SKU на i7-13620H; но только маркетплейс и дороже -97GF |
| Acer Aspire 15 A15-51M-94GX (999 €, МП) и A15-51M-919A `NX.JCJEG.00T` (1044,10 €) | распайка LPDDR5 (как у `NX.JCJEG.00K`) или SO-DIMM | idealo пишет «DDR5», но у A15-51M-93FG даташит Acer — «32 GB LPDDR5 onboard» |

## Что нового по сравнению с REPORT.md

- **Новое:** HP OmniBook 7 AI 16-ay0770ng — 979,30 € (Arrow Lake-H, 32/1 ТБ). До проверки раскладки памяти — кандидат в A- или B-список.
- **Цена ниже, чем в REPORT:** `NX.JS9EG.005` — 849,00 € (technik-brandenburg.de) вместо 899 €.
- **Подтверждено на idealo:** `83HS00BLGE` — 995,00 € (technowelt24 / expert), `NX.JS9EG.00C` — 906,99–907,99 €, `NX.JCJEG.00K` — 999 € только у Amazon Marketplace (у Acer — 1199 €),
  `MD600023` — 699,97 € (expert), `21SK0083GE` — 1122,00 € (jb-computer), `22AY004XGE` — 1207,78 € только у Amazon Marketplace (обычный магазин — 1584,24 €).
- **Изменилось:** `21MA000RGE` — у обычного магазина теперь 1308,34 € (ab 1190,28 € — только Amazon Marketplace).
- **Новые SKU без улучшения:** AG15-71P-75W4, A15-51M-94GX, A15-51M-919A (`NX.JCJEG.00T`), A15-51M-95T2, Aspire 5 A515-58GM-50RV (RTX 2050), Nitro V15 ANV15-52-74JQ (RTX 5050, 1199 € с купоном), LOQ Essential 15 `83SC0028SP` (RTX 5050, 1181,86 €).
- **Ловушки 1×32 (TMP215-75-G2 -70VW / -789W) по-прежнему продаются** за ~1005 € (playox).
