# Аудит HEVC (H.265): кто отключает аппаратный кодек и как проверить SKU

_2026-09-30, облачная сессия. Новых SKU здесь нет — только проверка HEVC по источникам. Каждый факт со ссылкой; «не проверено» = первоисточник не найден._
_Уже было в `candidates-lenovo-hp-dell.md` и `sweep-dell-hp.md`: цитата QuickSpecs ProBook 4 G1i 16 и ProBook 460 G11, заявления HP/Dell для Ars. Здесь — полная картина и новые факты._

## Вывод (коротко)

1. **Отключают HP и Dell.** У HP это видно по QuickSpecs. У Dell — только по правилу «HEVC есть лишь в конфигурации с дискреткой / 4K-экраном / Dolby Vision / CyberLink / Linux». Для Lenovo, ASUS и MSI отключения не нашёл. **Acer** с июня 2026 года в Германии продаёт часть устройств **«без HEVC-кодека»**. Что именно отключено, Acer не уточняет.
2. **Как это сделано.** В прошивке стоит флаг (SMBIOS/ACPI), и **сам драйвер Intel** по этому флагу скрывает профили HEVC. Поэтому не помогают ни «чистый» драйвер Intel, ни переустановка Windows, ни расширение HEVC из Microsoft Store (оно даёт только программный декодер). Под Linux аппаратный HEVC работает.
3. **Для монтажа это критично.** Premiere и Resolve Studio переходят на декодирование процессором (Ars пишет это прямо про Premiere). По заявлению HP, отключено и кодирование. H.264 и AV1 не затронуты.
4. **Вернуть можно только «хаком»** (патч DLL драйвера или подмена ACPI, в обоих случаях с отключением Secure Boot). Для рабочего ноутбука это не вариант. Официального способа (BIOS-опции или обновления) нет.
5. **Проверка SKU.** У HP — QuickSpecs, раздел GRAPHICS; маркетинговый Datasheet не годится. У остальных брендов — тест на экземпляре: DXVA Checker, `dxdiag`, `edge://gpu`, диспетчер задач. Покупать онлайн, чтобы в 14 дней на возврат успеть проверить.
6. **Наши кандидаты.** Lenovo/ASUS/Acer **напрямую «HEVC OK» не подтверждён ни один SKU** (даташиты молчат). Но и признаков отключения у Lenovo/ASUS нет. У Acer — повышенный риск. HP ProBook 4 G1i / 460 G11 — **HEVC выключен** (подтверждено). HP 15-fd1555ng — неизвестно.

---

## 1. Кто отключает и с какого времени

### HP — подтверждено по QuickSpecs (проверил сам, PDF скачаны 30.09.2026)
- Заявление HP для Ars (20.11.2025): «In 2024, HP disabled the HEVC (H.265) codec hardware on select devices, including the 600 Series G11, 400 Series G11, and 200 Series G9 products. Customers requiring the ability to **encode or decode** HEVC content … can utilize licensed third-party software» — [Ars Technica, 20.11.2025, обн. 03.02.2026](https://arstechnica.com/gadgets/2025/11/hp-and-dell-disable-hevc-support-built-into-their-laptops-cpus/).
- **В QuickSpecs встречаются три формулировки** (раздел GRAPHICS):

| Формулировка в QuickSpecs | Модели (версия QuickSpecs) |
|---|---|
| **«Hardware acceleration for CODEC H.265/HEVC (High Efficiency Video Coding) is disabled on this platform»** → HEVC выключен | ProBook 440 G11 ([c08915500 v13, 23.04.2025](https://www8.hp.com/h20195/V2/GetPDF.aspx/c08915500)); ProBook 460 G11 ([c08915560 v13, 23.04.2026](https://www8.hp.com/h20195/V2/GetPDF.aspx/c08915560)); ProBook 465 G11, AMD ([c08908497 v10](https://www8.hp.com/h20195/V2/GetPDF.aspx/c08908497)); EliteBook 640 G11 ([c08915793 v24, 15.09.2026](https://www8.hp.com/h20195/V2/GetPDF.aspx/c08915793)); EliteBook 660 G11 ([c08915794 v25](https://www8.hp.com/h20195/V2/GetPDF.aspx/c08915794)); EliteBook 665 G11, AMD ([c08927104 v11](https://www8.hp.com/h20195/V2/GetPDF.aspx/c08927104)); **ProBook 4 G1i 14/16** ([c09102586](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09102586) / [c09102587](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09102587), v11, 23.04.2026); ProBook 4 G1a 16, AMD ([c09111176 v15](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09111176)); **EliteBook 6 G1i 14/16** ([c09100635 v15](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09100635) / [c09100636 v16, 23.09.2026](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09100636)) |
| **«Codec Hardware Acceleration: HEVC (H.265) CODEC is an optional feature and must be configured at purchase»** → опция при заказе; у розничных SKU не видно | ProBook 4 G2i 16 ([c09231091 v11, 24.08.2026](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09231091)); EliteBook 6 G2i 16 ([c09237493 v11, 28.09.2026](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09237493)) |
| **«Codec Hardware Acceleration: HEVC (H.265) CODEC is supported»** → HEVC есть | EliteBook 8 G1i 16 ([c09097612 v21](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09097612), [c09097613 v21](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09097613)); EliteBook 8 G2i 16 ([c09230112 v18, 09.09.2026](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09230112)) |

- ⚠️ В **маркетинговом Datasheet** ProBook 4 G1i 16 ([c09121792](https://h20195.www2.hp.com/v2/getpdf.aspx/c09121792)) слова HEVC **нет**. Смотреть нужно только QuickSpecs.
- ⚠️ В розничных SKU HP ProBook/EliteBook 6 поколения G2i (2026) опцию HEVC, по-видимому, надо заказывать отдельно. Как понять, есть ли она у конкретного розничного P/N, — **не проверено**. → проверено в браузере 30.09.2026: (п. 5.1) По открытым данным не узнать: QuickSpecs G2i — «optional feature and must be configured at purchase», номера опции нет; в даташите E04G3ET, на страницах HP и в PartSurfer про HEVC ни слова. Спросить HP или продавца либо проверить экземпляр (линейка и так отброшена) ([hp.com](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09231091)).
- **Потребительские HP:** QuickSpecs нет, в MSG оговорки нет. Автор расследования нашёл потребительский SKU с отключённым HEVC, который **нигде не задокументирован** (HP OmniDesk M02-0000a, B5TQ8AA, AMD). Для ноутбуков HP 15/Pavilion подтверждения нет → **риск** ([smith6612.me, 19.04.2026, обн. 12.06.2026](https://smith6612.me/2026/04/19/its-me-i-started-the-hevc-disablement-press-storm/)).
- **С какого времени:** по словам HP — с 2024 года. Модели G11 вышли в 2024-м; эта фраза есть в QuickSpecs 460 G11 v11 от 16.09.2025 ([копия у Ars](https://cdn.arstechnica.net/wp-content/uploads/2025/11/ProBook-460-G11.pdf)). В каких версиях QuickSpecs она появилась впервые — не проверено. → проверено в браузере 30.09.2026: (п. 5.2) Фраза «…is disabled on this platform» есть уже в QuickSpecs ProBook 440 G11 v2 от 20.05.2024 — то есть с выхода линейки ([web.archive.org](https://web.archive.org/web/20240524150047/https://h20195.www2.hp.com/v2/GetPDF.aspx/c08915500.pdf)).

### Dell — политика «HEVC только в дорогих конфигурациях», по моделям не документируется
- Заявление Dell для Ars: «HEVC video playback is available on Dell's premium systems and in select standard models equipped with … integrated 4K displays, discrete graphics cards, Dolby Vision, or Cyberlink BluRay software. On other standard and base systems, HEVC playback is not included» — [Ars](https://arstechnica.com/gadgets/2025/11/hp-and-dell-disable-hevc-support-built-into-their-laptops-cpus/).
- **Новое:** в брошюре Dell Pro 14/16 (PC14250/PC16250; PDF изменён 31.07.2026) у строки GRAPHICS стоит сноска 18: «HEVC content playback … is supported on configurations with a discrete graphics card, **Linux/Thin OS**, built in 4K panel, Dolby Vision or CyberLink Blue-ray player; for other configurations HEVC content playback … will require a separate purchase and download of software HEVC codec or third-party media players» — [Dell brochure PDF](https://www.delltechnologies.com/asset/en-in/products/laptops-and-2-in-1s/technical-support/dell-pro-14-16-laptop-product-brochure.pdf).
- Dell KB 000222670 (изм. 11.09.2026) говорит только о расширении HEVC Video Extensions. Список продуктов: Dell Laptops, Dell Plus, Dell Pro, Dell Pro Plus/Premium/Max, Inspiron, Latitude, OptiPlex и др. ([Dell KB](https://www.dell.com/support/kbdoc/en-us/000222670/how-to-identify-if-you-cannot-view-4k-video-content-due-to-a-hevc-codec)). Что аппаратный декод выключен прошивкой, в KB не сказано.
- Подтверждённые пользователями случаи на Dell (DXVA Checker / ПО):
  - Latitude 5450 (Core Ultra 5 135U), пост от 09.10.2025;
  - Dell 16 Plus 2-in-1 (Core Ultra 7 258V): «I cannot use any GPU (hardware) based video decoding of H265 … **regardless of the application**», при этом под Linux работает;
  - Dell Pro 14 Plus (Core Ultra 5 235U): в DXVA Checker нет H265.

  Всё — [Dell Community](https://www.dell.com/community/en/conversations/latitude/8k-hevc-h265-video-decoding-uses-cpu-instead-of-igpu-dell-latitude-5450-intel-core-ultra-5-135u-w11-education/68e7ca0f1d13525e1287147f); ответа Dell нет. Ещё жалобы на Dell Pro 16 Plus и Latitude 7350 — [TechSpot](https://www.techspot.com/news/110343-dell-hp-turned-off-hevc-decoding-recent-laptops.html).
- Вывод по Dell: любой Dell Pro / Dell / Dell Plus / Latitude / Inspiron **с Windows, iGPU и экраном не 4K** — считать, что HEVC выключен.

### Lenovo — отключения не нашёл
- В заявлениях HP/Dell, у Ars, Tom's Hardware, ComputerBase, TechSpot и smith6612 Lenovo **нет** (ссылки выше/ниже).
- Заголовок [devinthreethousand (21.11.2025)](https://devinthreethousand.substack.com/p/hevc-hardware-support-being-removed) звучит так: «HEVC hardware support being removed from Dell, HP, **Lenovo** and more». Но в тексте нет ни одной модели и ни одного теста Lenovo. Утверждение **не подтверждено**. → проверено в браузере 30.09.2026: (п. 5.4) У devinthreethousand доказательств про Lenovo нет (все примеры — Dell и HP); по ThinkBook, IdeaPad, ThinkPad с iGPU сообщений нет. Прецеденты Lenovo — только NVIDIA: 2021 (H.264, Германия), 2024 (BIOS Legion, HEVC) ([devinthreethousand.substack.com](https://devinthreethousand.substack.com/p/hevc-hardware-support-being-removed)).
- PSREF: в 20 PDF платформ Lenovo (ThinkBook 16 G6–G9, ThinkPad E16 Gen 1–3, L16, V15 G5, IdeaPad Slim 5 16IRH10/IMH10/IPH11 и др.) слова HEVC нет (`sweep-lenovo.md`). Я дополнительно проверил ThinkPad T16 Gen 3 — тоже нет ([PSREF PDF](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_T16_Gen_3/ThinkPad_T16_Gen_3_Spec.pdf)).
- Лицензии (косвенный признак, не доказательство):
  - «Lenovo PC HK Limited» — в списке лицензиатов пула HEVC Advance ([Access Advance](https://accessadvance.com/hevc-advance-patent-pool-licensees/)). Там же HP и Dell, так что само по себе это ничего не гарантирует.
  - Двусторонняя лицензия HEVC с InterDigital, 02.11.2023 ([GlobeNewswire](https://www.globenewswire.com/fr/news-release/2023/11/02/2771969/24691/en/InterDigital-signs-HEVC-license-agreement-with-Lenovo.html)).
  - Мировое соглашение с Ericsson (2025), упомянуто в [Ars, 20.04.2026](https://arstechnica.com/gadgets/2026/04/lawsuits-licensing-and-royalties-are-complicating-4k-video-support-in-gadgets/).
- Статус для ThinkBook / IdeaPad / ThinkPad / LOQ: **«признаков отключения нет; прямого подтверждения, что HEVC включён, тоже нет»**. Проверять на экземпляре.

### ASUS — отключения не нашёл
- С 22.01.2026 суд Мюнхена запрещал ASUS и Acer продавать ПК в Германии (Az. 7 O 4100/25, патент Nokia на HEVC EP 2 661 892) — [ComputerBase](https://www.computerbase.de/news/notebooks/patenstreit-mit-nokia-beigelegt-acer-und-asus-duerfen-in-deutschland-wieder-verkaufen.98037/), [ChannelPartner](https://www.channelpartner.de/article/4187748/acer-und-asus-liefern-wieder.html).
- 22.06.2026 ASUS заключила с Nokia арбитражное соглашение, процессы остановлены — [Hardwareluxx, 22.06.2026](https://www.hardwareluxx.de/index.php/news/allgemein/wirtschaft/69494-patentstreit-mit-nokia-beendet-asus-und-acer-duerfen-in-deutschland-wieder-verkaufen.html). Об отключении HEVC у ASUS сообщений нет. ASUS есть в списке лицензиатов HEVC Advance ([Access Advance](https://accessadvance.com/hevc-advance-patent-pool-licensees/)).

### Acer — повышенный риск (Германия, с 06.2026)
- Заявление Acer (ChannelPartner, 22.06.2026): «Acer wird Produkte **sowohl mit als auch ohne HEVC-Codec** ausliefern. Bei Produkten ohne vorinstallierten HEVC-Codec können Kunden die Unterstützung aktivieren, indem sie die erforderliche Software separat über offizielle Drittanbieter-Kanäle installieren» — [ChannelPartner](https://www.channelpartner.de/article/4187748/acer-und-asus-liefern-wieder.html). Hardwareluxx: «Einige Modelle werden künftig ohne vorinstallierte Unterstützung für den HEVC-Codec ausgeliefert» — [Hardwareluxx](https://www.hardwareluxx.de/index.php/news/allgemein/wirtschaft/69494-patentstreit-mit-nokia-beendet-asus-und-acer-duerfen-in-deutschland-wieder-verkaufen.html).
- **Не выяснено:**
  - какие именно модели;
  - что значит «без кодека»: нет только расширения Windows (тогда для Premiere/Resolve Studio не страшно) или аппаратный профиль скрыт, как у HP/Dell (тогда критично).

  Слова «установить ПО» больше похожи на первый вариант, но это **моё предположение**. В даташитах Acer (генератор Acer: Aspire Go 16 AG16-71P-95Q7/-952H/-97GF, TravelMate P2 TMP215-75-G2) и в Icecat (NX.B9BEG.002, NX.JS9EG.005/.00C, NX.JRREG.00B, NX.JP1EG.007) слова HEVC нет — проверил 30.09.2026.
- Вывод: любой Acer, выпущенный для Германии после 22.06.2026, **проверять DXVA Checker'ом в течение 14 дней на возврат**.

### MSI, Medion, Gigabyte, Samsung
- Сообщений об отключении не нашёл (поиск 30.09.2026). MSI и Samsung — лицензиаты HEVC Advance ([Access Advance](https://accessadvance.com/hevc-advance-patent-pool-licensees/)). Статус — «неизвестно».

### Фон: почему отключают
- Ars (20.04.2026): Access Advance перенёс новые ставки на 01.07.2026; ставки HP и Dell зафиксированы контрактами до 2030 года. Access считает, что причина скорее в риске исков от патентодержателей вне пула (Nokia и др.): «It may be that HP was taking an action that would not only evade pool royalties but also make their risk with respect to somebody like Nokia less» — [Ars, 20.04.2026](https://arstechnica.com/gadgets/2026/04/lawsuits-licensing-and-royalties-are-complicating-4k-video-support-in-gadgets/).

---

## 2. Как реализовано, что затрагивает, можно ли вернуть

- **Механизм у Dell (разбор бинарника):** DXVA-драйвер Intel (`igd11dxva64.dll`, официальный драйвер с intel.com 32.0.101.8331) проверяет в SMBIOS производителя «Dell Inc.» и бит в OEM-строке (SMBIOS Type 11). Если бит = 0, драйвер стирает биты HEVC VLD в списке возможностей — [Dell_HEVC_Patch, README](https://github.com/jimmytheshoebill/Dell_HEVC_Patch) (дата репозитория не проверена).
  → Флаг ставится **на заводе, в прошивке конкретного SKU**, а выполняет запрет **сам драйвер Intel**.
- **Механизм у HP/Dell (по наблюдениям):** в ACPI/SKU-прошивке ставится бит; Windows (DirectX / Media Foundation) не видит аппаратный путь HEVC; «чистый» драйвер Intel не помогает; Linux бит игнорирует и декодирует — [smith6612](https://smith6612.me/2026/04/19/its-me-i-started-the-hevc-disablement-press-storm/), [devinthreethousand](https://devinthreethousand.substack.com/p/hevc-hardware-support-being-removed). Там же: «installing a non-OEM Windows image sees HEVC continue not to report hardware acceleration».
- **Кодирование тоже затронуто:** HP в заявлении пишет «encode or decode». Devinthreethousand: «can only use software decode/encode». Ветка на форуме HP называется «H265/HEVC HW **encoder and decoder** not available» ([HP Community](https://h30434.www3.hp.com/t5/Notebook-Video-Display-and-Touch/H265-HEVC-HW-encoder-and-decoder-not-available/td-p/9431209); из облака 403, видел только заголовок).
- **Затронут только HEVC.** Патч Dell трогает лишь биты HEVC VLD. H.264 и AV1 работают: пострадавшим советуют переходить на AV1 ([VideoCardz](https://videocardz.com/newz/hp-and-dell-disable-hevc-hardware-decoding-on-select-laptops-as-royalties-rise)).
- **Влияние на программы:**

| Программа | Эффект на ноутбуке с отключённым HEVC | Источник / статус |
|---|---|---|
| Расширение **HEVC Video Extensions** (Microsoft Store) | Даёт только программный декодер; аппаратный путь не возвращает; браузеры и VLC могут «висеть» | [smith6612](https://smith6612.me/2026/04/19/its-me-i-started-the-hevc-disablement-press-storm/), [Tom's Hardware](https://www.tomshardware.com/pc-components/gpus/dell-and-hp-disable-hardware-h-265-decoding-on-select-pcs-due-to-rising-royalty-costs-companies-could-save-big-on-hevc-royalties-but-at-the-expense-of-users): «no third-party player can re-enable hardware HEVC decoding if it is disabled in drivers or firmware»; TechSpot: у части пользователей расширение не помогло. ⚠️ Ars (04.2026) пишет обратное («restore hardware acceleration»), но без теста — считаю ошибкой → проверено в браузере 30.09.2026: (п. 5.8) Расширение HEVC из Microsoft Store аппаратный путь не возвращает (Microsoft: без аппаратной поддержки — «software support»; HP 460 G11, r/HEVC, r/sysadmin) ([apps.microsoft.com](https://apps.microsoft.com/detail/9nmzlz57r3t7)). |
| **Adobe Premiere Pro** | Декод и экспорт HEVC — только процессором, медленнее | [Ars, 20.04.2026](https://arstechnica.com/gadgets/2026/04/lawsuits-licensing-and-royalties-are-complicating-4k-video-support-in-gadgets/): «editing and exporting HEVC videos in Adobe Premiere Pro become slower, since all the decoding and encoding must be handled by software» |
| **DaVinci Resolve Studio** | Аппаратный декод HEVC на Intel iGPU недоступен → CPU. Файлы открываются (у Studio свои декодеры), но таймлайн 4K HEVC 10 бит будет тяжёлым | **не проверено тестом**; вывод из механизма (драйвер скрывает профиль) и отчёта «regardless of the application» ([Dell Community](https://www.dell.com/community/en/conversations/latitude/8k-hevc-h265-video-decoding-uses-cpu-instead-of-igpu-dell-latitude-5450-intel-core-ultra-5-135u-w11-education/68e7ca0f1d13525e1287147f)) → проверено в браузере 30.09.2026: (п. 5.9) Теста монтажа с отключённым HEVC нет нигде. Бесплатный Resolve и так декодирует процессором (аппаратный H.264/H.265 — только Studio); блокировка задевает не только Media Foundation (OBS на HP) — значит, Premiere и Resolve Studio через Intel HEVC, скорее всего, не получат, «H.265 (Intel QSV)» в HandBrake, скорее всего, пропадёт. Это вывод, не тест ([blackmagicdesign.com](https://www.blackmagicdesign.com/products/davinciresolve/studio)). |
| **Resolve (бесплатный)** | Под Windows берёт HEVC через кодеки Windows (`intel-cpu.md`, [R1]) → без расширения HEVC не откроет, с расширением — программный декод | вывод, не проверено → проверено в браузере 30.09.2026: (п. 5.9) см. строку 90 ([blackmagicdesign.com](https://www.blackmagicdesign.com/products/davinciresolve/studio)). |
| **HandBrake** | x265 (программный) работает всегда; кодировщик «H.265 (Intel QSV)», скорее всего, недоступен | **не проверено тестом** (по заявлению HP про encode) → проверено в браузере 30.09.2026: (п. 5.9) см. строку 90 ([blackmagicdesign.com](https://www.blackmagicdesign.com/products/davinciresolve/studio)). |
| Браузеры, Teams, VLC | Бесконечная загрузка / чёрный экран на HEVC; лечится отключением аппаратного ускорения (с побочными эффектами) | [smith6612](https://smith6612.me/2026/04/19/its-me-i-started-the-hevc-disablement-press-storm/), [HowToGeek, 06.11.2025](https://www.howtogeek.com/hp-is-breaking-video-playback-on-these-windows-laptops/) |

- **Можно ли включить обратно:**
  - Официально — нет: ни опции BIOS, ни обновления. Автор расследования требует от HP/Dell выпустить BIOS-обновление, но его нет ([smith6612](https://smith6612.me/2026/04/19/its-me-i-started-the-hevc-disablement-press-storm/)). → проверено в браузере 30.09.2026: (п. 5.10) МЕНЯЕТ ВЫВОД (только для Dell, Dell отброшен): сообщений «Dell Ubuntu → Windows» нет; флаг в SMBIOS, при смене ОС, скорее всего, остаётся; в Dell Command | Configure есть BIOS-атрибут --HEVC (Enabled/Disabled) — работает ли на Dell Pro 2025–26, не проверено ([dell.com](https://www.dell.com/support/manuals/en-us/command-configure/dcc_5.x_ref_guide/-hevc?guid=guid-bb1a3deb-1ebb-4ee4-9d50-6d1e32bd1496&lang=en-us)).
  - Неофициально, Dell: патч DLL драйвера Intel ([Dell_HEVC_Patch](https://github.com/jimmytheshoebill/Dell_HEVC_Patch)). Нужны отключённый Secure Boot и тестовый режим, повторять после каждого обновления драйвера. Проверено только на Dell Latitude Rugged.
  - Неофициально, HP/Dell: подмена ACPI-таблиц (пост в r/HEVC, по [smith6612](https://smith6612.me/2026/04/19/its-me-i-started-the-hevc-disablement-press-storm/)). Снимает защиту Windows (неподписанный ACPI-код). Из облака Reddit закрыт — не читал. → проверено в браузере 30.09.2026: (п. 5.11) Пост u/No-Visit6399 (r/HEVC, 23.01.2026): SSDT-подмена метода GLID через acpitabl.dat, нужны отключённый Secure Boot и testsigning — для рабочего ноутбука не рекомендую ([web.archive.org](https://web.archive.org/web/20260412001545/https://old.reddit.com/r/HEVC/comments/1qklgon/how_to_enable_hevc_hardware_support_on_2025_dell/)).
  - **Для рабочего ноутбука монтажёра оба «хака» не рекомендую.**
  - Dell: HEVC есть в конфигурациях с дискреткой / 4K / Dolby Vision / CyberLink / Linux ([брошюра Dell Pro 14/16](https://www.delltechnologies.com/asset/en-in/products/laptops-and-2-in-1s/technical-support/dell-pro-14-16-laptop-product-brochure.pdf)). Остаётся ли флаг включённым, если на Dell с Ubuntu поставить Windows, — **не проверено** (гипотеза). → проверено в браузере 30.09.2026: (п. 5.10) см. строку 96 ([dell.com](https://www.dell.com/support/manuals/en-us/command-configure/dcc_5.x_ref_guide/-hevc?guid=guid-bb1a3deb-1ebb-4ee4-9d50-6d1e32bd1496&lang=en-us)).
  - HP G2i: HEVC — опция при заказе (CTO). HP с FreeDOS не спасает: у ProBook 4 G1i фраза «disabled on this platform» относится ко всей платформе.

---

## 3. Как проверить конкретный SKU до покупки

1. **HP (бизнес):** открыть **QuickSpecs** модели (h20195 / `GetPDF.aspx/c0…`) → раздел GRAPHICS → искать «HEVC» / «Codec».
   - «is disabled on this platform» → **нет**.
   - «optional feature … configured at purchase» → **неизвестно для розничного SKU**, считать «нет».
   - «HEVC (H.265) CODEC is supported» → **да**.

   Маркетинговый Datasheet и карточки магазинов про HEVC молчат. У потребительских HP QuickSpecs нет → только тест.
2. **Dell:** в брошюре или Tech Specs искать сноску про HEVC. Если в конфигурации (по Service Tag) нет дискретки, 4K-экрана, Dolby Vision, CyberLink или Linux → считать, что HEVC выключен ([Dell KB 000222670](https://www.dell.com/support/kbdoc/en-us/000222670/how-to-identify-if-you-cannot-view-4k-video-content-due-to-a-hevc-codec)).
3. **Lenovo, ASUS, Acer, MSI, Medion:** в даташитах (PSREF, Icecat, даташиты Acer) HEVC не упоминается → только тест на экземпляре.
4. **Тест на экземпляре** (витрина или первые 14 дней после онлайн-покупки — право отказа от договора, Widerrufsrecht):
   - **DXVA Checker** → вкладка «Decoder Device»: должны быть `HEVC_VLD_Main` и `HEVC_VLD_Main10` (у Intel есть и расширенные профили HEVC 4:2:2/4:4:4). Это самый надёжный тест — [Bluesky DXVA Checker](https://bluesky-soft.com/en/DXVAChecker.html); так проверяли и в [Dell_HEVC_Patch](https://github.com/jimmytheshoebill/Dell_HEVC_Patch). Список ожидаемых профилей Intel — [bluesky-soft (Intel)](https://bluesky-soft.com/en/dxvac/deviceInfo/decoder/intel.html).
   - **dxdiag без установки ПО:** `dxdiag /t %USERPROFILE%\dx.txt` → в разделе Display Devices строка «DXVA2 Modes:» должна содержать `DXVA2_ModeHEVC_VLD_Main` и `…Main10` (формат отчёта — [пример DxDiag](https://pastebin.com/Wsagkhe9)). Косвенная проверка: на пострадавших машинах эти режимы не видны по той же причине.
   - **Edge/Chrome без установки ПО:** `edge://gpu` или `chrome://gpu` → «Video Acceleration Information»: должны быть «Decode hevc main», «Decode hevc main 10» (и «Encode hevc main» для кодирования) — [StaZhu/enable-chromium-hevc-hardware-decoding](https://github.com/StaZhu/enable-chromium-hevc-hardware-decoding).
   - **Диспетчер задач** → Производительность → GPU → «Video Decode» (при проигрывании файла HEVC 10 бит) и «Video Encode» (при экспорте). Если нагрузка 0 %, а CPU под 100 % — HEVC выключен ([StaZhu](https://github.com/StaZhu/enable-chromium-hevc-hardware-decoding)).
   - **HandBrake / Resolve Studio:** есть ли в списке кодировщиков «H.265 (Intel QSV)»; в Resolve — Preferences → Decode Options + проверка через диспетчер задач. Как HandBrake ведёт себя на машине с отключённым HEVC — не проверено. → проверено в браузере 30.09.2026: (п. 5.9) см. строку 90 ([blackmagicdesign.com](https://www.blackmagicdesign.com/products/davinciresolve/studio)).
   - **GPU-Z** — ненадёжен: использует старый API D3D9 и может показать HEVC недоступным даже там, где он работает ([Dell_HEVC_Patch](https://github.com/jimmytheshoebill/Dell_HEVC_Patch)).
   - **Intel Graphics Command Center / Intel Graphics Software** — в найденных источниках для такой проверки не упоминается; показывает ли список декодеров — **не проверено**. Не полагаться. → проверено в браузере 30.09.2026: (п. 5.12) Не удалось проверить: в описании Intel Graphics Software (MS Store) и в статье Intel 000037112 списка декодеров нет, без установки на Windows не узнать; проверять DXVA Checker ([apps.microsoft.com](https://apps.microsoft.com/detail/9p8k5g2mww6z)).

---

## 4. Lenovo (ThinkBook / IdeaPad / ThinkPad / LOQ) — итог
- Отключение HEVC у Lenovo **не задокументировано** (PSREF, публикации, заявления). Единственное упоминание Lenovo — заголовок блога без доказательств.
- Lenovo — лицензиат HEVC Advance, у неё есть двусторонняя лицензия с InterDigital. Мотив отключать слабее, чем у HP/Dell, но это не доказательство.
- Вывод: **ThinkBook, IdeaPad, ThinkPad — «вероятно OK, не подтверждено»**. После покупки сразу проверить DXVA Checker'ом и `edge://gpu`. → проверено в браузере 30.09.2026: (п. 5.4) см. строку 48 ([devinthreethousand.substack.com](https://devinthreethousand.substack.com/p/hevc-hardware-support-being-removed)).

---

## 5. HEVC по SKU из `notes/candidates-*.md` (и `sweep-*.md`)

«Не подтверждено» = в даташите оговорки нет и отчётов об отключении нет, но и теста или подтверждения «HEVC включён» тоже нет.

### Lenovo — признаков отключения нет (не подтверждено) → проверено в браузере 30.09.2026: (п. 5.4) см. строку 48 ([devinthreethousand.substack.com](https://devinthreethousand.substack.com/p/hevc-hardware-support-being-removed)).
- 83HS00BLGE — IdeaPad Slim 5 16IRH10, i7-13620H, 2×16 — PSREF без оговорки
- 83V70077GE — IdeaPad Slim 5 16IMH10, Ultra 5 135H, 24+слот — то же
- 83V70037GE — IdeaPad Slim 5 16IMH10, Ultra 9 185H, 2×16 (`sweep-lenovo.md`) — то же
- 83GW00A9GE — V15 G5 IRL — в PSREF этого MTM нет; платформа V15 G5 без оговорки
- 21SK0083GE — ThinkBook 16 G8 IAL; 21UR005AGE — ThinkBook 16 G9 IPL; 21MS004SGE — ThinkBook 16 G7 — PSREF без оговорки
- 21MA000RGE — ThinkPad E16 Gen 2; 22AY004XGE / 22AY004VGE — ThinkPad E16 Gen 3 (Lunar Lake) — PSREF без оговорки
- LOQ 83JE014MGE / 83JE00TYGE / 83SC0026GE (с RTX) — оговорки нет; к тому же у RTX свой NVDEC/NVENC
- Medion (дочерняя компания Lenovo), MD600023 / Erazer — данных нет

### ASUS — признаков отключения нет (не подтверждено) → проверено в браузере 30.09.2026: (п. 5.6) см. `browser-todo.md` ([accessadvance.com](https://accessadvance.com/hevc-advance-patent-pool-licensees/)).
- ExpertBook B3 G1 B3606CCA-MB0094X (90NX0AR2-M00390, near-miss); ExpertBook P1 P1503CVA (отброшен по SSD)

### Acer — повышенный риск (после 22.06.2026 часть устройств поставляется в DE «без HEVC-кодека»)
- NX.B9BEG.002 (TravelMate P4 16); NX.JRREG.00B (Aspire Go 15)
- NX.JS9EG.005 / .00C / .00B / .00A (Aspire Go 16, i9-13900H)
- NX.JP1EG.007 / .00W (Aspire 16 AI, Lunar Lake)
- NH.QZ9EG.002 и ANV15-52 с 32 ГБ (Nitro V 15, RTX 5050: NVDEC от HEVC-флага iGPU, скорее всего, не зависит — не проверено) → проверено в браузере 30.09.2026: (п. 5.7) МЕНЯЕТ ВЫВОД (мягко): флаг HP/Dell действует в DXVA-драйвере Intel, на NVIDIA не распространяется; но OEM-BIOS умеет резать и NVENC/NVDEC (Lenovo 2021 в Германии, Legion 2024). По Nitro и OMEN/Victus сообщений нет — в DXVA Checker проверять и декодер NVIDIA ([github.com](https://github.com/jimmytheshoebill/Dell_HEVC_Patch)).

В даташитах и Icecat HEVC не упоминается → **тест обязателен**.

### HP — отключение подтверждено
- **C7SR2ES**, D74TZES, D74TYES, D74V6ES, C7SR8ES, AD2P1ET — ProBook 4 G1i 16 → **HEVC ВЫКЛ** (QuickSpecs)
- **B2MK5ES**, B2MK4ES, D05D3ES — ProBook 460 G11 → **HEVC ВЫКЛ** (QuickSpecs)
- EliteBook 6 G1i 16, EliteBook 660 G11 → **ВЫКЛ**
- EliteBook 8 G1i / G2i 16 → **ВКЛ** (QuickSpecs), но это другой ценовой класс
- HP 15-fd1555ng **CU7G6EA** / 15-fd0068ng D46JPEA → **неизвестно, риск** (потребительская линейка, недокументированные случаи у HP есть)
- HP OMEN / Victus с RTX — iGPU не проверено; NVDEC, вероятно, OK (у Dell дискретка = HEVC есть) → проверено в браузере 30.09.2026: (п. 5.7) см. строку 154 ([github.com](https://github.com/jimmytheshoebill/Dell_HEVC_Patch)).

### Dell — для Windows + iGPU + не-4K считать выключенным
- Dell Pro 16 Plus T17XR; Dell Pro 15 Essential PV15250 (4VD04, PVYN6, GYXJD); Dell 16 DC16250 → **риск / скорее выкл** (политика Dell, брошюра Dell Pro 14/16)

### Прочие — данных нет, проверять тестом
- Captiva, Wortmann TERRA, MSI, Gigabyte

---

## Источники (сводно)
- Ars Technica: [20.11.2025](https://arstechnica.com/gadgets/2025/11/hp-and-dell-disable-hevc-support-built-into-their-laptops-cpus/), [20.04.2026](https://arstechnica.com/gadgets/2026/04/lawsuits-licensing-and-royalties-are-complicating-4k-video-support-in-gadgets/)
- HP QuickSpecs: c08915500, c08915560, c08908497, c08915793, c08915794, c08927104, c09102586, c09102587, c09111176, c09100635, c09100636, c09231091, c09237493, c09097612, c09097613, c09230112 — `https://www8.hp.com/h20195/V2/GetPDF.aspx/<id>`, скачаны 30.09.2026
- Dell: [KB 000222670](https://www.dell.com/support/kbdoc/en-us/000222670/how-to-identify-if-you-cannot-view-4k-video-content-due-to-a-hevc-codec), [брошюра Dell Pro 14/16](https://www.delltechnologies.com/asset/en-in/products/laptops-and-2-in-1s/technical-support/dell-pro-14-16-laptop-product-brochure.pdf), [Dell Community](https://www.dell.com/community/en/conversations/latitude/8k-hevc-h265-video-decoding-uses-cpu-instead-of-igpu-dell-latitude-5450-intel-core-ultra-5-135u-w11-education/68e7ca0f1d13525e1287147f)
- Механизм: [smith6612.me](https://smith6612.me/2026/04/19/its-me-i-started-the-hevc-disablement-press-storm/), [devinthreethousand](https://devinthreethousand.substack.com/p/hevc-hardware-support-being-removed), [Dell_HEVC_Patch](https://github.com/jimmytheshoebill/Dell_HEVC_Patch), [Tom's Hardware](https://www.tomshardware.com/pc-components/gpus/dell-and-hp-disable-hardware-h-265-decoding-on-select-pcs-due-to-rising-royalty-costs-companies-could-save-big-on-hevc-royalties-but-at-the-expense-of-users)
- Acer/ASUS/Nokia: [ChannelPartner](https://www.channelpartner.de/article/4187748/acer-und-asus-liefern-wieder.html), [ComputerBase](https://www.computerbase.de/news/notebooks/patenstreit-mit-nokia-beigelegt-acer-und-asus-duerfen-in-deutschland-wieder-verkaufen.98037/), [Hardwareluxx](https://www.hardwareluxx.de/index.php/news/allgemein/wirtschaft/69494-patentstreit-mit-nokia-beendet-asus-und-acer-duerfen-in-deutschland-wieder-verkaufen.html), [slashCAM](https://www.slashcam.de/news/single/Verkaufsstopp-fuer-Acer-und-Asus-in-Deutschland---N-19814.html)
- Лицензии: [Access Advance — лицензиаты HEVC Advance](https://accessadvance.com/hevc-advance-patent-pool-licensees/), [InterDigital–Lenovo](https://www.globenewswire.com/fr/news-release/2023/11/02/2771969/24691/en/InterDigital-signs-HEVC-license-agreement-with-Lenovo.html)
- Проверка: [DXVA Checker](https://bluesky-soft.com/en/DXVAChecker.html), [StaZhu (chrome://gpu)](https://github.com/StaZhu/enable-chromium-hevc-hardware-decoding)
- Из облака закрыты (403, защиту не обходил): community.intel.com, h30434.www3.hp.com (форум HP), forum.kodi.tv, forum.blackmagicdesign.com, community.acer.com, reddit.com, guru3d, winfuture.
