# Черновик итога и доводы трёх судей (30.09.2026, вечер)

_Архив. Итоговый выбор сделан в [`../../REPORT.md`](../../REPORT.md): HP OmniBook 7 16 `BM9T4EA#ABD`. Черновик синтезатора ниже выбирал Acer R2R1 — его главная посылка «владелец сделал экран главным критерием» появилась из формулировки задания основной сессии, а не от владельца; поэтому основная сессия выбор пересмотрела (обоснование — «Почему Intel и почему именно HP» в итоговом отчёте)._

## Судья: риски и цена

**Выбор:** Intel — Lenovo IdeaPad Slim 5 16IRH10 `83HS00BLGE`, итог 993,30 € без докупки (i7-13620H, 2×16 ГБ SO-DIMM DDR5-5600, 1 ТБ + свободный M.2 2280, зарядка 65 Вт в комплекте, гарантия 2 года). Карточка: https://www.idealo.de/preisvergleich/OffersOfProduct/209881995_-ideapad-slim-5-16-83hs00blge-lenovo.html. Перепроверено 30.09 в 20:27: 993,30 € на Kaufland (маркетплейс, возврат 14 дней), 995,00 € у technowelt24 и у expert-technomarkt, 995,98 € у expert.de (14 дней) и на eBay (30 дней), 1005 € у boomstore — 6 предложений в пределах 12 €.

**Запасной:** Другой класс — Lenovo ThinkPad E16 Gen 3 `22AY003WGE` + SSD, итог 1038,06 € (917,07 € у jacob.de в 20:27 + Verbatim Vi3000 1 ТБ за 120,99 € у notebooksbilliger, возврат 30 дней). Core Ultra 5 228V (Lunar Lake), Arc 130V, 32 ГБ LPDDR5X-8533 распаяны, двухканал гарантирован, 2× TB4, HDMI 2.1, RJ45. Карточки: https://www.idealo.de/preisvergleich/OffersOfProduct/209382343_-thinkpad-e16-g3-22ay003wge-lenovo.html и https://www.idealo.de/preisvergleich/OffersOfProduct/202702551_-vi3000-1tb-verbatim.html. Если хочется запасной из ветки AMD: IdeaPad Slim 5 16AKP10 `83HY008CGE` за 1059,99 € — но только если его единственное предложение ещё живо в момент заказа (см. финалистов).

**Пятёрка:**
- 8 — 83HS00BLGE (Intel, IdeaPad Slim 5 16IRH10) — 993,30 €: Минимум риска при покупке сейчас. Предложений 7, из них 6 в пределах 993,30–1005 € (idealo, 20:27): https://www.idealo.de/preisvergleich/OffersOfProduct/209881995_-ideapad-slim-5-16-83hs00blge-lenovo.html. Докупать ничего не нужно, поэтому нет ни зависимости от единственной планки за 187,56 €, ни риска «24+16». 2×16 и свободный M.2 2280 подтверждены PSREF; там же гарантия «2-year, Courier or Carry-in» (батарея — 1 год) и End of Support 2030-12-18: https://psref.lenovo.com/Detail/IdeaPad/IdeaPad_Slim_5_16IRH10?M=83HS00BLGE. У Lenovo отключённого HEVC во встроенной графике не нашли (Intel/notes/browser-check-hevc.md, п. 5.4). Декодирует HEVC 4:2:2 10 бит, как любой Intel 11+ (Puget: https://www.pugetsystems.com/labs/articles/what-h-264-and-h-265-hardware-decoding-is-supported-in-premiere-pro-2120/). Mobile Raptor Lake не затронут дефектом Vmin Shift — это подтверждает сама Intel: https://community.intel.com/t5/Blogs/Tech-Innovation/Client/Intel-Core-13th-and-14th-Gen-Desktop-Instability-Root-Cause/post/1633239. Минусы: драйверы графики с 19.09.2025 в режиме legacy — только критические исправления раз в квартал (https://www.intel.com/content/www/us/en/support/articles/000101986/graphics.html, проверено 30.09); корпус горячий и шумный — 43 Вт при 96 °C у версии с 210H (LaptopMedia) и 50,4 дБ(A) (NBC); памяти не больше 32 ГБ; AV1 аппаратно не кодирует.
- 7 — 22AY003WGE + SSD (Intel, ThinkPad E16 G3) — 1038,06 €: Самое надёжное предложение из всех: 36 предложений на ноутбук (917,07 € у jacob.de; следующие — 926,60 € и 941,90 €) и 30 на SSD (idealo, 20:27). Драйверы Lunar Lake актуальные. Декод самый широкий в бюджете: HEVC 4:2:2 плюс кодирование AV1. Память распаяна (32 ГБ LPDDR5X-8533), значит планка и «24+16» не нужны. У ThinkPad End of Support — 2032-08-20 (PSREF: https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=22AY003WGE&country_code=DE), у iFixit — 9/10. Риски: базовая гарантия 1 год (PSREF), а продление примерно за 102–109 € (lap4worx) выводит итог за 1100 €. Слот M.2 один, поэтому SSD надо менять: сначала проверить экземпляр, потом вскрывать (§ 357a BGB). Если память откажет — менять плату. Процессор слабый: 8 потоков, R23 9932 — на 35 % слабее 13620H. При неизвестном кодеке это худший программный запасной путь для форматов вроде H.264 4:2:2 10 бит, которые не декодирует аппаратно ни один ноутбук в бюджете.
- 6 — 83HY008CGE (AMD, IdeaPad Slim 5 16AKP10) — 1059,99 €: Если бы не риски, это был бы лучший вариант по сроку службы. Zen 5, графика 860M (RDNA 3.5) с актуальными драйверами, кодирует AV1, корпус тихий. 2×16, свободный M.2, гарантия 2 года, End of Support 2031-03-12 (PSREF). Но в 20:27 предложение по-прежнему одно — Kaufland, маркетплейс, продаёт expert, возврат 14 дней (https://www.idealo.de/preisvergleich/OffersOfProduct/209439304_-ideapad-slim-5-16-83hy008cge-lenovo.html). Если оно исчезнет, такого же SKU за эти деньги нет: у `83HY0061GE` только б/у. До потолка 40 €. HEVC 4:2:2 не декодирует ни один AMD («All codecs are 4:2:0», AMD AMF), поэтому при неизвестном кодеке это открытый риск. NBC отметил высокие DPC-задержки.
- 5 — 21MW00AYGE (AMD, ThinkBook 16 G7 ARP) — 998,99 €: Предложение надёжное: 14 предложений около 999–1005 € (idealo, 20:27): https://www.idealo.de/preisvergleich/OffersOfProduct/207306483_-thinkbook-16-g7-21mw00ayge-lenovo.html. Два слота до 64 ГБ, два M.2, USB4, SD и RJ45 (бонус), запчасти ThinkBook. Но устареет первым из финалистов: Zen 3+ 2022 года (R23 8613), графика 660M на RDNA 2 — драйверы в maintenance mode с осени 2025 (heise: https://www.heise.de/en/news/Confusion-over-AMD-s-graphics-drivers-for-RDNA-1-and-2-in-maintenance-mode-10966044.html). Не кодирует AV1 и не декодирует HEVC 4:2:2. Гарантия 1 год. Цена сейчас на максимуме года: за полгода минимум был 833,81 €, то есть переплата около 165 €.
- 3 — NX.JP0EG.00Z (AMD, Acer Aspire 16 AI OLED R2R1) — 1081,21 €: Единственный вариант с процессором для 4K и экраном для цвета (OLED, 95–100 % DCI-P3 по даташиту). Но рисков больше всего. В бюджете фактически одно предложение — computeruniverse за 1081,21 €, второе у e-tec стоит 1111,90 € и выше потолка (idealo, 20:28): https://www.idealo.de/preisvergleich/OffersOfProduct/211631508_-aspire-16-ai-a16-61m-r2r1-acer.html. В этой же карточке computeruniverse и cyberport продают за 801,82 € «R2R1» с Ryzen AI 5 330 16/512, так что есть риск получить не ту конфигурацию. Acer продаёт в Германии часть устройств «ohne HEVC-Codec» (https://www.channelpartner.de/article/4187748/acer-und-asus-liefern-wieder.html). Память и SSD распаяны. Замеров экрана нет, ШИМ не проверен. У Techradar — 60 % и «build quality issues». Комплектность блока питания не подтверждена.

**Довод:** Через линзу «риски и цена покупки сейчас» (перепроверил в Chrome 30.09, 20:27–20:28).

1) Итог и запас. `83HS00BLGE` — 993,30 €, докупать ничего не нужно, до потолка 106,70 €. Остальные уязвимы. Intel `83V70077GE` + планка + зарядка (1081,58 €) держится на единственной планке Kingston за 187,56 € (Galaxus МП): если её раскупят, итог 1100,82 € — выше потолка (AMD/notes/prices-final.md). `83HY008CGE` (1059,99 €) — одно предложение. Acer R2R1 (1081,21 €) — одно предложение в бюджете, второе за 1111,90 € уже выше потолка.

2) Надёжность предложения. У №1 шесть продавцов в пределах 993,30–1005 €: если маркетплейс Kaufland пропадёт, у technowelt24 выйдет +1,70 €, у eBay с возвратом 30 дней — +2,68 € (https://www.idealo.de/preisvergleich/OffersOfProduct/209881995_-ideapad-slim-5-16-83hs00blge-lenovo.html). У запасного 36 предложений на ноутбук и 30 на SSD.

3) Отключённый HEVC. Оба выбора — Lenovo, а у Lenovo отключений во встроенной графике не находили. Кандидаты HP (`BM9T4EA`, `CU7G6EA`) и все Acer (включая оба OLED) несут этот риск (Intel/REPORT «Ловушка с отключённым HEVC»). Проверка экземпляра — DXVA Checker, `HEVC_VLD_Main10`.

4) «24+16» и прочие допущения. Ни в одном из двух выборов «24+16» нет: у №1 2×16 с завода по PSREF, у запасного 32 ГБ распаяны. Непроверенными остаются: охват экрана №1 — замер NBC сделан на родственной 16IRH10R, производитель панели может отличаться; нагрев с i7 — тест LaptopMedia делали на 210H. Блок 65 Вт на H-процессоре Medion и Acer штрафовали −0,5, а IdeaPad нет, хотя у №1 по PSREF тоже 65 Вт. Всё это проверяется в срок возврата. Mobile Raptor Lake дефект Vmin не затрагивает (Intel).

5) Гарантия и ремонт. У №1 2 года (PSREF), два слота SO-DIMM, два M.2, End of Support 2030-12-18. У запасного 1 год, но запчасти ThinkPad и End of Support 2032-08-20.

6) Драйверы и срок службы. Слабое место №1 — графика: UHD Raptor Lake в режиме legacy (Intel 000101986) и Time Spy 1110. Устареет раньше всего именно она. Процессор (R23 15 176) и аппаратный HEVC 4:2:2 остаются. При неизвестном кодеке это главное: то, что не декодирует ни один ноутбук в бюджете (H.264 4:2:2 10 бит), ляжет на процессор, а у №1 он один из сильнейших. У AMD `21MW00AYGE` устареет всё сразу — RDNA 2 в maintenance, Zen 3+, нет AV1. Поэтому запасной — ThinkPad на Lunar Lake: драйверы актуальные, HEVC 4:2:2 + AV1, предложение не исчезнет. Слабый процессор у него — осознанная уступка. AMD `83HY008CGE` ставлю третьим: по сроку службы он лучше обоих, но единственное предложение и отсутствие HEVC 4:2:2 — именно те риски, которые линза должна отсечь.

**Что теряет владелец:** С выбором `83HS00BLGE` владелец теряет:

1) Экран. IPS 45 % NTSC, у той же панели NBC намерил около 57,7 % sRGB и 39,7 % DCI-P3, 300 нит. Точно работать с цветом на нём нельзя. Экран для цвета в бюджете есть только у Acer OLED — 95–100 % DCI-P3, но с распаянной памятью, риском HEVC и одним предложением.

2) Графику. Time Spy 1110 против 2565 у AMD 860M (`83HY008CGE`, +66,69 €) и 3401 у Arc 130V (запасной): GPU-эффекты, шумодав и цветокоррекция будут идти медленнее. Драйверы только в режиме legacy.

3) Аппаратное кодирование AV1.

4) Тишину и холод: около 96 °C и 50,4 дБ(A) под нагрузкой против 42 дБ(A) у AMD-сестры.

5) Бонусные порты. USB-C только 5 Гбит/с — сброс 4K-материала с внешнего SSD идёт медленнее; HDMI 1.4b; нет TB4 и RJ45 (у запасного всё это есть).

6) Потолок роста: 32 ГБ по PSREF. Запчасти и сервис — до 2030-12-18, у ThinkPad — до 2032-08-20.

Цена ошибки:
- Исходники окажутся 4:2:0 (смартфон, GoPro, DJI) — AMD за +66,69 € дал бы графику в 2,3 раза сильнее и AV1.
- Окажутся HEVC 4:2:2 (Sony, Canon, Fuji) — выигрывает №1, AMD декодировал бы это процессором.
- H.264 4:2:2 10 бит — не декодирует ни один ноутбук в бюджете; нужен прокси, а процессор №1 здесь один из лучших запасных вариантов.
- Выяснится, что нужен точный цвет, — ошибкой будет любой Lenovo в бюджете. Тогда вернуть ноутбук в срок: 14 дней у Kaufland и expert, 30 дней на eBay (995,98 €) — и перейти на Acer OLED со всеми его рисками.

С запасным `22AY003WGE` владелец теряет примерно 35 % многопотока (R23 9932), второй год базовой гарантии, возможность расширить память и второй M.2. Кроме того, SSD придётся менять самому.

## Судья: кодеки и программы

**Выбор:** HP OmniBook 7 AI 16-ay0770ng `BM9T4EA#ABD`: 979,30 € на hp.com, других продавцов нет, доставка до 10.10 ([idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/206602335_-omnibook-7-ai-16-ay0770ng-hp.html), [prices-final.md](/AMD/notes/prices-final.md)). Это Intel №8 в Intel-отчёте. Внутри Core Ultra 7 255H (Arrow Lake-H) и Arc 140T, 32 ГБ DDR5-5600 распаяны, 1 ТБ и свободный второй M.2 ([даташит HP](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09154072)).
Беру с одним условием: в день получения проверить, не отключён ли HEVC. Для этого до установки программ открыть DXVA Checker и найти там HEVC_VLD_Main, HEVC_VLD_Main10 и профиль 4:2:2 10 бит, затем сделать короткий экспорт H.265 10 бит через QSV в HandBrake, а в Диспетчере задач убедиться, что графика определилась как «Arc 140T». Если профилей HEVC нет, ноутбук вернуть: HP Store даёт 30 дней ([HP](https://www.hp.com/de-de/shop/faq/returns/how-to-return-and-request-refund-or-replacement)), по idealo — 14. Тогда брать запасной.

**Запасной:** Lenovo IdeaPad Slim 5 16IRH10 `83HS00BLGE`: 993,30 € на Kaufland (маркетплейс, возврат 14 дней), всего 7 предложений ([idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/209881995_-ideapad-slim-5-16-83hs00blge-lenovo.html)). Это ноутбук другого класса: Raptor Lake-H i7-13620H, 2×16 SO-DIMM, свободный второй M.2 ([PSREF](https://psref.lenovo.com/Detail/IdeaPad/IdeaPad_Slim_5_16IRH10?M=83HS00BLGE)).
Декодирует аппаратно то же, что №1, включая HEVC 4:2:2 10 бит ([Puget, Premiere](https://www.pugetsystems.com/labs/articles/what-h-264-and-h-265-hardware-decoding-is-supported-in-premiere-pro-2120/)). Случаев, чтобы Lenovo отключала HEVC во встроенной графике, не нашли ([browser-check-hevc.md](/Intel/notes/browser-check-hevc.md), п. 5.4). Процессор на случай программного декода тоже крепкий: R23 15 176.
Почему запасной не из AMD: по моей линзе единственная дыра, которую в 1100 € вообще можно закрыть, — HEVC 4:2:2. Закрывает её только Intel, а у AMD её нет ни в одной программе и ни в одном поколении ([AMF wiki: «All codecs are 4:2:0»](https://github.com/GPUOpen-LibrariesAndSDKs/AMF/wiki/GPU%20and%20APU%20HW%20Features%20and%20Support)).

**Пятёрка:**
- 8 — HP OmniBook 7 16 `BM9T4EA#ABD` — 979,30 € ([idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/206602335_-omnibook-7-ai-16-ay0770ng-hp.html)): Лучший и там, где есть аппаратный декод, и там, где его нет. Декод как у любого Intel 11+: HEVC 4:2:0/4:2:2/4:4:4, 12 бит, AV1. Плюс кодирует AV1. Процессор 255H — R23 17 845, сильнейший в бюджете ([NBC](https://www.notebookcheck.net/Mobile-Processors-Benchmark-List.2436.0.html)). Arc 140T — Time Spy 3843 ([NBC GPU](https://www.notebookcheck.net/Mobile-Graphics-Cards-Benchmark-List.844.0.html)). В Puget Bench (Resolve 20, 4K HEVC 4:2:2 10 бит) — 56,3 кадра/с, лучший замер среди iGPU ([PB1](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/27/GPU/AMD%20Radeon%20890M%20Graphics/Intel%20Arc%20140T%20GPU%20%2816GB%29/)); Lumetri ×40 в Premiere — 18,2 кадра/с. −2 за риск, что HP без документов отключила HEVC: такое уже было у OmniBook 7 Aero 13 ([HP Community](https://h30434.www3.hp.com/t5/Notebook-Video-Display-and-Touch/H265-HEVC-HW-encoder-and-decoder-not-available/td-p/9431209)) и у OmniDesk ([smith6612](https://smith6612.me/2026/04/19/its-me-i-started-the-hevc-disablement-press-storm/)). Этот риск проверяется в первый день и обратим.
- 7 — Lenovo IdeaPad Slim 5 16IRH10 `83HS00BLGE` — 993,30 € ([idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/209881995_-ideapad-slim-5-16-83hs00blge-lenovo.html)): Тот же аппаратный декод, что у №1, включая HEVC 4:2:2 в Resolve Studio, Premiere и VEGAS 22 ([Puget Resolve](https://www.pugetsystems.com/labs/articles/what-h-264-and-h-265-hardware-decoding-is-supported-in-davinci-resolve-studio-2122/), [VEGAS](https://help.magix-hub.com/video/vegas/22/en/content/topics/13-appendix/codecoverview.htm)). Риска отключения HEVC нет. Процессор 13620H (R23 15 176, 16 потоков) нормально вытягивает форматы, которые никто не декодирует аппаратно. Минусы: графика UHD 64 EU — Time Spy 1110, в 3,5 раза слабее Arc 140T, поэтому в Resolve (он всё обрабатывает на GPU) и в Lumetri будет тяжело. AV1 не кодирует; драйверы графики legacy с 19.09.2025 ([Intel](https://www.intel.com/content/www/us/en/support/articles/000101986/graphics.html)).
- 6.5 — Lenovo ThinkPad E16 Gen 3 `22AY003WGE` + SSD — 1038,06 € ([idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/209382343_-thinkpad-e16-g3-22ay003wge-lenovo.html)): Самый широкий медиадвижок: Lunar Lake декодирует и кодирует HEVC 4:2:2, кодирует AV1, декодирует VVC ([media-driver](https://raw.githubusercontent.com/intel/media-driver/master/docs/media_features.md)). Arc 130V (Time Spy 3401) с актуальными драйверами, у ThinkPad риска с HEVC нет. Но всего 8 потоков, R23 9932 — худший запас на всё, что уходит на процессор. Это H.264 4:2:2 10 бит, ProRes, весь декод в бесплатном Resolve (аппаратный декод — только в Studio, [Blackmagic](https://documents.blackmagicdesign.com/SupportNotes/DaVinci_Resolve_21_Supported_Codec_List.pdf)), Shotcut в 4K (аппаратный декод только до 1080p, [FAQ](https://www.shotcut.org/FAQ/)) и перекодирование в прокси. Lunar Lake Puget не тестировал. Цену пересчитать: в соседней вкладке idealo около 20:30 карточка показывала «ab 912,33 €» — я это не проверял.
- 6.5 — Acer Aspire Go 16 `NX.JS9EG.005` — 849,00 € ([idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/209373295_-aspire-go-16-ag16-71p-97gf-acer.html)): Декод как у всех Intel 11+, включая HEVC 4:2:2. Процессор i9-13900H — R23 17 471, самый сильный запас на программный декод среди Raptor Lake. Но блок питания 65 Вт при потреблении 68 Вт ([overclockers.ua](https://www.overclockers.ua/ru/notebook/acer-aspire-go-16-ag16-71p/all/)), так что частоту под нагрузкой он не удержит. Iris Xe — Time Spy 1561, AV1 не кодирует. В Германии Acer поставляет часть устройств «ohne HEVC-Codec» ([ChannelPartner](https://www.channelpartner.de/article/4187748/acer-und-asus-liefern-wieder.html)), и какие именно модели — неизвестно. По словам Acer, речь о программном кодеке, так что риск ниже, чем у HP, но экземпляр всё равно проверять.
- 6 — Lenovo IdeaPad Slim 5 16AKP10 `83HY008CGE` — 1059,99 € ([idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/209439304_-ideapad-slim-5-16-83hy008cge-lenovo.html)): Лучший AMD. Аппаратно декодирует всё 4:2:0 (смартфоны, GoPro, DJI, беззеркалки в режиме по умолчанию), кодирует AV1. Процессор Ryzen AI 7 350 — R23 16 015, графика 860M — Time Spy 2565. HEVC 4:2:2 10 бит (Sony XAVC HS 4:2:2, Canon R6 II 10 бит, Fuji) не декодирует ни в одной программе. Программный путь в экспорте терпим: 43,4 кадра/с против 56,3 у Arc 140T ([PB2](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/27/GPU/AMD%20Radeon%20860M%20Graphics/Intel%20Arc%20Graphics/)). На таймлайне хуже: у Framework 13 (7640U) файлы A7 IV 4:2:2 грузят CPU на 70–100 % и не проигрываются ([Framework](https://community.frame.work/t/42-video-on-amd/64502)). Предложение одно.

**Довод:** **Линза — неизвестный кодек и неизвестная программа.** Выбор решают три вещи: какую долю вероятных исходников ноутбук декодирует аппаратно, насколько больно там, где аппаратного декода нет, и есть ли риск, что производитель отключил HEVC.

1. **Самые вероятные исходники — 4:2:0.** Это смартфоны, GoPro 10 бит, DJI D-Log M, беззеркалки в режиме по умолчанию. Их аппаратно декодируют все финалисты, Intel и AMD одинаково ([Puget](https://www.pugetsystems.com/labs/articles/what-h-264-and-h-265-hardware-decoding-is-supported-in-davinci-resolve-studio-2122/), [amd-codecs.md](/AMD/notes/amd-codecs.md) §3.2).
   Здесь проиграть можно только одним способом: если производитель отключил HEVC. Тогда пропадает самый массовый формат. Поэтому риск HP и Acer для меня весит больше, чем любая разница в бенчмарках.

2. **Единственная дыра, которую в 1100 € можно закрыть, — HEVC 4:2:2 10 бит** (Sony XAVC HS 4:2:2, Canon R6 II 10 бит, Fujifilm H.265 4:2:2).
   - Закрывает её только Intel 11+: в Resolve Studio, в Premiere и в VEGAS 22 ([Puget Resolve](https://www.pugetsystems.com/labs/articles/what-h-264-and-h-265-hardware-decoding-is-supported-in-davinci-resolve-studio-2122/), [VEGAS](https://help.magix-hub.com/video/vegas/22/en/content/topics/13-appendix/codecoverview.htm)).
   - Страницу Adobe я открыл 30.09 в Chrome, она обновлена 07.01.2026: «support HEVC 4:2:2 10-bit decoding on Intel platforms» ([Adobe](https://helpx.adobe.com/premiere/desktop/get-started/technical-requirements/supported-codecs-and-drivers-for-hardware-accelerated-decoding.html)).
   - У AMD — «All codecs are 4:2:0» ([AMF](https://github.com/GPUOpen-LibrariesAndSDKs/AMF/wiki/GPU%20and%20APU%20HW%20Features%20and%20Support)).
   - Отсюда первое сито: Intel.

3. **Что не декодирует никто в бюджете, решает процессор, а в Resolve — ещё и iGPU.**
   - Аппаратного декода в 1100 € нет у H.264 4:2:2 10 бит (XAVC S 10 бит, Panasonic MOV, DJI ALL-I), ProRes и All-Intra.
   - Бесплатный Resolve декодирует процессором всё: аппаратный декод есть только в Studio ([Blackmagic](https://documents.blackmagicdesign.com/SupportNotes/DaVinci_Resolve_21_Supported_Codec_List.pdf)).
   - Shotcut декодирует аппаратно только до 1080p ([FAQ](https://www.shotcut.org/FAQ/)). HandBrake на AMD декодирует процессором ([HandBrake](https://handbrake.fr/docs/en/latest/technical/video-vcn.html)).
   - Что аппаратно декодирует CapCut, не проверено: 30.09 искал в Google, официальных данных нет.
   - Отсюда второе сито — многопоток (R23), третье — iGPU (Time Spy, Puget).

4. **Насколько больно без аппаратного декода.**
   - В экспорте терпимо. Puget Bench, Resolve 20, 4K HEVC 4:2:2 10 бит: Arc 140T аппаратно — 56,3 кадра/с, Ryzen AI 7 350 процессором — 43,4, Meteor Lake аппаратно — 41,7 ([PB1](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/27/GPU/AMD%20Radeon%20890M%20Graphics/Intel%20Arc%20140T%20GPU%20%2816GB%29/), [PB2](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/27/GPU/AMD%20Radeon%20860M%20Graphics/Intel%20Arc%20Graphics/)).
   - На таймлайне больно. Владелец Framework 13 (Ryzen 5 7640U) с Sony A7 IV 4:2:2: процессор загружен на 70–100 %, VLC файл не проигрывает ([Framework](https://community.frame.work/t/42-video-on-amd/64502)).

5. **Почему №1 — HP `BM9T4EA` (979,30 €).**
   - Он лучший по всем трём ситам сразу: полный декод Intel плюс AV1-кодирование; сильнейший процессор в бюджете (255H, R23 17 845) и сильнейший iGPU (Arc 140T, Time Spy 3843) ([NBC CPU](https://www.notebookcheck.net/Mobile-Processors-Benchmark-List.2436.0.html), [NBC GPU](https://www.notebookcheck.net/Mobile-Graphics-Cards-Benchmark-List.844.0.html)).
   - В Premiere Lumetri ×40 — 18,2 кадра/с против 11,9 у 860M ([PB6](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/23/GPU/AMD%20Radeon%20890M%20Graphics/Intel%20Arc%20140T%20GPU%20%2816GB%29/), [PB8](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/23/GPU/AMD%20Radeon%20860M%20Graphics/Intel%20Arc%20130T%20GPU%20%2816GB%29/)).
   - Его слабое место в моей линзе одно: HP может без документов отключить HEVC. Бизнес-HP это делают прямо по QuickSpecs ([ProBook 4 G1i](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09102587)), у потребительского OmniBook 7 Aero 13 так вышло без документов ([HP Community](https://h30434.www3.hp.com/t5/Notebook-Video-Display-and-Touch/H265-HEVC-HW-encoder-and-decoder-not-available/td-p/9431209)).
   - Но этот риск видно за 5 минут в DXVA Checker, и он обратим: HP Store принимает возврат 30 дней.
   - Слабость остальных — навсегда. У `83HS00BLGE` графика UHD в 3,5 раза слабее Arc 140T, у `22AY003WGE` только 8 потоков, у AMD нет 4:2:2. В отчётах HP стоит №8 (средн. 6) из-за Пробл. 3,5 и Ремонта 4,5. Это вне моей линзы, но другим судьям это учесть.

6. **Запасной — `83HS00BLGE` (993,30 €).**
   - Декодирует тот же набор форматов, и у Lenovo нет риска с HEVC. Если HP не пройдёт проверку, ноутбук возвращаем и берём этот.
   - Декод у запасного не хуже; теряем только графику и AV1-кодирование.
   - AMD `83HY008CGE` как запасной хуже по моей линзе: у него отсутствие 4:2:2 постоянное и во всех программах.

7. **Справка — что закрыло бы H.264 4:2:2.** Только RTX 50 (от 1266,66 €) или Panther Lake с Resolve Studio 21 (`21UR005AGE`, 1203,82 €) ([idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/209497615_-thinkbook-16-g9-21ur005age-lenovo.html)). Оба дороже потолка, в выбор не входят.

**Что теряет владелец:** 1. **H.264 4:2:2 10 бит, ProRes и All-Intra по-прежнему идут на процессор или через прокси.** Это Sony XAVC S 10 бит и S-I, Panasonic MOV 4:2:2, DJI Mavic 4 Pro ALL-I. Так у любого ноутбука до 1100 € ([amd-codecs.md](/AMD/notes/amd-codecs.md) §3.2). Процессор 255H тянет это лучше всех в бюджете, но таймлайн 4K с такими файлами всё равно будет дёргаться.

2. **Лотерея с HEVC у HP.** Если HP отключила HEVC, пропадает не только 4:2:2, но и обычный HEVC со смартфонов и дронов. Тогда возврат, а это потеря времени: доставка с hp.com — до 10.10, плюс сам возврат. Затем запасной — по цене на тот момент (7 предложений, сейчас 993,30 €).
   Проверять строго до установки программ и до любых изменений в ноутбуке: DXVA Checker, короткий экспорт через QSV в HandBrake, «Arc 140T» в Диспетчере задач.

3. **Потери вне моей линзы, но честно.**
   - 32 ГБ распаяны, расширить нельзя (для 4K Adobe рекомендует 32 ГБ — хватает).
   - Нет слотов SO-DIMM и экосистемы запчастей Lenovo. У потребительских HP запчасти снимают вскоре после конца гарантии ([IPC](https://blog.ipc-computer.de/2025/10/hp-service/)); гарантия 2 года.
   - Экран 62,5 % sRGB — лучше класса «45 % NTSC», но для цвета мало. OLED в бюджете есть только у Acer, и там AMD и риск с HEVC.
   - Нет кардридера и Ethernet (это бонус, но его нет).
   - Продавец один — hp.com.

4. **Если вместо HP сразу взять запасной `83HS00BLGE`**, декод не теряется, но теряется графика навсегда: Time Spy 1110 против 3843, то есть Resolve и Lumetri в 4K заметно медленнее. Плюс нет AV1-кодирования, а драйверы графики legacy (только квартальные исправления).

## Судья: производительность и экран

**Выбор:** Acer Aspire 16 AI OLED A16-61M-R2R1 — NX.JP0EG.00Z, 1081,21 € (computeruniverse.net, возврат 30 дней; перепроверено мной в 20:30, до потолка остаётся 18,79 €) — https://www.idealo.de/preisvergleich/OffersOfProduct/211631508_-aspire-16-ai-a16-61m-r2r1-acer.html . Ryzen AI 7 350 (Zen 5, 8 ядер) + Radeon 860M на распаянной LPDDR5X-8533 32 ГБ, 1 ТБ PCIe 4. OLED WUXGA: 95 % DCI-P3 по даташиту Acer, 100 % по Icecat, 300 нит, 60 Гц. 2× USB4, HDMI 2.1, microSD. Блок питания 100 Вт в комплекте, гарантия 2 года (даташит Acer https://gzhls.at/blob/ldb/e/9/9/4/1b8b6ae3e1047dc798a552be0d80e9a0f0ab.pdf ; Icecat «AC-Netzadapter: Ja» https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Acer&ProductCode=NX.JP0EG.00Z).

**Запасной:** Lenovo IdeaPad Slim 5 16AKP10 — 83HY008CGE, 1059,99 € (Kaufland, маркетплейс, продавец expert, возврат 14 дней; в 20:30 то же, предложение одно) — https://www.idealo.de/preisvergleich/OffersOfProduct/209439304_-ideapad-slim-5-16-83hy008cge-lenovo.html . Класс другой: 2×16 SO-DIMM, два M.2, IPS без ШИМ (PSREF https://psref.lenovo.com/Detail/IdeaPad/IdeaPad_Slim_5_16AKP10?M=83HY008CGE). Процессор и графика те же, что у №1, поэтому скорость не падает. Запасной закрывает все три причины, по которым №1 может не подойти: ШИМ или брак OLED, выключенный у Acer HEVC, пропавшее предложение. Теряется только экран. Если пропадёт и это предложение (оно одно), дальше — Intel 83HS00BLGE, 993,30 €, 7 предложений: https://www.idealo.de/preisvergleich/OffersOfProduct/209881995_-ideapad-slim-5-16-83hs00blge-lenovo.html

**Пятёрка:**
- 7.5 — NX.JP0EG.00Z (Acer Aspire 16 AI OLED R2R1), 1081,21 €: Единственный вариант ≤ 1100 €, где есть и экран для цвета, и достаточная мощность. OLED 95–100 % DCI-P3 по даташиту; ближайший замер — WUXGA OLED у Swift Air 16: 100 % sRGB и P3, 297 нит (https://laptopmedia.com/de/review/acer-swift-air-16-sfa16-61m-review-a-16-inch-laptop-that-weighs-under-1-kg/). Процессор AI 7 350 — медиана R23 16 015, разброс 12 647–18 243 в зависимости от лимита мощности (https://www.notebookcheck.net/AMD-Ryzen-AI-7-350-Processor-Benchmarks-and-Specs.949825.0.html). Графика 860M (Time Spy 2565) на LPDDR5X-8533 — у неё самая быстрая память среди 860M в списке. Минусы: длительная мощность, шум и ШИМ этого корпуса не измерены; у родственного Acer Swift Go 16 AI — 45 Вт длительно, 52–53 дБ(A), ШИМ 220 Гц (https://www.notebookcheck.com/Solide-Performance-und-farbechtes-OLED-Acer-Swift-Go-16-AI-mit-AMD-Ryzen-im-Test.1102652.0.html). Глянец, HEVC 4:2:2 не декодирует, у Acer есть риск с HEVC.
- 6.5 — 83HY008CGE (Lenovo IdeaPad Slim 5 16AKP10), 1059,99 €: Процессор и графика те же (AI 7 350, 860M), но память DDR5-5600 SO-DIMM: пропускная способность 89,6 ГБ/с против 136,5 ГБ/с у LPDDR5X-8533 (мой расчёт; сам эффект на графику не измерен). Корпус тихий и холодный: 42 дБ(A), PL1 25–36 Вт в тесте NBC версии с AI 5 330 (https://www.notebookcheck.net/Dual-debut-in-the-Lenovo-IdeaPad-Slim-5-16-Ryzen-AI-5-330-and-Radeon-820M-in-review.1166676.0.html); с AI 7 350 длительная мощность не проверена. Экран — главная потеря: 57,6 % sRGB, 39,1 % P3, 349 нит, ШИМ нет. Лучший ремонт: два слота, второй M.2.
- 6 — BM9T4EA#ABD (HP OmniBook 7 AI 16-ay0770ng), 979,30 €: Самый мощный вариант в бюджете. Ultra 7 255H — R23 17 845; Arc 140T — Time Spy 3843. В Puget Premiere Arc 140T быстрее 860M на 27 % в общем зачёте (3661 против 2882) и на 53 % в Lumetri ×40 (18,2 против 11,9) (https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/23/GPU/AMD%20Radeon%20860M%20Graphics/Intel%20Arc%20130T%20GPU%20%2816GB%29/ ; https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/23/GPU/AMD%20Radeon%20890M%20Graphics/Intel%20Arc%20140T%20GPU%20%2816GB%29/). Декодирует HEVC 4:2:2 и кодирует AV1. Но у потребительских HP есть риск выключенного HEVC (https://h30434.www3.hp.com/t5/Notebook-Video-Display-and-Touch/H265-HEVC-HW-encoder-and-decoder-not-available/td-p/9431209): если HEVC выключен, 4K-исходники декодирует процессор. Экран 62,5 % sRGB с DC dimming (https://www8.hp.com/h20195/V2/GetPDF.aspx/c09154072) — для цвета мало. Нагрев и шум не измерены, память распаяна, надёжность HP низкая.
- 5.5 — 22AY003WGE (Lenovo ThinkPad E16 Gen 3, 228V) + SSD, 1038,06 €: Медиадвижок лучший в списке: HEVC 4:2:2 и AV1; графика Arc 130V — Time Spy 3401. Корпус тихий. Но процессор слабый для длительной нагрузки: 8 потоков, R23 9932, длительная мощность Lunar Lake в ThinkPad E — 28 Вт (https://www.notebookcheck.net/Lenovo-ThinkPad-E14-Gen-7-review-Lunar-Lake-delivers-longer-battery-life-but-brings-trade-offs.1170838.0.html). H.264 4:2:2 10 бит в 1100 € никто не декодирует аппаратно — его декодирует процессор, и здесь он самый слабый. Экран 58,2 % sRGB у той же спецификации панели (https://www.notebookcheck.net/Lenovo-ThinkPad-E16-Gen-2-AMD-laptop-review-Cuts-corners-mostly-in-the-right-places.899320.0.html). Память распаяна, на завод стоит 512 ГБ — меняем на 1 ТБ.
- 5 — 83HS00BLGE (Lenovo IdeaPad Slim 5 16IRH10, i7-13620H), 993,30 €: Аппаратно декодирует HEVC 4:2:2 (https://www.pugetsystems.com/labs/articles/what-h-264-and-h-265-hardware-decoding-is-supported-in-premiere-pro-2120/), процессор сильный (R23 15 176, 43 Вт длительно). Но корпус горячий и громкий: 96 °C в среднем (https://laptopmedia.com/review/lenovo-ideapad-slim-5i-16-gen-10-review-a-great-laptop-held-back-by-our-bad-choices/), 50,4 дБ(A) (https://www.notebookcheck.com/Lenovo-IdeaPad-Slim-5-16IRH10.1089950.0.html). Графика UHD (Time Spy 1110) в 2,3 раза слабее 860M — эффекты и цветокоррекция будут тормозить. AV1 не кодирует, HDMI 1.4b, экран 57,7 % sRGB (https://www.notebookcheck.com/Lenovo-IdeaPad-Slim-5-16-Laptop-im-Test-Intel-Core-i5-vs-AMD-Ryzen-5.1174964.0.html). Рядом по оценке — Vivobook S16 M3607HA (5): сильный R7 260, но шумный корпус и экран без замеров.

**Довод:** Коротко: беру Acer R2R1, потому что это единственный ноутбук ≤ 1100 €, где экран годится для цвета, а процессор и графика — не хуже лидеров обеих веток.

1. Экран. Внешнего монитора не будет, поэтому экран — это то, что видит монтажёр при каждой цветокоррекции.
   - У 25 из 26 кандидатов «купить сейчас» бюджетные IPS: NBC и LaptopMedia намеряют у таких панелей 50–63 % sRGB (AMD/notes/displays.md). Насыщенные цвета на них бледнее, и никакой профиль этого не исправит: панель просто не показывает эти цвета.
   - У R2R1 — OLED 95–100 % DCI-P3 (даташит Acer, Icecat). Широкий охват можно сузить до sRGB/Rec.709 профилем или управлением цветом в программе, а узкий расширить нельзя. Это мой вывод, не цитата. Сам экземпляр надо проверить: есть ли sRGB-режим; в Premiere есть Display Color Management, в Resolve под Windows — не проверено.
   - Ближайший замер: Acer Swift Air 16, WUXGA OLED — 100 % sRGB и P3 (LaptopMedia).
2. Процессор. Ryzen AI 7 350 — на уровне лидеров обеих веток: медиана R23 16 015 против 16 015 у AMD №1 и 15 176 у Intel №1 (NBC).
   - Сколько корпус толщиной 15,9 мм держит длительно — не проверено. В комплекте блок 100 Вт.
   - Родственный Acer Swift Go 16 AI с тем же чипом держит 45 Вт, R23 16 150 (NBC).
3. Графика для эффектов. 860M в R2R1 стоит на LPDDR5X-8533, это на 52 % больше пропускной способности, чем у SO-DIMM DDR5-5600 в Lenovo (мой расчёт).
   - 860M в 2,3 раза сильнее UHD у Intel №1 (Time Spy 2565 против 1110, NBC).
   - В Resolve 860M на 12 % быстрее Meteor Lake Arc: 2402 против 2151 (https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/27/GPU/AMD%20Radeon%20860M%20Graphics/Intel%20Arc%20Graphics/).
   - Быстрее только Arc 140T у HP — на 27 % в Premiere, но у HP есть риск выключенного HEVC, а экран у него 62,5 % sRGB.
4. Неизвестный кодек.
   - HEVC 4:2:2 на AMD декодирует процессор. В экспорте Puget (Resolve 20) у AI 7 350 43,4 кадра/с, у Arc 140T 56,3, у Meteor Lake с аппаратным декодом 41,7 (AMD/notes/amd-codecs.md).
   - H.264 4:2:2 10 бит в 1100 € не декодирует аппаратно никто: там решает процессор, и у R2R1 он сильный.
   - Дыра в кодеках лечится прокси и оптимизированными медиа — это есть в любой монтажной программе. Плохой экран без внешнего монитора не лечится ничем.
5. Порты (бонус): 2× USB4, HDMI 2.1, microSD — лучше, чем у обоих IdeaPad.
6. Почему не Swift Air 16 OLED (999 €): экран у него измерен, но Ryzen AI 5 330 — R23 7840, графика 820M — Time Spy 786. Для 4K это вдвое слабее R2R1.

Что сделать в пределах 30 дней на возврат (computeruniverse):
- DXVA Checker — есть ли HEVC. Acer после спора с Nokia продаёт в Германии часть устройств «ohne HEVC-Codec», по словам Acer это ставится отдельным ПО (https://www.channelpartner.de/article/4187748/acer-und-asus-liefern-wieder.html).
- ШИМ на малой яркости.
- Cinebench R23 в цикле 10 минут и шум.
Если что-то не так — вернуть и брать запасной 83HY008CGE.

Перед заказом пересчитать цену: у R2R1 всего два предложения, второе — 1111,90 €, выше потолка.

**Что теряет владелец:** 1. Аппаратный декод HEVC 4:2:2 10 бит (есть у любого Intel 11+). Такие файлы декодирует процессор: ~43 кадра/с в экспорте Puget против 56 у Arc 140T. На многодорожечном таймлайне 4:2:2 могут понадобиться прокси — не проверено.
2. Расширение и ремонт. 32 ГБ распаяны навсегда. Сколько слотов M.2 — не проверено, в Icecat указан один установленный SSD. Сервис-мануалов у Acer нет. Запасной Lenovo здесь сильно лучше: два слота памяти и два M.2.
3. Неизмеренный экран и корпус:
   - ШИМ, скорее всего, есть: у Acer Swift Go 16 AI OLED NBC намерил 220 Гц при амплитуде 82 %, у Swift Air — ШИМ «с ограниченной амплитудой».
   - Экран глянцевый, 300 нит — в светлой комнате блики.
   - Длительная мощность и шум неизвестны; у родственного Acer — 52–53 дБ(A) и горячий воздух из-под экрана.
   - У IdeaPad AMD против этого — 42 дБ(A) и нет ШИМ.
4. Надёжность и HEVC. Techradar поставил 60 % и пишет о проблемах сборки (сборник NBC https://www.notebookcheck.net/Acer-Aspire-16-AI-A16-61M.1237489.0.html). Есть риск HEVC у Acer в Германии — проверить в первые дни.
5. Деньги и запас. На 21,22 € дороже запасного Lenovo и на 87,91 € дороже Intel 83HS00BLGE. До потолка 1100 € остаётся всего 18,79 €, а предложение за 1081,21 € одно.
6. Цена ошибки:
   - Если OLED или HEVC окажутся плохими — возврат за 30 дней и потерянное время, а у запасного тоже одно предложение.
   - Если взять вместо него IPS 57 % sRGB (оба IdeaPad, E16) — каждое видео после цветокоррекции будет выглядеть у зрителя иначе, чем на экране монтажёра, и без внешнего монитора это не исправить.

## Черновик итогового отчёта синтезатора (выбор — Acer R2R1)

### (черновик) Какой ноутбук брать: Intel или AMD

_30.09.2026, вечер. Монтаж 4K под Windows, Германия, до 1100 € с докупкой — жёстко._
_Вводные владельца 30.09: кодек и программа неизвестны навсегда; покупка сейчас; внешнего монитора не будет; планку и SSD ставит сам; порты — бонус._
_Цены — idealo в Chrome, перепроверены в 20:40, критик — ещё раз в 20:50 (минимум нового товара с доставкой, маркетплейсы включительно). Разборы веток: [Intel/REPORT.md](../../Intel/REPORT.md), [AMD/REPORT.md](../../AMD/REPORT.md)._

## Выбор — AMD: Acer Aspire 16 AI OLED A16-61M-R2R1

- **P/N `NX.JP0EG.00Z`.** Ryzen AI 7 350 (8 ядер / 16 потоков) и Radeon 860M, 32 ГБ LPDDR5X распаяны, SSD 1 ТБ PCIe 4. Экран — 16" OLED WUXGA. Блок 100 Вт в комплекте, 1,55 кг, 65 Втч, гарантия 2 года ([даташит Acer](https://gzhls.at/blob/ldb/e/9/9/4/1b8b6ae3e1047dc798a552be0d80e9a0f0ab.pdf)).
- **Итог — 1081,21 €, докупать ничего не нужно.** Продаёт computeruniverse.net, возврат 30 дней ([idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/211631508_-aspire-16-ai-a16-61m-r2r1-acer.html), 20:40; в 20:50 — то же).
  До потолка остаётся 18,79 €. Второе предложение, у e-tec, стоит 1111,90 € — это уже выше потолка.

**Почему он:**
1. **Это единственный экран для работы с цветом в бюджете при процессоре, который тянет 4K.** Второй OLED до 1100 € — Swift Air 16 с 4-ядерным AI 5 330 (см. «Запасной вариант»). OLED, 95 % DCI-P3 по даташиту Acer, 100 % по [Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Acer&ProductCode=NX.JP0EG.00Z).
   - У остальных финалистов IPS класса «45 % NTSC». NBC намеряет у таких панелей 57–58 % sRGB ([displays.md](../../AMD/notes/displays.md)).
   - «62,5 % sRGB» у HP — тот же класс: по площади треугольника охвата это примерно 44 % NTSC (мой расчёт).
   - Ближайший замер — у Swift Air 16 с WUXGA OLED: 100 % sRGB и 100 % P3 ([LaptopMedia](https://laptopmedia.com/de/review/acer-swift-air-16-sfa16-61m-review-a-16-inch-laptop-that-weighs-under-1-kg/)).
   - Внешнего монитора не будет, поэтому узкий охват не исправить ничем. Широкий можно сузить до sRGB профилем или режимом экрана (мой вывод).
2. **По мощности — на уровне лидеров обеих веток.**
   - Процессор: 16 015 в Cinebench R23 (медиана NBC) против 15 176 у Intel №1 ([NBC CPU](https://www.notebookcheck.net/Mobile-Processors-Benchmark-List.2436.0.html)).
   - Графика 860M: 2565 в Time Spy — в 2,3 раза больше, чем у UHD в Intel №1 (1110) ([NBC GPU](https://www.notebookcheck.net/Mobile-Graphics-Cards-Benchmark-List.844.0.html)).
3. **Самые вероятные исходники 4:2:0 он декодирует аппаратно.** Это смартфоны, GoPro, DJI и беззеркалки в режиме по умолчанию. Плюс кодирует AV1 ([AMD AMF](https://github.com/GPUOpen-LibrariesAndSDKs/AMF/wiki/GPU%20and%20APU%20HW%20Features%20and%20Support), [amd-codecs.md](../../AMD/notes/amd-codecs.md), §3.2).
   HEVC 4:2:2 декодирует процессор. Экспорт в Resolve 20 при этом идёт со скоростью 43,4 кадра/с. Для сравнения: Meteor Lake с аппаратным декодом — 41,7, Arc 140T — 56,3 ([PB2](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/27/GPU/AMD%20Radeon%20860M%20Graphics/Intel%20Arc%20Graphics/), [PB1](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/27/GPU/AMD%20Radeon%20890M%20Graphics/Intel%20Arc%20140T%20GPU%20%2816GB%29/)).
4. **В бесплатном Resolve аппаратного декода нет ни у кого** — он есть только в Studio ([Blackmagic](https://documents.blackmagicdesign.com/SupportNotes/DaVinci_Resolve_21_Supported_Codec_List.pdf)). Там преимущество Intel в 4:2:2 исчезает, и решают процессор и графика.
5. **Порты (бонус):** 2× USB4, HDMI 2.1, microSD ([даташит Acer](https://gzhls.at/blob/ldb/e/9/9/4/1b8b6ae3e1047dc798a552be0d80e9a0f0ab.pdf)).

## Запасной вариант — Intel: HP OmniBook 7 AI 16-ay0770ng

- **P/N `BM9T4EA#ABD`, 979,30 €.** Продавец один — hp.com, в 20:40 и 20:50 цена та же ([idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/206602335_-omnibook-7-ai-16-ay0770ng-hp.html)). HP Store даёт 30 дней на возврат ([HP](https://www.hp.com/de-de/shop/faq/returns/how-to-return-and-request-refund-or-replacement)), по idealo — 14.
- **Когда брать:** R2R1 раскупили или он подорожал выше 1100 €.
  Другого OLED с процессором, который тянет 4K, до 1100 € нет. Swift Air 16 OLED `NX.DL5EG.002` стоит 993,50 € (expert, 20:50), но в нём Ryzen AI 5 330 — 4 ядра ([idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/211778543_-swift-air-16-oled-16-wuxga-amd-ryzen-ai-5-32gb-1tb-ssd-silber-nx-dl5eg-002-acer.html)).
- **Почему именно он.** Без OLED экраны у всех одного класса. Тогда решают мощность и ширина декода, и здесь HP лучший в бюджете ([даташит HP](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09154072)):
  - процессор 255H — 17 845 в R23, графика Arc 140T — 3843 в Time Spy;
  - декодирует HEVC 4:2:2, кодирует AV1;
  - экран с DC dimming;
  - TB4 и HDMI 2.1.
- **Условие.** HP уже отключала HEVC без упоминания в документах ([HP Community](https://h30434.www3.hp.com/t5/Notebook-Video-Display-and-Touch/H265-HEVC-HW-encoder-and-decoder-not-available/td-p/9431209), [smith6612](https://smith6612.me/2026/04/19/its-me-i-started-the-hevc-disablement-press-storm/)). Поэтому в первый же день — DXVA Checker. Если HEVC нет, ноутбук вернуть.
- **Третья линия — Lenovo IdeaPad Slim 5 16IRH10 `83HS00BLGE`, 993,30 €.** Kaufland (маркетплейс, возврат 14 дней), ещё 5 предложений за 995–1005 € и Galaxus (маркетплейс) за 1323,47 € — всего 7, в 20:50 ([idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/209881995_-ideapad-slim-5-16-83hs00blge-lenovo.html)).
  Это самый безопасный вариант: сообщений об отключении HEVC у Lenovo не нашли ([browser-check-hevc.md](../../Intel/notes/browser-check-hevc.md), п. 5.4), память 2×16 SO-DIMM ([PSREF](https://psref.lenovo.com/Detail/IdeaPad/IdeaPad_Slim_5_16IRH10?M=83HS00BLGE)), HEVC 4:2:2 декодирует ([Puget](https://www.pugetsystems.com/labs/articles/what-h-264-and-h-265-hardware-decoding-is-supported-in-premiere-pro-2120/)). Но графика UHD — 1110 в Time Spy, а экран такой же узкий.

## Что теряем с R2R1

1. **Аппаратный декод HEVC 4:2:2 10 бит.** Такие файлы пишут Sony в режиме XAVC HS 4:2:2, Canon в 10 битах и Fuji.
   - Их декодирует процессор. Таймлайн будет тяжёлым: у Framework 13 с 7640U такие файлы грузят процессор на 70–100 % ([Framework](https://community.frame.work/t/42-video-on-amd/64502)). Выход — прокси.
2. **Форматы, которые в бюджете аппаратно не декодирует никто:** H.264 4:2:2 10 бит, ProRes, All-I. Они идут на процессор или через прокси.
   Закрыли бы их только ноутбуки дороже потолка:
   - RTX 50 — Gigabyte GAMING A16 `3VHK3DE894SH` с планкой за 1286,56 € ([idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/207329496_-gaming-a16-3vhk3de894sh-gigabyte.html)); MSI `B2RWFKG-068` в 20:50 подорожал до 1199 €, с планкой — 1386,56 € ([idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/206837107_-cyborg-15-b2rwfkg-068-msi.html));
   - Panther Lake с Resolve Studio 21 — `21UR005AGE` за 1204,00 € (easynotebooks, 20:50; 1202,91–1203,73 € — только с купоном) ([idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/209497615_-thinkbook-16-g9-21ur005age-lenovo.html)).
3. **Графика слабее, чем у HP.** В Premiere общий балл 2882 против 3661, в Lumetri ×40 — 11,9 кадра/с против 18,2 ([PB8](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/23/GPU/AMD%20Radeon%20860M%20Graphics/Intel%20Arc%20130T%20GPU%20%2816GB%29/), [PB6](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/23/GPU/AMD%20Radeon%20890M%20Graphics/Intel%20Arc%20140T%20GPU%20%2816GB%29/)).
4. **Расширение и ремонт.**
   - 32 ГБ распаяны навсегда. Сколько слотов M.2 — не проверено.
   - Сервис-мануалов у Acer нет ([brands.md](../../Intel/notes/brands.md)).
   - Techradar дал ему 60 % и отмечает «build quality issues» ([сборник NBC](https://www.notebookcheck.net/Acer-Aspire-16-AI-A16-61M.1237489.0.html)).
5. **Экран не измерен.**
   - ШИМ вероятен: у родственного Swift Go 16 AI OLED NBC намерил 220 Гц ([NBC](https://www.notebookcheck.com/Solide-Performance-und-farbechtes-OLED-Acer-Swift-Go-16-AI-mit-AMD-Ryzen-im-Test.1102652.0.html)).
   - Глянец, 300 нит, 60 Гц ([Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Acer&ProductCode=NX.JP0EG.00Z), [displays.md](../../AMD/notes/displays.md)).
6. **Риск с HEVC у Acer.** В Германии Acer продаёт часть устройств «ohne HEVC-Codec». По словам Acer, это программный кодек, и его ставят отдельно ([ChannelPartner](https://www.channelpartner.de/article/4187748/acer-und-asus-liefern-wieder.html)).
7. **Деньги.** Запас до потолка — 18,79 €. Это на 101,91 € дороже HP и на 87,91 € дороже `83HS00BLGE`. Порта RJ45 нет — это бонус, но его нет.

## Финалисты

| Ветка | Модель · P/N (idealo) | Итог | Экран | CPU (R23) / iGPU (Time Spy) | Аппаратный декод | Средн. в отчёте | Судьи: кодеки / мощн. и экран / риски |
|---|---|---|---|---|---|---|---|
| AMD | Acer Aspire 16 AI OLED · [`NX.JP0EG.00Z`](https://www.idealo.de/preisvergleich/OffersOfProduct/211631508_-aspire-16-ai-a16-61m-r2r1-acer.html) | **1081,21 €** | OLED 95–100 % P3, не измерен | AI 7 350 16 015 / 860M 2565 | 4:2:0, AV1 (кодирование); 4:2:2 нет | 5,5 (AMD №10) | — / **7,5** / 3 |
| Intel | HP OmniBook 7 16 · [`BM9T4EA#ABD`](https://www.idealo.de/preisvergleich/OffersOfProduct/206602335_-omnibook-7-ai-16-ay0770ng-hp.html) | 979,30 € | IPS 62,5 % sRGB, DC dimming | 255H 17 845 / Arc 140T 3843 | + HEVC 4:2:2, AV1; риск отключения HEVC | 6 (Intel №8) | **8** / 6 / — |
| Intel | IdeaPad Slim 5 16IRH10 · [`83HS00BLGE`](https://www.idealo.de/preisvergleich/OffersOfProduct/209881995_-ideapad-slim-5-16-83hs00blge-lenovo.html) | 993,30 € | IPS 45 % NTSC (NBC: 57,7 % sRGB) | i7-13620H 15 176 / UHD 1110 | + HEVC 4:2:2; AV1 нет | 7 (Intel №1) | 7 / 5 / **8** |
| Intel | ThinkPad E16 Gen 3 · [`22AY003WGE`](https://www.idealo.de/preisvergleich/OffersOfProduct/209382343_-thinkpad-e16-g3-22ay003wge-lenovo.html) + SSD | 1038,06 € | IPS 45 % NTSC (NBC: 58,2 %) | 228V 9932 / Arc 130V 3401 | + HEVC 4:2:2, AV1 | 6,5 (Intel №6) | 6,5 / 5,5 / 7 |
| AMD | IdeaPad Slim 5 16AKP10 · [`83HY008CGE`](https://www.idealo.de/preisvergleich/OffersOfProduct/209439304_-ideapad-slim-5-16-83hy008cge-lenovo.html) | 1059,99 € | IPS 45 % NTSC (NBC: 57,6 %) | AI 7 350 16 015 / 860M 2565 | 4:2:0, AV1; 4:2:2 нет | 7 (AMD №1) | 6 / 6,5 / 6 |

- «—» — судья не взял ноутбук в финалисты. Судья по кодекам не взял R2R1: нет 4:2:2 и есть риск с HEVC у Acer. Судья по рискам не взял HP: риск с HEVC у HP.
- Цены сняты в 20:40; критик перепроверил в 20:50 — у всей пятёрки и у SSD без изменений.
  - `22AY003WGE`: 917,07 € у jacob.de + SSD Verbatim Vi3000 1 ТБ за 120,99 € у notebooksbilliger ([idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/202702551_-vi3000-1tb-verbatim.html)). «ab 912,33 €» в заголовке карточки — цена с купоном, она не считается.
  - `83HY008CGE`: предложение одно, Kaufland (маркетплейс).
- Экраны — [displays.md](../../AMD/notes/displays.md). R23 и Time Spy — медианы NBC ([CPU](https://www.notebookcheck.net/Mobile-Processors-Benchmark-List.2436.0.html), [GPU](https://www.notebookcheck.net/Mobile-Graphics-Cards-Benchmark-List.844.0.html)).
- Вне пятёрки — ещё два ноутбука, каждый назвал только один судья:
  - Acer Aspire Go 16 `NX.JS9EG.005` — 849 € ([idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/209373295_-aspire-go-16-ag16-71p-97gf-acer.html)): блок 65 Вт, риск с HEVC у Acer;
  - ThinkBook 16 G7 `21MW00AYGE` — 998,99 € ([idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/207306483_-thinkbook-16-g7-21mw00ayge-lenovo.html)): Zen 3+, графика RDNA 2 в maintenance.

## Почему AMD

- **Что дали два анализа.**
  - Intel: HEVC 4:2:2 декодируют все кандидаты, но экрана для цвета до 1100 € нет ([Intel/REPORT.md](../../Intel/REPORT.md), «Итог коротко», п. 3).
  - AMD: графика сильнее, есть AV1, но 4:2:2 не декодирует никто. Экран для цвета есть только у двух Acer OLED ([AMD/REPORT.md](../../AMD/REPORT.md), [display-sweep.md](../../AMD/notes/display-sweep.md)).
- **Почему финал не по «Средн.».** В отчётах лидируют `83HS00BLGE` и `83HY008CGE` — по 7. Но там экран — лишь 25 % «Мощн.», то есть 5 % итоговой оценки. Владелец сделал экран одним из главных критериев, поэтому финал решён не по «Средн.».
- **Как разошлись судьи.** Судья по кодекам выбрал HP, судья по рискам — `83HS00BLGE`, судья по мощности и экрану — R2R1.
- **Двое за Intel против одного за AMD — с большинством не согласен.** Их линзы экран не взвешивали, и оба судьи сами признают, что для цвета их выбор не годится.
  Судья по рискам пишет: если нужен точный цвет, «ошибкой будет любой Lenovo в бюджете», и тогда — Acer OLED.
  Довод судьи по экрану никто не опроверг: дыру в кодеках лечат прокси, а плохой экран без внешнего монитора не лечится ничем.
- **Где с большинством согласен — риски R2R1 реальны.** Предложение одно, карточка смешанная, экран не измерен, есть риск с HEVC у Acer.
  - Поэтому: заказывать сейчас, проверять в течение 30 дней на возврат.
  - Запасной — HP: судьи по кодекам и по экрану ставят его выше `83HS00BLGE` (8 против 7 и 6 против 5).
  - Третья линия — `83HS00BLGE`, выбор судьи по рискам.
  - Сомнение судьи по рискам насчёт блока питания снято: в даташите Acer — «100W Netzteil».

## Что сделать при покупке

1. **Перед заказом** открыть [карточку](https://www.idealo.de/preisvergleich/OffersOfProduct/211631508_-aspire-16-ai-a16-61m-r2r1-acer.html) и найти предложение computeruniverse: в названии должно быть «Ryzen AI 7 350 32GB/1TB».
   В [той же карточке](https://www.idealo.de/preisvergleich/OffersOfProduct/211631508_-aspire-16-ai-a16-61m-r2r1-acer.html) продаётся R5H7 `NX.JP0EG.010` (AI 5 330, 16/512) от 794,83 € — это не он. У computeruniverse и cyberport есть и предложения с «A16-61M-R2R1» в названии, но с «Ryzen AI 5 330 16GB/512GB» за 801,82 € — тоже не он (20:50, [prices-final.md](../../AMD/notes/prices-final.md)).
   Если цена выше 1100 € или предложения нет — брать запасной.
2. **Докупать — ничего:** 32 ГБ, 1 ТБ и зарядка 100 Вт уже в комплекте. У HP и `83HS00BLGE` докупка тоже не нужна.
3. **В первые дни**, до своих программ (у computeruniverse 30 дней на возврат):
   - **DXVA Checker → Decoder Device:** должны быть `HEVC_VLD_Main` и `HEVC_VLD_Main10`. Профилей 4:2:2 у AMD нет — это нормально ([hevc-amd.md](../../AMD/notes/hevc-amd.md), §4). Если HEVC нет — вернуть;
   - **HandBrake**, пресет «H.265 VCN 2160p 4K»: кодирование через AMF работает;
   - **CPU-Z или HWiNFO:** Ryzen AI 7 350, 32 ГБ LPDDR5X, память не в одноканальном режиме;
   - **нагрузка:** экспорт 4K-ролика и 10 минут Cinebench R23 в цикле — смотреть частоты, температуру, шум;
   - **экран:**
     - мерцание на 20–30 % яркости (камера телефона в замедленной съёмке);
     - битые пиксели и однородность на сером фоне;
     - есть ли режим sRGB — не проверено.
4. **Если что-то не так** — вернуть в срок и брать HP. Проверки те же, плюс:
   - в DXVA Checker — `HEVC_VLD_Main10` и профиль 4:2:2;
   - экспорт H.265 10 бит через QSV в HandBrake;
   - в Диспетчере задач графика определилась как «Arc 140T».

## Ветки

- Intel — [Intel/REPORT.md](../../Intel/REPORT.md); AMD и сравнение веток — [AMD/REPORT.md](../../AMD/REPORT.md), «AMD против Intel».
- Цены вечера 30.09 — [AMD/notes/prices-final.md](../../AMD/notes/prices-final.md); экраны — [AMD/notes/displays.md](../../AMD/notes/displays.md), [AMD/notes/display-sweep.md](../../AMD/notes/display-sweep.md).
