## Проверка other-brands

_30.09.2026, локальная сессия, скептическая проверка шорт-листа [`candidates-other-brands.md`](candidates-other-brands.md). Память — Icecat open по каждому P/N + asus.com techspec (DE и глобальная версия); CPU — [amd-cpu.md](amd-cpu.md); HEVC — [hevc-amd.md](hevc-amd.md); цены — idealo.de в Chrome пользователя (своя вкладка), история — API idealo `period=1Y` (30.09 днём отвечал 200). Правило цены — корневой `../../CLAUDE.md`: минимум нового у любого продавца, маркетплейсы включительно; условные цены («Preis inkl. Gutschein») не считаются._
_Статус: готово (30.09.2026, ~14:30)._

### Вывод

1. **Все шесть SKU шорт-листа устояли — ни один не выпал**, но в двух ExpertBook P1 исправлен расчёт:
   - **второй M.2 у P1 PM1503 — формата 2230**, а посчитанная NV3 1 ТБ — 2280, туда она не встанет. Итог 950,51 € у `S70264X` держится только как **замена** 512 ГБ на 1 ТБ. Добавить 1 ТБ 2230 — 1034,82 €;
   - `S70262`: 730,54 € — цена с купоном («Preis inkl. Gutschein»). Без условий — 735,88 €, итог **1066,33 €**.
2. **Раскладка P1 теперь подтверждена даташитами ASUS на каждый P/N** (агент поиска опирался на серию): у `S70264X` и `S70262` — «16GB DDR5 (16GB DDR5 SO-DIMM)» + 2 слота. Для сравнения, у B1 `BM1503CDA-S71655` даташит ASUS пишет «2x 8GB». Heise на PM1503 тоже видел одну планку Samsung и свободный слот.
3. Vivobook `M3607HA-RP017W` и `M1607GA-MB020W` — 16 распайки + пустой SO-DIMM (Icecat по P/N, глобальные страницы ASUS). Ссылки агента на `asus.com/de` этих CPU не содержат.
4. **Лучший в группе по-прежнему `M3607HA-RP017W`**: Ryzen 7 260 (8 ядер Zen 4, 780M), 144 Гц, итог 1006,56 €. У `M1607GA` AI 7 445 — урезанный (6 ядер, 840M).
5. Acer `R8T1` и `R2R1` — 32 ГБ LPDDR5X-8533 распайки (Icecat), 1080,25 / 1081,21 €. У R8T1 21–29.09 было 995 €. acer.com не открылся ни в curl, ни в Chrome.
6. Отброшенные проверены выборочно: `BM1503CDA-S71655` — даташит ASUS подтвердил **2×8**, отброшен верно; `M1607KA-MB172W` — AI 5 330, 4 ядра, тоже верно.
7. **Планка за 187,56 € — одно предложение на маркетплейсе Galaxus**, неделю назад она стоила ~400 €. Запасной вариант — 206,80 € (+19,24 € к каждому итогу с планкой).

### Сводная таблица (idealo, 30.09.2026, цены с доставкой)

| P/N | CPU (кремний) | Память (даташит) | SSD / M.2 | Цена сейчас · магазин | Мин. 1 год | Итог | Вердикт |
|---|---|---|---|---|---|---|---|
| ASUS `M3607HA-RP017W` | R7 260 — Hawk Point, 8× Zen 4, 780M ✅ | 16 распайки + пустой SO-DIMM ✅ (Icecat, asus.com) | 1 ТБ, один M.2 2280 | **819,00 €** expert.de, 14 дн. — [206751394](https://www.idealo.de/preisvergleich/OffersOfProduct/206751394_-vivobook-s16-m3607ha-rp017w-asus.html) | 699,96 € (26.08.2026) | **1006,56 €** | ✅ confirmed · B (16+16) |
| ASUS `M1607GA-MB020W` | AI 7 445 — Gorgon Point, **6 ядер**, 840M ⚠️ | 16 распайки + пустой SO-DIMM ✅ (Icecat, asus.com) | 1 ТБ, один M.2 2280 | **806,99 €** nullprozentshop.de (NBB 807,99, 30 дн.) — [209172185](https://www.idealo.de/preisvergleich/OffersOfProduct/209172185_-vivobook-16-m1607ga-mb020w-asus.html) | 799 € (всё время; 81 день в продаже) | **994,55 €** | ✅ confirmed · B (16+16), CPU урезанный |
| ASUS `PM1503CDA-S70264X` | R5 150 — Rembrandt, 6× Zen 3+, 660M ⚠️ | **1×16 SO-DIMM + слот** ✅ (даташит ASUS по P/N) | 512 ГБ 2280 + **свободный 2230** | **620,06 €** xtreme.metacomp.de — [209457310](https://www.idealo.de/preisvergleich/OffersOfProduct/209457310_-expertbook-p1-pm1503cda-s70264x-asus.html) | 612,18 € (03.09.2026) | **950,51 €** (замена SSD) / 1034,82 € (+2230) | ✏️ исправлено · C (планка + SSD) |
| ASUS `PM1503CDA-S70262` | R7 170 — Rembrandt, 8× Zen 3+, 680M | **1×16 SO-DIMM + слот** ✅ (даташит ASUS по P/N) | 512 ГБ 2280 + свободный 2230 | **735,88 €** serverhero.de (730,54 — купон) — [209457306](https://www.idealo.de/preisvergleich/OffersOfProduct/209457306_-expertbook-p1-pm1503cda-s70262-asus.html) | 558,00 € (19.03.2026) | **1066,33 €** (замена SSD) / 1150,64 € (+2230) | ✏️ исправлено · C |
| Acer `NX.JLLEG.009` (R8T1) | AI 7 350 — Krackan, 8 ядер, 860M ✅ | 32 LPDDR5X-8533 распайки ✅ (Icecat) | 1 ТБ (вероятно QLC) | **1080,25 €** easynotebooks.de, 14 дн. — [208031586](https://www.idealo.de/preisvergleich/OffersOfProduct/208031586_-aspire-16-ai-a16-61m-r8t1-acer.html) | 886,36 € (01.07.2026); 995 € ещё 29.09 | **1080,25 €** | ✅ confirmed · B (распайка), риск HEVC (Acer) |
| Acer `NX.JP0EG.00Z` (R2R1, OLED) | AI 7 350 — Krackan, 860M ✅ | 32 LPDDR5X-8533 распайки ✅ (Icecat) | 1 ТБ | **1081,21 €** computeruniverse.net, 30 дн. — [211631508](https://www.idealo.de/preisvergleich/OffersOfProduct/211631508_-aspire-16-ai-a16-61m-r2r1-acer.html) (карточка смешана с R5H7) | не показательна | **1081,21 €** | ✅ confirmed · B (распайка), риск HEVC |

«Итог» — с планкой Kingston 187,56 € и, где нужно, SSD NV3 1 ТБ 142,89 € (замена). Все шесть — с блоком питания в комплекте (Icecat «AC-Netzadapter: Ja» / даташит ASUS «Power adapter 65W»). У R2R1 проверить у продавца: e-tec у соседнего R5H7 пишет «Netzteil separat erhältlich».

### Докупка (idealo, 30.09.2026)

| Что | Цена с доставкой | Магазин · возврат | Карточка |
|---|---|---|---|
| Планка DDR5-5600 16 ГБ SO-DIMM — Kingston `KVR56S46BS8-16` | **187,56 €** | Galaxus **Marktplatz** (продавец Avanturis), 30 дн.; **единственное предложение**; до 25.09 карточка стоила 396–426 € — цена скачет | [213624753](https://www.idealo.de/preisvergleich/OffersOfProduct/213624753_-valueram-16gb-ddr5-5600mhz-cl46-so-dimm-on-die-ecc-kvr56s46bs8-16-kingston.html) ✅ |
| Запасной вариант планки — Lenovo `4X71M23186` DDR5-5600 | 206,80 € | notebookkontor.de (из [verify-idealo-sweep.md](verify-idealo-sweep.md), 12:51) | [205464660](https://www.idealo.de/preisvergleich/OffersOfProduct/205464660_-thinkpad-16gb-ddr5-5600-4x71m23186-lenovo.html) |
| SSD 1 ТБ M.2 **2280** — Kingston NV3 | **142,89 €** | alternate.de, 14 дн.; x-kom 146,89; alza 147,89 (30 дн.) | [204697967](https://www.idealo.de/preisvergleich/OffersOfProduct/204697967_-nv3-1tb-kingston.html) ✅ |
| SSD 1 ТБ M.2 **2230** (для второго слота ExpertBook P1) — Silicon Power UD90 | **227,20 €** | kaufland.de МП, 14 дн.; siliconpowereu.com 229,97. Kingston NV3 2230 — от 230,85 € (reichelt) | [UD90](https://www.idealo.de/preisvergleich/OffersOfProduct/203279966_-ud90-1tb-m-2-2230-silicon-power.html), [NV3 2230](https://www.idealo.de/preisvergleich/OffersOfProduct/206803359_-nv3-1tb-2230-kingston.html) |

Если Kingston за 187,56 € исчезнет, у всех «+ планка» итог вырастет на ~19 € (Lenovo 206,80 €).

### По SKU

#### ASUS Vivobook S16 M3607HA — `M3607HA-RP017W` (90NB16F1-M00B30)
- **Память** ✅: [Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=ASUS&ProductCode=M3607HA-RP017W) — «Memory Formfaktor: On-board + SO-DIMM», «Speicherkartensteckplätze: 1x SO-DIMM», 16 ГБ DDR5, «RAM-Speicher maximal: 32 GB». [asus.com M3607 (глобальная)](https://www.asus.com/laptops/for-home/vivobook/asus-vivobook-s16-m3607/techspec/): варианты «16GB DDR5 on board» и «16GB DDR5 on board + 16GB DDR5 SO-DIMM», «1x DDR5 SO-DIMM slot», «1x M.2 2280 PCIe 4.0x4». Итог: 16 распайки + пустой слот → B-список (16+16).
- **Поправка к источнику:** немецкая страница [asus.com/de M3607](https://www.asus.com/de/laptops/for-home/vivobook/asus-vivobook-s16-m3607/techspec/), на которую ссылается агент поиска, **Ryzen 7 260 не содержит** (там только AI 7 350 / AI 5 330 / AI 7 445 — модели M3607KA/GA). M3607HA и Ryzen 7 260 есть только на глобальной странице.
- **CPU** ✅: Ryzen 7 260 — Hawk Point (= 8845HS), 8 ядер Zen 4, 780M (12 CU), 45 Вт (`amd-cpu.md`, строки 13, 145, 168). Не урезанный. Для 4K: HEVC/AV1 4:2:0 аппаратно, 4:2:2 — нет (как у всех AMD). 780M в двухканале — только после установки планки.
- **Экран — поправка:** Icecat: WUXGA IPS-level, 300 нит, **45 % NTSC, 144 Гц**, «Display-Oberfläche: Glanz». На глобальной странице ASUS все WUXGA-панели M3607 — «Anti-glare», 144 Гц. Про 144 Гц агент поиска не написал; «глянец» — только по Icecat, у ASUS — матовый (не проверено на живом образце).
- Порты (Icecat, asus.com): 2× USB-C 5 Гбит/с (DP, PD), 2× USB-A 5 Гбит/с, HDMI 2.1 (TMDS), без кардридера, без USB4. 70 Втч, 1,7 кг, «AC-Netzadapter: Ja», 65 Вт.
- **Цена** ✅ ([idealo 206751394](https://www.idealo.de/preisvergleich/OffersOfProduct/206751394_-vivobook-s16-m3607ha-rp017w-asus.html), «Daten vom 30.09.2026 13:01»): **819,00 €** expert.de (обычный магазин, возврат 14 дн., до 05.10); kaufland МП 831,18 (14 дн.); eBay МП 839,99 (30 дн.); otto МП 859,99 (30 дн.) — 4 предложения, все от сети expert.
- **История 1 год** ✅: 361 точка с 30.09.2025; минимум **699,96 € (26.08.2026)**, максимум 860,02 €, средняя 779,85 €; 182 из 182 последних дней ≤ 1100 €.
- **Итог:** 819,00 + 187,56 = **1006,56 €** ✅ (с Lenovo-планкой 1025,80 €).

#### ASUS Vivobook 16 M1607GA — `M1607GA-MB020W` (90NB16Z2-M00120)
- **Память** ✅: [Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=ASUS&ProductCode=M1607GA-MB020W) — «On-board + SO-DIMM», «1x SO-DIMM», 16 ГБ, max 32 ГБ. [asus.com M1607 (глобальная)](https://www.asus.com/laptops/for-home/vivobook/asus-vivobook-16-m1607/techspec/): «16GB DDR5 on board» (+ вариант «+ 16GB DDR5 SO-DIMM»), «1x DDR5 SO-DIMM slot», «*Dual-channel memory support requires at least one SO-DIMM module», один M.2 2280.
- **Поправка к источнику:** на немецкой странице [asus.com/de M1607](https://www.asus.com/de/laptops/for-home/vivobook/asus-vivobook-16-m1607/techspec/) есть только M1607KA (AI 7 350 / 5 340 / 5 330); **AI 7 445 (M1607GA) — только на глобальной.**
- **CPU** ⚠️: Ryzen AI 7 445 — Gorgon Point, **6 ядер (2 Zen 5 + 4 Zen 5c), 840M (4 CU)**, L3 8 МБ (Icecat: 6 ядер, 12 потоков, L3 8 MB; `amd-cpu.md` строки 180, 297: «6 ядер под именем "7"», ≈ AI 5 340). Урезанный — слабее Ryzen 7 260 и по CPU, и по iGPU (840M 1415 против 780M ~2800 в Time Spy, `amd-cpu.md` строки 209, 331). Для 4K — нижняя граница.
- Экран (Icecat): WUXGA IPS-level, 300 нит, 45 % NTSC, **60 Гц**, матовый. Порты: 2× USB-C 5G, 2× USB-A 5G, HDMI 2.1 TMDS. 70 Втч, **1,88 кг**, 68 Вт в комплекте («AC-Netzadapter: Ja»).
- **Цена** ✅ ([idealo 209172185](https://www.idealo.de/preisvergleich/OffersOfProduct/209172185_-vivobook-16-m1607ga-mb020w-asus.html), 30.09.2026): **806,99 €** nullprozentshop.de (срок возврата idealo не показывает; тот же «Shop aus Sarstedt», что NBB); notebooksbilliger.de 807,99 € (30 дн., до 02.10) — 2 предложения.
- **История — поправка:** карточка с 22.01.2026, **всего 81 точка за 252 дня** — в остальные дни предложений не было. «81 день ≤ 1100 € из 182» у агента поиска означает не «101 день дороже», а «101 день не было в продаже». Цена всё время 799 € (min = max).
- **Итог:** 806,99 + 187,56 = **994,55 €** ✅.

#### ASUS ExpertBook P1 PM1503CDA — `PM1503CDA-S70264X` (90NX09D1-M00A70)
- **Память** ✅ **по даташиту ASUS на этот P/N**: [ASUS-даташит S70264X (EN)](https://gzhls.at/blob/ldb/7/7/9/4/57187dc9af3bd89f8e8a348d096d24911e28.pdf) / [(DE)](https://gzhls.at/blob/ldb/1/0/1/a/db4b585f4f802984828fb01cd584e42bdc86.pdf) (EAN 4711636328364): «Memory: 16GB DDR5 (**16GB DDR5 SO-DIMM**) · 2x DDR5 SO-DIMM slots», «Storage: 512GB PCIe Gen4 M.2 SSD · 1x M.2 2230 PCIe 4.0x4», 65 Вт USB-C, 1,807 кг, **36 месяцев международной гарантии**. Для сравнения — даташит того же формата у B1 `BM1503CDA-S71655`: «16GB DDR5 (**2x 8GB** DDR5 SO-DIMM)» — ASUS явно различает 1×16 и 2×8. Независимо: [heise, 09.11.2025](https://www.heise.de/bestenlisten/testbericht/asus-expert-book-pm1-im-test-guenstiger-laptop-mit-ryzen-5-und-16-gb-ram-ueberzeugt/jqmdlcc) (PM1503, 7535HS, 16 ГБ): «16 GB DDR5-RAM als einzelnes SO-DIMM-Modul von Samsung mit 4800 MT/s. Der zweite RAM-Slot bleibt frei». Rembrandt работает с DDR5-4800 — планка 5600 пойдёт на 4800.
- Раньше (у агента поиска) — только по серии: [Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=ASUS&ProductCode=90NX09D1-M00A70) — «Memory Formfaktor: SO-DIMM», «2x SO-DIMM», 16 ГБ, max 64 (поля «Speicherlayout» нет). [asus.com PM1503 (глобальная)](https://www.asus.com/laptops/for-work/expertbook/asus-expertbook-p1-pm1503/techspec/) перечисляет «8GB DDR5 SO-DIMM», «16GB DDR5 SO-DIMM», «16GB DDR5 SO-DIMM x 2», «32GB DDR5 SO-DIMM» — **2×8 у P1 нет**, и ASUS пишет «x 2», когда планок две (у B1 BM1503 — «8GB DDR5 SO-DIMM x 2»). [asus.com/de PM1503](https://www.asus.com/de/laptops/for-work/expertbook/asus-expertbook-p1-pm1503/techspec/) — единственный вариант «16GB DDR5 SO-DIMM, Memory Max Up to:64GB». Значит 16 ГБ = 1×16 + свободный слот. На живом образце не проверено (CPU-Z → SPD).
- **SSD / второй M.2 — исправлено:** слоты «1x M.2 2280 PCIe 4.0x4» (занят 512 ГБ) и «1x M.2 **2230** PCIe 4.0x4» (свободен) — asus.com. **Kingston NV3 1 ТБ (2280), которую посчитал агент поиска, во второй слот не встанет.** Два пути:
  1. заменить 512 ГБ на NV3 1 ТБ 2280 (ноутбук продаётся «ohne OS» — клонировать нечего): +142,89 € → SSD 1 ТБ;
  2. добавить 1 ТБ **2230** во второй слот: +227,20 € (UD90) → 1,5 ТБ.
- **CPU** ⚠️: Ryzen 5 150 — Rembrandt (= 7535HS), 6 ядер Zen 3+, 2022 г., **660M (6 CU, RDNA 2 — maintenance mode с 10.2025)** (`amd-cpu.md` строки 15, 82, 142, 175). Немецкая страница ASUS называет CPU серии «7535HS», глобальная — и «Ryzen 5 150», и «7535HS». VCN 3.1: HEVC/AV1-декод есть, AV1-кодирования нет. Для 4K — слабый (эффекты и цветокоррекция на 660M).
- Экран: 15,6" FHD IPS-level 300 нит, 45 % NTSC, 60 Гц (Icecat, asus.com). Порты: 2× USB-C 10 Гбит/с, 2× USB-A 5 Гбит/с, RJ45, **HDMI 1.4 (4K 30 Гц)**. 50 Втч; 65 Вт USB-C (asus.com; Icecat «Netzteilstärke 65 W», поля «AC-Netzadapter» нет — комплектацию БП подтверждают только названия предложений). Вес: asus.com 1,60 кг, Icecat и даташит ASUS — 1,81 кг. **ОС — противоречие:** даташит ASUS и Icecat — «Windows 11 Pro», заголовки jacob / easynotebooks / notebook.de — «ohne OS / ohne Windows». Для замены SSD не мешает (ключ OEM в прошивке, Windows переустанавливается).
- **Цена** ✅ ([idealo 209457310](https://www.idealo.de/preisvergleich/OffersOfProduct/209457310_-expertbook-p1-pm1503cda-s70264x-asus.html), 30.09.2026): **620,06 €** xtreme.metacomp.de (обычный магазин, срок возврата не показан, до 05.10); jacob.de 635,09; jb-computer.de 635,10 (30 дн.); easynotebooks.de 635,13 (14 дн.); notebook.de 635,14 — 17 предложений.
- **История — новое** (агент поиска: «не проверено, API 404»): карточка с 17.02.2026, 220 точек; минимум **612,18 € (03.09.2026)**, максимум 910,22 €, средняя 719,26 €; 182/182 дней ≤ 1100 €.
- **Итог:** путь 1 — 620,06 + 187,56 + 142,89 = **950,51 €** ✅ (совпало, но это замена SSD, а не второй слот); путь 2 — 620,06 + 187,56 + 227,20 = **1034,82 €**.

#### ASUS ExpertBook P1 PM1503CDA — `PM1503CDA-S70262`
- **Память — исправлено, теперь ✅:** агент поиска: «SKU в Icecat нет, раскладка только по серии». Нашёлся даташит ASUS на этот P/N: [EN](https://gzhls.at/blob/ldb/a/6/a/e/01a53b1dc91ce2d747f13f0a811c3802b2e6.pdf) / [DE](https://gzhls.at/blob/ldb/3/b/9/2/cf362d6162f5f699852f905348737c5af342.pdf) — `90NX09D1-M00A50`, EAN 4711636328357: «16GB DDR5 (**16GB DDR5 SO-DIMM**) · 2x DDR5 SO-DIMM slots», «512GB PCIe Gen4 M.2 SSD · 1x M.2 2230 PCIe 4.0x4», 65 Вт USB-C, 1,807 кг, «**Without OS**», 36 месяцев гарантии. Итог: 1×16 + свободный слот.
- **CPU:** Ryzen 7 170 — Rembrandt (= 7735HS), 8 ядер Zen 3+, **680M (12 CU, RDNA 2)** (`amd-cpu.md` строки 82, 174). iGPU вдвое сильнее 660M, архитектура та же (2022).
- **Цена — исправлено** ([idealo 209457306](https://www.idealo.de/preisvergleich/OffersOfProduct/209457306_-expertbook-p1-pm1503cda-s70262-asus.html), 30.09.2026): 730,54 € у eBay (МП, computeruniverse) — это **«Preis inkl. Gutschein»**, условная цена → не считается. Безусловный минимум — **735,88 €** serverhero.de (срок возврата не показан); playox.de 735,89 (30 дн.); office-partner.de 735,90 (30 дн.); computeruniverse / cyberport 742,89 (30 дн.) — 21 предложение.
- **История — новое:** с 17.02.2026, 226 точек; минимум **558,00 € (19.03.2026)**, максимум 895,27 €, средняя 680,17 €.
- **Итог:** 735,88 + 187,56 + 142,89 (замена SSD на 2280) = **1066,33 €** (агент поиска: 1060,99 € — по условной цене); с SSD 2230 во второй слот — 1150,64 € (> 1100).

#### Acer Aspire 16 AI A16-61M-R8T1 — `NX.JLLEG.009` (EAN 4711474665621)
- **Память** ✅: [Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Acer&ProductCode=NX.JLLEG.009) — 32 ГБ **LPDDR5X-8533**, «Memory Formfaktor: On-board», «RAM-Speicher maximal: 32 GB». Слотов нет → B-список (32 распайки, двухканал есть, апгрейда нет).
- Даташит Acer **не проверено**: acer.com отвечает `ERR_HTTP2_PROTOCOL_ERROR` и в curl, и в Chrome пользователя (30.09.2026, `/de-de/laptops/aspire/aspire-16-ai/pdp/NX.JLLEG.009`, `/de-de/laptops/aspire`). Раскладка — только по Icecat.
- **CPU** ✅: Ryzen AI 7 350 — Krackan Point, 8 ядер (4 Zen 5 + 4 Zen 5c), 860M (8 CU, RDNA 3.5) (`amd-cpu.md` строки 94, 149, 333). Не урезанный; с LPDDR5X-8533 iGPU работает в полную силу. Кодирует AV1; 4:2:2 не декодирует.
- **SSD — уточнено:** 1 ТБ PCIe 4.0 M.2 (Icecat). У трёх продавцов на idealo (office-lieferant, itkadmin и ещё один, одинаковый дистрибьюторский текст) — «1.024 TB SSD NVMe, **QLC**». Вероятно QLC, у Acer не проверено.
- Экран (Icecat): WUXGA IPS, 350 нит, **45 % NTSC**, 120 Гц, 1000:1. Порты: **2× USB4 40 Гбит/с**, 2× USB-A 5 Гбит/с, HDMI, microSD. 65 Втч, 1,55 кг, 100 Вт USB-C («AC-Netzadapter: Ja»).
- **HEVC:** Acer — повышенный риск по `hevc-amd.md` (строки 13, 157): с 06.2026 часть устройств в DE идёт «ohne vorinstallierten HEVC-Codec»; по контексту это непредустановленное расширение Windows, а не аппаратная блокировка. Фразу в даташите Acer проверить не удалось (acer.com не открылся); в Icecat про HEVC ничего нет.
- **Цена** ✅ ([idealo 208031586](https://www.idealo.de/preisvergleich/OffersOfProduct/208031586_-aspire-16-ai-a16-61m-r8t1-acer.html), 30.09.2026): **1080,25 €** easynotebooks.de (14 дн.) и technikdirekt.de (срок не показан); notebook.de 1080,26 (14 дн.); jacob.de 1087,73; office-lieferant 1090,06; euronics МП 1104,95.
- **История** ✅: 353 точки с 13.10.2025; минимум **886,36 € (01.07.2026)**; 1080,25 € — годовой максимум. **Новое:** 21–29.09 дневной минимум был **995,00 €** (кроме 27.09); сегодня этого предложения нет — вероятен возврат к ~995 €.
- **Итог:** **1080,25 €** ✅ (докупать нечего; в пределах 1100 € с запасом 19,75 €).

#### Acer Aspire 16 AI OLED A16-61M-R2R1 — `NX.JP0EG.00Z` (EAN 4711474850324)
- **Память** ✅: [Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Acer&ProductCode=NX.JP0EG.00Z) — 32 ГБ LPDDR5X-8533, «On-board», max 32. Даташит Acer — не проверено (acer.com недоступен, см. выше).
- CPU — как у R8T1 (AI 7 350, Krackan, 860M) ✅.
- Экран (Icecat): **OLED** WUXGA, 300 нит, **100 % DCI-P3**, 60 Гц. ШИМ OLED — не проверено. Порты, батарея, вес, БП 100 Вт — как у R8T1.
- **Цена** ✅ ([idealo 211631508](https://www.idealo.de/preisvergleich/OffersOfProduct/211631508_-aspire-16-ai-a16-61m-r2r1-acer.html), 30.09.2026): карточка смешанная, «ab 794,83 €» — это **A16-61M-R5H7** (NX.JP0EG.010, AI 5 330, 16/512) у computeruniverse, cyberport, e-tec, Galaxus, kaufland; у computeruniverse даже заголовок «R2R1 … Ryzen AI 5 330 16GB/512GB» — ошибка магазина. Настоящий R2R1 (AI 7 350, 32/1 ТБ): **1081,21 €** computeruniverse.net (30 дн., доставка до 09.10); e-tec.at 1111,90 € (с NX.JP0EG.00Z в заголовке).
- e-tec у R5H7 пишет «**Netzteil separat erhältlich**»; Icecat у R2R1 — «AC-Netzadapter: Ja». Перед покупкой R2R1 проверить комплектность у продавца.
- История карточки из-за смеси конфигураций не показательна (минимум 749,00 € 11.08 — это R5H7) ✅ (как у агента поиска).
- **Итог:** **1081,21 €** ✅.

### Наблюдать и вне группы (idealo, 30.09.2026, цены с доставкой)

| P/N | Память (источник) | Цена сейчас | Итог | Вердикт |
|---|---|---|---|---|
| ASUS Vivobook 16 `M1607KA-MB187W` (90NB15F1-M00C70), AI 7 350 / 860M | 16 распайки + 1× SO-DIMM, max 32 ([Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=ASUS&ProductCode=90NB15F1-M00C70): «On-board», «1x SO-DIMM»; серия M1607KA на [asus.com/de](https://www.asus.com/de/laptops/for-home/vivobook/asus-vivobook-16-m1607/techspec/)) ✅ | **949,00 €** electronic4you.de (1 обычный магазин; galaxus 1487,33) — [210697864](https://www.idealo.de/preisvergleich/OffersOfProduct/210697864_-vivobook-16-m1607ka-mb187w-asus.html). История с 04.06.2026: минимум **890,10 € (22.06)** | 949 + 187,56 = 1136,56 € | ✅ наблюдать: в бюджете при цене ≤ 912,44 € |
| ASUS ExpertBook B1 `BM1503CDA-S72123` (90NX0821-M02BX0), R7 170 / 680M | **не подтверждено**: Icecat 404; у B1 бывают 1×16 и 2×8 (у соседнего `-S71655` даташит ASUS — 2×8, см. ниже). На geizhals под этим P/N 15 «nicht kategorisiert» листингов, в т. ч. **64 ГБ** — сборки продавцов («aufgerüstet») | **909,99 €** otto.de МП (30 дн.); Galaxus МП 919,99; kaufland МП 929,99; eBay МП 939,99 — только маркетплейсы — [213397785](https://www.idealo.de/preisvergleich/OffersOfProduct/213397785_-expertbook-b1-bm1503cda-s72123-15-6-amd-ryzen-7-170-16gb-ram-1tb-ssd-90nx0821-m02bx0-asus.html) | при 1×16: 1097,55 €; при 2×8: > 1100 € | ⚠️ наблюдать, но вероятнее 2×8 (как у S71655) → скорее reject |
| ASUS Vivobook S16 `M3607GA-SH004W` (90NB17M1-M00580), AI 7 445 (6 ядер) | 32 = 16 распайки + 16 SO-DIMM: [Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=ASUS&ProductCode=90NB17M1-M00580) «On-board + SO-DIMM», «Speicherlayout: 1 x 16 GB», «1x SO-DIMM» ✅ (исправлено: у агента было «по SKU не проверено») | **1249,00 €** electronic4you.de; galaxus 1369 — [209456208](https://www.idealo.de/preisvergleich/OffersOfProduct/209456208_-vivobook-s16-m3607ga-sh004w-asus.html). В названии у electronic4you — «WUXGA **OLED**» | 1249 € | ✅ выше потолка |
| ASUS ExpertBook P1 `PM1503CDA-S70254X`, R7 170, 32/1 ТБ | не проверено по SKU; у серии PM1503 есть и «16GB DDR5 SO-DIMM x 2», и «**32GB DDR5 SO-DIMM**» (1×32 — не подходит) — [asus.com](https://www.asus.com/laptops/for-work/expertbook/asus-expertbook-p1-pm1503/techspec/) | **1194,14 €** bueromarkt-ag.de (1189,99 + доставка; агент поиска писал 1189,99) — [210991758](https://www.idealo.de/preisvergleich/OffersOfProduct/210991758_-expertbook-p1-pm1503cda-s70254x-asus.html) | 1194,14 € | ✅ выше потолка; при снижении проверить, не 1×32 ли |
| Acer Swift Air 16 `NX.DL5EG.001` (SFA16-61M-R559), AI 7 350 | 32 ГБ LPDDR5 распайки; в [Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Acer&ProductCode=NX.DL5EG.001) противоречие: «RAM-Speicher maximal: 16 GB» при 32 установленных | **1156,99 €** nullprozentshop.de; NBB 1157,99; galaxus 1157,99 (агент поиска: 1149 — без доставки) — [209373389](https://www.idealo.de/preisvergleich/OffersOfProduct/209373389_-swift-air-16-oled-sfa16-61m-r559-acer.html) | 1156,99 € | ✅ выше потолка |
| Gigabyte Gaming A16 `3VHK3DE894SH`, R7 260 + RTX 5060, 16 ГБ | вне группы (разбирает `verify-gpu.md`) | **1099,00 €** coolblue.de / mediamarkt.de / computeruniverse.net — [207329496](https://www.idealo.de/preisvergleich/OffersOfProduct/207329496_-gaming-a16-3vhk3de894sh-gigabyte.html) | с планкой > 1100 € | ✅ GPU-список |

### Выборочная проверка отброшенных

| P/N | Почему отброшен | Проверка | Вердикт |
|---|---|---|---|
| ASUS ExpertBook B1 `BM1503CDA-S71655` (90NX0821-M01U90), R7 170 — «самый обидный»: при 1×16 итог был бы 1015,14 € (дешевле P1 S70262 при том же CPU) | раскладка не подтверждена | **Даташит ASUS на этот P/N** ([gzhls.at PDF](https://gzhls.at/blob/ldb/4/1/3/4/187b24741cf9d760f91fc6f3f6c8825bb088.pdf), EAN 4711636328241): «Memory: 16GB DDR5 (**2x 8GB DDR5 SO-DIMM**) · 2x DDR5 SO-DIMM slots», «1x M.2 2230 PCIe 4.0x4», без ОС, 36 мес. гарантии. Цена сейчас 684,69 € playox.de (30 дн.) — [209405016](https://www.idealo.de/preisvergleich/OffersOfProduct/209405016_-expertbook-b1-bm1503cda-s71655-asus.html) | ✅ **отброшен верно**, теперь по даташиту: 2×8 → менять обе планки, > 1100 € |
| ASUS Vivobook 16 `M1607KA-MB172W` (90NB15F2-M00BJ0) — 799 € + планка = 986,56 €, дешевле M1607GA | Ryzen AI 5 330 | [Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=ASUS&ProductCode=90NB15F2-M00BJ0): «Prozessor: 330», «Anzahl Prozessorkerne: 4», «Radeon 820M»; «On-board + SO-DIMM», «1x SO-DIMM» | ✅ отброшен верно: 4 ядра и 820M (2 CU) для 4K мало (`amd-cpu.md` строки 149, 297) |
| ASUS ExpertBook B1 `BM1503CDA-S71654` (90NX0821-M01U80), R5 150 | раскладка не подтверждена | Icecat — «SO-DIMM», «2x SO-DIMM», без раскладки; даташит ASUS по этому P/N не искал (DuckDuckGo выдал капчу — не проходил). По аналогии с S71655 — вероятно 2×8 | ✅ отброс оставить (к тому же P1 S70264X с подтверждённым 1×16 дешевле) |

### Опровергнуто / исправлено

| # | Утверждение агента поиска | Что на самом деле | Источник |
|---|---|---|---|
| 1 | P1 PM1503: «докупить SSD 1 ТБ во второй M.2» за 142,89 € (NV3 2280) | второй слот — **M.2 2230**, NV3 2280 туда не встанет. Итог 950,51 € держится только как **замена** 512 ГБ на 1 ТБ; добавить 1 ТБ 2230 — +227,20 € (итог 1034,82 €) | даташит ASUS, [asus.com](https://www.asus.com/laptops/for-work/expertbook/asus-expertbook-p1-pm1503/techspec/), [heise](https://www.heise.de/bestenlisten/testbericht/asus-expert-book-pm1-im-test-guenstiger-laptop-mit-ryzen-5-und-16-gb-ram-ueberzeugt/jqmdlcc), idealo [UD90](https://www.idealo.de/preisvergleich/OffersOfProduct/203279966_-ud90-1tb-m-2-2230-silicon-power.html) |
| 2 | `PM1503CDA-S70262` — 730,54 € (eBay МП) → итог 1060,99 € | 730,54 € — «Preis inkl. Gutschein» (условная); безусловно — 735,88 € serverhero.de → итог **1066,33 €** | [idealo 209457306](https://www.idealo.de/preisvergleich/OffersOfProduct/209457306_-expertbook-p1-pm1503cda-s70262-asus.html) |
| 3 | `PM1503CDA-S70262`: «раскладка только по серии, в Icecat нет» | даташит ASUS на P/N: 1×16 + слот, без ОС | [gzhls.at PDF](https://gzhls.at/blob/ldb/a/6/a/e/01a53b1dc91ce2d747f13f0a811c3802b2e6.pdf) |
| 4 | P1 S70264X / S70262: «история не проверено (API 404)» | API ответил: S70264X мин. 612,18 € (03.09.2026); S70262 мин. 558,00 € (19.03.2026) | API idealo |
| 5 | P1: «гарантия не проверено» | 36 месяцев международной гарантии | даташиты ASUS |
| 6 | M3607HA / M1607GA — источник памяти `asus.com/de/...` | на немецких страницах этих CPU нет (там M3607KA/GA и M1607KA); Ryzen 7 260 и AI 7 445 — только на глобальных страницах ASUS | [asus.com M3607](https://www.asus.com/laptops/for-home/vivobook/asus-vivobook-s16-m3607/techspec/), [asus.com M1607](https://www.asus.com/laptops/for-home/vivobook/asus-vivobook-16-m1607/techspec/) |
| 7 | M3607HA: экран «глянец», частота не указана | Icecat: 144 Гц и «Glanz»; ASUS: все WUXGA-панели M3607 — Anti-glare → глянец сомнителен | Icecat, asus.com |
| 8 | M1607GA: «81 день ≤ 1100 € из 182» | 81 — это все точки истории: остальные дни товара не было в продаже | API idealo |
| 9 | Acer R8T1: «сегодня — годовой максимум» | верно (1080,25 = максимум), но 21–29.09 дневной минимум был 995,00 € | API idealo |
| 10 | `M3607GA-SH004W`: «16+16 по SKU не проверено» | Icecat по 90NB17M1-M00580: «On-board + SO-DIMM», «Speicherlayout 1 x 16 GB» — 16+16 подтверждено | Icecat |
| 11 | `PM1503CDA-S70254X` 1189,99 €, Swift Air `R559` 1149 € | с доставкой 1194,14 € и 1156,99 € (выше потолка в любом случае) | idealo |
| 12 | Планка 187,56 € как стабильная цена | одно предложение на маркетплейсе Galaxus, неделю назад 396–426 € — может пропасть; запасной вариант 206,80 € | [idealo 213624753](https://www.idealo.de/preisvergleich/OffersOfProduct/213624753_-valueram-16gb-ddr5-5600mhz-cl46-so-dimm-on-die-ecc-kvr56s46bs8-16-kingston.html) |

### Известные проблемы (обзоры)

- **Vivobook 16 M1607 (тест M1607KA / «M1606K», AI 7 350, 16 ГБ), 78 %** — [Notebookcheck, 26.02.2025](https://www.notebookcheck.net/Asus-Vivobook-16-laptop-review-AI-features-at-the-forefront-genuine-productivity-boost-or-marketing-hype.971144.0.html). Корпус тот же, что у M1607GA:
  - экран B160UAN04.3: **55,3 % sRGB**, 325 нит, 1358:1, без ШИМ, медленный;
  - все USB — 5 Гбит/с; нет подсветки клавиатуры, SD, LAN, Wi-Fi 6E;
  - рамка экрана легко отходит;
  - SSD Micron 2500 троттлит при долгой нагрузке;
  - охлаждение несбалансированное, батарея слабее конкурентов; 860M ниже среднего (у M1607GA — ещё слабее, 840M).
- **Vivobook S16 M3607**: теста WUXGA-версии на AMD не нашёл. Родственный [NBC S3607QA (Snapdragon, 2,5K), 84 %](https://www.notebookcheck.net/Asus-Vivobook-S16-Laptop-Review-Good-everyday-computer-with-almost-20-hours-of-battery-life-for-EUR899.1002073.0.html): корпус хороший, под полной нагрузкой шумно (47,6–50,2 дБ(A)), плохо видны символы клавиш. Панель там другая (98 % sRGB) — к нашей WUXGA 45 % NTSC не относится; по аналогии с M1607 ждать ~55–60 % sRGB.
- **ExpertBook P1 PM1503 (R5 7535HS = R5 150, 16 ГБ), 90 %** — [heise, 09.11.2025](https://www.heise.de/bestenlisten/testbericht/asus-expert-book-pm1-im-test-guenstiger-laptop-mit-ryzen-5-und-16-gb-ram-ueberzeugt/jqmdlcc): свободный слот RAM и M.2 2230, MIL-STD-810H; экран 287 кд/м² — темновато; HDMI 1.4; вентилятор до 36 дБ(A); батарея ~7 ч. Сестра на Intel — [NBC P1503CVA, 80 %](https://www.notebookcheck.net/Asus-ExpertBook-P1-review-The-affordable-laptop-for-office-use-and-working-from-home-comes-with-numerous-security-features.961204.0.html): панель CMN1565 — **63,3 % sRGB**, 295 нит, без ШИМ, неравномерная подсветка; до 46,7 дБ(A) в режиме Performance.
- **Acer Aspire 16 AI A16-61M**: своего теста NBC нет, только [сборник](https://www.notebookcheck.net/Acer-Aspire-16-AI-A16-61M.1237489.0.html): Techradar (01.2026) — **60 %**, «build quality issues», для тяжёлых задач «isn't great»; Trusted Reviews (12.2025) — хвалит OLED и порты, батарея «a little disappointing».

### HEVC

- ASUS (M3607HA, M1607GA, PM1503): в Icecat, даташитах ASUS по P/N, руководствах пользователя ([M3607HA](https://objects.icecat.biz/objects/mmo_135052170_1758701985_2971_3708122.pdf), [PM1503](https://objects.icecat.biz/objects/mmo_140207157_1779454078_2889_240.pdf)) и на страницах asus.com слов HEVC/H.265 нет. Отключений у ASUS не найдено (`hevc-amd.md` строки 156, 179) → риск **низкий, «нет данных»**.
- Acer (R8T1, R2R1): риск **повышенный** (`hevc-amd.md` строки 13, 157, 241) — вероятно, только непредустановленное расширение Windows. Фразу в документах Acer проверить не удалось: acer.com — `ERR_HTTP2_PROTOCOL_ERROR` в curl и Chrome; в Icecat про HEVC ничего.
- Всем: DXVA Checker в срок возврата.

### Что не проверено

- Acer: даташит и мануал на acer.com (сайт не открылся 30.09 ни в curl, ни в Chrome). Раскладка R8T1/R2R1 — только Icecat.
- Даташиты ASUS по P/N для M3607HA-RP017W и M1607GA-MB020W: на geizhals у M3607HA только «nicht kategorisiert» без PDF, DuckDuckGo выдал капчу (не проходил). У Vivobook это не критично: у серий один слот и 16 ГБ распайки — другой раскладки 16 ГБ нет.
- Раскладка `BM1503CDA-S72123` и `-S71654`; `PM1503CDA-S70254X` (1×32 или 2×16).
- Сроки возврата у xtreme.metacomp.de, serverhero.de, nullprozentshop.de, technikdirekt.de — idealo их не показывает.
- Гарантия Vivobook и Acer — не проверено.
