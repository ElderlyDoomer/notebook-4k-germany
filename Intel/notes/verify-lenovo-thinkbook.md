## Проверка lenovo-thinkbook

_Проверено 30.09.2026 (облачная сессия, скептическая проверка). SKU: ThinkBook 16 G8 IAL 21SK0083GE / 21SK007KGE, ThinkBook 16 G7 IML 21MS004SGE / 21MS0054GE, ThinkBook 16 G9 IPL 21UR005AGE._
_Первоисточник — PDF PSREF по каждому MTM: `https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=<MTM>&country_code=` (та же кнопка «Export PDF» на странице PSREF). Сверено с Icecat (open) по EAN; цены и история — billiger.de; Alternate.de; Easynotebooks.de. Цены из облака — перепроверить на idealo._

### Вывод

1. **Раскладка 2×16 ГБ SO-DIMM DDR5-5600 подтверждена у всех пяти SKU** — в PDF PSREF по каждому MTM, в Icecat и (для G8) в обзорах-сделках Notebookcheck. Опровергнуть не удалось.
   Оба слота памяти заняты (так и нужно), максимум 64 ГБ. **Свободен второй слот M.2 2280** (PSREF: «Lenovo offers only one SSD configuration with a second slot for user self-expansion»).
   Единственное противоречие: Alternate для 21SK0083GE пишет «2 Speicherbänke, davon belegt 1». PSREF, Icecat и Easynotebooks говорят 2×16. Считаю это ошибкой карточки Alternate, но при получении стоит проверить (CPU-Z → SPD / диспетчер задач → «Используется гнёзд: 2 из 2»).
2. **Зарядка в комплекте у всех пяти** (PSREF: 65 Вт USB-C; у 21MS0054GE — 100 Вт USB-C Slim). Планку докупать не нужно, поэтому **итог = цена**.
3. **Сегодня ни один SKU не укладывается в 1100 €.** Ближе всех **21SK0083GE — 1122 €** (Easynotebooks, «Sofort ab Lager»). За полгода он стоил ≤ 1100 € 171 день из 182, последний раз 19.09.
   21SK007KGE (255H) — 1349 €; за полгода ≤ 1100 € был 76 дней, последний раз 18.09. G7 продаются только через Amazon Marketplace. G9 (1205 €) за полгода ни разу не опускался ниже 1205 €.
4. **Экран у всех пяти слабый для цветокоррекции:** 16" WUXGA IPS, 45 % NTSC, 60 Гц (300 нит; у G9 — 400 нит). Notebookcheck намерил у той же серии 59–61 % sRGB. Для работы с цветом в 4K нужен внешний монитор (есть TB4/HDMI 2.1).
5. **HEVC:** отключение у Lenovo не задокументировано. В PDF PSREF этих пяти MTM слов HEVC/H.265 нет. Прямого подтверждения, что HEVC включён, тоже нет → проверить DXVA Checker'ом в окно возврата.

### Сводная таблица (billiger.de, 30.09.2026)

| MTM | CPU (класс) | ОЗУ | SSD / M.2 | Экран | БП | Цена сейчас | Мин. 6 мес. | Дней ≤ 1100 € | Итог | Вердикт |
|---|---|---|---|---|---|---|---|---|---|---|
| 21SK0083GE | Ultra 5 225U — Arrow Lake-U = Meteor Lake-U refresh (ловушка имени, медиадвижок современный) | 2×16 ✅ | 1 ТБ 2242 + свободный 2280 | WUXGA 300 нит 45 % NTSC | 65 Вт ✅ | **1122,00 €** Easynotebooks / JB-Computer, в наличии | **881,50 €** (11–12.06) | 171 / 182 | 1122 € | наблюдать, ждать ≤ 1100 € |
| 21SK007KGE | Ultra 7 255H — Arrow Lake-H, Arc 140T (современный) | 2×16 ✅ | 1 ТБ 2242 + свободный 2280 | WUXGA 300 нит 45 % NTSC | 65 Вт ✅ | 1349,00 € Easynotebooks, в наличии | **1049,01 €** (27–29.08, 31.08) | 76 / 182 | 1349 € | лучший по мощности; алерт ≤ 1100 € |
| 21MS004SGE | Ultra 5 125U — Meteor Lake-U (старее, слабый для 4K) | 2×16 ✅ | 1 ТБ 2242 + свободный 2280 | WUXGA 300 нит 45 % NTSC | 65 Вт ✅ | 1241,58 € (+4 € доставка), Amazon MP TechPoint1111, 1 шт. | 775,65 € (03–04.06), история «пилой» | 141 / 179 | 1245,58 € | не рекомендую (вытеснен 21SK0083GE) |
| 21MS0054GE | Ultra 7 155H — Meteor Lake-H, Arc (старее, ок) | 2×16 ✅ | 1 ТБ 2242 + свободный 2280 | WUXGA 300 нит 45 % NTSC | **100 Вт** ✅ | 1299,00 € Amazon MP REBERION, 14 шт. | 1092,49 € (02–03.04) | 2 / 182 | 1299 € | не рекомендую (шанс ≤ 1100 € низкий) |
| 21UR005AGE | Ultra 5 325 — Panther Lake 4P+4LPE, 4 Xe3 (современный, но младший) | 2×16 ✅ | 1 ТБ 2242 (**QLC?**) + свободный 2280 | WUXGA **400 нит** 45 % NTSC | 65 Вт ✅ | 1205,00 € c-nw; Alternate 1308 € в наличии | 1205,00 € (= сегодня) | 0 / 182 | 1205 € | наблюдать (низкий приоритет) |

«Дней ≤ 1100 €» — по дневному минимуму billiger. Магазин, давший минимум, график не показывает. Включена ли в дневной минимум доставка — не проверено.

### По SKU

#### ThinkBook 16 G8 IAL — 21SK0083GE (EAN 198156460400)
- PSREF ([страница](https://psref.lenovo.com/Detail/ThinkBook/ThinkBook_16_G8_IAL?M=21SK0083GE), [PDF](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=21SK0083GE&country_code=)):
  - CPU и память: Core Ultra 5 225U (2P+8E+2LPE / 14T, до 4,8 ГГц), Intel Graphics; «2x 16GB SODIMM DDR5-5600», «Two DDR5 SODIMM slots, dual-channel capable», до 64 ГБ.
  - SSD: 1 ТБ M.2 2242 PCIe 4.0 x4; «Two M.2 2280 PCIe 4.0 x4 slots».
  - Экран: WUXGA IPS 300 нит, 45 % NTSC, 60 Гц.
  - Питание и вес: 45 Втч, **65 Вт USB-C в комплекте**, 1,7 кг.
  - Порты: 1× TB4/USB4 40 Гбит/с (DP 2.1), 1× USB-C 10 Гбит/с (DP 1.4), HDMI 2.1 (4K60), SD, RJ45, 2× USB-A 5 Гбит/с.
  - Прочее: Wi-Fi 6E, Win 11 Pro (DE), подсветка клавиатуры. Гарантия: 1 год Courier/Carry-in + «Included Upgrade: 1Y Premier WHB (CPN)» (расшифровка не проверена). Анонс 27.02.2025.
- Icecat ([open](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Lenovo&ProductCode=21SK0083GE)): «Speicherlayout 2 x 16 GB», «2x SO-DIMM», «AC-Netzadapter: Ja», 65 Вт.
- Notebookcheck (сделка 23.05.2026): «32 GB RAM (2x 16 GB, DDR5-5600, zwei Slots)… Dual-Channel» и «äußerlich baugleiche Vorgängermodell» (G7) — [NBC](https://www.notebookcheck.com/Core-Ultra-5-32-GB-RAM-1-TB-SSD-Lenovo-ThinkBook-16-G8-im-Angebot.1304169.0.html).
- CPU: Arrow Lake-U — «uses refreshed Meteor Lake silicon fabricated on the Intel 3 node» ([Wikipedia](https://en.wikipedia.org/wiki/Arrow_Lake_(microprocessor))). Медиадвижок как у Meteor Lake: декодирует HEVC 10 бит 4:2:2, кодирует AV1 (`notes/intel-cpu.md`). iGPU — 4 Xe, не Arc: для эффектов в таймлайне 4K слабо.
- Цена ([billiger](https://www.billiger.de/products/5228834927-lenovo-thinkbook-16-g8-ial-21sk0083ge)):
  - предложения: **1122,00 €** Easynotebooks (бесплатная доставка, «Sofort ab Lager lieferbar»; подтверждено на [easynotebooks.de](https://www.easynotebooks.de/Notebooks/Lenovo/ThinkPad/ThinkBook/1092306/Lenovo-ThinkBook-16-G8-IAL-16-WUXGA-Core-Ultra-5-225U-32GB-1TB-SSD-Win11-Pro), EAN совпадает с PSREF); JB-Computer 1122,00 € (1–2 рабочих дня); Electronis 1135,88; Proshop 1137,52; JACOB 1139,64; всего 13 предложений.
  - история: минимум 881,50 € (11–12.06); ≤ 1000 € — 58 дней; до 19.09 — 1081,01 €, с 20.09 — 1122 €.
  - Alternate: 1110 €, «Artikel kann derzeit nicht gekauft werden» ([Alternate](https://www.alternate.de/Lenovo/ThinkBook-16-G8-IAL-21SK0083GE-Notebook/html/product/100137135)).
- Опровергнуто / поправлено:
  - «6-мес. минимум 989,73 €» (`candidates-lenovo-hp-dell.md`, `MEMORY.md`) — это нижняя граница «нормальной цены» billiger, а не минимум. Реальный минимум — 881,50 € (в `sweep-deals-watch.md` уже исправлено).
  - Alternate «belegt 1 Speicherbank» — противоречит PSREF и Icecat (см. «Вывод»).
  - Сниппеты geizhals «ab 997,90 / 1045,58 €» (`market.md`) проверить нельзя: geizhals блокирует облако.

#### ThinkBook 16 G8 IAL — 21SK007KGE (EAN 198156359001)
- PSREF ([страница](https://psref.lenovo.com/Detail/ThinkBook/ThinkBook_16_G8_IAL?M=21SK007KGE), [PDF](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=21SK007KGE&country_code=)): Core Ultra 7 255H (6P+8E+2LPE / 16T, до 5,1 ГГц), **Intel Arc 140T**; 2×16 SO-DIMM DDR5-5600. Остальное (SSD и слоты, экран, 45 Втч, 65 Вт в комплекте, порты, 1,7 кг, гарантия) — как у 21SK0083GE.
- Icecat: «2 x 16 GB», «AC-Netzadapter: Ja» ([Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Lenovo&ProductCode=21SK007KGE)). NBC (сделка 24.03.2026): «2x 16 GB, DDR5-5600, zwei Slots… Dual-Channel» ([NBC](https://www.notebookcheck.com/Lenovo-ThinkBook-16-mit-Core-Ultra-7-32-GB-RAM-1-TB-SSD-im-Angebot.1257770.0.html)).
- CPU: Arrow Lake-H — современный. Arc 140T работает, потому что память в двухканале.
- Цена ([billiger](https://www.billiger.de/products/5228830251-lenovo-thinkbook-16-g8-ial-21sk007kge)):
  - предложения: **1349,00 €** Easynotebooks, в наличии ([easynotebooks.de](https://www.easynotebooks.de/Notebooks/Lenovo/ThinkPad/ThinkBook/1092309/Lenovo-ThinkBook-16-G8-16-WUXGA-Core-Ultra-7-255H-32GB-RAM-1TB-SSD-Win11-Pro)); Amazon MP Tec & More 1383,88 (1 шт.); Heinzsoft 1507,90; Galaxus 1548; всего 8 предложений.
  - история: минимум 1049,01 € (27–29.08 и 31.08); 18.09 — 1095 €; 25–28.09 — 1380,39 €.
  - На Alternate по MTM не найден.
- Подтверждено (из `sweep-deals-watch.md`): минимум 1049,01 €, 76 дней ≤ 1100 €. В таблице `candidates-lenovo-hp-dell.md` стоит «(1078,83 €)» — это граница полосы, а не минимум.

#### ThinkBook 16 G7 IML — 21MS004SGE (EAN 197531872753)
- PSREF ([страница](https://psref.lenovo.com/Detail/ThinkBook/ThinkBook_16_G7_IML?M=21MS004SGE), [PDF](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=21MS004SGE&country_code=)):
  - Core Ultra 5 125U (Meteor Lake-U), Intel Graphics; 2×16 SO-DIMM DDR5-5600; 1 ТБ 2242 в одном из двух слотов M.2 2280.
  - WUXGA 300 нит 45 % NTSC; 45 Втч; **65 Вт в комплекте**; 1,7 кг; порты как у G8. Гарантия 1 год; анонс 18.02.2024.
- Icecat: «2 x 16 GB» ([Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Lenovo&ProductCode=21MS004SGE)).
- Цена ([billiger](https://www.billiger.de/pricelist/4952539795-lenovo-thinkbook-16-g7-iml-intel-core-ultra-5-125u-32-gb-ram-1-tb-ssd-win11-pro-arctic-grey-21ms004sge)):
  - единственный продавец — Amazon Marketplace **TechPoint1111**: 1241,58 € + 4 € доставка, «Nur noch 1 auf Lager». Заголовок предложения французский («Ordinateur Portable… 32 Go»): раскладку и происхождение уточнять у продавца.
  - история «пилой»: цена падает примерно на 1 % в день, потом скачет вверх (роботы-переоценщики маркетплейса). Минимум 775,65 € (03–04.06); с 16 по 18.09 данных нет.
- Опровергнуто: «минимум 894,98 €» (`sweep-lenovo.md`, `candidates-lenovo-hp-dell.md`) — это граница полосы. Реальный минимум 775,65 €, но на такие «минимумы» маркетплейса полагаться нельзя.
- Вывод: тот же корпус и порты, что у 21SK0083GE, CPU чуть слабее, продаёт только маркетплейс → **не держать в топ-10**.

#### ThinkBook 16 G7 IML — 21MS0054GE (EAN 197531874030)
- PSREF ([страница](https://psref.lenovo.com/Detail/ThinkBook/ThinkBook_16_G7_IML?M=21MS0054GE), [PDF](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=21MS0054GE&country_code=)): Core Ultra 7 155H (6P+8E+2LPE / 22T), Intel Arc; 2×16 SO-DIMM DDR5-5600; 1 ТБ 2242 + свободный слот 2280; **батарея 71 Втч**; **БП 100 Вт USB-C Slim в комплекте**; экран, порты и вес — как у 21MS004SGE.
- Подтверждено: «71 Втч (Icecat, не сверено с PSREF)» из `sweep-deals-watch.md` — PSREF подтверждает. Icecat: «2 x 16 GB», 100 Вт.
- Цена ([billiger](https://www.billiger.de/products/4934173452-lenovo-thinkbook-16-g7-iml-intel-core-ultra-7-155h-32-gb-ram-1-tb-ssd-win11-pro-arctic-grey-21ms0054ge)): только Amazon MP **REBERION GMBH** — 1299,00 € (14 шт.). Минимум 1092,49 € (02–03.04); ≤ 1150 € было 14 дней в апреле; дальше 1185–1380 €.
- Опровергнуто: «6-мес. мин. 1233,31 €» (таблица в `candidates-lenovo-hp-dell.md`) — это граница полосы; реальный минимум 1092,49 € (в `sweep-deals-watch.md` верно).
- Вывод: мощнее G8 225U, лучшая батарея, но продаёт только маркетплейс, и к 1100 € не приближался с апреля → **не держать**.

#### ThinkBook 16 G9 IPL — 21UR005AGE (EAN 199274233518)
- PSREF ([страница](https://psref.lenovo.com/Detail/ThinkBook/ThinkBook_16_G9_IPL?M=21UR005AGE), [PDF](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=21UR005AGE&country_code=)):
  - CPU и память: Core Ultra 5 325 (4P+4LPE / 8T, до 4,5 ГГц), Intel Graphics; 2×16 SO-DIMM DDR5-5600.
  - SSD: 1 ТБ M.2 2242; слоты «One M.2 2242 + One M.2 2280» — второй (2280) свободен.
  - Экран: WUXGA IPS **400 нит**, 45 % NTSC, 60 Гц.
  - Питание и вес: 48 Втч, **65 Вт в комплекте**, 1,7 кг.
  - Порты: **2× TB4** (DP 2.1), HDMI 2.1, SD, RJ45, 2× USB-A.
  - Прочее: Wi-Fi 7, дискретный TPM, гарантия 1 год, анонс 23.01.2026.
- Icecat: «2 x 16 GB», «AC-Netzadapter: Ja». Alternate: «2 Speicherbänke, davon belegt 2» (здесь совпадает) ([Alternate](https://www.alternate.de/Lenovo/ThinkBook-16-G9-21UR005AGE-Notebook/html/product/100190023)).
- CPU: Panther Lake, iGPU «Intel Graphics 4 Xe3», PL1 25 Вт ([NBC CPU](https://www.notebookcheck.net/Intel-Core-Ultra-5-325-Processor-Benchmarks-and-Specs.1196417.0.html)). Медиадвижок новейший (добавлен декод VVC), но по мощности младший. NBC: ThinkBook 14 G8 (255H) на **32 % быстрее по CPU и на 55 % по GPU**, чем ThinkBook 14 G9 (325) ([NBC](https://www.notebookcheck.net/Why-2026-laptops-like-this-Lenovo-ThinkBook-face-an-uphill-battle.1337031.0.html)).
- **Новое: SSD, вероятно, QLC.** В описаниях Amazon и Heinzsoft на billiger — «1x1TB SSD M.2 2242 PCIe Gen4 QLC». В PSREF тип памяти не указан → не проверено. У сестры 14 G9 NBC нашёл YMTC PC42Q, «одну из медленных» и с троттлингом. → проверено в браузере 30.09.2026: (п. 4.18) 21UR005AGE: SSD Micron 1 ТБ 2242 (FRU 5SS1T10167); тип флеш-памяти PSREF не указывает, модель по FRU не нашлась — QLC правдоподобно, не подтверждено ([pcsupport.lenovo.com](https://pcsupport.lenovo.com/de/de/products/laptops-and-netbooks/thinkbook-series/thinkbook-16-g9-ipl/21ur/21ur005age/parts/display/model)).
- Цена ([billiger](https://www.billiger.de/products/5542697625-lenovo-thinkbook-16-g9-intel-core-ultra-5-325-32-gb-ram-1-tb-ssd-win11-pro-21ur005age)):
  - предложения: **1205,00 €** c-nw (1–3 рабочих дня; в заголовке «30€ Gutschein» — условия не проверены; c-nw ориентирован на B2B, продаёт ли частным лицам — не проверено); Heinzsoft 1209,91; lapstars 1215; Notebookstore 1219,90; Alternate 1308 € + 7,99 €, «Sofort verfügbar»; всего 24 предложения.
  - история: 1205 € — минимум за 6 месяцев (29–30.09), максимум 1394 €; ≤ 1150 € не было ни разу.
- Подтверждено: `sweep-deals-watch.md` (диапазон 1205–1394). «6 мес.: 1220–1280 €» в `candidates-lenovo-hp-dell.md` — это полоса «нормальной цены», а не диапазон.

### Известные проблемы (Notebookcheck; G8 внешне идентичен G7 — по словам NBC)
- **ThinkBook 16 G7 IML** (тест 21MS0067US: 125U, 16 ГБ в одноканале — не наша конфигурация), 83 %, [NBC](https://www.notebookcheck.net/Lenovo-ThinkBook-16-G7-IML-laptop-review-Affordable-yet-professional.933265.0.html):
  - экран LEN160WUXGA: 61,2 % sRGB, 335 нит, 868:1, ΔE 9,2 до калибровки, PWM нет;
  - SSD SK hynix троттлит под нагрузкой;
  - мягкие клавиатура и тачпад, пластиковое дно;
  - Prime95: 100 °C ~30 с, дальше 30 Вт и 80 °C; шум ~32,6 дБ(A). NBC: «155H may run even warmer or louder or risk throttling more heavily».
- **ThinkBook 14 G8 IAL** (сестра, 255H), 84 %, [NBC](https://www.notebookcheck.net/This-affordable-Lenovo-laptop-is-more-upgradeable-than-most-ThinkPads-ThinkBook-14-Gen-8-IAL-review.1031134.0.html):
  - люфт шарнира;
  - экран 60,3 % sRGB, 290 нит;
  - маленькая батарея 45 Втч;
  - троттлинга и писка дросселей нет; шум до 43,9 дБ(A);
  - 2× SO-DIMM, 2× M.2, Wi-Fi на разъёме.
- **ThinkBook 14 G9 IPL** (сестра, 325), 84 %, [NBC](https://www.notebookcheck.net/32-GB-DDR5-RAM-and-affordable-Lenovo-ThinkBook-14-G9-IPL-laptop-review.1327762.0.html):
  - экран ниже среднего: 59 % sRGB, 386 нит, PWM нет;
  - под нагрузкой громко, до 49,7 дБ(A);
  - SSD YMTC медленный и троттлит; CPU за час стресса не троттлит.
- Обзора Notebookcheck именно ThinkBook 16 G8 IAL или 16 G9 IPL не нашёл. testbericht.de (Cloudflare) и laptopmedia (403) из облака не открылись. → проверено в браузере 30.09.2026: (п. 5.21) Обзоров ThinkBook 16 G8 / G9 нет: testbericht.de — «Noch keine Testberichte», у LaptopMedia и NBC — только характеристики ([testbericht.de](https://www.testbericht.de/serien/notebook/641608-lenovo-thinkbook-16-g8-2025)).
- Форум Lenovo: тема «ThinkBook 16 G7 IML Screen flashing» ([ссылка](https://forums.lenovo.com/t5/ThinkBook-Laptops/ThinkBook-16-G7-IML-Screen-flashing/m-p/5339632)) — содержимое из облака не читается, **не проверено**.

### HEVC
- В PDF PSREF всех пяти MTM нет упоминания HEVC/H.265 (grep по тексту).
- Lenovo нет в списках отключивших HEVC: HP, Dell ([smith6612, обн. 2026](https://smith6612.me/2026/04/19/its-me-i-started-the-hevc-disablement-press-storm/)); подробности — в `hevc-audit.md`.
- Риск: G7 и G8 — **низкий** (не подтверждено). G9 — **средний**: платформа вышла в 2026 г., уже после повышения отчислений Access Advance, и на HEVC её никто не тестировал. → проверено в браузере 30.09.2026: (п. 5.4) У devinthreethousand доказательств про Lenovo нет (все примеры — Dell и HP); по ThinkBook, IdeaPad, ThinkPad с iGPU сообщений нет. Прецеденты Lenovo — только NVIDIA: 2021 (H.264, Германия), 2024 (BIOS Legion, HEVC) ([devinthreethousand.substack.com](https://devinthreethousand.substack.com/p/hevc-hardware-support-being-removed)).
- В любом случае — DXVA Checker (HEVC_VLD_Main10 / Main422_10) в окно возврата.

### Итог для топ-10
- **21SK007KGE** — лучший пакет для 4K (255H + Arc 140T, 2×16, 2× M.2, TB4, SD, RJ45). Сейчас 1349 € → алерт ≤ 1100 €.
- **21SK0083GE** — 1122 €, всего на 22 € выше потолка; почти всё полугодие стоил < 1100 €. CPU — Meteor Lake-U refresh (4 Xe, не Arc): для 4K слабее, чем 255H.
- **21UR005AGE** — Panther Lake, 400 нит, 2× TB4, но медленнее 255H, SSD, вероятно, QLC, и 1205 € — минимум за полгода. Низкий приоритет.
- 21MS004SGE и 21MS0054GE — только маркетплейс Amazon, модели 2024 г. → из топ-10 убрать.
