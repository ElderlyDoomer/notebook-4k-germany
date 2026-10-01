# Кандидаты AMD: прочие бренды (ASUS, Acer, MSI, Medion, Gigabyte, Tuxedo, XMG, Framework, CSL/Captiva/TERRA)

_30.09.2026, локальная сессия. Цены — idealo.de в Chrome пользователя (своя вкладка), история — API idealo `period=1Y` (с ~14:30 API отвечал 404 на все товары — у части SKU история «не проверено»). Раскладка памяти — asus.com techspec / Icecat open. Tuxedo и Framework — конфигураторы производителей (на idealo их нет). Итог = минимальная цена нового у любого продавца (решение пользователя в `MEMORY.md`), в скобках — только обычные магазины._
_Критерии и ловушки — `../CLAUDE.md`; исходные зацепки — `market-amd.md`, `brands-amd.md`, `hevc-amd.md`, `amd-cpu.md`. Планка DDR5-5600 16 ГБ — см. раздел «Планка»._

## Лучшие находки

**Заводских 2×16 SO-DIMM с 1 ТБ за ≤ 1100 € в этой группе нет** (A-список пуст). Всё, что проходит, — либо «докупить», либо распайка.

| # | SKU (P/N) | CPU · iGPU | Память (даташит) | Цена idealo → итог | Список | Главный минус |
|---|---|---|---|---|---|---|
| 1 | ASUS Vivobook S16 `M3607HA-RP017W` | R7 260, Hawk Point (Zen 4, 8 ядер) · 780M | 16 распайка + **пустой SO-DIMM** (Icecat, asus.com) | 819,00 € expert.de → **1006,56 €** с планкой (1067,89 € в обычных магазинах); за год минимум 699,96 € | B-список (16+16) | USB только 5 Гбит/с, 45 % NTSC, один M.2; возврат 14 дн. |
| 2 | ASUS Vivobook 16 `M1607GA-MB020W` | Ryzen AI 7 445, Gorgon Point (Zen 5, 6 ядер) · 840M | 16 распайка + пустой SO-DIMM | 806,99 € → **994,55 €** (1056,88 €) | B-список (16+16) | 6 ядер, USB 5 Гбит/с, 45 % NTSC |
| 3 | ASUS ExpertBook P1 `PM1503CDA-S70264X` | R5 150, **Rembrandt (Zen 3+)** · 660M | **1×16 SO-DIMM + свободный слот** (серия asus.com: 2×8 нет) | 620,06 € → **950,51 €** с планкой и SSD 1 ТБ (1026,88 €) | условный C (планка + SSD) | старый CPU и слабая iGPU, HDMI 1.4, 45 % NTSC |
| 4 | ASUS ExpertBook P1 `PM1503CDA-S70262` | R7 170, Rembrandt · 680M | 1×16 + слот (по серии) | 730,54 € (eBay МП) → **1060,99 €** (1127,67 €) | условный C | то же, дороже |
| 5 | Acer Aspire 16 AI `NX.JLLEG.009` (A16-61M-R8T1) | Ryzen AI 7 350, Krackan (Zen 5, 8 ядер) · 860M | 32 LPDDR5X распайка | **1080,25 €** easynotebooks.de; за год минимум 886,36 € | B-список (распайка) | HEVC-риск Acer; сегодня — годовой максимум цены |
| 6 | Acer Aspire 16 AI OLED `NX.JP0EG.00Z` (A16-61M-R2R1) | Ryzen AI 7 350 · 860M | 32 LPDDR5X распайка | **1081,21 €** computeruniverse.net | B-список (распайка) | HEVC-риск; карточка idealo смешана с 16/512 |

Вывод по группе: лучший баланс — **Vivobook S16 M3607HA** (8 ядер Zen 4 + 780M, после планки двухканал 16+16), самый дешёвый — **ExpertBook P1 PM1503CDA-S70264X**, но у него CPU 2022 года. Против лучшего Lenovo из `market-amd.md` (ThinkBook 16 G9 AHP `21UT004QGE`, 2×16 с завода, ~1067 €) ни один SKU этой группы не выигрывает явно.

## Списки

| Список | SKU |
|---|---|
| A — 2×16 SO-DIMM с завода, ≤ 1100 € | **нет** |
| B16 — 1×16 SO-DIMM + слот + планка, 1 ТБ, ≤ 1100 € | **нет подтверждённых**; `BM1503CDA-S72123` (909,99 € МП + 187,56 = 1097,55 €) — раскладка SKU не подтверждена |
| C — условный (докупить SSD 1 ТБ; здесь ещё и планку) | `PM1503CDA-S70264X` 950,51 €, `PM1503CDA-S70262` 1060,99 €; `BM1503CDA-S71654` / `-S71655` (989,07 / 1015,14 €) — только если 1×16, не подтверждено |
| B — распайка (16 распайка + 16 SO-DIMM или 32 распайка) | `M1607GA-MB020W` 994,55 €, `M3607HA-RP017W` 1006,56 €, Acer `NX.JLLEG.009` 1080,25 €, Acer `NX.JP0EG.00Z` 1081,21 € |
| Наблюдать (> 1100 €) | `M1607KA-MB187W` (949 € → 1136,56 €; в бюджете при ≤ 912 €), Vivobook S16 `M3607GA-SH004W` (AI 7 445, 32 = 16+16, 1249–1369 €), Acer Swift Air 16 `NX.DL5EG.001` (1149 €) |
| Отброшено | см. «Отброшено» в разделах брендов: AI 5 330 (M1607KA-MB172W, Swift Air R1FY, PM3606CKA), 8 распайки/максимум 24 (M1605NAQ), 16 распайки без слота (Aspire 16 AI 16 ГБ, Swift Air R6R8), 2×8 (MSI Venture A16), Barcelo/Lucienne/Mendocino (Aspire Go/Lite/3, Extensa, Medion Avantum 15 E1, TERRA, CSL), выше потолка (Tuxedo, XMG, Framework, Captiva, ExpertBook P3/P5 G2, Zenbook S16) |

## Карточки SKU

### Докупка: планка и SSD (idealo, 30.09.2026)

По `MEMORY.md` (ответ пользователя): магазин не важен, маркетплейсы подходят, **цена = минимальная цена нового товара у любого продавца**. Поэтому итог считаю по минимуму, а в скобках — вариант «только обычный магазин».

| Докупка | Минимум (любой продавец) | Обычный магазин | Ссылка |
|---|---|---|---|
| Планка DDR5-5600 16 ГБ SO-DIMM | **187,56 €** Kingston `KVR56S46BS8-16`, Galaxus (маркетплейс), возврат 30 дн., одно предложение | 248,89 € Crucial `CT16G56C46S5`, alza.de, 30 дн. (за 3 мес. минимум 178,90 € — 03.07) | [Kingston](https://www.idealo.de/preisvergleich/OffersOfProduct/213624753_-valueram-16gb-ddr5-5600mhz-cl46-so-dimm-on-die-ecc-kvr56s46bs8-16-kingston.html), [Crucial](https://www.idealo.de/preisvergleich/OffersOfProduct/202284828_-16gb-ddr5-5600-cl46-ct16g56c46s5-crucial.html) |
| SSD 1 ТБ NVMe M.2 2280 PCIe 4.0 | **142,89 €** Kingston NV3 1 ТБ, alternate.de, 14 дн. | то же | [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/204697967_-nv3-1tb-kingston.html) |
| (для сравнения) Crucial P310 1 ТБ 2280 | 173,00 € eBay (МП) | 174,89 € alza.de | [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/204799641_-p310-1tb-2280-crucial.html) |

ASUS не отказывает в гарантии только из-за установленных сторонних деталей (текст гарантии на странице [asus.com M1607](https://www.asus.com/de/laptops/for-home/vivobook/asus-vivobook-16-m1607/techspec/)); повреждения от неправильной установки — не гарантийные.

### ASUS

#### ASUS Vivobook 16 M1607GA — `M1607GA-MB020W` · 806,99 € + планка = **994,55 €** (обычные магазины: 1056,88 €) · B-список (16 распайка + 16 SO-DIMM)

| Поле | Значение | Источник |
|---|---|---|
| CPU | Ryzen AI 7 445 — Gorgon Point (Zen 5, 6 ядер), Radeon 840M | Icecat; idealo «Prozessor Codename Gorgon Point» |
| Память | **16 ГБ DDR5 распаяно + 1 слот SO-DIMM (пустой)**, максимум 32 ГБ. Двухканал — только с планкой в слоте | [Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=ASUS&ProductCode=M1607GA-MB020W): «Memory Formfaktor: On-board + SO-DIMM», «1x SO-DIMM», 16 ГБ, «max. 32 GB»; [asus.com/de M1607](https://www.asus.com/de/laptops/for-home/vivobook/asus-vivobook-16-m1607/techspec/): у серии единственный вариант «16GB DDR5 on board», «1x DDR5 SO-DIMM slot», «*Dual-channel memory support requires at least one SO-DIMM module» |
| SSD | 1 ТБ PCIe 4.0, **один** M.2 2280 | Icecat; asus.com |
| Экран | 16" WUXGA IPS 300 нит, 45 % NTSC | Icecat; asus.com |
| Порты | 2× USB-C 5 Гбит/с (DP, зарядка), 2× USB-A 5 Гбит/с, HDMI 2.1 (TMDS); USB4 нет | asus.com |
| Вес / батарея / БП | 1,88 кг · 70 Втч · 68 Вт в комплекте | Icecat |
| ОС | Windows 11 Home | Icecat |
| HEVC | нет данных об отключении у ASUS (см. `hevc-amd.md` §5); проверить DXVA Checker в срок возврата | — |
| Цена | **807,99 €** notebooksbilliger.de (обычный магазин, возврат 30 дн.); 806,99 € nullprozentshop.de (тот же «Shop aus Sarstedt»). 2 предложения | [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/209172185_-vivobook-16-m1607ga-mb020w-asus.html), 30.09.2026 |
| История (1 год) | карточка с 22.01.2026; всё время 799 € (min = max) | API idealo |
| Итог | 806,99 + 187,56 (Kingston) = **994,55 €**; только обычные магазины: 807,99 (NBB) + 248,89 (Crucial) = 1056,88 € | расчёт |

#### ASUS Vivobook S16 M3607HA — `M3607HA-RP017W` · 819,00 € + планка = **1006,56 €** (обычные магазины: 1067,89 €) · B-список (16 распайка + 16 SO-DIMM)

| Поле | Значение | Источник |
|---|---|---|
| CPU | Ryzen 7 260 — Hawk Point (Zen 4, 8 ядер), Radeon 780M | Icecat; [amd.com](https://www.amd.com/en/products/processors/laptop/ryzen/200-series/amd-ryzen-7-260.html) (см. `market-amd.md` §5) |
| Память | **16 ГБ DDR5 распаяно + 1 слот SO-DIMM (пустой)**, максимум 32 ГБ | [Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=ASUS&ProductCode=M3607HA-RP017W): «On-board + SO-DIMM», «1x SO-DIMM», 16 ГБ, max 32; [asus.com/de M3607](https://www.asus.com/de/laptops/for-home/vivobook/asus-vivobook-s16-m3607/techspec/): варианты «16GB DDR5 on board» и «16GB on board + 16GB SO-DIMM», «1x DDR5 SO-DIMM slot» |
| SSD | 1 ТБ PCIe 4.0, один M.2 2280 | Icecat; asus.com |
| Экран | 16" WUXGA 300 нит, 45 % NTSC, глянец | Icecat; asus.com |
| Порты | 2× USB-C 5 Гбит/с, 2× USB-A 5 Гбит/с, HDMI 2.1 (TMDS); кардридера нет | asus.com; Icecat |
| Вес / батарея / БП | 1,7 кг · 70 Втч · 65 Вт | Icecat |
| HEVC | нет данных (ASUS) | `hevc-amd.md` |
| Цена | **819,00 €** expert.de (обычный магазин, возврат 14 дн.); kaufland.de 831,18 € (МП), eBay 839,99 € (МП), otto МП 859,99 €. 4 предложения | [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/206751394_-vivobook-s16-m3607ha-rp017w-asus.html), 30.09.2026 |
| История (1 год) | 361 точка с 30.09.2025; **минимум 699,96 € (26.08.2026)**, максимум 860,02 €; все 182 последних дня ≤ 1100 € | API idealo |
| Итог | 819,00 + 187,56 = **1006,56 €**; обычные магазины: 819,00 + 248,89 = 1067,89 € | расчёт |

#### ASUS Vivobook 16 M1607KA — `M1607KA-MB172W` (90NB15F2-M00BJ0) · 799 € · **отброшен: Ryzen AI 5 330**

- Память: 16 ГБ распаяно + 1 слот, max 32 ([Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=ASUS&ProductCode=90NB15F2-M00BJ0)); 70 Втч, 1,89 кг.
- CPU: **Ryzen AI 5 330** — 4 ядра, 820M (Icecat и название предложения; спор из `market-amd.md` закрыт — не AI 7 350). По `amd-cpu.md` §8 урезанный, не брать.
- Цена: 799,00 € — только electronic4you.de (предоплата, срок возврата idealo не показывает); с 04.06.2026 минимум 742,50 € (22.06) — [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/210698249_-vivobook-16-m1607ka-mb172w-asus.html). С планкой 986,56 € (Kingston) / 1047,89 € (Crucial).

#### ASUS Vivobook 16 M1607KA — `M1607KA-MB187W` (90NB15F1-M00C70) · 949 € + планка = 1136,56 € · **выше потолка**

- Ryzen AI 7 350 (Krackan), 16 ГБ «On-board» + 1 слот SO-DIMM, max 32 ([Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=ASUS&ProductCode=90NB15F1-M00C70)).
- 949,00 € electronic4you.de (1 обычный магазин), galaxus.de 1487,33 €; минимум с 04.06 — 890,10 € (22.06) → даже тогда с Kingston 1077,66 € (в бюджете только при такой цене) — [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/210697864_-vivobook-16-m1607ka-mb187w-asus.html). Наблюдать: сработает при цене ≤ 912 €.

#### Отброшено по ASUS (коротко)

| SKU | Почему | Источник |
|---|---|---|
| Vivobook 16 OLED `M1605NAQ-MB007W` (R7 170, 629 €), `-MB226W` (649 €), `-MB029W` (R5 150, 679 €) | у серии M1605 только «8GB DDR5 on board» + 1 слот, **максимум 24 ГБ** — 32 ГБ невозможно; CPU Rembrandt (Zen 3+) | [asus.com M1605](https://www.asus.com/de/laptops/for-home/vivobook/asus-vivobook-16-oled-m1605/techspec/); idealo [MB007W](https://www.idealo.de/preisvergleich/OffersOfProduct/210612660.html), [MB226W](https://www.idealo.de/preisvergleich/OffersOfProduct/213088511.html), [MB029W](https://www.idealo.de/preisvergleich/OffersOfProduct/208996010.html) |
| ExpertBook B1 `BM1503CDA-S72123` (90NX0821-M02BX0), R7 170, 16/1 ТБ | только маркетплейсы (otto МП 909,99 €, Galaxus МП 919,99 €); по серии 16 ГБ = 1×16 или 2×8, по SKU не проверено (Icecat: нет); при 1×16 итог 909,99 + 187,56 = **1097,55 €** — впритык, но раскладка SKU не подтверждена; CPU Rembrandt (Zen 3+). См. ExpertBook ниже | [asus.com BM1503](https://www.asus.com/de/laptops/for-work/expertbook/asus-expertbook-bm1-bm1503/techspec/); [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/213397785.html) |
| ExpertBook P3 `PM3606CKA-MB0196X`, AI 5 330, 16/1 ТБ, 959 € (цена из выдачи) | у серии 16 ГБ = «16GB DDR5 SO-DIMM» (1×16) + 2 слота, но 959 + 187,56 = 1146,56 € и AI 5 330 (4 ядра) | [asus.com PM3606](https://www.asus.com/de/laptops/for-work/expertbook/asus-expertbook-p3-pm3606/techspec/); [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/208508328.html) |

#### ASUS ExpertBook P1 PM1503CDA — `PM1503CDA-S70264X` (90NX09D1-M00A70) · 620,06 € + планка + SSD = **950,51 €** · условный (1×16 + слот, SSD 512 ГБ → докупить 1 ТБ)

| Поле | Значение | Источник |
|---|---|---|
| CPU | Ryzen 5 150 — **Rembrandt (Zen 3+, 2022)**, 6 ядер, Radeon 660M (RDNA 2, maintenance mode с 10.2025) | `amd-cpu.md` §1; [amd.com R5 150](https://www.amd.com/en/products/processors/laptop/ryzen/100-series/amd-ryzen-5-150.html) |
| Память | **16 ГБ = одна планка SO-DIMM, второй слот свободен**, до 64 ГБ. Серия PM1503 на asus.com знает только конфигурации «8GB SO-DIMM», «16GB DDR5 SO-DIMM», «16GB DDR5 SO-DIMM x 2», «32GB SO-DIMM» — варианта 2×8 нет; по SKU Icecat: «Memory Formfaktor: SO-DIMM», «2x SO-DIMM», max 64 | [asus.com PM1503](https://www.asus.com/de/laptops/for-work/expertbook/asus-expertbook-p1-pm1503/techspec/); [Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=ASUS&ProductCode=90NX09D1-M00A70) |
| SSD | 512 ГБ M.2 2280 PCIe 4.0; слоты: **M.2 2280 + M.2 2230** (оба PCIe 4.0 x4). ASUS: ставить M.2 «under professional supervision, which may void your warranty» | asus.com |
| Экран | 15,6" FHD 300 нит, **45 % NTSC** | asus.com; Icecat |
| Порты | 2× USB-C 10 Гбит/с, 2× USB-A 5 Гбит/с, RJ45, **HDMI 1.4 (4K только 30 Гц)**; USB4 нет | asus.com |
| Вес / батарея | 1,6 кг (asus.com; Icecat — 1,81 кг) · 50 Втч (у серии есть и 63 Втч) · 65 Вт | asus.com; Icecat |
| ОС | без ОС (предложения «ohne OS»/«ohne Windows»; Icecat пишет Win 11 Pro) | idealo; Icecat |
| HEVC | нет данных об отключении у ASUS; VCN 3.1 (Rembrandt) декодирует HEVC 4:2:0/AV1 | `hevc-amd.md`, `amd-cpu.md` |
| Гарантия | у ExpertBook B1 NBC пишет «3-year warranty» (`brands-amd.md`); для P1 — не проверено | — |
| Цена | **620,06 €** xtreme.metacomp.de (срок возврата idealo не показывает); jacob.de 635,09 €; jb-computer.de 635,10 € (30 дн.); easynotebooks.de 635,13 € (14 дн.) | [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/209457310_-expertbook-p1-pm1503cda-s70264x-asus.html), 30.09.2026 |
| История | **не проверено**: API idealo 30.09 днём отвечал 404 (как в `idealo-howto.md`) | — |
| Итог | 620,06 + 187,56 (планка) + 142,89 (SSD 1 ТБ) = **950,51 €**; только обычные магазины: 635,10 + 248,89 + 142,89 = 1026,88 € | расчёт |

#### ASUS ExpertBook P1 PM1503CDA — `PM1503CDA-S70262` · R7 170 · 730,54 € + планка + SSD = **1060,99 €** · условный

- Та же платформа PM1503, но Ryzen 7 170 (Rembrandt, 8 ядер, **Radeon 680M** — вдвое больше CU, чем 660M). Раскладка — как у серии (16 ГБ = 1×16, см. выше); SKU в Icecat нет — P/N по SKU не проверен.
- Цена: **730,54 €** eBay (МП, 30 дн.); serverhero.de 735,88 €; playox.de 735,89 € (30 дн.); office-partner.de 735,90 €; computeruniverse.net 742,89 € (30 дн.) — [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/209457306_-expertbook-p1-pm1503cda-s70262-asus.html). История — не проверено (API 404).
- Итог: 730,54 + 187,56 + 142,89 = **1060,99 €**; только обычные магазины: 735,89 + 248,89 + 142,89 = 1127,67 € (выше потолка).

#### ASUS ExpertBook B1 BM1503CDA — `-S71654` (R5 150) / `-S71655` (R7 170) · 658,62 / 684,69 € · раскладка не подтверждена

- Та же платформа (2× SO-DIMM, M.2 2280 + 2230, HDMI 1.4, RJ45), но у серии BM1503 есть и **«8GB DDR5 SO-DIMM x 2»** — 16 ГБ может быть 2×8 ([asus.com BM1503](https://www.asus.com/de/laptops/for-work/expertbook/asus-expertbook-bm1-bm1503/techspec/)). Icecat по SKU ([S71654 90NX0821-M01U80](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=ASUS&ProductCode=90NX0821-M01U80), [S71655 90NX0821-M01U90](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=ASUS&ProductCode=90NX0821-M01U90)): «SO-DIMM», «2x SO-DIMM», 63 Втч, 1,61 кг, без ОС — **сколько планок, не сказано**.
- Цены: S71654 — 658,62 € eBay (МП), 664,41 € serverhero.de, 664,42 € playox.de — [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/209425539_-expertbook-b1-bm1503cda-s71654-asus.html); S71655 — 684,69 € playox.de (30 дн.), 685,70 € computeruniverse/cyberport — [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/209405016_-expertbook-b1-bm1503cda-s71655-asus.html).
- Если 1×16: S71654 → 658,62 + 187,56 + 142,89 = 989,07 €; S71655 → 684,69 + 187,56 + 142,89 = 1015,14 €. Если 2×8 — нужен комплект 2×16 (≈ 475 €) → > 1100 €. **Не брать, пока раскладка не подтверждена** (у P1 PM1503 она подтверждена серией, и P1 дешевле).
- Другие B1 с 16/512: `-S71656X` (R5 150, 699 €), `-S71657X` (R7 170, 738 €), `-S70590X` (R5 7535U, 699 €) — [поиск](https://www.idealo.de/preisvergleich/ProductCategory/3751.html?q=ExpertBook%20AMD%20Ryzen&sortKey=minPrice); дороже S71654/S71655 при той же неизвестной раскладке.

### Acer

HEVC у Acer в Германии — **повышенный риск**: с 06.2026 часть устройств идёт «ohne HEVC-Codec», модели не названы (`hevc-amd.md` §5, [ChannelPartner](https://www.channelpartner.de/article/4187748/acer-und-asus-liefern-wieder.html)). Проверить DXVA Checker в срок возврата. Сервис-мануалов у Acer нет ([`brands.md`](../../Intel/notes/brands.md)).
Скан idealo (фильтр Acer `471878`, 15–16", 30.09.2026): [32 ГБ + 1 ТБ](https://www.idealo.de/preisvergleich/ProductCategory/3751F471878-699493-1568565-2682401-7612877.html?sortKey=minPrice) — 8 AMD-карточек; [16 ГБ + 1 ТБ](https://www.idealo.de/preisvergleich/ProductCategory/3751F471878-699493-1568565-2682401-7612874.html?sortKey=minPrice) — 8; [32 ГБ + 512 ГБ](https://www.idealo.de/preisvergleich/ProductCategory/3751F471878-699493-1568565-2682416-7612877.html?sortKey=minPrice) — 0 AMD.

#### Acer Aspire 16 AI A16-61M-R8T1 — `NX.JLLEG.009` · **1080,25 €** · B-список (32 ГБ распайка)

| Поле | Значение | Источник |
|---|---|---|
| CPU | Ryzen AI 7 350 — Krackan Point (Zen 5, 8 ядер), Radeon 860M | Icecat; [amd.com](https://www.amd.com/en/products/processors/laptop/ryzen/ai-300-series/amd-ryzen-ai-7-350.html) |
| Память | **32 ГБ LPDDR5X распаяно** («Memory Formfaktor: On-board», максимум 32 ГБ) — навсегда 32, двухканал есть | [Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Acer&ProductCode=NX.JLLEG.009) |
| SSD | 1 ТБ (по названию у office-lieferant — QLC, `market-amd.md`; не проверено) | Icecat |
| Экран | 16" WUXGA 120 Гц, 350 нит (охват в Icecat — «NTSC», % не указан) | Icecat; `market-amd.md` |
| Порты | **2× USB4**, кардридер | Icecat |
| Вес / батарея / БП | 1,55 кг · 65 Втч · 100 Вт | Icecat |
| HEVC | **риск (Acer)** | `hevc-amd.md` |
| Цена | **1080,25 €** easynotebooks.de (возврат 14 дн.) и technikdirekt.de; notebook.de 1080,26 €; jacob.de 1087,73 €; euronics МП 1104,95 € | [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/208031586_-aspire-16-ai-a16-61m-r8t1-acer.html), 30.09.2026 |
| История (1 год) | 353 точки с 13.10.2025; **минимум 886,36 € (01.07.2026)**; сегодняшняя цена = годовой максимум | API idealo |
| Итог | **1080,25 €** (докупать нечего) | — |

#### Acer Aspire 16 AI OLED A16-61M-R2R1 — `NX.JP0EG.00Z` · **1081,21 €** · B-список (32 ГБ распайка, OLED)

- Память: 32 ГБ LPDDR5X on-board, max 32; OLED 16" WUXGA DCI-P3 300 нит; 2× USB4; кардридер; 65 Втч; 1,55 кг; БП 100 Вт — [Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Acer&ProductCode=NX.JP0EG.00Z).
- **Ловушка карточки idealo:** «ab 794,83 €» — это чужие конфигурации 16 ГБ / 512 ГБ / AI 5 330 (`A16-61M-R5H7`, NX.JP0EG.010) у computeruniverse, cyberport, e-tec, Galaxus. Настоящий R2R1 (AI 7 350, 32/1 ТБ) — **1081,21 €** у computeruniverse.net (возврат 30 дн.) — [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/211631508_-aspire-16-ai-a16-61m-r2r1-acer.html). История карточки из-за смеси конфигураций не показательна.
- По сравнению с R8T1: +0,96 €, зато OLED с DCI-P3 (для цветокоррекции лучше), но 60 Гц/ШИМ — не проверено. HEVC — риск (Acer).

#### Acer Swift Air 16 SFA16-61M-R1FY — `NX.DL5EG.002` · 999 € · **отброшен: Ryzen AI 5 330**

- 32 ГБ LPDDR5 распайка, OLED DCI-P3, HDMI 1.4, 50 Втч, 1,1 кг, 2 года гарантии — [Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Acer&ProductCode=NX.DL5EG.002).
- 999,00 € expert.de (возврат 14 дн.), kaufland МП 999,00 €; минимум 950 € (27.09.2026), карточка с 09.07 — [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/211778543_-swift-air-16-oled-16-wuxga-amd-ryzen-ai-5-32gb-1tb-ssd-silber-nx-dl5eg-002-acer.html).
- CPU AI 5 330 — 4 ядра, 820M: для 4K слабый (`amd-cpu.md` §8).

#### Отброшено по Acer (коротко)

| SKU / линейка | Цена idealo 30.09 | Почему | Ссылка |
|---|---|---|---|
| Swift Air 16 `SFA16-61M-R559` (NX.DL5EG.001), AI 7 350, 32 распайка | 1149 € | выше потолка — наблюдать | [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/209373389.html) |
| Swift Go 16 AI `SFG16-61-R1WP` / `-R6QV`, AI 7 350, LPDDR5X распайка | 1278 / 1299 € | выше потолка | [R1WP](https://www.idealo.de/preisvergleich/OffersOfProduct/206775817.html), [R6QV](https://www.idealo.de/preisvergleich/OffersOfProduct/206349046.html) |
| Aspire 16 AI `A16-61M-R583`, AI 7 350, 32 ГБ | только б/у | нет новых предложений (минимум нового — 899 € в 12.2025) | [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/207875978.html) |
| Aspire 16 AI `A16-61M-R014` (899 €), `-R87H` (934 €), `A16-61` NX.JP0EG.009 (AI 5 340, 949 €) | 899–949 € | **16 ГБ распайки, максимум 16** (Icecat [NX.JP0EG.009](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Acer&ProductCode=NX.JP0EG.009): «On-board», max 16) | [R014](https://www.idealo.de/preisvergleich/OffersOfProduct/207965885.html), [R87H](https://www.idealo.de/preisvergleich/OffersOfProduct/212350121.html), [JP0EG.009](https://www.idealo.de/preisvergleich/OffersOfProduct/207234482.html) |
| Swift Air 16 `SFA16-61M-R6R8`, AI 7 350, 16 ГБ | 993,07 € | 16 ГБ LPDDR5 распайки | [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/208703820.html) |
| Aspire 15 `A15-61M-R86V`, R7 8840HS, 16 ГБ | 999 € | даже при свободном слоте 999 + 249 = 1248 € (раскладка не проверена) | [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/206524308.html) |
| Aspire Go 15 `AG15-42P-R3HH` / `-R5ZD`, R7 5825U, 32 ГБ | 699 / 729 € | **Barcelo (Zen 3, Vega)** — CPU-ловушка; R5ZD — 1 продавец на маркетплейсе | [R3HH](https://www.idealo.de/preisvergleich/OffersOfProduct/211709177.html), [R5ZD](https://www.idealo.de/preisvergleich/OffersOfProduct/208529022.html) |
| Aspire Lite 15 `AL15-45P-R15P` (5825U), `AL15-46P-R0HV` (5300U), Aspire 3 `A315-44P-R0TB` (5700U), Aspire 3 `A315-24P` (7520U), Aspire Go 15 `AG15-21P` (7320U) | 349–639 € | Barcelo / Lucienne (Zen 2) / Mendocino (Zen 2, максимум 16 ГБ) — CPU-ловушки | [AL15-45P](https://www.idealo.de/preisvergleich/OffersOfProduct/213318926.html), [AL15-46P](https://www.idealo.de/preisvergleich/OffersOfProduct/211794981.html), [A315-44P](https://www.idealo.de/preisvergleich/OffersOfProduct/205007917.html); [поиск «Aspire 5 Ryzen»](https://www.idealo.de/preisvergleich/ProductCategory/3751.html?q=Aspire%205%20Ryzen&sortKey=minPrice) |
| Extensa 15 AMD (R5 7430U / R7 7730U) | карточки вида `T-DEV00703-32-T1-WO` | **Barcelo-R** + конфигурации продавца (32/64 ГБ, 1–8 ТБ) вместо заводских SKU | [поиск «Extensa Ryzen»](https://www.idealo.de/preisvergleich/ProductCategory/3751.html?q=Extensa%20Ryzen&sortKey=minPrice) |
| TravelMate AMD 15–16" | — | в выдаче «TravelMate Ryzen» только 14" TMP414-42 и Intel-модели (TMP215/216) → **в DE нет подходящих SKU** | [поиск](https://www.idealo.de/preisvergleich/ProductCategory/3751.html?q=TravelMate%20Ryzen&sortKey=minPrice) |
| Aspire 5 AMD | — | в выдаче «Aspire 5 Ryzen» AMD-моделей Aspire 5 нет (A515-56 — Intel) → **нет SKU** | [поиск](https://www.idealo.de/preisvergleich/ProductCategory/3751.html?q=Aspire%205%20Ryzen&sortKey=minPrice) |

### MSI

Скан idealo (фильтр MSI `471897`, 15–16", 30.09.2026): [1 ТБ](https://www.idealo.de/preisvergleich/ProductCategory/3751F471897-699493-1568565-2682401.html?sortKey=minPrice) — самый дешёвый AMD **1359 €** (VenturePro A16 AI A3HW, AI 7 350, 16 ГБ); [512 ГБ](https://www.idealo.de/preisvergleich/ProductCategory/3751F471897-699493-1568565-2682416.html?sortKey=minPrice) — 2 AMD.

| SKU | Цена idealo 30.09 | Память (источник) | Вывод |
|---|---|---|---|
| Venture A16 AI+ `A3HMG-036DE`, AI 5 340, 16 ГБ, 512 ГБ | 859 € — [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/206751211.html) | **2×8** DDR5-5600 в 2 SO-DIMM, до 96 ГБ ([Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&GTIN=4711377358880)) | reject: менять обе планки (комплект 2×16 ≈ 475 €) + SSD → > 1100 € |
| VenturePro A16 AI `A3HW` / `A3HWEG-003` / `-002`, AI 7 350, 16 ГБ, 1 ТБ | 1359 / 1359 / 1449 € — [A3HW](https://www.idealo.de/preisvergleich/OffersOfProduct/206751226.html) | не проверял (цена уже выше потолка) | выше потолка |
| Thin A15 `B7VF-410`, R7 7735HS + RTX 4060 | 999 € — [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/206324439.html) | — | вне группы (дискретка; RTX 40 без 4:2:2), 512 ГБ, 16 ГБ |
| Modern 15 B7M (AMD) | — | — | на idealo нет: поиск «MSI Modern 15 B7M» даёт только Intel (F13/B12/H AI) — [поиск](https://www.idealo.de/preisvergleich/ProductCategory/3751.html?q=MSI%20Modern%2015%20B7M&sortKey=minPrice) → **в DE нет SKU** |
| Cyborg A15 AI, Prestige A16 AI+ | 1499–1539 € | — | выше потолка / дискретка |

### Medion

Скан idealo (фильтр Medion `471895`, 15–16", 1 ТБ): [выдача](https://www.idealo.de/preisvergleich/ProductCategory/3751F471895-699493-1568565-2682401.html?sortKey=minPrice) — AMD только Avantum 15 E1 и Erazer Beast 16 X1 (RTX, от 2899 €). Поиск [«Medion Ryzen»](https://www.idealo.de/preisvergleich/ProductCategory/3751.html?q=Medion%20Ryzen&sortKey=minPrice): остальное — 17" (Avantum 17), старые E15xxx или Intel (SPRCHRGD 16 S1 = Core Ultra 5 228V — [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/207195506.html)).

| SKU | Цена | Память | Вывод |
|---|---|---|---|
| Avantum 15 E1 `30039298`, R5 7430U, 15,6" FHD, 1 ТБ | 719,99 € kaufland.de (**маркетплейс**, 14 дн.), otto МП 739,99 €; минимум за год 503,36 € (23.10.2025) — [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/205551625.html) | **2×16 DDR4** («Speicherlayout 2 x 16 GB», [Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&GTIN=4061275237580)); idealo в фильтре пишет 16 ГБ — ошибка, в предложении 32 ГБ | **reject: Barcelo-R** (Zen 3, Vega, VCN 2.2 — нет AV1-декода), HDMI 1.4, только маркетплейсы |

### Gigabyte

Скан idealo (фильтр GigaByte `510253`, 15–16", любые ОЗУ/SSD): [выдача](https://www.idealo.de/preisvergleich/ProductCategory/3751F510253-699493-1568565.html?sortKey=minPrice) — все 6 AMD-карточек с RTX: Eagle `GL6J` / `9MJR2DEF93SH` (R5 7533HS + RTX 4050, 999 €), Gaming A16 `3VHK3DE894SH` (R7 260 + RTX 5060, 1099 €), `3WHK3DE894SH` (RTX 5070, 1399 €), Aero X16 (AI 7 350 + RTX 5060, от 1439 €). → **Gigabyte на AMD без дискретки в DE нет.** Gaming A16 — в группе GPU (`market-amd.md` §3).

### Tuxedo (конфигуратор tuxedocomputers.com, 30.09.2026; на idealo нет)

| Модель | База | 2×16 + 1 ТБ + без Windows | Вывод |
|---|---|---|---|
| InfinityBook Pro 15 Gen10 AMD | **1374,00 €**: 15,3" 2560×1600 до 300 Гц 500 нит, Ryzen 7 H 255 («lagernd ab 30.10.2026»), 16 ГБ (2×8) DDR5-5600, 500 ГБ WD SN5100, TUXEDO OS, «ohne Windows», 2 года гарантии | 1374 + 230 (32 ГБ 2×16 Crucial) + 55 (1 ТБ SN5100) = **1659,00 €**; Ryzen AI 7 350 — ещё +100 € | 2 слота SO-DIMM и 2 M.2 — хорошо, но **выше потолка на 559 €** — [конфигуратор](https://www.tuxedocomputers.com/de/TUXEDO-InfinityBook-Pro-15-Gen10-AMD.tuxedo#configurator) |
| InfinityBook Max 15 Gen10 AMD | **1894,00 €**: AI 7 350 + RTX 5060, 2×8, 500 ГБ | 1894 + 230 + 55 = **2179,00 €** | дискретка, вне бюджета — [конфигуратор](https://www.tuxedocomputers.com/de/TUXEDO-InfinityBook-Max-15-Gen10-AMD.tuxedo#configurator) |

Цены конфигуратора — с сайта производителя (idealo Tuxedo не ведёт; правило «только idealo» здесь неприменимо — как и требовала задача).

### XMG / Schenker

idealo, поиск [«XMG Ryzen»](https://www.idealo.de/preisvergleich/ProductCategory/3751.html?q=XMG%20Ryzen&sortKey=minPrice): EVO 15 (2025, AI 7 350, 860M, 32 ГБ) — ab **1489 €** ([карточка серии](https://www.idealo.de/preisvergleich/OffersOfProduct/207795301.html)), `E25HHN` — 1639 € ([idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/207795383.html)); Core 15/16 (2025) — от 2129 €; EVO 14 — 14". → **в бюджете нет**; раскладку EVO 15 не проверял (цена уже выше потолка).

### Framework Laptop 16 (DIY)

Конфигуратор [frame.work](https://frame.work/de/de/products/laptop16-diy-amd-ai300): DIY Edition AI 300 — «Est. Price» **1409,00 €** за базу (Ryzen AI 5 340, pre-order), 7040 Series — ab 1459 €. Память и SSD докупаются сверху: + 2×16 (от 2×187,56 € по idealo) + SSD 1 ТБ 142,89 € → **≈ 1927 €**. → вне бюджета.

### CSL, Captiva, TERRA (Wortmann)

| SKU | CPU | Цена idealo 30.09 | Вывод |
|---|---|---|---|
| CSL R'Evolve C15 `90610` / `90614` (32 ГБ), `90626` (64 ГБ), `90574` (8 ГБ) | R5 5500U — **Lucienne (Zen 2)** | 709 / 715,26 / 759 / 519 € — [поиск «CSL Ryzen»](https://www.idealo.de/preisvergleich/ProductCategory/3751.html?q=CSL%20Ryzen&sortKey=minPrice), [90610](https://www.idealo.de/preisvergleich/OffersOfProduct/203893407.html) | reject: Zen 2, Vega; сборки продавца |
| Captiva Business/Office R10-15.3 (`R10-1359GE`) | Ryzen 7 255 (Hawk Point-H, Zen 4, 780M) | **987,98 €** nexoc-store.de: 16 ГБ, 500 ГБ, без ОС, **без блока питания** — [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/210052443_-business-office-r10-15-3-captiva.html) | reject: + планка 187,56 + SSD 142,89 + зарядка → > 1300 €; раскладка 16 ГБ не проверена |
| Captiva Power Starter R97-15.3 / R94-15.3 | Ryzen 7 255 | 1000,27 / 987,98 € — [R97](https://www.idealo.de/preisvergleich/OffersOfProduct/208652669.html) | то же — выше потолка после докупок |
| TERRA MOBILE 1610 `1220869`, 1610A `1220868` (16 ГБ) | R7 7730U — **Barcelo-R** | 680 / 706 € — [поиск](https://www.idealo.de/preisvergleich/ProductCategory/3751.html?q=TERRA%20MOBILE%20Ryzen&sortKey=minPrice), [1220869](https://www.idealo.de/preisvergleich/OffersOfProduct/209516962.html) | reject: CPU-ловушка |
| TERRA MOBILE 1500P `1220818` / `1220819` (16 ГБ) | R5 7430U — **Barcelo-R** | 713,45 / 748,04 € — [1220818](https://www.idealo.de/preisvergleich/OffersOfProduct/205828453.html) | reject: CPU-ловушка |


## Линейки без подходящих SKU (где искал)

| Линейка | Результат | Где искал |
|---|---|---|
| ASUS Vivobook 15 M1502 / M1505, Vivobook 16 M1605 | серия: 8 ГБ распайки + 1 слот, максимум 16–24 ГБ → 32 ГБ невозможно | [asus.com M1605](https://www.asus.com/de/laptops/for-home/vivobook/asus-vivobook-16-oled-m1605/techspec/), [M1502](https://www.asus.com/Laptops/For-Home/Vivobook/vivobook-15-m1502/techspec/), [M1505](https://www.asus.com/Laptops/For-Home/Vivobook/ASUS-Vivobook-15-OLED-M1505/techspec/) (`brands-amd.md`) |
| ASUS Vivobook 16 M1606 | такой AMD-серии в выдачах idealo ASUS 15–16" (16 и 32 ГБ) нет — есть M1605 и M1607 | [idealo ASUS 16 ГБ/1 ТБ](https://www.idealo.de/preisvergleich/ProductCategory/3751F471881-699493-1568565-2682401-7612874.html?sortKey=minPrice), [32 ГБ/1 ТБ](https://www.idealo.de/preisvergleich/ProductCategory/3751F471881-699493-1568565-2682401-7612877.html?sortKey=minPrice) |
| ASUS ExpertBook P3 G2 / B3 G2 16 AMD | на idealo SKU нет; P3 PM3606 AI 7 350 16/1 ТБ — 1411,99 €, P5 G2 AI 7 445 — от 1296,47 € | [поиск «ExpertBook AMD Ryzen»](https://www.idealo.de/preisvergleich/ProductCategory/3751.html?q=ExpertBook%20AMD%20Ryzen&sortKey=minPrice), [PM3606CKA-MB0012X](https://www.idealo.de/preisvergleich/OffersOfProduct/211455115.html), [P5 G2](https://www.idealo.de/preisvergleich/OffersOfProduct/213769869.html) |
| ASUS ExpertBook 32/1 ТБ (P1 PM1503CDA-S70254X, B1 32 ГБ) | от 1189,99 € | [idealo ASUS 32/1 ТБ](https://www.idealo.de/preisvergleich/ProductCategory/3751F471881-699493-1568565-2682401-7612877.html?sortKey=minPrice) |
| ASUS Zenbook S16 / ProArt P16 (распайка) | Zenbook S16 UM5606GA от 1694,96 €; ProArt в выдаче 32/1 ТБ до 1800 € нет | там же |
| ASUS 32 ГБ + 512 ГБ (условный вариант) | только `BM1503CDA-S72123` 32/512 — 1069,99 € (конфигурация продавца) → с SSD > 1100 € | [idealo](https://www.idealo.de/preisvergleich/ProductCategory/3751F471881-699493-1568565-2682416-7612877.html?sortKey=minPrice) |
| Acer TravelMate AMD 15–16" | в DE нет (в выдаче только 14" TMP414-42 и Intel) | [поиск](https://www.idealo.de/preisvergleich/ProductCategory/3751.html?q=TravelMate%20Ryzen&sortKey=minPrice) |
| Acer Aspire 5 AMD | в DE нет | [поиск](https://www.idealo.de/preisvergleich/ProductCategory/3751.html?q=Aspire%205%20Ryzen&sortKey=minPrice) |
| Acer Aspire Go 15/16, Aspire Lite/3, Extensa 15 AMD | только Barcelo/Lucienne/Mendocino | раздел Acer |
| Acer Swift Go 16 AMD | от 1278 € | раздел Acer |
| Acer 32 ГБ + 512 ГБ | AMD-карточек нет | [idealo](https://www.idealo.de/preisvergleich/ProductCategory/3751F471878-699493-1568565-2682416-7612877.html?sortKey=minPrice) |
| MSI Modern 15 B7M | на idealo нет | раздел MSI |
| MSI Venture/VenturePro A16 | 2×8 (859 €) или от 1359 € | раздел MSI |
| Medion (кроме Avantum 15 E1) | AMD 15–16" без дискретки нет; SPRCHRGD 16 S1 — Intel | раздел Medion |
| Gigabyte без RTX | нет | раздел Gigabyte |
| Tuxedo IBP 15 Gen10 AMD / Max 15 AMD | 1659 € / 2179 € в нужной конфигурации | конфигуратор |
| XMG EVO/Core AMD | от 1489 € | idealo |
| Framework 16 | ≈ 1927 € с 2×16 и 1 ТБ | frame.work |
| CSL / Captiva / TERRA | Zen 2 / Barcelo-R или > 1100 € после докупок | раздел CSL/Captiva/TERRA |

## Что не проверено

- История цен idealo для ExpertBook P1/B1, M1607GA (повтор), Captiva, XMG — API 30.09 после ~14:30 отвечал 404 на все товары. billiger.de для `PM1503CDA-S70264X`: сейчас 635,10–773,49 €, 10 предложений ([billiger](https://www.billiger.de/pricelist/5538462139-asus-expertbook-p1-15-6-amd-ryzen-5-150-16-gb-ram-512-gb-ssd-ohne-betriebssystem)) — это срез, не история.
- Раскладка ExpertBook B1 `BM1503CDA-S71654/-S71655/-S72123` по SKU (1×16 или 2×8): Icecat пишет только «2x SO-DIMM»; SKU-даташита ASUS не нашёл.
- `PM1503CDA-S70262` в Icecat нет — раскладка только по серии.
- HEVC у ASUS на AMD — «нет данных» (отключений не найдено); у Acer — риск. Проверять DXVA Checker в срок возврата.
- Срок возврата xtreme.metacomp.de, serverhero.de, electronic4you.de — idealo не показывает.
