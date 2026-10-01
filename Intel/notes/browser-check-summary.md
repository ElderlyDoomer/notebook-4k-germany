# Итог браузерной проверки: что изменилось (30.09.2026)

_Сводка по `browser-todo.md` (141 пункт) и файлам групп `browser-check-*.md`. Сайты открывались через curl, в Chrome пользователя и через Wayback.
Цены — idealo.de, с доставкой; по правилу пользователя маркетплейсы тоже считаются. Ничего не покупалось, в аккаунты не входили, формы не отправлялись._

**Статусы:** закрыто 89, частично 42, нельзя проверить 3 (3.8, 5.12, 7.31), вопрос пользователю 7 (3.2, 3.5, 3.7, 4.4, 5.1, 5.26, 5.29). МЕНЯЕТ ВЫВОД — 19 пунктов.

## Коротко: что это меняет в выборе

- **SKU «современный Intel H + 2×16 SO-DIMM + 1 ТБ» дешевле 1100 € по-прежнему нет** (широкий скан idealo, п. 1.20).
- **Купить сейчас:**
  - №1 IdeaPad Slim 5 `83HS00BLGE` — без изменений: 989,05 € (Kaufland MP) или 995 € (Expert).
  - №2 Aspire Go 16 `NX.JS9EG.005` — **849 €**, это на 50 € дешевле. Продаёт маленький магазин technik-brandenburg.de, у Expert по-прежнему 899 €.
  - Medion E15433 `MD600023` переходит из «условных» в подтверждённые: **2×16 DDR4 по спецификации Medion**, 699,97 €. Самый дешёвый путь к 2×16 + 1 ТБ.
    Минусы: DDR4, HDMI 1.4b, Wi-Fi 5, блок 65 Вт, яркость экрана Medion не публикует.
  - V15 G5 `83GW00A9GE`: **1×16 + свободный слот подтверждены Lenovo** (список деталей). С планкой выходит ≈ 786–848 €. Экран IPS 300 нит (не TN), CPU и экран слабые.
  - HP 15-fd1555ng с планкой — 971–1032 €. Риски выросли: нашёлся ещё один потребительский HP без аппаратного HEVC (OmniBook 7 Aero, AMD) и жалоба на нагрев 15-fd1.
    Зато пара 24 + 16 косвенно работает: Best Buy продаёт 15-fd1095cl «Upgraded, 40GB».
- **Ждать просадку:**
  - №7 `21SK007KGE` сейчас стоит 1399 €, но на idealo 03.09 было 910 €, и за полгода он 89 дней стоил ≤ 1100 €. Ждать стоит.
  - Campus-вариант `21SK0083GE` отпал: этого SKU в Campus-магазинах больше нет.
  - №9 `22AY004XGE`: цены 909 € на idealo не было, минимум за полгода — 1099 €. Для B-списка «ждать» удобнее `22AY004VGE`: 168 дней из 183 он стоил ≤ 1100 €, экран у него проще.
- **№8 `83V70037GE` нигде не продаётся:** на idealo его нет, на geizhals нет предложений с 28.08, на Amazon — «Currently unavailable». Убрать из топа.
- **B-список (распайка):** новый кандидат — HP OmniBook 7 AI 16-ay0770ng. Core Ultra 7 255H, 32 ГБ распаяны, 1 ТБ, 979,30 € на hp.com. Минус — риск HEVC у потребительских HP.
- **Кодеки:**
  - **Panther Lake аппаратно декодирует H.264 4:2:2 10 бит** (даташит Intel), и Resolve Studio 21 это использует. Premiere и бесплатный Resolve — нет, независимых тестов нет.
  - PTL-ноутбука со слотами дешевле 1100 € нет: ThinkBook 16 G9 `21UR005AGE` стоит 1205 €.
  - Если камера пишет H.264 4:2:2 10 бит, а монтаж в Resolve Studio, это вторая альтернатива RTX 50: ждать `21UR005AGE` ≤ 1100 €.
- **Дискретка:** в 1100 € с 32 ГБ по-прежнему ничего нет.
  - MSI Cyborg 15 выходит дешевле, чем считали: ≈ 1273 €.
  - У Nitro V 15 -74JQ экран по заявке Acer лучше, чем думали.
  - У любых RTX в DXVA Checker проверять и декодер NVIDIA: OEM-BIOS умеет отключать и его.
- **Память:**
  - планка 16 ГБ DDR5 стоит 188–294 €, комплект 2×16 — 480–524 €, планка 24 ГБ — от 339 €;
  - у ThinkBook G8 разница между 16/512 и 32/1 ТБ — +223 €, то есть 32 ГБ с завода по-прежнему выгоднее.

## МЕНЯЕТ ВЫВОД

| Пункт | Было | Стало (30.09.2026) | Ссылка | Что поправить в `REPORT.md` |
|---|---|---|---|---|
| 1.2 | `21SK007KGE`: 1349 €, минимум за 6 мес. 1049,01 € (billiger), ≤ 1100 € — 76 дней | 1399 € (easynotebooks); минимум на idealo 910 € (03.09); ≤ 1100 € — 89 дней, последний раз 18.09 | [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/206151089_-thinkbook-16-g8-21sk007kge-lenovo.html) | Строки 41 и 90: цена 1399 €, минимум 910 €. Совет «ждать ≤ 1100 €» остаётся, теперь он убедительнее |
| 1.3 · 2.4 · 3.1 | `83V70037GE`: «~1059 € + зарядка (не подтв.)», 1049,49 € на Amazon 23.08, «проверить цену» | Не продаётся нигде. На idealo карточки нет. На geizhals: 1079,99 € 11–19.08, 1049,99 € до 27.08, с 28.08 предложений нет. Amazon B0GD827NG1 (MPN 83V70037GE) — «Currently unavailable». «1439 €» — это другой SKU, 83V70065NT | [geizhals](https://geizhals.de/a3734453.html), [Amazon](https://www.amazon.de/dp/B0GD827NG1) | Строки 42 и 104–109: убрать №8 из топа или пометить «нет в продаже — следить» |
| 1.8 | `22AY004XGE`: минимум 909,16 € (22.09, billiger) | На idealo минимум за 6 мес. — 1099 € (03–14.06), сейчас 1207,78 € (Amazon MP). `22AY004VGE`: ≤ 1100 € 168 дней, минимум 961,12 € (09.09) | [idealo 004X](https://www.idealo.de/preisvergleich/OffersOfProduct/209382346_-thinkpad-e16-g3-22ay004xge-lenovo.html), [idealo 004V](https://www.idealo.de/preisvergleich/OffersOfProduct/209221694_-thinkpad-e16-g3-22ay004vge-lenovo.html) | Строки 43, 111 и 227: убрать «909 €». Как «ждать» в B-списке — `22AY004VGE` |
| 1.10 | `NX.JS9EG.005` — 899 € | 849,00 € (technik-brandenburg.de, минимум за год; у Expert 899 €). У `.00C` минимум за полгода — 849 € (апрель). Версии без ОС с i9 / 32 / 1 ТБ нет | [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/209373295_-aspire-go-16-ag16-71p-97gf-acer.html) | Строки 12, 31 и 60: «849 € (мелкий магазин) / 899 € (Expert)» |
| 1.20 | B-список: лучший — `22AY004XGE` за 1208 € | Новый: HP OmniBook 7 AI 16-ay0770ng (`BM9T4EA`) — Core Ultra 7 255H, 32 ГБ DDR5-5600 распаяны (0 слотов), 1 ТБ, 979,30 € на hp.com | [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/206602335.html), [даташит HP](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09154072) | Добавить в B-список с пометкой «HEVC проверить на экземпляре» (п. 5.3, 6.3) |
| 2.2 | За +16 ГБ и +512 ГБ у ThinkBook G8 производитель берёт «около 150 €» (+147) | +223 €: 21SK006QGE стоит 899 €, 21SK0083GE — 1122 € | [geizhals](https://geizhals.de/a3464495.html) | Строка 148: «около 150 €» → «около 220 €». Вывод «32 ГБ с завода выгоднее» остаётся |
| 2.8 · 1.21 | Планка 16 ГБ DDR5 ~237–244 €, ADATA — 161 €, комплект 2×16 ~480 € | Планка 16 ГБ DDR5-5600: 187,56 € (Kingston, Galaxus MP), у обычных магазинов 206,80–293,77 €. Комплект 2×16: 479,99 € (Kaufland MP) или 524,04 €. ADATA за 161 € была в 12.2025, сейчас 259–282 €. Планка 24 ГБ — от 338,95 € | [idealo Crucial 16](https://www.idealo.de/preisvergleich/OffersOfProduct/202284828_-16gb-ddr5-5600-cl46-ct16g56c46s5-crucial.html), [geizhals ADATA](https://geizhals.de/adata-so-dimm-16gb-ad5s560016g-s-a2938017.html) | Строка 148: «планка ~188–294 €, комплект 2×16 ~480–524 €». Все итоги «+ планка» пересчитать по этим цифрам |
| 2.10 · 4.2 | V15 G5 `83GW00A9GE`: неизвестно, 1×16 + слот или 2×8 | 1×16 + свободный слот (список деталей Lenovo, FRU 5M31L87377). M.2 один, занят. Экран IPS 300 нит. FreeDOS. Гарантия — 1 год (по geizhals) | [Lenovo: детали](https://pcsupport.lenovo.com/de/de/products/laptops-and-netbooks/lenovo-v-series-laptops/lenovo-v15-g5-irl/83gw/83gw00a9ge/parts/display/model) | Строка 128: снять «неизвестно». Итог 598,98 + 187,56…248,89 ≈ 786–848 € |
| 3.10 | Campus-цены `21SK0083GE` 911–1099 € — «решение уже сейчас» | В Campus-программах lapstars, notebookstore и campuspoint этого SKU нет. Campus G8 бывает только 16/512: 21SK006QGE — 928,27 €, а до 32 ГБ / 1 ТБ ≈ 1434 € | [lapstars](https://www.lapstars.de/notebooks-campus/thinkbook-campus/thinkbook-16-campus/thinkbook-16-g8-intel-campus) | Строки 99 и 226: убрать Campus как решение |
| 4.1 | `MD600023`: раскладку 2×16 вывели по родственной модели | 2×16 DDR4-3200, оба слота заняты — спецификация Medion (MSN 30041451). 1,81 кг, блок 65 Вт, HDMI 1.4b, Wi-Fi 5, без подсветки | [Medion](https://service.medion.com/de/product-detail/30041451), [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/208688812_-e15433-md600023-medion.html) | Строка 126: из «условных» в подтверждённые, 699,97 € (Expert). Кандидат в топ «купить сейчас» |
| 4.7 | Nitro V 15 с 32 ГБ: «бледный экран ~60 % sRGB», P/N не найден | `ANV15-52-74JQ` = `NH.QZ9EG.00B`: 2×16 DDR4, FHD IPS 180 Гц, «100 % sRGB» (заявлено Acer, без замера); 76 Втч | [даташит Acer](https://gzhls.at/blob/ldb/0/4/e/2/2b75b4b7aa4f3707a348a747121c8a53d21f.pdf) | В разделе с дискреткой: убрать минус про экран, добавить P/N. 1199 € только с купоном — всё равно выше 1100 € |
| 4.10 | MSI Cyborg 15 `B2RWFKG-068`: 2×8, итог ~1559–1603 € | 1×16 + свободный слот, RTX 5060 до 55 Вт; итог ≈ 1079,10 + 193,40 = 1272,50 € | [MSI](https://storage-asset.msi.com/specSheet/de/nb/Cyborg%2015%20B2RWFKG-068DE.pdf) | Если Cyborg упоминается — поправить итог. В бюджет всё равно не проходит |
| 4.24 | CSL R'Evolve C16: «16 ГБ + планка ≈ 752–875 €» | 16 ГБ = 2×8 DDR4, путь не работает. Заводской 32 ГБ 2×16 есть (92685, 651,52 € на idealo), но CPU — i5-1235U | [CSL 16 ГБ](https://www.csl-computer.com/notebook-csl-r-evolve-c16-windows-11-home-1000gb-16gb.html) | В REPORT модели нет. В список «16 + планка» не включать |
| 5.7 | «У RTX свой NVDEC — HEVC, скорее всего, OK» | NVDEC от флага Intel не зависит, но OEM-BIOS может отключать и кодеки NVIDIA: Lenovo в 2021 году в Германии, Legion в 2024 году | [borncity](https://borncity.com/win/2021/08/15/lenovo-firmware-update-aktiviert-h-264-auf-notebooks-mit-nvidia-grafik/) | Строка 188 (проверка экземпляра): у ноутбуков с RTX смотреть в DXVA Checker и декодер NVIDIA |
| 5.10 | Dell: «официального способа (BIOS-опции) нет» | В Dell Command \| Configure есть BIOS-атрибут `--HEVC` (Enabled/Disabled). Работает ли он на Dell Pro 2025–26, не проверено | [Dell](https://www.dell.com/support/manuals/en-us/command-configure/dcc_5.x_ref_guide/-hevc?guid=guid-bb1a3deb-1ebb-4ee4-9d50-6d1e32bd1496&lang=en-us) | Строки 135 и 184: короткая оговорка. На выбор не влияет, Dell отброшен |
| 5.13 | «H.264 10 бит / 4:2:2 не декодирует ни один Intel… (для Panther Lake не проверено)» | Panther Lake (Xe3) аппаратно декодирует H.264 4:2:0 8/10 бит и 4:2:2 10 бит (даташит 872188, табл. 77). Resolve Studio 21 — да; Premiere и бесплатный Resolve — нет; тестов нет | [даташит Intel](https://cdrdv2.intel.com/v1/dl/getContent/872188?fileName=872188-002.pdf), [readme Resolve 21](https://www.blackmagicdesign.com/support/readme/2cda7ec076ea4b25aaa007fc68a5cbfc) | Строки 17–18, 194–195 и 224: «…кроме Panther Lake в Resolve Studio 21». PTL-кандидат `21UR005AGE` (1205 €) — в «ждать ≤ 1100 €» |

**Мелкие уточнения** (выбор не меняют, но в REPORT поправить):
- 4.6: у Aspire Go 16 второго M.2 нет. В строке 63 «не проверено» заменить на «второго M.2 нет». В строке 130 у `.00B` 2×16 подтверждено даташитом Acer, цена сейчас 951,46 €.
- 1.11: HP 15-fd1555ng с планкой — 971–1032 € (строки 33 и 73).
- 5.25 и 6.3: риски №4 — одна жалоба на нагрев 15-fd1 и ещё один потребительский HP без HEVC. 6.4: пара 24 + 16, скорее всего, работает (строка 77).
- 5.19: корпус IdeaPad Slim 5 16 держит ~43 Вт при ~96 °C.
- 5.20: у V15 G5 тугой шарнир.
- 7.11: у ASUS в DE теперь 3 года гарантии.
- 7.18: у IdeaPad запчасти выпускают 3 года (ECO-декларация 2023).
- 3.9: у computeruniverse возврат 30 дней; скидка Lenovo Education — от 7 %.
- 1.22: Windows 11 Home в магазине стоит ~131 €. 1.23: версия «без ОС» не всегда дешевле.
- Попутно, не проверено: у MediaMarkt и Saturn с 01.10 акция «19 % MwSt geschenkt», только для клиентов myMediaMarkt / mySaturn ([mydealz](https://www.mydealz.de/deals/mediamarkt-saturn-19-mwst-aktion-mehrwertsteuer-geschenkt-pre-sale-ab-0110-6-uhr-nur-fur-mymediamarkt-und-mysaturn-kunden-2845616)). Посмотреть 01.10: часть SKU может опуститься ниже 1100 €.

## Вопросы пользователю и продавцам

| # | Кому | SKU | Что спросить | Пункт |
|---|---|---|---|---|
| 1 | Владельцу ноутбука | — | Какой камерой снимает и в каком кодеке: открыть исходник в MediaInfo. Если там H.264 4:2:2 10 бит, нужна RTX 50 или Panther Lake + Resolve Studio 21 | 5.29 |
| 2 | Expert (продавец) | Medion E15433 `MD600023` | Срок гарантии Medion: 24 месяца или другой (по гарантийной карте) | 4.1 |
| 3 | easynotebooks / notebooksbilliger | Lenovo V15 G5 `83GW00A9GE` | Срок гарантии Lenovo: 1 год, 2 года или без базовой | 4.2 |
| 4 | Captiva или nexoc-store.de | Captiva `I82-531GE` | Как набраны 32 ГБ (2×16?), есть ли свободный M.2, яркость экрана | 4.4 |
| 5 | one.de | ASUS X1607CA-MB120, 32 ГБ / 1 ТБ (арт. 89162) | Марка и частота добавленной планки и SSD; сохраняется ли гарантия ASUS после доработки | 3.5 |
| 6 | TechPoint1111 (Amazon MP) | ThinkPad E16 G3 `22AY004VGE` (B0GP6T38P1) | Новый ли и запечатан ли; раскладка QWERTZ | 3.2 |
| 7 | Продавец на Amazon MP | ThinkBook 16 G7 `21MS004SGE` | Раскладка: оферта на французском, возможна AZERTY | 1.8 |
| 8 | Alternate | TERRA MOBILE 1516R `1220844` | Какой SSD придёт: 500 ГБ или 1 ТБ (только если брать там) | 3.11 |
| 9 | Acer или продавец | Aspire Go 16 `NX.JS9EG.005` / `.00C` | Поставляется ли SKU «ohne HEVC». Надёжнее проверить экземпляр в DXVA Checker в срок возврата (30 дней — NBB, Galaxus) | 1.24, 5.5 |
| 10 | HP или продавец | ProBook 4 G2i (например, E04G3ET) | Заказана ли опция HEVC. Низкий приоритет: линейка отброшена | 5.1 |
| 11 | Пользователю | Medion SPRCHRGD 16 S1 `30040200` | Есть ли доступ к heise+ или номеру c't 17/2026 (раздел «89-Prozent-Akku») | 5.26 |
| 12 | Пользователю | ThinkPad E16 G2 `21MA003RGE` | Проданные лоты eBay видны только после входа в аккаунт. Низкий приоритет | 3.7 |
| 13 | Пользователю | `21SK007KGE`, `21SK0083GE`, `22AY004VGE`, `30040200` | Поставить Preiswecker на idealo (нужны e-mail или аккаунт) | — |

## Досверка idealo при сводке (30.09.2026, Chrome пользователя)

Эти пункты группы не проверяли. Досмотрены в карточках idealo.
- 1.6: `83GW00FRGE` — 636,99 € (nullprozentshop), CPU Core 5 120U — ловушка. [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/209498379_-v15-g5-83gw00frge-lenovo.html)
- 1.10: у `.005` и `.00C` в карточках указана Windows 11 Home. Фильтр «ohne Betriebssystem» всё равно их показывает, ему верить нельзя. [idealo .005](https://www.idealo.de/preisvergleich/OffersOfProduct/209373295_-aspire-go-16-ag16-71p-97gf-acer.html)
- 1.12: `NX.B9BEG.004` на idealo нет, поиск выдаёт только общую карточку TMP416-53. [поиск](https://www.idealo.de/preisvergleich/MainSearchProductCategory.html?q=NX.B9BEG.004)
- 1.17: `NX.BMFEG.002` / `.003` / `.008` на idealo нет, в том числе по кодам -7774, -508E, -78X1. `.009` (2 ТБ) — от 1249 € (Amazon MP). [idealo .009](https://www.idealo.de/preisvergleich/OffersOfProduct/207760108_-travelmate-p2-tmp215-75-g2-tco-nx-bmfeg-009-acer.html)
- 1.19: MSI Thin 15 B13UC-2892 — 806,99 € (nullprozentshop). Карточки HP 15-fd0673ng на idealo нет: поиск выдаёт fc0673ng и fd0677ng. [idealo MSI](https://www.idealo.de/preisvergleich/OffersOfProduct/206211090_-thin-15-b13uc-2892-msi.html)
- 1.20: Aspire 16 AI с 288V: -984U — 1599 € (acer.com), -916J — от 1308,26 €, -92UY — от 1348 €. [idealo -984U](https://www.idealo.de/preisvergleich/OffersOfProduct/207403240_-aspire-16-ai-a16-52m-984u-acer.html)
- 1.21: DDR5-5600 24 ГБ: Lexar LD5S24G56C46ST-BGS — 338,95 € (nxus.ch), 339,90 € (MediaMarkt, Saturn); Crucial CT24G56C46S5 — 364,00 € (Amazon MP), 456,99 € (nullprozentshop). [idealo Lexar](https://www.idealo.de/preisvergleich/OffersOfProduct/212701811_-so-dimm-24gb-ddr5-5600mhz-cl46-ld5s24g56c46st-bgs-lexar.html), [idealo Crucial](https://www.idealo.de/preisvergleich/OffersOfProduct/203078719_-24gb-ddr5-5600-cl46-ct24g56c46s5-crucial.html)

## Что правилось в заметках

- `browser-todo.md`: у каждого пункта стоит итоговый статус и строка «→» с ответом и ссылкой.
- В исходных заметках к строкам пунктов категорий 1, 4, 5 и ко всем «МЕНЯЕТ ВЫВОД» дописано «→ проверено в браузере 30.09.2026: …». Это 211 строк в 18 файлах.
- Ложные места зачёркнуты `~~…~~`, рядом дано верное значение: цены планок, «+147 €», Campus-цены, экран Nitro, память MSI Cyborg, «16 + планка» у CSL, DDR5 у Aspire Go 15, «только Blackwell», три строки `MEMORY.md`.
- `REPORT.md` не правился.
