# Бренды ноутбуков: запчасти, проблемность, ремонт в Германии

_Обновлено 2026-09-30. Каждый факт — со ссылкой. «не проверено» — первоисточник не найден._
_Сбор из облака: сайты HP DE, ASUS, MSI, Acer, XMG частично закрыты (403/503/проверка от ботов). Лимит веб-поиска в сессии исчерпан, дальше работал только по прямым ссылкам._

## Итог

**Рейтинг линеек под задачу** (запчасти надолго, мало проблем, ремонт; Intel, 2×16 ГБ, 15–16", потолок 1100 €).

По MEMORY.md ноутбук нужен другому человеку под Windows, поэтому поддержка Linux и LVFS — второстепенный плюс.

1. **Lenovo ThinkPad E16 / L16** (и ThinkBook 16 G8 как более дешёвый вариант) — версии с 2× SO-DIMM, не Lunar Lake и не Wildcat Lake.
   Почему: лучшая экосистема запчастей (FRU-номера, HMM, официальный дистрибьютор в DE), iFixit 9/10, французский индекс 8,1–8,6.
   Минус: базовая гарантия часто 1 год — докупить 3 года (~100–110 €).
2. **Dell Pro 16** (преемник Latitude): 2× SO-DIMM, франц. индекс 9,2. Места 2 и 3 почти равны.
   Минусы: у бренда худшая надёжность у Consumer Reports (прежде всего из-за потребительских линеек); в опросе Notebookcheck сервис Dell откатился в конец середины.
3. **HP ProBook 4 G1i 16 / EliteBook 6 G1i 16**: 2× SO-DIMM ([datasheet Elite 6](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09121787)), открытые сервис-мануалы, индекс 8,3–8,5, запчасти «до 5 лет».
   Минусы: с осени 2025 HP продаёт запчасти наборами («Kitted Parts») — дороже; новый EliteBook 8 G2a 16 уже с распаянной памятью.
4. **ASUS ExpertBook** (P3/P5): 2× SO-DIMM, у PM3 3 года гарантии и 5 лет обновлений BIOS, индекс 9,5–9,7 (его выставляет сам производитель).
   Минусы: ремонт долгий (~40 % случаев дольше 14 дней), скандал с RMA в 2024 (США).
5. **Tuxedo, XMG/Schenker** (шасси Clevo/Tongfang): лучший сервис в DE (XMG — 1-е место у Notebookcheck), 2× RAM + 2× SSD, ремонт в Германии, гарантия до 5 лет (Tuxedo).
   Минусы: срок выпуска запчастей нигде не обещан; Intel-модели 15–16" обычно дороже 1100 € (XMG Evo 15 — от 1329 €).
6. **Игровые с 2× SO-DIMM** (Legion 5/LOQ, Nitro V, MSI Cyborg/Katana/Venture, Medion Erazer; Victus — не проверено) — только если нужна дискретка ≥ 8 ГБ (скорее вне бюджета, см. `market.md`).
   Минусы: тестовые экземпляры часто идут с одной планкой; у MSI предпоследнее место по надёжности у CR.

**Распаянная ОЗУ** (пользователь допускает её при хорошей цене, но для ремонтопригодности это минус): IdeaPad Pro 5, HP OmniBook 5 (индекс 6,1), Dell 16 Plus/16S и XPS 2026, ASUS Zenbook, Acer Swift, Samsung Galaxy Book, LG gram, Surface.
- Yoga и Vivobook S обычно тоже с распайкой — в этой сессии не проверено.
- Из таких брать только ThinkPad/Dell Pro/HP-бизнес на Lunar Lake, и только если они заметно дешевле.
- Samsung не брать в любом случае: последнее место по сервису в опросе Notebookcheck.
- Framework ремонтопригоден лучше всех, но 16" — только AMD, а Intel есть только в 13" → вне критериев.
- Fujitsu для частника в DE практически нет (статус не проверен).

**Ключевой вывод по запчастям.** Больше ~5 лет после конца производства не обещает никто:
- Lenovo ECO: 5 лет (и ThinkPad, и IdeaPad);
- HP: «до 5 лет»;
- Dell (Франция): минимум 5 лет на ключевые детали.

Реально запчасти дольше и проще всего найти для ThinkPad, затем для Dell Latitude/Pro и HP Elite/ProBook. По ASUS, Acer, MSI и Clevo-брендам публичных обязательств нет.

## Сводная таблица

Индекс FR — французский индекс ремонтопригодности, модели 2025–26 (LDLC).

| Линейка | ОЗУ 15–16" | Индекс FR | Гарантия DE |
|---|---|---|---|
| ThinkPad E16/L16 | 2× (кроме Lunar/Wildcat Lake) | 8,1–8,6 | 1–3 г. по MTM |
| ThinkBook 16 G8 | 2× SO-DIMM | нет данных | 1–2 г. |
| IdeaPad Pro 5 16 | распайка | — | 1–3 г. |
| Legion 5 / LOQ | 2× SO-DIMM | LOQ 6,7 | 1–3 г. |
| HP ProBook 4 / Elite 6 | 2× SO-DIMM | 8,3–8,5 | 1 г. (варианты по стране) |
| HP OmniBook 5 16 | распайка | 6,1 | не проверено |
| Dell Pro 16 | 2× SO-DIMM | 9,2 | DE не пров. (США 3 г.) |
| Dell 16 / 16 Plus | 2× / распайка | — | 1 г., курьер |
| ASUS ExpertBook P3/P5/B1 | 2× SO-DIMM (P5605) | 9,5–9,7 | 1–3 г. |
| ASUS Vivobook 16 | не проверено | 9,1–9,4 | 2 г.? (как TUF/Zenbook) |
| Acer Aspire Go / Nitro | 2× (Nitro V 16, Aspire Go 15) | 6,9–7,1 | 2 г. |
| MSI Cyborg / Venture | 2× SO-DIMM | 7,9–8,0 | 2 г. |
| Medion Erazer | 2× SO-DIMM | — | 2 г. |
| Tuxedo / XMG | 2× (не все) | Clevo 9,4–9,7* | 2 г., до 5 лет |

\* Индекс Clevo — по моделям под маркой Why! (Франция). Индексы ASUS и других брендов выставляет сам производитель.

## Сквозные данные

### Сроки выпуска запчастей (официально)
- **ECO-декларации ECMA-370**, поле «P7.9 Spare parts are available after end of production for: N years».
  - Lenovo ThinkPad T14s Gen 3 AMD: **5 лет запчасти + 5 лет сервис** — [PDF](https://static.lenovo.com/ww/docs/regulatory/eco-declaration/eco-thinkpad-t14s-gen-3-amd.pdf).
  - Lenovo IdeaPad 5 Pro 16IHU6 и IdeaPad 5 15ALC05: тоже 5 + 5 — [1](https://static.lenovo.com/ww/docs/regulatory/eco-declaration/2021/eco-ideapad-5-pro-16-ihu6.pdf), [2](https://static.lenovo.com/ww/docs/regulatory/eco-declaration/2021/eco-ideapad-5-15-alc05.pdf).
  - Это модели 2021–22 годов; для 2025–26 не проверено.
- **HP QuickSpecs** (ProBook 4 G1i 16, v11 от 23.04.2026): «Spare parts are available throughout the warranty period and or for **up to 5 years** after the end of production» — [QuickSpecs](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09102587). «Up to» — это «до», а не «минимум».
- **Dell Франция (закон AGEC).** У ноутбуков без тачскрина плата, ОЗУ, вентиляторы, радиаторы, клавиатура, порты, SSD, экран, разъём питания и зарядка доступны **минимум 5 лет** после выпуска последней единицы модели на рынок Франции. Остальные запчасти — минимум 3 года от покупки — [Dell FR](https://www.dell.com/support/contents/fr-fr/article/warranty/regulatory-requirements). Для DE такого текста нет (не проверено).
- ASUS, Acer, MSI, Samsung, LG, Tuxedo, XMG — публичных цифр не нашёл (не проверено).
- Экометки: Blauer Engel для ПК требовал запчасти «mindestens fünf Jahre», но производители ноутбуков под него почти не сертифицировались — [WinFuture, 2012](https://winfuture.de/news,68372.html). Требование TCO Certified gen 10 к запчастям — не проверено (сайт TCO закрыт проверкой от ботов).

### Независимый дистрибьютор запчастей в DE: IPC-Computer
- Серия «Notebook-Hersteller-Check» — [обзор](https://blog.ipc-computer.de/notebook-hersteller-check/). Большинство оценок 2016–17 гг.; свежие только HP (11/2025) и Acer (07/2026).
- HP: у дешёвых потребительских моделей часть запчастей получает статус EOL «вскоре после конца гарантии», у бизнес-линеек лучше. С осени 2025 — «Kitted Parts» (наборы; дороже, больше отходов) — [IPC HP](https://blog.ipc-computer.de/2025/10/hp-service/).
- Acer (07/2026): оценка 1,8, поставка ~8 дней, 93 % заказов приходят за 30 дней. Обещанный срок поставки выполняется лишь в ~1/3 случаев. Типичные дефекты — петли и крышка экрана у Spin/Swift — [IPC Acer](https://blog.ipc-computer.de/2026/07/acer-service/).
- Старые оценки: Fujitsu 1,9 (2016), Lenovo 2,4 (2016), Clevo 2,4 (2017) — [обзор](https://blog.ipc-computer.de/notebook-hersteller-check/); ASUS 2,2 — [2016](https://blog.ipc-computer.de/2016/05/asus-service/); Dell 2,8 — [2017](https://blog.ipc-computer.de/2017/05/dell-service/).

### Надёжность: какие данные вообще есть
- **Consumer Reports** (США, обновлено 08.01.2026): 75 923 ноутбука 2019–2025 гг. 16 % за 3 года сломались или стали работать хуже. Таблица по брендам — за пейволлом — [CR](https://www.consumerreports.org/electronics-computers/laptops-chromebooks/most-reliable-laptop-brands-a1961456199/).
- **Пересказ CR + PCMag Readers' Choice 2025** (BGR, 13.01.2026), от лучших к худшим: Apple, LG, Microsoft, Samsung, Lenovo, MSI, ASUS, Acer, HP, Dell.
  - Dell — последний у CR; MSI — предпоследний у CR, но 3-й у PCMag; Samsung — 3-й у CR, последний у PCMag — [BGR](https://www.bgr.com/2072636/most-reliable-laptop-brands-ranked-worst-best/).
- **SquareTrade 2009** (отказы за 3 года): ASUS 15,6 %, Dell 18,3 %, Lenovo 21,5 %, Acer 23,3 %, HP 25,6 %. Устарело — [Wikibooks](https://de.wikibooks.org/wiki/Computerhardware:_Notebook:_Reparaturen:_Statistik).
- Статистики отказов по брендам именно для Германии за 2024–26 не нашёл. Индекс WERTGARANTIE последний раз выходил в 11/2021 — [Wertgarantie](https://www.wertgarantie.de/presse/indizes/notebook).

### Сервис в Германии: опрос Notebookcheck (2024, >500 участников, немецкоязычный сайт)
Источник — [NBC](https://www.notebookcheck.com/Umfrage-Service-und-Support-im-Reparaturfall-Diese-Laptop-und-Smartphone-Hersteller-koennen-nicht-ueberzeugen.905354.0.html).
- **1-е место — Schenker/XMG**: >90 % довольны телефонной поддержкой. Дальше Apple и Acer. Хуже год к году — Dell и Gigabyte. Последние места — Huawei и Samsung.
- **Samsung:** >60 % недовольных поддержкой, ~75 % называют процесс сложным.
- **ASUS:** ~40 % ремонтов дольше 14 дней.
- **Dell:** много повторных ремонтов; скатился с 3-го места в конец середины.
- **Lenovo:** большинство называет процесс простым.
- ~60 % владельцев Dell и Lenovo покупали продление гарантии; выезд на место: у Dell ~2/3, у Lenovo ~50 %.
- Опрос 2025/26 ещё идёт — [NBC](https://www.notebookcheck.com/Umfrage-zur-Servicezufriedenheit-bei-Laptops-und-Smartphones-2025-26.1199815.0.html).

### Французский индекс ремонтопригодности (карточки LDLC, 30.09.2026)
- **Lenovo:** ThinkPad E16 Gen 3 (AMD-версия) — [8,6](https://www.ldlc.com/fiche/PB00752717.html); E16 Gen 4 (Intel) — [8,3](https://www.ldlc.com/fiche/PB00755296.html); L16 Gen 2 (AMD) — [8,1](https://www.ldlc.com/fiche/PB00753818.html); IdeaPad Slim 3 16IPH11 — [7,3](https://www.ldlc.com/fiche/PB00746926.html); LOQ 15AHP10 — [6,7](https://www.ldlc.com/fiche/PB00691203.html); Legion Pro 7 16 — [8,6](https://www.ldlc.com/fiche/PB00741782.html); Yoga Slim 7 14 — [6,9](https://www.ldlc.com/fiche/PB00740736.html).
- **HP:** ProBook 4 G1i — [8,3](https://www.ldlc.com/fiche/PB00697397.html); ProBook 460 G11 — [8,4](https://www.ldlc.com/fiche/PB00717118.html); EliteBook 6 G2i 16 — [8,5](https://www.ldlc.com/fiche/PB00750152.html); EliteBook 8 G1a 16 — [8,7](https://www.ldlc.com/fiche/PB00744397.html); OmniBook 5 16 — [6,1](https://www.ldlc.com/fiche/PB00744082.html).
- **Dell:** Pro 16 PC16250 — [9,2](https://www.ldlc.com/fiche/PB00745126.html); Pro 16 PC16255 — [9,2](https://www.ldlc.com/fiche/PB00747346.html); Pro 16 Plus — [8,9](https://www.ldlc.com/fiche/PB00745247.html); Pro 15 Essential — [7,1](https://www.ldlc.com/fiche/PB00745194.html).
- **ASUS:** ExpertBook P3 16 — [9,7](https://www.ldlc.com/fiche/PB00750584.html); ExpertBook B1 15 — [9,5](https://www.ldlc.com/fiche/PB00726264.html); Vivobook 16 X1605VA — [9,4](https://www.ldlc.com/fiche/PB00715266.html); X1607CA — [9,1](https://www.ldlc.com/fiche/PB00729199.html); TUF F16 — [9,8](https://www.ldlc.com/fiche/PB00754907.html); ProArt P16 — [9,5](https://www.ldlc.com/fiche/PB00725227.html); ROG Strix G16 — [9,9](https://www.ldlc.com/fiche/PB00750601.html).
- **Acer:** Aspire Go 15 — [6,9](https://www.ldlc.com/fiche/PB00698153.html); Aspire Go 16 — [7,1](https://www.ldlc.com/fiche/PB00724970.html); Aspire 14 AI — [6,8](https://www.ldlc.com/fiche/PB00686783.html); Extensa 15 — [7,7](https://www.ldlc.com/fiche/PB00745811.html); Nitro 18 — [6,9](https://www.ldlc.com/fiche/PB00698651.html).
- **MSI:** Modern 15 — [7,9](https://www.ldlc.com/fiche/PB00750617.html); Modern 15 H AI — [8,0](https://www.ldlc.com/fiche/PB00715366.html); Cyborg 15 — [7,9](https://www.ldlc.com/fiche/PB00696744.html); Katana 15 HX — [8,0](https://www.ldlc.com/fiche/PB00747543.html).
- **Прочие:** Samsung Galaxy Book4 — [8,7](https://www.ldlc.com/fiche/PB00684317.html); Surface Laptop 7 15" — [6,4](https://www.ldlc.com/fiche/PB00616730.html); Surface Laptop 8 15" — [7,7](https://www.ldlc.com/fiche/PB00745822.html); Gigabyte Aero X16 — [6,6](https://www.ldlc.com/fiche/PB00684437.html).
- **Clevo** под маркой Why! (NS50AU, V540TU, L140PU): 9,4–9,7 — [indicereparabilite.fr](https://www.indicereparabilite.fr/appareils/ordinateur-portable/).
- **Важно.** Индекс рассчитывает сам производитель, прозрачности мало — [LaptopSpirit](https://www.laptopspirit.fr/328916/indice-de-reparabilite-pc-portable-pourquoi-il-faut-lignorer-pour-linstant.html). ASUS ставит 9+ даже моделям с распаянной памятью (ProArt P16), поэтому индекс полезен как ориентир, но не как доказательство.
- Средние по брендам на данных 2021 (PIRG): Dell 7,81, ASUS 7,61, Lenovo 6,99, Acer 6,87, HP 6,39, Microsoft 4,60 — [BDM](https://www.blogdumoderateur.com/indice-reparabilite-apple-google-microsoft-pires-scores/).

### iFixit (собственные оценки)
- ThinkPad: T14 Gen 7 / T16 Gen 5 (2026) — 10/10; E16 Gen 2/3, E14 Gen 6/7, L14 Gen 5/6, L16 Gen 2, T14 Gen 5/6, T16 Gen 3/4 — 9/10.
- Framework 16 и 12 — 10/10; Surface Laptop 7 — 8/10. Моделей HP, Dell, ASUS, Acer, MSI, Samsung, LG в таблице нет — [iFixit](https://www.ifixit.com/repairability/laptop-repairability-scores).

### Прошивки под Linux (LVFS/fwupd, 30.09.2026)
- Много файлов: Dell 9339 · Lenovo ThinkPad 4130 · HP 721.
- Среднее и мало: Framework 68 · Fujitsu FCCL 45 (новых нет) · Lenovo Legion 19 · Microsoft 15 · MSI 13 (+1) · ASUS 8 · Acer 3 (новых нет).
- TUXEDO — только тестовый аккаунт. Schenker/XMG, Samsung (как производитель ноутбуков), LG — нет — [LVFS](https://fwupd.org/lvfs/vendors/).

### Цены продления гарантии (пример: магазин lap4worx, 30.09.2026)
- Lenovo 3 года Premier Support (с 1 года): ~102–109 €; 5 лет Premier Support AIPC: ~137 € — [lap4worx](https://www.lap4worx.de/markenwelt/lenovo/garantieverlaengerung/).
- HP 3 года Premium Vor-Ort: ~61–94 €; 5 лет: ~164–185 € — [lap4worx](https://www.lap4worx.de/markenwelt/hp/garantieverlaengerung/).
- Dell 3 года ProSupport (с 1 года): ~132–138 € — [lap4worx](https://www.lap4worx.de/markenwelt/dell/garantieverlaengerung/).
- Цена зависит от модели; соответствие позиций и цен на странице сверял выборочно.

### Тренды 2026, важные для «2×16 ГБ»
- Всё больше распайки: HP EliteBook 8 G2a 16 (2026) — «unerwartet für einen Business-Laptop» — [NBC](https://www.notebookcheck.com/UEberraschend-schnell-mit-32-GB-RAM-und-Ryzen-7-HP-EliteBook-8-G2a-16-Laptop-Test.1404986.0.html).
- **LPCAMM2** (ThinkPad T14 Gen 7/T16 Gen 5, Framework 13 Pro) — один сменный модуль, но двухканальный: не «2 планки», хотя функционально задачу решает — [iFixit](https://www.ifixit.com/News/115827/new-thinkpads-score-perfect-10-repairability).
- **Подвох:** «8 ГБ распаяно + 1 слот» (Schenker Element 16 E26) — набрать 2×16 нельзя — [NBC](https://www.notebookcheck.com/Bis-zu-72-GB-RAM-und-leicht-zu-reparieren-Schenker-Element-16-E26-Laptop-im-Test.1395704.0.html).
- Тестовые Legion 5 15IAX11 и LOQ Essential 15 пришли с одной планкой (Single-Channel), хотя слотов два — [Legion](https://www.notebookcheck.com/Testbericht-zum-Lenovo-Legion-5-15IAX11-Optimiert-fuer-Gaming-mit-1440p.1382357.0.html), [LOQ](https://www.notebookcheck.com/Lenovo-LOQ-Essential-15-im-Test-RTX-Gaming-ohne-Schnickschnack.1379158.0.html). Проверять парт-номер.

## Бренды

### Lenovo — ThinkPad, ThinkBook, IdeaPad/Yoga, Legion/LOQ
**Запчасти.** ECO-декларации обещают 5 лет после конца производства — и ThinkPad, и IdeaPad (см. выше).
- FRU-поиск по серийнику: [support.lenovo.com/de/de/parts-lookup](https://support.lenovo.com/de/de/parts-lookup). Своего магазина для частников в DE не нашёл — не проверено.
- IPC-Computer — «Certified Authorised Reseller für Ersatzteile in Deutschland», 444 000 позиций Lenovo, >90 % на складе — [IPC](https://www.ipc-computer.de/lenovo/).
- iFixit EU: 236 позиций Lenovo, аккумуляторы ThinkPad около 55–74 € — [iFixit](https://www.ifixit.com/en-eu/Parts/Lenovo_Laptop).

**Документация.** PSREF по каждому MTM; Hardware Maintenance Manual с FRU есть и у IdeaPad (пример: [16IMH9](https://www.manualslib.com/manual/3601016/Lenovo-16imh9.html), копия).
- С 02/2024 Lenovo работает с iFixit; цель — к 2025 году 84 % ремонтов без отправки в сервис — [iFixit](https://www.ifixit.com/News/95395/ifixit-and-lenovo-work-together-to-make-laptop-repairability-the-standard-en).

**Гарантия** (базовая, варианты по PSREF; в DE — по конкретному MTM):
- E16 Gen 3 Intel: 1 год (mail-in / carry-in / onsite) — [PSREF](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_E16_Gen_3_Intel/ThinkPad_E16_Gen_3_Intel_Spec.PDF).
- L16 Gen 2 и T16 Gen 4: 1 или 3 года — [L16](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_L16_Gen_2_Intel/ThinkPad_L16_Gen_2_Intel_Spec.PDF), [T16](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_T16_Gen_4_Intel/ThinkPad_T16_Gen_4_Intel_Spec.PDF).
- ThinkBook 16 G8: 1 или 2 года — [PSREF](https://psref.lenovo.com/syspool/Sys/PDF/ThinkBook/ThinkBook_16_G8_IAL/ThinkBook_16_G8_IAL_Spec.PDF).
- IdeaPad Pro 5 16IAH10, Legion 5 15IAX10, LOQ 15IAX9: 1, 2 или 3 года carry-in — [IdeaPad](https://psref.lenovo.com/syspool/Sys/PDF/IdeaPad/IdeaPad_Pro_5_16IAH10/IdeaPad_Pro_5_16IAH10_Spec.PDF), [Legion](https://psref.lenovo.com/syspool/Sys/PDF/Legion/Legion_5_15IAX10/Legion_5_15IAX10_Spec.PDF), [LOQ](https://psref.lenovo.com/syspool/Sys/PDF/LOQ/LOQ_15IAX9/LOQ_15IAX9_Spec.PDF).
- Тестовые ThinkPad E14 G8, Legion 5 15IAX11 и LOQ Essential 15 у Notebookcheck — 12 месяцев — [E14 G8](https://www.notebookcheck.com/Lenovo-ThinkPad-E14-G8-im-Test-Leises-Business-Notebook-mit-langen-Akkulaufzeiten.1352243.0.html), [Legion](https://www.notebookcheck.com/Testbericht-zum-Lenovo-Legion-5-15IAX11-Optimiert-fuer-Gaming-mit-1440p.1382357.0.html), [LOQ](https://www.notebookcheck.com/Lenovo-LOQ-Essential-15-im-Test-RTX-Gaming-ohne-Schnickschnack.1379158.0.html).

**Конструкция 15–16"** (PSREF):
- E16 Gen 3 Intel: Arrow/Meteor/Raptor Lake — 2× DDR5 SO-DIMM и 2× M.2 (2242 + 2280); Lunar Lake — распайка.
- **E16 Gen 4 Intel (2026):** Panther Lake — 2× SO-DIMM; **Wildcat Lake — только 1 слот** и один M.2 2242. Ловушка! Базовая гарантия 1 год — [PSREF](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_E16_Gen_4_Intel/ThinkPad_E16_Gen_4_Intel_Spec.PDF).
- L16 Gen 3 Intel (2026): 2× SO-DIMM, 1× M.2 2280, гарантия 1 или 3 года — [PSREF](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_L16_Gen_3_Intel/ThinkPad_L16_Gen_3_Intel_Spec.PDF).
- T16 Gen 4 Intel: Arrow Lake — 2× SO-DIMM/CSODIMM. L16 Gen 2 — 2× SO-DIMM, 1× M.2.
- ThinkBook 16 G8, Legion 5 15IAX10, LOQ 15IAX9 — 2× SO-DIMM и 2× M.2.
- IdeaPad Pro 5 16IAH10 — распайка 16/24/32 ГБ.
- У ThinkPad T/E/L клавиатура — отдельная деталь, iFixit хвалит её замену. У IdeaPad/Legion — не проверено.

**Проблемность.** Середина рейтинга, 5-е место — [BGR](https://www.bgr.com/2072636/most-reliable-laptop-brands-ranked-worst-best/). В опросе NBC процесс ремонта «простой» — [NBC](https://www.notebookcheck.com/Umfrage-Service-und-Support-im-Reparaturfall-Diese-Laptop-und-Smartphone-Hersteller-koennen-nicht-ueberzeugen.905354.0.html).
- IdeaPad 5 (2020, Type 81YK): трещины петель; юрфирма в 08/2025 начала расследование — [classlawdc](https://classlawdc.com/2025/08/26/lenovo-ideapad-5-type-81yk-hinge-crack-investigation/).
- 03/2025: Windows блокировала утилиту обновления BIOS ThinkPad как «уязвимый драйвер»; обход — через Windows Update — [gHacks](https://www.ghacks.net/2025/03/28/windows-bug-blocks-bios-updates-for-lenovo-thinkpad-laptops/).

**Linux.** ThinkPad — 4130 файлов в LVFS; Legion — 19; IdeaPad и ThinkBook отдельно не значатся.

**Вердикт.** ThinkPad E16/L16 (Intel, не Lunar Lake и не Wildcat Lake) — №1. ThinkBook 16 — хороший запасной вариант. IdeaPad Pro/Yoga — мимо (распайка).

### HP — EliteBook, ProBook, OmniBook/Envy/Pavilion, Victus/Omen
**Запчасти.** Бизнес-линейки: «до 5 лет» после конца производства — [QuickSpecs](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09102587). По потребительским — EOL вскоре после гарантии, с осени 2025 «Kitted Parts» — [IPC](https://blog.ipc-computer.de/2025/10/hp-service/).
- Официальный магазин запчастей для DE: [HP Parts Store](https://parts.hp.com/hpparts/default.aspx?cc=DE&lang=DE).
- iFixit + HP (с 2023, расширено 01.05.2025): оригинальные запчасти и гайды только для EliteBook 840/845 G7–G9 и 840 Aero G8 + набор Revivekit для аккумулятора — [iFixit](https://www.ifixit.com/News/109015/ifixit-and-hp-expand-partnership).

**Документация.** Maintenance & Service Guide есть и для бизнес-, и для потребительских моделей: [ProBook 4 G1i 16](https://kaas.hpcloud.hp.com/pdf-public/pdf_12003181_en-US-1.pdf), [OmniBook 5 16](https://kaas.hpcloud.hp.com/pdf-public/pdf_10220266_en-US-1.pdf).

**Гарантия.**
- ProBook 4 G1i 16 и EliteBook 6 G1i 16: «1-year… options depending on country» — [QuickSpecs](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09102587), [datasheet](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09121787).
- EliteBook 8 G1a/G2a 16: 3 года (G1a — при покупке у HP в США; G2a — у тестового NBC) — [G1a](https://www.notebookcheck.net/HP-EliteBook-8-G1a-16-AI-laptop-review-Redesigned-inside-and-out.1103659.0.html), [G2a](https://www.notebookcheck.com/UEberraschend-schnell-mit-32-GB-RAM-und-Ryzen-7-HP-EliteBook-8-G2a-16-Laptop-Test.1404986.0.html).
- Care Pack для Pavilion/Victus/OmniBook в DE — [HP DE](https://www.hp.com/de-de/shop/product.aspx?id=u4820pe&opt=&sel=cpk).
- Базовую потребительскую гарантию в DE проверить не удалось (сайты HP отдают 503) — не проверено.

**Конструкция.**
- ProBook 4 G1i 16: 2× SO-DIMM и M.2 2280; аккумулятор меняет сервис («not replaceable by customer») — [QuickSpecs](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09102587).
- EliteBook 8 G1a 16: 2× SO-DIMM, один M.2, дно на 4 винтах.
- EliteBook 8 G2a 16 (2026) — распайка.
- На LDLC у EliteBook 6 G2i 16 (Core 5 320), ProBook 4 G1i и ProBook 460 G11 значится «1 модуль + 1 свободный слот», то есть два слота — [Elite 6](https://www.ldlc.com/fiche/PB00750152.html), [ProBook 4](https://www.ldlc.com/fiche/PB00697397.html), [460](https://www.ldlc.com/fiche/PB00717118.html).
- Но Core 5 320 — это Wildcat Lake, по `intel-cpu.md` у него один канал памяти. Двухканальность EliteBook 6 G2i с таким CPU — не проверено.
- OmniBook 5 16 — распайка, один M.2 — [NBC](https://www.notebookcheck.com/HP-Omnibook-5-16-Laptop-Test-Nur-das-Noetigste-zu-einem-guenstigen-Preis.1189652.0.html).

**Проблемность.** 9-е место из 10 в пересказе CR + PCMag — [BGR](https://www.bgr.com/2072636/most-reliable-laptop-brands-ranked-worst-best/).

**Linux.** 721 файл в LVFS.

**Вердикт.** ProBook 4 G1i 16 и EliteBook 6 G1i 16 — да, но проверять у каждой новой серии, не распаяна ли память. OmniBook/Pavilion — избегать.

### Dell — Dell Pro (ex-Latitude), Dell / Dell Plus (ex-Inspiron), XPS, Alienware
Переименование 2025: Inspiron → «Dell»/«Dell Plus», Latitude → «Dell Pro», Precision → «Dell Pro Max» — [PCWorld](https://www.pcworld.com/article/2567199/dell-drops-xps-inspiron-and-latitude-brands.html).
- В 2026 вернулся XPS 14/16 на Panther Lake (распайка, от 2199 $) — [TweakTown](https://www.tweaktown.com/news/109570/dells-new-xps-16-and-xps-14-laptops-announced-at-ces-2026-with-intel-panther-lake-cpus/index.html).
- В 2026 появились «Dell 16S», «Dell Pro 5 16» и т. п. — [NBC](https://www.notebookcheck.com/Dell-16S-DS16260-im-Test-Ein-besseres-Dell-16-Plus.1374074.0.html).

**Запчасти.** Франция: ключевые детали — минимум 5 лет (см. выше).
- В DE — подбор по Service Tag: [parts selector](https://www.dell.com/de-de/shop/partsbytype/dellpartsselector/).
- Программа CSR: деталь присылают, клиент меняет сам — [Dell](https://www.dell.com/support/kbdoc/en-us/000133412/customer-self-replaceable-parts).
- Официального партнёрства с iFixit не нашёл — не проверено.

**Документация.** Owner's/Service Manual на dell.com обычно есть и для потребительских линеек — для моделей 2025–26 не проверено.

**Гарантия в DE.**
- Dell 16 (DC16250) на dell.de: «Basic Hardware Service mit Abhol- und Reparaturservice», 2×8 ГБ, 1099,56 € — [dell.de](https://www.dell.com/de-de/shop/dell-laptops/dell-16-laptop/spd/dell-dc16250-laptop); срок 1 год — [notebookinfo](https://www.notebookinfo.de/produkt/dell-16-dc16250-bndc1625003sb-47615).
- Dell Pro 5 16: 3 года в США — [NBC](https://www.notebookcheck.com/Testbericht-zum-Dell-Pro-5-16-P516265-Traditionell-und-zuverlaessig.1352142.0.html).

**Конструкция.**
- Dell Pro 16 PC16250: 2 слота DDR5 SO-DIMM, до 96 ГБ — [speicher.de](https://www.speicher.de/arbeitsspeicher/dell/pro/16/pro-16-pc16250.html).
- Dell Pro 5 16 (2026): сменные SO-DIMM — [NBC](https://www.notebookcheck.com/Testbericht-zum-Dell-Pro-5-16-P516265-Traditionell-und-zuverlaessig.1352142.0.html).
- Dell 16 (DC16250): 2×8 ГБ DDR5 SO-DIMM в базовой конфигурации — [dell.de](https://www.dell.com/de-de/shop/dell-laptops/dell-16-laptop/spd/dell-dc16250-laptop).
- Dell Pro 16 Plus PB16250 на Lunar Lake (Core Ultra 7 268V): 1 модуль, 0 свободных слотов — фактически распайка — [LDLC](https://www.ldlc.com/fiche/PB00745247.html).
- Dell 16 Plus: распайка, один M.2 — [NBC](https://www.notebookcheck.net/Dell-16-Plus-laptop-review-A-wave-goodbye-to-the-Inspiron-series.1028836.0.html). Dell 16S (2026): распайка LPDDR5x — [NBC](https://www.notebookcheck.com/Dell-16S-DS16260-im-Test-Ein-besseres-Dell-16-Plus.1374074.0.html).

**Проблемность.** Последнее место у CR (проблемы у потребительских линеек, Latitude «rugged») — [BGR](https://www.bgr.com/2072636/most-reliable-laptop-brands-ranked-worst-best/). В опросе NBC — много повторных ремонтов.

**Linux.** Лидер LVFS: 9339 файлов.

**Вердикт.** Dell Pro 16 — да. Dell 16 — допустимо. Dell 16 Plus/16S и XPS — нет.

### ASUS — Vivobook, Zenbook, ProArt, TUF/ROG, ExpertBook
**Запчасти.** Официального срока и магазина запчастей для частников в DE не нашёл — не проверено. IPC (2016): оценка 2,2, «хорошее наличие» — устарело — [IPC](https://blog.ipc-computer.de/2016/05/asus-service/).

**Документация.** Публичных сервис-мануалов не нашёл — не проверено. Индекс FR высокий (9,1–9,9), но его выставляет сам ASUS.

**Гарантия.**
- ExpertBook PM3: 3 года и «5 Jahre Software- sowie BIOS-Updates» — [NBC](https://www.notebookcheck.com/Test-Asus-ExpertBook-PM3-Office-Laptop-mit-AMD-langer-Akkulaufzeit-Copilot.1196995.0.html).
- ExpertBook P5605CAA: 12 месяцев у тестового — [NBC](https://www.notebookcheck.com/Intel-Core-Ultra-vs-AMD-Ryzen-im-Asus-ExpertBook-P5605CAA.1388825.0.html).
- TUF A16 и Zenbook S16: 24 месяца — [TUF](https://www.notebookcheck.com/Sind-2-200-Euro-fuer-Zen-4-RTX-5070-gerechtfertigt-Asus-TUF-Gaming-A16-Laptop-im-Test.1109786.0.html), [Zenbook](https://www.notebookcheck.com/Der-perfekte-Alltagsrechner-mit-AMD-Ryzen-400-Asus-Zenbook-S16-OLED-Laptop-im-Test.1211553.0.html).

**Сервис и скандалы.**
- 05/2024: Gamers Nexus показал, как ASUS навязывал платный ремонт по «customer damage» (ROG Ally). Критика была и годом раньше (2023). ASUS признал «пробелы» для США и Канады и обещал реформу с 16.05.2024 — [computerbase](https://www.computerbase.de/news/wirtschaft/asus-hat-uns-betrogen-umgang-mit-garantiefaellen-steht-erneut-in-der-kritik.88091/), [hardwareluxx](https://www.hardwareluxx.de/index.php/news/allgemein/wirtschaft/63568-kritik-an-rma-prozess-asus-soll-nicht-notwendige-reparaturen-in-rechnung-stellen.html).
- Касается ли это DE — «nicht ganz klar» (hardwareluxx).
- В опросе NBC ~40 % ремонтов ASUS длились дольше 14 дней.

**Конструкция.**
- ExpertBook P5605CAA: 2× SODIMM.
- TUF A16 (2025): теперь 2× RAM + 2× SSD, раньше была распайка — [NBC](https://www.notebookcheck.com/Sind-2-200-Euro-fuer-Zen-4-RTX-5070-gerechtfertigt-Asus-TUF-Gaming-A16-Laptop-im-Test.1109786.0.html).
- Zenbook S16: распайка — [NBC](https://www.notebookcheck.com/Der-perfekte-Alltagsrechner-mit-AMD-Ryzen-400-Asus-Zenbook-S16-OLED-Laptop-im-Test.1211553.0.html).

**Надёжность.** Нижняя половина рейтинга — [BGR](https://www.bgr.com/2072636/most-reliable-laptop-brands-ranked-worst-best/). **Linux:** 8 файлов в LVFS.

**Вердикт.** ExpertBook P3/P5 — допустимо (условия гарантии и обновлений хорошие, сервис медленный). Потребительские ASUS — только после проверки SKU на 2× SO-DIMM.

### Acer — Aspire, Swift, Nitro/Predator, TravelMate
- **Запчасти:** через IPC ~8 дней, обещанные сроки ненадёжны; петли у Spin/Swift — [IPC](https://blog.ipc-computer.de/2026/07/acer-service/). Официального срока нет — не проверено.
- **Документация:** «Offizielle Wartungsanleitungen sind seitens Acer jedoch nicht aufzufinden» — [NBC Aspire Go 15](https://www.notebookcheck.com/Guenstiger-Laptop-mit-guter-Leistung-Acer-Aspire-Go-15-im-Test.1092155.0.html).
- **Гарантия:** 24 месяца в Германии (Nitro V 16 AI) — [NBC](https://www.notebookcheck.com/Preiswerter-Gaming-Laptop-mit-super-Laufzeit-Acer-Nitro-V-16-AI-im-Test.1146412.0.html); TravelMate P6 — 36 месяцев — [NBC](https://www.notebookcheck.com/Ein-Kilo-Technik-die-begeistert-Acer-TravelMate-P6-Business-Laptop-im-Test.1064220.0.html).
- **Сервис:** 3-е место у NBC (2024).
- **Конструкция:** Nitro V 16 AI — 2× SO-DIMM, 2× M.2. Swift 16 AI — распайка, «kaum Wartungsmöglichkeiten» — [NBC](https://www.notebookcheck.com/Kuehl-wie-kaum-ein-anderer-Acer-Swift-16-AI-im-Test.1286726.0.html).
- **Надёжность:** нижняя половина — [BGR](https://www.bgr.com/2072636/most-reliable-laptop-brands-ranked-worst-best/). **LVFS:** 3 файла.
- **Вердикт:** средне. Swift — нет; Nitro/Aspire — только с проверкой SKU.

### MSI
- **Гарантия:** 24 месяца (Cyborg 15) — [NBC](https://www.notebookcheck.com/Der-perfekte-Budget-Gaming-Laptop-fuer-2026-MSI-Cyborg-15-im-Test.1210162.0.html).
- **Конструкция:** Cyborg 15 — 2× SO-DIMM, 1× M.2; Venture 16 AI — 2× SODIMM, 1× M.2 — [NBC](https://www.notebookcheck.com/MSI-Venture-16-AI-A2HMTG-Laptop-Test-Basic-Budget-Business.1244796.0.html).
- **Запчасти и мануалы:** публичных нет — не проверено (сайт MSI отдаёт 403).
- **Безопасность:** 2023 — утечка приватных ключей Intel Boot Guard для 116 продуктов MSI (11–13-е поколение Intel); ключи зашиты в железо и не отзываются — [BleepingComputer](https://www.bleepingcomputer.com/news/security/intel-investigating-leak-of-intel-boot-guard-private-keys-after-msi-breach/).
- **Надёжность:** предпоследний у CR, 3-й у PCMag — [BGR](https://www.bgr.com/2072636/most-reliable-laptop-brands-ranked-worst-best/). **LVFS:** 13 (+1).
- **Вердикт:** запасной вариант для игровых конфигураций.

### Medion (принадлежит Lenovo)
- **Гарантия:** 2 года. На аккумуляторы гарантии нет («Für Batterien oder Akkus wird keine Garantie übernommen»). Пересылку оплачивает клиент, если в гарантийной карте не указано иное — [условия Medion](https://www.medion.com/de/shop/garantiebedingungen).
- **Запчасти:** собственный магазин [Medion Service Shop](https://www.medion.com/medionserviceshop/de/) и сервис-приложение — [Medion Service](https://www.medion.com/de/service/start/). Срок выпуска запчастей — не проверено.
- **Конструкция:** Erazer Deputy 15 P1 — 2× SO-DIMM и 2× M.2, 24 месяца. Но процессор Core 7 250H — это Raptor Lake-H Refresh, старое ядро под новым именем (см. `intel-cpu.md`) — [NBC](https://www.notebookcheck.com/Hat-ein-deutscher-Budget-Gaming-Laptop-Chancen-gegen-die-Big-Player-Medion-Erazer-Deputy-15-P1-im-Test.1227553.0.html).
- **Вердикт:** допустимо, но условия гарантии слабее, чем у Lenovo/Dell/HP.

### Fujitsu
- Сайт fujitsu.com/de перенаправляет на global.fujitsu (429); в LVFS у FCCL 45 файлов, новых нет — [LVFS](https://fwupd.org/lvfs/vendors/).
- IPC (2016): лучшие оценки за запчасти — [IPC](https://blog.ipc-computer.de/2016/09/fujitsu-service/).
- Продаются ли сейчас Lifebook 15–16" частникам в DE — не проверено. На практике в кандидаты не брать.

### Samsung
- **Сервис:** последнее место у NBC (2024), >60 % недовольных — [NBC](https://www.notebookcheck.com/Umfrage-Service-und-Support-im-Reparaturfall-Diese-Laptop-und-Smartphone-Hersteller-koennen-nicht-ueberzeugen.905354.0.html).
- **Конструкция:** Galaxy Book6 Pro — LPDDR5x распаяна, 2× M.2, 24 месяца — [NBC](https://www.notebookcheck.com/Samsung-Galaxy-Book6-Pro-Laptop-im-Test-Besser-als-das-neue-XPS-16.1263970.0.html).
- **Индекс FR:** Galaxy Book4 — 8,7.
- **Вердикт:** нет (распайка + сервис).

### LG
- **Надёжность:** 2-е место у CR, 1-е у PCMag (9,6) — [BGR](https://www.bgr.com/2072636/most-reliable-laptop-brands-ranked-worst-best/).
- **Конструкция:** gram 17 (2025, Lunar Lake) — память в корпусе процессора; аккумулятор, динамики и вентиляторы не на клею; 24 месяца — [NBC](https://www.notebookcheck.com/Neues-Modell-Originaldesign-LG-Gram-17-2025-Lunar-Lake-Laptop-im-Test.1142044.0.html).
- Бюджетный Gram Book 15U55T: 2× DDR5 SO-DIMM и 2× M.2, но в целом «viele Kompromisse» — [NBC](https://www.notebookcheck.com/LG-Gram-Book-15U55T-Laptop-im-Test-Viele-Kompromisse.1238163.0.html).
- **Запчасти и сервис в DE:** не проверено. **LVFS:** нет.
- **Вердикт:** gram — нет (распайка); Gram Book — слабоват.

### Microsoft Surface
- **Ремонтопригодность:** iFixit — 8/10 (Surface Laptop 7); индекс FR — 6,4 (SL7 15") и 7,7 (SL8 15").
- **Конструкция:** распайка, 12 месяцев (Surface Laptop 13,8 2026) — [NBC](https://www.notebookcheck.com/Der-Snapdragon-X2-Plus-ist-deutlich-schneller-Microsoft-Surface-Laptop-13-8-2026-im-Test.1338690.0.html).
- **Вердикт:** нет (распайка; потребительские модели на Snapdragon).

### Framework
- Laptop 16 — только AMD Ryzen AI 300 (опционально RTX 5070) — [frame.work](https://frame.work/de/en/laptop16).
- Laptop 13 Pro — Intel Core Ultra Series 3 + LPCAMM2, но 13" — [frame.work](https://frame.work/de/en/laptop13pro), [NBC](https://www.notebookcheck.com/Testbericht-zum-Framework-Laptop-13-Pro-Der-Koenig-der-Reparierbarkeit-ist-zurueck.1356597.0.html).
- **Гарантия:** 2 года в ЕС; при поломке Framework может прислать деталь для самостоятельного ремонта — [warranty](https://frame.work/de/en/warranty).
- Marketplace (запчасти) есть, срок выпуска запчастей — не проверено. **LVFS:** 68.
- **Вердикт:** эталон ремонтопригодности, но вне критериев (нет Intel 15–16").

### Tuxedo Computers (Аугсбург; шасси Clevo/Tongfang)
- **Гарантия:** 2 года, в конфигураторе можно продлить до 5 лет (Pick-Up & Return, кроме расходников). Ремонт и сервис — на собственной площадке в Аугсбурге — [Tuxedo](https://www.tuxedocomputers.com/de/warum-TUXEDO.tuxedo). Платный ремонт — 5–7 дней после получения — [AGB](https://www.tuxedocomputers.com/de/Unsere-AGB.tuxedo).
- **Запчасти:** продаются аккумуляторы и блоки питания для своих моделей — [Akkus](https://www.tuxedocomputers.com/de/Linux-Hardware/Zubehoer-USB-Co./Notebook-Akkus.tuxedo). Срок выпуска запчастей не обещан — не проверено.
- **Конструкция:** InfinityBook Pro 14 Gen10 — 2× RAM (до 128 ГБ) и 2× M.2 2280, 24 месяца — [NBC](https://www.notebookcheck.com/Tuxedo-InfinityBook-Pro-14-Gen10-AMD-im-Test-Linux-Ultrabook-mit-Zen-5-und-128-GB-RAM.1093913.0.html).
- **Linux:** родной, но в LVFS только тестовый аккаунт.
- **Вердикт:** хорошо для Linux и сервиса; надёжность запчастей зависит от ODM.

### Schenker / XMG (Лейпциг, bestware; шасси Clevo/Tongfang)
- **Сервис:** №1 у Notebookcheck (итоги 2024, пятый год подряд) — [NBC](https://www.notebookcheck.com/Umfrage-Service-und-Support-im-Reparaturfall-Diese-Laptop-und-Smartphone-Hersteller-koennen-nicht-ueberzeugen.905354.0.html).
- **Гарантия:** XMG Core 15 и Evo 15 — 24 месяца; Schenker Element 16 — 36; Connect 15 — 24. Условия на help.bestware.com закрыты проверкой Cloudflare — не проверено.
- **Запчасти:** в магазине bestware есть разделы с аккумуляторами и блоками питания ([bestware](https://bestware.com/de/)); срок выпуска — не проверено.
- **Конструкция:**
  - XMG Evo 15 M25 (Core Ultra 7 255H): 2× SO-DIMM, 2× SSD, от 1329 € — [NBC](https://www.notebookcheck.com/Test-XMG-Evo-15-M25-Laptop-Eine-gute-Windows-Alternative-zum-MacBook-Air-15.1206611.0.html).
  - XMG Core 15 M25: 2× SO-DIMM, 2× M.2 — [NBC](https://www.notebookcheck.com/Deutsche-Konkurrenz-fuer-das-Legion-5-XMG-Core-15-M25-Gaming-Laptop-im-Test.1113865.0.html).
  - Schenker Element 16 E26: 8 ГБ распаяно + 1 слот, все детали на винтах, от 1499 €.
  - Schenker Connect 15 E26: Lunar Lake (распайка), зато съёмный аккумулятор — [NBC](https://www.notebookcheck.com/Schenker-Connect-15-E26-im-Test-Business-Laptop-mit-Wechselakku-Smartcard-Wi-Fi-7-LTE.1291469.0.html).
- **Linux:** в LVFS нет.
- **Вердикт:** лучший сервис; модели с 2× SO-DIMM — хороший выбор, если уложатся в бюджет.
- **Clevo/Tongfang:** это ODM-платформы. Clevo-модели набирают 9,4–9,7 по индексу FR (Why!), IPC ставил Clevo 2,4 (2017). Текущее состояние поставок запчастей от ODM — не проверено.

## Что не удалось проверить
- Базовая гарантия HP и ASUS для потребителей в DE по первоисточнику (сайты закрыты).
- Официальные сроки запчастей у ASUS, Acer, MSI, Samsung, LG, Tuxedo, XMG, Framework.
- ECO-декларации Lenovo для моделей 2025–26 (проверены только 2021–22).
- Формулировка TCO gen 10 о запчастях; текущий статус Fujitsu в DE.
- Отдельные потребительские сервис-мануалы Dell/ASUS для конкретных моделей 2025–26.
