## Проверка idealo-sweep

_30.09.2026, локальная сессия, скептическая проверка шорт-листа [`candidates-idealo-sweep.md`](candidates-idealo-sweep.md) (7 SKU) и выборочно 4 отброшенных._
_Память — PDF PSREF по каждому MTM (скачал заново), HP QuickSpecs c09053765 v7 + сервис-мануал HP + Icecat open. CPU — [amd-cpu.md](amd-cpu.md), кодеки — [amd-codecs.md](amd-codecs.md), HEVC — [hevc-amd.md](hevc-amd.md). Цены — idealo.de в Chrome пользователя, своя вкладка, «Daten vom 30.09.2026 12:47–12:58»; история — API idealo (в 12:47–12:55 отвечал 404, с ~12:58 — 200)._
_Статус: готово (30.09.2026, ~14:05)._

### Вывод

1. **Раскладка памяти у всех 5 Lenovo подтверждена PDF PSREF** — везде «2x 16GB SODIMM», два слота. У `83HY008CGE`, `83HU004KGE`, `21MW009MGE`, `21UT004EGE` второй слот M.2 есть. Опровергнуть не удалось.
2. **`83HY008CGE` (IdeaPad Slim 5 16AKP10, Ryzen AI 7 350) — подтверждён, список A.** Это единственный Zen 5 с 2×16 в бюджете: **1059,99 €** на Kaufland, маркетплейс, продавец expert, возврат 14 дн. Предложение одно. За полгода цена всегда была ≤ 1100 €, минимум 896,28 €.
3. **`83HU004KGE` — подтверждён, условный вариант «+ SSD»: 941,82 €** (776,90 + SSD 142,89 + зарядка 22,03). Зарядки в комплекте действительно нет: PSREF «No Power Adapter», а даташит idealo «Netzteil 65 Watt» ошибается. Самую низкую цену даёт маленький магазин (33 отзыва, срок возврата не показан); у expert.de с возвратом 14 дн. выходит 963,92 €. CPU Zen 3+ 2022 г.
4. **`21MW009MGE` — подтверждён (1091,89 €), но смысла нет.** Тот же ноутбук `21MW00AYGE` с 1 ТБ с завода стоит 998,99 €. Цена растёт: 865,67 € 01.09 → 949 € с 10.09.
5. **`21UT004EGE` — исправлен итог: 1091,89 €, а не 1036,89.** Цена 894 € действует только с купоном («Preis inkl. Gutschein»), и в ней нет 4,90 € доставки. Без купона — 949 € (Galaxus, маркетплейс). Порог SSD-варианта (≤ 957 €) за полгода выполнялся 16 дней из 182. Ryzen 5 220 в [amd-cpu.md](amd-cpu.md) (п. 8) стоит в списке **«Не брать»**. `21UT004QGE` с 1 ТБ с завода (1066,82 €, по sweep) дешевле этого варианта.
6. **HP 255R G10 `CJ5Q2EA` / `CJ5Q1EA` — опровергнуто → reject.**
   - Сервис-мануал HP пишет «Onboard memory up to 16 GB, not accessible or upgradeable». Планки идут как деталь для авторизованного сервиса. Icecat: «RAM maximal 16 GB». Схему 2×16 HP нигде не подтверждает.
   - Для этого семейства (HP 200 Series) HEVC — риск высокий: HP отключила его на 255 G9.
   - Продавец один: только предоплата, 3,8 ★ по 30 отзывам, срок возврата не показан.
   - У `CJ5Q1EA` заголовок предложения («7530U, Windows 11 Pro») не совпадает с P/N.
   - Итог с самой дешёвой планкой был бы 792,56 €, а не 853,89.
7. **`21KK0074GE` — цена опровергнута, SKU → reject по CPU.** Цена не «1149 €»: в 12:50 снова 1007,99 € у electronic4you.de (только предоплата, 2,6 ★). Но R7 7730U — Barcelo-R (Zen 3, Vega, DDR4), в [amd-cpu.md](amd-cpu.md) он в списке «Не брать». Сам агент поиска по той же причине отбросил `AG15-42P-R3HH` и `CA8S1EA`.
8. **Отброшенные (выборочно 4) — отброшены верно.** Пограничный случай — V15 G6 ARP `83UU001LGE`: заменить SSD на 1 ТБ вышло бы ≈ 933 €. Но это не «второй M.2», к тому же HDMI 1.4b и DP 1.2.

### Сводная таблица

| P/N | CPU (кремний) | Память (даташит) | SSD / 2-й M.2 | БП | Цена сейчас (с доставкой) | Итог с докупкой | Мин. 1 год | Дней ≤ порога / 182 | Вердикт | Список |
|---|---|---|---|---|---|---|---|---|---|---|
| [83HY008CGE](https://www.idealo.de/preisvergleich/OffersOfProduct/209439304_-ideapad-slim-5-16-83hy008cge-lenovo.html) | AI 7 350 — Krackan Point, Zen 5 4+4c, 860M | 2×16 DDR5-5600 ✅ [PSREF](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=83HY008CGE&country_code=) | 1 ТБ 2242 + свободный 2280 | 65 Вт ✅ | **1059,99** kaufland МП (expert), 14 дн. | **1059,99** | 896,28 (23.02.2026) | 179/179 | ✅ подтверждён | A-2x16 |
| [83HU004KGE](https://www.idealo.de/preisvergleich/OffersOfProduct/210287882_-ideapad-slim-5-16-83hu004kge-lenovo.html) | R5 7535HS — Rembrandt-R, Zen 3+, 660M | 2×16 DDR5-4800 ✅ [PSREF](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=83HU004KGE&country_code=) | 512 ГБ 2242 + свободный 2280 | **нет** | **776,90** technik-brandenburg.de; 799 expert.de (14 дн.) | **941,82** (+ NV3 + 65 Вт) | 699,00 (20.05.2026) | 125/125 (≤ 935) | ✅ подтверждён | C-plus-ssd |
| [21MW009MGE](https://www.idealo.de/preisvergleich/OffersOfProduct/206598202_-thinkbook-16-g7-21mw009mge-lenovo.html) | R5 7535HS — Rembrandt-R | 2×16 DDR5-4800 ✅ [PSREF](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=21MW009MGE&country_code=) | 512 ГБ + «Two M.2 2280» | 65 Вт ✅ | **949,00** easynotebooks.de, 14 дн. | **1091,89** | 672,26 (23.10.2025) | 182/182 (≤ 957) | ✅, но вытеснен `21MW00AYGE` | C-plus-ssd |
| [21UT004EGE](https://www.idealo.de/preisvergleich/OffersOfProduct/209122443_-thinkbook-16-g9-21ut004ege-lenovo.html) | R5 220 — Hawk Point (Phoenix 2), 2 Zen 4 + 4 Zen 4c, 740M | 2×16 DDR5-5600 ✅ [PSREF](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=21UT004EGE&country_code=) | 512 ГБ 2242 + свободный 2280 | 65 Вт ✅ | 898,90 **с купоном**; без условий **949,00** Galaxus МП (HEINZSOFT), 30 дн.; обычный магазин 1015,90 | **1091,89** (с купоном 1041,79) | 889,00 (26.09.2026, «ab», с купоном) | 16/182 (≤ 957) | ⚠️ исправлено: итог и CPU | C-plus-ssd (слабо) |
| [CJ5Q2EA](https://www.idealo.de/preisvergleich/OffersOfProduct/208126554_-255-g10-cj5q2ea-hp.html) | R5 7535U — Rembrandt-R, 28 Вт, 660M | 1×16 DDR5-4800, «2x SO-DIMM» (Icecat); HP MSG: «onboard up to 16 GB» ⚠️ | 1 ТБ 2280, второго M.2 нет | 65 Вт ✅ | **605,00** asaboshisystems.de, только предоплата | 792,56 (+ Kingston 187,56) | 548,99 (28.11.2025) | 27/27 точек | ❌ опровергнуто | reject |
| [CJ5Q1EA](https://www.idealo.de/preisvergleich/OffersOfProduct/208126364_-255-g10-cj5q1ea-hp.html) | как CJ5Q2EA (FreeDOS) | как CJ5Q2EA ⚠️ | как CJ5Q2EA | 65 Вт ✅ | **605,00** asaboshisystems.de — заголовок «7530U, Win 11 Pro» ≠ P/N | 792,56 | 499,00 (23.11.2025) | 28/28 точек | ❌ опровергнуто | reject |
| [21KK0074GE](https://www.idealo.de/preisvergleich/OffersOfProduct/203811127_-thinkbook-16-g6-21kk0074ge-lenovo.html) | R7 7730U — **Barcelo-R, Zen 3, Vega 8**, DDR4 | 2×16 DDR4-3200 ✅ [PSREF](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=21KK0074GE&country_code=) | 1 ТБ; «Two M.2 2280 **PCIe 3.0**» | 65 Вт ✅ | **1007,99** electronic4you.de (предоплата, 2,6 ★); дальше 1149 easynotebooks | 1007,99 | 767,62 (05.10.2025) | 176/182 (≤ 1100) | ⚠️ цена опровергнута; CPU — «не брать» | reject |

- Порог = 1100 € минус докупка: SSD Kingston NV3 142,89 €; зарядка Lenovo 65 Вт 22,03 €; планка Kingston 187,56 €. Дни — дневные минимумы API idealo: цена «ab», без доставки, с условными ценами.
- HEVC: у Lenovo во всех 6 PDF PSREF (5 шорт-листа + `83UU001LGE`) слов HEVC/H.265 нет. Отключений у Lenovo на AMD не найдено ([hevc-amd.md](hevc-amd.md), п. 7) → риск **низкий**, проверить DXVA Checker'ом в срок возврата. HP 255R G10 — риск **высокий** (см. ниже).

### По SKU

#### 1. IdeaPad Slim 5 16AKP10 — `83HY008CGE` (EAN 199273505975) — ✅ подтверждён, A-2x16
- PSREF [PDF](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=83HY008CGE&country_code=):
  - AI 7 350 (8C/16T, 2,0/5,0 ГГц), Radeon 860M;
  - «2x 16GB SODIMM DDR5-5600», «Two DDR5 SODIMM slots, dual-channel capable», «Up to 32GB»;
  - 1 ТБ M.2 2242 PCIe 4.0 x4; «Models with AMD Ryzen AI 5 340 / 350 processor: two M.2 slots • One M.2 2242 … • One M.2 2280 PCIe 4.0 x4»;
  - 16" WUXGA IPS 300 нит, 45 % NTSC, 60 Гц;
  - 2× USB-A 5 Гбит/с, 2× USB-C 10 Гбит/с (PD 65–100 Вт, DP 1.4), HDMI 2.1 4K60, microSD; USB4 и Ethernet нет;
  - 60 Втч, **65 Вт USB-C**, ~1,85 кг, алюминий сверху и снизу;
  - Win 11 Home; гарантия 2 года Courier/Carry-in, батарея 1 год; анонс 23.10.2025.
- CPU: Krackan Point, Zen 5 + Zen 5c, 860M 8 CU, VCN 4.0.5 ([amd-cpu.md](amd-cpu.md): «AI 7 350 — ок/лучший»).
  - Для 4K: декод H.264 8 бит, HEVC 4:2:0 8/10 бит, AV1; кодирует AV1. 4:2:2 и H.264 10 бит не декодирует ([amd-codecs.md](amd-codecs.md)).
- Цена ([idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/209439304_-ideapad-slim-5-16-83hy008cge-lenovo.html), 12:47):
  - единственное новое предложение: **1059,99 €** с доставкой — kaufland.de, маркетплейс, «Verkauf durch: expertDeutschland» (4,5 ★, 56 396 отзывов), возврат 14 дн., доставка до 06.10;
  - б/у и B-Ware — отдельная вкладка.
- История (API, 1 год): 179 точек с 13.02.2026.
  - Минимум **896,28 €** (с 23.02, 9 дней); средняя 952,23 €; максимум 1059,99 € (30.09).
  - Последние дни: 25–26.09 — 979 €, 27–29.09 — 1049,99 €.
- Подтверждено всё из candidates. Уточнение: утром 30.09 [market-amd.md](market-amd.md) видел «только б/у 949 €», а точка истории за 29.09 — 1049,99 €. Значит, в истории новые предложения, и до 30.09 они уже появлялись. Какой продавец дал минимум 896,28 € — **не проверено**: API этого не показывает.
- Риск: цена у верхней границы года и только одно предложение — может исчезнуть. Поставить Preiswecker.

#### 2. IdeaPad Slim 5 16ARP10 — `83HU004KGE` (EAN 199275056086) — ✅ подтверждён, C-plus-ssd
- PSREF [PDF](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=83HU004KGE&country_code=):
  - R5 7535HS (6C/12T, 3,3/4,55 ГГц), 660M;
  - «2x 16GB SODIMM DDR5-4800». Сноска [1]: «Installed memory is actually DDR5-5600 but runs as DDR5-4800 due to platform limitation»;
  - два слота, «Up to 32GB»;
  - 512 ГБ M.2 2242; «Two M.2 slots • One M.2 2242 … • One M.2 2280 PCIe 4.0 x4»;
  - **«Power Adapter: No Power Adapter»**;
  - порты: 2× USB-C **5 Гбит/с** (PD 65–100 Вт, DP 1.4), HDMI 2.1, microSD;
  - 60 Втч, ~1,85 кг, корпус как у `83HY008CGE`; гарантия 2 года; анонс **22.01.2026** — модель 2026 г. на CPU 2022 г.
- CPU: Rembrandt-R, Zen 3+, 660M 6 CU RDNA 2, VCN 3.1.1. Драйверы RDNA 2 с 10.2025 в «maintenance mode». AV1 не кодирует. [amd-cpu.md](amd-cpu.md): «только если очень дёшево». При итоге 942 € это дёшево.
- Цена ([idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/210287882_-ideapad-slim-5-16-83hu004kge-lenovo.html), 12:48), 5 предложений:
  - **776,90 €** — technik-brandenburg.de (5,0 ★, всего 33 отзыва), срок возврата не показан, доставка до 05.10;
  - 799 € — expert-technomarkt.de (4,4 ★ / 3447), boomstore.de (3,7 ★ / 645), **expert.de (возврат 14 дн., 2,4 ★ / 4371)**, eBay МП expert_ecommerce (возврат 30 дн.).
- История: 125 точек с 07.05.2026; минимум **699,00 €** (с 20.05, 9 дней); средняя 769,45 €; максимум 831 €.
- Итог: 776,90 + 142,89 (Kingston NV3 1 ТБ, alternate.de) + 22,03 (Lenovo 65 Вт `4X20M26272`, computeruniverse.net) = **941,82 €**, диск 1,5 ТБ. У expert.de — 963,92 €.
- Исправлено: даташит idealo указывает «Netzteil 65 Watt», а у этого MTM зарядки нет → докупка обязательна (как и считал агент поиска).

#### 3. ThinkBook 16 G7 ARP — `21MW009MGE` (EAN 199271442500) — ✅ подтверждён, C-plus-ssd, но вытеснен
- PSREF [PDF](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=21MW009MGE&country_code=):
  - R5 7535HS, 660M; «2x 16GB SODIMM DDR5-4800», два слота, «Up to 64GB»;
  - 512 ГБ 2242; «Two M.2 2280 PCIe 4.0 x4 slots», «M.2 2280 SSD up to 2TB each»;
  - порты: USB4 40 Гбит/с (PD 45–65 Вт, DP 1.4), USB-C 10 Гбит/с, HDMI 2.1, SD, RJ45, 2× USB-A;
  - **45 Втч**, 65 Вт USB-C, от 1,7 кг, дно из PC-ABS;
  - гарантия 1 год + «1Y Premier WHB (CPN)»; анонс 15.05.2025.
- Цена ([idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/206598202_-thinkbook-16-g7-21mw009mge-lenovo.html), 12:48), 11 предложений: **949,00 €** easynotebooks.de (14 дн., до 01.10); notebook.de 949,01 (14 дн.); notebooksbilliger.de и galaxus.de 1007,99 (30 дн.).
- История: минимум **672,26 €** (23–24.10.2025), средняя 819,41 €, все 182 дня ≤ 957 €. Но в сентябре цена растёт: 01.09 — 865,67 €, с 10.09 — 949 €.
- Итог: 949 + 142,89 = **1091,89 €**. Запас до потолка — 8 €.
- Вывод агента верен: хуже `21MW00AYGE` (тот же ноутбук, 1 ТБ с завода, 998,99 € по [market-amd.md](market-amd.md); в этой проверке не перепроверял).

#### 4. ThinkBook 16 G9 AHP — `21UT004EGE` (EAN 199273308026) — ⚠️ исправлено
- PSREF [PDF](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=21UT004EGE&country_code=):
  - R5 220 (6C/12T, 3,2/4,9 ГГц), 740M; «2x 16GB SODIMM DDR5-5600», два слота, «Up to 64GB»;
  - 512 ГБ 2242; «Two M.2 slots • One M.2 2242 … • One M.2 2280 PCIe 4.0 x4»;
  - **2× USB4 40 Гбит/с** (DP 1.4a), HDMI 2.1, SD, RJ45;
  - экран **400 нит**, 45 % NTSC, 60 Гц;
  - 48 Втч, 65 Вт USB-C, от 1,7 кг; гарантия 1 год + 1Y Premier; анонс 14.11.2025.
- CPU: Hawk Point (Phoenix 2): **2 полных Zen 4 + 4 Zen 4c**, 740M — всего 4 CU, без NPU; VCN 4.0.2 — AV1 кодирует ([amd-cpu.md](amd-cpu.md), таблица «Ryzen 200»).
  - [amd-cpu.md](amd-cpu.md), п. 8: «Не брать: … Ryzen 5 220». Для 4K на таймлайне iGPU слабая.
  - Противоречие в проекте: [market-amd.md](market-amd.md) называет лучшим в бюджете `21UT004QGE` — это тот же Ryzen 5 220. Решить при сборке `REPORT.md`.
- Цена ([idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/209122443_-thinkbook-16-g9-21ut004ege-lenovo.html), 12:50), 7 предложений:
  - 894 € + 4,90 € = **898,90 € — «Preis inkl. Gutschein»** (technikdeals24.de 5,0 ★ / 6; heinzsoft-shop.de 4,7 ★ / 142; только предоплата);
  - без условий: **949,00 €** Galaxus, маркетплейс (HEINZSOFT), возврат 30 дн.; eBay МП heinzsoft 981,23;
  - обычные магазины: notebookstore.de 1015,90 (14 дн.), bueromarkt-ag.de 1143,13.
- История: 236 точек с 21.01.2026; минимум 889 € (26.09, с купоном); средняя 1017,74 €. ≤ 1100 € — 150 из 182 дней, **≤ 957 € — только 16 из 182**.
- Опровергнуто / исправлено:
  - «894 € → + SSD = 1036,89 €». Это цена с купоном и без доставки. С купоном выходит 1041,79 €, без купона — **1091,89 €**.
  - Смысл варианта — только ради 1,5 ТБ: `21UT004QGE` с 1 ТБ с завода — 1066,82 € (по [candidates-idealo-sweep.md](candidates-idealo-sweep.md), не перепроверял).

#### 5–6. HP 255R G10 — `CJ5Q2EA` (Win 11 Pro, GTIN 199764044174) / `CJ5Q1EA` (FreeDOS, GTIN 199764044150) — ❌ опровергнуто → reject
- Icecat ([CJ5Q2EA](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=HP&ProductCode=CJ5Q2EA), [CJ5Q1EA](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=HP&ProductCode=CJ5Q1EA)):
  - 7535U, 660M; «Speicherlayout 1 x 16 GB», «Speicherkartensteckplätze 2x SO-DIMM», DDR5-4800;
  - **«RAM-Speicher maximal: 16 GB»** — агент поиска эту строку не указал;
  - 1 ТБ M.2 NVMe, «Anzahl SSD installiert 1»; экран **300 нит**, 45 % NTSC (закрывает «250 или 300 — не проверено»);
  - 2× USB-A 5 Гбит/с, 1× USB-C 10 Гбит/с (DP, PD), HDMI 1.4b; 41 Втч, 65 Вт, 1,66 кг;
  - гарантия 1 год, без выезда.
- [QuickSpecs c09053765 v7](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09053765) (06.03.2026):
  - «Maximum Memory 32GB DDR5-4800 (**1 x 32GB**)»; среди конфигураций 16 ГБ — «1 x 16 GB», «2 x 8 GB» и распайка LPDDR5;
  - «2 SODIMM (RMB-UR only)», «**All slots are customer non-accessible / non-upgradeable**», «Support Dual Channel Memory»;
  - один «Primary Storage»; в GRAPHICS только «Support HD decode, DX12, HDMI 1.4b».
- [Сервис-мануал HP 255R G10](https://kaas.hpcloud.hp.com/pdf-public/pdf_11296126_en-US-1.pdf) (P22370-001, First Edition 12.2024):
  - в таблице 1-1 только «Onboard memory supporting up to 16 GB of RAM (not accessible or upgradeable), LPDDR5-4800»;
  - раздел «Memory modules (select products only)» — планки 16 и 8 ГБ, глава «Removal and replacement procedures for **authorized service provider parts**»; перед заменой снять дно и батарею;
  - SSD — один M.2 2280.
- Вывод по памяти: 1×16 + свободный слот — **вероятно** (Icecat + «2 SODIMM» в QuickSpecs). **2×16 HP не подтверждает**: максимум по документам HP — 16 или 32 ГБ одной планкой, а слоты «не для пользователя». Проверить можно только после покупки (CPU-Z → SPD).
- HEVC: в QuickSpecs и сервис-мануале фразы нет. По заявлению HP, HEVC отключён у «200 Series G9» (255 G9 — [Ars](https://arstechnica.com/gadgets/2025/11/hp-and-dell-disable-hevc-support-built-into-their-laptops-cpus/), через [hevc-amd.md](hevc-amd.md)). Вывод проекта: «HP на AMD — только EliteBook 8 … или не брать» ([hevc-amd.md](hevc-amd.md), п. 10).
- CPU: Rembrandt-R U (28 Вт), 660M, VCN 3.1.1, AV1 не кодирует — самый слабый в шорт-листе.
- Цена (idealo, 12:49): по одному предложению на каждой карточке.
  - [CJ5Q2EA](https://www.idealo.de/preisvergleich/OffersOfProduct/208126554_-255-g10-cj5q2ea-hp.html) и [CJ5Q1EA](https://www.idealo.de/preisvergleich/OffersOfProduct/208126364_-255-g10-cj5q1ea-hp.html): 599 + 6 = **605,00 €**, asaboshisystems.de, **только предоплата** (Vorkasse), 3,8 ★ / 30 отзывов, срок возврата не показан.
  - Предложение на карточке `CJ5Q1EA` называется «HP 255 G10 AMD Ryzen 5 **7530U** 2.0GHz … **Windows 11 Pro**». Это другой CPU (Barcelo-R, DDR4) и не FreeDOS → неясно, что продают.
- История: 27–28 точек с 24.10.2025, с большими дырами; минимум 548,99 / 499,00 €; 20.08 и 22.09 — 999,95 €.
- Итог, если всё же брать: 605 + **187,56** (Kingston `KVR56S46BS8-16`, МП, 30 дн.) = **792,56 €**. Не 853,89: Crucial за 248,89 € — не самая дешёвая планка.

#### 7. ThinkBook 16 G6 ABP — `21KK0074GE` (EAN 197530285905) — ⚠️ цена опровергнута, reject по CPU
- PSREF [PDF](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=21KK0074GE&country_code=):
  - R7 7730U (8C/16T); «2x 16GB SO-DIMM DDR4-3200», два слота, до 64 ГБ;
  - 1 ТБ 2242; «Two M.2 2280 **PCIe 3.0** x4 slots»;
  - **71 Втч**, 65 Вт USB-C; 2× USB-C 3.2 Gen 2 (USB4 нет), HDMI 2.1, SD, RJ45;
  - гарантия 1 год; анонс 2024.
- CPU: Barcelo-R — «кремний 2021 года, DDR4, драйвер Vega», VCN 2.2, AV1 не декодирует. [amd-cpu.md](amd-cpu.md), п. 8: «Не брать: … Barcelo-R».
- Цена ([idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/203811127_-thinkbook-16-g6-21kk0074ge-lenovo.html), 12:50), 9 предложений:
  - **999 + 8,99 = 1007,99 €** — electronic4you.de, **только предоплата, 2,6 ★ / 592**, срок возврата не показан;
  - дальше easynotebooks.de 1149 (14 дн.), notebook.de 1149,01, galaxus.de 1159 (30 дн.).
- История: минимум 767,62 € (05.10.2025); ≤ 1100 € — 176 из 182 дней. В сентябре: 01–08.09 — 999; 09–10.09 — 1099; 11–16.09 — 1149; с 17.09 — снова 999.
- Опровергнуто:
  - «сейчас ab 1149 € — выше потолка»: в 12:50 снова 999 €;
  - список «watch-over-1100» неверен по цене. Но по правилу CPU это reject — так же, как агент сам отбросил `AG15-42P-R3HH` (Barcelo) и `CA8S1EA` (Barcelo-R).

### Отброшенные — выборочная проверка

| P/N | Довод агента | Проверка | Итог |
|---|---|---|---|
| Lenovo V15 G6 ARP `83UU001LGE` | нет второго M.2 | PSREF [PDF](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=83UU001LGE&country_code=): «One M.2 2280 PCIe 4.0 x4 slot», «One drive, up to 1TB M.2 2242»; 2×16 DDR5-4800; 15,6" FHD 300 нит 45 % NTSC; USB-C 10 Гбит/с с **DP 1.2**, **HDMI 1.4b**; 65 Вт Round Tip в комплекте. [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/209094412_-v15-g6-83uu001lge-lenovo.html) (12:58): ab 759 € aitek.de; galaxus.de 789,95 € (30 дн.); минимум 712,52 € (10.08.2026) | **верно** по правилу. Замена SSD на 1 ТБ: ≈ 789,95 + 142,89 = 932,84 €. Это не вариант «+ второй M.2», а внешний 4K-монитор — только 30 Гц по HDMI 1.4b |
| HP EliteBook 665 G11 `8Z719AV` | HEVC выключен | [QuickSpecs c08927104 v11](https://www8.hp.com/h20195/V2/GetPDF.aspx/c08927104) (19.09.2025), GRAPHICS: «Hardware acceleration for CODEC H.265/HEVC … is disabled on this platform» | **верно** |
| IdeaPad Slim 5 16AKP10 `83HY009NGE` | 2×8 | PSREF [PDF](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=83HY009NGE&country_code=): «2x 8GB SODIMM DDR5-5600»; AI 5 330 (4C/8T); второй M.2 2280 только **PCIe 4.0 x2**. Две планки по 16 ГБ — 2 × 187,56 = 375 € → ≈ 1223 € | **верно** |
| HP EliteBook 8 G1a 16 `CN0Q3EC` | 999 + SSD > 1100 | HEVC включён ([hevc-amd.md](hevc-amd.md)). Самые дешёвые 1 ТБ NVMe на idealo — Kingston NV3 ab 134,90 € (142,89 с доставкой, [карточка](https://www.idealo.de/preisvergleich/OffersOfProduct/204697967_-nv3-1tb-kingston.html)), Patriot P300 1 ТБ ab 141,90 € ([карточка](https://www.idealo.de/preisvergleich/OffersOfProduct/200465701_-p300-m-2-patriot.html)) → итог ≥ 1134 € | **верно** (не хватает ~35–42 €; стоит поставить Preiswecker) |

### Докупка (idealo, 30.09.2026, 12:51–12:58)

| Что | Цена с доставкой | Магазин · возврат | Карточка |
|---|---|---|---|
| SSD Kingston NV3 1 ТБ M.2 2280 | **142,89 €** | alternate.de, 14 дн.; bueromarkt-ag.de 143,98; x-kom.de 146,89; alza.de 147,89 (30 дн.) | [204697967](https://www.idealo.de/preisvergleich/OffersOfProduct/204697967_-nv3-1tb-kingston.html) ✅ |
| Lenovo 65W USB-C `4X20M26272` | **22,03 €** | computeruniverse.net (возврат не показан); cyberport.de 22,55 (30 дн.) | [5584731](https://www.idealo.de/preisvergleich/OffersOfProduct/5584731_-65w-usb-c-4x20m26272-lenovo.html) ✅ |
| DDR5 SO-DIMM 16 ГБ — Kingston `KVR56S46BS8-16` | **187,56 €** | маркетплейс (Avanturis, 4,6 ★ / 41), 30 дн. | [213624753](https://www.idealo.de/preisvergleich/OffersOfProduct/213624753_-valueram-16gb-ddr5-5600mhz-cl46-so-dimm-on-die-ecc-kvr56s46bs8-16-kingston.html) |
| DDR5 SO-DIMM 16 ГБ — обычный магазин, Lenovo `4X71M23186` | 206,80 € | notebookkontor.de (OEM bulk), возврат не показан | [205464660](https://www.idealo.de/preisvergleich/OffersOfProduct/205464660_-thinkpad-16gb-ddr5-5600-4x71m23186-lenovo.html) |
| Crucial `CT16G56C46S5` (брал агент поиска) | 248,89 € | alza.de, 30 дн. | [202284828](https://www.idealo.de/preisvergleich/OffersOfProduct/202284828_-16gb-ddr5-5600-cl46-ct16g56c46s5-crucial.html) — не самая дешёвая |

### Опровергнуто / исправлено (сводка)

| Утверждение в candidates-idealo-sweep | Как на самом деле | Источник |
|---|---|---|
| `21KK0074GE` «сейчас ab 1149 € — выше потолка», watch-over-1100 | 1007,99 € (electronic4you.de) в 12:50; но CPU Barcelo-R → reject | [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/203811127_-thinkbook-16-g6-21kk0074ge-lenovo.html), [amd-cpu.md](amd-cpu.md) п. 8 |
| `21UT004EGE` 894 € + SSD = 1036,89 € | 894 € — цена с купоном и без доставки; с купоном 1041,79, без — **1091,89 €** | idealo: «Preis inkl. Gutschein» |
| `21UT004EGE` без оговорок о CPU | Ryzen 5 220 — в списке «Не брать» [amd-cpu.md](amd-cpu.md) | amd-cpu.md п. 8 |
| HP 255R G10: «1×16 + свободный слот, макс. 32 ГБ» | Icecat: «RAM maximal 16 GB»; сервис-мануал: «onboard up to 16 GB, not upgradeable», планки — деталь для сервиса; QuickSpecs: максимум 1×32 | Icecat, [MSG](https://kaas.hpcloud.hp.com/pdf-public/pdf_11296126_en-US-1.pdf), [QuickSpecs](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09053765) |
| HP 255R G10: HEVC «риск» | для HP 200 Series — высокий риск, вывод проекта «HP на AMD — не брать, кроме EliteBook 8» | [hevc-amd.md](hevc-amd.md) п. 10 |
| HP 255R G10 итог 853,89 € | 792,56 € (Kingston 187,56) или 811,80 € (обычный магазин) | idealo |
| HP 255R G10: «250 или 300 нит — не проверено» | 300 нит, 45 % NTSC у обоих SKU | Icecat |
| HP `CJ5Q1EA`: «CPU расходится» | предложение вообще не про этот P/N: «7530U, Win 11 Pro», а P/N — 7535U, FreeDOS | idealo 208126364, Icecat |
| `83HU004KGE`: зарядки нет | подтверждено; даташит idealo («Netzteil 65 Watt») ошибается | PSREF, idealo |

### Известные проблемы (Notebookcheck)

- **IdeaPad Slim 5 16AKP10** — корпус тот же, что у `83HY008CGE` и `83HU004KGE`: в PSREF одинаковы размеры 356,5 × 250,6 × 16,9 мм и вес 1,85 кг. Тест конфигурации AI 5 330 / 2×8, 81 %, 21.11.2025 ([NBC](https://www.notebookcheck.net/Dual-debut-in-the-Lenovo-IdeaPad-Slim-5-16-Ryzen-AI-5-330-and-Radeon-820M-in-review.1166676.0.html)):
  - экран LEN160WUM: **57,6 % sRGB**, 332 нит, ~1060:1, ΔE 5,57, **PWM нет**;
  - под нагрузкой ~42 дБ(A); PL1 25–36 Вт; корпус холодный;
  - дно — 6 винтов Torx; внутри 2 SO-DIMM и 2 M.2 (2280 свободен, SSD в 2242);
  - минусы: слабые динамики, малый цветовой охват, высокие задержки; плюсы: металлический корпус, клавиатура, автономность.
- **IdeaPad Slim 5 16IRH10R** — Intel-сестра в том же корпусе ([NBC](https://www.notebookcheck.net/Lenovo-IdeaPad-Slim-5-16-laptop-review-Intel-Core-i5-vs-AMD-Ryzen-5.1170394.0.html), 01.12.2025): 57,7 % sRGB, засветка в нижних углах, шум до 50,4 дБ(A), «spongy clickpad», тесные порты.
- **ThinkBook 16 G6 ABP** (7530U, 2×8), 86 %, 28.11.2023 ([NBC](https://www.notebookcheck.net/Lenovo-ThinkBook-16-G6-review-The-inexpensive-multimedia-laptop-with-a-Ryzen-7000.774481.0.html)) — для `21KK0074GE`, корпус того же семейства, что G7 ARP / G9 AHP:
  - 59,8 % sRGB, 290 нит, > 1400:1, PWM нет, заметные ореолы по краям;
  - до 41,4 дБ(A);
  - плюсы: RAM, WLAN и SSD меняются; минусы: нет USB4, узкий охват.
  - У тестового экземпляра NBC описал «one M.2-2280 slot», а PSREF у `21KK0074GE` пишет «Two M.2 2280» → при получении проверить.
- **ThinkBook 16 G7 ARP** — отдельного теста NBC нет, только сборник внешних обзоров ([NBC](https://www.notebookcheck.net/Lenovo-ThinkBook-16-G7-ARP.1187767.0.html), 17.12.2025). Плюсы: «Dual RAM slots», «Dual SSD slots». Минусы: «Battery only 45Wh», «60Hz display panel».
- **ThinkBook 16 G9 AHP** — теста NBC не нашёл (поиск по notebookcheck.net / .com, 30.09.2026) → **не проверено**; ближайшие — G6 ABP и G7 ARP выше.
- **HP 255R G10** — теста NBC не нашёл → **не проверено**.
  - Ближайший — HP 255 G10 C07Q0ES (Athlon 7120U, распайка 8 ГБ, TN) ([NBC](https://www.notebookcheck.net/HP-255-G10-with-7120U-review-Small-budget-low-performance.1293092.0.html), 10.05.2026): «housing warps a lot», только USB 5 Гбит/с; дно на 4 винтах и защёлках, вентилятор, SSD и WLAN доступны; 58 % sRGB (TN).

### Что не проверено

- Срок возврата: technik-brandenburg.de (`83HU004KGE`), asaboshisystems.de (HP), electronic4you.de (`21KK0074GE`), computeruniverse.net (зарядка) — idealo не показывает.
- Кто давал минимум 896,28 € у `83HY008CGE`: API не показывает продавца.
- Есть ли физически второй слот SO-DIMM у конкретного экземпляра HP 255R G10 — документы HP расходятся.
- HEVC на Lenovo — только по отсутствию отключений в PSREF; DXVA Checker — в срок возврата.
- Цены `21MW00AYGE` и `21UT004QGE` в этой проверке не перепроверял (взяты из sweep / market-amd).

### Источники

- idealo.de (Chrome пользователя, 30.09.2026, 12:47–12:58): карточки — ссылки в таблицах; история — `https://www.idealo.de/price-chart/sites/1/products/<pid>/history?period=1Y`.
- Lenovo PSREF, PDF-экспорт: [83HY008CGE](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=83HY008CGE&country_code=), [83HU004KGE](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=83HU004KGE&country_code=), [21MW009MGE](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=21MW009MGE&country_code=), [21UT004EGE](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=21UT004EGE&country_code=), [21KK0074GE](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=21KK0074GE&country_code=), [83UU001LGE](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=83UU001LGE&country_code=), [83HY009NGE](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=83HY009NGE&country_code=).
- HP: [QuickSpecs 255R G10 c09053765 v7](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09053765), [Maintenance and Service Guide 255R G10](https://kaas.hpcloud.hp.com/pdf-public/pdf_11296126_en-US-1.pdf), [QuickSpecs EliteBook 665 G11 c08927104 v11](https://www8.hp.com/h20195/V2/GetPDF.aspx/c08927104).
- Icecat open: [CJ5Q2EA](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=HP&ProductCode=CJ5Q2EA), [CJ5Q1EA](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=HP&ProductCode=CJ5Q1EA).
- Notebookcheck: ссылки в разделе «Известные проблемы».
- Проект: [amd-cpu.md](amd-cpu.md), [amd-codecs.md](amd-codecs.md), [hevc-amd.md](hevc-amd.md), [market-amd.md](market-amd.md), [candidates-idealo-sweep.md](candidates-idealo-sweep.md).
