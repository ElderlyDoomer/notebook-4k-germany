## Проверка lenovo-thinkpad

_Проверено 30.09.2026 (облачная сессия, скептическая проверка). SKU: ThinkPad E16 Gen 2 Intel **21MA000RGE** / **21MA003RGE**, ThinkPad E16 Gen 3 Intel (Lunar Lake) **22AY004XGE** / **22AY004VGE**._
_Первоисточник — PDF PSREF по каждому MTM (`https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=<MTM>&country_code=`) и PDF платформ: [E16 Gen 2 Intel, ред. 04.02.2026](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_E16_Gen_2_Intel/ThinkPad_E16_Gen_2_Intel_Spec.PDF), [E16 Gen 3 Intel, ред. 27.07.2026](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_E16_Gen_3_Intel/ThinkPad_E16_Gen_3_Intel_Spec.PDF). Сверено с Icecat (open) по EAN. Цены и история — billiger.de (дневной минимум за 6 мес., 02.04–30.09.2026), Alternate.de, сайты магазинов. Цены из облака — перепроверить на idealo._

### Вывод

1. **Раскладка памяти подтверждена у всех четырёх.** Опровергнуть не удалось.
   - E16 Gen 2 (21MA000RGE, 21MA003RGE): **2×16 ГБ SO-DIMM DDR5-5600**, оба слота заняты, максимум 64 ГБ. PSREF: «2x 16GB SODIMM DDR5-5600», «Two DDR5 SODIMM slots, dual-channel capable». Icecat: «Speicherlayout 2 x 16 GB», «2x SO-DIMM». Свободен **второй слот M.2 2280** (PSREF: «only one SSD configuration with a second slot for user self-expansion»).
   - E16 Gen 3 (22AY004XGE, 22AY004VGE): **32 ГБ LPDDR5X-8533 на корпусе процессора (MoP)**, слотов нет, двухканал, апгрейда нет. Слот M.2 **один** (2280), в нём SSD 2242 на 1 ТБ. Это B-список (распайка).
2. **Зарядка в комплекте у всех четырёх** — 65 Вт USB-C (PSREF «Power Adapter: 65W USB-C (3-pin)», Icecat «AC-Netzadapter: Ja»). Планку докупать не нужно, поэтому **итог = цена + доставка**.
3. **Сегодня ни один SKU не укладывается в 1100 €.**
   - 21MA000RGE — 1194,28 € с доставкой, единственный продавец на Amazon Marketplace, «Nur noch 1 auf Lager».
   - 21MA003RGE — 1299 €, Easynotebooks, в наличии.
   - 22AY004XGE — 1207,78 € с доставкой, тот же единственный продавец Amazon MP, 1 шт.
   - 22AY004VGE — 1242,62 €, Galaxus.
   Ближе всего к цели 22AY004VGE: за полгода он стоил ≤ 1100 € 149 дней из 182, последний раз 09.09.
4. **CPU.** Ловушек имени нет.
   - 125U — Meteor Lake-U (2P+8E+2LPE, 4 Xe, «Intel Graphics», не Arc): для таймлайна 4K слабый.
   - 155H — Meteor Lake-H, Arc 8 Xe (Arc работает, потому что 2×16 в двухканале).
   - 228V — Lunar Lake 4P+4LPE, 8 потоков, Arc 130V (7 Xe2). Медиадвижок LNL: HEVC 4:2:2 10 бит — декод и энкод, AV1 — энкод, VVC — декод (`notes/intel-cpu.md`, [Wikipedia](https://en.wikipedia.org/wiki/Lunar_Lake)). Многопоточная производительность ниже, чем у Meteor/Arrow Lake-H.
5. **Экран.** Годный для цвета только у **22AY004XGE**: WQXGA IPS 400 нит, 100 % sRGB, 120 Гц VRR, 1200:1 (PSREF). Notebookcheck намерил на такой же панели E16 G3 (Arrow Lake) 99,1 % sRGB и 445 нит. У остальных трёх экран WUXGA IPS 300 нит, 45 % NTSC, 800:1, 60 Гц (Notebookcheck на E16 G2 AMD: 58,2 % sRGB).
6. **HEVC.** Отключение у Lenovo не задокументировано.
   - В PDF PSREF этих четырёх MTM и обеих платформ слов HEVC/H.265/codec нет (проверил поиском по тексту).
   - Блог devinthreethousand упоминает Lenovo только в заголовке, ни одной модели и ни одного теста Lenovo в тексте нет ([статья, 21.11.2025](https://devinthreethousand.substack.com/p/hevc-hardware-support-being-removed)). В статье smith6612 Lenovo нет ([статья](https://smith6612.me/2026/04/19/its-me-i-started-the-hevc-disablement-press-storm/)).
   - Прямого подтверждения, что HEVC включён, тоже нет. Риск низкий, но после покупки проверить DXVA Checker'ом в срок возврата.

### Сводная таблица (billiger.de, 30.09.2026)

| MTM | CPU (класс) | ОЗУ | SSD / M.2 | Экран | БП | Цена сейчас (с доставкой) | Мин. 6 мес. | Дней ≤ 1100 € | Итог | Вердикт |
|---|---|---|---|---|---|---|---|---|---|---|
| 21MA000RGE | Ultra 5 125U — Meteor Lake-U (современный, слабый для 4K) | 2×16 SO-DIMM ✅ | 1 ТБ 2242 + свободный 2280 | WUXGA 300 нит 45 % NTSC | 65 Вт ✅ | 1190,28 + 4 € = **1194,28 €**, Amazon MP TechPoint1111, 1 шт. | **843,57 €** (01.06) | 85 / 182, последний раз 02.07 | 1194,28 € | не держать (вытеснен ThinkBook 16 G8 21SK0083GE) |
| 21MA003RGE | Ultra 7 155H — Meteor Lake-H, Arc 8 Xe (старее, ок) | 2×16 SO-DIMM ✅ | 1 ТБ 2242 + свободный 2280 | WUXGA 300 нит 45 % NTSC | 65 Вт ✅ | **1299,00 €**, Easynotebooks, «Sofort ab Lager» | **1092,61 €** (22.04) | 8 / 182 (20–27.04) | 1299 € | наблюдать, алерт ≤ 1100 € (шанс низкий) |
| 22AY004XGE | Ultra 5 228V — Lunar Lake, Arc 130V (современный, распайка) | 32 LPDDR5X MoP (B) ✅ | 1 ТБ 2242, слот один | **WQXGA 400 нит 100 % sRGB 120 Гц** | 65 Вт ✅ | 1203,78 + 4 € = **1207,78 €**, Amazon MP TechPoint1111, 1 шт. | **909,16 €** (22.09, 1 день) | 14 / 182 (03–14.06 по 1099 €; 21–22.09) | 1207,78 € | лучший B-вариант; алерт ≤ 1100 € |
| 22AY004VGE | Ultra 5 228V — Lunar Lake, Arc 130V | 32 LPDDR5X MoP (B) ✅ | 1 ТБ 2242, слот один | WUXGA 300 нит 45 % NTSC | 65 Вт ✅ | **1242,62 €**, Galaxus (1 рабочий день) | **961,12 €** (09.09, 1 день) | 149 / 182, последний раз 09.09 | 1242,62 € | B-запасной: брать при ≤ 1100 €, только если -XGE недоступен → проверено в браузере 30.09.2026: (п. 1.8) МЕНЯЕТ ВЫВОД (№9): 22AY004XGE — 1207,78 € (Amazon MP), мин. за 6 мес. 1099 € — цены 909 € на idealo не было. 22AY004VGE — 1242,62 € (Galaxus), мин. 961,12 € (09.09), ≤ 1100 € 168 дней; 21MA000RGE — 1194,28 € (Amazon MP); 21MA003RGE — 1299 €; 21UR005AGE — 1205 €; 21MS004SGE — 1245,58 € (Amazon MP, возможна AZERTY) ([idealo.de](https://www.idealo.de/preisvergleich/OffersOfProduct/209382346_-thinkpad-e16-g3-22ay004xge-lenovo.html)). |

«Дней ≤ 1100 €» — по дневному минимуму billiger. Какой магазин дал минимум, график не показывает. Входит ли доставка в дневной минимум — не проверено.

### По SKU

#### ThinkPad E16 Gen 2 Intel — 21MA000RGE (EAN 0197530206962)
- PSREF ([страница](https://psref.lenovo.com/Detail/ThinkPad/ThinkPad_E16_Gen_2_Intel?M=21MA000RGE), [PDF](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=21MA000RGE&country_code=)):
  - CPU и память: Core Ultra 5 125U (12C: 2P+8E+2LPE / 14T, до 4,3 ГГц), Integrated Intel Graphics; 2×16 SO-DIMM DDR5-5600, два слота, до 64 ГБ.
  - SSD: 1 ТБ M.2 2242 PCIe 4.0 x4 Opal. Слотов M.2 два: 2242 и 2280.
  - Экран: 16" WUXGA IPS 300 нит, антиблик, 45 % NTSC (в таблице платформы: 800:1, 60 Гц).
  - Порты: 1× TB4/USB4 40 Гбит/с (DP 2.1), 1× USB-C 20 Гбит/с (DP 1.4), USB-A 5 и 10 Гбит/с, HDMI 2.1 (4K60), RJ45. **Кардридера нет.**
  - Питание и вес: 57 Втч, **65 Вт USB-C в комплекте**, от 1,81 кг, алюминий.
  - Прочее: Win 11 Pro (DE), подсветка клавиатуры. Гарантия 1 год Courier/Carry-in + «Included Upgrade: 1Y Premier WHB (CPN)» (расшифровка не проверена). Анонс 19.03.2024.
- Icecat ([open](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Lenovo&ProductCode=21MA000RGE)): «Speicherlayout 2 x 16 GB», «2x SO-DIMM», «AC-Netzadapter: Ja», 65 Вт, 1 TB4. Совпадает с PSREF.
- Цена ([billiger](https://www.billiger.de/pricelist/4907757793-lenovo-thinkpad-e16-g2-intel-core-ultra-5-125u-32-gb-ram-1-tb-ssd-21ma000rge); старая ссылка `/products/4907757793…` отдаёт 410):
  - предложения: **1190,28 € + 4 € доставка**, Amazon Marketplace, продавец **TechPoint1111**, «Nur noch 1 auf Lager». «2 предложения» — это один и тот же продавец в двух фидах Amazon.
  - нет в наличии: [JACOB](https://www.jacob.de/produkte/lenovo-tp-e16-21ma000rge-artnr-100472016.html) («nicht verfügbar»), [Bechtle](https://www.bechtle.com/shop/lenovo-thinkpad-e16-g2-u5-32-gb-1-tb--4814336--p) (OutOfStock), [lapstore](https://www.lapstore.de/a.php/shop/lapstore/lang/en/a/72852/kw/Lenovo-ThinkPad-E16-Gen-2-21MA000RGE/) («sold out»). На Alternate.de по MTM не найден. Страница Easynotebooks — 404.
  - история: **минимум 843,57 € (01.06)**. ≤ 1100 € держалась 02.04–24.06 и 02.07, с 03.07 — 1117–1499 €. С 05.09 цена скачет между 1120,98 и 1289 €.
- Опровергнуто / поправлено:
  - «6-мес. минимум 968,10 €» (`candidates-lenovo-hp-dell.md`) — это нижняя граница полосы «normaler Preis» billiger. Реальный минимум 843,57 € (в `sweep-deals-watch.md` уже верно).
  - «2 предложения» — по факту один продавец и одна штука.
- Вывод: модель 2024 года, распродана у нормальных магазинов. CPU слабее, чем у ThinkBook 16 G8 21SK0083GE (225U, те же 2×16, есть SD, продаётся в магазинах за 1122 €) → **в топ-10 не держать**.

#### ThinkPad E16 Gen 2 Intel — 21MA003RGE (EAN 0198153668939)
- PSREF ([страница](https://psref.lenovo.com/Detail/ThinkPad/ThinkPad_E16_Gen_2_Intel?M=21MA003RGE), [PDF](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=21MA003RGE&country_code=)):
  - CPU: Core Ultra 7 155H (16C: 6P+8E+2LPE / 22T, до 4,8 ГГц), **Integrated Intel Arc Graphics**.
  - Остальное как у 21MA000RGE: 2×16 SO-DIMM DDR5-5600, 1 ТБ 2242 + свободный 2280, WUXGA 300 нит 45 % NTSC, 57 Втч, **65 Вт USB-C в комплекте**, 1,81 кг, порты те же, без SD. Анонс 09.04.2024.
  - Мелочь: у 155H в комплекте всего 65 Вт (у ThinkBook 16 G7 с тем же 155H — 100 Вт).
- Icecat ([open](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Lenovo&ProductCode=21MA003RGE)): «2 x 16 GB», «2x SO-DIMM», Intel Arc Graphics, «AC-Netzadapter: Ja».
- Цена ([billiger](https://www.billiger.de/products/4907757817-lenovo-thinkpad-e16-g2-intel-core-ultra-7-155h-32-gb-ram-1-tb-ssd-21ma003rge)):
  - предложения: **1299,00 €** Easynotebooks (бесплатная доставка, «Sofort ab Lager lieferbar, 24h Express möglich»; на [easynotebooks.de](https://www.easynotebooks.de/Notebooks/Lenovo/ThinkPad/E-Serie/485171/Lenovo-ThinkPad-E16-G2-16-WUXGA-Core-Ultra-7-155H-32GB-RAM-1TB-SSD-Win11-Pro) MPN и EAN совпадают с PSREF, schema.org — InStock); маркетплейс netfactory_gmbh 1373,78 €; 1400,90 € с доставкой; Amazon MP DASTRO 1430,54 €; маркетплейс Easynotebooks 1481,95 €. Всего 8 предложений, до 1516,09 €.
  - история: **минимум 1092,61 € (22.04)**. ≤ 1100 € — только 20–27.04. В сентябре 1155,80–1299 €, с 22.09 — 1299 €.
  - На Alternate.de по MTM не найден.
- Подтверждено (из `sweep-deals-watch.md`): минимум 1092,61 €, 8 дней ≤ 1100 €. «6-мес. мин. 1127,70 €» (таблица в `candidates-lenovo-hp-dell.md`) — это граница полосы, а не минимум.
- Вывод: пакет A-класса (155H + Arc + 2×16 + TB4), продаётся в нормальном магазине. Но до 1100 € цена опускалась лишь 8 дней в апреле → **только в наблюдение** (алерт ≤ 1100 €).

#### ThinkPad E16 Gen 3 Intel (Lunar Lake) — 22AY004XGE (EAN 0199274286095)
- PSREF ([страница](https://psref.lenovo.com/Detail/ThinkPad/ThinkPad_E16_Gen_3_Intel?M=22AY004XGE), [PDF](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=22AY004XGE&country_code=)):
  - CPU и память: Core Ultra 5 228V (8C: 4P+4LPE / 8T, до 4,5 ГГц), Arc 130V, NPU 40 TOPS (Copilot+). **«32GB Soldered LPDDR5X-8533, MoP Memory»**, «no slots, dual-channel», «not upgradable».
  - SSD: 1 ТБ M.2 2242 PCIe 4.0 x4 Opal 2.0. «Lunar Lake: one M.2 2280 PCIe 4.0 x4 slot» — второго слота нет.
  - Экран: **16" WQXGA (2560×1600) IPS 400 нит, 100 % sRGB, 120 Гц** (в таблице платформы: 1200:1, VRR, Eyesafe 2.0).
  - Порты: **2× TB4/USB4 40 Гбит/с** (PD 15–65 Вт, DP 2.1; второй — «Optional Ports (configured)», в PDF платформы: «Port 5 is Thunderbolt 4 (models with Lunar Lake)»), USB-A 5 и 10 Гбит/с, HDMI 2.1 (4K60), RJ45. Без SD.
  - Питание и вес: 64 Втч, **65 Вт USB-C в комплекте**, от 1,62 кг, алюминий.
  - Прочее: Wi-Fi 6E AX211, Win 11 Pro (DE). Гарантия 1 год Courier/Carry-in + 1Y Premier WHB (CPN). Анонс 20.01.2026.
- Icecat ([open](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Lenovo&ProductCode=22AY004XGE)): LPDDR5X-8533 «On-board», max 32 ГБ, «Zweikanalig», 2560×1600 400 нит sRGB 120 Гц, 2 TB4, 64 Втч, «AC-Netzadapter: Ja».
- Цена ([billiger](https://www.billiger.de/products/5527165842-lenovo-thinkpad-e16-g3-intel-core-ultra-5-228v-32-gb-ram-1-tb-ssd-22ay004xge)):
  - предложения: **1203,78 € + 4 €**, Amazon MP **TechPoint1111**, «Nur noch 1 auf Lager». «2 предложения» — один продавец в двух фидах.
  - не продают: [Bechtle](https://www.bechtle.com/shop/lenovo-thinkpad-e16-g3-u5-32-gb-1-tb--4982152--p) (OutOfStock); на Alternate.de поиск по MTM выдаёт только 22AY004VGE, а старый URL товара 100190043 открывает главную.
  - история (серия «billiger»; 07–19.09 частично пунктир «billiger_missing»):
    - апрель–май — 1134–1182 €;
    - **1099 € — 03–14.06** (Notebookcheck 02/08.06: Galaxus 1099 €, Klarsicht-it 1148,81 € — [NBC](https://www.notebookcheck.com/ThinkPad-mit-2-5k-Bildschirm-Core-Ultra-5-32-GB-RAM-1-TB-SSD-im-Angebot.1313444.0.html));
    - июль–август — 1115–1299 €;
    - 21.09 — 1045,50 €, **22.09 — 909,16 €** (магазин неизвестен, похоже на короткий сбой или акцию маркетплейса);
    - с 23.09 — 1204–1328 €.
  - до окна billiger: Alternate 925 € (NBC, 08/13.03.2026 — [NBC](https://www.notebookcheck.com/Lenovo-ThinkPad-E16-mit-2-5k-Bildschirm-sRGB-120-Hz-Core-Ultra-5-32-GB-RAM-1-TB-SSD-im-Angebot.1245288.0.html)). Подтверждает строку в `market.md`, но это март, и сейчас Alternate его не продаёт.
- Поправлено: «909,16 € 21–22.09 (2 дня)» (`sweep-deals-watch.md`) — 909,16 € было только 22.09; 21.09 — 1045,50 €. Оба дня ≤ 1100 €.
- Вывод: **лучший B-вариант группы** (экран, 2× TB4, 64 Втч, 1,62 кг). Минусы: распайка, один M.2, 8 потоков, продавец сейчас один. Держать в B-списке с алертом ≤ 1100 €.

#### ThinkPad E16 Gen 3 Intel (Lunar Lake) — 22AY004VGE (EAN 0199274286118)
- PSREF ([страница](https://psref.lenovo.com/Detail/ThinkPad/ThinkPad_E16_Gen_3_Intel?M=22AY004VGE), [PDF](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=22AY004VGE&country_code=)):
  - всё как у 22AY004XGE (228V, 32 ГБ LPDDR5X MoP, 1 ТБ, один M.2 2280, **2× TB4**, 64 Втч, 65 Вт в комплекте, 1,62 кг);
  - отличие — экран: **16" WUXGA IPS 300 нит, 45 % NTSC, 60 Гц** (800:1).
- Icecat ([open](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Lenovo&ProductCode=22AY004VGE)): «Anzahl Thunderbolt 4-Ports: 2», 1920×1200 300 нит NTSC 60 Гц, «AC-Netzadapter: Ja».
- Цена ([billiger](https://www.billiger.de/products/5527165900-lenovo-thinkpad-e16-g3-intel-core-ultra-5-228v-32-gb-ram-1-tb-ssd-22ay004vge)):
  - предложения: **1242,62 €** Galaxus.de (без пометки «Marktplatz», доставка за 1 рабочий день, 30 дней бесплатного возврата; сам сайт Galaxus из облака закрыт — перепроверить); Amazon MP TechPoint1111 1443,81 € + 4 €; маркетплейс SKWarenhandel 1521,99 €. Всего 4 предложения. → проверено в браузере 30.09.2026: (п. 1.8) см. строку 35 ([idealo.de](https://www.idealo.de/preisvergleich/OffersOfProduct/209382346_-thinkpad-e16-g3-22ay004xge-lenovo.html)).
  - [Alternate](https://www.alternate.de/Lenovo/ThinkPad-E16-G3-22AY004VGE-Notebook/html/product/100190040): 1249,00 € (зачёркнуто 1356,60), «Artikel kann derzeit nicht gekauft werden». EAN совпадает, «Zubehör: 65 Watt Netzteil».
  - история: **минимум 961,12 € (09.09, 1 день)**. ≤ 1100 € — 149 дней из 182 (обычно 1055–1095 €), до 09.09 включительно. С 10.09 цена 1125–1255 €.
- Опровергнуто / поправлено (`sweep-lenovo.md`):
  - «Минимум за 6 месяцев 1078,67 €» — это граница полосы billiger. Реальный минимум 961,12 € (в `sweep-deals-watch.md` верно).
  - «Порты: 1× TB4/USB4» — **неверно: 2× TB4** (PSREF по MTM, примечание платформы про Port 5, Icecat).
  - «Galaxus (Marktplatz)» — billiger показывает предложение самого Galaxus.de без пометки «Marktplatz».
- Вывод: из четырёх чаще всего бывал ≤ 1100 €, но экран 45 % NTSC для цветокоррекции не годится (нужен внешний монитор). **B-запасной**: брать при ≤ 1100 €, если -XGE недоступен.

### Известные проблемы (обзоры того же шасси)

- **E16 Gen 2 Intel:** собственного обзора Notebookcheck нет. На страницах серии только LaptopMedia (155H) ([NBC-сводка](https://www.notebookcheck.net/Lenovo-ThinkPad-E16-Gen-2.909545.0.html)). Сам laptopmedia.com отдаёт 403, поэтому его выводы («quiet fan during heavy CPU stress»; по сниппету поиска — панель MNG007QS1-3, без PWM, ~353 нит, узкий охват) — **не проверено напрямую**. → проверено в браузере 30.09.2026: (п. 5.22) LaptopMedia, E16 Gen 2 Intel: панель MNG007QS1-3 — 49 % sRGB, 353 нит, без PWM; вентилятор «quiet»; 155H через 10–15 мин держит только 28 Вт ([laptopmedia.com](https://laptopmedia.com/review/lenovo-thinkpad-e16-gen-2-intel-review-great-value-for-a-quiet-performer/)).
- **E16 Gen 2 AMD (то же шасси и панель MNG007QS1-3):** 83,8 %, 08.10.2024 ([NBC](https://www.notebookcheck.net/Lenovo-ThinkPad-E16-Gen-2-AMD-laptop-review-Cuts-corners-mostly-in-the-right-places.899320.0.html)):
  - экран: 364 нит в центре, **58,2 % sRGB**, 1456:1, PWM нет, **засветка по краям**;
  - корпус жёсткий, но сильно собирает отпечатки;
  - RAM, SSD, Wi-Fi и батарея легко доступны, есть свободный слот 2280;
  - производительность под долгой нагрузкой стабильная;
  - клавиатура хуже, чем у T-серии.
- **Сестра E14 G6 Intel (155U):** «the Core Ultra 155U is already running very warm on the E14 G6 chassis» — сомнения насчёт H-серии в этом шасси ([NBC](https://www.notebookcheck.net/Lenovo-ThinkPad-E14-G6-laptop-review-Fixes-lots-of-problems-on-the-E14-G5.927075.0.html)). У 16-дюймового E16 G2 с 155H троттлинг — **не проверено**. → проверено в браузере 30.09.2026: (п. 5.22) см. строку 111 ([laptopmedia.com](https://laptopmedia.com/review/lenovo-thinkpad-e16-gen-2-intel-review-great-value-for-a-quiet-performer/)).
- **E16 Gen 3 (обзор на Arrow Lake 225U с той же 2,5K-панелью):** 87 %, 16.07.2025 ([NBC](https://www.notebookcheck.net/Lenovo-ThinkPad-E16-G3-Review-Affordable-office-laptop-is-even-better-with-a-120-Hz-display.1059930.0.html)):
  - экран: 445 нит, 99,1 % sRGB, 71,3 % P3, 1352:1, PWM нет, отклик 5,9 / 12,6 мс;
  - «the hinges are a bit too light and there is some wobbling» — экран покачивается на шарнирах;
  - центр клавиатуры слегка продавливается.
  Та ли же панель стоит в 22AY004XGE — не проверено, но в PSREF платформы вариант 2,5K один. → проверено в браузере 30.09.2026: (п. 4.19) 22AY004XGE: панель 2560×1600 IPS 400 нит, 100 % sRGB, 120 Гц (PSREF), но у FRU два «äquivalent» — производитель панели может отличаться от теста NBC ([psref.lenovo.com](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=22AY004XGE&country_code=DE)).
- **Lunar Lake в E-серии (E14 Gen 7, 228V, 32 ГБ):** 87 %, 25.11.2025 ([NBC](https://www.notebookcheck.net/Lenovo-ThinkPad-E14-Gen-7-review-Lunar-Lake-delivers-longer-battery-life-but-brings-trade-offs.1170838.0.html)):
  - PL1 28 Вт / PL2 37 Вт;
  - многопоточная производительность заметно ниже, чем у версии с Arrow Lake;
  - нагрев низкий;
  - «the second SSD slot has also been eliminated»;
  - SD нет.
  Отдельного обзора E16 Gen 3 на Lunar Lake нет.
- BIOS и массовые жалобы (форумы Lenovo) по E16 Gen 2/Gen 3 Intel — не нашёл (не проверено).

### Что сделать перед покупкой
- Проверить цену на idealo по MTM. У TechPoint1111 (Amazon MP) уточнить, что товар новый, запечатанный, с немецкой раскладкой. → проверено в браузере 30.09.2026: (п. 1.8) см. строку 35 ([idealo.de](https://www.idealo.de/preisvergleich/OffersOfProduct/209382346_-thinkpad-e16-g3-22ay004xge-lenovo.html)).
- После получения:
  - 21MA: CPU-Z → SPD, два модуля по 16 ГБ; в диспетчере задач «Используется гнёзд: 2 из 2»;
  - все четыре: DXVA Checker — есть ли профили HEVC_VLD_Main10 / 4:2:2. Проверить в 14-дневный срок возврата.
