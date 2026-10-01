# idealo.de: проверка Lenovo-SKU из разбора Intel

_Проверено 30.09.2026 в Chrome пользователя (Claude in Chrome), карточки idealo открывались по одной. Капчи не было._
_Цена = «inkl. Versand» у обычного магазина; маркетплейс (Amazon MP, Kaufland, eBay, Galaxus-Marktplatz) и «Preis nur mit…/Gutschein» — отдельно._
_История — API графика idealo (`/price-chart/.../history?period=1Y`, дневной минимум idealo, включая маркетплейсы). «Дней ≤1100» — за 01.04–30.09.2026 (183 дня); если данных меньше, указано «из N дней с данными»._
_Около 30.09 днём API истории стал отвечать 404 на все товары (и на самой странице график пропал) — у последних 5 карточек истории нет, повторы не делал, чтобы не долбить сайт._

## Итог коротко

- **В бюджете ≤ 1100 € с 2×16 и 1 ТБ на idealo сейчас только `83HS00BLGE`: 995 € у обычного магазина (989,05 € на Kaufland).** За полгода был ≤ 1100 € каждый день, минимум 899 € (ещё 01–08.09).
- **ThinkBook 16 G8 `21SK0083GE`: 1122 € — совпадает с отчётом.** Последний день ≤ 1100 € — 20.09.
- **`21SK007KGE` сейчас 1399 € (в отчёте 1349 €).** Минимум за 6 мес. на idealo — **910 € (03.09)**, а не 1049 €. Ниже 1100 € был 89 дней, последний раз — 18.09.
- **`22AY004XGE`: цены 909 € в сентябре на idealo нет.** За 6 мес. минимум 1099 € (03.06–14.06), сейчас 1207,78 € только на Amazon MP.
- **`22AY004VGE` (тот же 228V, 1 ТБ, экран WUXGA) почти всё полугодие стоил ≤ 1100 €** (168 из 183 дней, минимум 961,12 € 09.09). Сейчас 1242,62 € на Galaxus — ждать возврата цены.
- **`22AY003XGE` — это 512 ГБ, а не 1 ТБ.** Так в PSREF и в названиях предложений; ошибка в данных карточки idealo. В `idealo-prices.md` он записан как 32/1 ТБ, это неверно.
- **На idealo не найдены:** 83V70037GE, 83GW00AHGE, 83J1006UGE, 83J1006HGE, 83JE014MGE, 83JE00TYGE (плюс доп. 83V70033GE, 83J1006XGE, 21SK008CGE, 21SK008MGE, 21SR0079GE, 21SR004LGE).
- Более дешёвого варианта с 2×16 и 1 ТБ среди «Variante» нет. Близко (B-список, **512 ГБ**): ThinkPad E16 G3 `22AY003WGE` (228V, 32 ГБ распайка) — от 927,91 €. Слот M.2 2280 один, до 1 ТБ; SSD придётся менять самому (цену SSD не проверял).
- Зарядки: 65 Вт USB-C `4X20M26272` — **22,27 €**; 100 Вт USB-C `4X21M37469` — **49,35 €** с доставкой (в отчёте ~41 €); 100 Вт `GX21V43585` — **33,89 €** (alza.de).

## Таблица

| P/N | Модель | CPU · ОЗУ · SSD (карточка idealo) | Лучшая цена (магазин, возврат) · вообще / предл. | Мин. 1 год (дата) | Мин. 6 мес. | Дней ≤1100 | Было в отчёте/notes | Расхождение |
|---|---|---|---|---|---|---|---|---|
| 83HS00BLGE | IdeaPad Slim 5 16IRH10 | i7-13620H · 32 · 1 ТБ | **995,00 €** technowelt24.de (возврат не указан); expert.de 995,00 (14 дн.) · Kaufland MP 989,05 (14) / 7 | 899,00 (27.05; и 01–08.09) — данные с 01.04 | 899,00 | 177 из 177, последний 30.09 | 995 € technowelt24/Expert, 989,05 Kaufland, мин. 899 | нет |
| 21SK0083GE | ThinkBook 16 G8 IAL | Ultra 5 225U · 32 · 1 ТБ | **1122,00 €** jb-computer.de (30); easynotebooks 1122,00 (14) / 15 | 823,52 (23.10.2025) | 881,49 (11.06) | 173, последний 20.09 | 1122 €, мин. 881,50, 171/182 | нет (±1 цент, ±2 дня) |
| 21SK007KGE | ThinkBook 16 G8 IAL | Ultra 7 255H · 32 · 1 ТБ | **1399,00 €** easynotebooks.de (14) / 9 | 910,00 (03.09.2026) | 910,00 (03.09) | 89, последний 18.09 | 1349 €, мин. 1049,01, 76 дн., 18.09 — 1095 | цена +50 €; мин. 910, а не 1049; 89 дней, а не 76 |
| 83V70037GE | IdeaPad Slim 5 16IMH10 | — | **не найден на idealo** (поиск по P/N; нет и в «Variante» IdeaPad Slim 5 16) | — | — | — | ~1059 € (сниппет), 1049,49 Amazon 23.08 | на idealo нет |
| 22AY004XGE | ThinkPad E16 G3 (Lunar Lake) | Ultra 5 228V · 32 распайка · 1 ТБ · 2560×1600 | обычный: techpointonline.de 1584,24 · **Amazon MP 1207,78** / 2 | 925,00 (12.03.2026) | 1099,00 (03.06) | 12 (03.06–14.06) | 1208 € Amazon MP; «21–22.09 — 909,16 €» | 909 € на idealo нет: мин. за 6 мес. 1099 |
| 83V70077GE | IdeaPad Slim 5 16IMH10 | Ultra 5 135H · 24 · 1 ТБ | **871,37 €** cyberport.de (30) / computeruniverse.net (30) / 13 | 830,15 (06.07.2026) — данные с 06.05 | 830,15 | 116 из 116 | 871,37 € Cyberport/computeruniverse | нет |
| 83GW00A9GE | V15 G5 IRL | i5-13420H · 16 · 1 ТБ · FreeDOS | **598,98 €** easynotebooks.de (14); notebooksbilliger 607,99 (30) / 20 | 459,00 (26.01.2026) | 499,00 (01.04) | 183 | 599 € | нет |
| 83GW00AHGE | V15 G5 IRL | — | **не найден на idealo** (поиск по P/N) | — | — | — | «в продаже не найден» | совпадает |
| 21MA000RGE | ThinkPad E16 G2 | Ultra 5 125U · 32 · 1 ТБ | обычный: techpointonline.de 1308,34 · **Amazon MP 1194,28** / 2 | 843,57 (01.06.2026) | 843,57 | 72 из 161, последний 02.07 | ~1190 € Amazon MP, мин. 843,57, 85 дн. | цена и мин. совпадают; дней 72, а не 85 |
| 21MA003RGE | ThinkPad E16 G2 | Ultra 7 155H · 32 · 1 ТБ | **1299,00 €** easynotebooks.de (14) / 9 | 742,63 (11.02.2026) | 1019,58 (01.07) | 9, последний 01.07 | 1299 €, мин. 1092,61 (апрель) | мин. 6 мес. 1019,58 (01.07) |
| 21UR005AGE | ThinkBook 16 G9 IPL | Ultra 5 325 · 32 · 1 ТБ · 400 нит | **1205,00 €** easynotebooks.de (14) (1204,91 у technikdeals24 — условная) / 37 | 1151,00 (16.03.2026) | 1166,99 (02.04) | 0 | 1205 € | нет |
| 22AY004VGE | ThinkPad E16 G3 (Lunar Lake) | Ultra 5 228V · 32 распайка · 1 ТБ · WUXGA | **1242,62 €** galaxus.de (30) / 4 | 961,12 (09.09.2026) | 961,12 | **168**, последний 15.09 | 1242,62 € Galaxus, мин. 961,12 | нет |
| 22AY003XGE | ThinkPad E16 G3 (Lunar Lake) | Ultra 7 258V · 32 распайка · **512 ГБ** (карточка пишет 1 ТБ — ошибка) | **1257,90 €** electronis.de (?) / 6 | 916,00 (15.05.2026) | 916,00 | 5, последний 24.08 | в idealo-prices.md: 32/1 ТБ ab 1251 | **SSD 512 ГБ (PSREF) → не подходит** |
| 21MS004SGE | ThinkBook 16 G7 IML | Ultra 5 125U · 32 · 1 ТБ | только **Amazon MP 1245,58** / 1 | 757,77 (17.12.2025) | 775,65 (03.06) | 98 из 122, последний 14.09 | 1241,58 Amazon MP, мин. 775,65 (03.06), 141 дн., 15.09 | цена/мин. совпадают; дней 98, а не 141 |
| 21MS0054GE | ThinkBook 16 G7 IML | Ultra 7 155H · 32 · 1 ТБ | **1296,00 €** techpointonline.de (?) · Amazon MP 1299 / 2 | 732,99 (19.03.2026) | 1162,80 (27.04) | 0 | 1299 € Amazon MP, 1092,49 (02–03.04), 2/182 | мин. 6 мес. 1162,80, 0 дней |
| 83J1006UGE | IdeaPad Slim 5 16IRH10R | — | **не найден на idealo** (поиск по P/N) | — | — | — | «не найден» | совпадает |
| 83J1006HGE | IdeaPad Slim 5 16IRH10R | — | **не найден на idealo** (поиск по P/N) | — | — | — | «продаётся ли?» | — |
| 21YC000MGE | ThinkPad E16 G4 | Ultra 5 325 · 32 · 1 ТБ · 400 нит | **1566,90 €** notebookstore.de (14) / 37 | 1191,83 (11.07.2026) — данные с 21.04 | 1191,83 | 0 | 1560 €; «740,76 € 01.09 — ошибка» | 740 € на idealo нет |
| 21SR000JGE | ThinkPad E16 G3 (Arrow Lake) | Ultra 5 225U · 32 (**1×32**, PSREF) · 1 ТБ | **1314,02 €** galaxus.de (30) / 17 | 929,91 (16.12.2025) | 1009,95 (17.04) | 5, последний 01.07 | 1314 €, ловушка 1×32 | нет (не подходит) |
| 21KS0001GE | ThinkPad P16s G3 | Ultra 7 155H · 32 · 1 ТБ | **1739,69 €** galaxus.de (30) / 8 | 1249,89 (01.07.2026) | 1249,89 | 0 | 1739,69 Galaxus; «950 € 04–12.05» (billiger) | 950 € на idealo нет |
| 83JE014MGE | LOQ 15IRX10 | — | **не найден на idealo** (поиск по P/N; в общей карточке «LOQ 15 G10 2025» его нет) | — | — | — | 1499 € Lenovo DE | на idealo нет |
| 83JE00TYGE | LOQ 15IRX10 | — | **не найден на idealo** (поиск по P/N) | — | — | — | цены нет | совпадает |
| 83SC0026GE | LOQ Essential 15IRX11 | i5-13450HX · 16 · 1 ТБ · RTX 5060 | **1117,99 €** expert.de (14) / 3 | 959,00 (16.03.2026) | 999,00 (22.06) | 85, последний 31.07 | 1099 € | сейчас 1111 € (+доставка 6,99 €) |
| **доп.** 21SA0049GE | ThinkPad L16 G2 | Ultra 5 225U · 32 · 1 ТБ · 400 нит | **1298,81 €** klarsicht-it.de (?); easynotebooks 1299,14 (14) / 40 | история: API 404 | — | — | 1299 € (lapstars 1304), мин. 1198 | цена совпадает |
| **доп.** 21SA004AGE | ThinkPad L16 G2 | Ultra 7 255U · 32 · 1 ТБ | **1509,86 €** klarsicht-it.de (?); easynotebooks 1510,46 (14) / 37 | история: API 404 | — | — | 1510,61 € Heinzsoft, мин. 999 (22–28.05) | цена совпадает |
| **новый** 22AY003WGE | ThinkPad E16 G3 (Lunar Lake) | Ultra 5 228V · 32 распайка · **512 ГБ** | **927,91 €** klarsicht-it.de (?); notebookstore.de 941,90 (14); easynotebooks 947,90 (14) / 34 | история: API 404 | — | — | не было | B-список, SSD менять самому |
| **новый** 21SK00C2GE | ThinkBook 16 G8 IAL | Ultra 5 225U · 32 · **512 ГБ** | **1099,00 €** easynotebooks.de (14) / 9 | история: API 404 | — | — | «от 1099 €» | с SSD 1 ТБ выйдет > 1100 € |

## Пометки по SKU

- **83HS00BLGE** — всё сходится с отчётом. Держится у 946–995 €, в сентябре несколько дней было 899 € (01–08.09), 901,55 € (20.09 и 27.09). Обычный магазин с понятным возвратом — expert.de (14 дней). У eBay 995,98 € (30 дней, продавец из Берна — маркетплейс).
  Variante (IdeaPad Slim 5 16): 83HS00AAGE 799 € (2×8), 83J10065GE 859 € (Core 5 210H, 24 ГБ), 83V70077GE 864 €, 83V70078GE 873,88 € (135H, **16 ГБ / 512 ГБ**), 83HY/83KU — AMD, 83HU004KGE (776,90 €) не проверял. Подходящего Intel дешевле нет.
  83HS00BMGE (i5-13420H, 32/1 ТБ) — **новых предложений нет**, только б/у от 769 €.
- **21SK0083GE** — в Германии нормальные магазины (jb-computer — 30 дней возврата). Variante ThinkBook 16 G8: 21SK00C2GE 1099 € (32/**512**), 21SK007BGE 1098,98 € (255H 16/512), 21SK006QGE 899 € (16/512), 21SK00K6GE 897,89 € (185H 16/512), 21SK00EEGE 795 € (135H 16/512), конфигурации CTO от 1123 €. **С 32 ГБ и 1 ТБ дешевле нет.** 21SK008CGE / 21SK008MGE (1×16 + 1 ТБ) на idealo нет.
- **21SK007KGE** — 03.09 на idealo был 910 € (в какой день и у кого — по истории не видно). 10–16.09 стоил 1095–1099,99 €, 17.09 — 1245,98 €, 18.09 — снова 1095 €, с 19.09 — от 1236 €, сейчас 1399 €.
- **22AY004XGE** — сейчас только один продавец на Amazon MP (плюс techpointonline за 1584 €). С 15.06 не опускался ниже 1100 €. Цены 909,16 € «21–22.09» из billiger на idealo нет.
  Variante E16 G3 (Lunar Lake 22AY): 004X 1203,78 · 004V 1242,62 · 003X 1251 (512 ГБ!) · 001U 1411,71 (258V, 1 ТБ) · 004W 1599 (258V, 1 ТБ, WQXGA) · 003W 923,61 (228V, **512 ГБ**) · 001V 964 и 00A5 992,63 (16 ГБ) · 002P 1014 (16/512).
- **22AY004VGE** — лучший кандидат для «ждать» в B-списке: 1 ТБ, почти всё полугодие стоил ≤ 1100 €, 09.09 — 961,12 €. Экран простой (WUXGA 300 нит), в отличие от 004X.
- **22AY003XGE** — PSREF ([страница](https://psref.lenovo.com/Detail/ThinkPad/ThinkPad_E16_Gen_3_Intel?M=22AY003XGE)): «512GB SSD M.2 2242», WUXGA 300 нит. В характеристиках idealo записан 1 ТБ — это ошибка. **Не подходит.**
- **22AY003WGE (новый)** — 32 ГБ LPDDR5X, 512 ГБ. По спецификации PSREF у Lunar Lake «one M.2 2280 PCIe 4.0 x4 slot», максимум 1 ТБ ([PDF](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_E16_Gen_3_Intel/ThinkPad_E16_Gen_3_Intel_Spec.pdf)). Итог = ~928–948 € + SSD 1 ТБ 2280 (цену не проверял). Годится только для B-списка.
  → PSREF по MTM проверен 30.09.2026 (curl, [PDF](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=22AY003WGE&country_code=DE)): 228V, «32GB Soldered LPDDR5X-8533, MoP», «512GB SSD M.2 2242», «one M.2 2280 PCIe 4.0 x4 slot», «up to 1TB»; экран 16" WUXGA IPS 300 нит 45 % NTSC 60 Гц; 2× TB4 (второй — «Optional Ports (configured)»), HDMI 2.1, RJ45; 64 Втч; 65 Вт USB-C в комплекте; 1,62 кг; гарантия 1 год. То есть это 22AY004VGE с SSD 512 ГБ. С Kingston NV3 1 ТБ (142,89 €, Alternate — `browser-check-geizhals-idealo.md`, п. 2.9) итог **1070,80 €**.
- **83V70077GE** — 24 ГБ; цена совпадает с отчётом. Идёт без зарядки (по отчёту), 65 Вт USB-C — 22,27 €. Итог с планкой — считать по актуальной цене планки 16 ГБ DDR5 (другой агент).
- **83V70037GE / 83V70033GE** (185H, 2×16) — на idealo карточек нет. В «Variante» IdeaPad Slim 5 16 из 83V7 есть только 0077 и 0078.
- **83GW00A9GE** — раскладка памяти по-прежнему неизвестна. Variante V15 G5: 83GW00HMGE 832,89 € (2×16, **512 ГБ**), 83GW00KKGE 767,96 € (Core 7 240H, 16/512), «T-LM-V15G5-…-32-…» 999–1069 € — это сборки магазина с доставленной памятью, не заводские.
- **21MA000RGE / 21MA003RGE** — E16 G2. Variante: 21MA001YGE 1099 € (125U 16/512), 21MA000HGE 997,70 € (8/256), 21MA002NGE 1173,29 €, 21MA000PGE 1490,40 €, 21MA004UGE 1699,01 € (155H, 2,5K); конфигурацию 21MA002NGE (1173,29 €) не проверял. Среди проверенных с 32/1 ТБ дешевле 1190 € нет. 21MA000RGE — фактически только Amazon MP.
- **21UR005AGE** — Variante ThinkBook 16 G9: 21UR0059GE 1173,79 € (325, 32/**512**), 21UR0057GE 999,98 € (355, 16/512), 21UR0002GE 953,63 € (325, 16/512), 21UR0058GE 1499,98 € (355, 32/1 ТБ), 21UR005WGE 1429 € (355, 32/512). 21UT — AMD. Дешевле с 32/1 ТБ нет.
- **21MS004SGE** — единственное предложение Amazon MP с французским названием («Ordinateur Portable») — **возможна раскладка AZERTY**, проверить до покупки. Variante ThinkBook 16 G7: 21MS0047GE 1099,01 € и 21MS004NGE 1222 € — 16/512; 21MS004HGE (1099,01 €) не проверял; 21MW — AMD.
- **21MS0054GE** — techpointonline.de 1296 €; Amazon MP 1299 €.
- **21YC000MGE** — Variante E16 G4: 21YC0008GE 1118,81 € (512 ГБ по notes), остальные 21YC дороже; 21Y4 / 21YE — не Intel 16" или другие конфигурации (не разбирал).
- **21SR000JGE** — 1×32 (PSREF, notes), не подходит. Остальные E16 G3 Arrow Lake с 32/1 ТБ: 21SR0041GE 1534 €, 21SR007BGE 1559 €, 21SR0046GE 1699 € (тоже 1×32 по notes).
- **21KS0001GE** — эпизода «950 € в мае» на idealo нет, минимум за год 1249,89 €.
- **83SC0026GE** — Raptor Lake-HX, 16 ГБ; с планкой выходит за 1100 €. Variante LOQ Essential: 83SC000EGE 1111 € (та же конфигурация по карточке), 83SC000MGE 1165 €.
- **L16 G2 21SA** — Variante: 21SA0016GE 1027 € (225U 16/512), 21SA002EGE 1144 €, 21SA002HGE 1189 €, 21SA0046GE 1199,90 €, 21SA004BGE 1516 € (255U 32/1 ТБ). Конфигурации 002E / 002H / 0046 не проверял; среди проверенных с 32/1 ТБ дешевле 1295 € нет.
- **IdeaPad Pro 5 16 (Intel, 32/1 ТБ)** — самый дешёвый 83SK0012GE (356H + RTX 5050) — 2055,38 €. IdeaPad Slim 5i 16 83S60031GE — 1699 €.
- **Скан «Lenovo + Intel + 32 ГБ + 1 ТБ», сортировка по цене** ([ссылка](https://www.idealo.de/preisvergleich/ProductCategory/3751F2682401-7612877-107335535.html?q=Lenovo&sortKey=minPrice)): до 1122 € там только б/у, 17" и сборки магазинов (V15/V17 G4 с EAN вместо P/N, «T-LM-…»). Первый заводской 16" — 21SK0083GE за 1122 €.
  **Внимание:** 83HS00BLGE в этот фильтр не попадает — в его характеристиках на idealo нет поля «Prozessorhersteller». Скан по фильтрам может пропускать SKU.
- **Скан «Lenovo + Intel + 16 ГБ + 1 ТБ, 15–16"»** ([ссылка](https://www.idealo.de/preisvergleich/ProductCategory/3751F699493-1568565-2682401-7612874-107335535.html?q=Lenovo&sortKey=minPrice)): V15 G5 83GW00A9GE 598,98 €, IdeaPad Slim 3 IRH10 (83K1/83K2 — один слот, двухканал невозможен), 83HS00AAGE 799 € (2×8). Нового кандидата «16 + слот» нет.

## Зарядки Lenovo USB-C (для 83V7…)

| P/N | Что | Лучшая цена с доставкой | Предл. | Отчёт |
|---|---|---|---|---|
| 4X20M26272 | 65 Вт USB-C (стандартный) | **22,27 €** computeruniverse.net; 22,36 € cyberport.de (30 дн.) | 46 | ~22 € — совпадает |
| 4X21M37469 | 100 Вт USB-C | **49,35 €** jacob.de; 49,36 € proshop.de; «ab 42,90 €» — без доставки (notebookkontor, 49,80 с доставкой) | 19 | ~41 € — дороже на ~8 € |
| GX21V43585 | 100 Вт USB-C, EU (новый P/N) | **33,89 €** alza.de (30 дн.); Amazon MP 42,15; galaxus 46,94 | 3 | — |

## Ссылки на карточки idealo

- 83HS00BLGE — https://www.idealo.de/preisvergleich/OffersOfProduct/209881995_-ideapad-slim-5-16-83hs00blge-lenovo.html
- 21SK0083GE — https://www.idealo.de/preisvergleich/OffersOfProduct/206151171_-thinkbook-16-g8-21sk0083ge-lenovo.html
- 21SK007KGE — https://www.idealo.de/preisvergleich/OffersOfProduct/206151089_-thinkbook-16-g8-21sk007kge-lenovo.html
- 22AY004XGE — https://www.idealo.de/preisvergleich/OffersOfProduct/209382346_-thinkpad-e16-g3-22ay004xge-lenovo.html
- 83V70077GE — https://www.idealo.de/preisvergleich/OffersOfProduct/210281880_-ideapad-slim-5-16-83v70077ge-lenovo.html
- 83GW00A9GE — https://www.idealo.de/preisvergleich/OffersOfProduct/208744735_-v15-g5-83gw00a9ge-lenovo.html
- 21MA000RGE — https://www.idealo.de/preisvergleich/OffersOfProduct/204203147_-thinkpad-e16-g2-21ma000rge-lenovo.html
- 21MA003RGE — https://www.idealo.de/preisvergleich/OffersOfProduct/204203123_-thinkpad-e16-g2-21ma003rge-lenovo.html
- 21UR005AGE — https://www.idealo.de/preisvergleich/OffersOfProduct/209497615_-thinkbook-16-g9-21ur005age-lenovo.html
- 22AY004VGE — https://www.idealo.de/preisvergleich/OffersOfProduct/209221694_-thinkpad-e16-g3-22ay004vge-lenovo.html
- 22AY003XGE — https://www.idealo.de/preisvergleich/OffersOfProduct/209910718_-thinkpad-e16-g3-22ay003xge-lenovo.html
- 21MS004SGE — https://www.idealo.de/preisvergleich/OffersOfProduct/204414891_-thinkbook-16-g7-21ms004sge-lenovo.html
- 21MS0054GE — https://www.idealo.de/preisvergleich/OffersOfProduct/204331946_-thinkbook-16-g7-21ms0054ge-lenovo.html
- 21YC000MGE — https://www.idealo.de/preisvergleich/OffersOfProduct/209986038_-thinkpad-e16-g4-21yc000mge-lenovo.html
- 21SR000JGE — https://www.idealo.de/preisvergleich/OffersOfProduct/206352320_-thinkpad-e16-g3-21sr000jge-lenovo.html
- 21KS0001GE — https://www.idealo.de/preisvergleich/OffersOfProduct/204413152_-thinkpad-p16s-g3-21ks0001ge-lenovo.html
- 83SC0026GE — https://www.idealo.de/preisvergleich/OffersOfProduct/207948303_-loq-essential-15-83sc0026ge-lenovo.html
- 21SA0049GE — https://www.idealo.de/preisvergleich/OffersOfProduct/206765336_-thinkpad-l16-g2-21sa0049ge-lenovo.html
- 21SA004AGE — https://www.idealo.de/preisvergleich/OffersOfProduct/206765340_-thinkpad-l16-g2-21sa004age-lenovo.html
- 22AY003WGE — https://www.idealo.de/preisvergleich/OffersOfProduct/209382343_-thinkpad-e16-g3-22ay003wge-lenovo.html
- 21SK00C2GE — https://www.idealo.de/preisvergleich/OffersOfProduct/206563452_-thinkbook-16-g8-21sk00c2ge-lenovo.html
- 83HS00BMGE (только б/у) — https://www.idealo.de/preisvergleich/OffersOfProduct/209006181_-ideapad-slim-5-16-83hs00bmge-lenovo.html
- Зарядки: [4X20M26272](https://www.idealo.de/preisvergleich/OffersOfProduct/5584731_-65w-usb-c-4x20m26272-lenovo.html) · [4X21M37469](https://www.idealo.de/preisvergleich/OffersOfProduct/204066642_-100w-usb-c-4x21m37469-lenovo.html) · [GX21V43585](https://www.idealo.de/preisvergleich/OffersOfProduct/213644597_-usb-c-netzteil-100w-fuer-laptop-eu-stecker-gx21v43585-lenovo.html)
- Не найдены (поиск `MainSearchProductCategory.html?q=<P/N>`): 83V70037GE, 83GW00AHGE, 83J1006UGE, 83J1006HGE, 83JE014MGE, 83JE00TYGE, 83V70033GE, 83J1006XGE, 21SK008CGE, 21SK008MGE, 21SR0079GE, 21SR004LGE.
