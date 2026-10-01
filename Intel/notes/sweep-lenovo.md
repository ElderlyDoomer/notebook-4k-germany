# Добор Lenovo: полный проход по PSREF (Германия) + цены

_2026-09-30, облачная сессия. Все цены «из облака» (billiger.de, Cyberport, Alternate, Lenovo.de, сниппеты поиска) — **перепроверить на idealo**._
_Уже известные SKU из `candidates-lenovo-hp-dell.md` здесь повторяются только если появились новые факты._

## Коротко

1. **Новый кандидат A: IdeaPad Slim 5 16IMH10 — 83V70037GE** (Core Ultra 9 185H, 2×16 SO-DIMM, 1 ТБ). По PSREF — 2×16, два слота M.2. Продавался на Amazon.de за **1049,49 €** (notebookcheck, 23.08.2026); в сниппете geizhals — 1079,99 € (дата неизвестна). На billiger.de его нет. **Блок питания в комплект не входит** (PSREF: «No Power Adapter»), нужен USB-C PD на 65–100 Вт. Сегодняшняя цена не проверена: Amazon.de из облака отвечает 503. → проверено в браузере 30.09.2026: (п. 1.3) МЕНЯЕТ ВЫВОД: 83V70037GE на idealo нет (ни по P/N, ни в «Variante»); на geizhals предложений нет с 28.08 (п. 2.4), Amazon — «Currently unavailable» (п. 3.1). №8 — «сейчас нет в продаже» ([idealo.de](https://www.idealo.de/preisvergleich/MainSearchProductCategory.html?q=83V70037GE)); (п. 2.4) МЕНЯЕТ ВЫВОД: «1 Angebot 1079,99 €» — 83V70037GE (11–19.08), потом 1049,99 € до 27.08, с 28.08 предложений нет; «1439 €» — другой SKU 83V70065NT (185H 16/512); у 83V70033GE предложений не было ([geizhals.de](https://geizhals.de/lenovo-ideapad-slim-5-16imh10-v228573.html)).
2. **Поправка к 83V70077GE** (24 ГБ + слот, 864 €): по PSREF он тоже продаётся **без блока питания**. К итогу «ноутбук + планка» добавляется зарядка: фирменный Lenovo 65 Вт USB-C — от ~22–28 €.
3. **83HS00BLGE** (i7-13620H, 2×16): минимум за 6 месяцев на billiger — **949 €**, средняя цена — 999 €, сейчас 989,05 €.
4. **22AY004VGE** (E16 Gen 3, Lunar Lake 228V, 32 ГБ распайка, экран WUXGA): минимум за 6 месяцев — **1078,67 €**, сейчас 1242,62 €. Это B-список: брать при просадке.
5. **21MS004SGE** (ThinkBook 16 G7, 125U, 2×16): в сниппете geizhals «ab € 994,91 (2026)», дата неизвестна. На billiger сейчас 1241,58 €, минимум за 6 месяцев — 894,98 €.
6. **Конфигуратор Lenovo.de (CTO) не подходит.** ThinkPad E16 Gen 3 с 2×16, 1 ТБ, Core Ultra 5 225H и без ОС стоит **1538,19 €** (цена кликнута в конфигураторе). ThinkBook 16 G8, E16 Gen 4 и ThinkBook 16 G9 выходят ≥ ~1550 €.
7. **HEVC у Lenovo.** В PSREF-даташитах 20 платформ Lenovo нет ни одного упоминания HEVC/H.265, есть только аудиокодеки. В списках моделей с отключённым HEVC (Ars Technica, smith6612.me, 04.2026) Lenovo нет. Статус: **«неизвестно, признаков отключения нет»**.
8. Других Lenovo с Intel, 1 ТБ и 32 ГБ (2×16, или 16/24 + слот) за ≤ 1100 € в продаже не нашёл. Проверены billiger.de (поиск с фильтрами RAM 16/24/32 ГБ + 1 ТБ, сортировка по цене; поиск по MTM), Cyberport (все Lenovo Intel без дискретки до ~1300 €), Alternate, Lenovo.de, hardwareschotte.de, expert.de.

## Охват и метод

- PSREF, фильтр Country = Germany (публичный API psref.lenovo.com). Загружено **2278 MTM** по 60+ платформам, в том числе 17 старых платформ, добавленных в этом проходе.
- Отбор: Intel, SSD 1 ТБ, экран 15–16", подходящая память. Получилось **354 MTM**:
  - 247 — 2×16 SO-DIMM;
  - 58 — 1×16 + свободный слот;
  - 3 — 1×24 + свободный слот;
  - 46 — 32 ГБ распайки.
  В продаже на billiger.de нашлись только **46** из них. Почти все — ThinkPad/ThinkBook дороже 1100 €.
- Нет в PSREF для Германии: IdeaPad Slim 5 16IAH10, 16IRU9 и Slim 5 15IWC11; Lenovo V16 в PSREF нет вовсе.
- Не открывал (блокировка из облака): idealo, geizhals, MediaMarkt, Galaxus, computeruniverse, notebooksbilliger, Amazon.de (503). guenstiger.de и heise-Preisvergleich тоже отвечают 403 — не обходил.

## Кандидаты (новые или с новыми фактами)

| MTM | Модель | CPU | ОЗУ | Цена, € | Итог с планкой/БП | Статус |
|---|---|---|---|---|---|---|
| 83V70037GE | IdeaPad Slim 5 16IMH10 | Ultra 9 185H (Meteor Lake-H) | 2×16 | 1049,49 (Amazon.de, 23.08) / 1079,99 (geizhals, дата?) | +БП ~22–28 → ~1072–1108 | A, цену перепроверить → проверено в браузере 30.09.2026: (п. 1.3) см. строку 8 ([idealo.de](https://www.idealo.de/preisvergleich/MainSearchProductCategory.html?q=83V70037GE)); (п. 2.4) см. строку 8 ([geizhals.de](https://geizhals.de/lenovo-ideapad-slim-5-16imh10-v228573.html)). |
| 83V70077GE | IdeaPad Slim 5 16IMH10 | Ultra 5 135H | 1×24 + слот | 864,38 | +16 ГБ 161–260 +БП → ~1047–1152 | B16, без БП |
| 83HS00BLGE | IdeaPad Slim 5 16IRH10 | i7-13620H (13-е пок.) | 2×16 | 989,05 (6-мес. мин. 949) | 989 | A (старый CPU) |
| 83GW00AHGE | V15 G5 IRL | i7-13620H | 2×16 | ? (предложение 1018,37 — не подтверждено) | — | A по PSREF, цены нет → проверено в браузере 30.09.2026: (п. 1.6) 83GW00A9GE — 598,98 € (easynotebooks); 83GW00FRGE — 636,99 € (nullprozentshop), CPU Core 5 120U — ловушка; 83GW00AHGE на idealo нет ([idealo.de](https://www.idealo.de/preisvergleich/OffersOfProduct/208744735_-v15-g5-83gw00a9ge-lenovo.html)). |
| 22AY004VGE | ThinkPad E16 Gen 3 | Ultra 5 228V | 32 распайка | 1242,62 (6-мес. мин. 1078,67) | — | B-список, ждать |
| 21MS004SGE | ThinkBook 16 G7 IML | Ultra 5 125U | 2×16 | 1241,58 (geizhals «ab 994,91»?) | — | почти подходит |

### IdeaPad Slim 5 16IMH10 — 83V70037GE (НОВЫЙ)
- Даташит ✅ [PSREF 83V70037GE](https://psref.lenovo.com/Detail/IdeaPad/IdeaPad_Slim_5_16IMH10?M=83V70037GE), анонс 26.12.2025, EAN 199274493059.
- CPU: Core Ultra 9 185H, 16 ядер (6P+8E+2LPE), Meteor Lake-H (Core Ultra 1-го поколения). iGPU Intel Arc (8 Xe) — Arc работает, потому что память в двухканале; есть аппаратный AV1-энкодер.
- ОЗУ: **2×16 SO-DIMM DDR5-5600**, 2 слота, оба заняты. PSREF «Up to 32GB offering» — это то, что продаёт Lenovo, а не предел платформы.
- SSD: 1 ТБ M.2 2242 PCIe 4.0 x4 + **свободный M.2 2280** PCIe 4.0 x4.
- Экран (PSREF): 16" WUXGA IPS, 300 нит, 45 % NTSC, 60 Гц, матовый. Модель матрицы в PSREF не указана.
- Порты (PSREF): 2× USB-C 10 Гбит/с (PD 65–100 Вт, DP 1.4), **HDMI 2.1 (4K/60)**, 2× USB-A 5 Гбит/с, microSD, аудио. TB4 — нет, RJ45 — нет. Wi-Fi 7.
- Батарея 60 Втч; ~1,85 кг; алюминий; Windows 11 Home (DE); подсветка клавиатуры; цвет Cosmic Blue; гарантия 2 года.
- **Блок питания не входит** (PSREF «No Power Adapter»). Платформа поддерживает 65 и 100 Вт USB-C — [PSREF PDF](https://psref.lenovo.com/syspool/Sys/PDF/IdeaPad/IdeaPad_Slim_5_16IMH10/IdeaPad_Slim_5_16IMH10_Spec.pdf). Lenovo 65 Вт USB-C — «ab 21,97 €» / «ab 28,00 €» (4X20V24678), [billiger](https://www.billiger.de/search?searchstring=Lenovo+65W+USB-C+AC+Adapter+4X20M26272&order=s_price).
- Цена:
  - **1049,49 € на Amazon.de** — [notebookcheck, 23.08.2026](https://www.notebookcheck.com/Core-Ultra-9-32-GB-RAM-1-TB-SSD-Lenovo-Office-Notebook-im-Angebot.1376162.0.html);
  - в сниппете поиска geizhals — «1 Angebot 1079,99 €» и отдельно 1439 €, даты неизвестны ([geizhals, семейство 16IMH10](https://geizhals.de/lenovo-ideapad-slim-5-16imh10-v228573.html), страницу не открывал); → проверено в браузере 30.09.2026: (п. 2.4) см. строку 8 ([geizhals.de](https://geizhals.de/lenovo-ideapad-slim-5-16imh10-v228573.html)).
  - на billiger.de и Cyberport не найден. Сегодняшнюю цену **проверить на idealo**. → проверено в браузере 30.09.2026: (п. 1.3) см. строку 8 ([idealo.de](https://www.idealo.de/preisvergleich/MainSearchProductCategory.html?q=83V70037GE)).
- HEVC: неизвестно; в PSREF оговорок нет.
- Близнец **83V70033GE** (Luna Grey, всё остальное то же) в продаже не найден.
- Вывод: самый сильный Lenovo с 2×16 в районе 1100 €. CPU новее, чем i7-13620H у 83HS00BLGE, есть Arc и HDMI 2.1. Экран такой же слабый. Если цена ≤ ~1070 €, то вместе с зарядкой он укладывается в 1100 €.

### IdeaPad Slim 5 16IMH10 — 83V70077GE (дополнение)
- **Новое:** PSREF — «Power Adapter: No Power Adapter» ([PSREF](https://psref.lenovo.com/Detail/IdeaPad/IdeaPad_Slim_5_16IMH10?M=83V70077GE)). Добавить к бюджету зарядку USB-C 65–100 Вт (~22–28 € за фирменную 65 Вт).
- Цена без изменений: **864,38 €** (минимальная цена товара), с доставкой 871,37 € (computeruniverse, Cyberport); 12 предложений — [billiger](https://www.billiger.de/pricelist/5716403846-lenovo-ideapad-slim-5-16-intel-core-ultra-5-135h-24-gb-ram-1-tb-ssd-win11-home). На [Cyberport](https://www.cyberport.de/notebook-und-tablet/notebooks/lenovo/pdp/1c31-484/lenovo-ideapad-slim-5-16imh10-16-wuxga-core-ultra-5-135h-24gb-1tb-ssd-win11.html) — 864,38 €, в наличии. → проверено в браузере 30.09.2026: (п. 1.4) 83V70077GE — 871,37 € (Cyberport, computeruniverse, 30 дн.), мин. 830,15 € (06.07); совпадает с отчётом ([idealo.de](https://www.idealo.de/preisvergleich/OffersOfProduct/210281880_-ideapad-slim-5-16-83v70077ge-lenovo.html)).
- Итог: 864 + планка 16 ГБ (161–260 €) + БП (~22–28 €) ≈ **1047–1152 €**. Укладывается в 1100 € только с самой дешёвой планкой.

### IdeaPad Slim 5 16IRH10 — 83HS00BLGE (дополнение)
- **Новое:** billiger — минимум за 6 месяцев **949,00 €**, средняя цена 999,00 €, сейчас 989,05 € («Aktuell normaler Preis») — [billiger](https://www.billiger.de/pricelist/5613884860-lenovo-ideapad-slim-5-16-intel-core-i7-13620h-32-gb-ram-1-tb-ssd-win11-home). Сопоставлен по EAN 0199273506071 = PSREF.
- Блок питания 65 Вт USB-C **в комплекте** (PSREF).
- Порты по PSREF: 2× USB-C **5 Гбит/с** (PD, DP 1.4), **HDMI 1.4b**, 2× USB-A 5 Гбит/с, microSD. RJ45 и TB4 нет.
- Братья по PSREF (тоже 2×16 + 1 ТБ) в продаже не найдены:
  - 83HS00B7GE — тот же i7-13620H;
  - 83HS00BMGE — i5-13420H. На expert.de он есть, но «ausverkauft» — [expert](https://www.expert.de/shop/unsere-produkte/computer-zubehor/notebooks/laptops/17043158543-ideapad-slim-5-16irh10-16-zoll-wuxga-ips-intel-core-i5-13420h-32-gb-1-tb-ssd-intel-uhd.html).

### Lenovo V15 G5 IRL — 83GW00AHGE (новый по PSREF, цены нет)
- Даташит ✅ [PSREF 83GW00AHGE](https://psref.lenovo.com/Detail/Lenovo/Lenovo_V15_G5_IRL?M=83GW00AHGE), анонс 20.10.2025, EAN 199273467884.
- CPU: i7-13620H (Raptor Lake-H, 13-е поколение), iGPU UHD. ОЗУ: **2×16 SO-DIMM DDR5-5200**. SSD: 1 ТБ M.2 2242, **слот M.2 один**.
- Экран: 15,6" FHD IPS, 300 нит, 45 % NTSC.
- Порты: 1× USB-C 5 Гбит/с (PD 45–65 Вт, **DP 1.2**), HDMI 1.4b, 2× USB-A, **RJ45**. Кардридера нет. Блок питания 65 Вт с круглым штекером.
- Батарея 47 Втч; 1,61 кг; пластик; клавиатура без подсветки; гарантия 1 год.
- Цена: по MTM на billiger/Alternate/Cyberport **не найден**. Есть предложение маркетплейса «Lenovo V15 G5 IRL i7-13620H» за **1018,37 €**, billiger относит его к 32 ГБ/1 ТБ — [billiger](https://www.billiger.de/search?searchstring=lenovo+v15&filter=f_category_2303,f_brand_1507,f_4266_32000000000x32000000000,f_5198_1000000000000x1000000000000&order=s_price). Но у этого предложения EAN 199272202875, которого нет в PSREF → конфигурация **не подтверждена**. → проверено в браузере 30.09.2026: (п. 1.6) см. строку 36 ([idealo.de](https://www.idealo.de/preisvergleich/OffersOfProduct/208744735_-v15-g5-83gw00a9ge-lenovo.html)).
- Вывод: по всем параметрам хуже 83HS00BLGE и не дешевле. Интерес только из-за RJ45.

### ThinkPad E16 Gen 3 (Intel) — 22AY004VGE (дополнение)
- **Новое:** минимум за 6 месяцев **1078,67 €** (billiger), сейчас 1242,62 € на Galaxus (Marktplatz), «Aktuell hoher Preis» — [billiger](https://www.billiger.de/products/5527165900-lenovo-thinkpad-e16-g3-intel-core-ultra-5-228v-32-gb-ram-1-tb-ssd-22ay004vge).
- PSREF ([22AY004VGE](https://psref.lenovo.com/Detail/ThinkPad/ThinkPad_E16_Gen_3_Intel?M=22AY004VGE)):
  - CPU и память: Ultra 5 228V (Lunar Lake), 32 ГБ LPDDR5X-8533 на корпусе процессора, апгрейда нет;
  - SSD: 1 ТБ, один слот M.2 2280;
  - экран: 16" WUXGA IPS, 300 нит, 45 % NTSC;
  - порты: 1× TB4/USB4 (DP 2.1), HDMI 2.1, USB-A 10 + 5 Гбит/с, RJ45; кардридера нет;
  - прочее: 64 Втч, 1,62 кг, алюминий, Windows 11 Pro, 1 год гарантии.
- Экран хуже, чем у 22AY004XGE (2,5K, 120 Гц, 100 % sRGB), но исторически он был дешевле. Брать только при цене ≤ 1100 €.

### ThinkBook 16 G7 IML — 21MS004SGE (дополнение)
- billiger: 1241,58 € (Amazon Marketplace), минимум за 6 месяцев 894,98 € — [billiger](https://www.billiger.de/pricelist/4952539795-lenovo-thinkbook-16-g7-iml-intel-core-ultra-5-125u-32-gb-ram-1-tb-ssd-win11-pro-arctic-grey-21ms004sge).
- Сниппет поиска: «Lenovo ThinkBook 16 G7 IML ab € 994,91 (2026)», [geizhals](https://geizhals.de/lenovo-thinkbook-16-g7-iml-21ms004sge-a3212977.html). Дата и магазин неизвестны, страницу не открывал → **проверить на idealo**.
- Campus-предложения (только для студентов и преподавателей): lapstars «Campus» — 874 €, SoldOut ([lapstars](https://www.lapstars.de/lenovo-thinkbook-16-intel-g7-21ms004sge-campus)). Скорее всего, нашему пользователю не подходит.
- PSREF: Ultra 5 125U (Meteor Lake-U), 2×16, **два M.2 2280**, WUXGA IPS 300 нит 45 % NTSC, **TB4**, HDMI 2.1, **SD**, **RJ45**, 45 Втч, 1,7 кг, 1 год гарантии.

## Lenovo.de: что продаёт сам Lenovo (30.09.2026)

- По MTM из списка кандидатов Lenovo.de почти ничего не продаёт. Страницы серий показывают либо «End of Life» (IdeaPad Slim 5i Gen 10, E16 Gen 2, L16 Gen 2, ThinkBook 16 G7), либо только CTO.
- Готовые MTM на Lenovo.de:
  - V15 G5 83GW009EGE / 009FGE (1×16, **512 ГБ**) — от 899,01 €;
  - ThinkBook 16 G9 21UR0059GE (2×16, **512 ГБ**) и 21UR0002GE;
  - E16 Gen 4 21YC0008GE / 005YGE (512 ГБ);
  - L16 Gen 3 21X8003CGE (512 ГБ).
  С 1 ТБ среди них нет ни одного.
- CTO (конфигуратор, цены кликнуты или посчитаны по доплатам):
  - [E16 Gen 3 21SRCTO1WW](https://www.lenovo.com/de/de/configurator/cto/?bundleId=21SRCTO1WWDE1): Ultra 5 225H + 2×16 + 1 ТБ + **без ОС** = **1538,19 €** (прейскурант 1899 €, −19 %). По умолчанию (255H, Win Pro) — 1781,19 €. Есть опции «Ohne Betriebssystem» (−130 €) и экран 2,5K 120 Гц 100 % sRGB (+50 €).
  - [ThinkBook 16 G8 21SKCTO1WW](https://www.lenovo.com/de/de/configurator/cto/?bundleId=21SKCTO1WWDE1): база (135H, 2×16, 256 ГБ, Win Pro) — 1599 €; +1 ТБ (+260) −ОС (−130) → ~1729 € (посчитано по доплатам).
  - [E16 Gen 4 21YCCTO1WW](https://www.lenovo.com/de/de/configurator/cto/?bundleId=21YCCTO1WWDE1): база — 1824,41 € (прейскурант 2303 €); с Ultra 5 325 без ОС → ~1555 € (посчитано).
  - [ThinkBook 16 G9 21URCTO1WW](https://www.lenovo.com/de/de/configurator/cto/?bundleId=21URCTO1WWDE1): 2169 € (Ultra 7 355, 2×16, 1 ТБ); с Ultra 5 325 без ОС → ~1839 €.
  - [IdeaPad 5i 2-in-1 16" 83KSCTO1WW](https://www.lenovo.com/de/de/configurator/cto/?bundleId=83KSCTO1WWDE1): память только 16 ГБ распайки → не подходит.
  - Вывод: CTO на Lenovo.de на 400–700 € дороже магазинных MTM.

## В PSREF для Германии есть, но в магазинах не найдено (billiger / Cyberport / Alternate / поиск)

- IdeaPad Slim 5 16IRH10R:
  - **83J1006UGE** — Core 7 240H (ребренд 13-го поколения), 2×16, 1 ТБ, **OLED 2,8K 120 Гц 100 % DCI-P3 500 нит**, HDMI 1.4b. На geizhals есть карточка, но без предложений (сниппет: [geizhals](https://geizhals.de/lenovo-ideapad-slim-5-16irh10r-83j1006uge-a3655581.html)).
  - 83J1006HGE (240H, 2×16, WUXGA) и 83J1006BGE (Core 5 210H, 2×16). 83J1006BGE по [hardwareschotte](https://www.hardwareschotte.de/preisvergleich/Lenovo-IdeaPad-Slim-5-16IRH10R-83J1006BGE-p22318700) «seit 12.05.2026 nicht mehr erhältlich».
  - 83J1006WGE / 83J1006XGE — 1×24 + свободный слот (210H / 240H).
- IdeaPad Slim 5 16IMH10 83V70033GE (185H, 2×16) — близнец 83V70037GE.
- V15 G5 83GW002JGE / 2PGE (Core 5 120U) и 83GW002MGE / 2NGE (Core 7 150U) — 2×16, 1 ТБ. Все CPU — ловушки Raptor Lake-U.
- ThinkBook 16 G6 IRL — 16 MTM с 2×16 или 1×16 + слот, 1 ТБ (i5-1335U, i5-13420H, i7-13700H). Не найдены.
- ThinkBook 16 G8 IAL 1×16 + слот, 1 ТБ: 21SK008CGE, 21SK008MGE (225U), 21SK007L/N/P/Q/SGE (255H), 21SK00K8/K9/KAGE (185H). ThinkBook 16 G8 IRL 21SH008Q/R/W/X/91GE (240H) — тоже нет.
- E16 Gen 2 1×16 + слот, 1 ТБ (21MA001RGE, 002QGE, 002SGE — 155H; 21MA0051GE — 125U), E16 Gen 3 21SR0079GE / 21SR004LGE, L16 Gen 1 21L3002FGE / 002YGE — нет в продаже.
- E16 Gen 1 (Intel, **DDR4**): 21JN00D6/D9/DB/DHGE — 16 ГБ распайки + свободный слот, i7-13700H, 1 ТБ (путь «16 распайка + 16 SO-DIMM»). Не найдены. 21JN00D5GE (16 + 16) — 1459 € ([billiger](https://www.billiger.de/search?searchstring=21JN00D5GE)).
- B-список (32 ГБ распайки): IdeaPad Pro 5 16IMH9 83D40019GE / 48GE / 35GE (2,5K 120 Гц 100 % sRGB), IdeaPad Slim 5 16IMH9 83DC003PGE (OLED; по hardwareschotte «seit 26.01.2026 nicht mehr erhältlich»), Yoga Slim 7 15ILL9 (7 MTM, 258V, 2,8K), Yoga 7 2-in-1 16ILL10 / 16IPH11, Yoga Pro 9 16IMH9 / 16IAH10 / 16IPH11, IdeaPad Pro 5 16IAH10 / 16IPH11. В продаже либо нет, либо ≥ 1600 € (Yoga 7i 2-in-1 16" 83TE001EGE — 2183,96 €; IdeaPad Pro 5 16IPH11 с RTX 5050 — 2055 €; Yoga Pro 9 16IPH11 — от 2941 €).
- Старые платформы с 32 ГБ распайки (ThinkBook 16 G4+ IAP 21CY0060/005V/004PGE, Yoga 7 16IAH7, Yoga Slim 7 Pro 16IAH7 — 12-е поколение) — не найдены.

## Отброшено в этом проходе (новое)

- **V15 G5 «32 GB 1 TB»** на billiger — это сборки продавцов, а не заводские SKU:
  - i3-1315U — 919,99 € (Galaxus), [billiger](https://www.billiger.de/pricelist/5782559621-lenovo-v15-g5-intel-core-i3-1315u-32-gb-ram-1-tb-ssd-win11-pro);
  - i5-13420H — 1069 € (Galaxus), [billiger](https://www.billiger.de/pricelist/5593444416-lenovo-v15-g5-intel-core-i5-13420h-32-gb-ram-1-tb-ssd-win11-pro).
  EAN 4049998799530 и 0194778257596 — не Lenovo и не из PSREF. В PSREF DE нет заводских конфигураций с таким CPU + 32 ГБ + 1 ТБ → aufgerüstet.
- **IdeaPad Slim 5 16" Core 5 210H 24 GB 1 TB, 859 €** — по EAN 0199271585177 это **83J10065GE, 2×12 DDR5-4800** (PSREF). Двухканал на 32 ГБ без замены обеих планок не собрать — [billiger](https://www.billiger.de/pricelist/5356835617-lenovo-ideapad-slim-5-16-intel-core-5-210h-24-gb-ram-1-tb-ssd-win11-home).
- **IdeaPad 5 2-in-1 15IPH11** (Panther Lake, 15,3", 1 ТБ): 83UL0026GE (Ultra 7 355) — 1099 €, 83UL0025GE (Ultra 5 322) — 1149 € ([Cyberport](https://www.cyberport.de/notebook-und-tablet/notebooks/lenovo/pdp/1c31-48c/lenovo-ideapad-5-2-in-1-15iph11-15-3-wuxga-core-ultra-7-355-16gb-1tb-ssd-win11.html)). По PSREF — **2×8** → отброшено.
- **IdeaPad Slim 5 16IPH11** 83S60033GE (999 €) и 83S60034GE (1079,94 €, Cyberport) — 2×8 (уже было). 83S60031GE (2×16, OLED) — 1699 € и тоже без блока питания.
- **V15 G4 IRU / IAH**: DDR4, 8 ГБ распайки или один слот → 2×16 невозможно. 83A100JFGE (701 €) в PSREF нет.
- **V15 G5 83GW00A9GE** (598,98 €, минимум за 6 месяцев 598,31 €) и 83GW00FRGE (629 €): в Icecat — «2x SO-DIMM, Dual-channel», раскладка 1×16 или 2×8 по-прежнему **не подтверждена**. В PSREF этих MTM нет (проверено через поиск PSREF). CPU — ловушки. → проверено в браузере 30.09.2026: (п. 4.2) МЕНЯЕТ ВЫВОД: 83GW00A9GE — 1×16 ГБ + свободный слот (список деталей Lenovo, FRU 5M31L87377), итог с планкой ≈ 790–850 €; M.2 один (2242), занят; экран IPS 300 нит 45 % NTSC — не TN; 83GW00FRGE — то же. Гарантия: geizhals — 1 год, Lenovo показывает её только по серийнику ([pcsupport.lenovo.com](https://pcsupport.lenovo.com/de/de/products/laptops-and-netbooks/lenovo-v-series-laptops/lenovo-v15-g5-irl/83gw/83gw00a9ge/parts/display/model)).
- **Kaufland «E16 Gen1 i5-1335U 32GB 1TB» 979 €** (из `idealo-prices.md`): в PSREF DE у E16 Gen 1 с i5-1335U память только 8 ГБ распайки + 8/16 SO-DIMM. Симметричные 32 ГБ невозможны → сборка продавца.
- **Yoga 16" с Intel и 32 ГБ**: всё ≥ 1700 € (billiger, 30.09).

## HEVC (аппаратный H.265) у Lenovo

- Просмотрены тексты PSREF-даташитов 20 платформ: ThinkBook 16 G6 IRL, G7 IML, G8 IAL, G8 IRL, G9 IPL, G9 IRL; ThinkPad E16 Gen 1, 2, 3; L16 Gen 1; V15 G5 IRL; IdeaPad Slim 5 16IRH10, 16IRH10R, 16IMH9, 16IMH10, 16IPH11; IdeaPad Pro 5 16IMH9; Yoga Slim 7 15ILL9; Yoga 7 2-in-1 16ILL10 и 16IPH11. Слова «HEVC/H.265» нигде нет, «codec» встречается только как аудиокодек.
- В публикациях об отключении HEVC названы HP и Dell, Lenovo нет:
  - [Ars Technica, 11.2025](https://arstechnica.com/gadgets/2025/11/hp-and-dell-disable-hevc-support-built-into-their-laptops-cpus/);
  - [smith6612.me, 19.04.2026](https://smith6612.me/2026/04/19/its-me-i-started-the-hevc-disablement-press-storm/) — HP ProBook 640/465 G11, EliteBook 665 G11, ProBook 4 G1i 16, EliteBook 6 G1i 16, ProBook 4 G1a 16 и условная политика Dell.
- Итог: у Lenovo признаков отключения нет, но и прямого подтверждения «HEVC включён» нет. Проверить по факту: DXVA Checker или GPU-Z на витринном экземпляре, либо спросить у Lenovo.

## Источники

- PSREF: https://psref.lenovo.com (API ShowModel с фильтром Country/Region = Germany, 30.09.2026) и PDF-спецификации платформ `https://psref.lenovo.com/syspool/Sys/PDF/<Brand>/<Key>/<Key>_Spec.pdf`.
- billiger.de: поиск с фильтрами `f_4266` (RAM) и `f_5198` (SSD), сортировка `order=s_price`; страницы товаров (EAN, предложения, 6-месячная история), 30.09.2026.
- Cyberport: Lenovo, Intel, без дискретки, до ~1100 € нетто. Alternate: поиск по MTM. Lenovo.de: страницы MTM, серий и CTO-конфигуратор (Playwright).
- hardwareschotte.de, expert.de, lapstars.de; notebookcheck.com (новость про 83V70037GE); сниппеты веб-поиска (geizhals) — помечены как «дата неизвестна».
