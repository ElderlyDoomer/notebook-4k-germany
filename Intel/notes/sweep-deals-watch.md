# Добор: сделки и «ждать просадку» — Intel, заводские 2×16, 1 ТБ, 15–16"

_2026-09-30, облачная сессия. Цены — billiger.de (предложения магазинов и дневной график за 6 мес., 02.04–30.09.2026), статьи notebookcheck.com «im Angebot» 2026, сниппеты mydealz/поиска. «Из облака — перепроверить на idealo»._
_Раскладка памяти — Icecat (данные производителя) и PSREF (по `candidates-lenovo-hp-dell.md` / `sweep-lenovo.md`). Уже известные SKU повторяю только с новыми фактами (в основном — реальные 6-мес. минимумы)._

## Коротко

1. **Сегодня (30.09) нет ни одного SKU** с заводскими 2×16, 1 ТБ и современным CPU (Meteor/Arrow Lake-H, Panther Lake), который стоит ≤ 1100 €. С ~19–20.09 ThinkBook 16 G8 резко подорожал (21SK007KGE: 1095 € 18.09 → 1349–1380 €; 21SK0083GE: < 1100 € до 19.09 → 1122 €).
2. **Но за полгода такие цены были часто.** Лучший кандидат «ждать просадку» — **ThinkBook 16 G8 IAL 21SK007KGE (Core Ultra 7 255H)**: ≤ 1100 € — 76 дней из 182, минимум **1049,01 €** (27–31.08), сейчас 1349 €.
   Дальше — ThinkPad E16 G2 **21MA003RGE** (155H): 1092,61 € в апреле, сейчас 1299 €; ThinkBook 16 G7 **21MS0054GE** (155H): 1092,49 € в начале апреля, сейчас 1299 € (только Amazon Marketplace).
3. **Поправка к прошлым заметкам.** В тексте страницы billiger «Preisentwicklung X € Y €» — это границы **типичного диапазона** за 6 мес., а **не минимум**. Реальный дневной минимум лежит в JSON графика и ниже:
   21SK0083GE — 881,50 € (а не 989,73); 21MA000RGE — 843,57 (не 968,10); 21MS004SGE — 775,65 (не 894,98); 21MA003RGE — 1092,61 (не 1127,70); 21SK007KGE — 1049,01 (не 1078,83); 22AY004VGE — 961,12 (не 1078,67).
   Дневное значение — это цена «ab» у billiger в этот день, в том числе от маркетплейсов (Amazon MP, eBay, Kaufland); одно-двухдневные провалы могут быть ошибкой магазина.
4. **ThinkBook 16 G8 21SK0083GE (225U)** почти всё полугодие стоил < 1100 € (171 из 182 дней, до 19.09 включительно; минимум 881,50 € 11.06). Сейчас 1122 €. Если ждать — он вернётся первым.
5. **B-список (распайка):** Medion SPRCHRGD 16 S1 OLED **30040200** (258V, 2,8K OLED 120 Гц) — **999 €** 73 дня (май–июнь, июль–09.08), сейчас 1299 €. ThinkPad E16 G3 **22AY004XGE** (2,5K 120 Гц, 100 % sRGB) — **909,16 € 21–22.09** (2 дня), 1099 € в июне; сейчас 1203,78 €.
6. **HP ProBook 4 G1i 16 C7SS0ES (255H, 2×16) стоил 999 €** (15–29.04), ProBook 460 G11 B2MK4ES (155H) — 999–1075 € весной. **HEVC отключён (QuickSpecs) → не брать** даже по этим ценам.
7. Panther Lake с SO-DIMM ≤ 1150 € за полгода **не было**: ThinkBook 16 G9 21UR005AGE — минимум 1205 € (= сегодня), E16 Gen 4 — от 1380 € (кроме однодневного 740,76 € — вероятно ошибка).

## Метод

- billiger.de: поиск по каждому CPU (125H/135H/155H/165H/185H, 225H/235H/255H/265H/285H, 322/325/332/335/338H/355/356H/365/366H/X7 358H, для сравнения 125U/155U/225U/255U) с фильтрами «Notebooks», RAM = 32 ГБ, SSD = 1 ТБ, сортировка по цене; ~416 лотов.
  Для всех 15–16" с ценой ≤ 1800 € (≈ 75 лотов) снят график за 6 мес. (JSON `data-pricehistory-data` на странице товара), предложения магазинов и EAN; посчитаны дни ≤ 1100 и ≤ 1150 €.
- notebookcheck.com: статьи «im Angebot» 2025–2026 по 32 ГБ + Core Ultra + 16". mydealz: поиск без JS отдаёт только первый тред — использовал один сниппет.
- Раскладка: Icecat по MTM/EAN (поле «Speicherlayout»). PSREF API из облака требует токен — не обходил, PSREF-ссылки взяты из прошлых заметок.
- Не открывал (блок): idealo, geizhals, printus.de («Pardon Our Interruption»). mydealz-треды без slug → 410.

---

## A. Заводские 2×16 + современный CPU — сейчас дороже 1100 €, «ждать просадку»

### Lenovo ThinkBook 16 G8 IAL — 21SK007KGE ⭐ главный кандидат на просадку
- Даташит: PSREF ✅ ([21SK007KGE](https://psref.lenovo.com/Detail/ThinkBook/ThinkBook_16_G8_IAL?M=21SK007KGE)); Icecat ✅ «Speicherlayout 2 x 16 GB, 2x SO-DIMM, max 64 GB» ([Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Lenovo&ProductCode=21SK007KGE)); NBC: «32 GB RAM (2x 16 GB, DDR5-5600, zwei Slots)».
- CPU Core Ultra 7 255H (Arrow Lake-H), iGPU Arc 140T. 1 ТБ M.2 2242 + свободный 2280. 16" WUXGA IPS 300 нит, 45 % NTSC, 60 Гц.
- Порты: 1× TB4, 1× USB-C 10 Гбит/с, HDMI 2.1, SD, RJ45, 2× USB-A. 45 Втч, 65 Вт, 1,7 кг, Win 11 Pro (Icecat).
- **Сейчас: 1349,00 €** Easynotebooks; Amazon MP 1383,88; Heinzsoft 1507,90; Kaufland 1536,49; Galaxus 1548 (8 предложений) — [billiger](https://www.billiger.de/products/5228830251-lenovo-thinkbook-16-g8-ial-21sk007kge). → проверено в браузере 30.09.2026: (п. 1.2) МЕНЯЕТ ВЫВОД (цифры): 21SK007KGE — 1399,00 € (easynotebooks), а не 1349 €; мин. за 6 мес. на idealo 910 € (03.09), а не 1049 €; ≤ 1100 € — 89 дней, последний 18.09 ([idealo.de](https://www.idealo.de/preisvergleich/OffersOfProduct/206151089_-thinkbook-16-g8-21sk007kge-lenovo.html)).
- **6 мес.: минимум 1049,01 € (27–31.08).** ≤ 1100 € — 76 дней: 02–29.04 (1068), 06.05–12.06 (1079), 27–31.08 (1049), 07–11.09 (1100), 18.09 (1095). Типичный диапазон 1078,83–1174,93 €. Максимум 1380,39 (25.09).
- Сделки: NBC 30.11.2025 — **934,15 €** (Amazon.de и Lenovo Shop) ([NBC](https://www.notebookcheck.com/Core-Ultra-7-32-GB-RAM-1-TB-SSD-Lenovo-Office-Notebook-im-Angebot.1174221.0.html)); NBC 24.03.2026 — **1068 €** Notebookstore.de ([NBC](https://www.notebookcheck.com/Lenovo-ThinkBook-16-mit-Core-Ultra-7-32-GB-RAM-1-TB-SSD-im-Angebot.1257770.0.html)); mydealz 15.06.2026 — 1113,90 € Heinzsoft с купоном (сниппет поиска mydealz, тред 2795625).
  Сниппеты поиска, дата неизвестна: LAP4WORX 1032 €, Alternate 1079 €, C-NW 1073,95 € — не проверено (страницы сейчас без цены/404).
- HEVC: неизвестно; в PSREF оговорок нет (см. `sweep-lenovo.md`).
- Вывод: **ставить алерт ≤ 1100 €** (idealo/billiger). Весь пакет (255H, 2×16, TB4, SD, RJ45, 2 M.2) — лучший из найденных; слабое место — экран 45 % NTSC.

### Lenovo ThinkPad E16 Gen 2 (Intel) — 21MA003RGE
- Даташит: PSREF ✅ (таблица в `candidates-lenovo-hp-dell.md`); Icecat ✅ «2 x 16 GB, 2x SO-DIMM, max 64 GB» ([Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Lenovo&ProductCode=21MA003RGE)).
- Core Ultra 7 155H (Meteor Lake-H), Arc. 1 ТБ. 16" WUXGA IPS 300 нит NTSC. 1× TB4, HDMI 2.1, RJ45, **без SD**. 57 Втч, 1,81 кг, Win 11 Pro.
- **Сейчас: 1299,00 €** Easynotebooks (подтверждено на [easynotebooks.de](https://www.easynotebooks.de/Notebooks/Lenovo/ThinkPad/E-Serie/485171/Lenovo-ThinkPad-E16-G2-16-WUXGA-Core-Ultra-7-155H-32GB-RAM-1TB-SSD-Win11-Pro)); eBay 1373,78; Heinzsoft 1400,90; Amazon MP 1430,54; Kaufland 1481,95 — [billiger](https://www.billiger.de/products/4907757817-lenovo-thinkpad-e16-g2-intel-core-ultra-7-155h-32-gb-ram-1-tb-ssd-21ma003rge).
- **6 мес.: минимум 1092,61 € (20–27.04, 8 дней ≤ 1100).** ≤ 1150 € — 88 дней (апрель–июнь, начало июля, 28.07–08.08). Типичный диапазон 1127,70–1199,93.
- Сниппет поиска: eBay.de 1076,76 € (дата неизвестна).
- HEVC: неизвестно (PSREF без оговорок).
- Вывод: следить, цель ≤ 1100 €. Модель 2024 г. — остатки, предложений всё меньше.
- Близнецы: **21MA000PGE** (то же, WUXGA) — 1490,40 € (1 предложение, Kaufland), минимум 1187,83 (26.05) — неинтересно.
  **21MA004UGE** (155H, 2×16, **2,5K 400 нит sRGB** — [Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Lenovo&ProductCode=21MA004UGE)) — на billiger нет; lapstars 1121 € «nicht mehr lieferbar» ([lapstars](https://www.lapstars.de/lenovo-thinkpad-e16-intel-g2-21ma004uge)) → снят с продажи.

### Lenovo ThinkBook 16 G7 IML — 21MS0054GE
- Даташит: PSREF ✅ (таблица в `candidates-lenovo-hp-dell.md`); Icecat ✅ «2 x 16 GB, 2x SO-DIMM, max 64 GB» ([Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Lenovo&ProductCode=21MS0054GE)).
- Core Ultra 7 155H, Arc. 1 ТБ. 16" WUXGA 300 нит NTSC. 1× TB4, HDMI 2.1, SD, RJ45. Icecat: 71 Втч (не сверено с PSREF), 1,7 кг.
- **Сейчас: 1299,00 €** — только Amazon Marketplace (2 предложения) — [billiger](https://www.billiger.de/products/4934173452-lenovo-thinkbook-16-g7-iml-intel-core-ultra-7-155h-32-gb-ram-1-tb-ssd-win11-pro-arctic-grey-21ms0054ge).
- **6 мес.: минимум 1092,49 € (02–03.04)**; ≤ 1150 € — 14 дней (02–15.04), дальше 1233–1380 €.
- Вывод: модель 2024 г., нормальных магазинов нет — шанс просадки низкий.

### Lenovo ThinkBook 16 G9 IPL — 21UR005AGE (Panther Lake) — уже в заметках, новое: история
- Core Ultra 5 325, 2×16 (Icecat ✅, PSREF ✅), 1 ТБ, 400 нит, 2× TB4, SD, RJ45, 48 Втч, 1,7 кг ([Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Lenovo&ProductCode=21UR005AGE)).
- **Сейчас 1205,00 € (c-nw) = минимум за 6 мес.**; Heinzsoft 1209,91, lapstars 1215, Notebookstore 1219,90 — [billiger](https://www.billiger.de/products/5542697625-lenovo-thinkbook-16-g9-intel-core-ultra-5-325-32-gb-ram-1-tb-ssd-win11-pro-21ur005age). Диапазон за полгода 1205–1394 €; ≤ 1150 € не был ни разу.
- Вывод: цена медленно падает (billiger: «Aktuell sehr günstig»). До 1100 € — вряд ли раньше Black Friday.
- Брат 21UR0058GE (Ultra 7 355): 1499,98 € (25n.de), минимум 1327,29 (02.04) — вне бюджета.

### Lenovo ThinkPad P16s Gen 3 (Intel) — 21KS0001GE (аномалия, не цель)
- Core Ultra 7 155H, 2×16 до 96 ГБ, 2× TB4, HDMI 2.1, RJ45, 75 Втч, 1,82 кг, WUXGA 300 нит ([Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Lenovo&ProductCode=21KS0001GE)).
- Сейчас 1739,69 € (Galaxus); **950 € с 04 по 12.05** (9 дней), всё остальное время ≥ 1400 € — [billiger](https://www.billiger.de/pricelist/4970000313-lenovo-thinkpad-p16s-g3-intel-core-ultra-7-155h-32-gb-ram-1-tb-ssd-intel-arc-graphics-21ks0001ge). Магазин эпизода неизвестен; Bechtle — «nicht mehr verfügbar» (сниппет).
- Вывод: разовая распродажа или ошибка; модель снимается. Только если снова всплывёт ≤ 1100 €.

### Lenovo ThinkPad E16 Gen 4 (Intel) — 21YC000MGE (Panther Lake) — уже в заметках, новое
- Ultra 5 325, 2×16 (Icecat), 400 нит, 2× TB4, 64 Втч. Сейчас 1560 € (Notebookstore 1566,90). На графике **740,76 € 01.09 — один день, почти наверняка ошибка цены**; в остальное время ≥ 1380 €. Не цель.

---

## Не «современный» CPU (U-серия), 2×16, 1 ТБ — уже известны, новое: реальные минимумы

| SKU | CPU | Сейчас (billiger 30.09) | Реальный мин. за 6 мес. | Дней ≤ 1100 € |
|---|---|---|---|---|
| **21SK0083GE** ThinkBook 16 G8 | Ultra 5 225U (ловушка-лайт) | 1122 € Easynotebooks, JB-Computer; Electronis 1135,88; Proshop 1137,52; JACOB 1139,64 (13 предл.) | **881,50 € (11.06)** | **171 из 182** (02.04–19.09 без перерыва) |
| 21MA000RGE ThinkPad E16 G2 | Ultra 5 125U | 1190,28 € (только Amazon MP) | 843,57 € (01.06) | 85 (02.04–24.06, 02.07) |
| 21MS004SGE ThinkBook 16 G7 | Ultra 5 125U | 1241,58 € (только Amazon MP) | 775,65 € (03.06) | 141 (последний раз 15.09) |
| 21SA004AGE ThinkPad L16 G2 | Ultra 7 255U (ловушка-лайт) | 1510,61 € Heinzsoft / lapstars 1511,47 | 999 € (22–28.05) | 7 |
| 21SA0049GE ThinkPad L16 G2 | Ultra 5 225U | 1299 € (lapstars 1304) | 1198 € (03.07) | 0 |

- 21SK0083GE: NBC 23.05.2026 — **927,55 €** у Minaxum.it (Италия) ([NBC](https://www.notebookcheck.com/Core-Ultra-5-32-GB-RAM-1-TB-SSD-Lenovo-ThinkBook-16-G8-im-Angebot.1304169.0.html)). [billiger](https://www.billiger.de/products/5228834927-lenovo-thinkbook-16-g8-ial-21sk0083ge).
- 21SA004AGE: Icecat — 2×16, 400 нит, 2× TB4, 57 Втч, 1,79 кг ([Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Lenovo&ProductCode=21SA004AGE)).
- Ссылки billiger: [21MA000RGE](https://www.billiger.de/pricelist/4907757793-lenovo-thinkpad-e16-g2-intel-core-ultra-5-125u-32-gb-ram-1-tb-ssd-21ma000rge), [21MS004SGE](https://www.billiger.de/pricelist/4952539795-lenovo-thinkbook-16-g7-iml-intel-core-ultra-5-125u-32-gb-ram-1-tb-ssd-win11-pro-arctic-grey-21ms004sge), [21SA004AGE](https://www.billiger.de/products/5310779993-lenovo-thinkpad-l16-g2-intel-core-ultra-7-255u-32-gb-ram-1-tb-ssd-21sa004age).

---

## B-список: распаянные 32 ГБ (Lunar Lake / Panther Lake)

### Medion SPRCHRGD 16 S1 OLED — 30040200 (MD62744) ⭐ лучший B-вариант по экрану
- Icecat ✅ по EAN 4061275241600 ([Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&GTIN=4061275241600)); NBC ([22.06.2026](https://www.notebookcheck.com/Deal-Medion-SPRCHRGD-16-S1-OLED-mit-32-GB-RAM-und-Lunar-Lake-gibts-jetzt-zum-Allzeit-Bestpreis.1326199.0.html), [29.07.2026](https://www.notebookcheck.com/Abverkauf-Medion-Multimedia-Notebook-mit-Lunar-Lake-32-GB-RAM-1-TB-SSD-2-8k-OLED.1354760.0.html)).
- Core Ultra 7 258V (Lunar Lake), 32 ГБ LPDDR5X-8533 распайка, 1 ТБ. **16" OLED 2880×1800, 120 Гц, 500 нит, DCI-P3.** 1× USB4 40 Гбит/с + USB-C, HDMI 2.0, 3× USB-A, microSD. 80,5 Втч, 1,49 кг, Win 11 Home.
- **Сейчас 1299 €** coolblue; Energeto 1354,98; Kaufland 1590,99 — [billiger](https://www.billiger.de/products/5357141091-medion-sprchrgd-16-s1-oled-intel-core-ultra-7-258v-32-gb-ram-1-tb-ssd-win11-home).
- **6 мес.: минимум 999 €** (08.05–24.06 и 16.07–09.08); ≤ 1100 € — 99 дней. NBC: 999 € у computeruniverse (и Cyberport.at), «Allzeit-Bestpreis».
- HEVC: неизвестно (Medion, данных нет). Гарантия — не проверено. → проверено в браузере 30.09.2026: (п. 5.6) Сообщений об отключении HEVC у ASUS, MSI, Gigabyte, Medion, Captiva, TERRA нет; ASUS, MSI и Acer — лицензиаты HEVC Advance, Gigabyte, Medion, Wortmann и Captiva — нет (само по себе не признак отключения) ([accessadvance.com](https://accessadvance.com/hevc-advance-patent-pool-licensees/)).
- Вывод: при 999–1050 € — лучший B-вариант (экран для монтажа несравнимо лучше IPS 45 % NTSC). Память не расширить.

### Lenovo ThinkPad E16 Gen 3 — 22AY004XGE (уже в заметках; новое)
- 228V, 32 ГБ LPDDR5X, 2,5K IPS 120 Гц 400 нит 100 % sRGB, 2× TB4, RJ45, 64 Втч.
- Сейчас 1203,78 € (только Amazon MP) — [billiger](https://www.billiger.de/products/5527165842-lenovo-thinkpad-e16-g3-intel-core-ultra-5-228v-32-gb-ram-1-tb-ssd-22ay004xge).
- **6 мес.: 909,16 € 21–22.09** (2 дня, магазин неизвестен); 1099 € — 03–14.06 (12 дней). NBC 02.06/08.06.2026: Galaxus 1099 €, Klarsicht-it 1148,81 € ([NBC](https://www.notebookcheck.com/ThinkPad-mit-2-5k-Bildschirm-Core-Ultra-5-32-GB-RAM-1-TB-SSD-im-Angebot.1313444.0.html)); NBC 04.08.2026: ~1200 € Office-Partner / Klarsicht-it ([NBC](https://www.notebookcheck.com/ThinkPad-mit-Core-Ultra-7-32-GB-RAM-1-TB-SSD-2-5k-Display-im-Angebot.1359661.0.html)).
- Вывод: цель ≤ 1100 € (бывало дважды за полгода).

### Lenovo ThinkPad E16 Gen 3 — 22AY004VGE (уже в заметках; новое)
- 228V, WUXGA 300 нит 45 % NTSC. Сейчас 1242,62 € (Galaxus) — [billiger](https://www.billiger.de/products/5527165900-lenovo-thinkpad-e16-g3-intel-core-ultra-5-228v-32-gb-ram-1-tb-ssd-22ay004vge).
- **≤ 1100 € — 149 дней** (обычно 1055–1094 €, минимум 961,12 € 09.09); с 10.09 — выше. Экран хуже, чем у -XGE, — брать только если -XGE недоступен. → проверено в браузере 30.09.2026: (п. 1.8) МЕНЯЕТ ВЫВОД (№9): 22AY004XGE — 1207,78 € (Amazon MP), мин. за 6 мес. 1099 € — цены 909 € на idealo не было. 22AY004VGE — 1242,62 € (Galaxus), мин. 961,12 € (09.09), ≤ 1100 € 168 дней; 21MA000RGE — 1194,28 € (Amazon MP); 21MA003RGE — 1299 €; 21UR005AGE — 1205 €; 21MS004SGE — 1245,58 € (Amazon MP, возможна AZERTY) ([idealo.de](https://www.idealo.de/preisvergleich/OffersOfProduct/209382346_-thinkpad-e16-g3-22ay004xge-lenovo.html)).

### Прочие B (для справки)
- **22AY004WGE** E16 G3 (258V, 2,5K 120 Гц 400 нит sRGB, 2× TB4, 64 Втч — [Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Lenovo&ProductCode=22AY004WGE)) — сейчас 1599 € Easynotebooks; минимум 1099 € (20–26.06).
- **22AY001UGE** E16 G3 (258V, WUXGA) — 1411,71 €; минимум 1098 € (09.09, 1 день).
- **Acer Aspire 16 AI OLED NX.JP1EG.007** (уже в заметках) — 1143 € (Galaxus, Amazon MP); 21–30.04 — 1090,99 €; 02–03.04 — 750 € (вероятно ошибка).
- **Acer Swift Go 16 AI SFG16-74-71TF — NX.JNMEG.005** (258V, OLED 2048×1280 120 Гц, SD, 1,52 кг — [Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&GTIN=4711474712110)) — 1399 € (Galaxus 1402,86, NBB 1406,99, Acer DE 1499); минимум 1149 € (02–09.04). HEVC у Acer — см. оговорку про Nokia в `sweep-asus-acer-msi-medion.md`.
- **MSI Prestige 16 AI+ C3MG-071** (уже в заметках; Ultra 7 355, 2,8K OLED 120 Гц, 2× TB4, 81 Втч) — 1595,98 € JACOB; минимум **1149 € (16–19.06)**.
- **HP OmniBook X Flip 16-as0177ng — BZ8B4EA** (258V, 2880×1800 OLED 120 Гц touch, 1× TB4, 68 Втч, 1,88 кг — [Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&GTIN=0199251800924)) — 1399 € NBB; минимум 1199 € (45 дней, май–июль). HEVC у потребительских HP — не проверено. → проверено в браузере 30.09.2026: (п. 5.3) Сообщений по ProBook 4 G1iR, 250/250R G10, HP 15-fd1, Pavilion 16, OmniBook 5 16 и X Flip 16 нет; у free-codecs источников нет. Новое: потребительский HP OmniBook 7 Aero 13 (AMD) — DXVA без HEVC (форум HP, 04.07.2025) ([h30434.www3.hp.com](https://h30434.www3.hp.com/t5/Notebook-Video-Display-and-Touch/H265-HEVC-HW-encoder-and-decoder-not-available/td-p/9431209)).

---

## Ловушка HEVC: дешёвые HP с 2×16 — не брать

| SKU | CPU | Сейчас | Минимум за 6 мес. | Почему нет |
|---|---|---|---|---|
| HP ProBook 4 G1i 16 **C7SS0ES** | Ultra 7 255H | 1269 € (NBB 1276,99, Galaxus 1277,99) | **999 € (15–29.04)** | HEVC отключён — [QuickSpecs c09102587](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09102587) |
| HP ProBook 4 G1i 16 C7SR2ES | Ultra 5 225H | 1199 € NBB | 1060,32 € (09.09); 1099 € 02–16.04 | то же |
| HP ProBook 4 G1i 16 C7SS3ES | Ultra 7 255H | 1499 € | 1164,20 € (09.09) | то же |
| HP ProBook 460 G11 **B2MK4ES** | Ultra 7 155H | 1319 € (Amazon MP) | 999 € (02.04); 1074,99 € 04.05–10.06 | серия 400 G11 в списке HP с отключённым HEVC |

Источники цен: [C7SS0ES](https://www.billiger.de/products/5406906479-hp-probook-4-g1i-16-intel-core-ultra-7-255h-32-gb-ram-1-tb-ssd-c7ss0es), [B2MK4ES](https://www.billiger.de/pricelist/5165815851-hp-probook-460-g11-intel-core-ultra-7-155h-32-gb-ram-1-tb-ssd-win11-pro-b2mk4es). NBC писал о ProBook 4 G1i 16 с Ultra 7 / 32 ГБ за 999 € ([NBC](https://www.notebookcheck.com/Core-Ultra-7-32-GB-RAM-1-TB-SSD-HP-ProBook-im-Angebot.1257073.0.html)).

---

## Отброшено / не подтверждено

- **Acer TravelMate P2 15 «Ultra 5 225H / 32 ГБ / 1 ТБ»** (лот billiger 5830414105, 1135,60 €, минимум 1046,16 € 22.07; ≤ 1100 € 73 дня) — по EAN 4711474961334 это **TMP215-55-G2-TCO-5346, NX.BLREG.003**. У Galaxus в названии «512 GB, 16 GB»; Icecat и Easynotebooks характеристик не дают. Конфигурация **не подтверждена** — не кандидат до даташита ([billiger](https://www.billiger.de/pricelist/5830414105-acer-travelmate-p2-15-6-intel-core-ultra-5-225h-32-gb-ram-1-tb-ssd-win11-pro)). → проверено в браузере 30.09.2026: (п. 4.22) NX.BLREG.003 (TMP215-55-G2-TCO-5346): Core Ultra 5 115U / 16 ГБ (1×16) / 512 ГБ по даташиту Acer — не «225H / 32 / 1 ТБ»; не кандидат ([gzhls.at](https://gzhls.at/blob/ldb/f/c/d/0/34b90439880ea7a02b26bc4c34954c68cc41.pdf)).
- **ThinkBook 16 G8 IAL 21SK00K6GE** (Ultra 9 185H, **1×16 + слот, 512 ГБ** — Icecat) — 897,89 € Easynotebooks, минимум 749 € (13.08); NBC 19.08.2026: 799 € JB-Computer ([NBC](https://www.notebookcheck.com/Lenovo-ThinkBook-16-mit-Core-Ultra-9-im-Angebot.1372576.0.html)). Нет 1 ТБ; с планкой 16 ГБ и SSD во второй слот — > 1100 € (цену SSD не проверял).
- **Medion S10 OLED MD62633** (155H, 4K OLED, 1 ТБ) — 999 € Amazon.de (NBC 28.07.2026, [NBC](https://www.notebookcheck.com/Core-Ultra-7-1-TB-SSD-4k-Bildschirm-Medion-Notebook-16-Zoll-im-Angebot.1353489.0.html)) — **2×8 ГБ**, для 32 ГБ менять обе планки (~480 €).
- ASUS Vivobook 16 X1607CA 255H «32/1 ТБ» — сборка one.de (уже в `sweep-asus-acer-msi-medion.md`), без изменений: 1069,99 € OTTO, минимум 1029,99 €.
- ThinkPad E16 Gen 3 с 255H/225U и 32 ГБ (21SR0041GE, 21SR0046GE, 21SR000JGE, 21SR007BGE) — **1×32** (см. `candidates-lenovo-hp-dell.md`); минимумы 1109–1199 € не важны.
- Captiva I99-xxx / Business I10-145xGE (255H, 15,3") — минимумы 1388–1607 €; XMG EVO 15 M25 — 1699 €; Tarox Modula X16 (155H) — 1369 €; ASUS ExpertBook B5 16 (225H) — 1749 €. Всё вне бюджета.
- 14" (ThinkBook 14 G9 21UX005NGE 1279 €, ThinkPad E14 G6/G7, Zenbook 14, TravelMate P6 14 и т. п.) — вне 15–16".

---

## Список «ждать просадку» (алерты на idealo / billiger)

| Приоритет | SKU | Тип | Цель | Сейчас | Мин. за 6 мес. | Как часто бывало |
|---|---|---|---|---|---|---|
| 1 | **21SK007KGE** ThinkBook 16 G8, Ultra 7 255H | A | ≤ 1100 € | ~~1349 €~~ 1399 € (idealo, 30.09) | 1049,01 € (27.08; на idealo — 910 € 03.09) | 76 дней из 182 (на idealo — 89) → проверено в браузере 30.09.2026: (п. 1.2) см. строку 35 ([idealo.de](https://www.idealo.de/preisvergleich/OffersOfProduct/206151089_-thinkbook-16-g8-21sk007kge-lenovo.html)). |
| 2 | **21SK0083GE** ThinkBook 16 G8, Ultra 5 225U | A (CPU слабее) | ≤ 1000 € | 1122 € | 881,50 € (11.06) | ≤ 1100 — 171 день |
| 3 | **30040200** Medion SPRCHRGD 16 S1 OLED, 258V | B (распайка) | ≤ 1050 € | 1299 € | 999 € | 99 дней ≤ 1100 → проверено в браузере 30.09.2026: (п. 1.9) 30040200 — 1299,00 € (coolblue, 30 дн.); 999 € было 100 дней за полгода, последний раз 10.08; цели ≤ 1050 € сейчас нет ([idealo.de](https://www.idealo.de/preisvergleich/OffersOfProduct/207280444_-sprchrgd-16-s1-30040200-medion.html)). |
| 4 | **22AY004XGE** ThinkPad E16 G3 2,5K, 228V | B (распайка) | ≤ 1100 € | ~~1203,78 €~~ 1207,78 € (Amazon MP, idealo 30.09) | 909,16 € (22.09, billiger; на idealo такой цены не было — мин. 1099 €) | 14 дней (на idealo — 12) |
| 5 | **21MA003RGE** ThinkPad E16 G2, Ultra 7 155H | A | ≤ 1100 € | 1299 € | 1092,61 € (апрель) | 8 дней (≤ 1150 — 88) |
| 6 | 21UR005AGE ThinkBook 16 G9, Ultra 5 325 | A (Panther Lake) | ≤ 1100 € | 1205 € | 1205 € (сейчас) | ни разу |
| 7 | 21MA000RGE / 21MS004SGE (125U) | A (U-серия) | ≤ 1000 € | 1190 / 1242 € (Amazon MP) | 843,57 / 775,65 € | 85 / 141 день |

Ближайшие поводы: Amazon Prime Deal Days (сниппеты mydealz 29.09 — «Early Prime Days» уже идут), Black Friday 27.11.

## Источники

- billiger.de — страницы товаров (ссылки в блоках), график `data-pricehistory-data` за 02.04–30.09.2026, предложения и EAN, 30.09.2026.
- Icecat Open Catalog — раскладка памяти и порты (ссылки в блоках).
- notebookcheck.com — статьи «im Angebot»: [1174221](https://www.notebookcheck.com/Core-Ultra-7-32-GB-RAM-1-TB-SSD-Lenovo-Office-Notebook-im-Angebot.1174221.0.html), [1257770](https://www.notebookcheck.com/Lenovo-ThinkBook-16-mit-Core-Ultra-7-32-GB-RAM-1-TB-SSD-im-Angebot.1257770.0.html), [1304169](https://www.notebookcheck.com/Core-Ultra-5-32-GB-RAM-1-TB-SSD-Lenovo-ThinkBook-16-G8-im-Angebot.1304169.0.html), [1313444](https://www.notebookcheck.com/ThinkPad-mit-2-5k-Bildschirm-Core-Ultra-5-32-GB-RAM-1-TB-SSD-im-Angebot.1313444.0.html), [1326199](https://www.notebookcheck.com/Deal-Medion-SPRCHRGD-16-S1-OLED-mit-32-GB-RAM-und-Lunar-Lake-gibts-jetzt-zum-Allzeit-Bestpreis.1326199.0.html), [1353489](https://www.notebookcheck.com/Core-Ultra-7-1-TB-SSD-4k-Bildschirm-Medion-Notebook-16-Zoll-im-Angebot.1353489.0.html), [1354760](https://www.notebookcheck.com/Abverkauf-Medion-Multimedia-Notebook-mit-Lunar-Lake-32-GB-RAM-1-TB-SSD-2-8k-OLED.1354760.0.html), [1359661](https://www.notebookcheck.com/ThinkPad-mit-Core-Ultra-7-32-GB-RAM-1-TB-SSD-2-5k-Display-im-Angebot.1359661.0.html), [1372576](https://www.notebookcheck.com/Lenovo-ThinkBook-16-mit-Core-Ultra-9-im-Angebot.1372576.0.html).
- mydealz — сниппет поиска «ThinkBook 16 G8» (тред 2795625, 15.06.2026, 1113,90 € Heinzsoft); сам тред из облака не открылся (410 без slug).
- Easynotebooks.de, lapstars.de — страницы товаров, 30.09.2026.
