## Проверка acer-medion-misc

_Проверено 30.09.2026, облачная сессия, скептическая перепроверка._

**SKU:** Acer TravelMate P4 16 NX.B9BEG.002; Acer Aspire 16 AI OLED NX.JP1EG.00W и NX.JP1EG.007; Medion E15433 MD600023; Medion SPRCHRGD 16 S1 OLED 30040200 (MD62744); Captiva Power Starter I82-531; Wortmann TERRA MOBILE 1516R 1220844.

**Источники:**
- Даташиты Acer (зеркала gzhls.at / media.bechtle.com), Icecat (open) по коду и EAN, сайты medion.com и wortmann.de, руководство Medion E15433.
- Карточки магазинов: expert.de, Cyberport, Alternate, nexoc-store.de.
- Цены — billiger.de. История — полная дневная серия из слоя «Weitere Details»: серия `billiger` без маркетплейсов, 01.04–30.09.2026.
- Всё «из облака — перепроверить на idealo».

### Вывод

1. **Сегодня в 1100 € с подтверждённой раскладкой — только TERRA 1516R.** 1×16 + свободный слот — так написано у самого Wortmann. Итог с планкой DDR4 **931,79 €**. Но CPU i5-1334U (Raptor Lake-U) для 4K слабый.
2. **Medion E15433 MD600023 — 699,97 € (Expert, в наличии), раскладка по-прежнему НЕ проверена.** Даташита на этот SKU нет. 2×16 выведено по брату MD62727 (i5-1334U): medion.com пишет «2 x, davon 2 x belegt», Icecat — «2 x 16 GB». Для MD600023 это **не проверено**. → проверено в браузере 30.09.2026: (п. 4.1) МЕНЯЕТ ВЫВОД (условность снимается): MD600023 = MSN 30041451 — 2×16 DDR4-3200, оба слота заняты (Medion); SSD 1 ТБ, 1,81 кг, блок 65 Вт, HDMI 1.4b, Wi-Fi 5, без подсветки; батарея 55 Втч (idealo); яркость Medion не публикует; срок гарантии — «по гарантийной карте», вопрос продавцу ([service.medion.com](https://service.medion.com/de/product-detail/30041451)).
3. **Captiva I82-531 — 916,02 € (nexoc-store.de) / 987,12 € (billiger, Galaxus).** 2×16 — только «по логике»: у Cyberport «2 слота, свободно 0». У производителя не подтверждено (captiva-power.de блокирует ботов, Icecat закрыт: 403). CPU 12-го поколения. → проверено в браузере 30.09.2026: (п. 4.4) Captiva I82-531GE: DDR4-3200 (не 2400), 2 слота, раскладка не указана; HDMI 2.1; SSD 1 ТБ, свободный M.2 не указан; яркость и охват не указаны. Раскладку — спросить Captiva или продавца ([captiva-power.de](https://www.captiva-power.de/produkte/business-office-notebook/business-office-i82-531ge)).
4. **Acer TravelMate P4 16 NX.B9BEG.002 — купить негде.**
   - Cyberport: 1066,32 € «Nicht verfügbar». ARLT: «Artikel nicht mehr verfügbar». На billiger и в Alternate SKU нет.
   - 2×16 — «вероятно»: Icecat пишет «2 x 16 GB». Даташит Acer соседнего NX.B9BEG.004 — «Memory configuration 2 x 16 GB». У Cyberport — «свободно 1», это противоречие.
5. **B-список (распайка, Lunar Lake 258V) — сегодня всё дороже 1100 €.**
   - Medion 30040200 — **1299 €**. Минимум за 6 мес. — **999 €**; ≤ 1100 € было 99 дней из 183, последний раз 09.08.
   - Aspire 16 AI NX.JP1EG.007 — 1143 €. ≤ 1100 € было только в апреле.
   - NX.JP1EG.00W — 1125,51 € (pc-seller.de). В Alternate 1032 €, но «nicht kaufbar».
6. **HEVC.**
   - Acer — **высокий риск**: с 22.06.2026 Acer продаёт в DE часть устройств «без HEVC-кодека», см. `hevc-audit.md`.
   - Medion, Captiva, Wortmann — данных нет, в списке лицензиатов HEVC Advance их нет. Acer и «Lenovo PC HK» в списке есть ([Access Advance](https://accessadvance.com/hevc-advance-patent-pool-licensees/)).
   - У всех — проверка DXVA Checker'ом в срок возврата.

### Опровергнуто / исправлено

- **TERRA 1516R: «за 6 мес. 840–899 €» (`sweep-16gb-plus-stick.md`) — неверно.**
  - Полная серия billiger: минимум **775,00 €** (01–06.04.2026), помесячно 783–793 €. С 10.09 по 23.09 предложений не было.
  - 840–899 € — это линия-интерполяция пропуска (`billiger_missing`), а не цены. При разборе billiger брать серию `billiger`, а `*_missing` игнорировать.
- **Aspire 16 AI NX.JP1EG.00W: «RJ45 (Icecat)» — неверно.**
  - Даташит Acer (07.11.2025): «LAN -», «Ethernet (RJ-45) -».
  - В сборнике обзоров Notebookcheck по A16-52M Ethernet тоже нет.
  - Icecat ошибается («Ethernet/LAN: Ja»).
- **Aspire 16 AI NX.JP1EG.007: «1150 € Alternate» устарело.** Сейчас в Alternate «Artikel kann derzeit nicht gekauft werden» (B-Ware от 959 €). Апрельские 1090,99 € (21–30.04) и 750 € (02–03.04) подтверждаются полной серией billiger.
- **Medion 30040200:** «гарантия — не проверено» → **24 месяца** (medion.com, Icecat). Блок питания в комплекте: «externes Type-C Netzteil» (medion.com).
- **Captiva I82-531:**
  - «Батарея не указана» → **47 Втч, 4 ячейки, блок питания 45 Вт в комплекте** (nexoc-store.de).
  - Шасси — Clevo NJ56PU («BJ5 70IO 23V1»), есть DVD-RW и кардридер 6-в-1 (SD).
  - Частота памяти противоречит: Cyberport — 2400 МГц, Nexoc — 3200.
  - HDMI: у Captiva — 2.1 (Cyberport, Nexoc), у TERRA в том же по размерам шасси — 1.4b. Не проверено. → проверено в браузере 30.09.2026: (п. 4.4) см. строку 17 ([captiva-power.de](https://www.captiva-power.de/produkte/business-office-notebook/business-office-i82-531ge)).
- **TravelMate NX.B9BEG.002:** батарея 53 Втч (Icecat) или 65 Втч (Cyberport; даташит .004 — 65 Втч) — для .002 **не проверено**. Wi-Fi: Icecat — 6, Cyberport и даташиты соседних SKU — 6E. Текст Cyberport скопирован с P4 Spin («2-in-1 Convertible»), данные магазина неаккуратные. → проверено в браузере 30.09.2026: (п. 4.3) Даташит Acer NX.B9BEG.002: 2×16 DDR5, до 64 ГБ; IPS «100 % sRGB», 60 Гц; 53 Втч, Wi-Fi 6E, 1,65 кг; яркость, матрица и свободный M.2 не указаны. SKU не продаётся (на idealo нет, geizhals — «nicht verfügbar») ([gzhls.at](https://gzhls.at/blob/ldb/5/b/5/2/ff521cb8ef682d46e1ca48496a70e8b2e668.pdf)).
- **Alternate о TERRA 1516R (1220844) пишет «500 GB SSD» и «16:10».** Это противоречит Wortmann и Icecat (1 ТБ, 16:9). Если брать в Alternate — уточнить.

### Сводная таблица (30.09.2026)

| SKU | CPU (класс) | ОЗУ | БП | Цена сейчас | Мин. 6 мес. | Итог | Держать? |
|---|---|---|---|---|---|---|---|
| TERRA 1516R 1220844 | i5-1334U, Raptor Lake-U (старый) | 1×16 DDR4 + свободный слот ✅ (Wortmann) | ✅ | 818,62 € JB-Computer, 1–2 дня | 775,00 € (01–06.04) | 818,62 + 113,17 = **931,79 €** | B16, низкий приоритет |
| Medion E15433 MD600023 | i7-13620H, Raptor Lake-H (старше, но ок; UHD 64 EU) | 32 DDR4, раскладка **не проверена** | ✅ | 699,97 € Expert, 1–3 дня | 658,46 € (04.08) | **699,97 €** | условно: сначала подтвердить 2×16 |
| Captiva I82-531 | i7-1255U, Alder Lake-U (устаревший) | 32 DDR4, 2 слота, свободно 0 (Cyberport) — вероятно 2×16 | ✅ 45 Вт | 916,02 € nexoc-store / 987,12 € Galaxus | 881,53 € (13–14.06) | **916,02 €** | нет: вытеснен E15433 и TERRA |
| Acer TravelMate P4 16 NX.B9BEG.002 | Ultra 5 125U, Meteor Lake-U (современный) | 2×16 DDR5 — вероятно | ✅ | 1066,32 € Cyberport, **нет в наличии** | нет на billiger | 1066,32 € | следить |
| Medion SPRCHRGD 16 S1 30040200 | Ultra 7 258V, Lunar Lake | 32 LPDDR5X на корпусе (B) ✅ | ✅ USB-C | 1299 € coolblue, 1 день | **999 €** (16.06–24.06, 16.07–09.08) | 1299 € | B, алерт ≤ 1050–1100 € |
| Acer Aspire 16 AI NX.JP1EG.007 | Ultra 7 258V, Lunar Lake | 32 LPDDR5X (B) ✅ | ✅ 65 Вт | 1143 € Galaxus (6–8 дн.) / Amazon MP «cyberport» | 1090,99 € (21–30.04); 750 € 02–03.04 — вероятно ошибка | 1143 € | нет: вытеснен 30040200 |
| Acer Aspire 16 AI NX.JP1EG.00W | Ultra 7 258V, Lunar Lake | 32 LPDDR5X (B) ✅ (Acer) | ✅ 65 Вт | 1125,51 € + доставка, pc-seller.de | нет на billiger; NBC 20.04.2026: 1029 € | ≥ 1125,51 € | следить ≤ 1050 € |

Планка DDR4: G.Skill F4-3200C22S-16GRS — 113,17 € (JB-Computer, JACOB), минимум за 6 мес. 94,99 € — [billiger](https://www.billiger.de/products/2436174330-g-skill-ripjaws-ddr4-3200-16gb-modul-1x16gb-so-dimm-cl22-f4-3200c22s-16grs).

### По SKU

#### Wortmann TERRA MOBILE 1516R — 1220844 (EAN 4039407085040)
- **Производитель ✅** [wortmann.de](https://www.wortmann.de/de-de/product/aa_terra_mobile_nb/1220844/terra-mobile-1516r.aspx):
  - i5-1334U; 16 ГБ DDR4, **«Speicherkartensteckplätze: 2 Sockel, 1 x davon frei»**, макс. 64 ГБ;
  - iGPU «Iris Xe (if in dual-channel memory mode)» — с одной планкой работает как UHD;
  - 1 ТБ NVMe: «1 x M.2 2280 SSD, SATA/PCIe Gen4x4 + 1 x SATA (7mm HDD/SSD)»;
  - 15,6" FHD, Non Glare, 16:9; тип матрицы, яркость и охват не указаны;
  - «Zubehör im Lieferumfang: Netzteil, Stromkabel»; в аксессуарах к 1516R — «Netzteil 45W», мощность штатного БП напрямую не указана;
  - 47 Втч (на батарею гарантия 6 мес.), 2,2 кг;
  - USB-C 3.2 Gen2 (DP + PD), HDMI 1.4b, VGA, RJ45, кардридер 6-в-1, DVD±RW;
  - гарантия 24 мес. Pickup; UVP 909 €.
- **Icecat ✅** [по EAN](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&GTIN=4039407085040): «Speicherlayout 1 x 16 GB», «2x SO-DIMM», «AC-Netzadapter: Ja».
- **Alternate** [100195479](https://www.alternate.de/TERRA/MOBILE-1516R-i5-1334U-W11P-Notebook/html/product/100195479): «2 Speicherbänke vorhanden, davon belegt 1»; 840 € + 7,99 €, «Sofort verfügbar». ⚠️ Там же «500 GB SSD» и «16:10» — противоречие.
- **Цена** ([billiger](https://www.billiger.de/pricelist/5439679499-wortmann-terra-mobile-1516r-intel-core-i5-1334u-16-gb-ram-1-tb-ssd-win11-pro)):
  - 818,62 € — JB-Computer, 1–2 рабочих дня, без доставки;
  - 844,90 € — Heinzsoft; 847,99 € — Alternate; 849 € — Galaxus;
  - минимум за 6 мес. 775,00 € (01–06.04).
- Обзоров 1516R не нашёл. Шасси Clevo: Wortmann продаёт модуль «RAM SO-DIMM DDR4 16GB / PC3200 / Clevo».

#### Medion E15433 — MD600023 (EAN 4061275247398)
- **Даташит ❌.** На medion.com этого SKU нет (поиск по сайту), Icecat по EAN — 400, по коду — 404.
- **Карточка expert.de ✅** [expert.de](https://www.expert.de/shop/unsere-produkte/computer-zubehor/notebooks/laptops/17040046553-e15433-md600023-grau-15-6-zoll-full-hd-intel-core-i7-13620h-1-tb-ssd-32-gb-ddr4-intel-uhd.html):
  - i7-13620H; 32 ГБ DDR4 — **раскладки нет**;
  - 1 ТБ M.2; 15,6" FHD **IPS**;
  - 1× USB-C 2.0, 2× USB-A 5 Гбит/с, 1× USB-A 2.0, HDMI (версия не указана), microSD, DC-IN;
  - Wi-Fi AC 9461, BT 5.1; 55 Втч; 1,8 кг; 35,9×2,06×24 см;
  - «Lieferumfang: … externes Netzteil».
- **Брат MD62727** (i5-1334U, 30040188): «RAM-Steckplätze: 2 x, davon 2 x belegt», те же размеры, вес, батарея 55 Втч и порты — [medion.com](https://www.medion.com/de/shop/p/einsteiger-notebooks-medion-medion-e15433-laptop-intel-core-i5-1334u-windows-11-home-39-6-cm-15-6--fhd-display-1-tb-ssd-32-gb-ram-30040188A1). По Icecat у него «2 x 16 GB» — [Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Medion&ProductCode=30039505). Для MD600023 вывод по аналогии — **не проверено**. → проверено в браузере 30.09.2026: (п. 4.1) см. строку 16 ([service.medion.com](https://service.medion.com/de/product-detail/30041451)).
- **Руководство E15433** ([PDF](https://cdn.medion.com/downloads/anleitungen/bda_e15433_de.pdf), редакция 19.09.2023): блок питания Chicony A18-065N3A, **65 Вт**, 19 В 3,42 А. Для H-процессора (база 45 Вт) это может ограничивать мощность. Относится ли руководство к MD600023 — **не проверено**. О раскладке памяти в руководстве ничего нет. → проверено в браузере 30.09.2026: (п. 4.1) см. строку 16 ([service.medion.com](https://service.medion.com/de/product-detail/30041451)).
- **Цена** ([billiger](https://www.billiger.de/products/5438984171-medion-e15433-15-6-intel-core-i7-13620h-32-gb-ram-1-tb-ssd-win11-home)): 699,97 € — Expert, 1–3 рабочих дня; 739,99 € — expert на OTTO; 857,99 € — Kaufland. Минимум за 6 мес. 658,46 € (04.08).
- Обзора Notebookcheck нет. Новость NBC про MD62727: у USB-C нет ни PD, ни DP Alt-Mode — [NBC](https://www.notebookcheck.com/Core-i5-32-GB-RAM-1-TB-SSD-Medion-Office-Notebook-im-Angebot.1299080.0.html).
- Покупателям на medion.com (MD62727) иногда мешает шумный вентилятор.
- Гарантия 24 мес. — у MD62727; у MD600023 не проверено. → проверено в браузере 30.09.2026: (п. 4.1) см. строку 16 ([service.medion.com](https://service.medion.com/de/product-detail/30041451)).

#### Captiva Power Starter I82-531 (арт. 82531, EAN 4046373825310)
- **Производитель ❌:** captiva-power.de отвечает «BOTS NOT WELCOME», защиту не обходил. Icecat — 403. → проверено в браузере 30.09.2026: (п. 4.4) см. строку 17 ([captiva-power.de](https://www.captiva-power.de/produkte/business-office-notebook/business-office-i82-531ge)).
- **Cyberport** [1C05-986](https://www.cyberport.de/notebook-und-tablet/notebooks/captiva/pdp/1c05-986/captiva-power-starter-laptop-i82-531-15-6-fhd-intel-i7-1255u-32gb-1tb-ssd-win11.html):
  - DDR4, «RAM-Steckplätze gesamt: 2, frei: 0», «2400 MHz»;
  - IPS, матовый; HDMI 2.1; VGA; RJ45; SD;
  - 45 Вт; 2,1 кг;
  - 989 €, «In 2–4 Tagen verfügbar».
- **nexoc-store.de** [страница](https://www.nexoc-store.de/notebooks/office-notebooks/captiva-notebook-power-starter-i82-531-i7-1255u-15.6-32gb-1tb-ssd-intel-iris-xe-graphics-dvd-rw-win-11-home):
  - barebone Clevo NJ56PU («BJ5 70IO 23V1»); «Memory: 32GB DDR4 SO-DIMM», 2 слота, 3200 МГц — раскладки нет;
  - 1 ТБ M.2 2280 PCIe Gen4 x4; DVD-RW;
  - кардридер 6-в-1; USB-C Gen2 с DP и PD; RJ45; VGA; HDMI;
  - 47 Втч; «AC Adapter: 45W», «Netzteil inkl.: ja»; 361×256×24,1 мм;
  - **916,02 €**, доставка бесплатно, «2–3 Werktage nach Zahlungseingang».
- **Цена на billiger** ([billiger](https://www.billiger.de/pricelist/5369460567-captiva-i82-531-15-6-intel-core-i7-1255u-32-gb-ram-1-tb-ssd)): 987,12 € — Galaxus, 1–3 рабочих дня; 995,99 € с доставкой; 1009 € — OTTO. Минимум за 6 мес. 881,53 € (13–14.06). Nexoc на billiger нет.
- Обзоров нет.

#### Acer TravelMate P4 16 TMP416-53-TCO-56JM — NX.B9BEG.002 (EAN 4711474155894)
- **Даташит Acer на .002 не найден** (acer.com из облака закрыт). → проверено в браузере 30.09.2026: (п. 4.3) см. строку 46 ([gzhls.at](https://gzhls.at/blob/ldb/5/b/5/2/ff521cb8ef682d46e1ca48496a70e8b2e668.pdf)).
- **Icecat ✅** [NX.B9BEG.002](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Acer&ProductCode=NX.B9BEG.002):
  - «Speicherlayout 2 x 16 GB», 2× SO-DIMM, макс. 64 ГБ, «Zweikanalig»;
  - 1 ТБ PCIe 4.0; IPS, матовый, «sRGB 100 %»;
  - 53 Втч (3 ячейки); 65 Вт; «AC-Netzadapter: Ja»;
  - 2× USB4/TB4, HDMI 2.1, RJ45, microSD; 1,65 кг.
- **Даташит Acer соседнего NX.B9BEG.004** (155U, 32/1 ТБ) — [Bechtle](https://media.bechtle.com/asrc/180712/1c4b3d4ee288fc9434f5175bf56070570/c3/-/68ebba79c1864af9a9c96cccac8eb886/acer-travelmate-p4-16-u7-32gb-1tb-data-sheet-1):
  - «Memory configuration 2 x 16 GB DDR5 RAM»;
  - «ComfyView WUXGA IPS display with 100% sRGB»;
  - 65 Втч; «USB Type-C 100W PD AC Adapter»; Wi-Fi 6E.
- **Лист платформы TMP416-53** (U5, 16/512) — [Bechtle](https://media.bechtle.com/asrc/180712/1c4b3d4ee288fc9434f5175bf56070570/c3/-/0fc5829930764d98a557d7585356c4be/acer-travelmate-p4-tmp416-53-u5-16-512gb-datenblatt-1): 400 нит, sRGB 100 %, 65 Вт USB-C, 53 Втч.
- **Cyberport** [1C25-4A8](https://www.cyberport.de/notebook-und-tablet/notebooks/acer/pdp/1c25-4a8/acer-travemate-p4-mp416-53-tco-56jm-16-u5-125u-32gb-1tb-w11pro.html): 1066,32 €, «Nicht verfügbar», «RAM-Steckplätze frei: 1» (противоречие), 65 Втч, Wi-Fi 6E.
- ARLT: «Artikel nicht mehr verfügbar» — [arlt.com](https://arlt.com/Notebook/Notebooks/Acer-TravelMate-P4-TMP416-53-TCO-56JM-WUXGA-16-Zoll-Laptop.html). На billiger нет.
- Обзора TMP416-53 у Notebookcheck нет.
  - У предшественника TMP416-51 (другое поколение и панель BOE) NBC намерил 269 нит, 58,1 % sRGB, контраст 882:1; частоты под длительной нагрузкой проседают — [NBC](https://www.notebookcheck.net/Acer-TravelMate-P4-TMP416-51-Review-Lightweight-office-laptop-with-endurance-and-power.704827.0.html).
  - На TMP416-53 это не переносить.

#### Medion SPRCHRGD 16 S1 OLED — 30040200 / MD62744 (EAN 4061275241600)
- **medion.com ✅** [страница](https://www.medion.com/de/shop/p/multimedia-notebooks-medion-sprchrgd-16-s1-oled-copilot-pc-intel-core-ultra-7-258v--windows-11-home-40-6-cm-16--2-8k-oled-display-1-tb-ssd-32-gb-ram-30040200A1) ([PDF](https://media.medion.com/prod/medion/de_DE/0781/0810/0773/30040200.pdf)):
  - 258V; 32 ГБ LPDDR5x; 1 ТБ PCIe4;
  - 16" OLED 2880×1800, 120 Гц, 500 нит, 100 % DCI-P3;
  - «externes Type-C Netzteil» (мощность не указана);
  - 1× USB4, 1× USB-C 5 Гбит/с, 2× USB-A 5 Гбит/с, 1× USB-A 2.0, HDMI 2.0, microSD;
  - гарантия 24 мес.; на medion.com «Ausverkauft» (UVP 1399,95 €).
- **Icecat ✅** [по EAN](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&GTIN=4061275241600): 80,5 Втч, 1,49 кг, алюминий.
- **Цена** ([billiger](https://www.billiger.de/products/5357141091-medion-sprchrgd-16-s1-oled-intel-core-ultra-7-258v-32-gb-ram-1-tb-ssd-win11-home)):
  - 1299 € — coolblue, 1 рабочий день; 1354,98 € — Energeto; 1590,99 € — Kaufland;
  - минимум за 6 мес. **999 €** (08.05–24.06 и 16.07–09.08); ≤ 1100 € — 99 дней из 183.
- **Известные проблемы:**
  - heise (17.07.2026) в подзаголовке: «Wenn da nur kein Akkuproblem wäre». Суть — за пейволом: по сниппету поиска, заряд застревает на ~89 %, **не проверено** — [heise](https://www.heise.de/tests/Viel-RAM-fuers-Geld-Mittelklassenotebook-Medion-Sprchrgd-16-S1-im-Test-11354704.html). → проверено в браузере 30.09.2026: (п. 5.26) heise: видны подзаголовок «Wenn da nur kein Akkuproblem wäre» и раздел «89-Prozent-Akku» (c't 17/2026), суть — за пейволом heise+; тестировали 228V / 512 ГБ, не 30040200. Вопрос пользователю: есть ли heise+ или номер c't 17/2026 ([heise.de](https://www.heise.de/tests/Viel-RAM-fuers-Geld-Mittelklassenotebook-Medion-Sprchrgd-16-S1-im-Test-11354704.html)).
  - netzwelt (MD62745, 288V): сильные блики, «blecherne» динамики, нет Ethernet — [netzwelt](https://www.netzwelt.de/medion-sprchrgd-16-s1-oled/testbericht.html).
  - Покупатели на medion.com: реальная автономность далека от «19 ч», клавиатура так себе.

#### Acer Aspire 16 AI OLED A16-52M-75LW — NX.JP1EG.007 (EAN 4711474611390)
- **Icecat ✅** [NX.JP1EG.007](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Acer&ProductCode=NX.JP1EG.007):
  - 258V; 32 ГБ LPDDR5x «On-board», макс. 32 ГБ;
  - OLED 2048×1280, 120 Гц, 100 % DCI-P3;
  - 2× USB4/TB4, HDMI 2.1, microSD; 65 Втч; 65 Вт; «AC-Netzadapter: Ja»; QWERTZ.
- expert.de: «Lieferumfang: … USB-C 65W Netzteil» — [expert](https://www.expert.de/shop/unsere-produkte/computer-zubehor/notebooks/laptops/17040408024-aspire-16-ai-oled-a16-52m-75lw-16-zoll-wuxga-intel-core-ultra-5-226v-16-gb-1-tb-m-2-ssd.html). В URL expert написано «Ultra 5 226V 16 GB», а в характеристиках — 258V/32 ГБ: ошибка в URL.
- **Цена** ([billiger](https://www.billiger.de/products/5329156961-acer-aspire-16-ai-oled-a16-52m-75lw-intel-core-ultra-7-258v-32-gb-ram-1-tb-ssd)):
  - 1143 € — Galaxus (6–8 рабочих дней) и Amazon MP «cyberport» (в наличии); 1198,37 € — Cyberport;
  - в Alternate купить нельзя;
  - за 6 мес.: 750 € (02–03.04, вероятно ошибка), 1090,99 € (21–30.04), с мая ≥ 1143 €.
- Обзоры A16-52M (PC World, сборник NBC): слабая многопоточность, автономность ниже других Lunar Lake, глянцевые блики, RJ45 нет — [NBC](https://www.notebookcheck.net/Acer-Aspire-16-AI-A16-52M.1176237.0.html).

#### Acer Aspire 16 AI OLED A16-52M-70AJ — NX.JP1EG.00W (EAN 4711474850348)
- **Даташит Acer ✅** (07.11.2025) [PDF](https://gzhls.at/blob/ldb/0/9/4/1/b092f7130721353b3e3075dbc4bea5554aa6.pdf):
  - «Memory configuration 1 x 32 GB LPDDR5X (Onboard)», «not replaceable or expandable»;
  - OLED WUXGA 1920×1200, 95 % DCI-P3; частоту обновления даташит не называет, Icecat — 60 Гц;
  - **«LAN -» / «Ethernet (RJ-45) -»**; 2× USB4/TB4, HDMI 2.1, 2× USB-A Gen 2;
  - 65 Втч; «USB Type-C 65W power adapter»; «Warranty 2-year mail-in/return service»; сканера отпечатка нет.
- Icecat: 300 нит, 60 Гц, «Ethernet/LAN: Ja» — последнее неверно — [Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Acer&ProductCode=NX.JP1EG.00W).
- **Цена:**
  - на billiger нет;
  - Alternate — 1032 €, «Artikel kann derzeit nicht gekauft werden» — [Alternate](https://www.alternate.de/Acer/Aspire-16-AI-OLED-A16-52M-70AJ-Notebook/html/product/100211886);
  - pc-seller.de — 1125,51 € + доставка, «ca. 3–4 Werktage» — [pc-seller](https://pc-seller.de/produkt/acer-aspire-16-ai-oled-a16-52m-70aj-406cm-16-ultra-7-258v-32gb-1tb-w11/);
  - NBC 20.04.2026: 1029 € (computeruniverse, Cyberport) — [NBC](https://www.notebookcheck.com/2k-OLED-DCI-P3-Core-Ultra-7-1-TB-SSD-32-GB-RAM-Acer-Multimedia-Notebook-im-Angebot.1278385.0.html).

### Попутно (не проверено до конца)
- NBC 04.08.2026: Aspire 16 AI A16-52M с **Core Ultra 9 288V**, 32 ГБ, 1 ТБ, OLED 60 Гц 500 нит — **899 €** на Amazon.de ([NBC](https://www.notebookcheck.com/Deal-Acer-Aspire-16-AI-mit-OLED-Display-32-GB-RAM-und-1-TB-SSD-erreicht-Bestpreis.1359636.0.html)). Парт-номер не указан. На billiger есть A16-52M-984U / -92UY / -916J с 288V — кандидаты для B-списка, **не проверены**. → проверено в браузере 30.09.2026: (п. 1.20) МЕНЯЕТ ВЫВОД (B-список): Core Ultra H + 2×16 SO-DIMM + 1 ТБ ≤ 1100 € на idealo нет. Новое: HP OmniBook 7 AI 16-ay0770ng (BM9T4EA, 255H, 32 ГБ распайка, 1 ТБ) — 979,30 € (hp.com). X1607CA-MB120 32/1 ТБ — 1069,99 € (OTTO MP; у one.de 1039 €); AG16-71P-7607 — Core 7 150U (ловушка), 939,64 €; Aspire 16 AI 288V: -984U 1599 €, -916J от 1308,26 €, -92UY от 1348 €; Panther Lake со слотами ≤ 1100 € нет (21UR005AGE — 1205 €) ([idealo.de](https://www.idealo.de/preisvergleich/OffersOfProduct/206602335.html)).
- **Методика billiger:**
  - полный дневной ряд за 12 месяцев отдаёт слой «Weitere Details»: POST на URL товара с `?puzzle_command=refresh&puzzle_compo_ids=pricehistory_layer&render_params=%7B%7D`;
  - в данных несколько серий: `billiger` (магазины без маркетплейсов), `otto`, `kaufland`, `ebay`, `metro` (маркетплейсы) и `*_missing` (интерполяция пропусков);
  - если брать первую попавшуюся серию, можно получить пропуск вместо цен — так вышло с TERRA.
