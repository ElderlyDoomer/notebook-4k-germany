# Какой ноутбук брать: Intel или AMD

_Обновлено 01.10.2026, 03:20 (ночная проверка: оплата наличными без счёта, обычные магазины, наличие по рынкам). Монтаж 4K под Windows, Германия. Итог должен быть не больше 1100 € вместе с докупкой, лимит жёсткий._
_Жёсткие критерии с 30.09: экран с полным sRGB (замер ≥ ~95 % или 100 % sRGB/DCI-P3 по даташиту) и **оплата только наличными**. Подходят покупка в магазине, самовывоз с оплатой на месте и Nachnahme. Правила — в [CLAUDE.md](CLAUDE.md)._
_Вводные владельца: кодек камеры и программа неизвестны навсегда; внешнего монитора нет; планку и SSD ставит сам; порты — бонус._
_Цены — idealo и сайты магазинов в Chrome, 01.10: 00:03–00:15 проверяли три судьи, а в ~00:28 я перепроверил idealo R1FY (6 предложений, минимум 999,00 €, Nachnahme ни у кого нет) и expert (999,99 €, «Reservieren und sofort abholen»). В 00:31–00:40 критик финала ещё раз прошёл в своей вкладке Chrome карточки idealo R1FY, R2R1 и Medion, сайты expert, Cyberport, Galaxus, MEDIMAX и computeruniverse. Цены и способы оплаты не изменились; у R2R1 наличными по-прежнему нельзя (подробности в «Как купить за наличные»). Разборы веток: [Intel/REPORT.md](Intel/REPORT.md), [AMD/REPORT.md](AMD/REPORT.md)._

**Интерактивная страница — 109 ноутбуков с фото, оценками, фильтрами, сравнением и чек-листом покупателя: [открыть онлайн](https://elderlydoomer.github.io/notebook-4k-germany/page/laptops.html)** (в папке проекта — `page/laptops.html`; пересобрать — `python3 page/build.py`).

## Итог (01.10, 03:20)

**Брать — по порядку, в зависимости от того, что подтвердит звонок в магазин.** Все три варианта проходят все жёсткие критерии: полный sRGB, наличные, ≤ 1100 €, 32 ГБ в двухканале, 1 ТБ (у №1 и №3 — SSD 1 ТБ ставится самому).

| # | Ноутбук · P/N | Итог наличными | Где | Чем хорош | Чем плох |
|---|---|---|---|---|---|
| 1 | **Medion SPRCHRGD 16 S1 OLED** · [`30040202`](https://www.idealo.de/preisvergleich/OffersOfProduct/207222210_-sprchrgd-16-s1-30040202-medion.html) (Intel Core Ultra 5 228V) | **946,99 €** = 797 € + SSD 149,99 € | один экземпляр в [expert Bad Salzungen](https://www.expert.de/shop/unsere-produkte/computer-zubehor/notebooks/laptops/17040041553-sprchrgd-16-s1-oled-16-zoll-wqxga-intel-core-ultra-5-228v-32-gb-512-gb-ssd-intel-arc-140v.html?branch_id=32354097), тел. 03695 69630 | 2,8K OLED 120 Гц (CHIP: 100 % sRGB), Arc 130V — графика в 4,3 раза сильнее Swift Air, **аппаратный HEVC 4:2:2** и AV1 | одна штука, цена может быть ошибкой (в других рынках 1079–1099 €); SSD менять вместо заводского; запчастей почти нет, на аккумулятор гарантии нет |
| 2 | **Acer Swift Air 16 OLED R1FY** · [`NX.DL5EG.002`](https://www.idealo.de/preisvergleich/OffersOfProduct/211778543_-swift-air-16-oled-16-wuxga-amd-ryzen-ai-5-32gb-1tb-ssd-silber-nx-dl5eg-002-acer.html) (AMD Ryzen AI 5 330) | **959,14–999,99 €**, докупать нечего | 102 рынка expert по всей Германии (таблица по городам ниже) | проще всего найти; OLED 100 % sRGB по замеру | 4 ядра и Radeon 820M — для 4K слабо, нужны прокси; нет HEVC 4:2:2 |
| 3 | **Lenovo IdeaPad Slim 5 15ARP10 OLED** · `83J3006GGE` (AMD Ryzen 7 7735HS) | **1058,99 €** = 899 € + SSD 159,99 € | MEDIMAX Meißen, Frankfurt/Oder, Kempen ([карточка](https://www.medimax.de/p/1505157/ideapad-slim-5-15arp10)); SSD — MediaMarkt | 15,1" 2,5K OLED 165 Гц (100 % DCI-P3 по PSREF), процессор в 1,67 раза сильнее Swift Air, второй слот M.2 | платформа 2022 года, нет HEVC 4:2:2 и AV1-кодирования, экран не измерен |

- **Без банковского счёта работает один способ оплаты:** купить в магазине или зарезервировать на сайте и заплатить на кассе. Предоплата со взносом наличными в банке — только условно (не всякая Sparkasse, 10 €, паспорт). Наложенного платежа и Barzahlen для ноутбуков больше нет (подробно — ниже).
- **Перед поездкой — звонок** (скрипт на немецком ниже): есть ли товар новым, верна ли цена, можно ли заплатить наличными («bar» в правилах expert и MEDIMAX не написано), можно ли отложить, какие условия обмена.
- **Карта ничего явно лучшего не даёт** — оформлять её ради этой покупки не нужно.
- Всё это есть на интерактивной странице: раздел «Как заплатить наличными», таблица рынков, скрипт звонка с кнопкой «Скопировать».

### Medion — что сделать при покупке

1. В магазине сверить на коробке: SPRCHRGD 16 S1 OLED, 30040202, 32 ГБ, Core Ultra 5 228V; новый, в упаковке. Сохранить чек — Gewährleistung 2 года.
2. SSD на 1 ТБ ставится **вместо** заводского 512 ГБ (слот M.2 один — [даташит](https://media.medion.com/prod/medion/de_DE/0833/0732/0659/30040202.pdf)): либо клонировать диск (нужен USB-корпус для M.2 NVMe), либо поставить новый SSD и установить Windows с флешки. Сначала — проверки ниже, потом вскрывать: после вскрытия обменять сложнее.
3. **DXVA Checker → Decoder Devices:** `HEVC_VLD_Main`, `HEVC_VLD_Main10` и профиль HEVC 4:2:2 10 бит. У Medion отключений HEVC не находили ([hevc-audit.md](Intel/notes/hevc-audit.md)), но проверить.
4. Диспетчер задач → GPU: «Intel Arc 130V» (в даташите и на expert.de ошибочно «Arc 140V» — у 228V по Intel именно 130V).
5. Аккумулятор: у heise заряд «застревал» на ~89 % ([heise](https://www.heise.de/tests/Viel-RAM-fuers-Geld-Mittelklassenotebook-Medion-Sprchrgd-16-S1-im-Test-11354704.html)) — посмотреть в утилите Medion, не включён ли режим бережной зарядки, и зарядить до 100 %.
6. Экран: режим sRGB, если есть; ШИМ на 20–30 % яркости (камера телефона в замедленной съёмке); в Resolve — управление цветом экрана.

## Ночная проверка 01.10: как заплатить наличными и где купить

_01.10.2026, 01:40–03:07. Банковского счёта у покупателя нет, город неизвестен. Подробности — в заметках [cash-channels.md](AMD/notes/cash-channels.md), [retail-cash-sweep.md](AMD/notes/retail-cash-sweep.md), [store-availability.md](AMD/notes/store-availability.md), [night-verify.md](AMD/notes/night-verify.md). Данные для страницы — `data/patch-2026-10-01-night.json`._
_В 02:58–03:01 я ещё раз прошёлся по всем 319 рынкам expert и по MEDIMAX через API, который вызывает сама страница товара (только чтение). Ничего не покупал, не резервировал, в аккаунты не входил, формы не отправлял._

**Коротко:**
- **Без счёта и без карты работает один путь:** купить в магазине или зарезервировать на сайте и заплатить на кассе. Это бесплатно, и паспорт не нужен ([§ 10 Abs. 6a GwG](https://www.gesetze-im-internet.de/gwg_2017/__10.html): проверка личности — только при наличных от 10 000 €).
- **Выбор меняется — на Medion SPRCHRGD 16 S1 OLED `30040202`.** В expert Bad Salzungen он стоит 797 €, SSD на 1 ТБ там же — 149,99 €. **Итого 946,99 € наличными.** Но в рынке 1 штука, и цена может оказаться ошибкой. Поэтому сначала звонок (скрипт ниже).
- **Если Medion не подтвердят — Swift Air R1FY.** Он есть в 102 рынках expert. Дешевле всего в Schmalkalden — 959,14 € (18 км от Bad Salzungen), так что в одной поездке можно посмотреть оба.
- **Карта покупателю не нужна.** Ни один вариант «по карте» не лучше Medion за наличные (раздел «Если появится карта»).

### Новый выбор — Medion SPRCHRGD 16 S1 OLED `30040202`, 946,99 € наличными в expert Bad Salzungen

**Где и почём.**
- Рынок: expert Bad Salzungen, Bahnhofstraße 23, 36433 Bad Salzungen, тел. 03695 69630. На сайте — «Reservieren und sofort abholen» ([карточка с этим рынком](https://www.expert.de/shop/unsere-produkte/computer-zubehor/notebooks/laptops/17040041553-sprchrgd-16-s1-oled-16-zoll-wqxga-intel-core-ultra-5-228v-32-gb-512-gb-ssd-intel-arc-140v.html?branch_id=32354097)).
- 797 € проверены четыре раза: в 01:54, 02:14, 02:44 (в том числе в Chrome) и 02:58 (API). Каждый раз: 1 шт., `itemOnDisplay = false`, то есть не выставочный.
- SSD на 1 ТБ в том же рынке, по 1 шт. (02:58):
  - [Verbatim Vi3000](https://www.expert.de/shop/unsere-produkte/computer-zubehor/speichermedien/interne-festplatten/17320020417-vi3000-pcie-nvme-m-2-ssd-1tb-interne-festplatte-49375.html?branch_id=32354097) — 149,99 €, итог **946,99 €**;
  - [Samsung 990 EVO Plus](https://www.expert.de/shop/unsere-produkte/computer-zubehor/speichermedien/interne-festplatten/17320146488-990-evo-plus-nvmetm-m-2-ssd-1-tb.html?branch_id=32354097) — 199,90 €, итог **996,90 €**.
- Оплата: резерв «unverbindlich», «Die Bezahlung erfolgt direkt in Ihrem expert Fachmarkt» ([FAQ expert](https://www.expert.de/nuernberg1/Footer/Service/Fragen-Antworten)). Слова «bar» там нет — та же оговорка, что была у R1FY.

**Проходит все жёсткие критерии:**

| Критерий | Medion `30040202` | Источник |
|---|---|---|
| Экран 15–16", полный sRGB | 16" 2,8K OLED 120 Гц. По даташиту этого P/N — «500nits und 100% DCI-P3». CHIP намерил 100 % sRGB, но на версии с Core Ultra 9 | [даташит Medion 30040202](https://media.medion.com/prod/medion/de_DE/0833/0732/0659/30040202.pdf), [CHIP](https://www.chip.de/test/Medion-SPRCHRGD-16-S1-OLED-im-Test_186892299.html) |
| 32 ГБ в двухканале | «32 GB LPDDR5x RAM» в корпусе процессора; у 228V «Max # of Memory Channels: 2», максимум 32 ГБ | [даташит](https://media.medion.com/prod/medion/de_DE/0833/0732/0659/30040202.pdf), [Intel ARK](https://www.intel.com/content/www/us/en/products/sku/240955/intel-core-ultra-5-processor-228v-8m-cache-up-to-4-50-ghz/specifications.html) |
| 1 ТБ (или 512 + SSD самому) | 512 ГБ PCIe4 и один слот M.2 2280: SSD на 1 ТБ ставится **вместо** заводского, Windows придётся переустановить или склонировать | [даташит](https://media.medion.com/prod/medion/de_DE/0833/0732/0659/30040202.pdf), [IPC](https://www.ipc-computer.de/medion/notebook/sprchrgd-serie/sprchrgd-16-s1-a16lnl-mp/) |
| Наличные, итог ≤ 1100 € | 946,99 € в одном рынке; блок питания USB-C в комплекте | см. выше; даташит: «externes Type-C Netzteil» |

**Чем лучше Swift Air R1FY:**
- **Графика в 4,3 раза сильнее:** у Arc 130V Time Spy 3 401, у Radeon 820M — 786 ([NBC Arc 130V](https://www.notebookcheck.net/Intel-Arc-Graphics-130V-Benchmarks-and-Specs.854992.0.html), [NBC 820M](https://www.notebookcheck.net/AMD-Radeon-820M-Benchmarks-and-Specs.1059782.0.html)). От графики зависят эффекты, цветокоррекция и шумодав.
- **HEVC 4:2:2 декодируется аппаратно** ([Intel media-driver](https://raw.githubusercontent.com/intel/media-driver/master/docs/media_features.md)). Ни один AMD так не умеет ([AMD AMF](https://github.com/GPUOpen-LibrariesAndSDKs/AMF/wiki/GPU%20and%20APU%20HW%20Features%20and%20Support)). Кодек камеры неизвестен навсегда, поэтому это важно.
- **Процессор быстрее на 27 %:** R23 Multi 9 932 против 7 840 ([NBC 228V](https://www.notebookcheck.net/Intel-Core-Ultra-5-228V-Processor-Benchmarks-and-Specs.893277.0.html), [NBC AI 5 330](https://www.notebookcheck.net/AMD-Ryzen-AI-5-330-Processor-Benchmarks-and-Specs.1049553.0.html)).
- **Экран лучше:** 2,8K, 120 Гц, около 400 кд/м² по CHIP. У R1FY — 1920×1200, 60 Гц, 297 кд/м².
- **Больше портов:** USB4, HDMI 2.0, microSD. Аккумулятор 80,5 Вт·ч ([даташит](https://media.medion.com/prod/medion/de_DE/0833/0732/0659/30040202.pdf)).
- **Дешевле на 12–53 €:** 946,99 € против 959,14–999,99 €.
- По шкале веток Средн. 6,5 против 5,5 у R1FY (Цена 7,5 при 946,99 €).

**Риски — поэтому сначала звонок:**
1. **Возможно, ошибка цены.** Другие рынки просят за Medion 1079–1099 €, это на 282 € дороже. Резерв есть ещё в 15 рынках, но 13 из них — не новый товар: 8 остатков («Restposten»), 4 выставочных («Aussteller») и 1 демонстрационный («Vorführgerät»). Новые есть только в Soltau и Geesthacht — по 1079 € (API, 02:59; проверка критика). Онлайн Medion стоит 999–1089 € ([idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/207222210_-sprchrgd-16-s1-30040202-medion.html)), с SSD это больше 1100 €.
2. **В рынке одна штука,** а город покупателя неизвестен. Bad Salzungen — запад Тюрингии: от Эрфурта около 59 км, от Касселя около 76 км (по прямой).
3. **Модель:** на аккумулятор гарантии нет ([Medion](https://www.medion.com/de/shop/garantiebedingungen)); у heise заряд застревал на ~89 % ([heise](https://www.heise.de/tests/Viel-RAM-fuers-Geld-Mittelklassenotebook-Medion-Sprchrgd-16-S1-im-Test-11354704.html)); запчастей почти нет.
4. **Название графики:** в даташите и на expert.de написано «Arc 140V», но у 228V по Intel — Arc 130V ([ARK](https://www.intel.com/content/www/us/en/products/sku/240955/intel-core-ultra-5-processor-228v-8m-cache-up-to-4-50-ghz/specifications.html)).
5. **Отказа нет:** при покупке в магазине законных 14 дней на отказ нет ([§ 312g BGB](https://www.gesetze-im-internet.de/bgb/__312g.html)). Можно ли обменять — спросить по телефону.

**Если звонок не подтвердит 797 € или товара не будет — брать Swift Air R1FY.** В самом Bad Salzungen он стоит 999 € (2 шт.), в Schmalkalden — 959,14 €.

### Запасные

1. **Acer Swift Air 16 OLED R1FY `NX.DL5EG.002` — бывший выбор.** Тоже проходит все критерии. Его проще всего найти: 102 рынка expert с новым товаром, в 96 из них — не дороже 999,99 € (подробнее в следующем разделе). Слабые места прежние: 4 ядра и 820M.
2. **Lenovo IdeaPad Slim 5 15ARP10 OLED `83J3006GGE` — новая находка.** Проходит все критерии в варианте «512 ГБ + SSD самому».
   - Цена: 899 € в MEDIMAX ([карточка](https://www.medimax.de/p/1505157/ideapad-slim-5-15arp10), «899.00» в 03:00) + SSD на 1 ТБ 159,99 € в MediaMarkt ([SN5100](https://www.mediamarkt.de/de/product/_sandisk-wd-bluer-sn5100-nvmetm-festplatte-1-tb-ssd-m2-via-nvme-intern-2999770.html)) = **1058,99 €**.
   - Где: резерв только в трёх рынках — Meißen, Frankfurt/Oder (Lenné-Passagen) и Kempen. Оплата — в рынке, «mit den dort akzeptierten Zahlungsmitteln», слова «bar» нет. Цена в рынке может отличаться от сайта ([AGB MEDIMAX](https://www.medimax.de/agb), п. 3 и 7).
   - По [PSREF](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=83J3006GGE&country_code=DE):
     - память — «32GB Soldered LPDDR5X-6400 … dual-channel»;
     - накопитель — «Two M.2 2280 slots», второй свободен;
     - экран — 15,1" 2,5K OLED, 100 % DCI-P3, 165 Гц; замера нет;
     - зарядка 65 Вт в комплекте.
   - Против R1FY: процессор быстрее в 1,67 раза, графика — в 2,9 раза.
   - Против Medion — слабее:
     - платформа Zen 3+ 2022 года, драйверы RDNA 2 только поддерживаются ([amd-cpu.md](AMD/notes/amd-cpu.md));
     - нет аппаратного 4:2:2 и кодирования AV1;
     - экран подтверждён только даташитом.
3. **Aspire R2R1 `NX.JP0EG.00Z` больше не запасной.**
   - Наличными его теперь можно купить в MEDIMAX Nettetal за 1099 € — в 1 € от потолка. Резерв там подтверждён в 02:38 и 03:01 ([night-verify.md](AMD/notes/night-verify.md)).
   - Но экран по даташиту Acer — «95 % DCI-P3». Теперь есть три варианта без такой уступки.

### Как заплатить наличными без счёта

| Способ | Работает? | Подробности |
|---|---|---|
| **Купить в магазине или зарезервировать онлайн и заплатить на кассе** | **да** | Наличные написаны прямо у [MediaMarkt](https://www.mediamarkt.de/de/service/zahlung/zahlungsmoeglichkeiten) и [Saturn](https://www.saturn.de/de/service/zahlung/zahlungsmoeglichkeiten) (кроме маркетплейса), [Euronics](https://www.euronics.de/hilfe-infos/online-bestellung/zahlungsarten), [Cyberport Stores](https://www.cyberport.de/service/zahlungsweisen-und-finanzierung/abholung-und-girocard.html) (до 9 999 €) и [Alternate Linden](https://www.alternate.de/HILFE/Zahlungsarten). Оплата в магазине без слова «bar» — у [expert](https://www.expert.de/nuernberg1/Footer/Service/Fragen-Antworten), в [магазинах NBB](https://service.notebooksbilliger.de/help/de-de/35-ladengeschafte-stores/133-hinweise-zur-abholung-bestellter-ware-im-ladengeschaft-store) и при резерве в [MEDIMAX](https://www.medimax.de/help) (при «Abholung nach Bestellung» в MEDIMAX — только онлайн). Сборов нет |
| Предоплата (Vorkasse) + взнос наличными в Sparkasse на счёт магазина | частично | Vorkasse есть у [computeruniverse](https://www.computeruniverse.net/de/page/zahlungs) и [Kaufland.de](https://www.kaufland.de/help/marketplace/bezahlart/). Взнос от не-клиента принимает не каждая Sparkasse: [Nordhorn](https://www.sparkasse-nordhorn.de/content/dam/myif/ksk-nordhorn/work/dokumente/pdf/preise-leistungen/preis-leistungsverzeichnis.pdf) берёт 10 €, Barnim не принимает. Postbank и Commerzbank не принимают. От 1000 € нужен паспорт ([§ 10 Abs. 3 GwG](https://www.gesetze-im-internet.de/gwg_2017/__10.html)). На время перевода товар не резервируется |
| Счёт Klarna, оплаченный взносом в банке | не проверено | Одобрит ли [Klarna](https://www.klarna.com/de/kundenservice/wie-kann-ich-meine-rechnung-bei-klarna-bezahlen/) покупателя без счёта — неизвестно. [OTTO](https://www.otto.de/shoppages/ottopayments_zahlungsbedingungen) прямо требует счёт в зоне SEPA |
| Наложенный платёж (Nachnahme) | нет | Крупные магазины его не предлагают, Alternate в 2026 тоже убрал ([Alternate](https://www.alternate.de/HILFE/Zahlungsarten)) |
| Barzahlen/viacash, PaysafeCash, paysafecard | нет | Магазины электроники их не принимают. [viacash](https://www.viacash.com/de/faq/) — это взнос на свой счёт и оплата коммунальных счетов; [paysafecard](https://www.paysafecard.com/de-de/gebuehren-limits/) — до 50 € на код |
| Пополнить баланс Amazon наличными (Amazon vor Ort aufladen) | бесполезно | 5–500 € за раз ([Amazon](https://www.amazon.de/b?ie=UTF8&node=13847038031)). Из наших кандидатов там только R2R1 за 1112,99 € — дороже 1100 € |
| eBay, оплата при самовывозе | нет | Только для недвижимости, машин и лодок ([eBay](https://www.ebay.de/help/selling/listings/choosing-get-paid/accepting-other-payment-methods?id=4184)) |

### Где сейчас есть Swift Air R1FY (API expert, 02:59)

- **Наличные за R1FY принимает только expert.** В MediaMarkt/Saturn, Euronics, NBB, MEDIMAX и Cyberport этой модели нет ([store-availability.md](AMD/notes/store-availability.md), [night-verify.md](AMD/notes/night-verify.md)).
- **Новое: 19 из 121 рынка с резервом продают выставочный образец** («Aussteller», без упаковки), а не новый товар. Значит, новый R1FY с резервом есть в **102 рынках**. Ещё в 4 рынках он лежит у соседа, 75 могут заказать (в ответе — «Preis und Lieferdatum anfragen»), у 119 — только онлайн-оплата.
- **Поправка:** Peine за 986,51 € — выставочный, поэтому второй по цене новый вариант — Bening за 989 €. Там цена 1029 € минус 40 € «Sofort-Rabatt»; действует ли скидка на кассе — не проверено.
- **Самый дешёвый новый — [expert Schmalkalden](https://www.expert.de/shop/unsere-produkte/computer-zubehor/notebooks/laptops/17041266033-swift-air-16-oled-silber-16-zoll-wuxga-amd-ryzen-ai-5-330-32-gb-1024-gb-ssd-amd-radeon-820m.html?branch_id=32354099):** 959,14 €, Haindorfsgasse 3, тел. 03683 4692811.

| Город | Ближайший рынок с новым R1FY и резервом (по прямой) | Цена |
|---|---|---|
| Берлин | ESC Rangsdorf, 25 км | 999 € |
| Гамбург | Bening Buxtehude, 20 км | 989 € |
| Мюнхен | TeVi Landshut, 63 км | 999,99 € |
| Кёльн / Düsseldorf / Wuppertal | Herfort Bergisch Gladbach, 13 / 36 / 30 км | 999 € |
| Франкфурт / Висбаден | klein Hofheim-Wallau, 23 / 10 км | 999 € |
| Штутгарт | Schlagenhauf Aalen, 65 км (Deizisau — выставочный) | 999 € |
| Дортмунд / Бохум / Эссен | Brumberg Kamen, 16 / 33 / 47 км | 999 € |
| Бремен | Bening Delmenhorst, 11 км | 989 € |
| Ганновер | Walsrode или Gifhorn, 55 км (Peine — выставочный) | 999 € |
| Дрезден / Лейпциг / Хемниц | ESC Bautzen 49 км; для Лейпцига — Rangsdorf, 130 км (Bischofswerda — выставочный) | 999 € |
| Нюрнберг | TeVi Nürnberg, 2 км | 999,99 € |
| Эрфурт | Schmalkalden, 50 км (и Bad Salzungen, 59 км — там же Medion) | 959,14 € |

Адреса, телефоны и ссылки с выбранным рынком лежат в `cash_guide.markets` патча. Полная таблица 319 рынков — в [store-availability.md](AMD/notes/store-availability.md); выставочные там ещё не помечены.

### Если покупатель оформит карту (справка)

- **Как оформить:** Basiskonto банк обязан открыть не позже чем через 10 рабочих дней ([§ 31 ZKG](https://www.gesetze-im-internet.de/zkg/__31.html)). PaysafeWallet — карта без банка: +5 % за пополнение, до 1000 € в день ([Paysafe](https://www.paysafecard.com/de-de/paysafewallet/fees-and-limits/)).
- **Что это даст:**
  - R2R1 у [Galaxus](https://www.galaxus.de/de/s1/product/acer-aspire-16-ai-oled-16-1000-gb-32-gb-de-amd-ryzen-ai-7-350-notebook-66522762) — 1015,87 € (через PaysafeWallet около 1069 €), но экран не подтверждён;
  - R1FY онлайн — 999 € ([idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/211778543_-swift-air-16-oled-16-wuxga-amd-ryzen-ai-5-32gb-1tb-ssd-silber-nx-dl5eg-002-acer.html));
  - Medion онлайн — от 999 €, с SSD это больше 1100 €.
- **Вывод:** карта ничего явно лучше Medion за 946,99 € наличными не даёт.

### Звонок в рынок (по-немецки)

Что подставить:
- **Medion:** «MEDION SPRCHRGD 16 S1 OLED, Artikelnummer 30040202, expert-Webcode 17040041553»; SSD — «Verbatim Vi3000 1 TB, Webcode 17320020417».
- **Acer:** «Acer Swift Air 16 OLED, Teilenummer N-X-Punkt-D-L-5-E-G-Punkt-0-0-2, Webcode 17041266033».
- **Lenovo:** «Lenovo IdeaPad Slim 5 15ARP10, Teilenummer 83J3006GGE, MEDIMAX-Artikel 1505157».

1. «Guten Tag, ich interessiere mich für das Notebook [Modell], Teilenummer [P/N], aus Ihrem Online-Shop, Webcode [Webcode].»
2. «Ist das Gerät bei Ihnen im Markt vorrätig – neu und originalverpackt, kein Ausstellungsstück und kein Restposten?»
3. «Auf der Website steht [Preis] Euro. Gilt dieser Preis auch an der Kasse?» _(Bad Salzungen: «… 797 Euro für das Medion – ist das richtig, kein Preisfehler?»; Bening: «Gilt der Sofort-Rabatt von 40 Euro auch beim Kauf im Markt?»)_
4. «Kann ich im Markt bar bezahlen?»
5. «Können Sie mir das Gerät bis [Tag] zurücklegen? Auf welchen Namen?» _(MEDIMAX по телефону не резервирует ([AGB](https://www.medimax.de/agb), п. 4) — там только спросить про наличие, а резерв оформить на сайте.)_
6. «Haben Sie auch eine SSD 1 TB, M.2 2280, NVMe vorrätig? Zu welchem Preis?»
7. «Gibt es ein Umtausch- oder Rückgaberecht, wenn das Gerät unbenutzt ist – wie viele Tage?»
8. «Vielen Dank! Bis wann haben Sie heute geöffnet?»

Если товара нет: «Können Sie das Gerät bestellen? Wie lange dauert das, und kann ich bei Abholung bar bezahlen?»

### Не проверено

- **Наличные:** берут ли expert и MEDIMAX именно наличные — в их правилах слова «bar» нет.
- **Medion в Bad Salzungen:** настоящая ли это цена, а не ошибка.
- **Скидки и обмен:** действует ли «Sofort-Rabatt» у Bening на кассе; какие условия обмена в Bad Salzungen и Schmalkalden.
- **Экраны:** замеров у `83J3006GGE` нет; ШИМ у Medion и `83J3006GGE` неизвестен.
- **SSD:** есть ли нужный SSD в конкретном рынке MediaMarkt.
- **Galaxus:** примет ли e-money-карту Paysafe. На idealo у Galaxus стоит значок «Vorkasse», а на самом сайте такого способа нет.

---

# Разбор до ночной проверки (30.09 – 01.10, 01:00)

> Ниже — итог до ночной проверки, когда выбором был Swift Air R1FY. Он остаётся запасным №2, а подробности о нём, таблицы производительности, экраны и надёжность — по-прежнему верны. **Устарело:** раздел «Запасной вариант» (Medion теперь найден за 946,99 €, R2R1 — за 1099 € в MEDIMAX Nettetal, но экран не подтверждён), «Как купить за наличные» (см. ночную проверку выше) и «Почему AMD, а не Intel» (теперь №1 — Intel). Полная копия этой версии — [AMD/notes/report-2026-10-01-0100-swiftair.md](AMD/notes/report-2026-10-01-0100-swiftair.md).

## Swift Air R1FY подробно (выбор до ночной проверки, теперь №2)

- **P/N `NX.DL5EG.002`.** Ryzen AI 5 330 (4 ядра / 8 потоков: 1 Zen 5 + 3 Zen 5c), Radeon 820M (2 CU).
  - Память: 32 ГБ LPDDR5, распаяна. SSD 1 ТБ PCIe 4.0, слот M.2 один.
  - Экран: 16" WUXGA OLED, 60 Гц, глянец.
  - 1,1 кг, 50 Вт·ч, зарядка USB-C 65 Вт в комплекте, гарантия 2 года ([Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Acer&ProductCode=NX.DL5EG.002), [LaptopMedia](https://laptopmedia.com/de/review/acer-swift-air-16-sfa16-61m-review-a-16-inch-laptop-that-weighs-under-1-kg/)).
- **Итог — 999,99 € наличными, докупать нечего, сборов нет.**
  - Продавец — **expert** ([карточка expert](https://www.expert.de/shop/unsere-produkte/computer-zubehor/notebooks/laptops/17041266033-swift-air-16-oled-silber-16-zoll-wuxga-amd-ryzen-ai-5-330-32-gb-1024-gb-ssd-amd-radeon-820m.html)): на сайте кнопка «Reservieren und sofort abholen», оплата при получении в магазине.
  - В FAQ expert: резерв «unverbindlich», «Die Bezahlung erfolgt direkt in Ihrem expert Fachmarkt» ([FAQ expert](https://www.expert.de/nuernberg1/Footer/Service/Fragen-Antworten)).
  - Карточка idealo: [211778543](https://www.idealo.de/preisvergleich/OffersOfProduct/211778543_-swift-air-16-oled-16-wuxga-amd-ryzen-ai-5-32gb-1tb-ssd-silber-nx-dl5eg-002-acer.html). Минимум там — 999,00 € (Kaufland МП, продаёт expertDeutschland, и expert.de), но только онлайн-оплатой.
  - **Две оговорки.**
    1. Слова «bar» в FAQ нет. Что можно заплатить наличными — вывод из «оплата в Fachmarkt».
    2. Цена и наличие показаны для рынка expert TeVi Nürnberg. Рынки expert самостоятельные, поэтому до поездки нужно позвонить в свой ([screen-verify-1.md](AMD/notes/screen-verify-1.md)).
- **Выбран отсевом, а не по силе.** Это единственный ноутбук, который прошёл все жёсткие критерии. Для 4K он слабый: скорее всего, понадобится монтаж через прокси (см. «Что теряем»).

**Почему он:**
1. **Прошёл все жёсткие критерии, и других прошедших нет.**
   - Экран измерен.
   - Можно заплатить наличными.
   - Итог ≤ 1100 €.
   - 32 ГБ в двухканале (распайка).
   - 1 ТБ.

   Разобраны все OLED, IPS/mini-LED и игровые 15–16" ([screen-oled.md](AMD/notes/screen-oled.md), [screen-ips.md](AMD/notes/screen-ips.md), [screen-gaming.md](AMD/notes/screen-gaming.md), [display-sweep.md](AMD/notes/display-sweep.md)).
2. **Лучший измеренный экран в бюджете.** Панель Samsung ATNA60KJ04-0: 100 % sRGB и 100 % DCI-P3, ΔE 1,6 из коробки ([LaptopMedia](https://laptopmedia.com/de/review/acer-swift-air-16-sfa16-61m-review-a-16-inch-laptop-that-weighs-under-1-kg/)). Для владельца без внешнего монитора это главное.
3. **Докупать ничего не нужно, и до потолка остаётся 100 €.** 32 ГБ, 1 ТБ и зарядка уже в комплекте ([Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Acer&ProductCode=NX.DL5EG.002)).
4. **Самые частые 4K-исходники декодирует аппаратно.** Это H.264 8 бит и HEVC 8/10 бит 4:2:0 (телефоны, экшн-камеры, большинство камер в обычных режимах) и AV1; AV1 ещё и кодирует ([AMD AMF Wiki](https://github.com/GPUOpen-LibrariesAndSDKs/AMF/wiki/GPU%20and%20APU%20HW%20Features%20and%20Support)).
5. **Корпус прочный, сервис в Германии хороший.** Корпус из магниево-алюминиевого сплава — «überraschend stabil», аккумулятор и вентилятор крепятся на винтах ([LaptopMedia](https://laptopmedia.com/de/review/acer-swift-air-16-sfa16-61m-review-a-16-inch-laptop-that-weighs-under-1-kg/)). Acer — 3-е место по сервису в Германии в опросе NBC ([NBC](https://www.notebookcheck.com/Umfrage-Service-und-Support-im-Reparaturfall-Diese-Laptop-und-Smartphone-Hersteller-koennen-nicht-ueberzeugen.905354.0.html)).

## Запасной вариант

**Второго ноутбука, который прошёл бы все жёсткие критерии, нет** — ни у Intel, ни у AMD (ссылки на проходы — в п. 1 выше). Поэтому запасных вариантов три, и каждый — с уступкой:

1. **Тот же P/N в другом месте, тоже за наличные.** Нужно, если в своём рынке expert R1FY нет.
   - Взять его в другом рынке expert: на сайте выбрать рынок и смотреть, есть ли кнопка «Reservieren».
   - Или заказать в свой рынок через «Anfrage starten» ([FAQ expert](https://www.expert.de/nuernberg1/Footer/Service/Fragen-Antworten)).
   - MediaMarkt и Saturn этот SKU не продают ([screen-verify-1.md](AMD/notes/screen-verify-1.md)).
2. **Если у покупателя есть банковский счёт** (это не подтверждено):
   - Тот же `NX.DL5EG.002` за **999,00 €** переводом у Kaufland МП, продавец expertDeutschland ([idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/211778543_-swift-air-16-oled-16-wuxga-amd-ryzen-ai-5-32gb-1tb-ssd-silber-nx-dl5eg-002-acer.html)). При покупке онлайн по закону есть 14 дней на отказ.
   - Или **Acer Aspire 16 AI OLED A16-61M-R2R1 `NX.JP0EG.00Z`** — это условный запасной всех трёх судей.
     - Цена переводом: **1081,21 €** у computeruniverse (Rechnung/Vorkasse, [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/211631508_-aspire-16-ai-a16-61m-r2r1-acer.html)) или 1015,87 € на сайте Galaxus (на idealo этой цены нет).
     - Процессор вдвое сильнее, графика в 3,3 раза. Но экран подтверждён только даташитом (95 % DCI-P3 у Acer, 100 % у Icecat), замера нет.
       По строгой букве критерия (100 % sRGB / DCI-P3 в даташите производителя) экран **не подтверждён**: у самой Acer 95 %, а 100 % — только у Icecat. Значит, у R2R1 две уступки — оплата и экран.
     - **За наличные ≤ 1100 € его нет.** В Cyberport Store он стоит 2539 €. У MEDIMAX — 1099 € с «Abholung nach Bestellung», но оплата только онлайн, и в AGB прямо сказано: «Barzahlung bei Abholung ist nicht möglich» ([AGB MEDIMAX](https://www.medimax.de/agb), [screen-verify-1.md](AMD/notes/screen-verify-1.md)).
3. **Если можно поднять потолок примерно до 1200 €** — Intel **Medion SPRCHRGD 16 S1 OLED `30040202`**.
   - Цена: **1079 €** наличными в expert (MediaMarkt/Saturn — 1089 €) плюс SSD 1 ТБ за 120,99 € = **1199,99 €** ([idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/207222210_-sprchrgd-16-s1-30040202-medion.html)).
   - Что даёт: экран 2,8K OLED 120 Гц — CHIP намерил 100 % sRGB на версии с Core Ultra 9 ([CHIP](https://www.chip.de/test/Medion-SPRCHRGD-16-S1-OLED-im-Test_186892299.html)); аппаратный декод HEVC 4:2:2.
   - Выше потолка — жёсткий критерий не проходит.

## Производительность

Источник таблиц — [AMD/notes/perf-tables.md](AMD/notes/perf-tables.md).
- **CPU и графика** — медианы NBC; в скобках число протестированных ноутбуков (n). Имя процессора или GPU — ссылка на его страницу NBC.
- **[обзор]** — замер конкретного ноутбука. Он точнее медианы.
- **Puget** — это загрузки пользователей, а не лаборатория. † — меньше 10 прогонов.

### (а) Процессоры финалистов и прежних фаворитов

| CPU · где стоит | Ядра / потоки | TDP (NBC) | R23 Multi | R23 Single |
|---|---|---|---|---|
| [Ryzen AI 5 330](https://www.notebookcheck.net/AMD-Ryzen-AI-5-330-Processor-Benchmarks-and-Specs.1049553.0.html) · ✔ Swift Air R1FY | 4/8 (1 Zen 5 + 3 Zen 5c) | 28 Вт; в корпусе Swift Air — 22–23 Вт [обзор] | 7 840 (1) | 1 812 (1) |
| [Ryzen AI 7 350](https://www.notebookcheck.net/AMD-Ryzen-AI-7-350-Processor-Benchmarks-and-Specs.949825.0.html) · Aspire R2R1, Swift Air R559, IdeaPad `83HY008CGE` | 8/16 (4 Zen 5 + 4 Zen 5c) | 28 Вт | 16 014 (18) | 1 958 (18) |
| [Core Ultra 5 228V](https://www.notebookcheck.net/Intel-Core-Ultra-5-228V-Processor-Benchmarks-and-Specs.893277.0.html) · Medion `30040202` | 8/8 (4P + 4E) | 17 Вт | 9 932 (2) | 1 758 (2) |
| [Core Ultra 7 255H](https://www.notebookcheck.net/Intel-Core-Ultra-7-255H-Processor-Benchmarks-and-Specs.944139.0.html) · HP `BM9T4EA#ABD` | 16/16 (6P + 8E + 2LPE) | 28 Вт | 17 845 (20) | 2 061 (20) |
| [Core i7-13620H](https://www.notebookcheck.net/Intel-Core-i7-13620H-Processor-Benchmarks-and-Specs.677505.0.html) · IdeaPad `83HS00BLGE` | 10/16 (6P + 4E) | 45 Вт | 15 176 (7) | 1 833 (7) |

| CPU | CB2024 Multi / Single | Geekbench 6 Multi / Single | x265 4K, кадр/с | Blender, с (меньше — лучше) |
|---|---|---|---|---|
| Ryzen AI 5 330 | нет данных на NBC | 7 600 / 2 466 (2) | 10,3 (1) | 657 (1) |
| Ryzen AI 7 350 | 901 / 116 (15); **в корпусе Swift Air — 671 [обзор]** | 12 835 / 2 853 (17); в Swift Air — 11 278 / 2 866 [обзор] | 20,6 (16) | 322 (17) |
| Core Ultra 5 228V | 494 / 105 (2) | 10 313 / 2 585 (3) | 11,2 (2) | 689 (2) |
| Core Ultra 7 255H | 1 053 / 124 (13–15) | 15 223 / 2 866 (20) | 21,4 (19) | 326 (18) |
| Core i7-13620H | 696 / 110 (3) | 11 723 / 2 568 (6) | 16,6 (7) | 391 (7) |

- **У AI 5 330 есть всего один замер** — Lenovo IdeaPad Slim 5 16AKP10 при 40/30 Вт ([NBC](https://www.notebookcheck.net/Dual-debut-in-the-Lenovo-IdeaPad-Slim-5-16-Ryzen-AI-5-330-and-Radeon-820M-in-review.1166676.0.html)).
  Swift Air держит 22 Вт 30 минут при 68 °C. Мерили на версии с AI 7 350: CB2024 у неё 671, это на 26 % ниже медианы ([LaptopMedia](https://laptopmedia.com/de/review/acer-swift-air-16-sfa16-61m-review-a-16-inch-laptop-that-weighs-under-1-kg/)).
  Значит, R1FY в многопотоке, скорее всего, ниже 7 840. AI 5 330 в Swift Air никто не мерил — не проверено.
- **Многопоток:** AI 5 330 — это 49 % от AI 7 350 и 44 % от 255H. Программный декод и создание прокси на нём примерно вдвое медленнее. Это вывод по R23 и x265, а не замер монтажа.

### (б) Графика

| iGPU · где стоит | Time Spy Graphics | Steel Nomad Light | Puget Resolve 20.0–20.3 (PB 1.2, Standard) | Puget Premiere 25.1–25.2 (PB 1.x) |
|---|---|---|---|---|
| [Radeon 820M](https://www.notebookcheck.net/AMD-Radeon-820M-Benchmarks-and-Specs.1059782.0.html) (2 CU) · ✔ Swift Air R1FY | **786 (1)** | нет данных | **нет в базе Puget** | **нет в базе Puget** |
| [Radeon 840M](https://www.notebookcheck.net/AMD-Radeon-840M-Benchmarks-and-Specs.950405.0.html) (4 CU) — для масштаба, вдвое больше CU, чем у 820M | 1 415 (7) | нет данных | [1 262 †](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/27/GPU/AMD%20Radeon%20840M%20Graphics/AMD%20Radeon%20860M%20Graphics/) | [2 051 (11)](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/23/GPU/AMD%20Radeon%20840M%20Graphics/AMD%20Radeon%20860M%20Graphics/) |
| [Radeon 860M](https://www.notebookcheck.net/AMD-Radeon-860M-Benchmarks-and-Specs.949852.0.html) (8 CU) · R2R1, R559, `83HY008CGE` | 2 565 (23); в корпусе Swift Air — 2 252 [обзор] | 2 380 (11) | [2 402 (19)](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/27/GPU/AMD%20Radeon%20840M%20Graphics/AMD%20Radeon%20860M%20Graphics/) | [2 882 (27)](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/23/GPU/AMD%20Radeon%20840M%20Graphics/AMD%20Radeon%20860M%20Graphics/) |
| [Arc 130V](https://www.notebookcheck.net/Intel-Arc-Graphics-130V-Benchmarks-and-Specs.854992.0.html) · Medion `30040202` | 3 401 (10) | 2 670 (5) | [2 304 † (8 ГБ; у 16 ГБ данных нет)](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/27/GPU/Intel%20Arc%20130V%20GPU%20%2816GB%29/Intel%20Arc%20130V%20GPU%20%288GB%29/) | [2 809 (20, 8 ГБ) / 2 433 (11, 16 ГБ)](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/23/GPU/Intel%20Arc%20130V%20GPU%20%2816GB%29/Intel%20Arc%20130V%20GPU%20%288GB%29/) |
| [Arc 140T](https://www.notebookcheck.net/Intel-Arc-140T-Benchmarks-and-Specs.942050.0.html) · HP `BM9T4EA#ABD` | 3 843 (20) | 3 546 (6) | [2 489 (27)](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/27/GPU/Intel%20Arc%20130T%20GPU%20%2816GB%29/Intel%20Arc%20140T%20GPU%20%2816GB%29/) | [3 661 (70)](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/23/GPU/Intel%20Arc%20130T%20GPU%20%2816GB%29/Intel%20Arc%20140T%20GPU%20%2816GB%29/) |
| [UHD 64 EU](https://www.notebookcheck.net/Intel-UHD-Graphics-64EUs-Alder-Lake-GPU-Benchmarks-and-Specs.589905.0.html) · IdeaPad `83HS00BLGE` | 1 110 (12) | 976 (2) | [Basic 1 049 †](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/27/GPU/Intel%20UHD%20Graphics/Intel%20Iris%20Xe%20Graphics/) (Standard нет) | [1 599 (11)](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/23/GPU/Intel%20UHD%20Graphics/Intel%20Iris%20Xe%20Graphics/) |

**Подтесты Puget, кадр/с** (только GPU с ≥ 10 прогонами; ссылки — те же страницы, что в таблице выше):

| iGPU | Resolve: 4K HEVC 4:2:2 10 бит | Resolve: Color Node ×30 | Premiere: 4K H.264 8 бит | Premiere: Lumetri ×40 |
|---|---|---|---|---|
| 820M (R1FY) | нет данных | нет данных | нет данных | нет данных |
| 840M | — | — | 31,18 | 7,86 |
| 860M | 43,35 (декодирует CPU) | 13,64 | 44,95 | 11,9 |
| Arc 140V (Lunar Lake, старшая к 130V) | 67,05 ([Puget](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/27/GPU/Intel%20Arc%20140V%20GPU%20%2816GB%29/Intel%20Arc%20140V%20GPU%20%288GB%29/)) | 12,63 | 47,84 | 16,8 |
| Arc 130V (8 ГБ / 16 ГБ) | — | — | 44,88 / 40,07 | 16,89 / 14,14 |
| Arc 140T | 56,29 | 8,77 | 60,78 | 18,15 |
| UHD | — | — | 20,8 | 6,26 |

- **Графика 820M — самая слабая во всех таблицах.** Time Spy 786: это в 3,3 раза меньше 860M, в 4,3 раза меньше Arc 130V и в 4,9 раза меньше Arc 140T.
  Прогонов Puget у 820M нет вообще. Даже у 840M с вдвое большим числом CU — худший результат среди AMD в Premiere 25.1 ([perf-tables.md](AMD/notes/perf-tables.md), §3).
- **Экспорт и декод 4:2:0 у 820M идут через тот же медиаблок VCN 4.0.5, что у 860M.** Эффекты, цветокоррекцию и шумодав тянет только сама графика, и здесь разница — в разы.

### (в) Аппаратный декод и кодирование

Д — аппаратный декод, К — аппаратное кодирование, «нет» — делает процессор.

| Медиаблок · ноутбуки | H.264 8 бит 4:2:0 | H.264 10 бит | H.264 4:2:2 | HEVC 4:2:0 8/10 бит | HEVC 4:2:2 10 бит | AV1 |
|---|---|---|---|---|---|---|
| AMD VCN 4.0.5 · ✔ Swift Air, R2R1, R559, `83HY008CGE` | Д/К | нет | нет | Д/К | **нет** | Д/К |
| Intel Lunar Lake · Medion `30040202` | Д/К | нет | нет | Д/К | **Д/К** | Д/К |
| Intel Arrow Lake-H · HP `BM9T4EA#ABD` | Д/К | нет | нет | Д/К | **Д/К** | Д/К |
| Intel Raptor Lake-H · `83HS00BLGE` | Д/К | нет | нет | Д/К | **Д** (К — через шейдеры) | Д, К нет |
| NVIDIA RTX 50 (для справки, от 1266,66 €) | Д/К | Д | **Д/К** | Д/К | **Д/К** | Д/К |

Источники: Intel — [media-driver](https://raw.githubusercontent.com/intel/media-driver/master/docs/media_features.md) и [Intel EDC (Raptor Lake)](https://edc.intel.com/content/www/us/en/design/products/platforms/details/raptor-lake-s/13th-generation-core-processors-datasheet-volume-1-of-2/hardware-accelerated-video-decode/). AMD — [AMF Wiki](https://github.com/GPUOpen-LibrariesAndSDKs/AMF/wiki/GPU%20and%20APU%20HW%20Features%20and%20Support) («All codecs are 4:2:0»), версия VCN — по [таблице ядра Linux](https://raw.githubusercontent.com/torvalds/linux/master/Documentation/gpu/amdgpu/apu-asic-info-table.csv). NVIDIA — [Blackwell](https://images.nvidia.com/aem-dam/Solutions/geforce/blackwell/nvidia-rtx-blackwell-gpu-architecture.pdf).

Что это значит в программах:
- **Resolve Studio и Premiere** используют VCN для 4:2:0. 4:2:2 на AMD декодирует процессор ([Puget, Resolve](https://www.pugetsystems.com/labs/articles/what-h-264-and-h-265-hardware-decoding-is-supported-in-davinci-resolve-studio-2122/), [Puget, Premiere](https://www.pugetsystems.com/labs/articles/what-h-264-and-h-265-hardware-decoding-is-supported-in-premiere-pro-2120/)).
- **Бесплатный Resolve под Windows GPU-декод не использует вообще.** Он открывает только «OS-supported» профили: H.264 8 бит и H.265 8/10 бит. Остальное — «More profiles and GPU acceleration in Studio» ([Blackmagic, Resolve 21](https://documents.blackmagicdesign.com/SupportNotes/DaVinci_Resolve_21_Supported_Codec_List.pdf)).
  На R1FY это значит, что в бесплатном Resolve весь 4K декодируют 4 ядра при 22 Вт.
- **Какие камеры что снимают** ([amd-codecs.md](AMD/notes/amd-codecs.md)):
  - HEVC 10 бит 4:2:2 — Canon C-Log, Sony XAVC HS 4:2:2, Fujifilm H.265 4:2:2. Аппаратно их декодирует любой Intel с 11-го поколения, AMD — ни один.
  - H.264 10 бит 4:2:2 — Sony XAVC S 10 бит, Panasonic MOV 4:2:2, DJI ALL-I. Аппаратно их не декодирует ни один ноутбук до 1100 €: нужна RTX 50 или Panther Lake.
- **Риск Acer:** с 06.2026 часть устройств Acer в Германии идёт «ohne vorinstallierten HEVC-Codec» ([ChannelPartner](https://www.channelpartner.de/article/4187748/acer-und-asus-liefern-wieder.html)). По заявлению Acer, это непредустановленный программный кодек, а не аппаратная блокировка ([hevc-amd.md](AMD/notes/hevc-amd.md), §5).
  Лечится бесплатно: «HEVC-Videoerweiterungen vom Gerätehersteller» стоят 0 € ([Microsoft Store](https://apps.microsoft.com/detail/9N4WGH0Z6VHQ)).

## Экраны

Сводка по [displays.md](AMD/notes/displays.md), [display-sweep.md](AMD/notes/display-sweep.md) и [screen-oled.md](AMD/notes/screen-oled.md). Порог — ≥ ~95 % sRGB по замеру или 100 % sRGB / DCI-P3 по даташиту.

| Ноутбук · P/N | Панель | sRGB / DCI-P3 | Яркость, кд/м² | ШИМ | Источник | Порог |
|---|---|---|---|---|---|---|
| ✔ Swift Air 16 R1FY · `NX.DL5EG.002` | WUXGA OLED 60 Гц, Samsung ATNA60KJ04-0, глянец 178 GU | **замер: 100 % / 100 %**, ΔE 1,6 | 297 | есть, «mit begrenzter Amplitude», частота не указана | [LaptopMedia](https://laptopmedia.com/de/review/acer-swift-air-16-sfa16-61m-review-a-16-inch-laptop-that-weighs-under-1-kg/) (экземпляр с AI 7 350, панель та же); OLED у этого P/N — [Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Acer&ProductCode=NX.DL5EG.002) | ✔ |
| Swift Air 16 R559 · `SFA16-61M-R559` | та же панель | та же | 297 | та же | [LaptopMedia](https://laptopmedia.com/de/review/acer-swift-air-16-sfa16-61m-review-a-16-inch-laptop-that-weighs-under-1-kg/) | ✔, но от 1149 € |
| Aspire 16 AI R2R1 · `NX.JP0EG.00Z` | WUXGA OLED; 60 Гц по Icecat, 120 Гц по Cyberport | **по даташиту:** Acer — 95 % P3, Icecat — 100 % P3; замера нет | 300 (Icecat) | не проверено | [даташит Acer](https://gzhls.at/blob/ldb/e/9/9/4/1b8b6ae3e1047dc798a552be0d80e9a0f0ab.pdf), [Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Acer&ProductCode=NX.JP0EG.00Z) | ? не подтверждён: у Acer 95 % P3 (< 100 %), 100 % — только Icecat |
| Medion SPRCHRGD 16 S1 · `30040202` | 2,8K OLED 120 Гц | **замер: 100 % / 100 %**, 93 % AdobeRGB | ~400 (SDR) | не проверено | [CHIP](https://www.chip.de/test/Medion-SPRCHRGD-16-S1-OLED-im-Test_186892299.html) (версия с Core Ultra 9) | ✔, но 1199,99 € |
| HP OmniBook 7 16 · `BM9T4EA#ABD` | WUXGA IPS, антиблик | **62,5 % sRGB** по даташиту, замера нет | 300 | нет (DC dimming) | [даташит HP c09154072](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09154072) | ✘ |
| IdeaPad Slim 5 16IRH10 · `83HS00BLGE` | WUXGA IPS, антиблик | 45 % NTSC; **замер той же панели — 57,7 % / 39,7 %** | 360 | нет | [NBC 16IRH10R](https://www.notebookcheck.com/Lenovo-IdeaPad-Slim-5-16-Laptop-im-Test-Intel-Core-i5-vs-AMD-Ryzen-5.1174964.0.html) | ✘ |
| IdeaPad Slim 5 16AKP10 · `83HY008CGE` | WUXGA IPS, антиблик | 45 % NTSC; **замер — 57,6 % / 39,1 %** | 349 | нет | [NBC 16AKP10](https://www.notebookcheck.net/Dual-debut-in-the-Lenovo-IdeaPad-Slim-5-16-Ryzen-AI-5-330-and-Radeon-820M-in-review.1166676.0.html) | ✘ |

- **Минусы экрана R1FY:**
  - всего 297 кд/м² и сильный глянец — сами обозреватели называют блики главной слабостью;
  - 60 Гц;
  - мелкий текст мягче из-за необычной раскладки субпикселей ([LaptopMedia](https://laptopmedia.com/de/review/acer-swift-air-16-sfa16-61m-review-a-16-inch-laptop-that-weighs-under-1-kg/)).
- **Широкий охват — это ещё не точный цвет.** У OLED 100 % DCI-P3, поэтому sRGB-материал без режима sRGB или профиля будет перенасыщен. Resolve под Windows ICC-профиль экрана сам не применяет ([форум Blackmagic](https://forum.blackmagicdesign.com/viewtopic.php?uid=16&f=21&t=133034&start=0)).
  Есть ли у Acer режим sRGB для этой панели — не проверено. Что с этим делать — в разделе «Что сделать при покупке».
- **ШИМ.** У родственного Swift Go 16 AI OLED NBC намерил ШИМ 220 Гц ([NBC](https://www.notebookcheck.com/Solide-Performance-und-farbechtes-OLED-Acer-Swift-Go-16-AI-mit-AMD-Ryzen-im-Test.1102652.0.html)). У Swift Air частоту не мерил никто.

## Надёжность, ремонт и запчасти

По Acer данные собраны в [reliability.md](AMD/notes/reliability.md) (30.09, 23:30–23:58), по HP и Lenovo — в [Intel/REPORT.md](Intel/REPORT.md) и [Intel/notes/brands.md](Intel/notes/brands.md). Места брендов по надёжности — из сводки Consumer Reports и PCMag 2025 ([BGR](https://www.bgr.com/2072636/most-reliable-laptop-brands-ranked-worst-best/)).

| Ноутбук | Бренд и модель | Гарантия | Срок запчастей | Детали в продаже и цены | Сервис-мануал | Распространённость |
|---|---|---|---|---|---|---|
| ✔ **Swift Air 16 R1FY** | **Бренд:** Acer — 8-й из 10 по надёжности, но 3-й по сервису в DE ([NBC](https://www.notebookcheck.com/Umfrage-Service-und-Support-im-Reparaturfall-Diese-Laptop-und-Smartphone-Hersteller-koennen-nicht-ueberzeugen.905354.0.html)). У Swift бывают проблемы с петлями и крышкой ([IPC](https://blog.ipc-computer.de/2026/07/acer-service/)). **Модель:** корпус «überraschend stabil»; вентилятор крутится и в простое с тонким писком ([LaptopMedia](https://laptopmedia.com/de/review/acer-swift-air-16-sfa16-61m-review-a-16-inch-laptop-that-weighs-under-1-kg/)); BIOS 1.07 от 24.09.2026 — «Modify fan table» ([Acer](https://www.acer.com/de-de/support/product-support/SFA16-61M)) | 2 года с отправкой в сервис Acer ([Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Acer&ProductCode=NX.DL5EG.002)) + 2 года Gewährleistung у expert | Acer публичного срока не даёт | IPC ([страница модели](https://www.ipc-computer.de/acer/notebook/swift-serie/swift-air-16-sfa16-61m/)): дисплейный блок с петлями 225 € (последний на складе), топкейс 93 €, дно 105 €, плата 867 €, Wi-Fi 43 €, блок питания 33–39 €. **Аккумулятора и вентилятора в продаже нет** — ни у IPC, ни на eBay | нет, только User Manual | **редкая**: 6 предложений на idealo, 1 отзыв на expert, на Amazon оценок нет |
| Aspire 16 AI R2R1 | **Бренд:** Acer — как выше. **Модель:** TechRadar — «somewhat flimsy … flex», петля не самая устойчивая ([TechRadar](https://www.techradar.com/computing/windows-laptops/acer-aspire-16-ai-review)) | 2 года ([даташит](https://gzhls.at/blob/ldb/e/9/9/4/1b8b6ae3e1047dc798a552be0d80e9a0f0ab.pdf)) | нет обязательств | IPC ([A16-61M](https://www.ipc-computer.de/acer/notebook/aspire-serie/16/aspire-a16-61m/)): аккумулятор 94 €, OLED-матрица Samsung 333 €, топкейс 74 €, вентилятор 35 €. На eBay аккумулятор AP22ABN — 74 новых предложения по ~105 € ([eBay](https://www.ebay.de/sch/i.html?_nkw=AP22ABN&LH_ItemCondition=1000)) | публично нет; сервис-гайд существует ([Acer Community](https://community.acer.com/en/discussion/739642/urgent-aspire-16-ai-a16-61m-oled-latest-bios-shows-lcd-instead-of-oled-potential-burn-in-risk)) | заметно популярнее: 15 карточек A16-61M, на Amazon.de до 19 оценок (4,2★) |
| Medion `30040202` | **Бренд:** Medion (принадлежит Lenovo). **Модель:** heise — «Wenn da nur kein Akkuproblem wäre» (заряд застревает на ~89 %, суть за пейволлом) ([heise](https://www.heise.de/tests/Viel-RAM-fuers-Geld-Mittelklassenotebook-Medion-Sprchrgd-16-S1-im-Test-11354704.html)); netzwelt — сильные блики ([netzwelt](https://www.netzwelt.de/medion-sprchrgd-16-s1-oled/testbericht.html)) | 2 года, **на аккумулятор гарантии нет** ([Medion](https://www.medion.com/de/shop/garantiebedingungen)) | публичного срока нет, не проверено ([brands.md](Intel/notes/brands.md)) | **почти ничего** (01.10, ~00:37): в [Medion Service Shop](https://www.medion.com/medionserviceshop/de/search/?text=30040202) по «30040202» — «keine Treffer», по «SPRCHRGD» — только 14-дюймовые S1/S2. У IPC ([SPRCHRGD 16 S1 A16LNL-MP](https://www.ipc-computer.de/medion/notebook/sprchrgd-serie/sprchrgd-16-s1-a16lnl-mp/)) — только SSD (1 ТБ за 223 €) и RAM (распайка); аккумулятора, матрицы и вентилятора нет | не найден; отдельно не искал | средняя: 6 предложений на idealo; MediaMarkt, Saturn, expert. На [medion.com](https://www.medion.com/de/shop/p/multimedia-notebooks-medion-sprchrgd-16-s1-oled-copilot-pc-intel-core-ultra-5-228v--windows-11-home-40-6-cm-16--2-8k-oled-display-512-gb-ssd-32-gb-ram-30040202A1) — 1199,95 €, «Ausverkauft» |
| HP `BM9T4EA#ABD` | **Бренд:** HP — 9-я из 10. **Модель:** у потребительских HP бывает отключён HEVC ([HP Community](https://h30434.www3.hp.com/t5/Notebook-Video-Display-and-Touch/H265-HEVC-HW-encoder-and-decoder-not-available/td-p/9431209)) | 2 года | у потребительских HP запчасти снимают вскоре после конца гарантии ([IPC](https://blog.ipc-computer.de/2025/10/hp-service/)) | HP Parts Store; для этой модели не проверял | **есть** — HP MSG ([PDF](https://kaas.hpcloud.hp.com/pdf-public/pdf_12123979_en-US-1.pdf)) | один продавец (hp.com) |
| IdeaPad `83HS00BLGE` | **Бренд:** Lenovo — 5-й из 10. **Модель:** громкий вентилятор | 2 года ([PSREF](https://psref.lenovo.com/Detail/IdeaPad/IdeaPad_Slim_5_16IRH10?M=83HS00BLGE)) | Lenovo — 5 лет ([brands.md](Intel/notes/brands.md)) | у Lenovo DE для этого MTM 35 деталей с ценами ([Lenovo](https://pcsupport.lenovo.com/de/de/products/laptops-and-netbooks/ideapad-s-series-netbooks/ideapad-slim-5-16irh10/83hs/83hs00blge/parts/display/model)) | в этой сессии не проверял | массовая, 7 предложений |

**Коротко по каждому:**
- **Swift Air R1FY (выбор).** Первые 2 года прикрыты: гарантия Acer и Gewährleistung у того рынка expert, где купили: с дефектом можно прийти прямо туда.
  Ремонт после 2 лет — слабое место:
  - плата стоит 867 € (87 % цены ноутбука);
  - дисплейный блок — 225 € плюс 109 € за установку, остался последний;
  - аккумулятора 50 Вт·ч в продаже нет.

  Оценки из [reliability.md](AMD/notes/reliability.md): проблемность 4,5, ремонт 3,5.
- **Aspire R2R1.** По запчастям лучше Swift Air: массовый аккумулятор, есть OLED-матрица. Корпус слабее (TechRadar), разборку никто не публиковал. Проблемность 4, ремонт 4.
- **Medion 30040202.** Всё распаяно, M.2 один, на аккумулятор гарантии нет, у heise есть вопросы к аккумулятору.
  Запчастей к модели почти нет: у IPC — только SSD, в Medion Service Shop модели нет. Надёжности бренда в сводке CR/PCMag нет ([BGR](https://www.bgr.com/2072636/most-reliable-laptop-brands-ranked-worst-best/)). Ремонт после гарантии — самый рискованный из трёх финалистов.
- **HP и `83HS00BLGE`** — для справки, экран не прошёл. У `83HS00BLGE` лучший ремонт из всех (2×16 SO-DIMM, второй M.2, 35 деталей у Lenovo); у HP есть открытый мануал, но бренд предпоследний по надёжности.

## Как купить за наличные

**Nachnahme не предлагает ни один продавец ни в одной из этих карточек idealo** ([screen-oled.md](AMD/notes/screen-oled.md)). Значит, наличными можно заплатить только в магазине.

### Выбор — Swift Air R1FY `NX.DL5EG.002`: expert, резерв и оплата в магазине

| Что | Как |
|---|---|
| Продавец | Рынок expert (Fachmarkt). В сети MediaMarkt/Saturn этого SKU нет ([screen-verify-1.md](AMD/notes/screen-verify-1.md)) |
| Способ | На [странице товара](https://www.expert.de/shop/unsere-produkte/computer-zubehor/notebooks/laptops/17041266033-swift-air-16-oled-silber-16-zoll-wuxga-amd-ryzen-ai-5-330-32-gb-1024-gb-ssd-amd-radeon-820m.html) выбрать свой рынок, нажать «Reservieren und sofort abholen», забрать и заплатить на кассе. Резерв «unverbindlich» ([FAQ expert](https://www.expert.de/nuernberg1/Footer/Service/Fragen-Antworten)) |
| Цена и сбор | 999,99 €, сбора нет. Онлайн-оплата expert (WERO, карта, PayPal, Klarna) здесь не нужна |
| Срок | У рынка Nürnberg — «Abholbereit oder sofort auslieferbar», то есть в тот же день, если товар на месте (перепроверено 01.10, 00:31: 999,99 €, та же кнопка, 1 отзыв 5,0). Срок резерва у каждого рынка свой: например, expert TechnoMarkt держит товар 72 часа ([expert TechnoMarkt](https://wir.expert-technomarkt.de/services/services/online-reservieren/abholen/)). Для своего рынка — уточнить |
| Как проверить наличие | Выбрать на сайте свой рынок. Кнопка «Reservieren» значит, что товар в этом рынке есть; «Anfrage starten» — нет, но можно запросить (FAQ expert). Надёжнее — позвонить |
| Что спросить по телефону | 1) есть ли R1FY (`NX.DL5EG.002`) и по какой цене; 2) можно ли заплатить наличными — слова «bar» в FAQ нет; 3) есть ли добровольный обмен или возврат |
| Возврат | **Законного права на отказ за 14 дней при покупке в магазине нет.** Оно есть только при дистанционной покупке и покупке вне магазина ([§ 312g BGB](https://www.gesetze-im-internet.de/bgb/__312g.html), [Verbraucherzentrale](https://www.verbraucherzentrale.de/wissen/vertraege-reklamation/kundenrechte/von-widerruf-bis-umtausch-wenn-sie-mit-der-ware-nicht-zufrieden-sind-5117)). Онлайн-резерв договором не считается: договор заключают на кассе (мой вывод). Купленное в Fachmarkt возвращают только через сам рынок (FAQ expert). Добровольные условия зависят от рынка: например, у expert TechnoMarkt — 30 дней, но только для товара в «einwandfreiem ungebrauchtem Zustand» ([expert TechnoMarkt](https://wir.expert-technomarkt.de/services/services/geld-zurueck-garantie/)). Gewährleistung — 2 года в любом случае |

### Условный запасной — Aspire R2R1 `NX.JP0EG.00Z`: только переводом

| Что | Как |
|---|---|
| Продавец и цена | computeruniverse — **1081,21 €** с доставкой, Rechnung/Vorkasse ([idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/211631508_-aspire-16-ai-a16-61m-r2r1-acer.html)). Galaxus — 1015,87 €, доставка 7–13.10, по строке idealo Rechnung/Vorkasse. Этой цены на idealo нет, сайт Galaxus ([screen-verify-1.md](AMD/notes/screen-verify-1.md)) |
| Наличными | **Нельзя** (перепроверено 01.10, 00:32–00:40). В Cyberport Store он стоит 2539 € ([Cyberport](https://www.cyberport.de/notebook-und-tablet/notebooks/acer/pdp/1c26-cvs/acer-aspire-16-ai-oled-a16-61m-r2r1-16-wuxga-oled-ryzen-ai-7-350-32gb-1tb-win11.html)). У MEDIMAX — 1099 € с «Abholung nach Bestellung», но оплата только онлайн (PayPal, карта, Vorkasse, easyCredit, Amazon Pay — [MEDIMAX](https://www.medimax.de/zahlarten)), и в AGB: «Barzahlung bei Abholung ist nicht möglich» ([AGB](https://www.medimax.de/agb)). Резерва с оплатой в магазине у этого товара нет. У computeruniverse — финансирование, PayPal, Apple Pay, Amazon Pay, карта, Vorkasse, Klarna, Rechnung; Nachnahme и наличных нет ([computeruniverse](https://www.computeruniverse.net/de/page/zahlungs)). Nachnahme нет ни у кого |
| Когда годится | Только если у покупателя есть банковский счёт (не подтверждено). Можно ли внести Vorkasse наличными через кассу банка — не проверено |
| Возврат | Покупка дистанционная, поэтому по закону действует 14 дней на отказ. У computeruniverse — 30 дней (R30 в строке idealo, [prices-final.md](AMD/notes/prices-final.md)) |

### Справка — Medion `30040202`: наличными можно, но выше потолка

- В магазинах expert — 1079 €, MediaMarkt и Saturn — 1089 € ([idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/207222210_-sprchrgd-16-s1-30040202-medion.html), 01.10).
- SSD у него 512 ГБ, поэтому нужен SSD 1 ТБ: 120,99 € онлайн у notebooksbilliger. Сколько SSD стоит за наличные в магазине — не проверено.
- Итог ≥ 1199,99 €.

## Что теряем со Swift Air R1FY

1. **Мощность.** Это самый слабый вариант во всех таблицах (раздел «Производительность»):
   - процессор: R23 7 840 против 16 014 у AI 7 350 (−51 %) и 17 845 у 255H (−56 %);
   - графика: Time Spy 786 против 2 565 у 860M, 3 401 у Arc 130V, 3 843 у Arc 140T.

   Эффекты, шумодав, стабилизация и многослойный монтаж 4K, скорее всего, пойдут только через прокси, а таймлайн лучше вести в 1080p. Это вывод, замера монтажа на 820M нет.
2. **HEVC 4:2:2 10 бит** (Canon, Sony, Fujifilm в «pro»-режимах).
   - Здесь его декодирует процессор. По оценке судьи — примерно 15–20 кадр/с (пропорция по R23 от 43 кадр/с у 860M-машин), то есть ниже реального времени. Это не замер.
   - Любой Intel 11+ декодировал бы его аппаратно: 56–67 кадр/с в Puget ([perf-tables.md](AMD/notes/perf-tables.md), §3.1).
3. **H.264 10 бит 4:2:2** (Sony XAVC S 10 бит, Panasonic, DJI ALL-I) аппаратно не декодирует ни один ноутбук до 1100 €. Теряется только вдвое более сильный процессор R2R1 или HP.
   Бесплатный Resolve такой файл не откроет ни на каком ноутбуке — нужен Studio ([Blackmagic](https://documents.blackmagicdesign.com/SupportNotes/DaVinci_Resolve_21_Supported_Codec_List.pdf)).
4. **Бесплатный DaVinci Resolve** не использует GPU-декод. Весь 4K-декод ляжет на 4 ядра при 22 Вт. Программа неизвестна, а бесплатный Resolve для бюджетного пользователя вероятен. **Это главный риск.**
5. **Апгрейда не будет никогда.**
   - 32 ГБ распаяны, M.2 один.
   - USB-C только 5 Гбит/с, без USB4 и Thunderbolt, поэтому внешнюю видеокарту не подключить.
   - HDMI 1.4, кардридера нет ([LaptopMedia](https://laptopmedia.com/de/review/acer-swift-air-16-sfa16-61m-review-a-16-inch-laptop-that-weighs-under-1-kg/)).
6. **Возврат.** При покупке в магазине законного права на отказ нет. «Медленно монтирует» — не дефект, гарантия тут не поможет (раздел «Как купить за наличные»).
7. **Экран сверх порога:** 297 кд/м², сильные блики, 60 Гц, частота ШИМ неизвестна.
8. **Ремонт после 2 лет:** плата 867 €, аккумулятора и вентилятора в продаже нет ([reliability.md](AMD/notes/reliability.md)).

**Что даёт ослабление одного критерия:**

| Если… | Что брать | Что это даёт |
|---|---|---|
| у покупателя есть счёт (+81,22 €) | Aspire R2R1 за 1081,21 € переводом | CPU ×2, графика ×3,3, 2× USB4, HDMI 2.1, право отказа 14 дней. Кодеки те же (4:2:2 нет). Экран — только по даташиту, и у Acer там 95 % P3: по строгому правилу не подтверждён |
| потолок ~1200 € (+200 €) | Medion `30040202` за 1199,99 € наличными | аппаратный HEVC 4:2:2, Arc 130V (×4,3 по Time Spy), 2,8K OLED 120 Гц ~400 кд/м². Процессор тоже слабый (R23 9 932) |

Ноутбуки без полного sRGB (HP `BM9T4EA#ABD`, IdeaPad `83HS00BLGE` и `83HY008CGE`) здесь как вариант не приводятся: владелец исключил их при любой цене и мощности.

## Финалисты

У каждого судьи свой взгляд: судья 1 — кодеки при неизвестном исходнике, судья 2 — реальная работа с 4K (процессор, графика, шум, экран), судья 3 — надёжность и риски покупки. Шкала 1–10.
«Средн.» — среднее пяти оценок по общей шкале веток: проблемность, ремонт, цена за наличные, портативность, мощность ([screen-scores.md](AMD/notes/screen-scores.md), §3).

| Модель · P/N | Жёсткие критерии | Итог наличными / переводом | Средн. | Судья 1 кодеки | Судья 2 4K | Судья 3 риски |
|---|---|---|---|---|---|---|
| **Swift Air 16 OLED R1FY** · [`NX.DL5EG.002`](https://www.idealo.de/preisvergleich/OffersOfProduct/211778543_-swift-air-16-oled-16-wuxga-amd-ryzen-ai-5-32gb-1tb-ssd-silber-nx-dl5eg-002-acer.html) | ✔ все | **999,99 €** (expert) / 999,00 € | 5,5 | 3 | 3,5 | 5 |
| Aspire 16 AI OLED R2R1 · [`NX.JP0EG.00Z`](https://www.idealo.de/preisvergleich/OffersOfProduct/211631508_-aspire-16-ai-a16-61m-r2r1-acer.html) | ✘ наличные, ? экран (у Acer 95 % P3) | нет / 1081,21 € (Galaxus-сайт 1015,87) | 4,5 наличными, 5,5 переводом | 5 | 5,5 | 4,5 |
| Medion SPRCHRGD 16 S1 OLED · [`30040202`](https://www.idealo.de/preisvergleich/OffersOfProduct/207222210_-sprchrgd-16-s1-30040202-medion.html) | ✘ цена | 1199,99 € / 1119,99 € (с SSD; eBay МП, способы оплаты не показаны) | 6 и при 1119,99 €, и при 1199,99 € наличными: 6 / 4 / 4,5 или 3 / 9 / 7 → 6,1 или 5,8 ([Intel/REPORT.md](Intel/REPORT.md)) | 6 | 6,5 | 3 |
| HP OmniBook 7 AI 16 · [`BM9T4EA#ABD`](https://www.idealo.de/preisvergleich/OffersOfProduct/206602335_-omnibook-7-ai-16-ay0770ng-hp.html) | ✘ экран, ✘ наличные | нет / 979,30 € | 6 переводом | 7,5 | 6,5 | 2 |
| IdeaPad Slim 5 16IRH10 · [`83HS00BLGE`](https://www.idealo.de/preisvergleich/OffersOfProduct/209881995_-ideapad-slim-5-16-83hs00blge-lenovo.html) | ✘ экран | не проверено / 993,30 € | 7 | 5,5 | — | 2 |
| Swift Air 16 OLED R559 · [`SFA16-61M-R559`](https://www.idealo.de/preisvergleich/OffersOfProduct/209373389_-swift-air-16-oled-sfa16-61m-r559-acer.html) | ✘ цена | — / от 1149 € | — | — | 5 | — |
| IdeaPad Slim 5 16AKP10 · [`83HY008CGE`](https://www.idealo.de/preisvergleich/OffersOfProduct/209439304_-ideapad-slim-5-16-83hy008cge-lenovo.html) | ✘ экран, ✘ наличные | нет / 1059,99 € | 7 переводом | — | — | — |

«—» — судья этот ноутбук в свою пятёрку не брал. Строки с ✘ — справка, а не рекомендация: у них выше «Средн.», но каждая нарушает жёсткий критерий.

**Решение по сумме доводов судей.** Все трое ставят №1 **R1FY**, и все трое — отсевом: другие ноутбуки выше по их линзам, но нарушают жёсткие критерии. Условный запасной у всех один и тот же — R2R1, если есть счёт.

**Где судьи разошлись и как я решил:**
- **Достаточно ли R1FY хорош.** Оценки 3, 3,5 и 5.
  - Судья по кодекам: для «любого исходника» — нет, только с прокси.
  - Судья по 4K: на грани.
  - Судья по рискам: да, на ближайшие 2 года.

  Все трое правы в своём. Для 4:2:0 в Premiere или Resolve Studio он годится, для HEVC 4:2:2 и бесплатного Resolve — только через прокси. Поэтому выбор оставлен, а риски вынесены в «Что теряем» и «Что сделать при покупке».
- **Важен ли HEVC-кодек Windows.** Судья 3 считает, что для Premiere и Resolve он не нужен ([hevc-amd.md](AMD/notes/hevc-amd.md), §5). Судья 1 — что бесплатный Resolve открывает только «OS-supported» профили, а без расширения HEVC не откроется ни он, ни «Фото».
  Правы оба: Premiere и Resolve Studio декодируют сами, а бесплатный Resolve читает только «OS-supported» профили ([Blackmagic](https://documents.blackmagicdesign.com/SupportNotes/DaVinci_Resolve_21_Supported_Codec_List.pdf)). Что ему нужно именно расширение Windows — вывод, не проверено. Лечится бесплатно ([Microsoft Store](https://apps.microsoft.com/detail/9N4WGH0Z6VHQ)).
- **Проверять ли до оплаты.** Судья 1 предлагает запустить DXVA Checker в магазине до оплаты, судья 3 — позвонить и спросить про Umtausch.
  Новый ноутбук в запечатанной коробке до оплаты обычно не проверить (мой вывод). Поэтому главное — заранее узнать условия обмена в своём рынке, а проверки сделать в первый день.
- **Medion.** Судьи 1 и 2 дают ему 6–6,5 (HEVC 4:2:2 аппаратно, Arc 130V, 2,8K OLED), судья 3 — 3 (дороже потолка, риск неизвестен, вопросы к аккумулятору). Он всё равно выше потолка, поэтому остаётся справкой.

## Почему AMD, а не Intel

- **Ответ на вопрос «Intel или AMD» в этот раз — AMD, но только потому, что прошёл один AMD.** По силе и по кодекам Intel в бюджете был бы лучше: HEVC 4:2:2 он декодирует аппаратно, AMD — нет ([perf-tables.md](AMD/notes/perf-tables.md), §4).
- **У Intel до 1100 € за наличные нет ни одного ноутбука с полным sRGB** ([screen-oled.md](AMD/notes/screen-oled.md), [screen-ips.md](AMD/notes/screen-ips.md)):
  - Medion `30040202` (Lunar Lake) — 1199,99 € наличными;
  - Aspire 16 AI OLED A16-52M-75LW (258V) — 1143 € переводом ([idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/207120152_-aspire-16-ai-a16-52m-75lw-acer.html));
  - ThinkPad E16 G3 2,5K `22AY004XGE` — 1584,24 € ([idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/209382346_-thinkpad-e16-g3-22ay004xge-lenovo.html));
  - HP OmniBook 7 16 с 2,5K 100 % sRGB есть в даташите, но в Германии не продаётся.
  - Все Intel до 1100 € — с IPS «45 % NTSC» или 62,5 % sRGB.
- **У AMD экран есть у двух Acer OLED.** Наличными из них можно купить только Swift Air R1FY; R2R1 — только переводом ([display-sweep.md](AMD/notes/display-sweep.md)).

## Почему прежний выбор отменён

- Вечером 30.09 выбор был **HP OmniBook 7 16 `BM9T4EA#ABD`** (979,30 €), запасной — **IdeaPad `83HS00BLGE`**, «если главное экран» — **R2R1**. Тогда экран и способ оплаты жёсткими критериями не были.
- **Экран стал жёстким критерием** (полный sRGB). HP (62,5 % sRGB), `83HS00BLGE` (замер 57,7 %) и AMD №1 `83HY008CGE` (57,6 %) выпали ([displays.md](AMD/notes/displays.md)).
- **Оплата стала только наличными.** HP продаёт только hp.com — там PayPal, карта, Klarna, а на idealo Vorkasse ([HP](https://www.hp.com/de-de/shop/faq/payment)). R2R1 за наличные ≤ 1100 € не найден.
- Остался один ноутбук — Swift Air R1FY.

## Что сделать при покупке

**До поездки:**
1. На [странице expert](https://www.expert.de/shop/unsere-produkte/computer-zubehor/notebooks/laptops/17041266033-swift-air-16-oled-silber-16-zoll-wuxga-amd-ryzen-ai-5-330-32-gb-1024-gb-ssd-amd-radeon-820m.html) выбрать свой рынок. Проверить цену (999,99 €) и кнопку «Reservieren». Цена выше 1100 € или товара нигде нет — пересчитать варианты.
2. Позвонить в рынок и спросить три вещи:
   - есть ли `NX.DL5EG.002`;
   - можно ли заплатить наличными;
   - какие условия добровольного обмена или возврата.
3. В магазине сверить на коробке: SFA16-61M-R1FY / `NX.DL5EG.002`, OLED, 32 ГБ, 1 ТБ. Сохранить чек — это Gewährleistung на 2 года.

**В первый день:**
4. Обновить Windows и BIOS до 1.07 («Modify fan table», [Acer Support](https://www.acer.com/de-de/support/product-support/SFA16-61M)). Послушать, шумит ли вентилятор в простое.
5. **DXVA Checker → Decoder Devices.** Должны быть `HEVC_VLD_Main`, `HEVC_VLD_Main10` и AV1. Профилей 4:2:2 у AMD нет — это нормально ([hevc-amd.md](AMD/notes/hevc-amd.md)).
   Если HEVC не открывается в «Фото» или бесплатном Resolve, поставить «HEVC-Videoerweiterungen vom Gerätehersteller» (0 €, [Microsoft Store](https://apps.microsoft.com/detail/9N4WGH0Z6VHQ)).
6. **Кодирование:** в HandBrake запустить короткий экспорт пресетом «H.265 VCN 2160p 4K» ([HandBrake](https://handbrake.fr/docs/en/latest/technical/video-vcn.html)).
7. **Двухканал.** Память распаяна, так что одноканал здесь исключён конструкцией. Для контроля — HWiNFO или CPU-Z: 32 ГБ LPDDR5, суммарная ширина шины 128 бит (у LPDDR5 она бывает разбита на несколько каналов по 16/32 бит; это мой вывод).
8. **Экран:**
   - Поискать режим или профиль sRGB — в утилите Acer и в «Параметры → Дисплей». Есть ли он у этой модели — не проверено. Без него sRGB-материал на панели со 100 % DCI-P3 выглядит перенасыщенным.
   - В Resolve включить управление цветом экрана. Resolve под Windows сам не применяет ICC-профиль ([форум Blackmagic](https://forum.blackmagicdesign.com/viewtopic.php?uid=16&f=21&t=133034&start=0)). Точный цвет даст только калибровка колориметром.
   - ШИМ: на яркости 20–30 % снять экран замедленной съёмкой телефона. LaptopMedia пишет «begrenzte Amplitude», частоту никто не мерил.
9. **Монтаж:** при подтормаживании сразу переходить на прокси и таймлайн 1080p.
   - Premiere по умолчанию делает прокси в половинном разрешении в ProRes Proxy ([Adobe](https://helpx.adobe.com/premiere/desktop/organize-media/ingest-proxy-workflow/create-proxies.html)).
   - В Resolve — Proxy / Optimized Media в ProRes или DNxHR ([Blackmagic](https://documents.blackmagicdesign.com/SupportNotes/DaVinci_Resolve_21_Supported_Codec_List.pdf)).

## Ветки и заметки

- Intel — [Intel/REPORT.md](Intel/REPORT.md); AMD и сравнение веток — [AMD/REPORT.md](AMD/REPORT.md). Их топы составлены до новых жёстких критериев — см. вставки в начале обоих отчётов.
- Производительность — [AMD/notes/perf-tables.md](AMD/notes/perf-tables.md). Надёжность и запчасти — [AMD/notes/reliability.md](AMD/notes/reliability.md).
- Экран и наличные: [screen-oled.md](AMD/notes/screen-oled.md), [screen-ips.md](AMD/notes/screen-ips.md), [screen-gaming.md](AMD/notes/screen-gaming.md), [screen-verify-1.md](AMD/notes/screen-verify-1.md), [display-sweep.md](AMD/notes/display-sweep.md), [displays.md](AMD/notes/displays.md).
- Оценки кандидатов — [screen-scores.md](AMD/notes/screen-scores.md).
- Черновик итога 30.09 (тогда выбран R2R1) и доводы судей того раунда — [AMD/notes/final-draft-judges.md](AMD/notes/final-draft-judges.md). Итог 30.09 с выбором HP — [AMD/notes/report-2026-09-30-hp.md](AMD/notes/report-2026-09-30-hp.md).
- Ничего не покупали, в аккаунты не входили, продавцам не писали.
