# HEVC (H.265) на AMD-ноутбуках: кто отключает и как проверить

_30.09.2026, локальная сессия (IP в Германии). Общая картина, механизм у Intel, программы и способы вернуть HEVC — в `../../Intel/notes/hevc-audit.md`. Здесь только то, что касается AMD. Каждый факт со ссылкой; «не проверено» = первоисточник не найден или не открылся._

## Коротко

1. **HP отключает HEVC и на AMD — подтверждено по 6 QuickSpecs** (исправлено при проверке: было «7», а перечислено и найдено 6 документов — c08908497, c08927104, c09111175, c09111176, c09111177, c09111179). В разделе GRAPHICS стоит фраза «Hardware acceleration for CODEC H.265/HEVC … is disabled on this platform». Это ProBook 465 G11, ProBook 4 G1a 14/16, EliteBook 665 G11 и EliteBook 6 G1a 14/16 (AI PC, Ryzen 200).
2. **Популярная AMD-модель в нашем бюджете — с выключенным HEVC.** Пример: HP ProBook 4 G1a 16 `C7SP9ES` (Ryzen 5 230, 32 ГБ, 1 ТБ) — от 899 € на billiger.de (30.09.2026); на idealo тоже 899,00 € у notebooksbilliger.de и nullprozentshop.de, 8 предложений, «Daten vom 30.09.2026 08:00» ([idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/208030540_-probook-4-g1a-16-c7sp9es-hp.html)). ProBook 4 G1a 16 — 8-е место в «Top 10 Business Notebooks» idealo (там же). **Для монтажа не брать.**
3. **Из проверенных QuickSpecs HP на AMD HEVC включён только в EliteBook 8.** EliteBook 8 G1a 14/16 и 8 G2a 16: «HEVC (H.265) CODEC is supported». Но 32 ГБ / 1 ТБ с завода стоят от 1299 € (billiger и idealo, 30.09.2026) — выше потолка. (уточнено при проверке: есть 16" SKU дешевле, но с SSD 512 ГБ — `CN0Q3EC`, 32 ГБ / 512 ГБ, 999 € у asaboshisystems.de, одно предложение; `CT3V7ES`, 24 ГБ / 512 ГБ, от 969 €; idealo, 30.09.2026. Раскладка памяти этих SKU не проверена, SSD 1 ТБ пришлось бы ставить самому — см. «Вывод для выбора».)
4. **Новое поколение HP G2a (2026): HEVC — опция при заказе.** ProBook 4 G2a и EliteBook 6 G2a: «optional feature and must be configured at purchase». По розничному P/N не видно, заказана ли опция → считать «нет».
5. **У потребительских HP на AMD отключение бывает, но не документируется.** Реальный случай — OmniBook 7 Aero 13 на Ryzen AI 300 (Radeon 860M): в DXVA Checker нет ни одного профиля HEVC, OBS не может писать HEVC через AMD. Не помогли переустановка Windows, драйвера и BIOS. В MSG OmniBook 5 16 и Victus (AMD) про HEVC ничего нет → **риск**.
6. **Dell: политика общая для Intel и AMD.** Ars: HP и Dell выключили HEVC, «that has been in Intel and AMD CPUs since 2015». В фактшите Dell Pro 3 14/16 на AMD (Ryzen AI 400) есть та же сноска: HEVC есть только с дискреткой / 4K / Dolby Vision / CyberLink / Linux. В брошюрах Dell 15 DC15255, Dell 16 DC16255 и Dell Pro 14/16 Essential AMD сноски нет — но это не значит, что HEVC там есть.
7. **Lenovo, ASUS, MSI, Medion: отключения на AMD не нашёл.** В ~60 PDF PSREF по AMD-платформам Lenovo слова HEVC нет. Acer: с 06.2026 в Германии часть устройств идёт «без HEVC-кодека», модели и процессоры не названы → риск и для AMD. (уточнено при проверке: по тексту заявления речь, скорее всего, о непредустановленном программном кодеке, а не об аппаратной блокировке, — см. раздел 5.)
8. **Как это выглядит на AMD.** Пропадают `HEVC_VLD_Main` / `HEVC_VLD_Main10`, остаются H.264, VP9 и **AV1** (видно на скриншоте DXVA Checker). По заявлению HP и отчёту пользователя, выключено и кодирование HEVC. Точный механизм у AMD (что читает драйвер AMD) — **не проверено**. Под Linux драйвер amdgpu берёт список кодеков из своей таблицы и OEM-флаг не видит.
9. **Проверка экземпляра (14 дней на возврат):**
   - DXVA Checker: у Radeon 760M/780M/880M/890M в норме `HEVC_VLD_Main` и `HEVC_VLD_Main10` до 8K;
   - `edge://gpu` / `chrome://gpu`;
   - тест кодирования: `ffmpeg -c:v hevc_amf` или HandBrake, пресет «H.265 VCN 2160p 4K».

   Профилей HEVC 4:2:2 у AMD нет и на «здоровой» машине — это ограничение AMD, а не блокировка.
10. **Вывод для выбора:** HP на AMD — только EliteBook 8 (дорого) или не брать. Dell на AMD без дискретки — не брать. Lenovo / ASUS / MSI / Medion — можно, с проверкой по п. 9. Acer — только с проверкой в первые дни.

---

## 1. HP — QuickSpecs AMD-моделей (скачаны 30.09.2026)

PDF: `https://www8.hp.com/h20195/V2/GetPDF.aspx/<doc id>`. Везде фраза стоит в разделе **GRAPHICS**, после строк «Integrated AMD Radeon™ Graphics» и «HDMI 2.1».

### 1.1 Три формулировки, как у Intel

| Что написано в GRAPHICS | Значит |
|---|---|
| «Hardware acceleration for CODEC H.265/HEVC (High Efficiency Video Coding) is disabled on this platform.» | **HEVC выключен** |
| «Hardware Acceleration HEVC (H.265) CODEC is an optional feature and must be configured at purchase.» | опция при заказе (CTO); розничный SKU → считать «нет» |
| «Hardware Acceleration HEVC (H.265) CODEC is supported.» | **HEVC есть** |
| фразы нет | нет данных (бывает и у выключенных — см. OmniBook) |

### 1.2 По моделям

| Модель (AMD) | CPU в QuickSpecs | Документ, версия, дата | HEVC |
|---|---|---|---|
| ProBook 465 16 G11 | Ryzen 3/5/7 7x35U | [c08908497](https://www8.hp.com/h20195/V2/GetPDF.aspx/c08908497), DA17328, v10, 16.09.2025 | **ВЫКЛ** («is disabled on this platform») |
| EliteBook 665 16 G11 | Ryzen 7x35U (PRO) | [c08927104](https://www8.hp.com/h20195/V2/GetPDF.aspx/c08927104), DA17333, v11, 19.09.2025 | **ВЫКЛ** |
| ProBook 4 G1a 14 (и G1ah) | Ryzen 3 210 … Ryzen 7 255H | [c09111175](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09111175), v14, 16.06.2026 | **ВЫКЛ** |
| ProBook 4 G1a 16 (и G1ah) | Ryzen 3 210 … Ryzen 7 255H | [c09111176](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09111176), v15, 16.06.2026 | **ВЫКЛ** |
| EliteBook 6 G1a 14 AI PC (и G1ah) | Ryzen 3 210 … Ryzen 7 255H (исправлено при проверке: было «Ryzen 5 230 …», в таблице PROCESSORS c09111177 есть и Ryzen 3 210) | [c09111177](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09111177), v17, 15.09.2026 | **ВЫКЛ** |
| EliteBook 6 G1a 16 AI PC (и G1ah) | Ryzen 3 210 … Ryzen 7 255H | [c09111179](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09111179), v17, 15.09.2026 | **ВЫКЛ** |
| EliteBook 6 G1a 14 Next Gen AI PC | Ryzen AI 5 340 … AI 7 PRO 350 | [c09111178](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09111178), v13, 15.09.2026 | фразы нет → нет данных |
| EliteBook 8 G1a 14 AI PC | Ryzen 5 PRO 230, 7 PRO 250 | [c09120198](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09120198), v18, 11.09.2026 | **ВКЛ** («CODEC is supported») |
| EliteBook 8 G1a 14 Next Gen AI PC | Ryzen AI 300 | [c09120199](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09120199), v18, 02.09.2026 | **ВКЛ** |
| EliteBook 8 G1a 16 AI PC | Ryzen 5 230 … Ryzen 7 PRO 250 | [c09120200](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09120200), v21, 11.09.2026 | **ВКЛ** |
| EliteBook 8 G1a 16 Next Gen AI PC | Ryzen AI 5 340 … AI 7 PRO 350 | [c09120201](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09120201), v19, 02.09.2026 | **ВКЛ** |
| EliteBook 8 G2a 16 Next Gen AI PC | Ryzen AI 400 | [c09233498](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09233498), v18, 08.09.2026 | **ВКЛ** |
| ProBook 4 G2a 14 / 16 Next Gen AI PC | Ryzen AI 7 450 и др. | [c09228215](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09228215) / [c09228216](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09228216), v12, 24.08.2026 | **опция при заказе** |
| EliteBook 6 G2a 14 / 16 AI PC | Ryzen 3 205 … Ryzen 7 250 / 253 (серия 200) (исправлено при проверке: было «Ryzen 5 216 … Ryzen 7 250»; в c09236063/64 есть Ryzen 3 205, 210 и Ryzen 7 253, 249, 217) | [c09236063](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09236063) v16 / [c09236064](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09236064) v15, 28.09.2026 | **опция при заказе** |
| EliteBook 6 G2a 14 / 16 Next Gen AI PC | Ryzen AI 7 450 и др. | [c09236065](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09236065) / [c09236066](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09236066), v12, 28.09.2026 | **опция при заказе** |
| HP 255 15.6 G10 | Ryzen 5 7530U, 7 7730U и др. | [c08479497](https://www8.hp.com/h20195/V2/GetPDF.aspx/c08479497), DA17182, v12, 07.05.2025 | фразы нет (в GRAPHICS только «Support HD decode, DX12, HDMI 1.4b») → нет данных |
| HP 255R 15.6 G10 | Ryzen 7x35U | [c09053765](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09053765), DA17371, v7, 06.03.2026 | фразы нет → нет данных |
| HP 255 15.6 G9 | Ryzen 5000 | c08017466 — **не открылся** (www8: 503, h20195: DNS failure, 30.09.2026). При проверке: заведомо несуществующий id (c01234567) даёт у www8 тот же 503 «DNS failure», так что сам номер c08017466 тоже **не проверен** | по заявлению HP «200 Series G9» — **ВЫКЛ**; сам QuickSpecs не проверен. Для сравнения, у HP 250R G9 (Intel) фраза есть: [c08894835](https://www8.hp.com/h20195/V2/GetPDF.aspx/c08894835), v13, 06.03.2026 |
| HP 255 G11 | — | на billiger.de такой модели нет (поиск 30.09.2026), QuickSpecs не нашёл | не проверено (возможно, модели нет) |
| «HP 250 AMD» | — | на billiger так подписан «HP 250 G10 AMD Ryzen 3 7320U» ([поиск](https://www.billiger.de/search?searchstring=HP+255+G11)); по CPU это, скорее всего, 255 G10 | см. 255 G10; не проверено |
| ZBook Ultra 14 G1a | Ryzen AI Max (PRO) 380–395 | [c09119722](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09119722), v10, 16.09.2026 | фразы нет → нет данных (14", вне бюджета) |
| ZBook Power 16 G11 A | Ryzen 8040HS | c08954703 — **не открылся** (503, 30.09.2026; как и у 255 G9, 503 не отличает сбой от неверного id) | не проверено |

- Когда фраза появилась, по истории версий не видно. Гипотеза — 17.06.2024: в истории 465 G11 и 665 G11 в этот день записано «Added Graphics Section» (V4→V5 и V3→V4). Не проверено: старых версий PDF у меня нет.
- EliteBook 8 G1a 16 (c09120200): **2 × SODIMM**, варианты 32 ГБ = 2×16 или 1×32. У EliteBook 8 G2a 16 (c09233498) два варианта: 2×SODIMM DDR5 или распаянная LPDDR5X без слотов.
- Страница спецификаций конкретного SKU на hp.com про HEVC молчит. Проверил EliteBook 8 G2a 16 `DL9U0ET` ([hp.com/at-de](https://www.hp.com/at-de/products/laptops/product-details/product-specifications/2103952105), 30.09.2026). Для G2a нельзя узнать, заказана ли опция HEVC у розничного P/N — **не проверено**.

### 1.3 Потребительские HP на AMD (QuickSpecs нет)

| Линейка | Документ | HEVC |
|---|---|---|
| OmniBook 7 Aero 13 Next Gen AI (13-bg1000, `B4NF1AV`, Radeon 860M) | [HP Community, 04.07.2025](https://h30434.www3.hp.com/t5/Notebook-Video-Display-and-Touch/H265-HEVC-HW-encoder-and-decoder-not-available/td-p/9431209) | **ВЫКЛ** по отчёту пользователя (доверие: среднее — один пост со скриншотом, ответа HP по сути нет). Подробности в разделе 3 |
| OmniBook 5 16 Next Gen AI (16-ag1xxx, Ryzen AI 300) | [MSG pdf_10259267](https://kaas.hpcloud.hp.com/pdf-public/pdf_10259267_en-US-1.pdf) (изм. 28.07.2025) | в MSG слова HEVC нет → нет данных, **риск**; память распаяна (`../../Intel/notes/sweep-dell-hp.md`) |
| OmniBook 5 16 (16-cf0xxx, Ryzen AI 400) | [MSG pdf_13177184](https://kaas.hpcloud.hp.com/pdf-public/pdf_13177184_en-US-1.pdf) (изм. 17.03.2026) | в MSG нет → нет данных, риск |
| OmniBook 7 16 AMD | документ не нашёл | не проверено |
| HP 15-fc (Ryzen 7020/7030) | документ не нашёл | не проверено |
| Victus 15 (15-fb3xxx, Ryzen 8945HS и др.) | [MSG pdf_11551834](https://kaas.hpcloud.hp.com/pdf-public/pdf_11551834_en-US-1.pdf) (изм. 01.08.2025) | в MSG нет → нет данных. Работает ли NVDEC у RTX при флаге — не проверено |
| Victus 16 (16-s0xxx, Ryzen 7840HS и др.) | [MSG pdf_7911438](https://kaas.hpcloud.hp.com/pdf-public/pdf_7911438_en-US-1.pdf) (изм. 31.07.2025) | в MSG нет → нет данных |
| OmniDesk M02-0000a (`B5TQ8AA`, Ryzen 7 8700G, настольный) | [smith6612.me, 19.04.2026](https://smith6612.me/2026/04/19/its-me-i-started-the-hevc-disablement-press-storm/) | **ВЫКЛ** «in firmware», хотя в QuickSpecs этого нет. Показывает, что у HP бывает недокументированное отключение и на AMD |

---

## 2. Dell — политика распространяется и на AMD

- Ars (20.04.2026): «Dell and HP disabled HEVC support that has been in Intel and AMD CPUs since 2015». AMD на запрос не ответила — [Ars](https://arstechnica.com/gadgets/2026/04/lawsuits-licensing-and-royalties-are-complicating-4k-video-support-in-gadgets/).
- Заявление Dell для Ars не делает различий по CPU: HEVC есть только в «premium systems» и в конфигурациях с 4K / дискреткой / Dolby Vision / CyberLink — [Ars, 20.11.2025](https://arstechnica.com/gadgets/2025/11/hp-and-dell-disable-hevc-support-built-into-their-laptops-cpus/).
- Dell KB 000222670: условия те же, привязки к CPU нет — [Dell KB](https://www.dell.com/support/kbdoc/en-us/000222670/how-to-identify-if-you-cannot-view-4k-video-content-due-to-a-hevc-codec).

| Модель Dell (AMD) | Документ | Что про HEVC |
|---|---|---|
| **Dell Pro 3 14/16 AMD** (P314265 / P316265, Ryzen AI 400, Radeon 840M/860M) | [фактшит Dell Pro 3 14/16](https://www.delltechnologies.com/asset/en-us/products/laptops-and-2-in-1s/selling-competitive/dell-pro-3-14-16-laptop-product-fact-sheet.pdf) (отдаётся как .pptx, изм. 23.09.2026) | В AMD-таблице (слайд 5, P314265/P316265) у GRAPHICS сноски «1,4». Сноска 4: HEVC «is supported on configurations with a discrete graphics card, Linux/Thin OS, built in 4K panel, Dolby Vision or CyberLink Blue-ray player». **Подтверждение для AMD** (уточнено при проверке: слайд со сносками в файле один, он подписан «P314260, P316260», т. е. Intel-моделями; AMD-таблица ссылается на ту же сноску 4) |
| Dell Pro 14/16 Essential AMD (PC14255 / PC16255, Ryzen 200 / AI 300) | [брошюра AMD](https://www.delltechnologies.com/asset/en-us/products/laptops-and-2-in-1s/technical-support/dell-pro-14-16-laptop-product-brochure-amd.pdf) (изм. 18.06.2026) | Слова HEVC нет. У Intel-версии той же линейки (PC14250/PC16250) сноска есть — [брошюра Intel](https://www.delltechnologies.com/asset/en-in/products/laptops-and-2-in-1s/technical-support/dell-pro-14-16-laptop-product-brochure.pdf). По политике — считать выключенным |
| Dell 15 DC15255 (Ryzen 7320U … 7730U) | [брошюра](https://www.delltechnologies.com/asset/en-us/products/laptops-and-2-in-1s/briefs-summaries/dell-15-dc15255-laptop-product-brochure.pdf.external) (06.08.2025); [Owner's Manual, GPU](https://www.dell.com/support/manuals/en-us/dell-dc15255-laptop/dell_15_dc15255_owners_manual/gpuintegrated?guid=guid-e0431804-e795-4215-9cd1-1dfb991daa1d&lang=en-us) (открыт в Chrome 30.09.2026) | Слова HEVC нет ни там, ни там → по политике считать выключенным |
| Dell 16 DC16255 / DC16256 (Ryzen 200 / AI 300) | [брошюра](https://www.delltechnologies.com/asset/en-us/products/laptops-and-2-in-1s/briefs-summaries/dell-16-dc16255-dc16256-amd-laptop-product-brochure.pdf.external) (26.08.2025) | нет → считать выключенным |
| Dell 16 Plus AMD | брошюру не нашёл (угаданные URL дают 404) | не проверено; политика та же |
| Dell Pro Max 16 AMD | [брошюра](https://www.delltechnologies.com/asset/en-us/products/workstations/technical-support/dell-pro-max-16-workstation-amd-product-brochure.pdf) (27.05.2026) | нет; вне бюджета |

- Отчётов пользователей Dell именно на AMD (DXVA Checker и т. п.) не нашёл. Все найденные случаи — на Intel (`../../Intel/notes/hevc-audit.md`).
- Патч [Dell_HEVC_Patch](https://github.com/jimmytheshoebill/Dell_HEVC_Patch) правит DLL драйвера **Intel**. Для AMD он не применим. Аналога для AMD не нашёл.

---

## 3. Как это работает на AMD

| Вопрос | Ответ | Источник, доверие |
|---|---|---|
| Где стоит запрет | Бит в ACPI/SKU-прошивке, записывается на заводе. Windows (DirectX / Media Foundation) не видит аппаратный путь HEVC | [smith6612](https://smith6612.me/2026/04/19/its-me-i-started-the-hevc-disablement-press-storm/) — для HP/Dell в целом, без разбивки Intel/AMD; доверие среднее (расследование одного автора) |
| Соблюдает ли флаг драйвер AMD | Косвенно — да. На OmniBook 7 Aero (AMD) после переустановки Windows, драйвера GPU и обновления BIOS HEVC так и не появился. Какой компонент AMD читает флаг — **не проверено** (для Intel известен разбор DLL, для AMD аналога нет) | [HP Community](https://h30434.www3.hp.com/t5/Notebook-Video-Display-and-Touch/H265-HEVC-HW-encoder-and-decoder-not-available/td-p/9431209); доверие среднее |
| Декод | Выключен. В DXVA Checker на Radeon 860M есть только MJPEG_VLD_AMD, H264_VLD_*, VP9_VLD_Profile0 / 10bit_Profile2, AV1_VLD_Profile0. **HEVC нет вообще** | скриншот в [HP Community](https://h30434.www3.hp.com/t5/Notebook-Video-Display-and-Touch/H265-HEVC-HW-encoder-and-decoder-not-available/td-p/9431209) (смотрел 30.09.2026) |
| Кодирование | Выключено: «I can't record HEVC/H265 video with AMD HW encoder in OBS studio». HP: «encode or decode HEVC content» | HP Community (пользователь); заявление HP в [Ars](https://arstechnica.com/gadgets/2025/11/hp-and-dell-disable-hevc-support-built-into-their-laptops-cpus/) — доверие высокое |
| AV1, H.264, VP9 | Декод остаётся (тот же скриншот). Кодирование AV1 на заблокированной машине — **не проверено** | HP Community |
| Linux | Драйвер amdgpu берёт список кодеков из статической таблицы по версии блока VCN. Учитываются только отключённые на кристалле экземпляры VCN (`harvest_config`), OEM-флаг из ACPI не читается. smith6612: Linux «completely ignores the block bits» | [linux/soc21.c](https://github.com/torvalds/linux/blob/master/drivers/gpu/drm/amd/amdgpu/soc21.c) (`soc21_query_video_codecs`, master на 30.09.2026) — доверие высокое; [smith6612](https://smith6612.me/2026/04/19/its-me-i-started-the-hevc-disablement-press-storm/) |
| Вернуть на Windows | Официально — нет (ни BIOS-опции, ни обновления). Неофициальная подмена ACPI (пост в r/HEVC) — снимает защиту Windows, для рабочей машины не вариант. Reddit в Chrome закрыт («not allowed due to safety restrictions»), пост не читал | `../../Intel/notes/hevc-audit.md`, [smith6612](https://smith6612.me/2026/04/19/its-me-i-started-the-hevc-disablement-press-storm/) |
| Premiere / Resolve | Как у Intel: HEVC декодирует и кодирует процессор. На AMD отдельным тестом **не проверено** (вывод из механизма) | `../../Intel/notes/hevc-audit.md`, [Ars 04.2026](https://arstechnica.com/gadgets/2026/04/lawsuits-licensing-and-royalties-are-complicating-4k-video-support-in-gadgets/) |

---

## 4. Проверка конкретного экземпляра на AMD

Покупать онлайн и проверять в первые дни: 14 дней на отказ (Widerrufsrecht, `../../Intel/notes/market.md`).

1. **DXVA Checker** → вкладка «Decoder Device» — [bluesky-soft](https://bluesky-soft.com/en/DXVAChecker.html). Сверять с таблицей автора программы для AMD — [bluesky-soft (AMD)](https://bluesky-soft.com/en/dxvac/deviceInfo/decoder/amd.html):

   | iGPU | H.264 | HEVC Main | HEVC Main10 | HEVC 4:2:2 / 4:4:4 | VP9 P0 / P2 | AV1 P0 |
   |---|---|---|---|---|---|---|
   | Radeon 740M / 760M / 780M / 880M / 890M, 610M | 4K | 8K | 8K | — | 8K / 8K | 8K |
   | Radeon Graphics (Renoir … Barcelo, Ryzen 5000/7030) | 4K | 8K | 8K | — | 8K / 8K | — |

   - В норме должны быть строки `HEVC_VLD_Main` и `HEVC_VLD_Main10`. Нет ни одной → HEVC заблокирован.
   - Строк HEVC 4:2:2 у AMD **нет и в норме**. Это ограничение железа, а не блокировка (подробно — `amd-codecs.md`).
2. **Браузер без установки ПО:** `edge://gpu` или `chrome://gpu` → «Video Acceleration Information». Должны быть «Decode hevc main», «Decode hevc main 10», а для кодирования — «Encode hevc main» ([StaZhu](https://github.com/StaZhu/enable-chromium-hevc-hardware-decoding)).
3. **dxdiag:** `dxdiag /t %USERPROFILE%\dx.txt` → «DXVA2 Modes» должны содержать `DXVA2_ModeHEVC_VLD_Main` / `Main10` (как у Intel, `../../Intel/notes/hevc-audit.md`).
4. **Тест кодирования через AMF (ffmpeg):** в ffmpeg AMD-кодеры называются `h264_amf`, `hevc_amf`, `av1_amf`; аппаратный декод — `-hwaccel d3d11va` ([AMF wiki, изм. 17.03.2026](https://github.com/GPUOpen-LibrariesAndSDKs/AMF/wiki/FFmpeg-and-AMF-HW-Acceleration)).
   - `ffmpeg -f lavfi -i testsrc2=size=3840x2160:rate=30 -t 10 -c:v hevc_amf -y hevc.mp4` — должен отработать; для сравнения то же с `h264_amf` и `av1_amf`.
   - `ffmpeg -hwaccel d3d11va -i hevc.mp4 -f null -` — смотреть, нет ли ошибки инициализации hwaccel и не ушёл ли декод на CPU (диспетчер задач).
   - Какой именно текст ошибки выдаст ffmpeg на заблокированной машине — **не проверено**.
5. **HandBrake:** Preferences → Video → включить AMD VCN (если система не поддерживается, опция неактивна); пресет «H.265 VCN 2160p 4K» — [HandBrake docs](https://handbrake.fr/docs/en/latest/technical/video-vcn.html). Официально HandBrake поддерживает VCN только у Radeon RX 6000/7000/9000, на iGPU «might work». К тому же HandBrake **не** использует аппаратный декодер. Поэтому это тест только кодирования, и то не строгий.
6. **OBS:** в списке кодеров нет «AMD HW H.265 (HEVC)» → кодирование заблокировано (так нашли проблему на OmniBook 7 Aero, [HP Community](https://h30434.www3.hp.com/t5/Notebook-Video-Display-and-Touch/H265-HEVC-HW-encoder-and-decoder-not-available/td-p/9431209)).
7. **Диспетчер задач** → GPU: нагрузка на видеоблок при проигрывании HEVC 10 бит. Как на AMD называется движок — «Video Decode» или «Video Codec» — **не проверено**.
8. **Не полагаться:**
   - GPU-Z — использует старый API D3D9 ([Dell_HEVC_Patch](https://github.com/jimmytheshoebill/Dell_HEVC_Patch));
   - AMD Software: Adrenalin — показывает ли список декодеров, **не проверено**.

   Для продвинутых: пример `CapabilityManager` из AMF SDK выводит возможности кодеров/декодеров AMF, но его надо собирать из исходников ([AMF samples](https://github.com/GPUOpen-LibrariesAndSDKs/AMF/tree/master/amf/public/samples/CPPSamples)). На заблокированной машине не проверялся.

---

## 5. Остальные бренды на AMD

- **Lenovo:**
  - В PDF PSREF AMD-платформ слова HEVC нет. Сам проверил 30.09.2026: ThinkPad E16 Gen 2/3 AMD, L16 Gen 2 AMD, T16 Gen 4 AMD, ThinkBook 16 G7 ARP, IdeaPad Slim 5 16AKP10 / 16ARP10, IdeaPad Pro 5 16AKP10, IdeaPad Slim 3 15ARP10, V15 G4 AMN. URL вида `https://psref.lenovo.com/syspool/Sys/PDF/<серия>/<платформа>/<платформа>_Spec.pdf`, например [ThinkPad E16 Gen 3 AMD](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_E16_Gen_3_AMD/ThinkPad_E16_Gen_3_AMD_Spec.pdf).
  - Ещё около 50 AMD-платформ PSREF скачал параллельный агент (Legion, LOQ, Yoga, V15 G6, ThinkBook 16 G9 AHP и др.). В их тексте HEVC тоже нет. (при проверке заново скачаны только 10 PDF из списка выше, в них HEVC/H.265 — 0 совпадений. Эти ~50 — **не проверено**.)
  - Отчётов об отключении на Lenovo AMD не нашёл.
  - Статус: **признаков отключения нет, подтверждения «HEVC есть» тоже нет** — как у Intel.
- **ASUS:** сообщений об отключении нет, в т. ч. после соглашения с Nokia 22.06.2026 (`../../Intel/notes/hevc-audit.md`). Статус «нет данных».
- **Acer:** заявление «sowohl mit als auch ohne HEVC-Codec» ([ChannelPartner](https://www.channelpartner.de/article/4187748/acer-und-asus-liefern-wieder.html), [Hardwareluxx](https://www.hardwareluxx.de/index.php/news/allgemein/wirtschaft/69494-patentstreit-mit-nokia-beendet-asus-und-acer-duerfen-in-deutschland-wieder-verkaufen.html)) не называет ни моделей, ни процессоров. Затронуты ли AMD-модели и что именно выключают (расширение Windows или аппаратный профиль) — **не проверено**. Считать риск одинаковым для Intel и AMD. (уточнено при проверке: в том же заявлении Acer сказано, что у продуктов «ohne vorinstallierten HEVC-Codec» поддержку можно включить, поставив ПО из официальных сторонних каналов. Hardwareluxx пишет так же: «ohne vorinstallierte Unterstützung». То есть речь, скорее всего, о непредустановленном программном кодеке, а не о блокировке, как у HP. Для Premiere / Resolve это не важно; аппаратная блокировка у Acer не подтверждена.)
- **MSI, Medion:** сообщений нет (поиск 30.09.2026). Статус «нет данных».

---

## 6. Итоговая таблица: бренд / линейка AMD → HEVC

| Бренд / линейка (AMD) | HEVC | Основание |
|---|---|---|
| HP ProBook 465 G11 | **отключён (подтверждено)** | QuickSpecs c08908497 |
| HP ProBook 4 G1a 14 / 16 | **отключён (подтверждено)** | c09111175, c09111176 |
| HP EliteBook 665 G11 | **отключён (подтверждено)** | c08927104 |
| HP EliteBook 6 G1a 14 / 16 (AI PC, Ryzen 200) | **отключён (подтверждено)** | c09111177, c09111179 |
| HP 255 G9 | отключён (заявление HP о «200 Series G9»; QuickSpecs не открылся) | [Ars](https://arstechnica.com/gadgets/2025/11/hp-and-dell-disable-hevc-support-built-into-their-laptops-cpus/) |
| HP OmniBook 7 Aero 13 (AMD) | отключён (отчёт пользователя) | HP Community |
| HP ProBook 4 G2a, EliteBook 6 G2a | опция при заказе → для розницы считать «нет» | c09228215/16, c09236063–66 |
| HP EliteBook 8 G1a 14 / 16, EliteBook 8 G2a 16 | **включён (подтверждено)** | c09120198–c09120201, c09233498 |
| HP EliteBook 6 G1a 14 Next Gen, HP 255 / 255R G10, ZBook Ultra G1a | нет данных (фразы нет) | QuickSpecs |
| HP OmniBook 5 / 7 16 AMD, HP 15-fc, Victus 15/16 AMD, ZBook Power G11 A | нет данных, **риск** (у потребительских HP на AMD бывает недокументированное отключение) | MSG / smith6612 / HP Community |
| Dell Pro 3 14/16 AMD | **отключён без dGPU / 4K / Dolby Vision / CyberLink / Linux (подтверждено сноской)** | фактшит Dell Pro 3 |
| Dell 15 DC15255, Dell 16 DC16255/56, Dell Pro 14/16 Essential AMD, Dell 16 Plus AMD | нет данных в документах; по общей политике Dell **считать отключённым** | Ars, Dell KB |
| Lenovo (ThinkPad / ThinkBook / IdeaPad / V / LOQ / Legion на AMD) | нет данных; признаков отключения нет | PSREF, поиск |
| ASUS, MSI, Medion (AMD) | нет данных | поиск |
| Acer (AMD, Германия, после 22.06.2026) | нет данных, **повышенный риск** | ChannelPartner, Hardwareluxx |

**Вывод для выбора:**
- HP ProBook 4 G1a / EliteBook 6 G1a / ProBook 465 / EliteBook 665 — **исключить**. Это главная ловушка: например, `C7SP9ES` (ProBook 4 G1a 16, Ryzen 5 230, 32 ГБ / 1 ТБ) от 899 € ([billiger.de, 30.09.2026](https://www.billiger.de/products/5406909275-hp-probook-4-g1a-16-amd-ryzen-5-230-32-gb-ram-1-tb-ssd-c7sp9es)) подходит по цене и памяти, но HEVC выключен.
- HP G2a — исключить, если продавец не подтвердит опцию HEVC письменно.
- HP EliteBook 8 (G1a 14/16, G2a 16) — единственная подтверждённая AMD-линейка HP с HEVC. Но 32 ГБ / 1 ТБ `CT3V8ES` (16", Ryzen 7 250, FreeDOS) — от 1299 € ([billiger.de, 30.09.2026](https://www.billiger.de/products/5460257445-hp-elitebook-8-g1a-16-amd-ryzen-7-250-32-gb-ram-1-tb-ssd-radeon-780m-freedos-silber)); на [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/208652377_-elitebook-8-g1a-16-ct3v8es-hp.html) тоже 1299,00 € у notebooksbilliger.de и nullprozentshop.de (30.09.2026 08:01). Выше потолка. Раскладка его памяти (2×16 или 1×32) — не проверено: в Icecat SKU нет.
  - (уточнено при проверке) «Выше потолка» верно только для заводских 32 ГБ / 1 ТБ. Пограничный вариант — [`CN0Q3EC`](https://www.idealo.de/preisvergleich/OffersOfProduct/214137501_-elitebook-8-g1a-16-cn0q3ec-hp.html) (Ryzen 5 230, 32 ГБ / 512 ГБ, Win 11 Pro): 999 € у asaboshisystems.de, одно предложение, idealo 30.09.2026. Нужна замена SSD на 1 ТБ, её цена не проверена. Раскладка памяти (2×16 или 1×32) и HEVC для этого SKU не проверены: в Icecat SKU нет. По QuickSpecs c09120200 у модели 2 SODIMM и варианты 32 ГБ = 2×16 или 1×32.
- Потребительские HP на AMD — только с проверкой по разделу 4, и лучше вообще не брать.
- Dell на AMD без дискретки и 4K — исключить.
- Lenovo / ASUS / MSI / Medion на AMD — допустимы, но проверить по разделу 4 в первые дни после покупки.
- Acer — то же, с повышенным вниманием.

---

## Источники

- HP QuickSpecs (скачаны 30.09.2026, `https://www8.hp.com/h20195/V2/GetPDF.aspx/<id>`):
  - ProBook: [c08908497](https://www8.hp.com/h20195/V2/GetPDF.aspx/c08908497), [c09111175](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09111175), [c09111176](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09111176), [c09228215](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09228215), [c09228216](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09228216);
  - EliteBook 6 / 665: [c08927104](https://www8.hp.com/h20195/V2/GetPDF.aspx/c08927104), [c09111177](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09111177), [c09111178](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09111178), [c09111179](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09111179), [c09236063](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09236063), [c09236064](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09236064), [c09236065](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09236065), [c09236066](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09236066);
  - EliteBook 8: [c09120198](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09120198), [c09120199](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09120199), [c09120200](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09120200), [c09120201](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09120201), [c09233498](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09233498);
  - HP 250/255 и ZBook: [c08479497](https://www8.hp.com/h20195/V2/GetPDF.aspx/c08479497), [c09053765](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09053765), [c09053764](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09053764) (250R G10, Intel, фразы нет), [c08894835](https://www8.hp.com/h20195/V2/GetPDF.aspx/c08894835), [c09119722](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09119722);
  - не открылись: c08017466 (255 G9), c08954703 (ZBook Power 16 G11 A).
- HP MSG: [OmniBook 5 16 (16-ag1xxx)](https://kaas.hpcloud.hp.com/pdf-public/pdf_10259267_en-US-1.pdf), [OmniBook 5 16 (16-cf0xxx)](https://kaas.hpcloud.hp.com/pdf-public/pdf_13177184_en-US-1.pdf), [Victus 15 (15-fb3xxx)](https://kaas.hpcloud.hp.com/pdf-public/pdf_11551834_en-US-1.pdf), [Victus 16 (16-s0xxx)](https://kaas.hpcloud.hp.com/pdf-public/pdf_7911438_en-US-1.pdf)
- HP, прочее: [HP Community — OmniBook 7 Aero AMD, 04.07.2025](https://h30434.www3.hp.com/t5/Notebook-Video-Display-and-Touch/H265-HEVC-HW-encoder-and-decoder-not-available/td-p/9431209) (через Chrome; из curl — Cloudflare 403), [hp.com — EliteBook 8 G2a 16 DL9U0ET](https://www.hp.com/at-de/products/laptops/product-details/product-specifications/2103952105)
- Dell: [фактшит Dell Pro 3 14/16](https://www.delltechnologies.com/asset/en-us/products/laptops-and-2-in-1s/selling-competitive/dell-pro-3-14-16-laptop-product-fact-sheet.pdf), [брошюра Dell Pro 14/16 AMD](https://www.delltechnologies.com/asset/en-us/products/laptops-and-2-in-1s/technical-support/dell-pro-14-16-laptop-product-brochure-amd.pdf), [брошюра Dell Pro 14/16 Intel](https://www.delltechnologies.com/asset/en-in/products/laptops-and-2-in-1s/technical-support/dell-pro-14-16-laptop-product-brochure.pdf), [Dell 15 DC15255](https://www.delltechnologies.com/asset/en-us/products/laptops-and-2-in-1s/briefs-summaries/dell-15-dc15255-laptop-product-brochure.pdf.external), [Dell 16 DC16255/56](https://www.delltechnologies.com/asset/en-us/products/laptops-and-2-in-1s/briefs-summaries/dell-16-dc16255-dc16256-amd-laptop-product-brochure.pdf.external), [Dell Pro Max 16 AMD](https://www.delltechnologies.com/asset/en-us/products/workstations/technical-support/dell-pro-max-16-workstation-amd-product-brochure.pdf), [Owner's Manual DC15255 — GPU](https://www.dell.com/support/manuals/en-us/dell-dc15255-laptop/dell_15_dc15255_owners_manual/gpuintegrated?guid=guid-e0431804-e795-4215-9cd1-1dfb991daa1d&lang=en-us), [Dell KB 000222670](https://www.dell.com/support/kbdoc/en-us/000222670/how-to-identify-if-you-cannot-view-4k-video-content-due-to-a-hevc-codec)
- Публикации: [Ars Technica, 20.11.2025](https://arstechnica.com/gadgets/2025/11/hp-and-dell-disable-hevc-support-built-into-their-laptops-cpus/), [Ars Technica, 20.04.2026](https://arstechnica.com/gadgets/2026/04/lawsuits-licensing-and-royalties-are-complicating-4k-video-support-in-gadgets/), [smith6612.me, 19.04.2026](https://smith6612.me/2026/04/19/its-me-i-started-the-hevc-disablement-press-storm/), [devinthreethousand, 21.11.2025](https://devinthreethousand.substack.com/p/hevc-hardware-support-being-removed) (про AMD ничего конкретного)
- Acer/ASUS: [ChannelPartner](https://www.channelpartner.de/article/4187748/acer-und-asus-liefern-wieder.html), [Hardwareluxx, 22.06.2026](https://www.hardwareluxx.de/index.php/news/allgemein/wirtschaft/69494-patentstreit-mit-nokia-beendet-asus-und-acer-duerfen-in-deutschland-wieder-verkaufen.html)
- Техника и проверка:
  - DXVA Checker: [программа](https://bluesky-soft.com/en/DXVAChecker.html), [таблица декодеров AMD](https://bluesky-soft.com/en/dxvac/deviceInfo/decoder/amd.html);
  - AMF: [AMF wiki — FFmpeg](https://github.com/GPUOpen-LibrariesAndSDKs/AMF/wiki/FFmpeg-and-AMF-HW-Acceleration), [AMF samples (CapabilityManager)](https://github.com/GPUOpen-LibrariesAndSDKs/AMF/tree/master/amf/public/samples/CPPSamples);
  - [HandBrake — AMD VCN](https://handbrake.fr/docs/en/latest/technical/video-vcn.html), [Linux amdgpu soc21.c](https://github.com/torvalds/linux/blob/master/drivers/gpu/drm/amd/amdgpu/soc21.c), [StaZhu (chrome://gpu)](https://github.com/StaZhu/enable-chromium-hevc-hardware-decoding), [Dell_HEVC_Patch](https://github.com/jimmytheshoebill/Dell_HEVC_Patch).
- Lenovo PSREF (30.09.2026): [ThinkPad E16 Gen 3 AMD](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_E16_Gen_3_AMD/ThinkPad_E16_Gen_3_AMD_Spec.pdf), [ThinkPad E16 Gen 2 AMD](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_E16_Gen_2_AMD/ThinkPad_E16_Gen_2_AMD_Spec.pdf), [ThinkBook 16 G7 ARP](https://psref.lenovo.com/syspool/Sys/PDF/ThinkBook/ThinkBook_16_G7_ARP/ThinkBook_16_G7_ARP_Spec.pdf), [ThinkPad L16 Gen 2 AMD](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_L16_Gen_2_AMD/ThinkPad_L16_Gen_2_AMD_Spec.pdf), [ThinkPad T16 Gen 4 AMD](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_T16_Gen_4_AMD/ThinkPad_T16_Gen_4_AMD_Spec.pdf), [IdeaPad Slim 5 16AKP10](https://psref.lenovo.com/syspool/Sys/PDF/IdeaPad/IdeaPad_Slim_5_16AKP10/IdeaPad_Slim_5_16AKP10_Spec.pdf), [IdeaPad Slim 5 16ARP10](https://psref.lenovo.com/syspool/Sys/PDF/IdeaPad/IdeaPad_Slim_5_16ARP10/IdeaPad_Slim_5_16ARP10_Spec.pdf), [IdeaPad Pro 5 16AKP10](https://psref.lenovo.com/syspool/Sys/PDF/IdeaPad/IdeaPad_Pro_5_16AKP10/IdeaPad_Pro_5_16AKP10_Spec.pdf), [IdeaPad Slim 3 15ARP10](https://psref.lenovo.com/syspool/Sys/PDF/IdeaPad/IdeaPad_Slim_3_15ARP10/IdeaPad_Slim_3_15ARP10_Spec.pdf), [V15 G4 AMN](https://psref.lenovo.com/syspool/Sys/PDF/Lenovo/Lenovo_V15_G4_AMN/Lenovo_V15_G4_AMN_Spec.pdf)
- Цены idealo (30.09.2026, добавлено при проверке): [ProBook 4 G1a 16 C7SP9ES](https://www.idealo.de/preisvergleich/OffersOfProduct/208030540_-probook-4-g1a-16-c7sp9es-hp.html), [EliteBook 8 G1a 16 CT3V8ES](https://www.idealo.de/preisvergleich/OffersOfProduct/208652377_-elitebook-8-g1a-16-ct3v8es-hp.html), [EliteBook 8 G1a 16 CN0Q3EC](https://www.idealo.de/preisvergleich/OffersOfProduct/214137501_-elitebook-8-g1a-16-cn0q3ec-hp.html)
- Цены: [billiger.de — ProBook 4 G1a 16 C7SP9ES](https://www.billiger.de/products/5406909275-hp-probook-4-g1a-16-amd-ryzen-5-230-32-gb-ram-1-tb-ssd-c7sp9es), [billiger.de — EliteBook 8 G1a 16 CT3V8ES](https://www.billiger.de/products/5460257445-hp-elitebook-8-g1a-16-amd-ryzen-7-250-32-gb-ram-1-tb-ssd-radeon-780m-freedos-silber) (обе 30.09.2026)
- Закрыто или не читалось: reddit.com (в Chrome «not allowed due to safety restrictions», из curl — заглушка); h20195.www2.hp.com (из curl нет соединения, в Chrome «DNS failure» 30.09.2026 — PDF брал через www8.hp.com).

---

## Проверка (скептик, 30.09.2026)

Проверял заново по первоисточникам: 20 QuickSpecs скачаны с www8.hp.com, 4 MSG, 10 PDF PSREF, фактшит и брошюры Dell, обе статьи Ars, smith6612, ChannelPartner, Hardwareluxx, soc21.c / nv.c (master), bluesky-soft, HandBrake, AMF wiki. Через Chrome смотрел HP Community и idealo (своя вкладка, закрыта).

| # | Утверждение | Вердикт | Чем проверено |
|---|---|---|---|
| 1 | Фраза «…is disabled on this platform» в QuickSpecs 465 G11, 665 G11, ProBook 4 G1a 14/16, EliteBook 6 G1a 14/16 AI PC | **подтверждено**, но документов **6, а не 7** — исправлено в «Коротко» | pdftotext всех шести: [c08908497](https://www8.hp.com/h20195/V2/GetPDF.aspx/c08908497), [c08927104](https://www8.hp.com/h20195/V2/GetPDF.aspx/c08927104), [c09111175](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09111175), [c09111176](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09111176), [c09111177](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09111177), [c09111179](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09111179) |
| 2 | Версии и даты этих QuickSpecs (v10 16.09.2025, v11 19.09.2025, v14/v15 16.06.2026, v17 15.09.2026) | **подтверждено** | колонтитулы тех же PDF |
| 3 | EliteBook 8 G1a 14/16 (AI PC и Next Gen) и 8 G2a 16: «HEVC (H.265) CODEC is supported», версии v18/v18/v21/v19/v18 | **подтверждено** | [c09120198](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09120198)…[c09120201](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09120201), [c09233498](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09233498) |
| 4 | ProBook 4 G2a 14/16 и EliteBook 6 G2a 14/16 (обе ветки): «optional feature and must be configured at purchase» | **подтверждено** (все 6 PDF: v12 24.08.2026; v16/v15/v12/v12 28.09.2026) | [c09228215](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09228215), [c09228216](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09228216), [c09236063](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09236063)…[c09236066](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09236066) |
| 5 | EliteBook 6 G1a 14 Next Gen (c09111178), HP 255 G10, 255R G10, ZBook Ultra 14 G1a — фразы нет | **подтверждено** (0 совпадений HEVC/H.265; у 255 G10 в GRAPHICS «Support HD decode, DX12, HDMI 1.4b») | [c09111178](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09111178), [c08479497](https://www8.hp.com/h20195/V2/GetPDF.aspx/c08479497), [c09053765](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09053765), [c09119722](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09119722) |
| 6 | Диапазоны CPU в таблице 1.2 | **исправлено** для 2 строк: EliteBook 6 G1a 14 начинается с Ryzen 3 210; EliteBook 6 G2a AI PC — Ryzen 3 205 … Ryzen 7 250/253. Остальные совпадают | таблицы PROCESSORS в c09111177, c09236063, c09236064 |
| 7 | Память: EliteBook 8 G1a 16 — 2 SODIMM, 32 ГБ = 2×16 или 1×32; EliteBook 8 G2a 16 — либо 2 SODIMM DDR5, либо LPDDR5X без слотов; ProBook 4 G1a 16 — 2 SODIMM | **подтверждено** | разделы MEMORY в [c09120200](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09120200), [c09233498](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09233498), [c09111176](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09111176) |
| 8 | `C7SP9ES` = ProBook 4 G1a 16, Ryzen 5 230, 32 ГБ / 1 ТБ, от 899 € | **подтверждено**; добавлены магазины: idealo 899,00 € — notebooksbilliger.de и nullprozentshop.de, 8 предложений (30.09.2026 08:00). Страница товара на billiger при проверке отдавала 500, цена 899,00 € видна в [поиске billiger](https://www.billiger.de/search?searchstring=C7SP9ES). Раскладка памяти SKU (2×16 или 1×32) — не проверено, в Icecat SKU нет | [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/208030540_-probook-4-g1a-16-c7sp9es-hp.html) |
| 9 | EliteBook 8 с 32 ГБ / 1 ТБ — от 1299 €, выше потолка | **подтверждено** для `CT3V8ES` (idealo 1299,00 €: notebooksbilliger.de, nullprozentshop.de). **Вывод смягчён**: есть `CN0Q3EC` (32 ГБ / 512 ГБ) за 999 € и `CT3V7ES` (24 ГБ / 512 ГБ) от 969 €. Путь через замену SSD возможен, но раскладка памяти и цена SSD не проверены | [idealo CT3V8ES](https://www.idealo.de/preisvergleich/OffersOfProduct/208652377_-elitebook-8-g1a-16-ct3v8es-hp.html), [idealo CN0Q3EC](https://www.idealo.de/preisvergleich/OffersOfProduct/214137501_-elitebook-8-g1a-16-cn0q3ec-hp.html) |
| 10 | HP Community, OmniBook 7 Aero 13 (B4NF1AV, Radeon 860M): в DXVA Checker нет HEVC; OBS не пишет HEVC; не помогли переустановка Windows, драйвер, BIOS; пост 04.07.2025 | **подтверждено** (скриншот: MJPEG, 6 × H264, VP9 Profile0 / 10bit Profile2, AV1 Profile0). Ответ HP от 06.07.2025 — общие советы, по сути вопроса ответа нет | [HP Community](https://h30434.www3.hp.com/t5/Notebook-Video-Display-and-Touch/H265-HEVC-HW-encoder-and-decoder-not-available/td-p/9431209) (Chrome) |
| 11 | Ars: «Dell and HP disabled HEVC support that has been in Intel and AMD CPUs since 2015», AMD не ответила; HP: «600 Series G11, 400 Series G11, and 200 Series G9»; Dell: «premium systems» | **подтверждено** дословно | [Ars 20.11.2025](https://arstechnica.com/gadgets/2025/11/hp-and-dell-disable-hevc-support-built-into-their-laptops-cpus/), [Ars 20.04.2026](https://arstechnica.com/gadgets/2026/04/lawsuits-licensing-and-royalties-are-complicating-4k-video-support-in-gadgets/) |
| 12 | Фактшит Dell Pro 3 14/16 AMD: сноска 4 про HEVC, файл .pptx от 23.09.2026 | **подтверждено с оговоркой**: сноска 4 стоит на единственном слайде дисклеймеров, подписанном Intel-номерами P314260/P316260. AMD-таблица (P314265/P316265) ссылается на «1,4» | [фактшит](https://www.delltechnologies.com/asset/en-us/products/laptops-and-2-in-1s/selling-competitive/dell-pro-3-14-16-laptop-product-fact-sheet.pdf) (docProps: modified 2026-09-23) |
| 13 | В брошюрах Dell Pro 14/16 AMD, Dell 15 DC15255, Dell 16 DC16255/56 слова HEVC нет, в Intel-брошюре Dell Pro 14/16 есть | **подтверждено** (0 / 0 / 0 и 3 совпадения) | ссылки в разделе 2 |
| 14 | Linux: `soc21_query_video_codecs` выбирает статическую таблицу по версии VCN и учитывает только `harvest_config` | **подтверждено** (master на 30.09.2026). Уточнение: soc21.c — это VCN 4.x (Radeon 740M–890M); Ryzen 7x35U / 5000 (VCN 3.x) обрабатывает `nv_query_video_codecs` в nv.c, логика та же | [soc21.c](https://github.com/torvalds/linux/blob/master/drivers/gpu/drm/amd/amdgpu/soc21.c), [nv.c](https://github.com/torvalds/linux/blob/master/drivers/gpu/drm/amd/amdgpu/nv.c) |
| 15 | Таблица bluesky-soft: Radeon 610M / 740M / 760M / 780M / 880M / 890M — H.264 4K, HEVC Main / Main10 8K, VP9 8K, AV1 P0 8K; HEVC 4:2:2 нет; Renoir…Barcelo — без AV1 | **подтверждено** | [bluesky-soft AMD](https://bluesky-soft.com/en/dxvac/deviceInfo/decoder/amd.html) |
| 16 | smith6612: OmniDesk `B5TQ8AA` (Ryzen 7 8700G) — HEVC «disabled in firmware», в QuickSpecs не указано; блок в ACPI; Linux «completely ignores the block bits» | **подтверждено** (текст автора, одного источника) | [smith6612](https://smith6612.me/2026/04/19/its-me-i-started-the-hevc-disablement-press-storm/) |
| 17 | Lenovo: в PDF PSREF AMD-платформ нет HEVC | **подтверждено** для 10 названных PDF (0 совпадений). Про ~50 PDF параллельного агента — **не проверено** | [PSREF](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_E16_Gen_3_AMD/ThinkPad_E16_Gen_3_AMD_Spec.pdf) и др. из раздела 5 |
| 18 | Acer: «sowohl mit als auch ohne HEVC-Codec», модели не названы | **подтверждено**, но **уточнено**: по контексту речь о непредустановленном программном кодеке (включается установкой ПО). Аппаратная блокировка не подтверждена | [ChannelPartner, 22.06.2026](https://www.channelpartner.de/article/4187748/acer-und-asus-liefern-wieder.html), [Hardwareluxx](https://www.hardwareluxx.de/index.php/news/allgemein/wirtschaft/69494-patentstreit-mit-nokia-beendet-asus-und-acer-duerfen-in-deutschland-wieder-verkaufen.html) |
| 19 | HandBrake: пресет «H.265 VCN 2160p 4K», официально RX 6000/7000/9000, аппаратный декодер не используется; AMF wiki: `hevc_amf`, `av1_amf`, `-hwaccel d3d11va` (изм. 17.03.2026); chrome://gpu «Decode hevc main» / «Encode hevc main»; GPU-Z — D3D9, патч Dell — для DLL Intel | **подтверждено** | [HandBrake](https://handbrake.fr/docs/en/latest/technical/video-vcn.html), [AMF wiki](https://github.com/GPUOpen-LibrariesAndSDKs/AMF/wiki/FFmpeg-and-AMF-HW-Acceleration), [StaZhu](https://github.com/StaZhu/enable-chromium-hevc-hardware-decoding), [Dell_HEVC_Patch](https://github.com/jimmytheshoebill/Dell_HEVC_Patch) |
| 20 | QuickSpecs 255 G9 (c08017466) и ZBook Power G11 A (c08954703) «не открылись» | **уточнено**: www8 отвечает 503 «DNS failure» и на заведомо несуществующий id. Правильность самих id — **не проверено** | curl, 30.09.2026 |
| 21 | Гипотеза «фраза появилась 17.06.2024» | запись «Added Graphics Section» 17.06.2024 в истории 465 G11 (V4→V5) и 665 G11 (V3→V4) **есть**; что фраза появилась именно тогда — по-прежнему **не проверено** | история версий c08908497, c08927104 |

**Итог проверки:** главные выводы для выбора держатся. HP ProBook 4 G1a / EliteBook 6 G1a / 465 / 665 исключить. HP G2a — только с подтверждённой опцией. EliteBook 8 — единственная HP-линейка на AMD с HEVC. Исправлены: число QuickSpecs (6, а не 7) и диапазоны CPU в двух строках. Смягчены: «EliteBook 8 выше потолка» (есть SKU на 999 € с SSD 512 ГБ) и «повышенный риск Acer» (похоже на непредустановленный программный кодек). Помечены «не проверено»: ~50 PDF Lenovo, id двух неоткрывшихся QuickSpecs.

