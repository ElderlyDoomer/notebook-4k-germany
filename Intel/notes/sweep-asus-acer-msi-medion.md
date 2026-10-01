# Добор: ASUS / Acer / MSI / Medion / Dynabook / Captiva / TERRA

_2026-09-30, облачная сессия. Цены — billiger.de (предложения магазинов и дневная история цен за 6 мес. из графика на странице), Alternate, сайты магазинов. «Из облака — перепроверить на idealo»._
_Раскладка памяти — даташиты Acer (PDF с генератора Acer, копии на gzhls.at / bluechip.de), Icecat (open catalog), asus.com techspec, medion.com._
_Что уже было в `candidates-other-brands.md`, не повторяю, если нет новых фактов._

## Вывод

1. **Acer Aspire Go 16 (AG16-71P, Core i9-13900H) — лучшая находка у «прочих» брендов:** заводские **2×16 ГБ DDR5 SO-DIMM** (даташит Acer), 1 ТБ, 16" WUXGA, **899 €**.
   CPU — 13-е поколение (Raptor Lake-H, как i7-13620H у Lenovo 83HS00BLGE), но это i9 (6P+8E) с Iris Xe 96 EU. Это не Core Ultra, iGPU слабее Arc.
   Четыре SKU: **NX.JS9EG.005** (-97GF, 120 Гц, 899 €), **NX.JS9EG.00C** (-95Q7, 60 Гц, 899 €), NX.JS9EG.00B (-90SZ, 120 Гц, 945,59 €), NX.JS9EG.00A (-952H, 999 €).
2. **Medion E15433 MD600023** (i7-13620H, 32 ГБ DDR4, 1 ТБ, 15,6") — **699,97 €** (Expert). Самый дешёвый вариант 32 ГБ + 1 ТБ на Intel H.
   ⚠️ Раскладку 2×16 я вывел по брату MD62727 (у него 2 слота, оба заняты). Для MD600023 даташита нет. Порты слабые: USB-C только 2.0, Wi-Fi 5.
3. **Ловушка 1×32 у Acer TravelMate P2 15 (TMP215-75-G2):** SKU, которые продаются за ~1051 € как «32 ГБ / 1 ТБ / Core Ultra 7 155H» (-70VW **NX.BMCEG.001** и -789W **NX.BMGEG.002**), по даташиту Acer и Icecat — **1×32 ГБ**.
   Варианты с 2×16 существуют (NX.BMFEG.002/.003/.008/.009), но их нет в наличии, или они стоят >1300 €.
4. **ASUS:** заводских Intel-SKU 15–16" с 32 ГБ + 1 ТБ дешевле 1200 € не нашёл. Всё, что на billiger идёт как «Vivobook 16 / ExpertBook P1/B1 32 GB», — **сборки магазина one.de**
   (EAN 4049998…; один базовый SKU продаётся с 8–72 ГБ и SSD от 250 ГБ до 4 ТБ). Vivobook 16 X1607CA = распайка + 1 SO-DIMM → только B-список.
5. **MSI, Dynabook, TERRA:** подходящих SKU нет (детали — в таблице внизу).
6. **HEVC у Acer/ASUS в Германии — новая оговорка.** В феврале 2026 суд Мюнхена запретил Acer и ASUS продавать ПК в Германии: Nokia выиграла спор о патентах HEVC. Примерно через 4 месяца стороны договорились.
   Acer после этого поставляет устройства **«с предустановленным кодеком HEVC или без него»**; для устройств без кодека поддержку «можно активировать отдельным ПО через официальные сторонние каналы»
   ([ChannelPartner](https://www.channelpartner.de/article/4187748/acer-und-asus-liefern-wieder.html), [it-boltwise, 23.06.2026](https://www.it-boltwise.de/acer-liefert-wieder-hevc-codec-wahlweise-asus-stoppt-nokia-patentfaelle.html)).
   Какие модели без кодека и выключено ли аппаратное декодирование или только не поставлено расширение Windows — **не сказано**. ASUS подписала лицензию с Nokia в июне 2026 ([heise, 22.06.2026](https://www.heise.de/en/news/Acer-and-Asus-are-selling-PCs-and-notebooks-in-Germany-again-11340710.html)).
   Моё предположение (не проверено): Premiere и Resolve декодируют через драйвер Intel, а не через расширение Windows. Поэтому отсутствие расширения, скорее всего, не мешает монтажу. Отключение на уровне прошивки (как у HP) — мешает. → проверено в браузере 30.09.2026: (п. 5.9) Теста монтажа с отключённым HEVC нет нигде. Бесплатный Resolve и так декодирует процессором (аппаратный H.264/H.265 — только Studio); блокировка задевает не только Media Foundation (OBS на HP) — значит, Premiere и Resolve Studio через Intel HEVC, скорее всего, не получат, «H.265 (Intel QSV)» в HandBrake, скорее всего, пропадёт. Это вывод, не тест ([blackmagicdesign.com](https://www.blackmagicdesign.com/products/davinciresolve/studio)).
   **Для любого Acer: проверить в DXVA Checker / Resolve, работает ли аппаратный HEVC-декод.**

Цена планки 16 ГБ DDR5 SO-DIMM — ~160–260 € (по заданию). Для DDR4 (Medion) докупка не нужна.

---

## A. Заводские 2×16 ГБ SO-DIMM

### Acer Aspire Go 16 AG16-71P-97GF — NX.JS9EG.005
- Даташит ✅ Acer PDF: «Arbeitsspeicherbelegung 2 x 16 GB DDR5 RAM; max 32 GB (2x 16 GB soDIMM)» — [PDF](https://gzhls.at/blob/ldb/b/c/6/3/c4f2489d122d1102bde3c9c4a22390077b90.pdf); Icecat ✅ «2 x 16 GB, 2x SO-DIMM» — [Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Acer&ProductCode=NX.JS9EG.005); страница Acer: [acer.com](https://www.acer.com/de-de/laptops/aspire/aspire-go-intel/pdp/NX.JS9EG.005) (из облака закрыт) → проверено в браузере 30.09.2026: (п. 4.6) NX.JS9EG.00B: 2×16 DDR5 (даташит Acer), гарантия 2 года; второго M.2 у AG16-71P нет — на фото платы (overclockers.ua) один слот, занят ([gzhls.at](https://gzhls.at/blob/ldb/8/b/c/e/ca8e704c7ec56daa9172ecfea07af78d0e40.pdf)).
- CPU: Core i9-13900H (Raptor Lake-H, 13-е пок., 6P+8E, 45/115 Вт) — старое поколение, но не ребренд (класс «как 83HS00BLGE»)
- ОЗУ 2×16 DDR5, свободных слотов нет; SSD 1 ТБ PCIe 4.0 (второй M.2 — не проверено) → проверено в браузере 30.09.2026: (п. 4.6) см. строку 33 ([gzhls.at](https://gzhls.at/blob/ldb/8/b/c/e/ca8e704c7ec56daa9172ecfea07af78d0e40.pdf)).
- Экран: 16" WUXGA IPS ComfyView **120 Гц**, матовый (даташит). Яркость и охват у этого SKU не указаны; у соседних .00B/.00C по Icecat 300 нит, 45 % NTSC
- Графика: Iris Xe (96 EU; Quick Sync: HEVC 10 бит 4:2:2 декод, AV1 декод, без AV1-энкода)
- Порты: 2× USB-C 10 Гбит/с (DP, зарядка 65 Вт), 2× USB-A 5 Гбит/с, HDMI 2.1. **Нет** TB4, RJ45, кардридера (даташит). Wi-Fi 6
- 53 Втч, 1,65 кг, Windows 11 Home, QWERTZ с подсветкой; гарантия 2 года bring-in (даташит)
- Цена: **899,00 €** — technowelt24.de и Expert; 915,40 € — Kaufland ([billiger](https://www.billiger.de/pricelist/5535898327-acer-aspire-go-16-ag16-71p-97gf-16-intel-core-i9-13900h-32-gb-ram-1-tb-ssd-win11-home)).
  За 6 мес. (02.04–30.09.2026) — от **854,05 €** (30.08) до 899 €. Сниппет geizhals для родственного -95Q7 — «ab € 849» (дата не видна)
- HEVC: не проверено (см. оговорку про Acer) → проверено в браузере 30.09.2026: (п. 5.5) Acer публично не уточняет; WinFuture (22.06.2026): часть устройств «ab Werk ohne den HEVC-Codec», ставить «über Drittanbieter». Сообщений о скрытии аппаратного HEVC нет; Acer — лицензиат HEVC Advance. Остаётся тест экземпляра ([winfuture.de](https://winfuture.de/news,159511.html)).

### Acer Aspire Go 16 AG16-71P-95Q7 — NX.JS9EG.00C
- Даташит ✅ «2 x 16 GB DDR5 RAM» — [PDF](https://gzhls.at/blob/ldb/1/8/d/1/0ac8f27c1ae5f5bc4301a158a73bb89177cc.pdf); Icecat ✅ [NX.JS9EG.00C](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Acer&ProductCode=NX.JS9EG.00C)
- Как -97GF, но экран **60 Гц**: WUXGA IPS, 300 нит, 45 % NTSC (Icecat). Icecat пишет «Ethernet: да», даташит Acer — «RJ-45: —»; верю даташиту
- Цена: **899,00 €** + 7,99 € доставка — notebooksbilliger; 907,99 € — Galaxus; 966 € — Heinzsoft ([billiger](https://www.billiger.de/pricelist/5524733469-acer-aspire-go-16-16-intel-core-i9-13900h-32-gb-ram-1-tb-ssd-win11-home)). С 16.06.2026 цена стоит на 899 €

### Acer Aspire Go 16 AG16-71P-90SZ — NX.JS9EG.00B
- Icecat ✅ [NX.JS9EG.00B](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Acer&ProductCode=NX.JS9EG.00B): 32 ГБ DDR5 SO-DIMM, 2 слота, **максимум 32 ГБ** → логически 2×16. Даташит не открывал — **раскладка не проверена напрямую**
- Экран 120 Гц, 300 нит, 45 % NTSC (Icecat)
- Цена: **945,59 €** — JACOB; 956,90 € — TECHNIKdirekt ([billiger](https://www.billiger.de/products/5543976198-acer-aspire-go-16-ag16-71p-90sz-intel-core-i9-13900h-32-gb-ram-1-tb-ssd-win11-home)). За 6 мес. — от **860,76 €** (25.07)

### Acer Aspire Go 16 AG16-71P-952H — NX.JS9EG.00A
- Даташит ✅ «Memory configuration 2 x 16 GB DDR5 RAM» — [PDF](https://gzhls.at/blob/ldb/7/1/4/c/701b5bcede071a685a05f33e429db0daaf2c.pdf); Icecat ✅
- Экран WUXGA IPS (60 Гц по описанию магазина)
- Цена: **999,00 €** — магазин Acer DE; 1089 € — Amazon Marketplace ([billiger](https://www.billiger.de/pricelist/5770961052-acer-aspire-go-16-ag16-71p-intel-core-i9-13900h-32-gb-ram-1-tb-ssd-win11-home)). За 6 мес. — от 949 €

### Medion E15433 — MD600023 (i7-13620H, 32 ГБ DDR4, 1 ТБ)
- Даташит ❌: на medion.com этого SKU нет, похоже, это модель только для Expert. Карточка: [expert.de](https://www.expert.de/shop/unsere-produkte/computer-zubehor/notebooks/laptops/17040046553-e15433-md600023-grau-15-6-zoll-full-hd-intel-core-i7-13620h-1-tb-ssd-32-gb-ddr4-intel-uhd.html)
- ОЗУ: 32 ГБ DDR4. **Раскладка не проверена.** Брат E15433 MD62727 (i5-1334U): «RAM-Steckplätze: 2 x, davon 2 x belegt» ([medion.com](https://www.medion.com/de/shop/p/einsteiger-notebooks-medion-medion-e15433-laptop-intel-core-i5-1334u-windows-11-home-39-6-cm-15-6--fhd-display-1-tb-ssd-32-gb-ram-30040188A1)),
  по Icecat «2 x 16 GB, zweikanalig» ([Icecat 30039505](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Medion&ProductCode=30039505)). Для i7-версии — скорее всего так же
- CPU: i7-13620H (Raptor Lake-H, 6P+4E) — старое поколение; iGPU UHD (64 EU)
- Экран 15,6" FHD (IPS — по Icecat для MD62727; яркость — не проверено) → проверено в браузере 30.09.2026: (п. 4.1) МЕНЯЕТ ВЫВОД (условность снимается): MD600023 = MSN 30041451 — 2×16 DDR4-3200, оба слота заняты (Medion); SSD 1 ТБ, 1,81 кг, блок 65 Вт, HDMI 1.4b, Wi-Fi 5, без подсветки; батарея 55 Втч (idealo); яркость Medion не публикует; срок гарантии — «по гарантийной карте», вопрос продавцу ([service.medion.com](https://service.medion.com/de/product-detail/30041451)).
- Порты (expert.de): 1× USB-C **2.0**, 2× USB-A 5 Гбит/с, 1× USB-A 2.0, HDMI (версия не указана), microSD, DC-in; Wi-Fi 5 (AC 9461), BT 5.1
- У MD62727: 55 Втч, 1,8 кг. Для MD600023 — не проверено → проверено в браузере 30.09.2026: (п. 4.1) см. строку 64 ([service.medion.com](https://service.medion.com/de/product-detail/30041451)).
- Цена: **699,97 €** — Expert; 729,99 € — eBay; 739,99 € — OTTO ([billiger](https://www.billiger.de/products/5438984171-medion-e15433-15-6-intel-core-i7-13620h-32-gb-ram-1-tb-ssd-win11-home)). За 6 мес. — от **658,46 €** (04.08) до 739 €
- HEVC: данных нет. Гарантия у Medion — 24 мес. (для MD62727 по medion.com)
- Проверить: раскладку 2×16 (спросить Expert / открыть крышку), лимиты мощности H-процессора в тонком корпусе (обзора нет)

### Acer Aspire Go 16 AG16-71P-70RK — NX.JTGEG.00P (Core 7 150U — ловушка)
- Icecat ✅ «2 x 16 GB, 2x SO-DIMM, max 32 GB» — [Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Acer&ProductCode=NX.JTGEG.00P); CPU Core 7 150U = Raptor Lake-U refresh (**ловушка**)
- Цена: **849,00 €** — notebooksbilliger; 857,99 € — Galaxus ([billiger](https://www.billiger.de/pricelist/5526050827-acer-aspire-go-16-16-intel-core-7-150u-32-gb-ram-1-tb-ssd-win11-home)). На 50 € дешевле -97GF, но процессор заметно слабее
- Новое по уже известному **AG16-71P-7607**: парт-номер **NX.JTGEG.00N** (Icecat по EAN 4711474879103, раскладка там не указана). Цена 943,16 € (TECHNIKdirekt), 956,96 € (JACOB), 1074,08 € (OTTO)

---

## B16. 16 ГБ + свободный слот

### Acer Aspire Go 15 AG15-72P-792F — NX.JRREG.00B (уже в other-brands; новые цены)
- **729,99 €** (10 предложений), за 6 мес. — от **599,99 €** (23.06) до 799 € ([billiger](https://www.billiger.de/pricelist/5453448297-acer-aspire-go-15-ag15-72p-792f-intel-core-7-150u-16-gb-ram-1-tb-ssd-win11-home)). С планкой ≈ 890–990 €
- Хуже, чем Aspire Go 16 -97GF за 899 € с готовыми 2×16 и i9

Других B16 с 1 ТБ и нормальным CPU в пределах бюджета не нашёл. Пример: Acer TravelMate P2 TMP215-75-G2-TCO-72Z2 **NX.BMFEG.007** (Core Ultra 7 155H, 1×16 + слот, 1 ТБ — Icecat)
стоит от **1104,15 €** ([notebookinfo](https://www.notebookinfo.de/produkt/acer-travelmate-p2-tmp215-75-g2-tco-72z2-47864)); с планкой ≈ 1260–1360 €.

---

## Распайка (B-список)

### ASUS Vivobook 16 X1607CA-MB120 (Core Ultra 7 255H) — сборка one.de 32 ГБ / 1 ТБ
- Платформа (asus.com ✅ [X1607 techspec](https://www.asus.com/de/laptops/for-home/vivobook/asus-vivobook-16-x1607/techspec/)): 8 или 16 ГБ DDR5 распаяны + **1 слот SO-DIMM**, максимум 32 ГБ, 1× M.2 2280 PCIe 4.0.
  Экран 16" WUXGA IPS-level, 60 Гц, 300 нит, 45 % NTSC. Порты: 2× USB-C 5 Гбит/с, 2× USB-A 5 Гбит/с, **HDMI 1.4**. 42 Втч, 1,88 кг
- 32 ГБ здесь поставил **продавец one.de** («aufgerüstet»): EAN 4049998799219, тот же SKU продаётся с 16/32/48/64 ГБ. Скорее всего, 16 распайка + 16 SO-DIMM — **не проверено**
- Цена: **1069,99 €** — OTTO Marketplace (one.de); 1079,98 € — Galaxus; 1099,99 € — Kaufland ([billiger](https://www.billiger.de/pricelist/5775685814-asus-vivobook-16-intel-core-ultra-7-255h-32-gb-ram-1-tb-ssd-win11-pro-quiet-blue)).
  С 07.07.2026 — от 1029,99 €. В комплекте Win11 Pro от продавца
- Заводской брат X1607CA-MB045W (**90NB15A1-M004N0**, Ultra 5 225H, 16 ГБ / 512 ГБ, «On-board + SO-DIMM, 1x SO-DIMM, max 32 GB» — [Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=ASUS&ProductCode=90NB15A1-M004N0)) — 899 € (Expert, Kaufland)
- Аналог **X1607CA-MB058** (Ultra 5 225H, 32 ГБ / **2 ТБ**, тоже one.de) — **1039,99 €** ([billiger](https://www.billiger.de/pricelist/5831294247-asus-vivobook-16-intel-core-ultra-5-225h-32-gb-ram-2-tb-ssd-win11-pro-quiet-blue))
- Плюс: Arrow Lake-H — современный медиадвижок с AV1-энкодом. ASUS называет iGPU «Intel Graphics»; будет ли она работать как Arc при 16+16 — не проверено. Минус: распайка, слабые порты и экран, сборка у продавца → проверено в браузере 30.09.2026: (п. 4.20) X1607CA: варианта с 8 ГБ распайки нет (DE и global); ARK 255H — Arc 140T при ≥ 16 ГБ в двухканале плюс «OEM enablement»; в сноске ASUS 255H нет — будет ли Arc, не подтверждено ([asus.com](https://www.asus.com/laptops/for-home/vivobook/asus-vivobook-16-x1607/techspec/)).

### Acer Aspire 15 A15-51M-93FG — NX.JCJEG.00K (i9-13900H, 32 ГБ LPDDR5)
- Icecat: «32 GB **LPDDR5**-SDRAM», 15,6" FHD, Wi-Fi 6E ([Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Acer&ProductCode=NX.JCJEG.00K)) → распайка. Даташит не открывал
- Цена: **999,00 €** — «Offizieller Acer Store Deutschland» на Amazon; 1199 € и 1217 € — другие ([billiger](https://www.billiger.de/pricelist/5770961070-acer-aspire-15-a15-51m-93fg-intel-core-i9-13900h-32-gb-ram-1-tb-ssd-win11-home))
- Хуже Aspire Go 16 -97GF: тот же CPU, но распайка и 15,6" за бо́льшие деньги

---

## Почти / следить

- **ASUS ExpertBook P1 P1503CVA-S72336** (Core 5 210H — ловушка, = i5-13420H), 32 ГБ / 1 ТБ, Win11 Pro — **1009,99 €** (OTTO Marketplace, one.de) ([billiger](https://www.billiger.de/pricelist/5549327580-asus-expertbook-p1-15-6-intel-core-5-210h-32-gb-ram-1-tb-ssd-win11-pro)).
  Сборка one.de (EAN 4049998792258). Платформа — 2 слота SO-DIMM (см. other-brands). Ещё вариант: 1099 € у IT-tradeport, «mit Notebooktasche», тоже сборка. CPU слабее i7-13620H/i9-13900H
- **Acer TravelMate P2 TMP215-75-G2 с 2×16** (Icecat ✅): **NX.BMFEG.002** (-7774, Ultra 7 155H), **NX.BMFEG.003** (-508E, Ultra 5 125H), **NX.BMFEG.008** (-78X1, 155H), NX.BMFEG.009 (-73HH, 155H, 2 ТБ).
  Платформа хорошая: TB4, USB4, HDMI 2.1, RJ45, microSD, до 64 ГБ, 1,63 кг, **но экран 220 нит** (Icecat .001). -508E у office-partner.de — 1358,94 €, «nicht lieferbar»; -78X1 — «nicht verfügbar» (notebookinfo). Сейчас не купить ≤ 1100 €
- **Acer TravelMate P2 15 Core Ultra 5 125H 16 ГБ / 512 ГБ** — от 745,86 € (billiger; NX.BMCEG.002 — 769,87 €), но SSD 512 ГБ. Раскладка 1×16 + слот подтверждена только у NX.BMFEG.001 (Icecat); у NX.BMCEG.002 — не проверено → проверено в браузере 30.09.2026: (п. 4.21) NX.BMCEG.002: 1×16 DDR5 + слот, до 64 ГБ; 512 ГБ; 3 года Carry-In (даташит Acer) ([gzhls.at](https://gzhls.at/blob/ldb/e/8/f/c/91aa0dfd3d63ace4decc45c43508d57440cd.pdf)).

---

## Ловушки, найденные в этом проходе

| SKU | Что продаётся | Правда (источник) |
|---|---|---|
| Acer TMP215-75-G2-TCO-70VW **NX.BMCEG.001** | «32 GB / 1 TB / Ultra 7 155H», 1050,92 € (office-partner-gmbh) | **1×32 ГБ** — [Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Acer&ProductCode=NX.BMCEG.001) |
| Acer TMP215-75-G2-TCO-789W **NX.BMGEG.002** | «32 GB / 1 TB / 155H», 1051,10 € | **1×32 ГБ** — даташит Acer «Arbeitsspeicherbelegung 1 x 32 GB» ([PDF](https://www.bluechip.de/media/76/08/77/1772618431/Datenblatt_113459.pdf?ts=1772618431)) |
| ASUS Vivobook 16 / ExpertBook P1 / B1 «32/40/48 GB» | много вариантов с Win11 Pro | Сборки one.de (EAN 4049998…), не заводские |
| ASUS Vivobook 15 OLED X1505VA (i9-13900H, OLED 2,8K 120 Гц) | 760–799 € | Максимум **16 ГБ** (Icecat [90NB10P2-M014X0](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=ASUS&ProductCode=90NB10P2-M014X0)). Листинг за 760 € на деле — MA921 с 8 ГБ / 512 ГБ |
| Medion E16443 (i7-13620H, 16") | 749,95 € | 16 ГБ LPDDR5, «RAM-Steckplätze: keine» ([medion.com](https://www.medion.com/de/shop/p/multimedia-notebooks-medion-e16443-laptop-intel-core-i7-13620h-windows-11-home-40-6-cm-16-0--fhd-display-intel-uhd-grafik-1-tb-ssd-16-gb-ram-30038559A1)) |

## Отброшено / не найдено

| Бренд / линейка | Итог |
|---|---|
| ASUS ExpertBook P3 / B3 / B5 16" (Arrow Lake / Meteor Lake) | Только 8–16 ГБ и 256/512 ГБ: P3 16" Ultra 5 225H 8/512 без ОС — 834 €; B3 16" Ultra 5 125H 16/512 — 935,84 €; B5 16" — от 1001,90 € (billiger) |
| ASUS Vivobook S16 (S3607) | В DE только S3607VA (Core 7 240H, 8+8, max 16) — см. other-brands; Arrow Lake S3607CA в продаже не нашёл |
| ASUS Vivobook 16 с Core 9 270H (ловушка) | Только сборки one.de с 8–72 ГБ |
| ASUS Vivobook Pro 15/16 | Без дискретки с Intel — не найдено |
| Acer Swift Go 16 | Intel: 16 ГБ LPDDR5X / 512 ГБ от 949 € (125U); 32 ГБ / 1 ТБ — от 1399 € (155U, Lunar Lake). Распайка, дорого |
| Acer TravelMate P4 16 (TMP416-52/-53/-54) | В продаже 16/512: -53-TCO-59MM (125U) — 950,67 €, -53-TCO-75UQ (155U) — 967,55 €; -54-TCO-79UN 32/1 ТБ — 1457,72 €. NX.B9BEG.002 (2×16) на billiger не найден |
| Acer Extensa 15 EX215-57 (Core 7 150U — ловушка), 32/1 ТБ | 969 € (набор с Office, сумкой и мышью, EAN продавца) / 1029 € (OTTO). Раскладка не проверена; хуже Aspire Go 16 |
| Acer Aspire Go 15 AG15-C513-xx-Tx | Конфигурации продавца (суффикс -32-T1 и т. п.), Core 5 120U — ловушка |
| Acer Aspire 16 AI OLED A16-52M-75LW (Lunar Lake) | Уже в other-brands; сейчас 1143 € (Galaxus, Amazon) — [billiger](https://www.billiger.de/products/5329156961-acer-aspire-16-ai-oled-a16-52m-75lw-intel-core-ultra-7-258v-32-gb-ram-1-tb-ssd) |
| MSI Modern 15 H AI | C1MOG-242 (Ultra 7 155H, 16/512) — 719 €; C2HMG-265 (Ultra 7 255H, 16/512) — 777 € (billiger). SSD 512 ГБ, раскладка не проверена |
| MSI Modern 16S / Prestige 16 AI+ / Venture | Modern 16S Ultra 7 355 16/1 ТБ — 1149 € (распайка 16); Prestige 16 AI+ 32/1 ТБ — от 1595,98 €; Venture — только 17" |
| Medion (кроме E15433) | E15443 Ultra 5 125H 16/512 — 799 €; SPRCHRGD 16 S1 OLED (258V, 32/1 ТБ) — 1299 €; E17433 и Avantum 17 — 17" |
| Wortmann TERRA MOBILE 15–16" | Только i3/i5 13-го пок. U (ловушка) с 8–16 ГБ; 16 ГБ + 1 ТБ: 1516R — 818,62 €, 1517R — 869,90 €; 1610M (Ultra 5 125U) — 16/512 от 705,99 € |
| Captiva (i7-1255U, 12-е пок.) | Уже в other-brands; цены без изменений: I10-0771GE (без ОС) — 885 €, I81-317 — 892 € (voelkner), I82-531 — 987,12 € |
| Dynabook | На billiger ноутбуков нет |

## Проверить на idealo (локальная сессия)

1. NX.JS9EG.005 (AG16-71P-97GF) и NX.JS9EG.00C (-95Q7): минимальная цена, наличие; есть ли вариант без ОС. → проверено в браузере 30.09.2026: (п. 1.10) МЕНЯЕТ ВЫВОД (№2): NX.JS9EG.005 — 849,00 € (technik-brandenburg.de; у Expert 899 €); .00C — 906,99 €; .00B — 951,46 €; .00A — 999 € только с купоном (acer.com) / 1089 € (Amazon MP). Версии без ОС с i9 / 32 / 1 ТБ нет — все Windows 11 Home (фильтр idealo «ohne Betriebssystem» их всё равно показывает, ему верить нельзя) ([idealo.de](https://www.idealo.de/preisvergleich/OffersOfProduct/209373295_-aspire-go-16-ag16-71p-97gf-acer.html)).
2. Medion MD600023: цена; раскладка памяти (2×16?) — спросить продавца или посмотреть фото платы. → проверено в браузере 30.09.2026: (п. 1.16) MD600023 — 699,97 € (expert.de, 14 дн.), мин. 658,46 € (04.08); раскладка 2×16 подтверждена Medion (п. 4.1) ([idealo.de](https://www.idealo.de/preisvergleich/OffersOfProduct/208688812_-e15433-md600023-medion.html)); (п. 4.1) см. строку 64 ([service.medion.com](https://service.medion.com/de/product-detail/30041451)).
3. Любой Acer из списка: есть ли в описании пометка «ohne HEVC» / «HEVC-Codec nicht vorinstalliert». → проверено в браузере 30.09.2026: (п. 1.24) Пометок «ohne HEVC» / «HEVC-Codec nicht vorinstalliert» нет ни в карточках idealo и geizhals, ни у NBB и Galaxus; acer.com не открылся (ERR_HTTP2). По карточке не определить — только тест экземпляра ([idealo.de](https://www.idealo.de/preisvergleich/OffersOfProduct/209220720_-aspire-go-16-ag16-71p-95q7-acer.html)).
4. NX.BMFEG.002 / .003 / .008 (TravelMate P2, 2×16): вдруг где-то появятся ≤ 1100 €. → проверено в браузере 30.09.2026: (п. 1.17) NX.BMFEG.002 / .003 / .008 на idealo нет (искал по P/N и по кодам -7774, -508E, -78X1); есть только .009 (2 ТБ) — от 1249 € (Amazon MP) и .007 ([idealo.de](https://www.idealo.de/preisvergleich/OffersOfProduct/207760108_-travelmate-p2-tmp215-75-g2-tco-nx-bmfeg-009-acer.html)).
