# Рынок AMD-ноутбуков в Германии — сентябрь 2026

_Версия 2026-09-30. Скан idealo.de — локально, в Chrome пользователя, 30.09.2026 (~08:30–09:00). Капчи не было._
_Общий рынок (кризис памяти, магазины, сроки возврата, «aufgerüstet», ловушки idealo, распродажи) — в [`../../Intel/notes/market.md`](../../Intel/notes/market.md). Здесь — только AMD и свежие цифры._
_У каждого факта — ссылка. «не проверено» = первоисточник не нашёл. Цена idealo = минимальная «ab» на 30.09.2026, магазин — первый в списке предложений._

## Коротко

- **На idealo 183 карточки AMD 15–16" с 32 ГБ и 1 ТБ, у Intel — 589** (при повторной проверке 30.09 — 181 и 587, выдача плавает). Выбор у AMD в 3 раза меньше. Новых AMD-предложений ≤ 1100 € — 13 карточек, из них подходят по памяти (2×16 SO-DIMM, проверено по PSREF) только **4 Lenovo ThinkBook** и 1 HP без проверки.
- **Ни одного нового AMD на Zen 5 с 2×16 SO-DIMM за ≤ 1100 € нет.** Zen 5 (Krackan) за 986–1080 € есть только с **распаянными** 32 ГБ (Acer). IdeaPad Slim 5 16AKP10 с 2×16 сейчас продают только б/у.
- **Лучшее, что есть в бюджете: ThinkBook 16 G9 AHP `21UT004QGE`** (Ryzen 5 220 = Hawk Point, Zen 4; 2×16 DDR5-5600; второй слот M.2) — **ab 1068,01 €**, 39 предложений (при проверке — 1067,82 € у technikdeals24.de); за полгода подешевел с 1123 € до 1073 € (billiger; в апреле доходил до 1251 €).
  Тот же ноутбук с 2×16, но SSD 512 ГБ — `21UT004EGE` — ab 894 € (найдено при проверке, в скан 32/1 ТБ не попал; с SSD 1 ТБ выходит примерно та же цена — см. 1.1).
  Дешевле — только старые Zen 3/3+: ThinkBook 16 G7 ARP `21MW00AYGE` (R5 7535HS) — 998,99 €, `21MW007VGE` (R7 7735HS) — 1080,62 €, ThinkBook 16 G6 ABP `21KK0074GE` (R7 7730U, DDR4) — 999 € в одном магазине.
- **Ловушка №1 — HP ProBook 4 G1a:** самый дешёвый фирменный AMD с 32/1 ТБ (`C7SP9ES`, 899 €) и ещё 7 SKU до 1330 €. В QuickSpecs HP прямо написано: **аппаратный HEVC отключён**. Исключаем все ProBook 4 G1a.
- **Ловушка №2 — ThinkPad E16 Gen 3 AMD `21ST004GGE` / `21ST001YGE`:** по PSREF это **1×32 ГБ** одной планкой, а не 2×16 (второй слот SO-DIMM свободен). Одноканал — не подходит (в `MEMORY.md` они записаны как находка).
- **«16 ГБ + планка» у AMD почти не работает.** Все проверенные Lenovo с 16 ГБ — это **2×8** (менять обе, комплект 2×16 — 475 €) или распайка. Зацепка — ASUS Vivobook 16 M1607 за 799 €: по asus.com/de у серии **16 ГБ распаяно + 1 слот SO-DIMM, до 32 ГБ**; двухканал — только с планкой в слоте. Это вариант «16 распайка + 16 SO-DIMM» (третий приоритет), итог ≈ 987–1043 €.
  (исправлено при проверке: «единственная» — неверно, таких SKU два: M1607GA-MB020W (AI 7 445) и M1607KA-MB172W; по конкретным SKU раскладка не проверена.)
- **AMD + RTX (8 ГБ) + 1 ТБ:** до 1250 € — один новый SKU, GigaByte Gaming A16 `3VHK3DE894SH` (R7 260 + RTX 5060, **16 ГБ**) за 1099 €. С планкой 16 ГБ — ≈ 1287–1343 €, но только если там 1×16 + свободный слот (раскладка не проверена; при 2×8 ≈ 1574 €). С 32 ГБ с завода — от 1525 €. В бюджет не входит.
- **Планка DDR5-5600 16 ГБ на idealo:** обычно 234–270 € (Crucial 243,90 €, ADATA 263,55 €, при проверке — 259 €); одно предложение Kingston за 187,56 €. Комплект 2×16 — 475,25 €. DDR4-3200 16 ГБ — 113,17 €.
- **AMD против Intel:** в одном классе (бизнес 16", 2×16) AMD дешевле на 50–200 € (ThinkBook G9 AHP 1068 € против G8 IAL 1122 €). В дешёвом классе «старый CPU + 2×16» Intel дешевле (Acer Aspire Go 16 с i9-13900H — 849–899 €).
- **Что выйдет:** Gorgon Point (Ryzen AI 400) уже в продаже с января 2026. Следующее поколение — Zen 6 «Medusa» — AMD обещает на 2027 год; в классе ≤ 1100 € в ближайшие 3–6 месяцев новинок не ждать. Доля AMD в поставках мобильных x86 CPU (мир, Q2 2026, Mercury Research) — 28,9 % (исправлено при проверке: это доля в поставках x86-процессоров, а не в продажах ноутбуков).

## 0. Как сканировал idealo

- Категория «Notebooks» ([3751](https://www.idealo.de/preisvergleich/ProductCategory/3751.html)), фильтры кликами, сортировка «Preis: Günstigster zuerst». Коды фильтров в URL (из адресной строки):
  AMD `848110`, 16 Zoll `1568565`, 15 Zoll `699493` (сюда попадают 15,3" и 15,6"), 1 TB SSD `2682401`, 32 GB `7612877`, 16 GB `7612874`,
  RTX 5060 `106745465`, RTX 5050 `106843055`, RTX 4060 `104023766`, RTX 5070 `106697019`. Вторая страница — суффикс `I16-15`.
- Карточку каждого товара открывал: CPU, кодовое имя («Prozessor Codename»), ОЗУ, ОС, число предложений, первые магазины, названия предложений (там видно «aufgerüstet», чужие конфигурации).
- **idealo не показывает Herstellernummer в характеристиках.** Парт-номер — в названии карточки и в названиях предложений (например, `C7SP9ES#ABD`, `NX.JLLEG.009`).
- Карточки с пометкой «gebraucht» — только б/у предложения; в таблицах помечены «б/у», в кандидаты не идут.
- Контроль: текстовый поиск «32GB 1TB» в категории с фильтром AMD ([ссылка](https://www.idealo.de/preisvergleich/ProductCategory/3751F848110.html?q=32GB%201TB&sortKey=minPrice)) новых 15–16" карточек до 1250 € не добавил.
- Память по даташитам проверял для всех Lenovo (PSREF), части Acer и ASUS (Icecat) и HP ProBook (QuickSpecs). Остальное — «не проверено».

## 1. AMD, 15–16", 32 ГБ, 1 ТБ — все карточки до ~1330 €

Выдача: [idealo, 183 карточки](https://www.idealo.de/preisvergleich/ProductCategory/3751F699493-848110-1568565-2682401-7612877.html?sortKey=minPrice). Все цены — 30.09.2026.
Колонка «Память»: что пишет idealo → что в даташите.

| # | Модель · парт-номер | CPU (кодовое имя) | Память | Экран · GPU · ОС | ab, € (магазин) · предл. | Вывод |
|---|---|---|---|---|---|---|
| 1 | CSL R'Evolve C15 `90608` | R5 5500U (Lucienne, Zen 2) | 32 ГБ, раскладка — не проверено | 15,6" FHD · Vega 7 · без ОС | 659,00 (csl-computer.de) · 3 | старый CPU; сборка CSL |
| 2 | CSL R'Evolve C15 `90610` | R5 5500U | 32 ГБ | 15,6" FHD · Win 11 Home | 709,00 (csl-computer.de) · 6 | в карточке смешаны 5500U и 7430U |
| 3 | Acer Aspire Go 15 `AG15-42P-R5ZD` | R7 5825U (Barcelo, Zen 3) | 32 ГБ | 15,6" FHD · Win 11 Home | 729,00 (TIBERION, Marketplace) · 1 | старый CPU, 1 продавец |
| 4 | Lenovo IdeaPad Slim 5 16AKP10 `83HY0061GE` | Ryzen AI 5 340 (Krackan, Zen 5) | **2×16 SO-DIMM** ([PSREF](https://psref.lenovo.com/Detail/IdeaPad/IdeaPad_Slim_5_16AKP10?M=83HY0061GE)) | 16" WUXGA 300 нит · 840M · Win 11 Home | 877,00 — **только б/у** · 1 | следить за новыми |
| 5 | HP ProBook 4 G1a 16 `C7SP9ES` | R5 230 (Hawk Point, Zen 4) | 32 ГБ (2 слота SO-DIMM по QuickSpecs) | 16" WUXGA 300 нит · 760M · FreeDOS | 899,00 (notebooksbilliger.de, nullprozentshop.de) · 8 | **HEVC отключён — исключить** |
| 6 | HP 255 G10 «884420874911» | R5 7530U/7535U (данные расходятся) | 32 ГБ — сборка продавца | 15,6" FHD · Win 11 Pro | 919,00 (Marketplace) · 1 | «HP 255R G10 … 32GB … //Notebooktasche» — не заводской SKU |
| 7 | HP 15-fc0677ng `C8TT7EA` | R7 7730U (Barcelo-R, Zen 3) | 32 ГБ DDR4, раскладка — не проверено | 15,6" FHD · Win 11 Home · 1,6 кг | 929,00 (galaxus.de, easynotebooks.de) · 8 | старый CPU; HEVC у HP consumer — не проверено |
| 8 | HP 15 «4260260631727» | R5 7530U | 32 ГБ — сборка продавца | 15,6" FHD · Win 11 Pro | 929,00 (Softech2000, Marketplace) · 2 | «individuell konfigurierbar» |
| 9 | Lenovo IdeaPad Slim 5 16AKP10 `83HY008CGE` | Ryzen AI 7 350 (Krackan) | **2×16 SO-DIMM** ([PSREF](https://psref.lenovo.com/Detail/IdeaPad/IdeaPad_Slim_5_16AKP10?M=83HY008CGE)) | 16" WUXGA · 860M | 949,00 — **только б/у** · 1 | следить за новыми |
| 10 | Acer Aspire 16 AI `A16-61M-R583` | Ryzen AI 7 350 | 32 ГБ | 16" 2K 120 Гц | 983,33 — **только б/у** · 2 | — |
| 11 | Acer Swift Air 16 `NX.DL5EG.002` (SFA16-61M-R1FY) | **Ryzen AI 5 330** (Krackan, 4 ядра) | 32 ГБ **LPDDR5, распайка** ([Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Acer&ProductCode=NX.DL5EG.002)) | 16" WUXGA OLED · 820M · 1,1 кг | 986,51 (expert.de) · 6 | распайка + слабый CPU |
| 12 | **Lenovo ThinkBook 16 G7 ARP `21MW00AYGE`** | R5 7535HS (Rembrandt-R, Zen 3+) | **2×16 DDR5-4800 SO-DIMM**, 2 слота M.2 2280 ([PSREF](https://psref.lenovo.com/Detail/ThinkBook/ThinkBook_16_G7_ARP?M=21MW00AYGE)) | 16" WUXGA 300 нит 45 % NTSC · 660M · Win 11 Pro · 45 Втч | **998,99** (easynotebooks.de, playox.de) · 14 | подходит; CPU 2023 г. |
| 13 | **Lenovo ThinkBook 16 G6 ABP `21KK0074GE`** | R7 7730U (Barcelo-R, Zen 3) | **2×16 DDR4-3200 SO-DIMM** ([PSREF](https://psref.lenovo.com/Detail/ThinkBook/ThinkBook_16_G6_ABP?M=21KK0074GE)) | 16" WUXGA · Win 11 Pro · 71 Втч | **999,00** (electronic4you.de), дальше 1149 · 8 | подходит; старый CPU, 1 дешёвый магазин |
| 14 | **Lenovo ThinkBook 16 G9 AHP `21UT004QGE`** | R5 220 (Hawk Point, Zen 4) | **2×16 DDR5-5600 SO-DIMM**, до 64 ГБ; M.2 2242 + свободный M.2 2280 ([PSREF](https://psref.lenovo.com/Detail/ThinkBook/ThinkBook_16_G9_AHP?M=21UT004QGE)) | 16" WUXGA 400 нит 45 % NTSC · 740M · Win 11 Pro · 48 Втч | **1068,01** (technikdeals24.de, heinzsoft-shop.de) · 39 | **лучший в бюджете** |
| 15 | Acer Aspire 16 AI `A16-61M-R8T1` (`NX.JLLEG.009`) | Ryzen AI 7 350 (Krackan) | 32 ГБ **LPDDR5X, распайка** ([Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Acer&ProductCode=NX.JLLEG.009)) | 16" WUXGA 120 Гц · 860M · 1,55 кг · БП 100 Вт | 1080,25 (easynotebooks.de, technikdirekt.de) · 17 | список «распайка»; SSD QLC (по названию у office-lieferant) |
| 16 | **Lenovo ThinkBook 16 G7 ARP `21MW007VGE`** | R7 7735HS (Rembrandt-R) | **2×16 DDR5-4800** ([PSREF](https://psref.lenovo.com/Detail/ThinkBook/ThinkBook_16_G7_ARP?M=21MW007VGE)) | 16" WUXGA · 680M · Win 11 Pro | **1080,62** (cyclotron.de) · 36 | подходит; CPU 2023 г. |
| 17 | HP OmniBook 5 16 `16-ag1477ng` | Ryzen AI 7 350 | 32 ГБ | 16" WUXGA | 1105,36 — **только б/у** · 2 | — |
| 18 | HP ProBook 4 G1a 16 `C7SQ0ES` | R5 230 | 32 ГБ | Win 11 Pro | 1129,00 (NBB) · 8 | HEVC отключён |
| 19 | Lenovo ThinkPad E16 Gen 3 AMD `21ST004GGE` | R5 220 (Hawk Point) | **1×32 ГБ** ([PSREF](https://psref.lenovo.com/Detail/ThinkPad/ThinkPad_E16_Gen_3_AMD?M=21ST004GGE)) | 16" WUXGA · 740M | 1149,00 (NBB) · 19 | **одна планка — не подходит** |
| 20 | Acer Swift Air 16 `SFA16-61M-R559` (`NX.DL5EG.001`) | Ryzen AI 7 350 | LPDDR5, распайка ([Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Acer&ProductCode=NX.DL5EG.001)) | 16" WUXGA OLED · ~1 кг | 1149,00 (NBB, nullprozentshop.de) · 11 | «распайка», наблюдать |
| 21 | LG Gram 15 `15Z80T-G.AU88G` | Ryzen AI 7 350 | idealo: 32 ГБ; единственное предложение: **«16GB RAM»** | 15,6" FHD · 1,3 кг | 1159,00 (joybuy.de) · 1 | данные расходятся |
| 22 | HP ProBook 4 G1a 16 `AD2N2ET` | R7 250 | 32 ГБ | Win 11 Pro | 1167,99 (directdeal.me) · 31 | HEVC отключён |
| 23 | Lenovo ThinkPad L16 Gen 3 AMD `21XC002BGE` | Ryzen AI 7 445 (Gorgon Point, Zen 5) | **2×16 DDR5-5600**, один M.2 ([PSREF](https://psref.lenovo.com/Detail/ThinkPad/ThinkPad_L16_Gen_3_AMD?M=21XC002BGE)) | 16" WUXGA 400 нит · 840M · 1,85 кг | 1171,23 (buyzoxs.de, **«differenzbesteuert»**), дальше **1675,97** (klarsicht-it.de) · 35 | реальная цена ~1676 € |
| 24 | Lenovo ThinkBook 16 G9 AHP `21UT000RGE` | R7 250 (Hawk Point) | **2×16 DDR5-5600** ([PSREF](https://psref.lenovo.com/Detail/ThinkBook/ThinkBook_16_G9_AHP?M=21UT000RGE)) | 16" WUXGA 400 нит · 780M | 1188,00 (notebookstore.de) · 32 | наблюдать |
| 25 | HP ProBook 4 G1a 16 `C65TTES` | R7 250 | 32 ГБ | Win 11 Pro | 1189,00 (Marketplace) · 3 | HEVC отключён |
| 26 | Lenovo ThinkPad E16 Gen 3 AMD `21ST001YGE` | R7 250 | **1×32 ГБ** ([PSREF](https://psref.lenovo.com/Detail/ThinkPad/ThinkPad_E16_Gen_3_AMD?M=21ST001YGE)) | 16" WUXGA · 780M | 1194,84 (technikdeals24.de) · 43 | одна планка |
| 27 | HP ProBook 4 G1a 16 `C7SQ3ES` | R7 250 | 32 ГБ | Win 11 Pro | 1199,00 (NBB) · 8 | HEVC отключён |
| 28 | Lenovo ThinkPad E16 Gen 2 AMD `21M5002DGE` | idealo: R5 7535HS; **PSREF: R7 7735HS** (Rembrandt-R) | **2×16 DDR5-4800** ([PSREF](https://psref.lenovo.com/Detail/ThinkPad/ThinkPad_E16_Gen_2_AMD?M=21M5002DGE)) | 16" WUXGA · 680M · 1,81 кг | 1199,00 (electronic4you.de) · 1 | наблюдать; idealo ошибается в CPU |
| 29 | Lenovo ThinkPad E16 Gen 2 AMD `21M5002VGE` | R5 7535HS | 2×16 DDR5-4800 ([PSREF](https://psref.lenovo.com/Detail/ThinkPad/ThinkPad_E16_Gen_2_AMD?M=21M5002VGE)) | 16" WUXGA · 660M | 1256,32 (Marketplace) · 3 | дороже 1250 |
| 30 | Lenovo IdeaPad 5 2-in-1 15AGP11 `83UM002BGE` | Ryzen AI 7 445 (Gorgon) | **2×16 DDR5-5600** ([PSREF](https://psref.lenovo.com/Detail/IdeaPad/IdeaPad_5_2_in_1_15AGP11?M=83UM002BGE)) | 15,3" 2.5K OLED 165 Гц · **без блока питания** | 1267,07 (computeruniverse.net, cyberport.de) · 13 | за 6 мес. минимум 1234,88 € ([billiger](https://www.billiger.de/pricelist/5781548420-lenovo-ideapad-5-2-in-1-15agp11-15-3-amd-ryzen-ai-7-445-32-gb-ram-1-tb-ssd-83um002bge)) |
| 31 | Acer Swift Go 16 AI `SFG16-61-R1WP` | Ryzen AI 7 350 | 32 ГБ, раскладка — не проверено | 16" 120 Гц · 1,5 кг | 1278,00 (easynotebooks.de) · 5 | дороже 1250 |
| 32–36 | HP ProBook 4 G1a `T-HM-…` (2 шт.), `C7SQ4ES`, HP EliteBook 8 G1a 16 `CT3V8ES`, Acer Swift Go 16 `SFG16-61-R6QV` | R5 230 / R7 250 / AI 7 350 | — | — | 1279–1329 | вне диапазона; ProBook — HEVC отключён; HEVC у EliteBook 8 G1a — не проверено |

Карточки idealo (все — `https://www.idealo.de/preisvergleich/OffersOfProduct/<ID>.html`):
№1 [203893377](https://www.idealo.de/preisvergleich/OffersOfProduct/203893377.html), №2 [203893407](https://www.idealo.de/preisvergleich/OffersOfProduct/203893407.html), №3 [208529022](https://www.idealo.de/preisvergleich/OffersOfProduct/208529022.html),
№4 [207280344](https://www.idealo.de/preisvergleich/OffersOfProduct/207280344.html), №5 [208030540](https://www.idealo.de/preisvergleich/OffersOfProduct/208030540.html), №6 [205898880](https://www.idealo.de/preisvergleich/OffersOfProduct/205898880.html),
№7 [207948312](https://www.idealo.de/preisvergleich/OffersOfProduct/207948312.html), №8 [207229437](https://www.idealo.de/preisvergleich/OffersOfProduct/207229437.html), №9 [209439304](https://www.idealo.de/preisvergleich/OffersOfProduct/209439304.html),
№10 [207875978](https://www.idealo.de/preisvergleich/OffersOfProduct/207875978.html), №11 [211778543](https://www.idealo.de/preisvergleich/OffersOfProduct/211778543.html), №12 [207306483](https://www.idealo.de/preisvergleich/OffersOfProduct/207306483.html),
№13 [203811127](https://www.idealo.de/preisvergleich/OffersOfProduct/203811127.html), №14 [209122445](https://www.idealo.de/preisvergleich/OffersOfProduct/209122445.html), №15 [208031586](https://www.idealo.de/preisvergleich/OffersOfProduct/208031586.html),
№16 [207306221](https://www.idealo.de/preisvergleich/OffersOfProduct/207306221.html), №17 [207390560](https://www.idealo.de/preisvergleich/OffersOfProduct/207390560.html), №18 [208030541](https://www.idealo.de/preisvergleich/OffersOfProduct/208030541.html),
№19 [207096771](https://www.idealo.de/preisvergleich/OffersOfProduct/207096771.html), №20 [209373389](https://www.idealo.de/preisvergleich/OffersOfProduct/209373389.html), №21 [206107976](https://www.idealo.de/preisvergleich/OffersOfProduct/206107976.html),
№22 [206571932](https://www.idealo.de/preisvergleich/OffersOfProduct/206571932.html), №23 [210622077](https://www.idealo.de/preisvergleich/OffersOfProduct/210622077.html), №24 [209122441](https://www.idealo.de/preisvergleich/OffersOfProduct/209122441.html),
№25 [208320156](https://www.idealo.de/preisvergleich/OffersOfProduct/208320156.html), №26 [206556600](https://www.idealo.de/preisvergleich/OffersOfProduct/206556600.html), №27 [208030543](https://www.idealo.de/preisvergleich/OffersOfProduct/208030543.html),
№28 [208145740](https://www.idealo.de/preisvergleich/OffersOfProduct/208145740.html), №29 [204203152](https://www.idealo.de/preisvergleich/OffersOfProduct/204203152.html), №30 [210991837](https://www.idealo.de/preisvergleich/OffersOfProduct/210991837.html),
№31 [206775817](https://www.idealo.de/preisvergleich/OffersOfProduct/206775817.html).

### 1.1 Что из этого проходит

**≤ 1100 €, 2×16 SO-DIMM с завода (проверено по PSREF):**

| Парт-номер | CPU | ab, € | Минус |
|---|---|---|---|
| ThinkBook 16 G9 AHP `21UT004QGE` | R5 220 (Hawk Point, Zen 4; iGPU 740M — [amd.com](https://www.amd.com/en/products/processors/laptop/ryzen/200-series/amd-ryzen-5-220.html)) | 1068,01 | младшая iGPU; экран 45 % NTSC |
| ThinkBook 16 G7 ARP `21MW00AYGE` | R5 7535HS (Zen 3+, 2023) | 998,99 | старая архитектура, DDR5-4800, 45 Втч |
| ThinkBook 16 G7 ARP `21MW007VGE` | R7 7735HS (Zen 3+, 680M) | 1080,62 | старая архитектура |
| ThinkBook 16 G6 ABP `21KK0074GE` | R7 7730U (Zen 3, Vega) | 999,00 (1 магазин) | самый старый CPU; DDR4 |

- billiger.de по `21UT004QGE`: 1073 €, 27 предложений; 02.04.2026 — 1123,19 €, с тех пор медленно дешевеет; минимум за полгода — сегодня ([billiger](https://www.billiger.de/products/5510914032-lenovo-thinkbook-16-g9-amd-ryzen-5-220-32-gb-ram-1-tb-ssd-win11-pro-21ut004qge)).
  Остальные три SKU billiger.de не знает («Keine Treffer»).
  Уточнение при проверке: история billiger не монотонная — 02.04 1123,19 €, 28.04 максимум 1251 €, 30.09 минимум 1072 € ([billiger](https://www.billiger.de/products/5510914032-lenovo-thinkbook-16-g9-amd-ryzen-5-220-32-gb-ram-1-tb-ssd-win11-pro-21ut004qge)).
  Два первых магазина на idealo (technikdeals24.de и heinzsoft-shop.de) — оба «Shop aus Herzberg», вероятно один продавец (не проверено).
- **Найдено при проверке — соседние SKU того же ThinkBook 16 G9 AHP (в скан 32/1 ТБ не попали из-за SSD 512 ГБ):**

| Парт-номер | CPU | Память (PSREF) | SSD | ab, € (магазин) · предл. | Итог |
|---|---|---|---|---|---|
| `21UT004EGE` | R5 220 | **2×16 DDR5-5600** ([PSREF](https://psref.lenovo.com/Detail/ThinkBook/ThinkBook_16_G9_AHP?M=21UT004EGE)) | 512 ГБ; слот M.2 2280 свободен | **894,00** (technikdeals24.de, heinzsoft-shop.de; дальше 949 Galaxus-МП) · 7 — [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/209122443_-thinkbook-16-g9-21ut004ege-lenovo.html) | + SSD 1 ТБ ~135–190 € ([market.md, 1.3](../../Intel/notes/market.md)) ≈ 1029–1084 € — примерно как `21UT004QGE`, зато 1,5 ТБ; критерий «1 ТБ с завода» не выполнен |
| `21UT0041GE` | R5 220 | 1×16 + свободный слот ([PSREF](https://psref.lenovo.com/Detail/ThinkBook/ThinkBook_16_G9_AHP?M=21UT0041GE)) | 512 ГБ | 949,00 (easynotebooks.de) · 34 — [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/209122446_-thinkbook-16-g9-21ut0041ge-lenovo.html) | + планка 244 € = 1193 € — дороже потолка |
- HP 15-fc0677ng `C8TT7EA` (929 €) — условно: раскладка 32 ГБ DDR4 и HEVC не проверены.

**≤ 1100 €, распаянные 32 ГБ (нежелательно):** Acer Aspire 16 AI `NX.JLLEG.009` (AI 7 350) — 1080,25 €; Acer Swift Air 16 `NX.DL5EG.002` (AI 5 330, слабый) — 986,51 €.
У Acer в Германии риск с HEVC — см. [`../../Intel/notes/hevc-audit.md`](../../Intel/notes/hevc-audit.md).

**1100–1250 € — наблюдать:** ThinkBook 16 G9 AHP `21UT000RGE` (R7 250, 1188 €), ThinkPad E16 Gen 2 `21M5002DGE` (7735HS, 2×16, 1199 €, 1 магазин), Acer Swift Air 16 `NX.DL5EG.001` (распайка, 1149 €).
Zen 5 с 2×16: IdeaPad Slim 5 16AKP10 `83HY0061GE` / `83HY008CGE` (сейчас только б/у), IdeaPad 5 2-in-1 15 `83UM002BGE` (1267 €), ThinkPad L16 Gen 3 `21XC002BGE` (~1676 € у обычных магазинов).

## 2. 16 ГБ + 1 ТБ, AMD 15–16" — кандидаты «16 ГБ + докупить планку»

Выдача: [стр. 1](https://www.idealo.de/preisvergleich/ProductCategory/3751F699493-848110-1568565-2682401-7612874.html?sortKey=minPrice), [стр. 2](https://www.idealo.de/preisvergleich/ProductCategory/3751F699493-848110-1568565-2682401-7612874I16-15.html?sortKey=minPrice) — 178 карточек. Просмотрел всё до ~950 €.
Схема работает, только если **1×16 + свободный слот** (докупить 1×16 за ~190–245 €, см. раздел 4). При 2×8 нужен комплект 2×16 за ~475 €.

| Модель · парт-номер | CPU (кодовое имя) | Память по даташиту | ab, € (магазин) · предл. | Итог с памятью | Вывод |
|---|---|---|---|---|---|
| HP 15-fc0554ng | R5 7520U (**Mendocino**, Zen 2) | DDR4 — не проверено | 579,00 (medimax.de) · 22 | — | слабый; не для 4K |
| HP 255 G10 `CJ5Q2EA` / `CJ5Q1EA` | R5 7535U (Rembrandt-R) | не проверено | 599,00 (asaboshisystems.de) · 1 | — | 1 магазин |
| HP 15-fc0680ng | R7 7730U (Barcelo-R) | 16 ГБ DDR4, раскладка — не проверено | 655,00 (Euronics, Marketplace) · 15 | 1×16: +113 € ≈ 768 €; 2×8: +258 € ≈ 913 € | старый CPU; HEVC у HP — не проверено |
| HP 15-fc0676ng | R7 7730U | то же | 674,47 (easynotebooks.de) · 12 | ≈ 787–932 € | то же |
| HP OmniBook 3 15 `15-fn0655ng` | Ryzen AI 5 340 (Krackan) | 2 слота SO-DIMM; 16 ГБ у похожих US-SKU = 2×8 ([laptopmedia](https://laptopmedia.com/laptop-specs/hp-omnibook-3-8/), для DE-SKU — не проверено) | 695,00 (Euronics, Marketplace) · 17 | 2×8: +475 € ≈ 1170 € | скорее не выходит |
| HP OmniBook 3 15 `15-fn0653ng` | Ryzen AI 5 330 | то же | 699,00 (allesfuerzuhause.de, galaxus.de) · 11 | — | слабый CPU |
| Lenovo IdeaPad Slim 3 16ABR8 `82XR009WGE` / `82XR0094GE` | R7 7730U | **16 ГБ распайка, не расширить** ([PSREF](https://psref.lenovo.com/Detail/IdeaPad/IdeaPad_Slim_3_16ABR8?M=82XR009WGE)) | 699,00 (expert.de) / 799,00 | — | **не подходит** |
| Lenovo IdeaPad Slim 3 15ARP10 `83K700ENGE` | R5 7535HS | **8 распайка + 8 SO-DIMM, максимум 24 ГБ** ([PSREF](https://psref.lenovo.com/Detail/IdeaPad/IdeaPad_Slim_3_15ARP10?M=83K700ENGE)) | 729,00 (e-tec.at) · 3 | — | **32 ГБ невозможно** |
| Lenovo IdeaPad Slim 3 16ARP10 `83K8006EGE` | R7 7735HS | то же, максимум 24 ГБ ([PSREF](https://psref.lenovo.com/Detail/IdeaPad/IdeaPad_Slim_3_16ARP10?M=83K8006EGE)) | 749,99 (expert.de) · 3 | — | **не подходит** |
| Lenovo IdeaPad Slim 5 16AKP10 `83HY006XGE` | Ryzen AI 5 330 | **2×8** ([PSREF](https://psref.lenovo.com/Detail/IdeaPad/IdeaPad_Slim_5_16AKP10?M=83HY006XGE)) | 796,39 (galaxus.de, easynotebooks.de) · 13 | +475 € ≈ 1271 € | не выходит |
| ASUS Vivobook 16 `M1607GA-MB020W` | Ryzen AI 7 445 (Gorgon Point) | 16 ГБ DDR5, **«On-board + SO-DIMM», 1 слот SO-DIMM**, максимум 32 ГБ ([Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=ASUS&ProductCode=M1607GA-MB020W)); у серии M1607 на asus.com/de — «16GB DDR5 on board», слот свободен, двухканал только с планкой ([asus.com](https://www.asus.com/de/laptops/for-home/vivobook/asus-vivobook-16-m1607/techspec/)); для GA-SKU страницы на asus.com нет — по SKU не проверено | 799,00 (notebooksbilliger.de, nullprozentshop.de) · 2 | если 16 распайка + пустой слот: +188–244 € ≈ **987–1043 €** | **единственная зацепка**; проверить на asus.com |
| ASUS Vivobook 16 `M1607KA-MB172W` | карточка idealo: Ryzen AI 7 350 (Krackan); **единственное предложение: «Ryzen AI 5 330»** (исправлено при проверке: CPU расходится) | 16 ГБ DDR5; у серии M1607KA на asus.com/de — 16 ГБ on board + 1 слот, до 32 ГБ ([asus.com](https://www.asus.com/de/laptops/for-home/vivobook/asus-vivobook-16-m1607/techspec/)); по SKU — не проверено (Icecat: нет) | 799,00 (electronic4you.de) · 1 | если 16 on board + пустой слот: ≈ 987–1043 € | вторая зацепка ASUS; сначала выяснить CPU |
| ASUS Vivobook S16 `M3607HA-RP017W` | R7 260 (Hawk Point) | 16 ГБ DDR5, раскладка — не проверено | 819,00 (expert.de) · 4 | — | проверить |
| Lenovo IdeaPad Slim 5a 16AGP11 `83S2000BGE` (в PSREF — «IdeaPad Slim 5 16AGP11») | Ryzen AI 7 445 (Gorgon) | **2×8**; экран OLED 100 % DCI-P3; **без блока питания** ([PSREF](https://psref.lenovo.com/Detail/IdeaPad/IdeaPad_Slim_5_16AGP11?M=83S2000BGE)) | 889,00 (galaxus.de), дальше 1032,97 · 20 | +475 € ≈ 1364 € | не выходит |
| Lenovo IdeaPad Slim 5 16AKP10 `83HY002SGE` | Ryzen AI 5 340 | **2×8** ([PSREF](https://psref.lenovo.com/Detail/IdeaPad/IdeaPad_Slim_5_16AKP10?M=83HY002SGE)) | 911,73 (Marketplace) · 1 | ≈ 1387 € | не выходит |
| Acer Aspire 16 AI `A16-61M-R87H` | Ryzen AI 7 350 | 16 ГБ **LPDDR5X** (распайка) | 934,00 (galaxus.de) · 5 | — | не подходит |
| Lenovo IdeaPad Slim 5a 16AGP11 `83S2004HGE` | Ryzen AI 7 445 | **2×8**, IPS 400 нит, без БП ([PSREF](https://psref.lenovo.com/Detail/IdeaPad/IdeaPad_Slim_5_16AGP11?M=83S2004HGE)) | 938,72 (allesfuerzuhause.de) · 4 | ≈ 1414 € | не выходит |
| HP ProBook 4 G1a 16 `C65TVES` | R7 250 | 2 слота | 949,00 (computeruniverse.net, cyberport.de) · 10 | — | HEVC отключён |
| Lenovo IdeaPad 5 2-in-1 16AKP10 `83KU0012GE` | Ryzen AI 7 350 | **16 ГБ LPDDR5X распайка** ([PSREF](https://psref.lenovo.com/Detail/IdeaPad/IdeaPad_5_2_in_1_16AKP10?M=83KU0012GE)) | 999,00 · 14 | — | не подходит |

Дешевле 580 € — только б/у или Zen 2 (Lucienne) и сборки CSL. Карточки: [HP 15-fc0680ng](https://www.idealo.de/preisvergleich/OffersOfProduct/208881762.html), [OmniBook 3 15-fn0655ng](https://www.idealo.de/preisvergleich/OffersOfProduct/206785231.html), [Vivobook 16 M1607GA-MB020W](https://www.idealo.de/preisvergleich/OffersOfProduct/209172185.html), [M1607KA-MB172W](https://www.idealo.de/preisvergleich/OffersOfProduct/210698249.html), [Vivobook S16 M3607HA](https://www.idealo.de/preisvergleich/OffersOfProduct/206751394.html), [83HY006XGE](https://www.idealo.de/preisvergleich/OffersOfProduct/208069128.html), [83S2000BGE](https://www.idealo.de/preisvergleich/OffersOfProduct/209325301.html), [83S2004HGE](https://www.idealo.de/preisvergleich/OffersOfProduct/213159323.html), [A16-61M-R87H](https://www.idealo.de/preisvergleich/OffersOfProduct/212350121.html), [C65TVES](https://www.idealo.de/preisvergleich/OffersOfProduct/207830979.html).

**Вывод:** у AMD 16-гигабайтные SKU почти всегда 2×8, распайка или «8 + 8». Схема «16 ГБ + планка» реальна только у ASUS Vivobook 16 M1607 (один слот; у серии по asus.com/de распаяно 16 ГБ) — два SKU по 799 €, M1607GA-MB020W и M1607KA-MB172W. Это вариант «16 распайка + 16 SO-DIMM» (третий по приоритету). Без докупленной планки такой ноутбук работает в одноканале.
У Lenovo 1×16 + свободный слот есть (например, ThinkBook 16 G9 AHP `21UT0041GE`), но с SSD 512 ГБ — в эту выдачу (1 ТБ) не попадает, см. 1.1.

## 3. AMD + видеокарта ≥ 8 ГБ, 1 ТБ, 15–16"

Выдача: [RTX 5050/5060/5070/4060, AMD, 1 ТБ, 15–16" — 154 карточки](https://www.idealo.de/preisvergleich/ProductCategory/3751F699493-848110-1568565-2682401-104023766-106697019-106745465-106843055.html?sortKey=minPrice).

| Модель · парт-номер | CPU (кодовое имя) | GPU | ОЗУ | ab, € (магазин) · предл. | Вывод |
|---|---|---|---|---|---|
| GigaByte Gaming A16 `3VHK3DE894SH` | R7 260 (Hawk Point) | RTX 5060 8 ГБ | 16 ГБ DDR5, раскладка — не проверено (Icecat: нет; gigabyte.com через curl — 403) | **1099,00** (coolblue.de, mediamarkt.de, computeruniverse.net, cyberport.de, alternate.de) · 16 — [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/207329496_-gaming-a16-3vhk3de894sh-gigabyte.html) | единственный ≤ 1250 €; с планкой ≈ 1287–1343 € **только при 1×16 + свободном слоте**; при 2×8 ≈ 1574 € |
| HP Omen 16 `16-xd0674ng` | R7 7840HS (Phoenix) | RTX 4060 8 ГБ | 16 ГБ | 1285,99 (Marketplace) · 2 | RTX 40 без NVDEC 4:2:2 |
| ASUS TUF Gaming A16 `FA608UMI-TU199W` | R7 260 | RTX 5060 | 16 ГБ | 1299,00 (Amazon) · 2 | дороже 1250 |
| Acer Nitro V 16 AI `ANV16-42-R9HY` / `-R7AC` | R7 260 | RTX 5060 / 5050 | 16 ГБ | 1299,00 (NBB) · 9–10 | дороже 1250 |
| AMD + RTX **с 32 ГБ**: MSI Cyborg A15 AI `B2HWGKG-089` (RTX 5070) · Lenovo LOQ 15 `83TNCTO1WWDE2` (RTX 5050, CTO) · GigaByte Aero X16 `1WH93DEC64AH` (RTX 5070) | R7 260 / R7 250 / AI 7 350 | — | 32 ГБ | 1525,10 · 1546,16 · 1599,00 | от 1525 € |

- Более дешёвые позиции в выдаче — только б/у (Acer Nitro V 16 `ANV16-42-R38V` 1070,99 € б/у; Nitro 16 `AN16-42-R64J` 1218,99 € б/у).
- **Вывод:** AMD + RTX + 32 ГБ + 1 ТБ за ≤ 1100 € нет; ближе всего — 16 ГБ за 1099 €, с планкой выше потолка. Картина та же, что у Intel ([`../../Intel/notes/candidates-gpu.md`](../../Intel/notes/candidates-gpu.md)).
- Почему RTX 50, а не 40: NVDEC Blackwell декодирует H.264/HEVC 4:2:2, Ada — нет ([NVIDIA NVDEC Guide 13.0](https://docs.nvidia.com/video-technologies/video-codec-sdk/13.0/nvdec-video-decoder-api-prog-guide/index.html), подробно — в Intel-заметке выше).

## 4. Планки памяти на idealo сегодня (30.09.2026)

Выдача: [SO-DIMM DDR5, 16 ГБ, по цене — 397 карточек](https://www.idealo.de/preisvergleich/ProductCategory/4552F102189756-102193939-102286859-107683716.html?sortKey=minPrice).

**DDR5-5600 SO-DIMM, 16 ГБ (1 модуль):**

| Модуль | ab, € · предл. | Источник |
|---|---|---|
| Kingston ValueRAM `KVR56S46BS8-16` | **187,56** (Avanturis) · 1 — отдельная карточка; основная карточка — ab 288,77 · 31 | [карточка 187,56 €](https://www.idealo.de/preisvergleich/OffersOfProduct/213624753.html), [поиск](https://www.idealo.de/preisvergleich/MainSearchProductCategory.html?q=KVR56S46BS8-16) |
| Lenovo `4X71M23186` (ThinkPad, DDR5-5600) | 199,90 · 5 | [выдача](https://www.idealo.de/preisvergleich/ProductCategory/4552F102189756-102193939-102286859-107683716.html?sortKey=minPrice) |
| Patriot `PSD516G560081S` | 233,90 · 9 | там же |
| Corsair Vengeance `CMSX16GX5M1A5600C48` | 239,99 · 10 | там же |
| Crucial `CT16G56C46S5` | **243,90** · 32 | там же |
| ADATA Premier `AD5S560016G-S` | 263,55 · 12 (при проверке 30.09 — 259,00) | там же |
| Kingston FURY Impact `KF556S40IB-16` | 269,00 · 32 | там же |

**DDR5-4800 / 5200, 16 ГБ:** Integral `IN5V16GNHRBX` — 193,40 € (5 предл.), Patriot `PSD516G480081S` — 209,90 € (8), Crucial `CT16G48C40S5` — 233,90 € (29); DDR5-5200 Corsair `CMSX16GX5M1A5200C44` — 272,98 € (не дешевле). Та же [выдача](https://www.idealo.de/preisvergleich/ProductCategory/4552F102189756-102193939-102286859-107683716.html?sortKey=minPrice).
DDR5-4800 ставить в ноутбук с DDR5-5600 можно, но пара заработает на 4800 (общий принцип — не проверено для конкретных моделей).

**Комплект 2×16 DDR5-5600:** Crucial `CT2K16G56C46S5` — **ab 475,25 €**, 25 предложений ([поиск idealo](https://www.idealo.de/preisvergleich/MainSearchProductCategory.html?q=CT2K16G56C46S5)). Kingston `KVR56S46BS8K2-32` на idealo — только чужие/совместимые модули.

**DDR4-3200 SO-DIMM (для HP 15-fc, ThinkBook 16 G6 ABP):** 16 ГБ G.Skill `F4-3200C22S-16GRS` — ab 113,17 € (22 предл.), 2×16 `F4-3200C22D-32GRS` — ab 257,69 € (11) — заголовки карточек idealo 30.09 ([16 ГБ](https://www.idealo.de/preisvergleich/OffersOfProduct/200683989.html), [2×16](https://www.idealo.de/preisvergleich/OffersOfProduct/200610619.html)).

**Для расчёта «16 ГБ + планка» (DDR5):** реальная планка — **~234–244 €** (Crucial/Patriot, много магазинов); 187,56 € — одно предложение, может исчезнуть.
Значит, ноутбук с 1×16 + свободным слотом должен стоить **≤ ~856–866 €** (или ≤ 912 € при планке за 188 €). С 2×8 — ≤ ~625 €.
По сравнению с Intel-заметкой (220–340 € за 16 ГБ, 480–615 € за 2×16 — [market.md, 1.3](../../Intel/notes/market.md)) на idealo сегодня немного дешевле, но порядок тот же.

## 5. Что на полках по поколениям AMD

Кодовые имена — из поля «Prozessor Codename» в карточках idealo и со страниц amd.com. Подробная карта имён — в `amd-cpu.md` (пишется параллельно).

| Кодовое имя (серия) | CPU / iGPU | Запуск | Что в скане (15–16", 1 ТБ) | Цены 32 ГБ / 1 ТБ | Память |
|---|---|---|---|---|---|
| **Gorgon Point** (Ryzen AI 400) | Zen 5 (+Zen 5c) / RDNA 3.5, 840M | 05.01.2026 ([amd.com AI 7 445](https://www.amd.com/en/products/processors/laptop/ryzen/ai-400-series/amd-ryzen-ai-7-445.html), [AI 5 430](https://www.amd.com/en/products/processors/laptop/ryzen/ai-400-series/amd-ryzen-ai-5-430.html)) | AI 7 445: ThinkPad L16 G3, IdeaPad 5 2-in-1 15, IdeaPad Slim 5a 16, Vivobook 16 M1607GA | от 1267 € (2×16) | у Lenovo — SO-DIMM |
| **Krackan Point** (Ryzen AI 300) | Zen 5 + Zen 5c / RDNA 3.5 (820M–860M) | 18.02.2025; AI 5 330 — 30.07.2025 ([AI 7 350](https://www.amd.com/en/products/processors/laptop/ryzen/ai-300-series/amd-ryzen-ai-7-350.html), [AI 5 340](https://www.amd.com/en/products/processors/laptop/ryzen/ai-300-series/amd-ryzen-ai-5-340.html), [AI 5 330](https://www.amd.com/en/products/processors/laptop/ryzen/ai-300-series/amd-ryzen-ai-5-330.html)) | самый частый CPU в выдаче (AI 7 350 — 26 карточек 32/1 ТБ) | 986–1149 € (Acer, распайка); 2×16 — только б/у | часто LPDDR5X распайка; IdeaPad Slim 5 16AKP10 — SO-DIMM |
| **Strix Point** (Ryzen AI 9 HX 370) | Zen 5 / RDNA 3.5 | — (amd.com не открывал) | 14 карточек 32/1 ТБ | дороже 1250 € в выдаче | — |
| **Hawk Point** (Ryzen 200 = переименованные 8040) | Zen 4 / RDNA 3 (740M–780M) | 18.02.2025 ([R5 220](https://www.amd.com/en/products/processors/laptop/ryzen/200-series/amd-ryzen-5-220.html), [R5 230](https://www.amd.com/en/products/processors/laptop/ryzen/200-series/amd-ryzen-5-230.html), [R7 260](https://www.amd.com/en/products/processors/laptop/ryzen/200-series/amd-ryzen-7-260.html)) | R5 220/230, R7 250 (19 карточек), R7 260 — почти все игровые с RTX | 1068–1199 € (ThinkBook G9, E16 G3, ProBook G1a) | SO-DIMM |
| Hawk Point-HS / Phoenix (8040HS / 7040HS) | Zen 4 / RDNA 3 | 2023–2024 | 8645HS, 8840HS, 8845HS, 7840HS | 16 ГБ-модели 899–1049 € | часто LPDDR5X |
| **Rembrandt-R** (Ryzen 7035) | Zen 3+ / RDNA 2 (660M/680M) | Q2 2023 ([R5 7535HS](https://www.amd.com/en/products/processors/laptop/ryzen/7000-series/amd-ryzen-5-7535hs.html), [R7 7735HS](https://www.amd.com/en/products/processors/laptop/ryzen/7000-series/amd-ryzen-7-7735hs.html)) | ThinkBook 16 G7 ARP, ThinkPad E16 G2, IdeaPad Slim 3 ARP10 | **999–1199 €** (2×16) | SO-DIMM (или 8 распайка + слот) |
| **Barcelo-R** (Ryzen 7030) | Zen 3 / Vega | Q1 2023 ([R7 7730U](https://www.amd.com/en/products/processors/laptop/ryzen/7000-series/amd-ryzen-7-7730u.html)) | HP 15-fc, ThinkBook 16 G6 ABP, IdeaPad Slim 3 ABR8 | 929–999 € | DDR4 |
| Barcelo / Lucienne / Mendocino | Zen 3 / Zen 2 / Zen 2 | 2021–2022 | 5825U, 5500U, 5700U, 7520U | 659–729 € | DDR4 |
| Fire Range (Ryzen 9 9955HX) | Zen 5 (десктопный кристалл) | — | ROG Strix G16 | от 1549 € (16 ГБ) | SO-DIMM |

Выводы:
- **Дешёвая AMD-полка ≤ 1100 € — это Zen 3/3+ (2023) и Zen 4 Hawk Point.** Zen 5 в бюджете — только с распайкой.
- «Ryzen 200» и «Ryzen 7035/7030» — переименования старых кристаллов: в серии 7000 архитектуру выдаёт последняя цифра, серии 200 — это Hawk Point (см. `CLAUDE.md`, ловушка 1).
- Ryzen AI 5 330 — 4 ядра, из них одно полноценное Zen 5 (amd.com: «1x Zen 5») и 820M. Для 4K-монтажа слабый.

### 5.1 Что выйдет в ближайшие 3–6 месяцев

- **Gorgon Point уже вышел** (январь 2026). По утечке роадмапа, он заменил Strix/Krackan в премиум-сегменте, а Hawk Point 8C остаётся в младшем мейнстриме **до 2-го полугодия 2027** ([Tom's Hardware, 25.08.2025](https://www.tomshardware.com/pc-components/cpus/amd-mobile-cpu-roadmap-leak-claims-zen-6-arrives-in-2027) — утечка, не официально).
- **Medusa (Zen 6):** на слайде AMD (Financial Analyst Day, ноябрь 2025) — «Medusa»-APU в **2027** ([PC Gamer, 12.11.2025](https://www.pcgamer.com/hardware/processors/amd-confirms-next-gen-zen-6-cpus-to-launch-in-2026-and-medusa-apus-to-launch-in-2027/)).
  По той же утечке: Medusa Point — для премиум-ноутбуков в 2027, «Medusa Baby» для мейнстрима — во 2-м полугодии 2027 ([Tom's Hardware, 25.08.2025](https://www.tomshardware.com/pc-components/cpus/amd-mobile-cpu-roadmap-leak-claims-zen-6-arrives-in-2027)).
  Анонс на CES 2027 — только ожидания в прессе, **не проверено**.
- **Вывод:** до марта 2027 в классе ≤ 1100 € нового поколения AMD не будет; ждать смысла нет. Цены на память растут — см. [market.md, 1.1–1.2](../../Intel/notes/market.md).

### 5.2 Доля AMD в ноутбуках

- **Мир, Mercury Research, Q2 2026:** AMD — **28,9 %** мобильных x86 CPU (Q1 2026 — 28,3 %, Q2 2025 — 20,6 %); Intel — 71,1 %. Intel в Q2 резко нарастил поставки мобильных CPU ([Tom's Hardware, 22.08.2026](https://www.tomshardware.com/pc-components/cpus/desktop-cpu-shipments-crater-20-percent-amid-high-component-costs-but-amd-gains-record-share-despite-ugly-desktop-processor-market-intel-floods-laptop-market-with-millions-of-cpus-but-amd-still-sets-all-time-share-records)).
- **Германия:** публичных данных не нашёл — **не проверено**.
- По моему скану idealo (15–16", 32 ГБ, 1 ТБ): 183 карточки AMD против 589 Intel — **~24 %** от суммы (это число карточек, а не продажи).

## 6. AMD против Intel: 32 ГБ / 1 ТБ, 16", цены 30.09.2026

| Класс | AMD | Intel | Разница |
|---|---|---|---|
| Бизнес 16", 2×16 SO-DIMM, младший CPU | ThinkBook 16 G9 AHP `21UT004QGE` (R5 220) — **1068,01 €** | ThinkBook 16 G8 IAL `21SK0083GE` (Core Ultra 5 225U) — 1122 € ([Intel REPORT](../../Intel/REPORT.md); idealo 30.09 — ab 1122,00 €) | **AMD дешевле на ~54 € (~5 %)** |
| То же, старший CPU | `21UT000RGE` (R7 250, 780M) — 1188 € | `21SK007KGE` (Core Ultra 7 255H, Arc 140T) — 1349 € в Intel REPORT, ab 1399 € на idealo 30.09 | AMD дешевле на ~160–210 €, но 255H — более новый и сильный CPU (сравнение производительности — не проверено здесь) |
| Самый дешёвый новый «2×16 с завода», CPU 2023 г. | ThinkBook 16 G7 ARP `21MW00AYGE` (R5 7535HS) — 998,99 € | Acer Aspire Go 16 `NX.JS9EG.005` (i9-13900H, 2×16) — 899 €; IdeaPad Slim 5 16IRH10 `83HS00BLGE` (i7-13620H) — 995 € ([Intel REPORT](../../Intel/REPORT.md)) | **Intel дешевле на 0–100 €** |
| Zen 5 / Lunar Lake, 32 ГБ распайка | Acer Aspire 16 AI `NX.JLLEG.009` (AI 7 350) — 1080,25 € | ThinkPad E16 G3 `22AY004XGE` (Core Ultra 5 228V) — 1203,78 € ([Intel REPORT](../../Intel/REPORT.md)) | AMD дешевле на ~120 € (разные классы) |
| С RTX 5060, 16 ГБ, 1 ТБ | GigaByte A16 `3VHK3DE894SH` (R7 260) — 1099 € | Intel + RTX 5060 с 16 ГБ — от ~1049–1100 € ([candidates-gpu.md](../../Intel/notes/candidates-gpu.md)) | примерно равно |
| Выбор на idealo (15–16", 32/1 ТБ) | 183 карточки | 589 карточек ([выдача Intel](https://www.idealo.de/preisvergleich/ProductCategory/3751F699493-1568565-2682401-7612877-107335535.html?sortKey=minPrice)) | у Intel в 3 раза больше |

- В выдаче Intel есть и то, чего нет у AMD: например, HP OmniBook 7 AI 16 `16-ay0770ng` (Core Ultra 7 255H, 32/1 ТБ) — ab 979,30 € (idealo 30.09; раскладка памяти — не проверено).
- **Итог:** AMD не «дешевле вообще». В паре одинаковых бизнес-шасси (ThinkBook 16 G9 AHP vs G8 IAL) AMD дешевле на 5–15 %. Но у AMD меньше выбор, в бюджете нет Zen 5 с 2×16, а у Intel есть дешёвые Raptor Lake с 2×16.
- Главный вопрос для монтажа — кодеки (4:2:2), а не цена: см. `amd-codecs.md` и [`../../Intel/notes/intel-cpu.md`](../../Intel/notes/intel-cpu.md).

## 7. Ловушки, найденные в скане (AMD)

| Ловушка | Пример | Как проверить |
|---|---|---|
| **Отключённый HEVC** | HP ProBook 4 G1a 16 — «Hardware acceleration for CODEC H.265/HEVC … is disabled on this platform» ([QuickSpecs c09111176, v15, 16.06.2026](https://www8.hp.com/h20195/v2/GetDocument.aspx?docname=c09111176)). Это 8 из 36 карточек до 1330 €, включая самую дешёвую подходящую по памяти (`C7SP9ES`, 899 €) | QuickSpecs каждого HP |
| **«32 ГБ» = 1×32** | ThinkPad E16 Gen 3 AMD `21ST004GGE`, `21ST001YGE` ([PSREF](https://psref.lenovo.com/Detail/ThinkPad/ThinkPad_E16_Gen_3_AMD?M=21ST004GGE)) | строка Memory в PSREF |
| **«16 ГБ» = 2×8** | IdeaPad Slim 5 16AKP10 `83HY006XGE`, `83HY002SGE`; IdeaPad Slim 5a 16AGP11 `83S2000BGE`, `83S2004HGE` ([PSREF](https://psref.lenovo.com/Detail/IdeaPad/IdeaPad_Slim_5_16AGP11?M=83S2000BGE)) | PSREF |
| **Потолок 24 ГБ** | IdeaPad Slim 3 ARP10 (8 распайка + 1 слот, «Up to 24GB») ([PSREF](https://psref.lenovo.com/Detail/IdeaPad/IdeaPad_Slim_3_16ARP10?M=83K8006EGE)) | Max Memory в PSREF |
| **Распайка без слотов** | IdeaPad Slim 3 ABR8 (16 ГБ DDR4), IdeaPad 5 2-in-1 16AKP10, Acer Aspire 16 AI, Swift Air 16 (Icecat) | даташит / Icecat |
| **Переименованный старый CPU** | Ryzen 5 220/230, 7 250/260 = Hawk Point (Zen 4); 7535HS/7735HS = Rembrandt-R (Zen 3+); 7530U/7730U = Barcelo-R (Zen 3) — [amd.com](https://www.amd.com/en/products/processors/laptop/ryzen/200-series/amd-ryzen-5-220.html) | поле «Former Codename» на amd.com |
| **idealo ошибается в характеристиках** | E16 Gen 2 `21M5002DGE`: idealo — R5 7535HS, PSREF — R7 7735HS; LG Gram 15 `15Z80T-G.AU88G`: idealo — 32 ГБ, предложение — «16GB RAM»; CSL C15 90610 — в одной карточке 5500U и 7430U; ASUS M1607KA-MB172W: карточка — AI 7 350, предложение — AI 5 330 (найдено при проверке) | сверять с даташитом и названием предложения |
| **Дешёвое «ab» от необычного продавца** | ThinkPad L16 G3 `21XC002BGE`: 1171,23 € у buyzoxs.de с пометкой «differenzbesteuert» (обычно так продают б/у или восстановленное — не проверено для этого магазина); следующее новое — 1675,97 € | читать название и условия предложения |
| **Сборки продавца под «чужим» номером** | «HP 255 G10 884420874911», «HP 15 4260260631727» — вместо парт-номера EAN, «individuell konfigurierbar» | нет HP P/N → не заводской SKU |
| **Без блока питания** | IdeaPad Slim 5a 16AGP11, IdeaPad 5 2-in-1 15AGP11 — «No Power Adapter» в PSREF | +~22–41 € за USB-C-зарядку (цены — [market.md](../../Intel/notes/market.md) / Intel REPORT) |
| **Только б/у** | Лучшие AMD Zen 5 с 2×16 (`83HY0061GE`, `83HY008CGE`) сейчас есть только «gebraucht» | метка «gebraucht» в выдаче |

Общие ловушки idealo («ab», Marketplace, B2B-магазины, серый импорт, «aufgerüstet») — в [market.md, раздел 4.2](../../Intel/notes/market.md). Явных «aufgerüstet» в названиях AMD-предложений до 1330 € я не встретил (проверял названия первых предложений в карточках).

## 8. Где и когда покупать — AMD-специфика

- Магазины и сроки возврата — [market.md, раздел 3](../../Intel/notes/market.md). В AMD-скане первыми чаще всего стоят notebooksbilliger.de (30 дней возврата), galaxus.de (30 дней), cyberport.de (30 дней), computeruniverse.net, а также мелкие easynotebooks.de, technikdeals24.de, heinzsoft-shop.de, electronic4you.de, cyclotron.de — их AGB (частный покупатель или только бизнес) **не проверено**.
- Распродажи: Prime Deal Days 6–7.10, Black Week 23–30.11 — [market.md, 2.4](../../Intel/notes/market.md).
- Цель для Preiswecker: `21UT004QGE` ≤ ~1000 €, `21UT000RGE` ≤ 1100 €, `83UM002BGE` ≤ 1100 €, новые `83HY008CGE` / `83HY0061GE`.

## 9. Что не проверено

- Раскладка памяти: HP 15-fc0677ng `C8TT7EA` (32 ГБ DDR4), HP 15-fc0680ng/0676ng, HP OmniBook 3 (DE-SKU), ASUS Vivobook 16 M1607GA/KA по конкретным SKU (у серии — 16 on board + слот) и S16 M3607HA, GigaByte A16 `3VHK3DE894SH`, Acer Swift Go 16, HP ProBook 4 G1a `C7SP9ES` (2×16 или 1×32 — не важно, модель исключена из-за HEVC).
- CPU у ASUS M1607KA-MB172W (AI 7 350 или AI 5 330).
- HEVC: HP consumer (15-fc, OmniBook), HP EliteBook 8 G1a, Acer (Nokia) — см. `hevc-amd.md`.
- AGB мелких магазинов (B2B или нет).
- Доля AMD именно в Германии.
- Сроки Medusa — официально только «2027».

## Источники

**idealo.de (скан 30.09.2026, Chrome пользователя):**
- [AMD, 15–16", 32 ГБ, 1 ТБ](https://www.idealo.de/preisvergleich/ProductCategory/3751F699493-848110-1568565-2682401-7612877.html?sortKey=minPrice)
- [AMD, 15–16", 16 ГБ, 1 ТБ, стр. 1](https://www.idealo.de/preisvergleich/ProductCategory/3751F699493-848110-1568565-2682401-7612874.html?sortKey=minPrice), [стр. 2](https://www.idealo.de/preisvergleich/ProductCategory/3751F699493-848110-1568565-2682401-7612874I16-15.html?sortKey=minPrice)
- [AMD + RTX 5050/5060/5070/4060, 1 ТБ, 15–16"](https://www.idealo.de/preisvergleich/ProductCategory/3751F699493-848110-1568565-2682401-104023766-106697019-106745465-106843055.html?sortKey=minPrice)
- [Intel, 15–16", 32 ГБ, 1 ТБ (для сравнения)](https://www.idealo.de/preisvergleich/ProductCategory/3751F699493-1568565-2682401-7612877-107335535.html?sortKey=minPrice)
- [Контрольный поиск «32GB 1TB», AMD](https://www.idealo.de/preisvergleich/ProductCategory/3751F848110.html?q=32GB%201TB&sortKey=minPrice)
- [SO-DIMM DDR5 16 ГБ](https://www.idealo.de/preisvergleich/ProductCategory/4552F102189756-102193939-102286859-107683716.html?sortKey=minPrice), [Kingston KVR56S46BS8-16 (187,56 €)](https://www.idealo.de/preisvergleich/OffersOfProduct/213624753.html), [поиск KVR56S46BS8-16](https://www.idealo.de/preisvergleich/MainSearchProductCategory.html?q=KVR56S46BS8-16), [CT2K16G56C46S5](https://www.idealo.de/preisvergleich/MainSearchProductCategory.html?q=CT2K16G56C46S5), [DDR4 16 ГБ](https://www.idealo.de/preisvergleich/OffersOfProduct/200683989.html), [DDR4 2×16](https://www.idealo.de/preisvergleich/OffersOfProduct/200610619.html)
- Карточки товаров — ссылки под таблицами разделов 1–2.

**Даташиты:**
- Lenovo PSREF: [ThinkBook 16 G9 AHP 21UT004QGE](https://psref.lenovo.com/Detail/ThinkBook/ThinkBook_16_G9_AHP?M=21UT004QGE), [21UT000RGE](https://psref.lenovo.com/Detail/ThinkBook/ThinkBook_16_G9_AHP?M=21UT000RGE), [ThinkBook 16 G7 ARP 21MW00AYGE](https://psref.lenovo.com/Detail/ThinkBook/ThinkBook_16_G7_ARP?M=21MW00AYGE), [21MW007VGE](https://psref.lenovo.com/Detail/ThinkBook/ThinkBook_16_G7_ARP?M=21MW007VGE), [ThinkBook 16 G6 ABP 21KK0074GE](https://psref.lenovo.com/Detail/ThinkBook/ThinkBook_16_G6_ABP?M=21KK0074GE), [ThinkPad E16 Gen 3 AMD 21ST004GGE](https://psref.lenovo.com/Detail/ThinkPad/ThinkPad_E16_Gen_3_AMD?M=21ST004GGE), [21ST001YGE](https://psref.lenovo.com/Detail/ThinkPad/ThinkPad_E16_Gen_3_AMD?M=21ST001YGE), [ThinkPad E16 Gen 2 AMD 21M5002DGE](https://psref.lenovo.com/Detail/ThinkPad/ThinkPad_E16_Gen_2_AMD?M=21M5002DGE), [21M5002VGE](https://psref.lenovo.com/Detail/ThinkPad/ThinkPad_E16_Gen_2_AMD?M=21M5002VGE), [ThinkPad L16 Gen 3 AMD 21XC002BGE](https://psref.lenovo.com/Detail/ThinkPad/ThinkPad_L16_Gen_3_AMD?M=21XC002BGE), [IdeaPad Slim 5 16AKP10 83HY0061GE](https://psref.lenovo.com/Detail/IdeaPad/IdeaPad_Slim_5_16AKP10?M=83HY0061GE), [83HY008CGE](https://psref.lenovo.com/Detail/IdeaPad/IdeaPad_Slim_5_16AKP10?M=83HY008CGE), [83HY006XGE](https://psref.lenovo.com/Detail/IdeaPad/IdeaPad_Slim_5_16AKP10?M=83HY006XGE), [83HY002SGE](https://psref.lenovo.com/Detail/IdeaPad/IdeaPad_Slim_5_16AKP10?M=83HY002SGE), [IdeaPad Slim 5 16AGP11 83S2000BGE](https://psref.lenovo.com/Detail/IdeaPad/IdeaPad_Slim_5_16AGP11?M=83S2000BGE), [83S2004HGE](https://psref.lenovo.com/Detail/IdeaPad/IdeaPad_Slim_5_16AGP11?M=83S2004HGE), [IdeaPad 5 2-in-1 15AGP11 83UM002BGE](https://psref.lenovo.com/Detail/IdeaPad/IdeaPad_5_2_in_1_15AGP11?M=83UM002BGE), [IdeaPad 5 2-in-1 16AKP10 83KU0012GE](https://psref.lenovo.com/Detail/IdeaPad/IdeaPad_5_2_in_1_16AKP10?M=83KU0012GE), [IdeaPad Slim 3 16ARP10 83K8006EGE](https://psref.lenovo.com/Detail/IdeaPad/IdeaPad_Slim_3_16ARP10?M=83K8006EGE), [15ARP10 83K700ENGE](https://psref.lenovo.com/Detail/IdeaPad/IdeaPad_Slim_3_15ARP10?M=83K700ENGE), [IdeaPad Slim 3 16ABR8 82XR009WGE](https://psref.lenovo.com/Detail/IdeaPad/IdeaPad_Slim_3_16ABR8?M=82XR009WGE), [82XR0094GE](https://psref.lenovo.com/Detail/IdeaPad/IdeaPad_Slim_3_16ABR8?M=82XR0094GE), [15ABR8 82XM008AGE](https://psref.lenovo.com/Detail/IdeaPad/IdeaPad_Slim_3_15ABR8?M=82XM008AGE)
- HP: [QuickSpecs ProBook 4 G1a 16, c09111176 v15 (16.06.2026)](https://www8.hp.com/h20195/v2/GetDocument.aspx?docname=c09111176)
- Icecat (open): [Acer NX.DL5EG.002](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Acer&ProductCode=NX.DL5EG.002), [Acer NX.DL5EG.001](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Acer&ProductCode=NX.DL5EG.001), [Acer NX.JLLEG.009](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Acer&ProductCode=NX.JLLEG.009), [ASUS M1607GA-MB020W](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=ASUS&ProductCode=M1607GA-MB020W)
- HP OmniBook 3 (US-SKU, навигация): [laptopmedia](https://laptopmedia.com/laptop-specs/hp-omnibook-3-8/)

**amd.com (кодовые имена, даты):** [Ryzen AI 7 445](https://www.amd.com/en/products/processors/laptop/ryzen/ai-400-series/amd-ryzen-ai-7-445.html), [Ryzen AI 5 430](https://www.amd.com/en/products/processors/laptop/ryzen/ai-400-series/amd-ryzen-ai-5-430.html), [Ryzen AI 7 350](https://www.amd.com/en/products/processors/laptop/ryzen/ai-300-series/amd-ryzen-ai-7-350.html), [Ryzen AI 5 340](https://www.amd.com/en/products/processors/laptop/ryzen/ai-300-series/amd-ryzen-ai-5-340.html), [Ryzen AI 5 330](https://www.amd.com/en/products/processors/laptop/ryzen/ai-300-series/amd-ryzen-ai-5-330.html), [Ryzen 5 220](https://www.amd.com/en/products/processors/laptop/ryzen/200-series/amd-ryzen-5-220.html), [Ryzen 5 230](https://www.amd.com/en/products/processors/laptop/ryzen/200-series/amd-ryzen-5-230.html), [Ryzen 7 260](https://www.amd.com/en/products/processors/laptop/ryzen/200-series/amd-ryzen-7-260.html), [Ryzen 5 7535HS](https://www.amd.com/en/products/processors/laptop/ryzen/7000-series/amd-ryzen-5-7535hs.html), [Ryzen 7 7735HS](https://www.amd.com/en/products/processors/laptop/ryzen/7000-series/amd-ryzen-7-7735hs.html), [Ryzen 7 7730U](https://www.amd.com/en/products/processors/laptop/ryzen/7000-series/amd-ryzen-7-7730u.html)

**billiger.de (история цен):** [ThinkBook 16 G9 AHP 21UT004QGE](https://www.billiger.de/products/5510914032-lenovo-thinkbook-16-g9-amd-ryzen-5-220-32-gb-ram-1-tb-ssd-win11-pro-21ut004qge), [IdeaPad 5 2-in-1 15AGP11 83UM002BGE](https://www.billiger.de/pricelist/5781548420-lenovo-ideapad-5-2-in-1-15agp11-15-3-amd-ryzen-ai-7-445-32-gb-ram-1-tb-ssd-83um002bge)

**Роадмап и доля рынка:**
- [PC Gamer, 12.11.2025 — слайд AMD: Medusa в 2027, Gorgon Point в 2026](https://www.pcgamer.com/hardware/processors/amd-confirms-next-gen-zen-6-cpus-to-launch-in-2026-and-medusa-apus-to-launch-in-2027/)
- [Tom's Hardware, 25.08.2025 — утечка мобильного роадмапа AMD](https://www.tomshardware.com/pc-components/cpus/amd-mobile-cpu-roadmap-leak-claims-zen-6-arrives-in-2027)
- [Tom's Hardware, 22.08.2026 — Mercury Research, Q2 2026](https://www.tomshardware.com/pc-components/cpus/desktop-cpu-shipments-crater-20-percent-amid-high-component-costs-but-amd-gains-record-share-despite-ugly-desktop-processor-market-intel-floods-laptop-market-with-millions-of-cpus-but-amd-still-sets-all-time-share-records)
- Навигация по Gorgon Point: [ultrabookreview — список ноутбуков](https://www.ultrabookreview.com/74602-amd-gorgon-point-laptops/), [videocardz — ASUS: продажи с 22.01](https://videocardz.com/newz/asus-confirms-amd-ryzen-ai-400-gorgon-point-laptops-are-set-to-launch-january-22nd) (не открывал)

**Кодеки NVIDIA:** [NVDEC Programming Guide, Video Codec SDK 13.0](https://docs.nvidia.com/video-technologies/video-codec-sdk/13.0/nvdec-video-decoder-api-prog-guide/index.html)

**Проект:** [`../../Intel/notes/market.md`](../../Intel/notes/market.md), [`../../Intel/REPORT.md`](../../Intel/REPORT.md), [`../../Intel/notes/candidates-gpu.md`](../../Intel/notes/candidates-gpu.md), [`../../Intel/notes/hevc-audit.md`](../../Intel/notes/hevc-audit.md), [`../../Intel/notes/intel-cpu.md`](../../Intel/notes/intel-cpu.md)

## Проверка (скептик, 30.09.2026)

Проверял по первоисточникам: PSREF (PDF-выгрузка `psref.lenovo.com/api/model/pdfexport/singleModel?model_code=<MTM>`), amd.com (страницы моделей), HP QuickSpecs, Icecat, asus.com, billiger.de, Tom's Hardware, PC Gamer, NVIDIA. idealo — в Chrome пользователя, своя вкладка, 30.09.2026; капчи не было, ничего не отправлял.

**Итог:** выбор из заметки держится. Лучший вариант в бюджете — по-прежнему `21UT004QGE`. Исправлено 4 утверждения: ASUS «единственная зацепка», CPU у M1607KA, условный расчёт для GigaByte, формулировка доли рынка. Найден соседний SKU `21UT004EGE` (2×16, 512 ГБ, 894 €).

| # | Утверждение | Вердикт | Источник / что нашёл |
|---|---|---|---|
| 1 | `21UT004QGE`: R5 220, 2×16 DDR5-5600, до 64 ГБ, M.2 2242 + свободный M.2 2280, 400 нит 45 % NTSC, 48 Втч, Win 11 Pro | **подтверждено** | [PSREF](https://psref.lenovo.com/Detail/ThinkBook/ThinkBook_16_G9_AHP?M=21UT004QGE): «2x 16GB SODIMM DDR5-5600», «Two DDR5 SODIMM slots», «One M.2 2242 … One M.2 2280» |
| 2 | R5 220 / 230 / 250 / 260 — Hawk Point, Zen 4; iGPU 740M / 760M / 780M / 780M; запуск 18.02.2025 | **подтверждено** | amd.com: [R5 220](https://www.amd.com/en/products/processors/laptop/ryzen/200-series/amd-ryzen-5-220.html) «Former Codename: Hawk Point», «2x Zen 4», 740M, 2/18/2025; [R5 230](https://www.amd.com/en/products/processors/laptop/ryzen/200-series/amd-ryzen-5-230.html) 760M; [R7 260](https://www.amd.com/en/products/processors/laptop/ryzen/200-series/amd-ryzen-7-260.html) 780M |
| 3 | 7535HS / 7735HS — Rembrandt-R, Zen 3+, Q2 2023; 7730U — Barcelo-R, Zen 3, Q1 2023 | **подтверждено** | amd.com: [7535HS](https://www.amd.com/en/products/processors/laptop/ryzen/7000-series/amd-ryzen-5-7535hs.html), [7735HS](https://www.amd.com/en/products/processors/laptop/ryzen/7000-series/amd-ryzen-7-7735hs.html), [7730U](https://www.amd.com/en/products/processors/laptop/ryzen/7000-series/amd-ryzen-7-7730u.html) |
| 4 | Krackan: AI 7 350 (8 ядер, 860M), AI 5 340 (6, 840M) — 18.02.2025; AI 5 330 — 4 ядра, «1x Zen 5», 820M, 30.07.2025. Gorgon Point AI 7 445 / AI 5 430 — 05.01.2026 | **подтверждено** | amd.com: [AI 7 350](https://www.amd.com/en/products/processors/laptop/ryzen/ai-300-series/amd-ryzen-ai-7-350.html), [AI 5 330](https://www.amd.com/en/products/processors/laptop/ryzen/ai-300-series/amd-ryzen-ai-5-330.html), [AI 7 445](https://www.amd.com/en/products/processors/laptop/ryzen/ai-400-series/amd-ryzen-ai-7-445.html) («Gorgon Point», 6 ядер, 840M, 1/5/2026). 05.01 — дата запуска на amd.com, а не начала продаж |
| 5 | ThinkBook 16 G7 ARP `21MW00AYGE` (R5 7535HS) и `21MW007VGE` (R7 7735HS): 2×16 DDR5-4800, 2 слота M.2 2280, 45 Втч | **подтверждено** | PSREF [00AY](https://psref.lenovo.com/Detail/ThinkBook/ThinkBook_16_G7_ARP?M=21MW00AYGE), [007V](https://psref.lenovo.com/Detail/ThinkBook/ThinkBook_16_G7_ARP?M=21MW007VGE) |
| 6 | ThinkBook 16 G6 ABP `21KK0074GE`: R7 7730U, 2×16 DDR4-3200 SO-DIMM, 71 Втч | **подтверждено** | [PSREF](https://psref.lenovo.com/Detail/ThinkBook/ThinkBook_16_G6_ABP?M=21KK0074GE). Добавка: оба слота M.2 — PCIe 3.0 x4 |
| 7 | ThinkPad E16 Gen 3 AMD `21ST004GGE` / `21ST001YGE` — 1×32 ГБ, одноканал | **подтверждено** | PSREF [004G](https://psref.lenovo.com/Detail/ThinkPad/ThinkPad_E16_Gen_3_AMD?M=21ST004GGE), [001Y](https://psref.lenovo.com/Detail/ThinkPad/ThinkPad_E16_Gen_3_AMD?M=21ST001YGE): «1x 32GB SODIMM DDR5-5600», второй слот свободен. Запись в `MEMORY.md` («Находки») действительно надо поправить |
| 8 | HP ProBook 4 G1a 16: аппаратный HEVC отключён; QuickSpecs c09111176 v15 от 16.06.2026; 2 слота SO-DIMM | **подтверждено** | [QuickSpecs c09111176](https://www8.hp.com/h20195/v2/GetDocument.aspx?docname=c09111176), с. 5: «Hardware acceleration for CODEC H.265/HEVC … is disabled on this platform»; «2 SODIMM», «Version 15 — June 16, 2026». `C7SP9ES` на idealo — R5 230, 32/1 ТБ, FreeDOS, ab 899 € (NBB, nullprozentshop.de) |
| 9 | Acer `NX.JLLEG.009` (AI 7 350) и `NX.DL5EG.002` (AI 5 330) — 32 ГБ распайка | **подтверждено** (с оговоркой) | Icecat [JLLEG.009](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Acer&ProductCode=NX.JLLEG.009): «LPDDR5x-SDRAM», 32 ГБ; [DL5EG.002](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Acer&ProductCode=NX.DL5EG.002): «LPDDR5-SDRAM». Слова «verlötet» в Icecat нет: вывод о распайке — из типа LPDDR5/5X |
| 10 | IdeaPad Slim 5 16AKP10 `83HY0061GE` / `83HY008CGE` — 2×16 SO-DIMM; новых предложений нет, только б/у | **подтверждено** | PSREF [0061](https://psref.lenovo.com/Detail/IdeaPad/IdeaPad_Slim_5_16AKP10?M=83HY0061GE), [008C](https://psref.lenovo.com/Detail/IdeaPad/IdeaPad_Slim_5_16AKP10?M=83HY008CGE) («2x 16GB SODIMM», но «Up to 32GB»); idealo [207280344](https://www.idealo.de/preisvergleich/OffersOfProduct/207280344.html): «Neu (keine Angebote) · B-Ware & Gebraucht ab 877,00 €», [209439304](https://www.idealo.de/preisvergleich/OffersOfProduct/209439304.html) — ab 949,00 € |
| 11 | «Все проверенные Lenovo с 16 ГБ — 2×8, распайка или потолок 24 ГБ» | **подтверждено** | PSREF: `83HY006XGE`, `83HY002SGE`, `83S2000BGE`, `83S2004HGE` — «2x 8GB SODIMM»; `83KU0012GE`, `82XR009WGE` — «soldered, not upgradable»; `83K700ENGE`, `83K8006EGE` — «Up to 24GB (8GB soldered + 16GB SODIMM)». Оговорка: у Lenovo бывает 1×16 + слот (`21UT0041GE`), но с SSD 512 ГБ |
| 12 | «Единственная зацепка» 16 ГБ + планка — ASUS M1607GA-MB020W, «сколько распаяно — не проверено» | **исправлено** | Icecat [M1607GA-MB020W](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=ASUS&ProductCode=M1607GA-MB020W): «On-board + SO-DIMM», 1 слот, до 32 ГБ. У серии на [asus.com/de](https://www.asus.com/de/laptops/for-home/vivobook/asus-vivobook-16-m1607/techspec/): «16GB DDR5 on board», слот свободен, «Dual-channel memory support requires at least one SO-DIMM module». Такая же схема у M1607KA-MB172W (799 €), но там CPU расходится: карточка [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/210698249.html) пишет AI 7 350, единственное предложение — «Ryzen AI 5 330». По SKU — не проверено |
| 13 | Цены idealo 30.09: `21UT004QGE` 1068,01 (39); `21MW00AYGE` 998,99; `21KK0074GE` 999 (1 магазин, дальше 1149); `21MW007VGE` 1080,62; `NX.JLLEG.009` 1080,25; `NX.DL5EG.002` 986,51; GigaByte A16 1099; L16 G3 1171,23 / 1675,97; `83UM002BGE` 1267,07; `21UT000RGE` 1188 | **подтверждено** | idealo, перепроверка 30.09: всё совпало до цента. Только `21UT004QGE` — 1067,82 € (technikdeals24.de), 1068,01 € (heinzsoft-shop.de), 39 предложений. [карточка](https://www.idealo.de/preisvergleich/OffersOfProduct/209122445_-thinkbook-16-g9-21ut004qge-lenovo.html) |
| 14 | Найдено при проверке: `21UT004EGE` (R5 220, 2×16, 512 ГБ, свободный M.2 2280) — ab 894 € | **новое** | [PSREF](https://psref.lenovo.com/Detail/ThinkBook/ThinkBook_16_G9_AHP?M=21UT004EGE), [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/209122443_-thinkbook-16-g9-21ut004ege-lenovo.html) (7 предложений). С SSD 1 ТБ — примерно та же цена, что у `21UT004QGE`; выгода только в объёме диска |
| 15 | billiger.de `21UT004QGE`: 1123 € (02.04) → 1073 €, «медленно дешевеет», минимум — сегодня | **уточнено** | [billiger](https://www.billiger.de/products/5510914032-lenovo-thinkbook-16-g9-amd-ryzen-5-220-32-gb-ram-1-tb-ssd-win11-pro-21ut004qge): lowPrice 1073, 27 предложений, в истории 30.09 — 1072 € (минимум). Но 28.04 был пик 1251 €, так что «медленно дешевеет» не совсем точно |
| 16 | GigaByte A16 `3VHK3DE894SH`: «с планкой ≈ 1287–1343 €» | **исправлено** | Раскладка 16 ГБ не проверена: Icecat — 404, gigabyte.com — 403, в названиях предложений на idealo раскладки нет. Расчёт верен только при 1×16 + свободном слоте; при 2×8 ≈ 1574 € |
| 17 | Планки: Crucial `CT16G56C46S5` 243,90; комплект `CT2K16G56C46S5` 475,25; Kingston `KVR56S46BS8-16` 187,56 (одна карточка) / 288,77 (основная); DDR4 G.Skill 113,17 / 257,69; ADATA 263,55 | **подтверждено**, ADATA — **уточнено** | idealo, 30.09: все цены совпали; ADATA `AD5S560016G-S` теперь ab 259,00 €. Выдача SO-DIMM DDR5 16 ГБ — 397 карточек |
| 18 | 183 карточки AMD против 589 Intel (15–16", 32 ГБ, 1 ТБ); 178 карточек AMD с 16 ГБ | **подтверждено** (с дрейфом) | При повторном открытии тех же фильтров — 181 / 587 / 178 «Ergebnisse». Соотношение ~3,2× не изменилось |
| 19 | AMD против Intel: `21SK0083GE` 1122 €, `21SK007KGE` 1399 € на idealo; Aspire Go 16 `NX.JS9EG.005` 849–899 € | **подтверждено** | idealo 30.09: `21SK0083GE` ab 1122,00, `21SK007KGE` ab 1399,00 (блок «Zurzeit beliebt» на карточке `21UT004QGE`); [Aspire Go 16](https://www.idealo.de/preisvergleich/OffersOfProduct/209373295_-aspire-go-16-ag16-71p-97gf-acer.html) — 849 € (technik-brandenburg.de), 899 € (technowelt24.de, expert.de). Арифметика −54 € (−4,8 %) и −12…15 % верна |
| 20 | Доля AMD 28,9 % (Q2 2026, Mercury Research), Q1 — 28,3 %, год назад — 20,6 %; Intel — 71,1 % | **подтверждено**, формулировка в «Коротко» **исправлена** | [Tom's Hardware, 22.08.2026](https://www.tomshardware.com/pc-components/cpus/desktop-cpu-shipments-crater-20-percent-amid-high-component-costs-but-amd-gains-record-share-despite-ugly-desktop-processor-market-intel-floods-laptop-market-with-millions-of-cpus-but-amd-still-sets-all-time-share-records): «AMD's mobile CPU unit share rose to 28.9%». Это поставки мобильных x86 CPU, а не продажи ноутбуков |
| 21 | Roadmap: Medusa в 2027 (слайд AMD); Hawk Point 8C в мейнстриме до 2-го полугодия 2027 (утечка) | **подтверждено** | [PC Gamer, 12.11.2025](https://www.pcgamer.com/hardware/processors/amd-confirms-next-gen-zen-6-cpus-to-launch-in-2026-and-medusa-apus-to-launch-in-2027/); [Tom's Hardware, 25.08.2025](https://www.tomshardware.com/pc-components/cpus/amd-mobile-cpu-roadmap-leak-claims-zen-6-arrives-in-2027): «…Hawk Point 8C … till the second half of 2027 when it will be replaced by Medusa Baby» |
| 22 | NVDEC Blackwell декодирует H.264/HEVC 4:2:2, Ada — нет | **подтверждено** | [NVDEC Guide 13.0](https://docs.nvidia.com/video-technologies/video-codec-sdk/13.0/nvdec-video-decoder-api-prog-guide/index.html): в строке «Blackwell» — «High 422» и «Main 4:2:2/4:4:4 10/12»; в строке GA10x/AD10x (Ampere/Ada) из 4:2:2/4:4:4 есть только «444 chroma format support» |
| 23 | L16 G3 `21XC002BGE` — один M.2; `83UM002BGE`, `83S2000BGE`, `83S2004HGE` — без блока питания | **подтверждено** | PSREF [21XC002BGE](https://psref.lenovo.com/Detail/ThinkPad/ThinkPad_L16_Gen_3_AMD?M=21XC002BGE) («One M.2 2280»); [83UM002BGE](https://psref.lenovo.com/Detail/IdeaPad/IdeaPad_5_2_in_1_15AGP11?M=83UM002BGE), [83S2000BGE](https://psref.lenovo.com/Detail/IdeaPad/IdeaPad_Slim_5_16AGP11?M=83S2000BGE) — «No Power Adapter» |

Не нашёл ошибок в кодовых именах и поколениях. Не нашёл и путаницы «SO-DIMM ↔ распайка» у Lenovo, HP и Acer. Выдуманных ссылок нет: все открытые ссылки отвечают и показывают то, что написано в заметке. Цены везде с магазином и датой.
