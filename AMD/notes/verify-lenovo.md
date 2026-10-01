## Проверка lenovo (AMD)

_Проверено 30.09.2026, ~15:20–16:10 (скептик по `candidates-lenovo.md`). 33 SKU шорт-листа + выборочно 7 отброшенных._
_Память, SSD, БП — PDF-экспорт PSREF по каждому MTM, скачан заново (`https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=<MTM>&country_code=`), второе мнение — Icecat open (для 9 SKU в бюджете)._
_Цены — idealo.de в Chrome пользователя, своя вкладка: карточка каждого P/N + API истории `price-chart/sites/1/products/<pid>/history?period=1Y`. Цена = минимум нового товара с доставкой у любого продавца, маркетплейсы включительно ([`../../CLAUDE.md`](../../CLAUDE.md)); купонные («Preis inkl. Gutschein») и б/у — отдельно._
_CPU — [`amd-cpu.md`](amd-cpu.md), кодеки — [`amd-codecs.md`](amd-codecs.md), HEVC — [`hevc-amd.md`](hevc-amd.md), обзоры — Notebookcheck (NBC)._

### Вывод

1. **Раскладка памяти подтверждена у всех 33 SKU** — PDF PSREF по каждому MTM; у 9 SKU в бюджете совпадает и Icecat («Speicherlayout 2 x 16 GB» / у 21KK007TGE «1 x 16 GB»). Ни одного 1×32 и ни одной скрытой распайки среди A/C. Опровергнуть не удалось.
   Второй M.2 свободен у всех A/C: PSREF «Lenovo offers only one SSD configuration with a second slot for user self-expansion». У NBC 16AKP10 это подтверждено вскрытием («The 2280 slot is free»).
2. **Главная поправка — цена SSD.** Самый дешёвый новый NVMe 1 ТБ M.2 2280 на idealo — **Verbatim Vi3000 (PCIe 3.0) 120,99 €** с доставкой, notebooksbilliger.de, возврат 30 дней ([карточка](https://www.idealo.de/preisvergleich/OffersOfProduct/202702551_-vi3000-1tb-verbatim.html)), а не Kingston NV3 за 142,89 €. PCIe 4.0 — Silicon Power UD90 138,97 € ([карточка](https://www.idealo.de/preisvergleich/OffersOfProduct/202130035_-ud90-1tb-m-2-silicon-power.html)), NV3 142,89 € ([карточка](https://www.idealo.de/preisvergleich/OffersOfProduct/204697967_-nv3-1tb-kingston.html)).
   Все C-итоги дешевле на 21,90 €. **21KK007TGE (1×16 + 512 ГБ) входит в бюджет: 849 + 113,17 + 120,99 = 1083,16 €** (было «1105,06 — на 5 € выше»). Но процессор там — ловушка Barcelo-R.
3. **В бюджете остаются 5 A и 3 C + один B16+C.** Лучший по железу — **83HY008CGE** (AI 7 350, Zen 5, 860M, 1059,99 €). Единственный продавец — Kaufland-маркетплейс (expert Deutschland, возврат 14 дней). По правилу пользователя цена засчитывается.
   Самый дешёвый A — 21MW00AYGE (998,99 €), но Zen 3+ 2022 года, и сейчас это максимум цены за год (минимум 731,36 €).
4. **Мелкие поправки цен:**
   - 21UT004QGE — 1072,00 €, а не 1073.
   - 21UT000KGE — 1252,90 €, а не 1246.
   - 83UU001LGE — от 789,95 €, а не 759.
   - L16 / T16 / P16s — на 5–12 € дороже, чем записано.
   **21M5002DGE найден:** карточка [208145740](https://www.idealo.de/preisvergleich/OffersOfProduct/208145740_-thinkpad-e16-g2-21m5002dge-lenovo.html), 1199 € (electronic4you.de). Минимум за год — 949 € (24.11.2025), ≤ 1100 € — 96 дней из 182, последний раз 17.08.2026. У Yoga 7a 16 (83TF003WGE), IdeaPad Pro 5a (83SJ000TGE) и Slim 5 15ARP10 (83J3008LGE) **нет блока питания** (PSREF), +22,03 €.
5. **HEVC:** в 38 скачанных PDF PSREF слов HEVC/H.265 нет (0 совпадений). Отключение у Lenovo на AMD не задокументировано ([`hevc-amd.md`](hevc-amd.md), п. 7). Прямого подтверждения, что HEVC включён, тоже нет → в срок возврата проверить DXVA Checker.
6. **Экран у всех A/C слабый для цвета:** WUXGA IPS, 45 % NTSC. NBC намерил у тех же корпусов 57,6–59,8 % sRGB. Для цветокоррекции 4K нужен внешний монитор.

### Сводная таблица — в бюджете (idealo, 30.09.2026 ~15:30)

| MTM · модель | CPU (кремний) · iGPU | Память (PSREF) | SSD / 2-й M.2 | БП | Цена сейчас, € (магазин) | Мин. 1 год | ≤ 1100 из 182 | Итог, € | Вердикт |
|---|---|---|---|---|---|---|---|---|---|
| [83HY008CGE](https://www.idealo.de/preisvergleich/OffersOfProduct/209439304_-ideapad-slim-5-16-83hy008cge-lenovo.html) · IdeaPad Slim 5 16AKP10 | AI 7 350 — Krackan, 4 Zen 5 + 4 Zen 5c · 860M | 2×16 SO-DIMM DDR5-5600 ✅ | 1 ТБ 2242 + свободный 2280 | 65 W ✅ | **1059,99** kaufland.de МП (expert Deutschland), возврат 14 дн., 1 предложение | 896,28 (23.02.2026) | 179/179 | **1059,99** | **A, подтверждено** — лучший CPU/iGPU |
| [21MW00AYGE](https://www.idealo.de/preisvergleich/OffersOfProduct/207306483_-thinkbook-16-g7-21mw00ayge-lenovo.html) · ThinkBook 16 G7 ARP | R5 7535HS — Rembrandt-R, Zen 3+ · 660M | 2×16 DDR5-4800 ✅ | 1 ТБ 2242; 2× M.2 2280 | 65 W ✅ | **998,99** easynotebooks.de, 14 дн.; 999,00 notebook.de | 731,36 (12.12.2025) | 182/182 | **998,99** | **A, подтверждено**; CPU 2022 г. |
| [21MW007VGE](https://www.idealo.de/preisvergleich/OffersOfProduct/207306221_-thinkbook-16-g7-21mw007vge-lenovo.html) · ThinkBook 16 G7 ARP | R7 7735HS — Rembrandt-R · 680M (12 CU) | 2×16 DDR5-4800 ✅ | 1 ТБ; 2× M.2 2280 | 65 W ✅ | **1088,57** cyclotron.de (возврат не указан); 1092,00 easynotebooks.de (14 дн.) | 808,60 (12.12.2025) | 182/182 | **1088,57** | **A, подтверждено**; запас 11 € |
| [21UT004QGE](https://www.idealo.de/preisvergleich/OffersOfProduct/209122445_-thinkbook-16-g9-21ut004qge-lenovo.html) · ThinkBook 16 G9 AHP | R5 220 = 8540U, 2 Zen 4 + 4 Zen 4c · 740M (4 CU) | 2×16 DDR5-5600 ✅ | 1 ТБ 2242 + свободный 2280 | 65 W ✅ | **1072,00** easynotebooks.de (14 дн.) / c-nw.de; купон 1071,72 — не в минимум | 999,00 (21.01.2026) | 52/182 | **1072,00** | A, **цена исправлена** (было 1073); CPU урезанный — «не брать» |
| [21KK0074GE](https://www.idealo.de/preisvergleich/OffersOfProduct/203811127_-thinkbook-16-g6-21kk0074ge-lenovo.html) · ThinkBook 16 G6 ABP | R7 7730U — Barcelo-R, Zen 3 · Vega 8 | 2×16 **DDR4-3200** ✅ | 1 ТБ; 2× M.2 2280 **PCIe 3.0** | 65 W ✅ | **1007,99** electronic4you.de (AT, возврат не указан); дальше 1149 | 767,62 (05.10.2025) | 176/182 | **1007,99** | A формально; **CPU-ловушка** (VCN 2.2 — AV1 не декодирует) |
| [83HU004KGE](https://www.idealo.de/preisvergleich/OffersOfProduct/210287882_-ideapad-slim-5-16-83hu004kge-lenovo.html) · IdeaPad Slim 5 16ARP10 | R5 7535HS — Rembrandt-R · 660M | 2×16 DDR5-4800 ✅ | **512 ГБ** 2242 + свободный 2280 | **нет** (PSREF «No Power Adapter», Icecat «AC-Netzadapter: Nein») | **776,90** technik-brandenburg.de (возврат не указан); 799 expert.de (14 дн.) | 699,00 (20.05.2026) | 125/125 | 776,90 + 120,99 + 22,03 = **919,92** | **C, итог исправлен** (было 941,82) |
| [21MW009MGE](https://www.idealo.de/preisvergleich/OffersOfProduct/206598202_-thinkbook-16-g7-21mw009mge-lenovo.html) · ThinkBook 16 G7 ARP | R5 7535HS · 660M | 2×16 DDR5-4800 ✅ | **512 ГБ**; 2× M.2 2280 | 65 W ✅ | **949,00** easynotebooks.de (14 дн.) | 672,26 (23.10.2025) | 182/182 | 949 + 120,99 = **1069,99** | **C, итог исправлен** (было 1091,89) |
| [21UT004EGE](https://www.idealo.de/preisvergleich/OffersOfProduct/209122443_-thinkbook-16-g9-21ut004ege-lenovo.html) · ThinkBook 16 G9 AHP | R5 220 · 740M | 2×16 DDR5-5600 ✅ | **512 ГБ** 2242 + свободный 2280 | 65 W ✅ | **949,00** Galaxus МП (HEINZSOFT), 30 дн.; купон 898,90 — не в минимум | 889,00 (26.09.2026) | 150/182 | 949 + 120,99 = **1069,99** | **C, итог исправлен**; CPU урезанный |
| [21KK007TGE](https://www.idealo.de/preisvergleich/OffersOfProduct/204414953_-thinkbook-16-g6-21kk007tge-lenovo.html) · ThinkBook 16 G6 ABP | R5 7430U — Barcelo-R · Vega 7 | **1×16** DDR4-3200 + свободный слот ✅ | **512 ГБ**; 2× M.2 2280 PCIe 3.0 | 65 W ✅ | **849,00** easynotebooks.de (14 дн.) | 647,97 (14.03.2026) | 182/182 | 849 + DDR4 113,17 + SSD 120,99 = **1083,16** | **B16 + C, исправлено: теперь ≤ 1100**; CPU-ловушка |

Докупка (idealo, 30.09):
- SSD 1 ТБ NVMe M.2 2280 — Verbatim Vi3000 **120,99 €** (NBB, 30 дн.); PCIe 4.0 — Silicon Power UD90 138,97 € (siliconpowereu.com) и Kingston NV3 142,89 € (alternate.de, 14 дн.). Ссылки — в п. 2 «Вывода». История NV3: год назад — 42 €.
- DDR4-3200 16 ГБ SO-DIMM — G.Skill F4-3200C22S-16GRS **113,17 €** (jacob.de) — [карточка](https://www.idealo.de/preisvergleich/OffersOfProduct/200683989_-ripjaws-16gb-so-dimm-ddr4-3200-cl22-f4-3200c22s-16grs-g-skill.html).
- DDR5-5600 16 ГБ SO-DIMM — Crucial CT16G56C46S5 248,89 € (alza.de) — [карточка](https://www.idealo.de/preisvergleich/OffersOfProduct/202284828_-16gb-ddr5-5600-cl46-ct16g56c46s5-crucial.html). В категории дешевле: Lenovo 4X71M23186 — от 199,90 € без доставки ([выдача SO-DIMM DDR5 16 ГБ](https://www.idealo.de/preisvergleich/ProductCategory/4552F102189756-102193939-102286859-107683716.html?sortKey=minPrice)). Ни один B16 с DDR5 в бюджет не попадает при любой из этих цен.
- Зарядка Lenovo 65 W USB-C 4X20M26272 — **22,03 €** (computeruniverse.net; 22,36 cyberport.de, 30 дн.) — [карточка](https://www.idealo.de/preisvergleich/OffersOfProduct/5584731_-65w-usb-c-4x20m26272-lenovo.html).

### По SKU (в бюджете)

#### IdeaPad Slim 5 16AKP10 — 83HY008CGE (EAN 199273505975)
- PSREF ([страница](https://psref.lenovo.com/Detail/IdeaPad/IdeaPad_Slim_5_16AKP10?M=83HY008CGE), [PDF](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=83HY008CGE&country_code=), анонс 23.10.2025):
  - память: «2x 16GB SODIMM DDR5-5600», «Two DDR5 SODIMM slots, dual-channel capable», «Up to 32GB DDR5-5600 offering» (сноска: максимум — по протестированным Lenovo модулям);
  - SSD: 1 ТБ M.2 2242; «Models with AMD Ryzen AI 5 340 / 350 processor: two M.2 slots • One M.2 2242 • One M.2 2280»;
  - экран: 16" WUXGA IPS 300 нит, 45 % NTSC, 60 Гц;
  - питание, вес, порты: 60 Втч, 65 W USB-C, ~1,85 кг; 2× USB-C 10 Гбит/с (PD, DP 1.4), HDMI 2.1, 2× USB-A, microSD. USB4 и RJ45 нет;
  - гарантия 2 года.
- Icecat ([open](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Lenovo&ProductCode=83HY008CGE)): «Speicherlayout 2 x 16 GB», «2x SO-DIMM», «AC-Netzadapter: Ja», 65 W.
- CPU: Krackan Point, 4 Zen 5 + 4 Zen 5c, 860M (8 CU), VCN 4.0.5 — декодирует и кодирует AV1. По [`amd-cpu.md`](amd-cpu.md) «AI 7 350 — ок/лучший». Для 4K — лучший вариант в группе; 4:2:2 не декодирует (как любой AMD).
- Цена: 1059,99 € — kaufland.de, маркетплейс, «Verkauf durch: expertDeutschland», возврат 14 дней, доставка до 06.10. Предложение **одно**, пометок б/у / B-Ware нет. История с 13.02.2026: минимум 896,28 € (23.02.2026), средняя 952,23 €; ≤ 1100 € — все 179 дней.
- Вердикт: **подтверждено, A, 1059,99 €.** Риск — один продавец: предложение может исчезнуть.

#### ThinkBook 16 G7 ARP — 21MW00AYGE (EAN 199272203506)
- PSREF ([страница](https://psref.lenovo.com/Detail/ThinkBook/ThinkBook_16_G7_ARP?M=21MW00AYGE), [PDF](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=21MW00AYGE&country_code=), анонс 11.07.2025):
  - память и SSD: 2×16 SO-DIMM DDR5-4800, два слота, до 64 ГБ; 1 ТБ M.2 2242, «Two M.2 2280 PCIe 4.0 x4 slots», второй — «for user self-expansion»;
  - экран: WUXGA IPS 300 нит, 45 % NTSC;
  - питание и вес: 45 Втч, 65 W, 1,7 кг;
  - порты: USB4 40 Гбит/с + USB-C 10 Гбит/с, HDMI 2.1, RJ45, SD;
  - гарантия 1 год.
- Icecat ([open](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Lenovo&ProductCode=21MW00AYGE)): «2 x 16 GB», адаптер «Ja».
- CPU: Rembrandt-R (Zen 3+, 6 ядер), 660M (6 CU), VCN 3.1.1 — AV1 только декодирует; RDNA 2 с 10.2025 в maintenance mode ([`amd-cpu.md`](amd-cpu.md), п. 5, 8). Для 4K H.264/HEVC 4:2:0 годится, эффекты в таймлайне — слабо.
- Цена: 998,99 € — easynotebooks.de (14 дн.); 999,00 notebook.de; 14 предложений. Минимум 731,36 € (12.12.2025); за 182 дня — 833,81 € (06.05.2026); средняя 848,78 €. Сейчас цена **на максимуме года**.
- Вердикт: **подтверждено, A, 998,99 €.**

#### ThinkBook 16 G7 ARP — 21MW007VGE (EAN 198158583695)
- PSREF ([страница](https://psref.lenovo.com/Detail/ThinkBook/ThinkBook_16_G7_ARP?M=21MW007VGE), [PDF](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=21MW007VGE&country_code=)): R7 7735HS (8C/16T), 680M; 2×16 DDR5-4800; 1 ТБ, 2× M.2 2280; остальное — как у 21MW00AYGE. Icecat ([open](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Lenovo&ProductCode=21MW007VGE)): «2 x 16 GB».
- CPU: Rembrandt-R, 8 ядер, 680M (12 CU) — вдвое больше блоков iGPU, чем у 660M; кодеки те же (VCN 3.1.1).
- Цена: 1088,57 € — cyclotron.de (срок возврата на idealo не указан, доставка до 05.10); 1092,00 easynotebooks.de (14 дн.); 20+ предложений. Минимум 808,60 € (12.12.2025), средняя 922,58 €.
- Вердикт: **подтверждено, A, 1088,57 €** (запас 11 €; у магазина с известным сроком возврата — 1092,00 €).

#### ThinkBook 16 G9 AHP — 21UT004QGE (EAN 199273311323)
- PSREF ([страница](https://psref.lenovo.com/Detail/ThinkBook/ThinkBook_16_G9_AHP?M=21UT004QGE), [PDF](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=21UT004QGE&country_code=)):
  - память и SSD: 2×16 DDR5-5600, до 64 ГБ; 1 ТБ 2242 + свободный 2280;
  - экран: WUXGA IPS **400 нит**, 45 % NTSC;
  - питание и вес: 48 Втч, 65 W, 1,7 кг;
  - порты: 2× USB4, HDMI 2.1, RJ45, SD.
  Icecat: «2 x 16 GB».
- CPU: Ryzen 5 220 = 8540U, 2 полных Zen 4 + 4 Zen 4c, 740M (4 CU), без NPU — [`amd-cpu.md`](amd-cpu.md), п. 8: «не брать». Медиадвижок современный (VCN 4.0.2, AV1 D/E), но iGPU 740M слабее 680M по числу блоков.
- Цена: **1072,00 €** — easynotebooks.de (14 дн.) и c-nw.de (в названии предложения — «30€ Gutschein, Sonderkonditionen ab 5 Stück»). 1071,72 € — technikdeals24 / heinzsoft, «Preis inkl. Gutschein» — купонная, не в минимум. История с 21.01.2026: минимум 999 €; ≤ 1100 € — 52 из 182 дней. Минимум за 182 дня в API — 1066,82 € сегодня: это, по-видимому, купонная цена.
- Вердикт: **исправлено: 1072,00 €** (было 1073). A, но CPU урезанный.

#### ThinkBook 16 G6 ABP — 21KK0074GE (EAN 197530285905)
- PSREF ([страница](https://psref.lenovo.com/Detail/ThinkBook/ThinkBook_16_G6_ABP?M=21KK0074GE), [PDF](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=21KK0074GE&country_code=)):
  - память и SSD: «2x 16GB SO-DIMM DDR4-3200»; 1 ТБ; «Two M.2 2280 PCIe 3.0 x4 slots» (сноска: «another SSD slot for user self-extension»);
  - экран: WUXGA 300 нит, 45 % NTSC;
  - питание и вес: **71 Втч**, 65 W, 1,7 кг.
  Icecat: «DDR4, 2 x 16 GB».
- CPU: Barcelo-R (Zen 3 ≈ 5825U), Vega 8, **VCN 2.2 — AV1 не декодирует** ([`amd-codecs.md`](amd-codecs.md)). Vega получает только критичные исправления. Для 4K — худший в списке.
- **Противоречие:** NBC у тестового G6 ABP (7530U) описал «two SO DIMM slots and one M.2-2280 slot» ([NBC](https://www.notebookcheck.net/Lenovo-ThinkBook-16-G6-review-The-inexpensive-multimedia-laptop-with-a-Ryzen-7000.774481.0.html)), а PSREF 21KK0074GE — два M.2 2280. Для A это неважно (1 ТБ с завода); для 21KK007TGE (C) — важно.
- Цена: 1007,99 € — electronic4you.de (Австрия, срок возврата не указан); следующий — 1149 €. Минимум 767,62 € (05.10.2025).
- Вердикт: **подтверждено, A формально, CPU-ловушка.**

#### IdeaPad Slim 5 16ARP10 — 83HU004KGE (EAN 199275056086)
- PSREF ([страница](https://psref.lenovo.com/Detail/IdeaPad/IdeaPad_Slim_5_16ARP10?M=83HU004KGE), [PDF](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=83HU004KGE&country_code=), анонс 22.01.2026):
  - память: 2×16 DDR5-4800 (сноска: «Installed memory is actually DDR5-5600 but runs as DDR5-4800»), два слота;
  - SSD: 512 ГБ 2242; «Two M.2 slots • One M.2 2242 • One M.2 2280»;
  - питание: **«No Power Adapter»**;
  - порты: 2× USB-C **5 Гбит/с**, HDMI 2.1, microSD; USB4 и RJ45 нет.
  Корпус тот же, что у 16AKP10: 356,5 × 250,6 × 16,9 мм, 1,85 кг.
- Icecat ([open](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Lenovo&ProductCode=83HU004KGE)): «2 x 16 GB», **«AC-Netzadapter: Nein»** — зарядки нет, подтверждено двумя источниками.
- CPU: Rembrandt-R, 660M (как у 21MW00AYGE).
- Цена: 776,90 € — technik-brandenburg.de (срок возврата не указан, доставка до 05.10); 799 € expert.de (14 дн.), expert-technomarkt, boomstore; 5 предложений. Минимум 699 € (20.05.2026).
- Итог: 776,90 + SSD 120,99 + зарядка 22,03 = **919,92 €**, диск 1,5 ТБ. С SSD PCIe 4.0 (UD90) — 937,90 €.
- Вердикт: **C, итог исправлен** (было 941,82). Самый дешёвый путь к 2×16 + 1 ТБ у Lenovo, но порты USB-C только 5 Гбит/с.

#### ThinkBook 16 G7 ARP — 21MW009MGE (EAN 199271442500)
- PSREF ([страница](https://psref.lenovo.com/Detail/ThinkBook/ThinkBook_16_G7_ARP?M=21MW009MGE), [PDF](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=21MW009MGE&country_code=)): R5 7535HS; 2×16 DDR5-4800; **512 ГБ**, 2× M.2 2280 (второй — для самостоятельного расширения); 65 W. Icecat: «2 x 16 GB».
- Цена: 949,00 € — easynotebooks.de (14 дн.); 949,01 notebook.de; 11 предложений. Минимум 672,26 € (23.10.2025).
- Итог: 949 + 120,99 = **1069,99 €**. Это на 71 € дороже 21MW00AYGE (998,99 € с 1 ТБ) при том же CPU — смысл только в 1,5 ТБ.
- Вердикт: **C, итог исправлен** (было 1091,89).

#### ThinkBook 16 G9 AHP — 21UT004EGE (EAN 199273308026)
- PSREF ([страница](https://psref.lenovo.com/Detail/ThinkBook/ThinkBook_16_G9_AHP?M=21UT004EGE), [PDF](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=21UT004EGE&country_code=)): R5 220; 2×16 DDR5-5600; 512 ГБ 2242 + свободный 2280; 400 нит; 65 W. Icecat: «2 x 16 GB».
- Цена: 949,00 € — Galaxus, маркетплейс (продавец HEINZSOFT), 30 дней; 981,23 € eBay. Купонные 898,90 € (technikdeals24 / heinzsoft) не в минимум. Минимум 889 € (26.09.2026).
- Итог: 949 + 120,99 = **1069,99 €**; дешевле 21UT004QGE (1072 €) на 2 € и с 1,5 ТБ, но CPU тот же урезанный.
- Вердикт: **C, итог исправлен** (было 1091,89).

#### ThinkBook 16 G6 ABP — 21KK007TGE (EAN 198153791187) — был «наблюдать», теперь в бюджете
- PSREF ([страница](https://psref.lenovo.com/Detail/ThinkBook/ThinkBook_16_G6_ABP?M=21KK007TGE), [PDF](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=21KK007TGE&country_code=)): R5 7430U; «1x 16GB SO-DIMM DDR4-3200», два слота; 512 ГБ; «Two M.2 2280 PCIe 3.0 x4 slots»; 65 W. Icecat ([open](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Lenovo&ProductCode=21KK007TGE)): «1 x 16 GB», «2x SO-DIMM».
- Цена: 849,00 € — easynotebooks.de (14 дн.); 849,01 notebook.de. Минимум 647,97 € (14.03.2026).
- Итог: 849 + DDR4 16 ГБ 113,17 + SSD 120,99 = **1083,16 €** — два условия сразу (планка и SSD).
- CPU: Barcelo-R, 6 ядер Zen 3, Vega 7, VCN 2.2 (без AV1), DDR4 — ловушка. Второй M.2 — см. противоречие NBC у 21KK0074GE.
- Вердикт: **исправлено: ≤ 1100 € (B16 + C)**. Не рекомендую из-за CPU.

### Дороже 1100 € — наблюдать (перепроверено)

| MTM | Модель, CPU | Память (PSREF PDF) | Сейчас, € (магазин) | Мин. 1 год | ≤ 1100 из 182 · последний | Итог | Что изменилось |
|---|---|---|---|---|---|---|---|
| [21M50027GE](https://www.idealo.de/preisvergleich/OffersOfProduct/208145677_-thinkpad-e16-g2-21m50027ge-lenovo.html) | E16 Gen 2, R5 7535HS | 1×16 DDR5-4800, 2 слота; 1 ТБ; 2 M.2 ([PDF](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=21M50027GE&country_code=)) | 1103,90 kaufland МП (PCSpezialistBonn), 14 дн.; 1208 techpointonline | 727 (04.12.2025) | 180 · 30.09 | ≥ 1103,90 + планка ≈ 1300 | подтверждено |
| [21M5002VGE](https://www.idealo.de/preisvergleich/OffersOfProduct/204203152_-thinkpad-e16-g2-21m5002vge-lenovo.html) | E16 Gen 2, R5 7535HS | 2×16, 1 ТБ, 2 M.2 ([PDF](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=21M5002VGE&country_code=)) | 1260,32 Amazon МП (TechPoint1111) | 789,90 (17.11.2025) | 161 · 08.09 | 1260,32 | подтверждено |
| [21M5002DGE](https://www.idealo.de/preisvergleich/OffersOfProduct/208145740_-thinkpad-e16-g2-21m5002dge-lenovo.html) | E16 Gen 2, R7 7735HS · 680M | 2×16, 1 ТБ, 2 M.2 ([PDF](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=21M5002DGE&country_code=)) | 1199,00 electronic4you.de (1 предл.) | 949 (24.11.2025) | 96 · 17.08 | 1199 | **исправлено: карточка есть** (найдена через «Variante» у 21M5002AGE) |
| [21MW001FGE](https://www.idealo.de/preisvergleich/OffersOfProduct/204282285_-thinkbook-16-g7-21mw001fge-lenovo.html) | TB16 G7, R7 7735HS | 2×16, 1 ТБ ([PDF](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=21MW001FGE&country_code=)) | 1333,01 techpointonline.de (1 предл.) | 550 (15.03.2026, выброс) | 121 · 15.09 | 1333,01 | подтверждено |
| [21Y4006CGE](https://www.idealo.de/preisvergleich/OffersOfProduct/210690958_-thinkpad-e16-g4-21y4006cge-lenovo.html) | E16 Gen 4, AI 5 330 (1 Zen 5 + 3 Zen 5c, 820M 2 CU — ловушка) | 2×16 DDR5-5600, 1 ТБ, 2 M.2 ([PDF](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=21Y4006CGE&country_code=)) | 1325,81 klarsicht-it.de | 929 (10.08.2026) | 2 из 120 · 11.08 | 1325,81 | подтверждено |
| [21UT000RGE](https://www.idealo.de/preisvergleich/OffersOfProduct/209122441_-thinkbook-16-g9-21ut000rge-lenovo.html) | TB16 G9, R7 250 = 8840U · 780M | 2×16, 1 ТБ ([PDF](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=21UT000RGE&country_code=)) | 1188,97 joybuy.de (30 дн.) / Amazon МП | 1045 (21.01.2026) | 0 | 1188,97 | подтверждено; NBC 29.05.2026 — 1153,61 € у office-partner (не idealo) |
| [21Y40068GE](https://www.idealo.de/preisvergleich/OffersOfProduct/210690957_-thinkpad-e16-g4-21y40068ge-lenovo.html) | E16 Gen 4, AI 5 330 | 2×16, **512 ГБ** + 2280 ([PDF](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=21Y40068GE&country_code=)) | 1086,21 Amazon МП (TechPoint1111) | 1045,85 (27.08.2026) | 7 из 120 · 30.09 | C: **1207,20** | итог исправлен (было 1229,10) |
| [21UT000KGE](https://www.idealo.de/preisvergleich/OffersOfProduct/209910744_-thinkbook-16-g9-21ut000kge-lenovo.html) | TB16 G9, R7 250 | 2×16, 512 ГБ + 2280 ([PDF](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=21UT000KGE&country_code=)) | **1252,90** notebookstore.de (14 дн.) | 1097,70 (01.07.2026) | 1 из 145 · 01.07 | C: **1373,89** | цена исправлена (было 1246) |
| [21XC002BGE](https://www.idealo.de/preisvergleich/OffersOfProduct/210622077_-thinkpad-l16-g3-21xc002bge-lenovo.html) | L16 Gen 3, AI 7 445 (6 ядер) | 2×16, 1 ТБ, **один** M.2 ([PDF](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=21XC002BGE&country_code=)) | 1675,97 klarsicht-it.de; 1171,23 buyzoxs — условная | 1171,23 (29.09, условная) | 0 | 1675,97 | подтверждено |
| [21SC002AGE](https://www.idealo.de/preisvergleich/OffersOfProduct/207096778_-thinkpad-l16-g2-21sc002age-lenovo.html) | L16 Gen 2, R5 PRO 215 · 740M | 2×16, 1 ТБ, один M.2 ([PDF](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=21SC002AGE&country_code=)) | 1231,81 klarsicht-it.de | 982,35 (23.10.2025) | 1 · 16.04 | 1231,81 | подтверждено |
| [83UM002BGE](https://www.idealo.de/preisvergleich/OffersOfProduct/210991837_-ideapad-5a-2-in-1-15-83um002bge-lenovo.html) | IdeaPad 5 2-in-1 15AGP11, AI 7 445 | 2×16, 1 ТБ, 2 M.2, **без БП** ([PDF](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=83UM002BGE&country_code=)) | 1274,06 computeruniverse / cyberport / galaxus (30 дн.) | 1234,88 (25.08.2026) | 0 | 1296,09 | подтверждено |
| [83HY0061GE](https://www.idealo.de/preisvergleich/OffersOfProduct/207280344_-ideapad-slim-5-16-83hy0061ge-lenovo.html) | Slim 5 16AKP10, AI 5 340 · 840M | 2×16, 1 ТБ + 2280 ([PDF](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=83HY0061GE&country_code=)) | новых нет, 1 предложение б/у | 776,15 (17.06.2026) | 180 · 25.09 | — | подтверждено; ждать нового |
| [21RH0013GE](https://www.idealo.de/preisvergleich/OffersOfProduct/207718331_-thinkpad-l16-g2-21rh0013ge-lenovo.html) | L16 Gen 2, AI 7 PRO 350 | 2×16, 1 ТБ, один M.2 ([PDF](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=21RH0013GE&country_code=)) | 1397,85 klarsicht-it.de | 1226 (10.11.2025) | 0 | 1397,85 | +5 € к записанному |
| [21SC0028GE](https://www.idealo.de/preisvergleich/OffersOfProduct/207096780_-thinkpad-l16-g2-21sc0028ge-lenovo.html) | L16 Gen 2, R7 PRO 250 | 2×16, 1 ТБ, один M.2 ([PDF](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=21SC0028GE&country_code=)) | 1410,28 klarsicht-it.de | 998,32 (23.10.2025) | 0 | 1410,28 | +5 € |
| [21Y4006NGE](https://www.idealo.de/preisvergleich/OffersOfProduct/210690963_-thinkpad-e16-g4-21y4006nge-lenovo.html) | E16 Gen 4, AI 7 345 (6 ядер) | 2×16, 1 ТБ ([PDF](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=21Y4006NGE&country_code=)) | 1424,81 klarsicht-it.de | 1169 (10.08.2026) | 0 | 1424,81 | подтверждено |
| [21Y4005QGE](https://www.idealo.de/preisvergleich/OffersOfProduct/211717421_-thinkpad-e16-g4-21y4005qge-lenovo.html) | E16 Gen 4, AI 7 445 (6 ядер) | 2×16, 1 ТБ ([PDF](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=21Y4005QGE&country_code=)) | 1551,81 klarsicht-it.de | 1259 (10.08.2026) | 0 | 1551,81 | подтверждено |
| [21XC002DGE](https://www.idealo.de/preisvergleich/OffersOfProduct/210622079_-thinkpad-l16-g3-21xc002dge-lenovo.html) | L16 Gen 3, AI 5 430 (4 ядра) | 2×16, 1 ТБ, один M.2 ([PDF](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=21XC002DGE&country_code=)) | 1541,90 notebookstore.de | 1400,92 (01.07.2026) | 0 | 1541,90 | +12 € |
| [21QN005KGE](https://www.idealo.de/preisvergleich/OffersOfProduct/206751404_-thinkpad-t16-g4-21qn005kge-lenovo.html) | T16 Gen 4, AI 7 PRO 350 | 2×16, 1 ТБ, один M.2, 100 W ([PDF](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=21QN005KGE&country_code=)) | 2058,76 klarsicht-it.de | 1559 (10.08.2026) | 0 | 2058,76 | +10 € |
| [21QR005BGE](https://www.idealo.de/preisvergleich/OffersOfProduct/209704276_-thinkpad-p16s-g4-21qr005bge-lenovo.html) | P16s Gen 4, AI 7 PRO 350 | 2×16, 512 ГБ, **один** M.2 → C невозможен ([PDF](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=21QR005BGE&country_code=)) | 1605,90 notebookstore.de | 1295,43 (13.08.2026) | 0 | — | +7 € |

### B — распайка 32 ГБ (перепроверено)

| MTM | Модель, CPU | Память (PSREF PDF) | Сейчас, € | БП | Итог | Что изменилось |
|---|---|---|---|---|---|---|
| [83TF003WGE](https://www.idealo.de/preisvergleich/OffersOfProduct/211633784_-yoga-7a-16-83tf003wge-lenovo.html) | Yoga 7 2-in-1 16AGP11, AI 7 445 | «32GB Soldered LPDDR5X-8000», один M.2 2242 ([PDF](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=83TF003WGE&country_code=)) | 1549,01 lenovo.com | **нет** | **1571,04** | исправлено: без БП |
| [83SJ000TGE](https://www.idealo.de/preisvergleich/OffersOfProduct/210046407_-ideapad-pro-5a-16-83sj000tge-lenovo.html) | IdeaPad Pro 5 16AGP11, AI 9 465 · 880M | 32 ГБ LPDDR5X-8533 распайка, 2 M.2 ([PDF](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=83SJ000TGE&country_code=)) | 1599,00 coolblue.de (30 дн.) | **нет** | **1621,03** | исправлено: без БП |
| [83JN0013GE](https://www.idealo.de/preisvergleich/OffersOfProduct/206526087_-ideapad-pro-5-16-83jn0013ge-lenovo.html) | IdeaPad Pro 5 16AKP10, AI 7 350 | 32 ГБ LPDDR5X-8000 распайка ([PDF](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=83JN0013GE&country_code=)) | 1599,00 Amazon МП (REBERION), 1 предл. | 100 W ✅ | 1599,00 | подтверждено |
| [83J3008LGE](https://www.idealo.de/preisvergleich/OffersOfProduct/211964640_-ideapad-slim-5-15-83j3008lge-lenovo.html) | IdeaPad Slim 5 15ARP10, R7 7735HS | 32 ГБ LPDDR5X-6400 распайка, 512 ГБ, 2× M.2 2280 ([PDF](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=83J3008LGE&country_code=)) | 1299,00 lenovo.com | **нет** | 1299 + SSD 120,99 + БП 22,03 = **1442,02** | исправлено: без БП, итог с SSD |
| [21K7003FGE](https://www.idealo.de/preisvergleich/OffersOfProduct/204386397_-thinkpad-t16-g2-21k7003fge-lenovo.html) | T16 Gen 2, R7 PRO 7840U | 32 ГБ LPDDR5X-6400 распайка ([PDF](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=21K7003FGE&country_code=)) | 2539,82 techpointonline.de | 65 W ✅ | 2539,82 | подтверждено |

### Отброшенные — выборочная проверка

| MTM | Причина у агента | Проверка (PSREF PDF, idealo 30.09) | Итог |
|---|---|---|---|
| 21ST004GGE, 21ST001YGE (E16 Gen 3) | 1×32 | «1x 32GB SODIMM DDR5-5600», два слота ([PDF 004G](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=21ST004GGE&country_code=), [PDF 001Y](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=21ST001YGE&country_code=)); 1156,99 nullprozentshop ([карточка](https://www.idealo.de/preisvergleich/OffersOfProduct/207096771_-thinkpad-e16-g3-21st004gge-lenovo.html)) / 1199,64 klarsicht ([карточка](https://www.idealo.de/preisvergleich/OffersOfProduct/206556600_-thinkpad-e16-g3-21st001yge-lenovo.html)) | отброшен верно. «Превратить» в 2×16 можно только заменой 1×32 → дороже 1100 |
| 83UU001LGE (V15 G6 ARP) | один M.2 → C невозможен | «One M.2 2280 PCIe 4.0 x4 slot», 2×16 DDR5-4800, 15,6" FHD, R5 150 ([PDF](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=83UU001LGE&country_code=)); **789,95** galaxus.de, 30 дн. ([карточка](https://www.idealo.de/preisvergleich/OffersOfProduct/209094412_-v15-g6-83uu001lge-lenovo.html)); «759 € aitek» сейчас нет | отброшен верно по критерию C. Замена SSD 512 → 1 ТБ = 910,94 € — вне критериев, но это самый дешёвый путь к «2×16 + 1 ТБ» у Lenovo. Решать пользователю |
| 83KU0012GE (IdeaPad 5 2-in-1 16AKP10) | 16 распайки без слота | «16GB Soldered LPDDR5X-7500», «no slots», «not upgradable» ([PDF](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=83KU0012GE&country_code=)) | верно |
| 83K800GQGE (Slim 3 16ARP10) | один слот | «1x 16GB SODIMM», «One DDR5 SODIMM slot», «Up to 16GB» ([PDF](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=83K800GQGE&country_code=)) | верно |
| 21MW001WGE (TB16 G7, 1×16/512) | с планкой и SSD 1290 | 898,97 easynotebooks ([карточка](https://www.idealo.de/preisvergleich/OffersOfProduct/204414902_-thinkbook-16-g7-21mw001wge-lenovo.html)) + DDR5 ≥ 199,90 + SSD 120,99 ≥ 1219,86 | верно, дороже 1100 |
| 21UT0041GE (TB16 G9, 1×16/512) | с планкой и SSD 1340 | 949,00 easynotebooks ([карточка](https://www.idealo.de/preisvergleich/OffersOfProduct/209122446_-thinkbook-16-g9-21ut0041ge-lenovo.html)) + ≥ 199,90 + 120,99 ≥ 1269,89 | верно |

### Опровергнуто / исправлено

1. SSD для C: 142,89 € (NV3) → **120,99 €** (Verbatim Vi3000, NVMe PCIe 3.0, M.2 2280, NBB). Итоги: 83HU004KGE 941,82 → **919,92**; 21MW009MGE и 21UT004EGE 1091,89 → **1069,99**; 21Y40068GE 1229,10 → 1207,20; 21UT000KGE → 1373,89.
2. 21KK007TGE: «1105,06 — на 5 € выше» → **1083,16 € — в бюджете** (B16 + C). Лист: watch → B16.
3. 21UT004QGE: 1073,00 → **1072,00 €** (easynotebooks / c-nw).
4. 21UT000KGE: 1246 → **1252,90 €**.
5. 21M5002DGE: «на idealo не найден» → карточка [208145740](https://www.idealo.de/preisvergleich/OffersOfProduct/208145740_-thinkpad-e16-g2-21m5002dge-lenovo.html), 1199 €. Поиск по MTM и EAN её не находит — только блок «Variante» соседних 21M5….
6. Без блока питания (PSREF): 83TF003WGE, 83SJ000TGE, 83J3008LGE — итоги +22,03 € (у агента не учтено).
7. 83UU001LGE: «ab 759 aitek» → сейчас 789,95 € (galaxus).
8. L16 G2/G3, T16 G4, P16s G4, 21RH0013GE, 21SC0028GE: цены на 5–12 € выше записанных — на вердикт не влияет.
9. Подтверждено без изменений: раскладка памяти у всех 33 SKU; второй M.2 у всех A/C; зарядка в комплекте у всех A и у 21MW009MGE / 21UT004EGE; отсутствие БП у 83HU004KGE (PSREF + Icecat).

### Известные проблемы (Notebookcheck)

- **IdeaPad Slim 5 16AKP10** — тот же корпус, что у 83HY008CGE и 83HU004KGE (PSREF: 356,5 × 250,6 × 16,9 мм). Тест конфигурации AI 5 330 / 2×8, 21.11.2025 ([NBC](https://www.notebookcheck.net/Dual-debut-in-the-Lenovo-IdeaPad-Slim-5-16-Ryzen-AI-5-330-and-Radeon-820M-in-review.1166676.0.html)):
  - экран LEN160WUM: **57,6 % sRGB**, ~1060:1, ΔE 5,57, PWM нет;
  - шум под нагрузкой 42 дБ(A), PL1 25–36 Вт;
  - вскрытие: 6 винтов Torx, 2 SO-DIMM, «The 2280 slot is free»;
  - минусы: «weak speakers», «small colour gamut», «high latencies»; плюсы — металлический корпус, низкие температуры, автономность.
- **ThinkBook 16 G6 ABP** (7530U), 85,7 %, 28.11.2023 ([NBC](https://www.notebookcheck.net/Lenovo-ThinkBook-16-G6-review-The-inexpensive-multimedia-laptop-with-a-Ryzen-7000.774481.0.html)):
  - экран: **59,8 % sRGB** («unsuitable for picture editing»), PWM нет, ореолы по краям;
  - шум: 41,4 дБ(A) в стресс-тесте;
  - минусы: «no USB 4.0», «low color space coverage». У тестового экземпляра один M.2-2280 (см. 21KK0074GE).
  Корпус того же семейства, что у G7 ARP и G9 AHP: PSREF 356 × 253,5 × 17,5 мм у всех трёх.
- **ThinkBook 16 G7 ARP** — собственного теста NBC нет, только сборник внешних обзоров ([NBC](https://www.notebookcheck.net/Lenovo-ThinkBook-16-G7-ARP.1187767.0.html), 17.12.2025): минусы «Battery only 45Wh», «60Hz display panel»; heise — 75 % («Ryzen 5 & USB4 für 582 Euro»).
- **ThinkBook 16 G9 AHP** — теста нет: NBC 29.05.2026 — «Es musste sich noch kein G9-Modell des ThinkBook 16 einem unserer Tests stellen» ([NBC](https://www.notebookcheck.com/Lenovo-ThinkBook-16-G9-mit-Ryzen-7-Zen-4-32-GB-RAM-1-TB-SSD-im-Angebot.1310427.0.html)). Там же для 21UT000RGE — «2x 16 GB, DDR5-5600, zwei Slots», «zweite SSD». Ближайший тест — G6 ABP.
- **ThinkPad E16 Gen 2 AMD** — тест именно **21M5002VGE**, 83,8 %, 11.10.2024 ([NBC](https://www.notebookcheck.net/Lenovo-ThinkPad-E16-Gen-2-AMD-laptop-review-Cuts-corners-mostly-in-the-right-places.899320.0.html)):
  - экран: 58,2 % sRGB, PWM нет;
  - нагрузка: 36,3 дБ(A), троттлинга нет;
  - плюсы: «free SSD slot»; минусы: «poor display scores», «no USB4».
- **IdeaPad Slim 5 16ARP10** (83HU004KGE) — отдельного теста не нашёл; ближайший — 16AKP10 выше (тот же корпус).

### Что не проверено

- Срок возврата у cyclotron.de (21MW007VGE), electronic4you.de (21KK0074GE, 21M5002DGE), technik-brandenburg.de (83HU004KGE), siliconpowereu.com, computeruniverse.net (зарядка) — idealo его не показывает.
- Второй M.2 у ThinkBook 16 G6 ABP: PSREF — два, тестовый образец NBC — один. Для 21KK007TGE (C) проверить при получении.
- HEVC на практике (DXVA Checker) — ни на одном SKU; есть только отсутствие оговорок в PSREF.
- DDR4-3200 16 ГБ дешевле 113,17 € не искал: фильтр idealo по DDR4 SO-DIMM 16 ГБ не подобрал, цена — с карточки G.Skill.
