## Проверка hp-dell (AMD)

_30.09.2026, локальная сессия, скептическая проверка [`candidates-hp-dell.md`](candidates-hp-dell.md). Цены — idealo.de в Chrome пользователя (своя вкладка, капчи не было, ничего не отправлял). Память — HP QuickSpecs (pdftotext) + HP PartSurfer (BOM по P/N; API `partsurfer.hpcloud.hp.com` из curl теперь отвечает «Access to the resource is prohibited», из вкладки partsurfer.hp.com — отвечает). Icecat: обоих P/N нет (404). Правило цены — корневой `../../CLAUDE.md` (минимум нового у любого продавца, маркетплейсы включительно). Файл пишется по ходу._

### Вывод

1. **Шорт-лист HP/Dell не даёт ни одного чистого кандидата в 1100 €.** Оба SKU остаются в своих списках, но с поправками.
2. **`CN0Q3EC` (EliteBook 8 G1a 16, HEVC есть) — watch-over-1100, риск выше, чем записал кандидат:**
   - раскладка **не подтверждена** и по BOM не определяется: в PartSurfer есть и модуль 16 ГБ, и модуль 32 ГБ; Icecat — 404;
   - **новое: это DaaS-юнит** («WHOLE UNIT DAAS CN0Q3EC ABD», PartSurfer). Продаёт один магазин — asaboshisystems.de, партнёр HP Renew (продаёт и новые, и восстановленные). Новый ли экземпляр и есть ли на него гарантия HP — не проверено;
   - второго M.2 нет → SSD только менять; итог **1147,89 €** (подтверждено), минимум за год = 999 € = сегодня.
3. **`CU0R1ES` (HP 255R G10) — B16-plus-stick (условно), итог исправлен: 937,44 €** (планка Kingston с маркетплейса Galaxus 187,56 € — по новому правилу цены маркетплейс считается). С Crucial из магазина — 998,77 €.
   - Память 1×16 + свободный слот держится на QuickSpecs + BOM. **Сервис-мануал HP противоречит** (в описании — «onboard, not upgradeable»), но в нём же есть SODIMM-модули с процедурой замены.
   - Против: Zen 3+ 2022 года (680M, RDNA 2 в maintenance), HEVC — нет данных при высоком риске, HDMI только до 1920×1200, второго M.2 нет. Панель — 45 % NTSC по QuickSpecs или 100 % sRGB по MSG (противоречие).
   - **Не рекомендую**: формально проходит, по сути — последний выбор.
4. **Выборочная проверка отброшенных — отброшены правильно:** `C7SP9ES` (фраза «HEVC … is disabled on this platform» есть в c09111176 v15; 2×16 и 1 ТБ подтверждены; 906,99 €); `CT3V8ES` — 1×32 (в BOM только модуль 32 ГБ). Арифметика «2×8 → ~1170 €» у `BP1G1EA` устарела (с Kingston 2×187,56 — ≈1070 €), но 2×8 исключено критериями.

### Сводная таблица (idealo, 30.09.2026)

| P/N | Модель | CPU | Память (даташит) | SSD / M.2 | HEVC | Цена сейчас (с доставкой) | Мин. за год | Итог с докупкой | Список | Вердикт |
|---|---|---|---|---|---|---|---|---|---|---|
| `CN0Q3EC` | EliteBook 8 G1a 16 | R5 PRO 230, Hawk Point, 6 Zen 4, 760M | 2 SODIMM; **2×16 или 1×32 — не подтверждено** ([c09120200](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09120200), [PartSurfer](https://partsurfer.hp.com/partsurfer/?searchtext=CN0Q3EC)) | 512 ГБ, один M.2 → менять | **есть** (QuickSpecs) | **1005,00 €** asaboshisystems.de, возврат не указан (14 законных), 1 предложение — [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/214137501_-elitebook-8-g1a-16-cn0q3ec-hp.html) | 999 € (17.09.2026, = сегодня) | 1005 + 142,89 = **1147,89 €** | watch-over-1100 | исправлено: + DaaS / Renew-риск |
| `CU0R1ES` | HP 255R G10 | R7 7735U, Rembrandt‑R, Zen 3+, 680M | **1×16 SODIMM + свободный слот** ([c09053765](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09053765), [PartSurfer](https://partsurfer.hp.com/partsurfer/?searchtext=CU0R1ES)); MSG частично противоречит | 512 ГБ, один M.2 → менять | нет данных, риск высокий | **606,99 €** nullprozentshop.de (возврат не указан); 607,99 NBB (30 дн.) — [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/210295290_-255r-g10-cu0r1es-hp.html) | 599 € (с 11.05.2026 без изменений) | 606,99 + 187,56 + 142,89 = **937,44 €** | B16-plus-stick | исправлено (итог −57 €); не рекомендую |

### Цены докупки (idealo, 30.09.2026, пересняты)

| Что | Минимум с доставкой | Магазин, возврат | Карточка |
|---|---|---|---|
| Планка DDR5-5600 16 ГБ — Kingston `KVR56S46BS8-16` | **187,56 €** | Galaxus — маркетплейс (продавец Avanturis), 30 дн.; единственное предложение | [213624753](https://www.idealo.de/preisvergleich/OffersOfProduct/213624753_-valueram-16gb-ddr5-5600mhz-cl46-so-dimm-on-die-ecc-kvr56s46bs8-16-kingston.html) |
| Планка DDR5-5600 16 ГБ — Crucial `CT16G56C46S5` | 248,89 € («ab 243,90» — без доставки) | alza.de, 30 дн.; дальше bueromarkt-ag 266,81 | [202284828](https://www.idealo.de/preisvergleich/OffersOfProduct/202284828_-16gb-ddr5-5600-cl46-ct16g56c46s5-crucial.html) |
| SSD 1 ТБ NVMe M.2 2280 — Kingston NV3 `SNV3S/1000G` | **142,89 €** | alternate.de, 14 дн.; bueromarkt-ag 143,98; x-kom 146,89 | [204697967](https://www.idealo.de/preisvergleich/OffersOfProduct/204697967_-nv3-1tb-kingston.html) |

### HP EliteBook 8 G1a 16 — `CN0Q3EC`

**Вердикт: исправлено — watch-over-1100 остаётся, но с двумя новыми рисками: это DaaS-юнит (HP Device as a Service), продаёт его партнёр HP Renew; раскладка памяти так и не подтверждена.**

- **Память — не подтверждено (2×16 или 1×32):**
  - QuickSpecs EliteBook 8 G1a 16 ([c09120200, v21, 11.09.2026](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09120200)), MEMORY: «32GB DDR5-5600 MT/s (1 x 32 GB)» и «32GB DDR5-5600 MT/s (2 x 16 GB)» — оба варианта; «Memory Slots 2 SODIMM», «Supports Dual Channel Memory(optional)», «accessible/upgradeable by IT or self-maintainers only».
  - PartSurfer `CN0Q3EC` ([UI](https://partsurfer.hp.com/partsurfer/?searchtext=CN0Q3EC)): в BOM **оба модуля** — `N77399-001` «SKO-SODIMM 16GB DDR5 5600» и `N77400-001` «SKO-SODIMM 32GB DDR5 5600»; поле `PartCount` = 0, количество не указано. Для сравнения, у той же модели BOM однозначен: `CT3V8ES` — только модуль 32 ГБ (**1×32**, подтверждаю), `CT3V9ES` и `AD3F6ET` — только 16 ГБ (2×16).
  - BOM `CN0Q3EC` сводный на 8 раскладок клавиатуры (UK, GR, FR, ITL, DEN, HUNG, SE/FI, CS/SK) — может быть, в разных локализациях разная память. Отдельно `CN0Q3EC#ABD` в PartSurfer не ищется (пустой ответ).
  - Icecat: `CN0Q3EC` и `CN0Q3EC#ABD` — 404. idealo-даташит («32 GB RAM») раскладку не даёт.
- **Новое: это DaaS-SKU.** В PartSurfer запчасть `P86979-001` названа «WHOLE UNIT DAAS CN0Q3EC ABD»; в выдаче поиска — такие же «SPS-WU DAAS CN0Q3EC» ABY/ABF/BCM/AK8 у дистрибьюторов запчастей ([DuckDuckGo «CN0Q3EC»](https://html.duckduckgo.com/html/?q=%22CN0Q3EC%22)). Единственный продавец на idealo — asaboshisystems.de; по описанию в поиске это «Versandhandel für günstige neue und generalüberholte Computer», «HP Renew Programm Partner» ([asaboshisystems.de](https://asaboshisystems.de/)). В предложении idealo состояние не указано, страница товара в магазине через поиск магазина не нашлась, переход «Zum Shop» idealo заблокировал (relocator → «Something has gone wrong»). → **Новый ли это ноутбук и с какой гарантией — не проверено**; спрашивать продавца письменно (новый/Renew, 2×16?, гарантия HP на серийный номер).
- **SSD:** 512 ГБ `N77392-001` (PartSurfer); в QuickSpecs раздел Storage — один накопитель, вторичного нет; NBC: «limited to a single M.2 2280 slot» ([NBC](https://www.notebookcheck.net/HP-EliteBook-8-G1a-16-AI-laptop-review-Redesigned-inside-and-out.1103659.0.html)). Условный вариант «+ SSD во второй слот» **не применим** — только замена.
- **CPU — подтверждено:** в BOM «SPS-MB UMA R5 PRO 230» → Ryzen 5 PRO 230: «Former Codename Hawk Point», Zen 4, 6 ядер / 12 потоков, Radeon 760M (8 CU) — [amd.com](https://www.amd.com/en/products/processors/laptop/ryzen-pro/200-series/amd-ryzen-5-pro-230.html); = 8640U/8640HS ([`amd-cpu.md`](amd-cpu.md), табл. «Ryzen 200»). Не урезан (урезан 5 220, не 230). Для 4K — нормально при двухканале; 760M слабее 780M.
- **HEVC — подтверждено:** «Hardware Acceleration HEVC (H.265) CODEC is supported.» (c09120200, GRAPHICS → Codec).
- **Экран:** в BOM панель `P54499-001` «RAW PANEL 16 WUXGA AG 400n» → по QuickSpecs это «WUXGA … 400 nits, Low Power, sRGB 100%» (единственная WUXGA 400 нит в списке). Лучше, чем 62,5 % sRGB у базовой.
- **Зарядка — исправлено:** в BOM «SKO-65W ADPTR, nPFC, USB-C» (65 Вт), idealo пишет 100 Вт — idealo ошибается. QuickSpecs: для батареи > 56 Втч «Power adapter minimum of 100 watts required» — речь о быстрой зарядке; с 62 Втч и 65 Вт заряжаться будет медленнее. Докупать не обязательно.
- **Цена — idealo, 30.09.2026** ([карточка этого P/N](https://www.idealo.de/preisvergleich/OffersOfProduct/214137501_-elitebook-8-g1a-16-cn0q3ec-hp.html)): одно предложение — asaboshisystems.de, **999,00 € / 1005,00 € с доставкой**, Vorkasse, доставка до 02.10; срок возврата в предложении не указан (законные 14 дней); рейтинг магазина 3,8. Подтверждено.
- **История — подтверждено (со второй попытки):** в ~14:00 API отвечал 404, в ~14:10 — 200. Точки 17.09, 22.09 и 30.09.2026 — все **999,00 €** (без доставки), `avgPriceDaysDataPeriod` = 14. Карточке две недели; минимум за год = 999 € = сегодня. «14 дней ≤ 1100 €» у кандидата — это длина периода с данными, а не 14 замеров.
- **Итог:** 1005,00 + SSD 142,89 = **1147,89 €** (> 1100, подтверждено). Чтобы влезть, нужен SSD 1 ТБ ≤ 95 € — на idealo сейчас дешевле 142,89 € нет (NV3 — самый дешёвый в расчётах всех групп, [`verify-idealo-sweep.md`](verify-idealo-sweep.md)).

### HP 255R G10 — `CU0R1ES`

**Вердикт: подтверждено по памяти и цене, итог исправлен вниз (937,44 € вместо 994,78 € — планка с маркетплейса); условно B16-plus-stick, не рекомендую (Zen 3+, HEVC неизвестен, слабый экран).**

- **Память — подтверждено (1×16 + свободный слот):**
  - PartSurfer `CU0R1ES` ([UI](https://partsurfer.hp.com/partsurfer/?searchtext=CU0R1ES)): один модуль `N77399-005` «SKO-SODIMM 16GB DDR5 5600»; MB `P19902-601` «UMA R7 7735U 255R G10».
  - QuickSpecs 255R G10 ([c09053765, v7, 06.03.2026](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09053765)), MEMORY: варианты «16GB DDR5-4800 (1 x 16 GB)» и «(2 x 8 GB)»; «Memory Slots 2 SODIMM (RMB-UR only)», «Support Dual Channel Memory», «System runs at 4800». Раз в BOM только модуль 16 ГБ, а 16 ГБ бывает 1×16 или 2×8 — это 1×16, второй слот пуст.
  - Оговорки из того же QuickSpecs: «All slots are customer non-accessible / non-upgradeable» (политика сервиса HP, не физический запрет); «Maximum Memory 32GB DDR5-4800 (1 x 32GB)», «Designed to support up to 32GB» — 2×16 = 32 ГБ в предел укладывается. Память будет работать на 4800.
- **Сервис-мануал найден:** [HP 255R 15.6 inch G10 MSG, P22370-001, First Edition 12.2024](https://kaas.hpcloud.hp.com/pdf-public/pdf_11296126_en-US-1.pdf) (ссылку дал обзор NBC 255 G10). В таблице Product description там написано «Onboard memory supporting up to 16 GB … (not accessible or upgradeable) LPDDR5-4800» — **противоречит** QuickSpecs и BOM. Но в том же MSG есть раздел «Memory modules (select products only)» с модулями SODIMM 16 ГБ `N38627-005` / `N77399-005` (тот самый, что стоит в `CU0R1ES`) и процедурой замены. Вывод: описание в MSG — для LPDDR5-вариантов, у 7735U — SODIMM. Раскладка 1×16 + слот держится на QuickSpecs («2 SODIMM (RMB-UR only)») + BOM; мануал её не опровергает, но и прямо не подтверждает число слотов. **При получении проверить** (CPU-Z / диспетчер задач «Гнёзд: 1 из 2»).
- **SSD:** 512 ГБ `N77392-005` → менять на 1 ТБ. И QuickSpecs, и MSG знают только «Primary storage: M.2 2280 PCIe NVMe»; вторичного накопителя нет → **второго M.2 нет** (по обоим документам HP).
- **CPU — подтверждено:** Ryzen 7 7735U: «Former Codename Rembrandt R», Zen 3+, 8 ядер / 16 потоков, Radeon 680M (12 CU) — [amd.com](https://www.amd.com/en/products/processors/laptop/ryzen/7000-series/amd-ryzen-7-7735u.html), QuickSpecs, табл. PROCESSOR; [`amd-cpu.md`](amd-cpu.md): «старый (2022); брать только очень дёшево»; RDNA 2 в maintenance mode с 10.2025. AV1-кодирования нет. Для 4K — слабо: таймлайн H.264/HEVC 4:2:0 8/10 бит декодирует (VCN 3.1), эффекты — медленно.
- **HEVC — риск высокий, подтверждено «нет данных»:** в QuickSpecs в GRAPHICS только «Support HD decode, DX12, HDMI 1.4b»; фразы «disabled» нет, фразы «supported» тоже. HP заявил отключение для «200 Series G9» ([`hevc-amd.md`](hevc-amd.md), §1.2, Ars). Проверять DXVA Checker в окно возврата.
- **Экран — противоречие документов HP, не проверено:** панель `P21489-001` «RAW PANEL 15.6 FHD AG LBL UWVA 300» (BOM). QuickSpecs: единственная UWVA 300 нит — «NTSC 45 %, 6 bit Hi-FRC, Low Blue Light: No». MSG: `P21489-001` = «FHD, antiglare, low blue light, UWVA, 300 nits», а в описании модели UWVA 300 нит — «sRGB 100%, eDP 1.4 + PSR 2, low blue light». Низкий синий («LBL») в имени детали совпадает с MSG, так что панель может оказаться 100 % sRGB — но замера нет. Кандидат записал 45 % NTSC.
- **Порты:** HDMI 1.4b, и QuickSpecs прямо пишет «Port supports resolutions up to 1920 x 1200 external resolution @60 Hz» — **4K-монитор по HDMI не подключить**; 4K — только через USB-C 10 Гбит/с (DP 1.4). 2× USB-A 5 Гбит/с. SD-карты нет. — QuickSpecs PORTS/SLOTS, HDMI.
- **Зарядка:** в BOM `741727-001` «SKO-45W ADPTR … 4.5mm» (45 Вт, круглый штекер); idealo пишет 65 Вт — ошибается. В комплекте, докупать не нужно. Батарея 41 Втч (`N21969-001`).
- **Цена — idealo, 30.09.2026** ([карточка этого P/N](https://www.idealo.de/preisvergleich/OffersOfProduct/210295290_-255r-g10-cu0r1es-hp.html)), 8 предложений:

| Магазин | С доставкой | Возврат | Доставка | Тип |
|---|---|---|---|---|
| nullprozentshop.de | **606,99 €** | не указан | до 02.10 | магазин |
| notebooksbilliger.de | 607,99 € | 30 дн. | до 02.10 | магазин |
| galaxus.de | 607,99 € | 30 дн. | **до 30.10** | магазин |
| jacob.de | 618,75 € | не указан | до 02.10 | магазин |
| heinzsoft-shop.de | 648,90 € | не указан | до 02.10 | магазин |
| eBay (продавец notebooksbilliger) | 663,99 € | 30 дн. | до 07.10 | МП |
| Kaufland (Heinzsoft) | 687,90 € | 14 дн. | до 06.10 | МП |
| Amazon MP (technikbilliger) | 714,44 € | — | до 07.10 | МП |

- **История (API 1Y, 200):** карточка с 11.05.2026, 140 точек, дневной минимум всё время **599,00 €** (min = max = avg 599). ≤ 1100 € — все 140 дней. Подтверждено.
- **Итог — исправлено:** 606,99 + 187,56 (Kingston, Galaxus-МП) + 142,89 (NV3) = **937,44 €**. С Crucial из обычного магазина: 606,99 + 248,89 + 142,89 = 998,77 €. У кандидата было 994,78 € (607,99 + 243,90 без доставки + 142,89).
- Старый SSD 512 ГБ остаётся лишним (второго слота, скорее всего, нет).

### Выборочно: не отброшены ли зря

| P/N | Причина отказа у кандидата | Что проверил | Итог |
|---|---|---|---|
| ProBook 4 G1a 16 `C7SP9ES` | HEVC выключен | QuickSpecs [c09111176, v15, 16.06.2026](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09111176), GRAPHICS: «Hardware acceleration for CODEC H.265/HEVC (High Efficiency Video Coding) is disabled on this platform.» PartSurfer: `N77399-001` SODIMM 16 ГБ + `N77394-001` SSD 1 ТБ → 2×16 / 1 ТБ. idealo ([карточка](https://www.idealo.de/preisvergleich/OffersOfProduct/208030540_-probook-4-g1a-16-c7sp9es-hp.html)): **906,99 €** nullprozentshop.de; 907,99 NBB и Galaxus (30 дн.); API: минимум 699 € (17.12.2025), ≤ 1100 € — 182 из 182 дней | **отказ верный** (ловушка HEVC). По всему остальному — лучший SKU группы; держать в отчёте как «цена ловушки» |
| EliteBook 8 G1a 16 `CT3V8ES` | 1×32 | PartSurfer: из памяти только `N77400-001` «SODIMM 32GB» (у `CT3V9ES` и `AD3F6ET` — только 16 ГБ, т. е. 2×16) | **отказ верный** (одноканал) |
| OmniBook 3 15 `BP1G1EA` | 2×8, «~1170 €» | даташит не перепроверял; цену ноутбука не переснимал | отказ верный **по критериям** (2×8 — «менять обе» → не подходит). Арифметика устарела: с Kingston 187,56 × 2 вышло бы ≈ 695 + 375 = 1070 €, но у Kingston одно предложение, и 2 шт. не гарантированы |

### Опровергнуто / исправлено в `candidates-hp-dell.md`

- `CU0R1ES`: итог 994,78 € → **937,44 €** (планка 243,90 € была без доставки и из магазина; по правилу цены берём минимум у любого продавца — Kingston 187,56 € на Galaxus-МП). С Crucial с доставкой — 998,77 €. Лучший магазин — nullprozentshop.de 606,99 € (у NBB 607,99).
- `CU0R1ES`: «второй M.2 — не проверено» → **нет** (QuickSpecs и MSG: только Primary storage). «45 % NTSC» → противоречие HP-документов (MSG: `P21489-001` low blue light, UWVA 300 нит; описание модели — sRGB 100 %). Добавлено: HDMI 1.4b — внешнее разрешение до 1920×1200.
- `CU0R1ES`: сервис-мануал HP ([P22370-001](https://kaas.hpcloud.hp.com/pdf-public/pdf_11296126_en-US-1.pdf)) пишет «onboard memory … not accessible or upgradeable» — кандидат этот документ не видел. Опровергнуть 1×16 + слот он не может (в нём же SODIMM-модули с процедурой замены), но это повод проверить на месте.
- `CN0Q3EC`: новое — DaaS-юнит у продавца-партнёра HP Renew; «новый» и гарантия — не проверено. Зарядка 65 Вт (BOM), idealo «100 Вт» — ошибка idealo (кандидат это отметил).
- `CN0Q3EC`: «14 дней ≤ 1100 €» — это длина периода; замеров три (17.09, 22.09, 30.09), все 999 €.
- Подтверждено без изменений: HEVC у EliteBook 8 G1a 16 («CODEC is supported»); один M.2 у EliteBook 8 G1a 16 (NBC); CPU обоих; цены ноутбуков на сегодня; SSD NV3 142,89 €.

### Известные проблемы (Notebookcheck)

- **EliteBook 8 G1a 16** — обзор родственной версии на Ryzen AI 7 PRO 350 (Zen 5, 860M; у нашего SKU другая плата — R5 PRO 230), 87 %, 09.09.2025 — [NBC](https://www.notebookcheck.net/HP-EliteBook-8-G1a-16-AI-laptop-review-Redesigned-inside-and-out.1103659.0.html):
  - экран WUXGA IPS без тача: 98,6 % sRGB, 70,4 % AdobeRGB, 439 нит, 1417:1, ΔE 2,2; ШИМ не обнаружен. Сенсорная версия — только ~63 % sRGB. Минус — медленный отклик (чёрный-белый 30,7 мс), 60 Гц;
  - шум под нагрузкой 46–49,5 дБ(A), в простое 22,8 дБ(A); серьёзного троттлинга нет;
  - **DPC latency: LatencyMon показал проблемы, 18 пропущенных кадров за минуту 4K60-видео** — для монтажа это минус, проверить на своём экземпляре (LatencyMon);
  - ремонт: дно на 4 винтах Phillips, 2× SODIMM под алюминиевой пластиной, **один M.2 2280**, Wi-Fi на разъёме.
- **HP 255 G10** — обзор того же корпуса с Athlon Silver 7120U (`C07Q0ES`, распайка, TN-экран — не наша конфигурация), 05.2026 — [NBC](https://www.notebookcheck.net/HP-255-G10-with-7120U-review-Small-budget-low-performance.1293092.0.html):
  - «housing warps a lot» — корпус сильно гнётся;
  - тихий (под нагрузкой до 40,3 дБ(A)), температуры в норме;
  - только USB 5 Гбит/с; блок 45 Вт с круглым штекером;
  - обслуживание простое: дно на 4 винтах и защёлках, доступны вентилятор, батарея, SSD, Wi-Fi. NBC сам ссылается на MSG — это тот же документ 255R G10 (P22370-001).
  - Обзора 255R G10 / 7735U у NBC не нашёл (поиск DuckDuckGo «notebookcheck HP 255 G10 review»).

### Что не проверено

- `CN0Q3EC`: раскладка (2×16 / 1×32), состояние (новый / HP Renew), гарантия HP на серийник. Где искал: QuickSpecs c09120200, PartSurfer (P/N и `#ABD` — пусто), Icecat (404), поиск на asaboshisystems.de (страница не найдена), переход «Zum Shop» с idealo (заблокирован). Остаётся письменный вопрос продавцу.
- `CU0R1ES`: реальный охват цвета панели (QuickSpecs против MSG), HEVC (нет фразы ни «disabled», ни «supported» — DXVA Checker в окно возврата), число слотов по MSG.
- Гарантия: QuickSpecs обеих моделей — «1-year or 3-year … depending on country» / «1-year warranty … depending on country»; срок для DE по P/N — не проверено.
