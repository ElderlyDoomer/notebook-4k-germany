# Надёжность, ремонт и распространённость кандидатов (AMD, экран + наличные)

_30.09.2026, ~23:30–23:58. Пишется по ходу. Кандидаты: Acer Swift Air 16 OLED `NX.DL5EG.002` (прошёл всё, включая наличные) и Acer Aspire 16 AI OLED `NX.JP0EG.00Z` (для сравнения — только перевод/онлайн)._
_Оба — Acer, поэтому общий блок «бренд» один, дальше — по моделям._

## 0. Бренд Acer — общее для обоих

- **Надёжность (сводки).** Consumer Reports + PCMag Readers' Choice 2025 в пересказе BGR (13.01.2026), от лучших к худшим: Apple, LG, Microsoft, Samsung, Lenovo, MSI, ASUS, **Acer**, HP, Dell — Acer 8-й из 10 ([BGR](https://www.bgr.com/2072636/most-reliable-laptop-brands-ranked-worst-best/); сводка в [`Intel/notes/brands.md`](../../Intel/notes/brands.md)). Таблица CR по брендам за пейволлом ([CR](https://www.consumerreports.org/electronics-computers/laptops-chromebooks/most-reliable-laptop-brands-a1961456199/)).
- **Сервис в DE (опрос NBC 2024, >500 участников):** Acer — **3-е место** после Schenker/XMG и Apple ([NBC](https://www.notebookcheck.com/Umfrage-Service-und-Support-im-Reparaturfall-Diese-Laptop-und-Smartphone-Hersteller-koennen-nicht-ueberzeugen.905354.0.html)).
- **Запчасти через IPC (07/2026):** оценка 1,8; поставка ~8 дней; 93 % заказов за 30 дней; обещанный срок выполняется лишь в ~1/3 случаев; типичные дефекты — **петли и крышка экрана у Spin/Swift** ([IPC Acer](https://blog.ipc-computer.de/2026/07/acer-service/)).
- **Официальный срок выпуска запчастей:** публичных обязательств Acer не найдено ([`brands.md`](../../Intel/notes/brands.md), [`right-to-repair.md`](../../Intel/notes/right-to-repair.md)).
- **Сервис-мануалы:** «Offizielle Wartungsanleitungen sind seitens Acer jedoch nicht aufzufinden» ([NBC Aspire Go 15](https://www.notebookcheck.com/Guenstiger-Laptop-mit-guter-Leistung-Acer-Aspire-Go-15-im-Test.1092155.0.html)).
- **Французский индекс ремонтопригодности:** средний у Acer 6,87 (PIRG, данные 2021 — [BDM](https://www.blogdumoderateur.com/indice-reparabilite-apple-google-microsoft-pires-scores/)); Aspire 14 AI — 6,8, Aspire Go 16 — 7,1 ([LDLC](https://www.ldlc.com/fiche/PB00686783.html), [LDLC](https://www.ldlc.com/fiche/PB00724970.html)).
- **iFixit:** моделей Acer в таблице оценок нет ([iFixit](https://www.ifixit.com/repairability/laptop-repairability-scores)).
- **LVFS (прошивки под Linux):** 3 файла ([LVFS](https://fwupd.org/lvfs/vendors/)) — для Windows-пользователя не важно.
- **HEVC:** с 06.2026 часть немецких устройств Acer идёт «ohne vorinstallierten HEVC-Codec», модели не названы ([ChannelPartner](https://www.channelpartner.de/article/4187748/acer-und-asus-liefern-wieder.html), `hevc-amd.md` §5) — проверить DXVA Checker в срок возврата.

## Сырые данные: запчасти в IPC-Computer (30.09.2026, ~23:40, Chrome)

### Swift Air 16 SFA16-61M — [IPC](https://www.ipc-computer.de/acer/notebook/swift-serie/swift-air-16-sfa16-61m/)
Категории на странице модели: RAM (1 — «fest verlötet»), Displayeinheiten (1), Festplatten (4), Gehäuseteile (1), Kabel (2), Mainboards (3), Netzteile (3), Platinen (1), Tastaturen (1). **Аккумуляторов и вентиляторов в каталоге нет.**
| Деталь | Цена | Наличие |
|---|---|---|
| Блок питания USB-C 65 Вт оригинал / совместимые | 39,00 / 35,00 / 33,00 € | на складе |
| Дисплейный блок 16" WUXGA 1920×1200, глянец, серебро, **целиком** (матрица + крышка + кабель + рамка + **петли**), оригинал Acer; тип матрицы (OLED/IPS) не указан, глянец → скорее OLED ([товар](https://www.ipc-computer.de/acer/notebook/swift-serie/swift-air-16-sfa16-61m/displayeinheit-152880795)) | 225,00 € (+109 € установка) | «Nur noch 1 Stück auf Lager» |
| Топкейс с немецкой клавиатурой (COVER UPPER SILVER W-KB GERMAN, 6B.DJBNI.003) | 93,00 € | под заказ у Acer, 3–8 дней |
| Нижняя крышка (COVER LOWER SILVER) | 105,00 € | под заказ, 3–8 дней |
| Плата с CPU R5 330 и 32 ГБ распайки | 867,00 € (16 ГБ — 794 €) | под заказ, 3–8 дней |
| Wi-Fi/BT модуль (CTE 2x2 AX+BT) | 43,00 € | под заказ |
| Ремонт гнезда питания / платы (пауш.) в мастерской IPC | 159 / 489 € | 5–7 дней |

### Aspire 16 AI A16-61M — у IPC две страницы
- [«Aspire 16 (A16-61M)»](https://www.ipc-computer.de/acer/notebook/aspire-serie/16/aspire-16-a16-61m/) (варианты R2E7, R0G4, R4JE, R0VS, R0Q9, R8T1; 65 Вт·ч, БП 100 Вт): БП 65 Вт 39 €, вентилятор с радиатором «95W TDP original» 36 € («Nur noch wenige»), SSD, RAM «fest verlötet»; под заказ — странные позиции («CPU-Kühler LGA1156», заглушки D-SUB/HDMI — похоже на ошибку привязки).
- [«Aspire A16-61M»](https://www.ipc-computer.de/acer/notebook/aspire-serie/16/aspire-a16-61m/) (вариант R6CW): категорий много — Akkus 2, Displays 4, Displaykabel 3, Gehäuseteile 12, Lüfter 5, Lautsprecher 2, Mainboards 7, Platinen 7, Tastaturen 5.
| Деталь | Цена | Наличие |
|---|---|---|
| Аккумулятор 65 Вт·ч оригинал AP22ABN (11,61 В) / AP22A8N (15,52 В) | 94,00 € каждый | на складе |
| БП USB-C 65 Вт оригинал / 100 Вт оригинал / совместимые | 39,00 / 62,00 / 35,00 / 33,00 € | на складе |
| **Матрица Samsung 16" с креплением («Displaymodul SAMSUNG 16" mit Halterung»)** — вероятно OLED (Samsung Display), тип не указан | 333,00 € | под заказ у Acer, 3–8 дней |
| Матрицы IPS AUO / BOE 16" WUXGA (для IPS-версий) | 114,00 € | под заказ |
| Топкейс с немецкой клавиатурой | 74,00 € | под заказ, 3–8 дней |
| Вентиляторы 65×65×5 и 93×86×5 мм; радиаторы | 35,00 € / 38,00 € | под заказ |
| Вентилятор с радиатором (стр. A16-61M) | 36,00 € | «Nur noch wenige» |

## Сырые данные: разборка Swift Air 16 SFA16-61M — LaptopMedia DE (15.07.2026)
Источник — [LaptopMedia DE](https://laptopmedia.com/de/review/acer-swift-air-16-sfa16-61m-review-a-16-inch-laptop-that-weighs-under-1-kg/), раздел «Demontage, Aufrüstungsmöglichkeiten und Wartung» и «Design und Verarbeitung» (тестовый образец — AI 7 350 / 16 ГБ, OLED WUXGA; шасси то же).
- **Вскрытие:** 12 винтов Torx T6 + защёлки по периметру нижней крышки (нужна тонкая пластиковая лопатка); винты разной длины.
- **Меняется:** SSD (1× M.2 2280 PCIe 4.0 x4, один винт; **второго слота нет**), Wi-Fi (M.2 2230, Realtek RTL8852CE), вентилятор (один, «leicht zugänglich»), аккумулятор (50 Вт·ч, 3 ячейки, 11,61 В, 4306 мА·ч — **на винтах**, разъём на плате; рядом кабели динамиков — осторожно), динамики.
- **Не меняется:** CPU и RAM — распаяны.
- **Корпус:** магниево-алюминиевый сплав; «überraschend stabil», дно не прогибается; петли хорошо сбалансированы, открытие одной рукой, дисплей при печати не качается; угол открытия ~120°.
- Охлаждение: один вентилятор + одна тепловая трубка; 22 Вт в 30-мин стресс-тесте, 68 °C.

## Сырые данные: обзоры, дата выхода, поддержка ПО (30.09.2026, ~23:45)
- **Swift Air 16 SFA16-61M:** анонс на IFA 03.09.2025, «ab November 2025 erhältlich», от 879 € ([NBC News](https://www.notebookcheck.com/Acer-Swift-Air-16-Leichtester-16-Zoll-Laptop-aller-Zeiten-schlaegt-LG-Gram-und-startet-guenstig-mit-Ryzen-AI-300-Power.1102769.0.html)).
  Своего теста у NBC нет — только сборник от 29.11.2025 (плюсы — вес, экран; минус — 50 Вт·ч) ([NBC](https://www.notebookcheck.com/Acer-Swift-Air-16-SFA16-61M.1173568.0.html)). Полный тест — LaptopMedia DE 15.07.2026 (выше).
  Hands-on WinFuture 11.09.2025: корпус «wirkt … weniger hochwertig als bei schwereren Metall-Ultrabooks», клавиши тесно, ход клавиатуры средний ([WinFuture](https://winfuture.de/videos/Hardware/Swift-Air-16-Sehr-leichtes-16-Zoll-Notebook-mit-Schwaechen-27897.html)).
  Поддержка Acer DE: 12 драйверов, BIOS 1.04 (04.12.2025) → 1.06 (03.08.2026, «enhance system performance») → **1.07 (24.09.2026, «Modify fan table»)**; документы — только User Manual, **сервис-мануала нет** ([Acer Support SFA16-61M](https://www.acer.com/de-de/support/product-support/SFA16-61M)).
- **Aspire 16 AI A16-61M:** у NBC — только сборник из 2 внешних тестов ([NBC](https://www.notebookcheck.net/Acer-Aspire-16-AI-A16-61M.1237489.0.html)):
  - TechRadar, 26.01.2026, 60 %, образец **Ryzen AI 7 350** / 16 ГБ: «somewhat flimsy build quality … a fair amount of flex to the chassis, while the lid hinge doesn't offer the greatest stability»; USB-C спереди (кабель зарядки пересекает USB-A), кардридер только microSD ([TechRadar](https://www.techradar.com/computing/windows-laptops/acer-aspire-16-ai-review)).
  - Trusted Reviews, 15.12.2025, AI 7 350, 2K 120 Гц OLED: плюсы — CPU, OLED, порты; минусы — «generic» корпус, слабая автономность; корпус алюминиевый ([Trusted Reviews](https://www.trustedreviews.com/reviews/acer-aspire-16-ai)).
  - LaptopMedia — только страница серии, **теста и разборки нет** ([LaptopMedia](https://laptopmedia.com/de/series/acer-aspire-16-ai-a16-61m/)). Compuram: RAM «fix onboard», совместимы M.2-SSD ([Compuram](https://www.compuram.de/arbeitsspeicher/acer/notebook/aspire/16-ai/a16-61m/0-00-1ae6a.htm)); число M.2-слотов — не нашёл (искал Google «A16-61M disassembly/teardown/M.2», LaptopMedia, NBC).
  - Поддержка Acer DE: 25 драйверов (последние 30.06.2026), BIOS 1.31 (26.06.2026); документы — User Manual (07.2025), **сервис-мануала нет** ([Acer Support A16-61M](https://www.acer.com/de-de/support/product-support/A16-61M)). Руководство пользователя от 04.07.2025 → модель на рынке примерно с лета 2025.
- **Жалобы владельцев:** Google `"Swift Air 16" (problem OR issue OR defekt) (reddit OR community.acer.com)` и `"SFA16-61M" site:community.acer.com` — тем о дефектах нет; в Acer Community одна тема (сброс пароля Windows, R1ZM) ([Acer Community](https://community.acer.com/en/discussion/742582/air-16-sfa16-61m-r1zm-unable-to-re-set-the-password-on-the-desktop-is-st)). Reddit — только обсуждение анонса ([r/AMDLaptops](https://www.reddit.com/r/AMDLaptops/comments/1n8353t/acer_swift_air_16_2025_is_my_dream_laptop_i_was/)).

## Сырые данные: eBay/AliExpress, idealo-распространённость (30.09.2026, ~23:50)
- **eBay.de, только новые** ([SFA16-61M](https://www.ebay.de/sch/i.html?_nkw=SFA16-61M&LH_ItemCondition=1000)): 33 результата — ноутбуки и SSD «passend für»; **аккумулятора, матрицы, клавиатуры, вентилятора для Swift Air нет**.
  [A16-61M](https://www.ebay.de/sch/i.html?_nkw=A16-61M&LH_ItemCondition=1000): 73 результата; из деталей — вентилятор с радиатором «95W TDP» 43,50 €.
  [AP22ABN](https://www.ebay.de/sch/i.html?_nkw=AP22ABN&LH_ItemCondition=1000) (аккумулятор 65 Вт·ч 11,61 В из списка IPC для A16-61M): **74 новых предложения, ~105–107 €**; тот же аккумулятор у Aspire 14 AI, Swift Go 16 (SFG16-72), TravelMate Spin P4, Chromebook Plus 516 — массовая деталь. Какой из двух аккумуляторов (AP22ABN или AP22A8N) стоит именно в R2R1 — не проверено.
- **AliExpress** ([SFA16-61M](https://de.aliexpress.com/w/wholesale-SFA16-61M.html)): выдача не отрисовалась (0 товаров, без капчи) — не проверено.
- **idealo, распространённость:** поиск [«Swift Air 16»](https://www.idealo.de/preisvergleich/MainSearchProductCategory.html?q=Swift%20Air%2016) — ~9 карточек SFA16-61M (R1FY, R559, R1ZM, R6R8, R564, R7VK, R2T2 и общая); [«A16-61M»](https://www.idealo.de/preisvergleich/MainSearchProductCategory.html?q=A16-61M) — 15 карточек (R98E, R8T1, R194, R473, R014, R87H, R2R1, R0Q9, R0G4, R5EH, R8RH, JP0EG.009/.008, JLLEG.00L…).
  В выдаче категории [16" + AMD](https://www.idealo.de/preisvergleich/ProductCategory/3751F848110-1568565.html) (сортировка idealo по умолчанию; 54 карточки на 1-й странице): Aspire 16 AI R8T1 — **7-е место**, Swift Air 16 OLED R1FY (наш P/N) — **14-е**, Aspire 16 AI R473 — 16-е, R194 — 19-е; R2R1 на 1-й странице нет.
  Предложений на карточках (~23:50): `NX.DL5EG.002` — 6 (Kaufland МП 999,00; expert 999,00; boomstore 1017; OTTO МП 1029,99; eBay 1046; Galaxus МП 1276,11 — без изменений) ([idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/211778543_-swift-air-16-oled-16-wuxga-amd-ryzen-ai-5-32gb-1tb-ssd-silber-nx-dl5eg-002-acer.html));
  `NX.JP0EG.00Z` 32/1 ТБ — 3 (computeruniverse 1081,21; e-tec 1111,90; voelkner МП 1156; остальные 5 строк — чужие 16-ГБ SKU) ([idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/211631508_-aspire-16-ai-a16-61m-r2r1-acer.html)).
- **expert, R1FY** ([товар](https://www.expert.de/shop/unsere-produkte/computer-zubehor/notebooks/laptops/17041266033-swift-air-16-oled-silber-16-zoll-wuxga-amd-ryzen-ai-5-330-32-gb-1024-gb-ssd-amd-radeon-820m.html), ~23:50): 999,99 €, «Reservieren und sofort abholen», **1 отзыв (5,0)**. В подвале — ссылки «60 Monate Garantie» и «Recht auf Reparatur»; текст страницы «60 Monate Garantie» не извлёкся — условия не проверены.
- **Icecat:** R1FY — дата выпуска SKU 21.07.2026, «Garantiezeit 2 Jahr(e)», аккумулятор 50 Вт·ч 3 ячейки ([Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Acer&ProductCode=NX.DL5EG.002)); R2R1 — поле гарантии пустое, 65 Вт·ч, microSD ([Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Acer&ProductCode=NX.JP0EG.00Z)).
- **Тип гарантии Acer в DE (Bring-in / Pick-up):** не проверено — acer.com/de-de/support/warranty и store.acer.com в Chrome отдали страницу ошибки/пустую страницу, curl к acer.com — нет ответа; Google на запросе про гарантию показал капчу (не проходил, перешёл на Bing — нужной выдачи нет). По выдаче Google у Acer Store есть платное продление «3 years Carry-in, 1st year International Travellers Warranty» для Aspire/Swift и у продавцов — «Acer Care Plus … Bring-in / Pick-Up & Return» ([Acer Store](https://store.acer.com/de-de/3-years-carry-in-1st-year-international-travellers-warranty-notebook-aspire), [office-partner](https://www.office-partner.de/acer-care-plus-advantage-4-jahre-bring-in-n2008295912)) — значит, базовая гарантия, скорее всего, Carry-in/Bring-in (вывод, не факт).

## Сырые данные: ремонтный индекс, гарантия, отзывы в магазинах (30.09.2026, ~23:55)
- **Французский индекс ремонтопригодности:** для SFA16-61M и A16-61M **не нашёл**. Где искал: LDLC (поиск «Swift Air 16», «SFA16-61M», «A16-61M» — этих моделей в ассортименте нет), Fnac — карточка A16-61M-R4KC без индекса у самого товара (индексы 6,8 и др. — у соседних моделей в карусели: Aspire 14 AI A14-52M 6,8; Nitro V 16 AI 6,9; Aspire Go 15 7,4) ([Fnac](https://www.fnac.com/PC-portable-Acer-Aspire-16-AI-A16-61M-R4KC-16-OLED-120-Hz-Copilot-AMD-Ryzen-5-AI-32-Go-RAM-512-Go-SSD-Gris/a21813322/w-4)), Darty и Boulanger — бот-защита / пустая страница, Pixmania — индекса нет, acer.com/fr-fr — страница ошибки, WebSearch — нет данных.
- **Гарантия Acer в DE — тип.** Продления в Acer Store DE называются «3 Jahre Einsende-/Rücksendeservice einschließlich 1 Jahr International Travellers Warranty» (для Aspire, Spin, Swift) — т. е. сервис Acer в DE — **отправка в сервисный центр Acer с бесплатной пересылкой** (Einsende-/Rücksendeservice ≈ Carry-in/Pick-up), не Vor-Ort ([Acer Store DE](https://store.acer.com/de-de/3-years-carry-in-1st-year-international-travellers-warranty-notebook-aspire) — заголовок из выдачи поиска, сама страница не открылась). Срок базовой гарантии — **2 года** (Icecat R1FY; даташит Acer R2R1 от 26.06.2026 — [даташит](https://gzhls.at/blob/ldb/e/9/9/4/1b8b6ae3e1047dc798a552be0d80e9a0f0ab.pdf), см. `AMD/REPORT.md` №10). Отдельный срок на аккумулятор для новых устройств — не проверено.
- **Отзывы Amazon.de (30.09, ~23:55):** [Aspire 16 AI A16-61M](https://www.amazon.de/s?k=Acer+Aspire+16+AI+A16-61M) — Ryzen AI 5 16/512: 4,2★ (19), «50+ bought»; OLED Ryzen AI 5 16/512: 4,6★ (6); OLED Ryzen AI 7 32/1 ТБ — без оценок. [Swift Air 16 SFA16-61M](https://www.amazon.de/s?k=Acer+Swift+Air+16+SFA16-61M) — ноутбуки без оценок; есть зарядки Delta 65 Вт и SSD «passend für».
- Google на запросе про гарантию (~23:50) выдал капчу «ungewöhnlicher Datenverkehr» — не проходил; дальше Bing (пустая выдача) и WebSearch.

---

# Итог по кандидатам

## 1. Acer Swift Air 16 OLED SFA16-61M-R1FY — `NX.DL5EG.002` (прошёл всё, включая наличные)
[idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/211778543_-swift-air-16-oled-16-wuxga-amd-ryzen-ai-5-32gb-1tb-ssd-silber-nx-dl5eg-002-acer.html) · за наличные 999,99 € expert (самовывоз, оплата в Fachmarkt).

**1) Надёжность**
- Бренд: Acer — 8-й из 10 в сводке CR + PCMag 2025 ([BGR](https://www.bgr.com/2072636/most-reliable-laptop-brands-ranked-worst-best/)); сервис в DE — 3-е место в опросе NBC 2024 ([NBC](https://www.notebookcheck.com/Umfrage-Service-und-Support-im-Reparaturfall-Diese-Laptop-und-Smartphone-Hersteller-koennen-nicht-ueberzeugen.905354.0.html)). Отдельной строки RTINGS по брендам не нашёл (только пересказ CR/PCMag у BGR).
- Типичные болячки линейки Swift: петли и крышка экрана (IPC, 07/2026 — [IPC Acer](https://blog.ipc-computer.de/2026/07/acer-service/)).
- Эта модель: корпус Mg-Al «überraschend stabil», дно не прогибается, петли сбалансированы ([LaptopMedia DE, 15.07.2026](https://laptopmedia.com/de/review/acer-swift-air-16-sfa16-61m-review-a-16-inch-laptop-that-weighs-under-1-kg/)); на hands-on WinFuture корпус показался «weniger hochwertig», клавиатура тесная ([WinFuture, 11.09.2025](https://winfuture.de/videos/Hardware/Swift-Air-16-Sehr-leichtes-16-Zoll-Notebook-mit-Schwaechen-27897.html)). OLED с ШИМ «mit begrenzter Amplitude» (частота не измерена) — LaptopMedia.
- Жалоб владельцев на дефекты не нашёл (Google по reddit + Acer Community; единственная тема — сброс пароля — [Acer Community](https://community.acer.com/en/discussion/742582/air-16-sfa16-61m-r1zm-unable-to-re-set-the-password-on-the-desktop-is-st)). Причина скорее в малой распространённости, а не в доказанной надёжности.
- ПО живое: BIOS 1.06 (03.08.2026) и **1.07 (24.09.2026, «Modify fan table»)** ([Acer Support](https://www.acer.com/de-de/support/product-support/SFA16-61M)).
- Риск HEVC у Acer DE с 06.2026 — проверить DXVA Checker в срок возврата ([ChannelPartner](https://www.channelpartner.de/article/4187748/acer-und-asus-liefern-wieder.html)).
- Гарантия: 2 года ([Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Acer&ProductCode=NX.DL5EG.002)); тип — Einsende-/Rücksendeservice (отправка в сервис Acer, пересылка бесплатно), не Vor-Ort ([Acer Store DE](https://store.acer.com/de-de/3-years-carry-in-1st-year-international-travellers-warranty-notebook-aspire), по заголовку продления). Плюс 2 года Gewährleistung продавца (expert — магазин рядом, можно сдать туда).

**2) Запчасти**
- Официальный срок выпуска запчастей Acer — публичных обязательств нет ([`brands.md`](../../Intel/notes/brands.md), [`right-to-repair.md`](../../Intel/notes/right-to-repair.md)).
- IPC ([страница модели](https://www.ipc-computer.de/acer/notebook/swift-serie/swift-air-16-sfa16-61m/), 30.09): **дисплейный блок целиком (матрица + крышка + петли) 225 €** — 1 шт. на складе ([товар](https://www.ipc-computer.de/acer/notebook/swift-serie/swift-air-16-sfa16-61m/displayeinheit-152880795)); топкейс с немецкой клавиатурой 93 € и нижняя крышка 105 € — под заказ у Acer (3–8 дней); плата с CPU + 32 ГБ 867 €; Wi-Fi 43 €; БП USB-C 65 Вт 33–39 € (на складе). **Аккумулятора и вентилятора нет.**
- eBay.de (новые): для SFA16-61M деталей нет, только SSD «passend für» и ноутбуки ([eBay](https://www.ebay.de/sch/i.html?_nkw=SFA16-61M&LH_ItemCondition=1000)); Amazon — только зарядки Delta 65 Вт ([Amazon](https://www.amazon.de/s?k=Acer+Swift+Air+16+SFA16-61M)). AliExpress — выдача пустая, не проверено.
- Зарядка — стандартная USB-C 65 Вт: замену найти легко.
- Сервис-мануала нет: на странице поддержки только User Manual ([Acer Support](https://www.acer.com/de-de/support/product-support/SFA16-61M)).

**3) Ремонтопригодность** ([LaptopMedia DE](https://laptopmedia.com/de/review/acer-swift-air-16-sfa16-61m-review-a-16-inch-laptop-that-weighs-under-1-kg/))
- Вскрытие: 12 винтов Torx T6 + защёлки по периметру (лопатка), винты разной длины.
- Меняется: SSD (**один** M.2 2280 PCIe 4.0, один винт), Wi-Fi (M.2 2230), вентилятор (легко снять и почистить), **аккумулятор 50 Вт·ч на винтах**, динамики.
- Не меняется: CPU и 32 ГБ LPDDR5 — распаяны; второго M.2 нет.
- Французский индекс — не нашёл (LDLC, Fnac, Darty, Boulanger, Bing, WebSearch). iFixit — нет гайда и оценки ([iFixit](https://www.ifixit.com/repairability/laptop-repairability-scores)).

**4) Распространённость**
- Анонс IFA 03.09.2025, в продаже с 11.2025 ([NBC](https://www.notebookcheck.com/Acer-Swift-Air-16-Leichtester-16-Zoll-Laptop-aller-Zeiten-schlaegt-LG-Gram-und-startet-guenstig-mit-Ryzen-AI-300-Power.1102769.0.html)); этот SKU R1FY в Icecat — с 21.07.2026.
- idealo: 6 предложений у R1FY; ~9 карточек модели; в выдаче «16" + AMD» — 14-е место ([idealo](https://www.idealo.de/preisvergleich/ProductCategory/3751F848110-1568565.html)).
- Обзоры: полный тест LaptopMedia (с разборкой); у NBC только сборник ([NBC](https://www.notebookcheck.com/Acer-Swift-Air-16-SFA16-61M.1173568.0.html)).
- Отзывы: expert — 1 (5,0); Amazon.de — оценок нет; форумов почти нет → **модель редкая**: помощь и б/у-доноров искать трудно.

**5) Оценки**
- **Ремонт — 3,5/10** (было 3): аккумулятор на винтах, вентилятор, SSD и Wi-Fi меняются легко; дисплейный блок с петлями и топкейс есть у IPC. Минусы: распайка RAM, один M.2, нет мануала, аккумулятора и вентилятора в продаже не нашёл, модель редкая.
- **Проблемность — 4,5/10** (без изменений): бренд в нижней половине по надёжности, у Swift бывают петли; риск HEVC; ШИМ OLED; BIOS правит вентилятор ещё в 09.2026. Плюс — прочный корпус по LaptopMedia и отсутствие жалоб (но и владельцев мало). Сервис Acer в DE хороший (3-е место NBC).

## 2. Acer Aspire 16 AI OLED A16-61M-R2R1 — `NX.JP0EG.00Z` (для сравнения: наличными в бюджете нет)
[idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/211631508_-aspire-16-ai-a16-61m-r2r1-acer.html) · 1081,21 € computeruniverse (Rechnung/Vorkasse), 3 продавца именно 32/1 ТБ.

**1) Надёжность**
- Бренд — как выше (BGR 8/10, NBC-сервис 3-е место).
- Эта модель: TechRadar (26.01.2026, образец AI 7 350, то же шасси): «somewhat flimsy build quality … a fair amount of flex to the chassis, while the lid hinge doesn't offer the greatest stability» ([TechRadar](https://www.techradar.com/computing/windows-laptops/acer-aspire-16-ai-review)). Trusted Reviews (15.12.2025): алюминиевый корпус, минусы — «generic» дизайн и автономность, о дефектах ничего ([Trusted Reviews](https://www.trustedreviews.com/reviews/acer-aspire-16-ai)).
- Отзывы Amazon.de по соседним SKU A16-61M: 4,2★ (19) и 4,6★ (6) ([Amazon](https://www.amazon.de/s?k=Acer+Aspire+16+AI+A16-61M)).
- Форумы (WebSearch `reddit "Aspire 16 AI" A16-61M problem OR issue OR hinge OR flicker`, 30.09, ~23:57): на reddit тем о дефектах нет. В Acer Community — тема от 14.06.2026: у OLED-версии BIOS пишет тип панели «LCD», автор боится, что не работает защита от выгорания; «Accepted Answer» от участника сообщества (TRAILBLAZER, не сотрудник Acer): «LCD» — общее слово Acer для экранов, модель панели смотреть в HWiNFO; ссылается на **сервис-гайд A16-61M** со списком панелей ([Acer Community](https://community.acer.com/en/discussion/739642/urgent-aspire-16-ai-a16-61m-oled-latest-bios-shows-lcd-instead-of-oled-potential-burn-in-risk)). Реальная проблема не доказана; сервис-гайд, значит, существует, но публично Acer его не выкладывает (на странице поддержки его нет).
- ШИМ и замер OLED — нет (см. `display-sweep.md`).
- ПО: BIOS 1.31 (26.06.2026), драйверы 30.06.2026 ([Acer Support](https://www.acer.com/de-de/support/product-support/A16-61M)).
- Риск HEVC у Acer DE — тот же.
- Гарантия: 2 года (даташит Acer 26.06.2026 — [PDF](https://gzhls.at/blob/ldb/e/9/9/4/1b8b6ae3e1047dc798a552be0d80e9a0f0ab.pdf)); тип — Einsende-/Rücksendeservice (как выше).

**2) Запчасти**
- Официального срока нет (как выше). Публичного сервис-мануала нет — на странице поддержки только User Manual ([Acer Support](https://www.acer.com/de-de/support/product-support/A16-61M)); участник Acer Community цитирует список панелей «from its service guide» — документ где-то ходит, но ссылки на него нет ([Acer Community](https://community.acer.com/en/discussion/739642/urgent-aspire-16-ai-a16-61m-oled-latest-bios-shows-lcd-instead-of-oled-potential-burn-in-risk)).
- IPC ([Aspire A16-61M](https://www.ipc-computer.de/acer/notebook/aspire-serie/16/aspire-a16-61m/), [Aspire 16 (A16-61M)](https://www.ipc-computer.de/acer/notebook/aspire-serie/16/aspire-16-a16-61m/), 30.09): **аккумулятор 65 Вт·ч оригинал 94 € (на складе, 2 варианта AP22ABN / AP22A8N)**; **матрица Samsung 16" с креплением 333 €** (под заказ; вероятно OLED — тип не указан); топкейс с немецкой клавиатурой 74 €; вентиляторы 35 €, радиаторы 38 €, вентилятор с радиатором 36 € («Nur noch wenige»); БП USB-C 65 Вт 39 €, 100 Вт 62 €; всего в каталоге ~12 корпусных деталей, 7 плат, динамики, кабели матрицы.
- eBay.de: аккумулятор AP22ABN — **74 новых предложения, ~105–107 €**, общий с Aspire 14 AI, Swift Go 16, TravelMate Spin P4 ([eBay](https://www.ebay.de/sch/i.html?_nkw=AP22ABN&LH_ItemCondition=1000)); вентилятор 43,50 € ([eBay](https://www.ebay.de/sch/i.html?_nkw=A16-61M&LH_ItemCondition=1000)). Какой из двух аккумуляторов в R2R1 — не проверено.

**3) Ремонтопригодность**
- Разборку A16-61M не нашёл (LaptopMedia — только страница серии, NBC — только сборник, WebSearch/Google «A16-61M disassembly/teardown»). Число M.2-слотов, крепление аккумулятора и винты — **не проверено**.
- Известно: RAM распаяна («Onboard-RAM (nicht austauschbar)» — даташит; «fix onboard» — [Compuram](https://www.compuram.de/arbeitsspeicher/acer/notebook/aspire/16-ai/a16-61m/0-00-1ae6a.htm)); SSD M.2 PCIe 4.0 — меняется (Icecat, Compuram).
- Французский индекс — не нашёл (Fnac R4KC без индекса, LDLC нет, Darty/Boulanger закрыты). Для ориентира: Aspire 14 AI — 6,8 ([LDLC](https://www.ldlc.com/fiche/PB00686783.html)). iFixit — нет.

**4) Распространённость**
- Модель A16-61M на рынке примерно с лета 2025 (User Manual Acer от 04.07.2025; обзоры 12.2025–01.2026); R2R1 — поздний SKU.
- idealo: 15 карточек A16-61M; R8T1 — 7-е место в выдаче «16" + AMD», R473 — 16-е, R194 — 19-е ([idealo](https://www.idealo.de/preisvergleich/ProductCategory/3751F848110-1568565.html)); у самого R2R1 32/1 ТБ — 3 продавца.
- Обзоры: 2 англоязычных теста (TechRadar, Trusted Reviews), своих тестов NBC/LaptopMedia нет.
- Отзывы: Amazon.de до 19 оценок на SKU, «50+ bought» → **заметно популярнее Swift Air**; детали общие с другими Acer (аккумулятор AP22ABN), помощь найти проще.

**5) Оценки**
- **Ремонт — 4/10** (было 3): запчасти есть и дешёвые (аккумулятор 94–107 € — массовая деталь, OLED-матрица 333 €, клавиатура 74 €, вентилятор 35 €), SSD меняется. Минусы: распайка RAM, нет мануала и разборки, число M.2 не проверено.
- **Проблемность — 4/10** (без изменений): TechRadar — прогиб корпуса и не самая устойчивая крышка; риск HEVC; ШИМ и замер OLED неизвестны; бренд в нижней половине по надёжности. Плюсы — отзывы 4,2–4,6★, BIOS обновляется.

## Сравнение в двух строках
- По ремонту и популярности R2R1 лучше: у него есть аккумулятор (массовый AP22ABN) и OLED-матрица в продаже. Swift Air разобран в тесте и собран аккуратнее (аккумулятор на винтах), но деталей к нему почти нет.
- По проблемности почти равны (оба Acer, риск HEVC, распайка). У Swift Air крепче корпус по тесту, у R2R1 — жалоба TechRadar на прогиб и петлю.
