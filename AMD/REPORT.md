# Ноутбук для монтажа 4K: AMD, до 1100 €, Германия

_Отчёт от 30.09.2026. Цены — idealo.de в Chrome пользователя, 30.09.2026: карточка каждого P/N, цена с доставкой, минимум нового товара у любого продавца, маркетплейсы включительно ([правило](../CLAUDE.md)). Цены с купоном и б/у в минимум не входят, они помечены отдельно._
_Критик перепроверил вживую 30.09.2026 в 17:26–17:28: карточки `83HY008CGE`, `21MW00AYGE`, `21UT000RGE`, `3VHK3DE894SH` и Intel `83HS00BLGE`, `21SK007KGE`, `21SK0083GE`; расхождения внесены в текст._
_Сверка с финальным `../Intel/REPORT.md` — 30.09.2026, 18:46–18:47: `83HY008CGE`, Intel `83HS00BLGE`, `MD600023`, `22AY003WGE`, планка и SSD — цены те же, что в Intel-отчёте; зарядка 22,03 → 22,65 €. Цены докупки и правила оценок теперь общие для обоих отчётов._
_Раскладка памяти — по даташитам производителя (Lenovo PSREF, даташиты ASUS, HP QuickSpecs и PartSurfer) и Icecat. Подробности — в `notes/`, вердикты скептиков — в `notes/verify-*.md`. Шкала оценок общая для отчётов AMD и Intel._
_**Версия 3 (30.09.2026, вечер) — пересобрана под новые вводные владельца:** кодек камеры и программа монтажа не будут известны никогда; покупка — сейчас; внешнего монитора не будет; планку и SSD владелец ставит сам; порты — приятный бонус. Цены «купить сейчас» — живые, 19:25–19:32 ([`notes/prices-final.md`](notes/prices-final.md)); экраны — [`notes/displays.md`](notes/displays.md) и проход «от экрана» [`notes/display-sweep.md`](notes/display-sweep.md). «Мощн.» пересчитана у каждой строки по единому составу (см. «Топ-10»), места — заново._

## Итог коротко

**Новые жёсткие критерии (30.09): экран с полным sRGB и оплата наличными — кандидаты этой ветки.**
- **Обновлено 01.10, ночь: в ветке AMD все жёсткие критерии проходят два ноутбука** — Acer Swift Air 16 OLED `NX.DL5EG.002` (ниже он №9) и Lenovo IdeaPad Slim 5 15ARP10 OLED `83J3006GGE` (Ryzen 7 7735HS, 15,1" 2,5K OLED, 32 ГБ; 899 € в MEDIMAX + SSD = 1058,99 €). Общий выбор — Intel Medion `30040202` за 946,99 € ([../REPORT.md](../REPORT.md)); Swift Air — запасной №2, Lenovo — №3.
  - Цена Swift Air — 959,14–999,99 € наличными в 102 рынках expert: резерв на сайте, оплата в магазине ([store-availability.md](notes/store-availability.md)).
  - Для 4K он слабый: Ryzen AI 5 330 (4 ядра, R23 7 840) и Radeon 820M (Time Spy 786) — скорее всего, понадобятся прокси.
- **Топ ниже составлен без этих двух критериев** и для покупки больше не действует. Производительность — [notes/perf-tables.md](notes/perf-tables.md), надёжность и запчасти — [notes/reliability.md](notes/reliability.md).

| P/N | Экран | Итог за наличные | idealo | Средн. |
|---|---|---|---|---|
| ✔ `NX.DL5EG.002` Swift Air 16 OLED R1FY (№9) | OLED; замер LaptopMedia — 100 % sRGB / 100 % DCI-P3 ([LaptopMedia](https://laptopmedia.com/de/review/acer-swift-air-16-sfa16-61m-review-a-16-inch-laptop-that-weighs-under-1-kg/)) | **999,99 €** — expert, оплата в Fachmarkt | [211778543](https://www.idealo.de/preisvergleich/OffersOfProduct/211778543_-swift-air-16-oled-16-wuxga-amd-ryzen-ai-5-32gb-1tb-ssd-silber-nx-dl5eg-002-acer.html) | 5,5 (пересчёт 01.10) |
| ✘ `NX.JP0EG.00Z` Aspire 16 AI OLED R2R1 (№10) | OLED, по даташиту 95–100 % DCI-P3, замера нет; по строгому правилу не подтверждён (у Acer 95 %, а не 100 %) | ✘ до 1100 € наличными нет: Cyberport Store 2539 €, у MEDIMAX 1099 €, но «Barzahlung bei Abholung ist nicht möglich» ([AGB](https://www.medimax.de/agb)); переводом 1081,21 € | [211631508](https://www.idealo.de/preisvergleich/OffersOfProduct/211631508_-aspire-16-ai-a16-61m-r2r1-acer.html) | 4,5 наличными / 5,5 переводом |
| ✘ `SFA16-61M-R559` Swift Air 16 OLED (AI 7 350) | та же панель, что у R1FY | ✘ от 1149 €, выше потолка | [209373389](https://www.idealo.de/preisvergleich/OffersOfProduct/209373389_-swift-air-16-oled-sfa16-61m-r559-acer.html) | — |
| ✘ `83HY008CGE` IdeaPad Slim 5 16AKP10 (№1 ниже) | ✘ 45 % NTSC, замер 57,6 % sRGB ([NBC](https://www.notebookcheck.net/Dual-debut-in-the-Lenovo-IdeaPad-Slim-5-16-Ryzen-AI-5-330-and-Radeon-820M-in-review.1166676.0.html)) | ✘ продавец один — Kaufland МП, наличными нельзя | [209439304](https://www.idealo.de/preisvergleich/OffersOfProduct/209439304_-ideapad-slim-5-16-83hy008cge-lenovo.html) | 7 (переводом) |

**Дальше — итог по старым критериям (без требований к экрану и оплате).**

1. **№1 — IdeaPad Slim 5 16AKP10 `83HY008CGE` за 1059,99 €, средн. 7.** Ryzen AI 7 350 (Zen 5, 8 ядер), Radeon 860M, кодирует AV1; 2×16 ГБ SO-DIMM, 1 ТБ + свободный M.2, 2 года гарантии ([PSREF](https://psref.lenovo.com/Detail/IdeaPad/IdeaPad_Slim_5_16AKP10?M=83HY008CGE)).
   Предложение одно: маркетплейс Kaufland, продаёт expert, возврат 14 дней; в 19:25 — то же ([idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/209439304_-ideapad-slim-5-16-83hy008cge-lenovo.html)). Может исчезнуть.
   Минусы: HEVC 4:2:2 не декодирует (ни один AMD), экран 45 % NTSC — NBC намерил у той же панели 57,6 % sRGB ([`notes/displays.md`](notes/displays.md)).
2. **Дешевле, но слабее — средн. 6,5:**
   - №2 IdeaPad Slim 5 16ARP10 `83HU004KGE` + SSD + зарядка — **920,54 €**: 2×16, 1,5 ТБ, но Zen 3+ и USB-C 5 Гбит/с ([idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/210287882_-ideapad-slim-5-16-83hu004kge-lenovo.html));
   - №3 ThinkBook 16 G7 ARP `21MW00AYGE` — 998,99 €: USB4, SD, RJ45 (бонус), процессор 2022 года; 998,99 € — максимум цены за год ([idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/207306483_-thinkbook-16-g7-21mw00ayge-lenovo.html));
   - №4 ThinkBook 16 G9 AHP `21UT004QGE` — 1071,82 €: самый яркий экран (400 нит), но урезанный Ryzen 5 220;
   - №5 `21MW007VGE` — 1088,57 €; №6 ExpertBook P1 + планка + SSD — 928,61 €;
   - №7 Vivobook S16 `M3607HA-RP017W` + планка — 1006,56 €: самый сильный процессор в бюджете (Ryzen 7 260 + 780M), но 16 ГБ распаяно.
3. **Экран для цвета в 1100 € есть только у Acer — с распаянной памятью и риском с HEVC** ([`notes/display-sweep.md`](notes/display-sweep.md)):
   - №9 Swift Air 16 OLED `NX.DL5EG.002` — 993,50 €: LaptopMedia намерил 100 % DCI-P3, но Ryzen AI 5 330 (4 ядра, 820M) для 4K слабый ([idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/211778543_-swift-air-16-oled-16-wuxga-amd-ryzen-ai-5-32gb-1tb-ssd-silber-nx-dl5eg-002-acer.html));
   - №10 Aspire 16 AI OLED R2R1 `NX.JP0EG.00Z` — 1081,21 €: Ryzen AI 7 350, OLED 95–100 % DCI-P3 по даташиту, но замеров нет и ШИМ не проверен ([idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/211631508_-aspire-16-ai-a16-61m-r2r1-acer.html)).

   С 2×16 или 1×16 + слот и хорошим экраном дешевле 1100 € моделей нет: у всех Lenovo со слотами в продаже — 45 % NTSC, OLED-версии со слотами — 2×8 или дороже 1100 €.
4. **AMD против Intel.** Лучший Intel — IdeaPad Slim 5 16IRH10 `83HS00BLGE` (i7-13620H) за 993,30 € — тоже средн. 7 ([idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/209881995_-ideapad-slim-5-16-83hs00blge-lenovo.html)). Корпус и экран те же.
   AMD дороже на 66,69 €, зато графика в 2,3 раза сильнее (Time Spy 2565 против 1110, [`notes/amd-cpu.md`](notes/amd-cpu.md)) и есть кодирование AV1. Intel аппаратно декодирует HEVC 4:2:2 10 бит, AMD — нет ([`notes/amd-codecs.md`](notes/amd-codecs.md)): при неизвестном навсегда кодеке это ширина декода в пользу Intel.
   Самый дешёвый Intel с 2×16 — Medion `MD600023` за 699,97 € ([idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/208688812_-e15433-md600023-medion.html)): DDR4, HDMI 1.4b, Wi-Fi 5 ([Intel-проверка, п. 4.1](../Intel/notes/browser-check-mem-acer-medion-other.md)).
5. **Ловушки:**
   - HP ProBook 4 G1a `C7SP9ES` за 906,99 € — аппаратный HEVC выключен ([QuickSpecs c09111176](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09111176));
   - ThinkPad E16 Gen 3 AMD с «32 ГБ» — это одна планка 1×32 ([PSREF](https://psref.lenovo.com/Detail/ThinkPad/ThinkPad_E16_Gen_3_AMD?M=21ST004GGE));
   - Ryzen 7x30 (Barcelo-R) — кремний 2021 года под новым именем ([`notes/amd-cpu.md`](notes/amd-cpu.md)).
   Ryzen 5 220 (в №4) — урезанный Hawk Point, Ryzen AI 5 330 (в №9) — 4 ядра: для 4K оба слабые.
6. **AMD + RTX 50** декодирует всё, включая 4:2:2 ([NVIDIA](https://docs.nvidia.com/video-technologies/video-codec-sdk/13.0/nvdec-video-decoder-api-prog-guide/index.html)). Ближе всех — Gigabyte GAMING A16 `3VHK3DE894SH`: с планкой 1286,56 € ([idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/207329496_-gaming-a16-3vhk3de894sh-gigabyte.html)). Это справка: покупка сейчас, а в 1100 € он войдёт, только если ноутбук подешевеет до 912 € — за год такого не было ([`notes/verify-gpu.md`](notes/verify-gpu.md)).

**Итоговый выбор по обеим веткам (01.10, ночь) — Intel Medion SPRCHRGD 16 S1 OLED `30040202`, 946,99 € наличными в expert Bad Salzungen (1 шт., сначала звонок); запасные — AMD Swift Air `NX.DL5EG.002` и Lenovo `83J3006GGE`** — см. [`../REPORT.md`](../REPORT.md). Прежний выбор 30.09 — HP OmniBook 7 16 — отменён: экран 62,5 % sRGB, наличными не купить ([архив](notes/report-2026-09-30-hp.md)).

## Топ-10

> Таблица — на 30.09, до ночной проверки. После неё у Swift Air R1FY Ремонт 3,5 и Цена 7,5 (959,14 € наличными, expert Schmalkalden), у Aspire R2R1 Ремонт 4 и Цена 5 (1099 € наличными в MEDIMAX Nettetal); Средняя у обоих 5,5. Актуальные оценки всех ноутбуков — на [странице](https://elderlydoomer.github.io/notebook-4k-germany/page/laptops.html), итоговый выбор — в [../REPORT.md](../REPORT.md).

Оценки 1–10 (10 — лучше), шкала общая для отчётов AMD и Intel:
- **Проблемность:** 10 = меньше всего проблем. Учитывает надёжность бренда, болячки из обзоров, риск отключённого HEVC (HP, Dell, Acer).
- **Ремонт:** слоты памяти, второй M.2 (распайка — ниже), мануалы, запчасти, гарантия.
- **Цена** (итог с планкой, SSD и зарядкой): ≤ 700 € → 10; от 700 до 1000 € — минус 1 за каждые 100 €; от 1000 до 1100 € — минус 1 за каждые 50 € (7 → 5); выше 1100 € — минус 1 за каждые 50 € (минимум 1). Округление до 0,5.
- **Порт.:** вес и батарея.
- **Мощн. (новый состав с 30.09, вечер; общий с `../Intel/REPORT.md`)** = 0,35 × процессор + 0,35 × графика и медиадвижок + 0,25 × экран + 0,05 × порты, округление до 0,5. Подоценки 1–10:
  - **процессор** (многопоток, устойчивость) — Cinebench R23 Multi, медиана NBC ([список NBC](https://www.notebookcheck.net/Mobile-Processors-Benchmark-List.2436.0.html), снят 30.09.2026) / 2000, но не больше 10; −0,5, если у этого SKU известен лимит (DDR4 или блок 65 Вт на H-процессоре, перегрев в обзоре);
  - **графика и медиадвижок** — среднее двух баллов. iGPU = Time Spy Graphics, среднее NBC ([список NBC](https://www.notebookcheck.net/Mobile-Graphics-Cards-Benchmark-List.844.0.html)) / 500, не больше 10. Медиадвижок — при неизвестном кодеке ценится ширина декода: 10 — RTX 50 (H.264 и HEVC 4:2:2 + AV1); 9 — Intel Panther Lake; 8 — Intel Meteor, Arrow и Lunar Lake (HEVC 4:2:2 + AV1); 6,5 — Intel Raptor Lake (HEVC 4:2:2 без AV1); 5 — AMD Phoenix и новее (кодирует AV1, 4:2:2 не декодирует); 3,5 — AMD Rembrandt (ни 4:2:2, ни AV1-кодирования). Источники — «Кодеки и камера» и [`notes/amd-codecs.md`](notes/amd-codecs.md);
  - **экран** — по [`notes/displays.md`](notes/displays.md), главное — охват: IPS «45 % NTSC» (NBC намеряет 50–63 % sRGB) — 3; охват не опубликован — 2,5; 62,5 % sRGB по даташиту — 3,5; IPS 100 % sRGB или OLED 95–100 % DCI-P3 по даташиту — 8. Поправки по 0,5: + независимый замер ≥ 99 % sRGB; + яркость ≥ 400 нит; + разрешение выше WUXGA; − 15,6" FHD 16:9; − OLED без проверки ШИМ; − сильный глянец;
  - **порты — бонус**: 10 — USB4/TB4 + HDMI 2.1 + SD + RJ45; 9 — TB4 + HDMI 2.1 + RJ45; 8 — USB4 + HDMI + microSD или RJ45; 7 — TB4/USB4 + HDMI 2.1; 6 — USB-C 10 Гбит/с с DP + HDMI 2.1 + microSD; 5 — USB-C с DP + HDMI 2.1; 4 — USB-C 5 Гбит/с + HDMI 1.4b или без кардридера; 3 — HDMI 1.4b и один USB-C; 2 — USB-C 2.0 без видео.
- **Средн.** — среднее пяти, округлено до 0,5.
- **Общие правила с `../Intel/REPORT.md`:**
  - графика, драйверы которой уже только в поддержке (AMD RDNA 2 — maintenance mode с 10.2025, Intel 11–14-го поколений — legacy с 19.09.2025), — −0,5 к Пробл. против того же корпуса с актуальными драйверами. Intel-якоря IdeaPad 16IRH10 и Aspire Go 16 — уже с legacy-драйверами;
  - зарядку, которую надо докупить, считаем в цене, а Порт. за неё не снижаем;
  - цены докупки одни и те же — таблица «Цены докупки» ниже;
  - «+ SSD» и «+ планка» — полноценные варианты: владелец ставит их сам (с 30.09, вечер).

Якоря шкалы — из прежней (29.09) версии `../Intel/REPORT.md`; в новой [`../Intel/REPORT.md`](../Intel/REPORT.md) они перечислены в разделе «Топ-10» (Пробл. / Ремонт / Порт. / Мощн.). **«Мощн.» якорей пересчитана 30.09 вечером по новому составу**, остальное прежнее:

| Intel-модель | Пробл. | Ремонт | Порт. | Мощн. (было → стало) |
|---|---|---|---|---|
| IdeaPad Slim 5 16IRH10, i7-13620H, 2×16 | 6,5 | 8,5 | 7 | 4 → **5** |
| ThinkBook 16 G8, 255H | 7,5 | 8,5 | 7 | 7 → **7** |
| ThinkPad E16 G3, 228V, распайка, 100 % sRGB | 7,5 | 5 | 8,5 | 8 → **7** |
| Acer Aspire Go 16, i9 | 4 | 6 | 7,5 | 5 → **5,5** |

**Как отбирал.** В топ попали 10 лучших по «Средн.» SKU, которые можно купить сейчас с итогом ≤ 1100 €. «Ждать» — только справка в конце топа. Из почти одинаковых SKU беру один, остальные — «варианты» при нём.

### Можно купить сейчас (итог ≤ 1100 €)

| # | Модель · парт-номер (карточка idealo) | Итог | Пробл. | Ремонт | Цена | Порт. | Мощн. | Средн. |
|---|---|---|---|---|---|---|---|---|
| 1 | Lenovo IdeaPad Slim 5 16AKP10 · [`83HY008CGE`](https://www.idealo.de/preisvergleich/OffersOfProduct/209439304_-ideapad-slim-5-16-83hy008cge-lenovo.html) | 1059,99 € | 7 | 8,5 | 6 | 7 | 5,5 | **7** |
| 2 | Lenovo IdeaPad Slim 5 16ARP10 · [`83HU004KGE`](https://www.idealo.de/preisvergleich/OffersOfProduct/210287882_-ideapad-slim-5-16-83hu004kge-lenovo.html) + SSD + зарядка | 920,54 € | 6,5 | 8,5 | 8 | 7 | 3,5 | **6,5** |
| 3 | Lenovo ThinkBook 16 G7 ARP · [`21MW00AYGE`](https://www.idealo.de/preisvergleich/OffersOfProduct/207306483_-thinkbook-16-g7-21mw00ayge-lenovo.html) | 998,99 € | 7 | 8,5 | 7 | 7 | 4 | **6,5** |
| 4 | Lenovo ThinkBook 16 G9 AHP · [`21UT004QGE`](https://www.idealo.de/preisvergleich/OffersOfProduct/209122445_-thinkbook-16-g9-21ut004qge-lenovo.html) | 1071,82 € | 7,5 | 8,5 | 5,5 | 7 | 4,5 | **6,5** |
| 5 | Lenovo ThinkBook 16 G7 ARP · [`21MW007VGE`](https://www.idealo.de/preisvergleich/OffersOfProduct/207306221_-thinkbook-16-g7-21mw007vge-lenovo.html) | 1088,57 € | 7 | 8,5 | 5 | 7 | 5 | **6,5** |
| 6 | ASUS ExpertBook P1 PM1503CDA · [`PM1503CDA-S70264X`](https://www.idealo.de/preisvergleich/OffersOfProduct/209457310_-expertbook-p1-pm1503cda-s70264x-asus.html) + планка + замена SSD | 928,61 € | 7 | 7,5 | 7,5 | 7 | 3,5 | **6,5** |
| 7 | ASUS Vivobook S16 M3607HA · [`M3607HA-RP017W`](https://www.idealo.de/preisvergleich/OffersOfProduct/206751394_-vivobook-s16-m3607ha-rp017w-asus.html) — 16 ГБ распаяно + планка | 1006,56 € | 6 | 5 | 7 | 7,5 | 6 | **6,5** |
| 8 | Lenovo V15 G6 ARP · [`83UU001LGE`](https://www.idealo.de/preisvergleich/OffersOfProduct/209094412_-v15-g6-83uu001lge-lenovo.html) + замена SSD | 910,94 € | 6 | 6,5 | 8 | 6,5 | 3,5 | **6** |
| 9 | Acer Swift Air 16 OLED SFA16-61M-R1FY · [`NX.DL5EG.002`](https://www.idealo.de/preisvergleich/OffersOfProduct/211778543_-swift-air-16-oled-16-wuxga-amd-ryzen-ai-5-32gb-1tb-ssd-silber-nx-dl5eg-002-acer.html) — 32 ГБ распаяно | 993,50 € | 4,5 | 3 | 7 | 8,5 | 4,5 | **5,5** |
| 10 | Acer Aspire 16 AI OLED A16-61M-R2R1 · [`NX.JP0EG.00Z`](https://www.idealo.de/preisvergleich/OffersOfProduct/211631508_-aspire-16-ai-a16-61m-r2r1-acer.html) — 32 ГБ распаяно | 1081,21 € | 4 | 3 | 5,5 | 8 | 6,5 | **5,5** |

Порядок: сначала средняя оценка; при равной — сначала 2×16 (с завода или + SSD), потом 1×16 + слот + планка, потом распайка (в том числе 16 распаяно + планка); внутри группы — по неокруглённой средней, затем дешевле.
Средние без округления: 6,8 · 6,7 · 6,7 · 6,6 · 6,5 · 6,5 · 6,3 · 6,1 · 5,5 · 5,4. У №2 и №3 они равны (6,7) — выше №2, он дешевле на 78,45 €.
Это правило общее с `../Intel/REPORT.md`.
Живые цены — 19:25–19:28, изменилась только у №4 (1072,00 → 1071,82 €) ([`notes/prices-final.md`](notes/prices-final.md)); №9 — 30.09 вечером ([`notes/display-sweep.md`](notes/display-sweep.md)); в 20:50 он подешевел с 999 до 993,50 € (expert), оценки те же.

**Из чего сложена «Мощн.»** (процессор · графика и медиадвижок · экран · порты-бонус → Мощн.; «было» — до 30.09, вечер):

| # | Процессор: R23 → балл | iGPU: Time Spy → балл · медиадвижок | Экран (displays.md) | Порты | Мощн.: было → стало |
|---|---|---|---|---|---|
| 1 | Ryzen AI 7 350 16 015 → 8,0 | 860M 2565 → 5,1 · 5 → **5,1** | 3 — 45 % NTSC, NBC 57,6 % sRGB | 6 | 6 → **5,5** |
| 2 | Ryzen 5 7535HS 8613 (n3) → 4,3 | 660M 1535 → 3,1 · 3,5 → **3,3** | 3 — 45 % NTSC, панель как у №1 | 5 | 3,5 → **3,5** |
| 3 | Ryzen 5 7535HS → 4,3 | 660M → **3,3** | 3 — 45 % NTSC, у G6/G7 того же корпуса 59,8–61,2 % sRGB | 10 | 4 → **4** |
| 4 | Ryzen 5 220 = 8540U 9722 (n2) → 4,9 | 740M 1527 → 3,1 · 5 → **4,0** | 3,5 — 45 % NTSC, 400 нит | 10 | 4,5 → **4,5** |
| 5 | Ryzen 7 7735HS 13 106 → 6,6 | 680M 2303 → 4,6 · 3,5 → **4,1** | 3 — 45 % NTSC | 10 | 5 → **5** |
| 6 | Ryzen 5 150 = 7535HS → 4,3 | 660M → **3,3** | 2,5 — 15,6" FHD, 45 % NTSC (у Intel-сестры — 63,3 % sRGB) | 4 | 3 → **3,5** |
| 7 | Ryzen 7 260 17 212 → 8,6 | 780M 2808 → 5,6 · 5 → **5,3** | 3 — 45 % NTSC, 144 Гц | 4 | 6 → **6** |
| 8 | Ryzen 5 150 = 7535HS → 4,3 | 660M → **3,3** | 2,5 — 15,6" FHD, 45 % NTSC | 3 | — → **3,5** |
| 9 | Ryzen AI 5 330 7840 → 3,9 | 820M 786 → 1,6 · 5 → **3,3** | 8 — OLED, замер 100 % DCI-P3 (+0,5), сильный глянец (−0,5) | 3 | — → **4,5** |
| 10 | Ryzen AI 7 350 → 8,0 | 860M → **5,1** | 7 — OLED 95–100 % DCI-P3 по даташиту, ШИМ не проверен (−0,5), глянец (−0,5) | 8 | 7 → **6,5** |
| 11 | Ryzen 7 250 14 676 → 7,3 | 780M → 5,6 · 5 → **5,3** | 3,5 — 45 % NTSC, 400 нит | 10 | 6 → **6** |
| 12 | Ryzen 7 260 → 8,6 | RTX 5060 11 937 → 10 · 10 → **10** | 3 — 52–60 % sRGB (3DNews, LaptopMedia) | 8 | 8,5 → **7,5** |

У Ryzen 5 150 и Ryzen 5 220 в списке NBC нет R23 — взяты их двойники 7535HS и 8540U ([`notes/amd-cpu.md`](notes/amd-cpu.md), раздел 1.4). Значения — медианы и средние NBC по разным ноутбукам; разброс внутри одной модели — ±20–45 % ([`notes/amd-cpu.md`](notes/amd-cpu.md), раздел 3). Медиана i7-13620H в списке NBC на вечер 30.09 — 15 176 (n7; днём было 15 953).

Варианты тех же моделей разобраны в «Кандидатах подробно» (Пробл. / Ремонт / Цена / Порт. / Мощн. → Средн.):
- `21MW009MGE` + SSD (1069,99 €) — при №3: 7 / 8,5 / 5,5 / 7 / 4 → 6,5;
- `21UT004EGE` + SSD (1069,99 €) — при №4: 7,5 / 8,5 / 5,5 / 7 / 4,5 → 6,5;
- `PM1503CDA-S70262` + планка + замена SSD (1044,43 €) — при №6: 7 / 7,5 / 6 / 7 / 4,5 → 6,5;
- `M1607GA-MB020W` + планка (994,55 €) — при №7: 5,5 / 5 / 7 / 7 / 4 → 5,5;
- Acer R8T1 `NX.JLLEG.009` (1080,25 €) — при №10: 4 / 3 / 5,5 / 8 / 5,5 → 5.

### Ждать — справка (покупка сейчас — не рассматриваем)

| # | Модель · парт-номер (карточка idealo) | Сейчас | Мин. за полгода | Пробл. | Ремонт | Цена | Порт. | Мощн. | Средн. |
|---|---|---|---|---|---|---|---|---|---|
| 11 | Lenovo ThinkBook 16 G9 AHP · [`21UT000RGE`](https://www.idealo.de/preisvergleich/OffersOfProduct/209122441_-thinkbook-16-g9-21ut000rge-lenovo.html) | 1188,97 € | 1109,82 € (21.09.2026, дневной минимум «ab»); ≤ 1100 € — ни одного дня из 182. За год — 1045 € (21.01.2026) | 7,5 | 8,5 | 3 | 7 | 6 | **6,5** |
| 12 | Gigabyte GAMING A16 (RTX 5060) · [`3VHK3DE894SH`](https://www.idealo.de/preisvergleich/OffersOfProduct/207329496_-gaming-a16-3vhk3de894sh-gigabyte.html) + планка | 1286,56 € | 1079 € (03–05.09.2026) → с планкой 1266,56 € | 6 | 7 | 1,5 | 6 | 7,5 | **5,5** |

Цены в 19:29 — те же ([`notes/prices-final.md`](notes/prices-final.md)).

### Цены докупки (idealo, 30.09.2026, с доставкой)

| Что | Цена | Магазин · возврат | Карточка |
|---|---|---|---|
| SSD 1 ТБ NVMe M.2 2280 — Verbatim Vi3000 (PCIe 3.0) | **120,99 €** | notebooksbilliger.de · 30 дн. | [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/202702551_-vi3000-1tb-verbatim.html) |
| SSD 1 ТБ PCIe 4.0 — Silicon Power UD90 / Kingston NV3 | 138,97 / 142,89 € | siliconpowereu.com / alternate.de (14 дн.) | [UD90](https://www.idealo.de/preisvergleich/OffersOfProduct/202130035_-ud90-1tb-m-2-silicon-power.html), [NV3](https://www.idealo.de/preisvergleich/OffersOfProduct/204697967_-nv3-1tb-kingston.html) |
| SSD 1 ТБ M.2 **2230** (второй слот ExpertBook P1) — UD90 | 219,97 € (было 227,20 €) | siliconpowereu.com; Kaufland, маркетплейс — 227,20 € (14 дн.) | [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/203279966_-ud90-1tb-m-2-2230-silicon-power.html) |
| Планка DDR5-5600 16 ГБ — Kingston KVR56S46BS8-16 | **187,56 €** | Galaxus, маркетплейс · 30 дн. — **одно предложение**, до 25.09 стоила 396–426 € | [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/213624753_-valueram-16gb-ddr5-5600mhz-cl46-so-dimm-on-die-ecc-kvr56s46bs8-16-kingston.html) |
| Запасная планка — Lenovo 4X71M23186 | 206,80 € (+19,24 € к итогу) | notebookkontor.de («ABVERKAUF, nur noch wenige»); дальше Patriot PSD516G560081S — 238,89 €, Corsair CMSX16GX5M1A5600C48 — 239,99 € | [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/205464660_-thinkpad-16gb-ddr5-5600-4x71m23186-lenovo.html) |
| Зарядка Lenovo 65 Вт USB-C 4X20M26272 | 22,65 € (18:46 и 19:30; днём было 22,03 €) | computeruniverse.net, cyberport.de · 30 дн. | [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/5584731_-65w-usb-c-4x20m26272-lenovo.html) |

Источники цен докупки — [`notes/verify-lenovo.md`](notes/verify-lenovo.md), [`notes/verify-other-brands.md`](notes/verify-other-brands.md); SSD, планка и зарядка перепроверены 30.09 в 18:46–18:47 и в 19:29–19:32 ([`notes/prices-final.md`](notes/prices-final.md)). Эти же цены — в `../Intel/REPORT.md`. SSD за год подорожал в 3,4 раза: NV3 год назад стоил 42 €.

## Кандидаты подробно

### 1. Lenovo IdeaPad Slim 5 16AKP10 — `83HY008CGE` · 1059,99 €
- **Процессор:** Ryzen AI 7 350 — Krackan Point, 4 Zen 5 + 4 Zen 5c, 8 ядер / 16 потоков ([amd.com](https://www.amd.com/en/products/processors/laptop/ryzen/ai-300-series/amd-ryzen-ai-7-350.html)).
  - Графика Radeon 860M (8 CU, RDNA 3.5), медиадвижок VCN 4.0.5: декодирует и **кодирует AV1**, 4:2:2 не декодирует ([`notes/amd-codecs.md`](notes/amd-codecs.md)).
  - Cinebench R23 Multi — 16 015, на уровне i7-13620H (15 176) ([NBC](https://www.notebookcheck.net/Mobile-Processors-Benchmark-List.2436.0.html)).
- **Память:** 2×16 ГБ SO-DIMM DDR5-5600, два слота; «Up to 32GB» — [PSREF](https://psref.lenovo.com/Detail/IdeaPad/IdeaPad_Slim_5_16AKP10?M=83HY008CGE), [PDF](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=83HY008CGE&country_code=), [Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Lenovo&ProductCode=83HY008CGE) («Speicherlayout 2 x 16 GB»).
- **SSD:** 1 ТБ M.2 2242 + свободный M.2 2280. NBC при вскрытии того же корпуса: «The 2280 slot is free» ([NBC](https://www.notebookcheck.net/Dual-debut-in-the-Lenovo-IdeaPad-Slim-5-16-Ryzen-AI-5-330-and-Radeon-820M-in-review.1166676.0.html)).
- **Экран:** 16" 1920×1200 IPS, 300 нит, 45 % NTSC, 60 Гц ([PSREF](https://psref.lenovo.com/Detail/IdeaPad/IdeaPad_Slim_5_16AKP10?M=83HY008CGE)). У той же панели NBC намерил 57,6 % sRGB, 39,1 % DCI-P3, 349 нит, 1058:1, ШИМ нет ([NBC](https://www.notebookcheck.net/Dual-debut-in-the-Lenovo-IdeaPad-Slim-5-16-Ryzen-AI-5-330-and-Radeon-820M-in-review.1166676.0.html), [`notes/displays.md`](notes/displays.md)). Для цвета слабо: насыщенные цвета будут бледнее, чем их увидит зритель.
- **Порты (бонус):** 2× USB-C 10 Гбит/с (PD, DP 1.4), 2× USB-A 5 Гбит/с, HDMI 2.1 (4K60), microSD. USB4 и Ethernet нет ([PSREF](https://psref.lenovo.com/Detail/IdeaPad/IdeaPad_Slim_5_16AKP10?M=83HY008CGE); HDMI 2.1 «up to 4K/60Hz» — перепроверено критиком 30.09).
- **Вес и батарея:** 1,85 кг, 60 Втч, зарядка 65 Вт в комплекте. **Гарантия** 2 года ([PSREF](https://psref.lenovo.com/Detail/IdeaPad/IdeaPad_Slim_5_16AKP10?M=83HY008CGE): «Base Warranty 2-year»).
- **Цена:** 1059,99 € на Kaufland, маркетплейс (продавец expertDeutschland, возврат 14 дней), 30.09.2026 — [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/209439304_-ideapad-slim-5-16-83hy008cge-lenovo.html). Критик в 17:26: то же, предложение по-прежнему одно.
  За год минимум 896,28 € (23.02.2026), средняя 952,23 €; все 179 дней карточки цена была ≤ 1100 € ([`notes/verify-lenovo.md`](notes/verify-lenovo.md)). Минимум за полгода — 897,00 € (09.07.2026, API idealo `period=6M`, 17:26). В 19:25 — 1059,99 €, предложение по-прежнему одно ([`notes/prices-final.md`](notes/prices-final.md)).
- **Обзор того же корпуса** ([NBC](https://www.notebookcheck.net/Dual-debut-in-the-Lenovo-IdeaPad-Slim-5-16-Ryzen-AI-5-330-and-Radeon-820M-in-review.1166676.0.html), версия с AI 5 330, 21.11.2025):
  - под нагрузкой 42 дБ(A), корпус холодный, металлический;
  - минусы — слабые динамики, узкий охват экрана, «high latencies» (задержки DPC, проверить LatencyMon).
- **Оценки:**
  - Пробл. 7 — Intel-якорь того же корпуса 16IRH10 — 6,5 с legacy-драйверами графики, а у 860M драйверы актуальные (+0,5, общее правило). Корпус тише и холоднее Intel-сестры (42 против 50,4 дБ(A); у неё 96 °C, [Intel-проверка, п. 5.19](../Intel/notes/browser-check-reviews-forums.md)), но NBC отметил высокие DPC-задержки — плюс и минус гасятся. Отключений HEVC у Lenovo не найдено ([`notes/hevc-amd.md`](notes/hevc-amd.md));
  - Ремонт 8,5 — как у якоря: 2 слота, второй M.2, 2 года гарантии;
  - Цена 6 — 1059,99 €;
  - Порт. 7 — 1,85 кг, 60 Втч;
  - Мощн. 6 → 5,5: процессор 8,0 (R23 16 015), графика и медиадвижок 5,1 (860M — Time Spy 2565, кодирует AV1, 4:2:2 не декодирует), экран 3 (45 % NTSC), порты — бонус 6 (HDMI 2.1, USB-C 10 Гбит/с, microSD).
  - Средн. 6,8 → **7** (было 7).
- **Почему №1:** единственный Zen 5 с 2×16 и 1 ТБ в бюджете. Риск — один продавец: брать быстро (покупка сейчас), перед заказом проверить, что предложение ещё есть.

### 2. Lenovo IdeaPad Slim 5 16ARP10 — `83HU004KGE` · 920,54 € (+ SSD + зарядка)
- **Процессор:** Ryzen 5 7535HS, графика 660M — как у №3.
- **Память:** 2×16 ГБ SO-DIMM. PSREF: «Installed memory is actually DDR5-5600 but runs as DDR5-4800» — [PSREF](https://psref.lenovo.com/Detail/IdeaPad/IdeaPad_Slim_5_16ARP10?M=83HU004KGE), [Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Lenovo&ProductCode=83HU004KGE).
- **SSD:** 512 ГБ M.2 2242 + свободный M.2 2280 ([PSREF](https://psref.lenovo.com/Detail/IdeaPad/IdeaPad_Slim_5_16ARP10?M=83HU004KGE)).
- **Зарядки в комплекте нет:** PSREF «No Power Adapter», Icecat «AC-Netzadapter: Nein» ([`notes/verify-lenovo.md`](notes/verify-lenovo.md)). Даташит idealo («65 Watt») ошибается.
- **Экран:** 16" WUXGA IPS, 300 нит, 45 % NTSC — панель как у №1 (NBC: 57,6 % sRGB, ШИМ нет) ([PSREF](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=83HU004KGE&country_code=DE), [`notes/displays.md`](notes/displays.md)).
- **Порты (бонус) слабые:** 2× USB-C **5 Гбит/с** (PD, DP 1.4), HDMI 2.1, microSD. USB4 и RJ45 нет ([PSREF](https://psref.lenovo.com/Detail/IdeaPad/IdeaPad_Slim_5_16ARP10?M=83HU004KGE)).
- **Корпус** как у №1: 1,85 кг, 60 Втч. **Гарантия** 2 года ([`notes/verify-lenovo.md`](notes/verify-lenovo.md)).
- **Цена:** 776,90 € у technik-brandenburg.de (срок возврата не показан), в 19:26 — то же; 799 € у expert.de (14 дней) — [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/210287882_-ideapad-slim-5-16-83hu004kge-lenovo.html). Минимум за год — 699 € (20.05.2026).
- **Итог:** 776,90 + SSD 120,99 + зарядка 22,65 = **920,54 €**, диск 1,5 ТБ. У expert.de — 942,64 €.
- **Оценки:**
  - Пробл. 6,5 — как у Intel-якоря 16IRH10: тот же корпус IdeaPad, драйверы графики тоже только в поддержке (RDNA 2 — maintenance mode, у Intel — legacy);
  - Ремонт 8,5;
  - Цена 8 — 920,54 €;
  - Порт. 7;
  - Мощн. 3,5 → 3,5: процессор 4,3 (R23 7535HS — 8613), графика и медиадвижок 3,3 (660M — Time Spy 1535, ни 4:2:2, ни AV1-кодирования), экран 3 (45 % NTSC), порты — бонус 5 (USB-C 5 Гбит/с, HDMI 2.1, microSD).
  - Средн. 6,7 → **6,5** (было 6,5). Выше №3 при равной неокруглённой средней — дешевле на 78,45 €.

### 3. Lenovo ThinkBook 16 G7 ARP — `21MW00AYGE` · 998,99 € (вариант `21MW009MGE`)
- **Процессор:** Ryzen 5 7535HS — Rembrandt-R, Zen 3+, 6 ядер, 2022 год ([amd.com](https://www.amd.com/en/products/processors/laptop/ryzen/7000-series/amd-ryzen-5-7535hs.html)).
  - Графика 660M (6 CU, RDNA 2). С 10.2025 драйверы RDNA 2 в режиме «maintenance mode» ([AMD](https://www.amd.com/en/resources/support-articles/release-notes/RN-RAD-WIN-25-10-2.html)).
  - VCN 3.1: AV1 только декодирует, не кодирует ([`notes/amd-codecs.md`](notes/amd-codecs.md)).
- **Память:** 2×16 ГБ SO-DIMM DDR5-4800, до 64 ГБ — [PSREF](https://psref.lenovo.com/Detail/ThinkBook/ThinkBook_16_G7_ARP?M=21MW00AYGE), [Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Lenovo&ProductCode=21MW00AYGE).
- **SSD:** 1 ТБ + второй свободный M.2 2280 («for user self-expansion», [PSREF](https://psref.lenovo.com/Detail/ThinkBook/ThinkBook_16_G7_ARP?M=21MW00AYGE)).
- **Экран:** 16" WUXGA IPS 300 нит, 45 % NTSC, 60 Гц ([PSREF](https://psref.lenovo.com/Detail/ThinkBook/ThinkBook_16_G7_ARP?M=21MW00AYGE)). Своего теста нет; у G6 ABP и G7 IML того же корпуса NBC намерил 59,8 и 61,2 % sRGB, ШИМ нет ([`notes/displays.md`](notes/displays.md)).
- **Порты (бонус):** USB4 40 Гбит/с, USB-C 10 Гбит/с, HDMI 2.1, полноразмерный SD, RJ45, 2× USB-A ([PSREF](https://psref.lenovo.com/Detail/ThinkBook/ThinkBook_16_G7_ARP?M=21MW00AYGE)). Лучше только у G9 AHP (№4, №11): там два USB4.
- **Вес и батарея:** 1,7 кг, 45 Втч (маловато), 65 Вт в комплекте. **Гарантия** 1 год ([`notes/verify-lenovo.md`](notes/verify-lenovo.md)).
- **Цена:** 998,99 € у easynotebooks.de (возврат 14 дней); 999,00 € у notebook.de; 15 предложений (критик, 17:26) — [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/207306483_-thinkbook-16-g7-21mw00ayge-lenovo.html).
  Сейчас это **максимум года**: минимум 731,36 € (12.12.2025), за полгода — 833,81 € (06.05.2026; критик перепроверил API `period=6M` в 17:26).
- **Обзоры:** своего теста у NBC нет, только сборник: «Battery only 45Wh», «60Hz display» ([NBC](https://www.notebookcheck.net/Lenovo-ThinkBook-16-G7-ARP.1187767.0.html)).
  У предшественника G6 ABP того же корпуса — 59,8 % sRGB и 41,4 дБ(A) ([NBC](https://www.notebookcheck.net/Lenovo-ThinkBook-16-G6-review-The-inexpensive-multimedia-laptop-with-a-Ryzen-7000.774481.0.html)).
- **Оценки:**
  - Пробл. 7 — экосистема ThinkBook (якорь 7,5), минус 0,5 за графику в maintenance mode;
  - Ремонт 8,5 — 2 слота до 64 ГБ, два M.2 2280;
  - Цена 7 — 998,99 €;
  - Порт. 7 — 1,7 кг, 45 Втч, как у ThinkBook-якоря;
  - Мощн. 4 → 4: процессор 4,3 (R23 7535HS — 8613), графика и медиадвижок 3,3 (660M, ни 4:2:2, ни AV1-кодирования), экран 3 (45 % NTSC), порты — бонус 10 (USB4, HDMI 2.1, SD, RJ45).
  - Средн. 6,7 → **6,5** (было 6,5).
- **Вариант `21MW009MGE` (+ SSD)** — тот же ноутбук, но 512 ГБ. 949 € (easynotebooks.de, 14 дней; в 19:26 — то же) + SSD 120,99 € = **1069,99 €**.
  Дороже `21MW00AYGE` на 71 €, смысл — только в 1,5 ТБ — [PSREF](https://psref.lenovo.com/Detail/ThinkBook/ThinkBook_16_G7_ARP?M=21MW009MGE), [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/206598202_-thinkbook-16-g7-21mw009mge-lenovo.html).
  Оценки: 7 / 8,5 / 5,5 / 7 / 4 (Мощн. как у №3), средняя 6,4 → 6,5.

### 4. Lenovo ThinkBook 16 G9 AHP — `21UT004QGE` · 1071,82 € (вариант `21UT004EGE`)
- **Процессор:** Ryzen 5 220 — это Hawk Point (= 8540U): 2 полных ядра Zen 4 + 4 компактных Zen 4c, графика 740M (4 CU) ([amd.com](https://www.amd.com/en/products/processors/laptop/ryzen/200-series/amd-ryzen-5-220.html)).
  - **Урезанный:** в [`notes/amd-cpu.md`](notes/amd-cpu.md) он в списке «не брать» — для 4K слабый.
  - Медиадвижок современный (VCN 4.0.2): кодирует AV1.
- **Память:** 2×16 ГБ SO-DIMM DDR5-5600, до 64 ГБ — [PSREF](https://psref.lenovo.com/Detail/ThinkBook/ThinkBook_16_G9_AHP?M=21UT004QGE).
- **SSD:** 1 ТБ M.2 2242 + свободный M.2 2280 ([PSREF](https://psref.lenovo.com/Detail/ThinkBook/ThinkBook_16_G9_AHP?M=21UT004QGE)).
- **Экран:** WUXGA IPS **400 нит**, 45 % NTSC, 60 Гц ([PSREF](https://psref.lenovo.com/Detail/ThinkBook/ThinkBook_16_G9_AHP?M=21UT004QGE)). Самый яркий в топе. Тестов G9 нет; та же спецификация Lenovo в ThinkPad L16 G2 AMD дала 52,9 % sRGB, 449 нит, 1760:1, ШИМ нет ([`notes/displays.md`](notes/displays.md)).
- **Порты (бонус):** 2× USB4 40 Гбит/с, HDMI 2.1, SD, RJ45 ([PSREF](https://psref.lenovo.com/Detail/ThinkBook/ThinkBook_16_G9_AHP?M=21UT004QGE)).
- **Вес и батарея:** 1,7 кг, 48 Втч, 65 Вт в комплекте. **Гарантия** 1 год ([`notes/verify-lenovo.md`](notes/verify-lenovo.md)).
- **Цена:** **1071,82 € у easynotebooks.de в 19:25** (14 дней; днём было 1072,00 €) — [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/209122445_-thinkbook-16-g9-21ut004qge-lenovo.html), [`notes/prices-final.md`](notes/prices-final.md). Купонные 1071,00–1071,73 € (c-nw, technikdeals24, heinzsoft) в минимум не входят.
  С 21.01.2026 минимум 999 €, ≤ 1100 € — 52 дня из 182.
- **Обзоры:** тестов G9 нет — NBC 29.05.2026: «Es musste sich noch kein G9-Modell … unseren Tests stellen» ([NBC](https://www.notebookcheck.com/Lenovo-ThinkBook-16-G9-mit-Ryzen-7-Zen-4-32-GB-RAM-1-TB-SSD-im-Angebot.1310427.0.html)).
- **Оценки:**
  - Пробл. 7,5 — ThinkBook, драйверы RDNA 3 поддерживаются полностью; тестов нет;
  - Ремонт 8,5;
  - Цена 5,5 — 1071,82 €;
  - Порт. 7 — 1,7 кг, 48 Втч;
  - Мощн. 4,5 → 4,5: процессор 4,9 (Ryzen 5 220 = 8540U, R23 9722), графика и медиадвижок 4,0 (740M — Time Spy 1527, кодирует AV1), экран 3,5 (45 % NTSC, 400 нит), порты — бонус 10 (2× USB4, SD, RJ45).
  - Средн. 6,6 → **6,5** (было 6,5).
- **Вывод:** брать ради яркого экрана и портов (бонус), не ради скорости.
- **Вариант `21UT004EGE` (+ SSD, 512 ГБ).** 949,00 € (Galaxus, маркетплейс, продавец HEINZSOFT, возврат 30 дней) + SSD 120,99 € = **1069,99 €**.
  Выходит на 2 € дешевле и с 1,5 ТБ, но SSD ставить самому. Купонные 898,90 € не считаются — [PSREF](https://psref.lenovo.com/Detail/ThinkBook/ThinkBook_16_G9_AHP?M=21UT004EGE), [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/209122443_-thinkbook-16-g9-21ut004ege-lenovo.html).
  Оценки: 7,5 / 8,5 / 5,5 / 7 / 4,5 (Мощн. как у №4), средняя 6,6 → 6,5.

### 5. Lenovo ThinkBook 16 G7 ARP — `21MW007VGE` · 1088,57 €
- То же, что №3, но **Ryzen 7 7735HS** (Rembrandt-R, 8 ядер) и графика **680M** (12 CU — вдвое больше, чем у 660M) ([amd.com](https://www.amd.com/en/products/processors/laptop/ryzen/7000-series/amd-ryzen-7-7735hs.html)).
  Cinebench R23 Multi — 13 106, Time Spy Graphics — 2303 ([`notes/amd-cpu.md`](notes/amd-cpu.md)).
- **Память:** 2×16 ГБ DDR5-4800 — [PSREF](https://psref.lenovo.com/Detail/ThinkBook/ThinkBook_16_G7_ARP?M=21MW007VGE), [Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Lenovo&ProductCode=21MW007VGE). SSD 1 ТБ, два M.2 2280.
- **Цена:** 1088,57 € у cyclotron.de (срок возврата idealo не показывает); 1092,00 € у easynotebooks.de (14 дней) — [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/207306221_-thinkbook-16-g7-21mw007vge-lenovo.html).
  Запас до потолка — 11 €. В 19:25 — то же. За год минимум 808,60 € (12.12.2025). Экран и порты — как у №3.
- **Оценки:** Пробл. 7 и Ремонт 8,5 — как у №3; Цена 5 — 1088,57 €; Порт. 7.
  - Мощн. 5 → 5: процессор 6,6 (R23 13 106), графика и медиадвижок 4,1 (680M — Time Spy 2303, без 4:2:2 и AV1-кодирования), экран 3 (45 % NTSC), порты — бонус 10.
  - Средн. 6,5 → **6,5** (было 6,5).
- **Когда брать:** если №1 раскупили, а нужен лучший из Zen 3+ в корпусе ThinkBook.

### 6. ASUS ExpertBook P1 PM1503CDA — `PM1503CDA-S70264X` · 928,61 € (+ планка + замена SSD; вариант `-S70262`)
- **Процессор:** Ryzen 5 150 — Rembrandt (= 7535HS, Zen 3+), графика 660M ([amd.com](https://www.amd.com/en/products/processors/laptop/ryzen/100-series/amd-ryzen-5-150.html)).
- **Память:** 1×16 ГБ SO-DIMM + свободный второй слот, до 64 ГБ. Даташит ASUS на этот P/N: «16GB DDR5 (16GB DDR5 SO-DIMM) · 2x DDR5 SO-DIMM slots» ([EN](https://gzhls.at/blob/ldb/7/7/9/4/57187dc9af3bd89f8e8a348d096d24911e28.pdf)).
  heise у PM1503 тоже видел одну планку и свободный слот ([heise](https://www.heise.de/bestenlisten/testbericht/asus-expert-book-pm1-im-test-guenstiger-laptop-mit-ryzen-5-und-16-gb-ram-ueberzeugt/jqmdlcc)).
- **SSD:** 512 ГБ в M.2 2280. Второй слот — **M.2 2230**, туда обычный 2280 не встанет ([asus.com](https://www.asus.com/laptops/for-work/expertbook/asus-expertbook-p1-pm1503/techspec/)). Два пути:
  - **заменить** 512 ГБ на 1 ТБ 2280: итог 620,06 + 187,56 + 120,99 = **928,61 €**;
  - **добавить** 1 ТБ 2230: итог 1027,59 € (SSD 2230 подешевел до 219,97 €, [`notes/prices-final.md`](notes/prices-final.md)), диск 1,5 ТБ.
- **Экран:** 15,6" FHD IPS-level, 300 нит, 45 % NTSC ([asus.com](https://www.asus.com/laptops/for-work/expertbook/asus-expertbook-p1-pm1503/techspec/)). heise намерил 287 кд/м² ([heise](https://www.heise.de/bestenlisten/testbericht/asus-expert-book-pm1-im-test-guenstiger-laptop-mit-ryzen-5-und-16-gb-ram-ueberzeugt/jqmdlcc)). У Intel-сестры P1503CVA (тот же корпус) NBC намерил 63,3 % sRGB, 1520:1, ΔE 3,69, ШИМ нет — лучший контраст среди IPS, но охват узкий ([`notes/displays.md`](notes/displays.md)).
- **Порты (бонус):** 2× USB-C 10 Гбит/с, 2× USB-A, RJ45, **HDMI 1.4 (4K только 30 Гц)**. Кардридера и USB4 нет ([asus.com](https://www.asus.com/laptops/for-work/expertbook/asus-expertbook-p1-pm1503/techspec/), [heise](https://www.heise.de/bestenlisten/testbericht/asus-expert-book-pm1-im-test-guenstiger-laptop-mit-ryzen-5-und-16-gb-ram-ueberzeugt/jqmdlcc)).
- **Вес и батарея:** 1,6 кг (asus.com) или 1,81 кг ([даташит](https://gzhls.at/blob/ldb/7/7/9/4/57187dc9af3bd89f8e8a348d096d24911e28.pdf)), 50 Втч. heise: около 7 часов, до 36 дБ(A), MIL-STD-810H.
- **Гарантия:** 36 месяцев международной (даташит ASUS).
- **Цена:** 620,06 € у xtreme.metacomp.de (срок возврата не показан; в 19:26 — то же); 635,10 € у jb-computer.de (30 дней) — [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/209457310_-expertbook-p1-pm1503cda-s70264x-asus.html).
  Минимум за год — 612,18 € (03.09.2026). С NV3 вместо Verbatim итог 950,51 € ([`notes/verify-other-brands.md`](notes/verify-other-brands.md)).
- **Оценки:**
  - Пробл. 7 — бизнес-линейка, отключений HEVC у ASUS не найдено; минус — графика в maintenance mode;
  - Ремонт 7,5 — 2 слота до 64 ГБ и 36 месяцев гарантии. Но второй M.2 только 2230, ASUS предупреждает, что установка M.2 «may void your warranty» ([asus.com](https://www.asus.com/laptops/for-work/expertbook/asus-expertbook-p1-pm1503/techspec/), [`notes/candidates-other-brands.md`](notes/candidates-other-brands.md)), ремонт у ASUS часто дольше 14 дней ([`../Intel/notes/brands.md`](../Intel/notes/brands.md));
  - Цена 7,5 — 928,61 €;
  - Порт. 7;
  - Мощн. 3 → 3,5: процессор 4,3 (Ryzen 5 150 = 7535HS), графика и медиадвижок 3,3 (660M, ни 4:2:2, ни AV1-кодирования), экран 2,5 (15,6" FHD, 45 % NTSC), порты — бонус 4 (USB-C 10 Гбит/с, RJ45, HDMI 1.4).
  - Средн. 6,5 → **6,5** (было 6,5).
- **Вариант `PM1503CDA-S70262`:** Ryzen 7 170 (8 ядер) и 680M; «Without OS»; раскладка та же ([даташит ASUS](https://gzhls.at/blob/ldb/a/6/a/e/01a53b1dc91ce2d747f13f0a811c3802b2e6.pdf)).
  - Цена 735,88 € у serverhero.de; 735,89 € у playox.de (30 дней) — [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/209457306_-expertbook-p1-pm1503cda-s70262-asus.html). 730,54 € — цена с купоном.
  - Итог с планкой и заменой SSD — **1044,43 €**. Оценки: 7 / 7,5 / 6 / 7 / 4,5 (Мощн. 4 → 4,5: процессор 6,6 — R7 170 = 7735HS, 680M), средняя 6,4 → 6,5.

### 7. ASUS Vivobook S16 M3607HA — `M3607HA-RP017W` · 1006,56 € (16 распаяно + планка; вариант `M1607GA-MB020W`)
- **Процессор:** Ryzen 7 260 — Hawk Point (= 8845HS), 8 ядер Zen 4. **Лучший CPU среди кандидатов в бюджете**: Cinebench R23 17 212 ([amd.com](https://www.amd.com/en/products/processors/laptop/ryzen/200-series/amd-ryzen-7-260.html), [`notes/amd-cpu.md`](notes/amd-cpu.md)).
  Графика 780M (12 CU, Time Spy 2808). Кодирует AV1.
- **Память:** 16 ГБ распаяно + пустой слот SO-DIMM, до 32 ГБ — [Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=ASUS&ProductCode=M3607HA-RP017W): «On-board + SO-DIMM», «1x SO-DIMM».
  На [asus.com](https://www.asus.com/laptops/for-home/vivobook/asus-vivobook-s16-m3607/techspec/) есть вариант «16GB on board + 16GB SO-DIMM». Двухканал включится только с планкой в слоте.
- **SSD:** 1 ТБ, один M.2 2280 ([asus.com](https://www.asus.com/laptops/for-home/vivobook/asus-vivobook-s16-m3607/techspec/)).
- **Экран:** WUXGA IPS-level, 300 нит, 45 % NTSC, **144 Гц** ([Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=ASUS&ProductCode=M3607HA-RP017W)). Icecat пишет «глянец», ASUS — матовый ([asus.com](https://www.asus.com/laptops/for-home/vivobook/asus-vivobook-s16-m3607/techspec/)), на живом образце не проверено. Замеров этой панели нет — единственный тест NBC Vivobook S16 сделан на другой панели, 2,5K ([`notes/displays.md`](notes/displays.md)).
- **Порты (бонус):** 2× USB-C 5 Гбит/с (DP, PD), 2× USB-A 5 Гбит/с, HDMI 2.1. Кардридера и USB4 нет ([Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=ASUS&ProductCode=M3607HA-RP017W), [asus.com](https://www.asus.com/laptops/for-home/vivobook/asus-vivobook-s16-m3607/techspec/)).
- **Вес и батарея:** 1,7 кг, 70 Втч, 65 Вт в комплекте ([Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=ASUS&ProductCode=M3607HA-RP017W)). **Гарантия** — не проверено: в проверке по Icecat и asus.com её не записали ([`notes/verify-other-brands.md`](notes/verify-other-brands.md), «Что не проверено»).
- **Цена:** 819,00 € у expert.de (обычный магазин, 14 дней; в 19:26 — то же) — [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/206751394_-vivobook-s16-m3607ha-rp017w-asus.html). Минимум за год — 699,96 € (26.08.2026).
  Итог с планкой Kingston — 1006,56 €, с запасной Lenovo — 1025,80 €.
- **Обзоры:** теста этой версии нет. У родственного S3607QA (Snapdragon) под полной нагрузкой шумно, 47,6–50,2 дБ(A) ([NBC](https://www.notebookcheck.net/Asus-Vivobook-S16-Laptop-Review-Good-everyday-computer-with-almost-20-hours-of-battery-life-for-EUR899.1002073.0.html)).
- **Оценки:**
  - Пробл. 6 — потребительская линия ASUS, шумный корпус;
  - Ремонт 5 — половина памяти распаяна, один M.2;
  - Цена 7 — 1006,56 €;
  - Порт. 7,5 — 1,7 кг, 70 Втч;
  - Мощн. 6 → 6: процессор 8,6 (R23 17 212 — сильнейший в бюджете), графика и медиадвижок 5,3 (780M — Time Spy 2808, AV1, без 4:2:2), экран 3 (45 % NTSC; 144 Гц на охват не влияет), порты — бонус 4 (USB-C 5 Гбит/с, HDMI 2.1).
  - Средн. 6,3 → **6,5** (было 6,5).
- **Вариант `M1607GA-MB020W` (Vivobook 16):** Ryzen AI 7 445 — урезанный, 6 ядер, 840M (4 CU); 60 Гц, 1,88 кг, 70 Втч. Раскладка та же, 16 распаяно + слот ([Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=ASUS&ProductCode=M1607GA-MB020W)).
  - Цена 806,99 € у nullprozentshop.de; 807,99 € у notebooksbilliger.de (30 дней) — [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/209172185_-vivobook-16-m1607ga-mb020w-asus.html). Итог с планкой — **994,55 €**.
  - NBC у этого корпуса (M1607KA, 78 %): рамка экрана отходит, SSD троттлит, охлаждение несбалансированное ([NBC](https://www.notebookcheck.net/Asus-Vivobook-16-laptop-review-AI-features-at-the-forefront-genuine-productivity-boost-or-marketing-hype.971144.0.html)).
  - Оценки: 5,5 / 5 / 7 / 7 / 4 (Мощн. 4,5 → 4: процессор 5,3 — R23 10 590, 840M — Time Spy 1415, экран 3 — у M1607KA 55,3 % sRGB; порты не проверены, взяты как у S16), средняя 5,7 → 5,5 (было 6). На 12 € дешевле №7, но слабее по всем пунктам.

### 8. Lenovo V15 G6 ARP — `83UU001LGE` + замена SSD · 910,94 €
_Раньше — в «Условных» («вне критерия C»: второго M.2 нет, 1 ТБ — только заменой диска). «+ SSD» теперь полноценный вариант, поэтому SKU оценён и вошёл в топ._
- **Процессор:** Ryzen 5 150 — Rembrandt (= 7535HS, Zen 3+), графика 660M (RDNA 2, драйверы в maintenance mode); AV1 не кодирует ([PSREF](https://psref.lenovo.com/Detail/Lenovo/Lenovo_V15_G6_ARP?M=83UU001LGE), [`notes/amd-cpu.md`](notes/amd-cpu.md)).
- **Память:** 2×16 ГБ DDR5 SO-DIMM, «Two DDR5 SODIMM slots, dual-channel capable»; «Installed memory is actually DDR5-5600 but runs as DDR5-4800» ([PSREF PDF](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=83UU001LGE&country_code=DE), проверено 30.09.2026).
- **SSD:** 512 ГБ M.2 2242 в единственном слоте — «One M.2 2280 PCIe 4.0 x4 slot» (PSREF PDF). 1 ТБ — только заменой: Verbatim Vi3000 за 120,99 €, родной диск остаётся лишним ([`notes/verify-lenovo.md`](notes/verify-lenovo.md)).
- **Экран:** 15,6" FHD IPS, 300 нит, 45 % NTSC, антиблик (PSREF PDF). Своих тестов V15 G5/G6 у NBC нет — не проверено ([`notes/displays.md`](notes/displays.md)).
- **Порты (бонус):** 1× USB-C 10 Гбит/с (PD, DisplayPort 1.2), 2× USB-A 5 Гбит/с, HDMI 1.4b, RJ45; кардридера нет (PSREF PDF).
- **Вес и батарея:** от 1,6 кг, 47 Втч, блок 65 Вт с круглым штекером; клавиатура без подсветки, немецкая. **Гарантия** 1 год (PSREF PDF).
- **Цена:** 789,95 € у galaxus.de (30 дней), 19:28 — [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/209094412_-v15-g6-83uu001lge-lenovo.html). У aitek.de — 759,00 €, но доставка «siehe Shop», сумма не видна, поэтому в минимум не брал ([`notes/prices-final.md`](notes/prices-final.md)).
  Итог с SSD — 789,95 + 120,99 = **910,94 €**. Минимум — 712,52 € (10.08.2026, [`notes/verify-idealo-sweep.md`](notes/verify-idealo-sweep.md)).
- **HEVC:** в PSREF слова HEVC нет, отключений у Lenovo на AMD не найдено ([`notes/verify-idealo-sweep.md`](notes/verify-idealo-sweep.md)) — проверить DXVA Checker'ом в срок возврата.
- **Оценки (выставлены впервые):**
  - Пробл. 6 — как у Intel V15 G5 (Lenovo V, 1 год гарантии); графика RDNA 2 только в поддержке — у Intel V15 G5 драйверы тоже legacy;
  - Ремонт 6,5 — оба слота заняты, M.2 один (родной SSD меняется), зато PSREF есть;
  - Цена 8 — 910,94 €;
  - Порт. 6,5 — 1,6 кг, 47 Втч, круглый штекер, как у Intel V15 G5;
  - Мощн. — → 3,5: процессор 4,3 (7535HS — R23 8613), графика и медиадвижок 3,3 (660M, ни 4:2:2, ни AV1-кодирования), экран 2,5 (15,6" FHD, 45 % NTSC), порты — бонус 3 (HDMI 1.4b, DP 1.2).
  - Средн. 6,1 → **6**.
- **Почему ниже №2:** тот же процессор и графика, но 15,6" FHD, один M.2 и 1 год гарантии.

### 9. Acer Swift Air 16 OLED SFA16-61M-R1FY — `NX.DL5EG.002` · 993,50 € (32 ГБ распаяно)
_Новая находка прохода «от экрана» ([`notes/display-sweep.md`](notes/display-sweep.md)): лучший **измеренный** экран в бюджете. Но процессор для 4K слабый — в [`notes/amd-cpu.md`](notes/amd-cpu.md) Ryzen AI 5 330 в списке «не брать»._
- **Процессор:** Ryzen AI 5 330 — Krackan Point 2: 1 Zen 5 + 3 Zen 5c, 4 ядра / 8 потоков, графика Radeon 820M (2 CU) ([`notes/amd-cpu.md`](notes/amd-cpu.md)). Cinebench R23 Multi — 7840, Time Spy Graphics — 786 ([NBC CPU](https://www.notebookcheck.net/Mobile-Processors-Benchmark-List.2436.0.html), [NBC GPU](https://www.notebookcheck.net/Mobile-Graphics-Cards-Benchmark-List.844.0.html)). VCN 4.0.5: кодирует AV1, 4:2:2 не декодирует ([`notes/amd-codecs.md`](notes/amd-codecs.md)).
- **Память:** 32 ГБ LPDDR5 распаяны, «RAM-Speicher maximal 32 GB»; SSD 1 ТБ ([Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Acer&ProductCode=NX.DL5EG.002)). Слот M.2 2280 один ([LaptopMedia](https://laptopmedia.com/de/review/acer-swift-air-16-sfa16-61m-review-a-16-inch-laptop-that-weighs-under-1-kg/)).
- **Экран:** 16" WUXGA OLED CineCrystal, DCI-P3 (Icecat). LaptopMedia у SFA16-61M (панель Samsung ATNA60KJ04-0) намерил **100 % sRGB и 100 % DCI-P3**, 297 кд/м²; экран очень глянцевый (178 GU — блики главный минус); ШИМ есть, но «с ограниченной амплитудой, относительно комфортно» ([LaptopMedia](https://laptopmedia.com/de/review/acer-swift-air-16-sfa16-61m-review-a-16-inch-laptop-that-weighs-under-1-kg/)). Своего теста NBC нет ([сборник NBC](https://www.notebookcheck.net/Acer-Swift-Air-16-SFA16-61M.1173569.0.html)).
- **Порты (бонус):** 2× USB-C 5 Гбит/с (DP), 1× USB-A 5 Гбит/с, HDMI 1.4 (Icecat).
- **Вес и батарея:** 1,1 кг, 50 Втч, зарядка USB-C 65 Вт (Icecat). **Гарантия** — не проверено.
- **Цена:** 993,50 € у expert.de (14 дней) — 20:50, критик; 999,00 € на Kaufland (маркетплейс, 14 дней); 1017 € у boomstore ([idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/211778543_-swift-air-16-oled-16-wuxga-amd-ryzen-ai-5-32gb-1tb-ssd-silber-nx-dl5eg-002-acer.html), [`notes/display-sweep.md`](notes/display-sweep.md)). Минимум за полгода — 950 € (27.09).
- **Риски:** HEVC у Acer — как у №10; память и SSD не расширить.
- **Оценки (выставлены впервые):**
  - Пробл. 4,5 — Acer-якорь 4 (с legacy-драйверами); у 820M драйверы актуальные (+0,5, как у №10); данных о надёжности этой модели нет — не проверено; риск HEVC тот же;
  - Ремонт 3 — как у №10: всё распаяно, мануалов у Acer нет;
  - Цена 7 — 993,50 €;
  - Порт. 8,5 — 1,1 кг, 50 Втч;
  - Мощн. — → 4,5: процессор 3,9 (R23 7840), графика и медиадвижок 3,3 (820M — Time Spy 786, AV1 без 4:2:2), экран 8 (OLED, замер 100 % DCI-P3: +0,5; сильный глянец: −0,5), порты — бонус 3 (USB-C 5 Гбит/с, HDMI 1.4).
  - Средн. 5,5 → **5,5**.
- **Вывод:** по шкале чуть выше №10 — дешевле на 87,71 € и легче, а экран измерен. Но для монтажа 4K процессор и графика у него слабейшие в топе: брать, только если экран важнее скорости.

### 10. Acer Aspire 16 AI OLED A16-61M-R2R1 — `NX.JP0EG.00Z` · 1081,21 € (32 ГБ распаяно; вариант R8T1)
- **Процессор:** Ryzen AI 7 350 (Krackan Point), графика 860M ([amd.com](https://www.amd.com/en/products/processors/laptop/ryzen/ai-300-series/amd-ryzen-ai-7-350.html)). С быстрой LPDDR5X-8533 графика работает в полную силу ([`notes/verify-other-brands.md`](notes/verify-other-brands.md)).
- **Память:** 32 ГБ LPDDR5X-8533 распаяны, не расширить — [Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Acer&ProductCode=NX.JP0EG.00Z). Даташит Acer от 26.06.2026 (копия на geizhals; acer.com 30.09 не открывался — [`notes/verify-other-brands.md`](notes/verify-other-brands.md)): «Onboard-RAM (nicht austauschbar …)», HDMI 2.1, «100W Netzteil», 2 года гарантии ([даташит](https://gzhls.at/blob/ldb/e/9/9/4/1b8b6ae3e1047dc798a552be0d80e9a0f0ab.pdf)).
- **Экран:** OLED CineCrystal (глянец) 16" WUXGA, 300 нит, 60 Гц; охват — **95 % DCI-P3** по даташиту Acer от 26.06.2026 ([даташит](https://gzhls.at/blob/ldb/e/9/9/4/1b8b6ae3e1047dc798a552be0d80e9a0f0ab.pdf)) и 100 % по Icecat ([Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Acer&ProductCode=NX.JP0EG.00Z)). Независимых замеров нет, ШИМ — не проверено (у NBC только [сборник](https://www.notebookcheck.net/Acer-Aspire-16-AI-A16-61M.1237489.0.html); та же ли панель, что у №9, — не проверено) ([`notes/displays.md`](notes/displays.md)). В срок возврата проверить мерцание на малой яркости и профиль sRGB.
- **Порты (бонус):** 2× USB4 40 Гбит/с, 2× USB-A, HDMI, microSD. 1,55 кг, 65 Втч, 100 Вт ([Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Acer&ProductCode=NX.JLLEG.009), у R2R1 — как у R8T1).
- **Цена:** 1081,21 € у computeruniverse.net (30 дней, доставка до 09.10; в 19:27 — то же, оффер «AI 7 350 32GB/1TB»); второе предложение R2R1 — 1111,90 € — [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/211631508_-aspire-16-ai-a16-61m-r2r1-acer.html).
  Карточка смешанная: «ab 794,83 €» и предложения за 801,50–852,99 € — это другая конфигурация, R5H7 `NX.JP0EG.010` (AI 5 330, 16/512); история цены тоже смешанная ([`notes/prices-final.md`](notes/prices-final.md)).
  У соседнего R5H7 e-tec пишет «Netzteil separat erhältlich», но у R2R1 блок 100 Вт в комплекте по даташиту Acer ([даташит](https://gzhls.at/blob/ldb/e/9/9/4/1b8b6ae3e1047dc798a552be0d80e9a0f0ab.pdf)).
- **Риски:**
  - HEVC: Acer после патентного спора продаёт в Германии часть устройств «ohne HEVC-Codec». По словам Acer, у устройств без предустановленного кодека поддержку можно включить, установив ПО отдельно ([ChannelPartner](https://www.channelpartner.de/article/4187748/acer-und-asus-liefern-wieder.html), открыто критиком 30.09). Похоже, речь о программном расширении, а не об аппаратной блокировке, но DXVA Checker — сразу после покупки;
  - Techradar — 60 %, «build quality issues» ([сборник NBC](https://www.notebookcheck.net/Acer-Aspire-16-AI-A16-61M.1237489.0.html)).
- **Оценки:**
  - Пробл. 4 — Acer-якорь 4 (с legacy-драйверами); у 860M драйверы актуальные (+0,5), но Techradar ругает сборку (−0,5); риск HEVC тот же;
  - Ремонт 3 — всё распаяно, мануалов у Acer нет;
  - Цена 5,5 — 1081,21 €;
  - Порт. 8 — 1,55 кг, 65 Втч;
  - Мощн. 7 → 6,5: процессор 8,0 (R23 16 015), графика и медиадвижок 5,1 (860M, AV1, без 4:2:2), экран 7 (OLED 95–100 % DCI-P3 по даташиту; −0,5 — ШИМ не проверен, −0,5 — глянец), порты — бонус 8 (2× USB4, HDMI, microSD).
  - Средн. 5,4 → **5,5** (было 5,5). Ниже №9 по неокруглённой средней: дороже на 87,71 €, а экран не измерен.
- **Вариант R8T1 `NX.JLLEG.009`:** экран IPS 120 Гц, 350 нит, 45 % NTSC; SSD, вероятно, QLC — [Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Acer&ProductCode=NX.JLLEG.009).
  - Цена 1080,25 € у easynotebooks.de (14 дней) — [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/208031586_-aspire-16-ai-a16-61m-r8t1-acer.html). Это максимум года; 21–29.09 было 995 €, минимум за год — 886,36 € (01.07.2026).
  - Оценки: 4 / 3 / 5,5 / 8 / 5,5 (Мощн. 6,5 → 5,5: экран 3 — IPS 45 % NTSC вместо OLED), средняя 5,2 → 5 (было 5,5).

### 11. Lenovo ThinkBook 16 G9 AHP — `21UT000RGE` · 1188,97 € — справка «ждать»
- **Процессор:** Ryzen 7 250 — Hawk Point (= 8840U), 8 ядер Zen 4, графика 780M, кодирует AV1 ([amd.com](https://www.amd.com/en/products/processors/laptop/ryzen/200-series/amd-ryzen-7-250.html)).
- **Память:** 2×16 ГБ SO-DIMM DDR5-5600, 1 ТБ + второй M.2 — [PSREF](https://psref.lenovo.com/Detail/ThinkBook/ThinkBook_16_G9_AHP?M=21UT000RGE).
  NBC: «2x 16 GB, DDR5-5600, zwei Slots» ([NBC](https://www.notebookcheck.com/Lenovo-ThinkBook-16-G9-mit-Ryzen-7-Zen-4-32-GB-RAM-1-TB-SSD-im-Angebot.1310427.0.html)).
- Корпус, порты и экран — как у №4: 2× USB4, SD, RJ45, 400 нит, 1,7 кг, 48 Втч ([PSREF](https://psref.lenovo.com/Detail/ThinkBook/ThinkBook_16_G9_AHP?M=21UT000RGE)).
- **Цена:** 1188,97 € у joybuy.de (30 дней); следующий — notebookstore.de, 1194,90 € (14 дней); 20 предложений, предложения Amazon в 17:26 уже нет — [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/209122441_-thinkbook-16-g9-21ut000rge-lenovo.html) (перепроверено критиком). В 19:29 — 1188,97 € (Amazon, продаёт cyberport, маркетплейс; joybuy.de — 30 дней), [`notes/prices-final.md`](notes/prices-final.md).
  За год минимум 1045 € (21.01.2026, [`notes/verify-lenovo.md`](notes/verify-lenovo.md)). За полгода минимум 1109,82 € (21.09.2026, API idealo `period=6M`), ≤ 1100 € — ни одного дня из 182.
- **Оценки:** Пробл. 7,5 и Ремонт 8,5 — как у №4; Цена 3 — 1188,97 €; Порт. 7.
  - Мощн. 6 → 6: процессор 7,3 (R23 14 676), графика и медиадвижок 5,3 (780M, AV1), экран 3,5 (45 % NTSC, 400 нит), порты — бонус 10.
  - Средн. 6,4 → **6,5** (было 6,5).
- **Справка:** это то, чем должен был быть №4, — полноценный процессор в том же корпусе. Но покупка сейчас, а сейчас он дороже потолка на 88,97 €.

### 12. Gigabyte GAMING A16 (GA63H) — `3VHK3DE894SH` · 1099 € + планка = 1286,56 € — справка «ждать»
- **Процессор и графика:** Ryzen 7 260 (Hawk Point, 8 ядер Zen 4) + **RTX 5060 8 ГБ** с MUX; TGP 75 Вт, то есть пониженный ([NBC](https://www.notebookcheck.net/Gigabyte-Gaming-A16-3VH.1188434.0.html)).
  NVDEC у Blackwell (RTX 50) декодирует H.264 и HEVC 4:2:2 ([NVIDIA](https://docs.nvidia.com/video-technologies/video-codec-sdk/13.0/nvdec-video-decoder-api-prog-guide/index.html)).
- **Память:** 1×16 ГБ + свободный SO-DIMM, до 64 ГБ.
  Подтверждают четыре источника: [gigabyte.com](https://www.gigabyte.com/de/Laptop/GIGABYTE-GAMING-A16-GA63H/sp), [Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&GTIN=4719331766764) («1 x 16 GB»), [Alternate](https://www.alternate.de/GIGABYTE/GAMING-A16-3VHK3DE894SH-Gaming-Notebook/html/product/100151262) («belegt 1»), [LaptopMedia](https://laptopmedia.com/review/gigabyte-gaming-a16-ga63h-amd-review-stealthy-sleeper-with-record-battery-life/).
- **SSD:** 1 ТБ + второй M.2 (PCIe 4.0 x2).
- **Порты (бонус):** USB4 (DP 1.4), HDMI 2.1, RJ45.
- **Экран:** 16" WUXGA 165 Гц; 60 % sRGB по 3DNews, 52 % по LaptopMedia ([3DNews](https://3dnews.ru/1132160/obzor-gigabyte-gaming-a16-3vh)) — для цвета слабо.
- **Шум и нагрев:** 47–50 дБА, CPU 90–94 °C, но без троттлинга.
- **Вес и батарея:** 2,2 кг, 76 Втч (около 8 часов по LaptopMedia), блок 150 Вт. **Гарантия** 2 года (Icecat).
- **Цена:** 1099,00 € у coolblue, MediaMarkt, computeruniverse и Cyberport (у всех 30 дней) — [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/207329496_-gaming-a16-3vhk3de894sh-gigabyte.html). Критик в 17:26 и 19:29 — то же; за полгода минимум 1079 € (03–05.09.2026).
  - За год минимум 999 € (28.10–31.12.2025), с января — не ниже 1079 €;
  - с планкой 1286,56 €; в 1100 € войдёт при цене ноутбука ≤ 912 € — за год такого не было ([`notes/verify-gpu.md`](notes/verify-gpu.md)).
- **Оценки:**
  - Пробл. 6 — громкий и горячий. HEVC у Gigabyte не отключают, но BIOS производителя умеет отключать и декодер NVIDIA ([Intel-проверка, п. 5.7](../Intel/notes/browser-check-summary.md));
  - Ремонт 7 — 2 слота и 2 M.2, данных о мануалах и запчастях нет;
  - Цена 1,5 — 1286,56 €;
  - Порт. 6 — 2,2 кг;
  - Мощн. 8,5 → 7,5: процессор 8,6 (R23 17 212), графика и медиадвижок 10 (RTX 5060 — Time Spy 11 937; единственный AMD, который декодирует 4:2:2 — через NVDEC), экран 3 (52–60 % sRGB), порты — бонус 8.
  - Средн. 5,6 → **5,5** (было 6).
- **Справка:** покупка сейчас, а с планкой он дороже потолка на 186,56 €.

## Условные варианты (раскладку проверить не удалось, вне критериев или цена выше 1100 €) — справка

_Покупка сейчас: всё ниже — справка. Цены — 19:28–19:29 ([`notes/prices-final.md`](notes/prices-final.md)). V15 G6 `83UU001LGE` перешёл в топ (№8): «+ SSD» теперь полноценный._

- **HP EliteBook 8 G1a 16 `CN0Q3EC`** — единственный дешёвый HP на AMD с HEVC («CODEC is supported», [QuickSpecs c09120200](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09120200)).
  - Ryzen 5 PRO 230 (Hawk Point, 6 ядер, 760M); экран WUXGA 400 нит, 100 % sRGB (по BOM).
  - **Исчез:** днём было 1005,00 € у asaboshisystems.de (одно предложение, предоплата), в 19:29 — «keine Angebote gefunden» ([idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/214137501_-elitebook-8-g1a-16-cn0q3ec-hp.html), [`notes/prices-final.md`](notes/prices-final.md)).
  - Второго M.2 нет, SSD пришлось бы менять: итог был **1125,99 €**.
  - **Раскладку проверить не удалось:** QuickSpecs перечисляет и 1×32, и 2×16; в BOM [PartSurfer](https://partsurfer.hp.com/partsurfer/?searchtext=CN0Q3EC) есть модули и 16, и 32 ГБ; в Icecat P/N нет (404) ([`notes/verify-hp-dell.md`](notes/verify-hp-dell.md)).
  - Это DaaS-юнит у партнёра HP Renew: новый ли экземпляр и есть ли на него гарантия — не проверено ([`notes/verify-hp-dell.md`](notes/verify-hp-dell.md)). LatencyMon у этой модели показал проблемы с DPC-задержками: 18 пропущенных кадров за минуту 4K60 ([`notes/verify-hp-dell.md`](notes/verify-hp-dell.md)).
- **Lenovo IdeaPad Slim 5 16AKP10 `83HY0061GE`** — Ryzen AI 5 340 (Zen 5, 6 ядер, 840M), 2×16 ГБ, 1 ТБ ([PSREF](https://psref.lenovo.com/Detail/IdeaPad/IdeaPad_Slim_5_16AKP10?M=83HY0061GE)).
  На idealo только б/у, в 19:28 — тоже ([idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/207280344_-ideapad-slim-5-16-83hy0061ge-lenovo.html)). 17.06.2026 новый стоил 776,15 €, ≤ 1100 € — 180 дней из 182. Нового предложения нет — для покупки сейчас не вариант.
- **ASUS Vivobook 16 `M1607KA-MB187W`** — Ryzen AI 7 350, 16 ГБ распаяно + слот ([Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=ASUS&ProductCode=90NB15F1-M00C70)).
  949 € + планка = 1136,56 € ([idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/210697864_-vivobook-16-m1607ka-mb187w-asus.html)). В бюджет войдёт при цене ≤ 912,44 €; 22.06 стоил 890,10 €, в 19:28 — 949 €.
- **ASUS ExpertBook B1 `BM1503CDA-S72123`** — Ryzen 7 170, 909,99 € только на маркетплейсах ([idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/213397785_-expertbook-b1-bm1503cda-s72123-15-6-amd-ryzen-7-170-16gb-ram-1tb-ssd-90nx0821-m02bx0-asus.html)).
  Раскладку проверить не удалось: Icecat — 404, даташита ASUS на этот P/N не нашли; на geizhals есть «aufgerüstet»-сборки до 64 ГБ ([`notes/verify-other-brands.md`](notes/verify-other-brands.md)). У соседнего `-S71655` [даташит ASUS](https://gzhls.at/blob/ldb/4/1/3/4/187b24741cf9d760f91fc6f3f6c8825bb088.pdf) пишет 2×8 — скорее всего, и здесь так же, и тогда он не подходит.
- **ThinkPad E16 Gen 2 AMD `21M5002DGE` / `21M5002VGE`** — 2×16 ГБ, 1 ТБ, R7 7735HS / R5 7535HS ([PSREF 002D](https://psref.lenovo.com/Detail/ThinkPad/ThinkPad_E16_Gen_2_AMD?M=21M5002DGE)).
  - Сейчас 1199 € ([idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/208145740_-thinkpad-e16-g2-21m5002dge-lenovo.html)) и 1260,32 € ([idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/204203152_-thinkpad-e16-g2-21m5002vge-lenovo.html)).
  - Минимумы за год — 949 € и 789,90 €.
  - По железу не лучше №3 и №5 (нет USB4), поэтому ждать их смысла нет.
- **OLED с 32 ГБ, но дороже 1100 €** (проход «от экрана», [`notes/display-sweep.md`](notes/display-sweep.md)):
  - Acer Swift Air 16 OLED `SFA16-61M-R559` (Ryzen AI 7 350, 32/1 ТБ) — 1149 €; за полгода минимум 999 € (01.07), ≤ 1100 € — 104 дня ([idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/209373389_-swift-air-16-oled-sfa16-61m-r559-acer.html));
  - Lenovo IdeaPad 5 2-in-1 15AGP11 `83UM002BGE` (Ryzen AI 7 445, 2×16, 1 ТБ, 15,3" 2,5K OLED 500 нит) — 1267,07 €, ≤ 1100 € — ни одного дня за полгода ([idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/210991837_-ideapad-5a-2-in-1-15-83um002bge-lenovo.html)).

## Отброшено (главное)

- **HP ProBook 4 G1a 16 `C7SP9ES`** — 906,99 €, 2×16, 1 ТБ; по всему остальному был бы лучшим в группе HP. Но в QuickSpecs: «Hardware acceleration for CODEC H.265/HEVC … is disabled on this platform» ([c09111176](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09111176), [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/208030540_-probook-4-g1a-16-c7sp9es-hp.html)).
  Так же выключен HEVC у ProBook 465 G11, EliteBook 665 G11 и EliteBook 6 G1a ([`notes/hevc-amd.md`](notes/hevc-amd.md)). **Не брать ни за какую цену.**
- **HP 255R G10 `CU0R1ES`** — формально проходит (606,99 + планка 187,56 + SSD 120,99 = 915,54 €, [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/210295290_-255r-g10-cu0r1es-hp.html)), но **не рекомендую**:
  - HEVC: высокий риск. HP отключила его у «200 Series G9» ([Ars Technica](https://arstechnica.com/gadgets/2025/11/hp-and-dell-disable-hevc-support-built-into-their-laptops-cpus/)), а в QuickSpecs 255R G10 нет ни «disabled», ни «supported»;
  - раскладка спорная, документы HP расходятся:
    - «за» 1×16 + слот — QuickSpecs: «Memory Slots 2 SODIMM (RMB-UR only)»; в BOM [PartSurfer](https://partsurfer.hp.com/partsurfer/?searchtext=CU0R1ES) один модуль 16 ГБ ([`notes/verify-hp-dell.md`](notes/verify-hp-dell.md));
    - «против» — сервис-мануал: «onboard memory … not accessible or upgradeable»; QuickSpecs: «slots customer non-accessible», максимум «32GB (1 x 32GB)»; у соседних `CJ5Q2EA` / `CJ5Q1EA` Icecat пишет «RAM maximal 16 GB» ([QuickSpecs](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09053765), [MSG](https://kaas.hpcloud.hp.com/pdf-public/pdf_11296126_en-US-1.pdf), [`notes/verify-idealo-sweep.md`](notes/verify-idealo-sweep.md)).
    Итог: 2×16 можно проверить только на живом экземпляре;
  - второго M.2 нет; HDMI 1.4b выводит максимум 1920×1200, то есть 4K-монитор — только через USB-C;
  - Ryzen 7 7735U (Zen 3+, 28 Вт), без AV1-кодирования;
  - корпус «warps a lot» ([NBC, 255 G10 с 7120U](https://www.notebookcheck.net/HP-255-G10-with-7120U-review-Small-budget-low-performance.1293092.0.html)); блок 45 Вт (BOM, [`notes/verify-hp-dell.md`](notes/verify-hp-dell.md)).
  Родственные `CJ5Q2EA` / `CJ5Q1EA` отброшены по тем же причинам ([`notes/verify-idealo-sweep.md`](notes/verify-idealo-sweep.md)).
- **Ловушка «1×32 ГБ»:** ThinkPad E16 Gen 3 AMD `21ST004GGE` (1156,99 €) и `21ST001YGE` (1199,64 €) — «1x 32GB SODIMM» ([PSREF](https://psref.lenovo.com/Detail/ThinkPad/ThinkPad_E16_Gen_3_AMD?M=21ST004GGE)). HP EliteBook 8 G1a `CT3V8ES` — тоже 1×32 (PartSurfer).
- **Barcelo и Barcelo-R (Ryzen 5x25U, 7x30: Zen 3, Vega, DDR4, AV1 не декодирует):**
  - ThinkBook 16 G6 ABP `21KK0074GE` (1007,99 €, формально 2×16 и 1 ТБ) и `21KK007TGE` (с планкой DDR4 и SSD — 1083,16 €);
  - Medion Avantum 15 E1, HP 15-fc, Acer Aspire Go 15, TERRA.
  Vega получает только критичные исправления ([`notes/amd-cpu.md`](notes/amd-cpu.md)).
- **Урезанные CPU:** AI 5 330 (4 ядра, 820M) — Vivobook 16 `M1607KA-MB172W`, ThinkPad E16 Gen 4 `21Y4006CGE`. Swift Air 16 R1FY с тем же процессором вошёл в топ (№9) только из-за измеренного OLED-экрана. Mendocino (Ryzen 7x20, Ryzen 10) — максимум 16 ГБ.
- **2×8 (менять обе планки, > 1100 €):** IdeaPad Slim 5 16AKP10 `83HY009NGE`, ExpertBook B1 `BM1503CDA-S71655` (по даташиту ASUS), MSI Venture A16.
- **Хороший экран, но не проходит память** (проход «от экрана», [`notes/display-sweep.md`](notes/display-sweep.md)):
  - IdeaPad Slim 5a 16AGP11 OLED (DCI-P3) `83S2003GGE`, `83S2000BGE` — 2×8 ([PSREF](https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=83S2003GGE&country_code=DE)), 849 и 889 €;
  - IdeaPad Slim 5 15ARP10 `83J3005FGE` (IPS 100 % sRGB) — 16 ГБ распаяно, слотов нет, 799 €;
  - ASUS Vivobook 16 OLED M1605NAQ — 8 ГБ распаяно + слот, максимум 24 ГБ; HP OmniBook 5 16 OLED — только 16 ГБ распаяно;
  - у всех Lenovo IdeaPad Slim 5 16 gen 10, ThinkBook и ThinkPad со слотами, что продаются в Германии, — WUXGA 45 % NTSC (PSREF по каждому MTM); OLED-версия 83J1006UGE с 2×16 снята с продажи.
- **Dell на AMD:** HEVC отключён той же политикой, что и на Intel ([Dell Pro 3, сноска](https://www.delltechnologies.com/asset/en-us/products/laptops-and-2-in-1s/selling-competitive/dell-pro-3-14-16-laptop-product-fact-sheet.pdf)); с 32 ГБ дешевле 1605 € нет ([`notes/candidates-hp-dell.md`](notes/candidates-hp-dell.md), [выдача idealo](https://www.idealo.de/preisvergleich/ProductCategory/3751F471884-699493-1568565-7612877.html?sortKey=minPrice)).
- **AMD + RTX 50 около 1100 €** — HP Omen 16-ap `C2VM8EA`, Acer Nitro V 16 AI `ANV16-42-R38V`, Victus 15 `15-fb3051ng`: новых предложений нет, только б/у ([`notes/verify-gpu.md`](notes/verify-gpu.md)).
- **Выше потолка:** Tuxedo InfinityBook Pro 15 Gen10 AMD — 1659 € в нужной конфигурации; XMG EVO 15 — от 1489 €; Framework 16 — ≈ 1927 € ([`notes/candidates-other-brands.md`](notes/candidates-other-brands.md)).

## AMD против Intel

### Итог по обеим веткам

> **Устарело 01.10.2026.** Ниже — итог 30.09, до новых жёстких критериев (экран с полным sRGB, оплата наличными). Актуальный выбор — Medion `30040202` (Intel), запасные — Swift Air `NX.DL5EG.002` и Lenovo `83J3006GGE`; см. [`../REPORT.md`](../REPORT.md).

_Версия 3 — согласовано с финальным [`../REPORT.md`](../REPORT.md) (30.09.2026, вечер). Вводные: кодек и программа неизвестны навсегда, покупка сейчас, внешнего монитора нет, планку и SSD ставит владелец, порты — бонус. Цены перепроверены в 20:40 ([`../REPORT.md`](../REPORT.md), «Финалисты»)._

1. **Выбор — Intel HP OmniBook 7 AI 16-ay0770ng `BM9T4EA#ABD`, 979,30 €** (hp.com, HP Store — 30 дней на возврат, докупать ничего; [idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/206602335_-omnibook-7-ai-16-ay0770ng-hp.html)).
   - Самый мощный в бюджете обеих веток: Core Ultra 7 255H (R23 17 845) и Arc 140T (Time Spy 3843) против Ryzen AI 7 350 (16 015) и 860M (2565) у лучших AMD ([NBC CPU](https://www.notebookcheck.net/Mobile-Processors-Benchmark-List.2436.0.html), [NBC GPU](https://www.notebookcheck.net/Mobile-Graphics-Cards-Benchmark-List.844.0.html)).
   - Самый широкий аппаратный декод: HEVC 4:2:2 и 4:4:4, AV1, плюс кодирование AV1 ([Intel media-driver](https://raw.githubusercontent.com/intel/media-driver/master/docs/media_features.md)). AMD HEVC 4:2:2 не декодирует ни в одном поколении ([AMD AMF](https://github.com/GPUOpen-LibrariesAndSDKs/AMF/wiki/GPU%20and%20APU%20HW%20Features%20and%20Support)). Кодек неизвестен навсегда — поэтому ширина декода решает.
   - Условия: 32 ГБ распаяны (допустимо по критериям); в первый день — DXVA Checker, потому что HP может отключить HEVC. Нет HEVC — вернуть.
2. **Запасной — Intel `83HS00BLGE`, 993,30 €** ([idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/209881995_-ideapad-slim-5-16-83hs00blge-lenovo.html)): 2×16 SO-DIMM, HEVC 4:2:2, Lenovo; но графика UHD в 3,5 раза слабее HP.
3. **Лучший AMD — №1 `83HY008CGE`, 1059,99 €** (idealo — см. таблицу «Топ-10»): тот же корпус, что у `83HS00BLGE`, графика в 2,3 раза сильнее, AV1 и HDMI 2.1, но без HEVC 4:2:2 и дороже HP на 81 €.
4. **Если для владельца главное — экран — AMD №10 Acer R2R1 `NX.JP0EG.00Z`, 1081,21 €** ([idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/211631508_-aspire-16-ai-a16-61m-r2r1-acer.html)): единственный OLED (95–100 % DCI-P3) в бюджете при процессоре, который тянет 4K. Минусы: нет HEVC 4:2:2, графика в 1,5 раза слабее HP, распайка, риски Acer; широкий охват требует включить управление цветом в Resolve ([форум Blackmagic](https://forum.blackmagicdesign.com/viewtopic.php?uid=16&f=21&t=133034&start=0)).
   Черновик итога выбирал именно его, но из-за ошибочной посылки «владелец сделал экран главным критерием» — подробно в [`../REPORT.md`](../REPORT.md) и [`notes/final-draft-judges.md`](notes/final-draft-judges.md).
5. **«Ждать» — справка.** Intel ThinkBook 16 G8 `21SK007KGE` при своём минимуме в 910 € набрал бы 7,5, но сейчас стоит 1349 € ([idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/206151089_-thinkbook-16-g8-21sk007kge-lenovo.html)).

### Откуда данные Intel

Данные Intel — из финального [`../Intel/REPORT.md`](../Intel/REPORT.md) (30.09.2026, вечер) и проверенных в браузере файлов:
[`idealo-sku-lenovo.md`](../Intel/notes/idealo-sku-lenovo.md), [`idealo-sku-other.md`](../Intel/notes/idealo-sku-other.md), [`verify-lenovo-ideapad-v.md`](../Intel/notes/verify-lenovo-ideapad-v.md), [`verify-idealo-new-scan-32gb.md`](../Intel/notes/verify-idealo-new-scan-32gb.md), [`browser-check-summary.md`](../Intel/notes/browser-check-summary.md).
Оценки и цены Intel ниже совпадают с `../Intel/REPORT.md` версии 3: №1 `83HS00BLGE` (993,30 €, средн. 7), №2 Medion `MD600023` (699,97 €, 6,5), №6 `22AY003WGE` + SSD (1038,06 €, 6,5), №8 HP `BM9T4EA` (979,30 €, 6). Правило мест при равной средней и состав «Мощн.» — общие для обоих отчётов.
Для сравнения здесь взят `83HS00BLGE`: тот же корпус, что у лучшего AMD, поэтому разница — только в CPU, графике и кодеках.

### 1. Лучший AMD против лучшего Intel в том же корпусе IdeaPad Slim 5 16

| | **AMD** — IdeaPad Slim 5 16AKP10 `83HY008CGE` | **Intel** — IdeaPad Slim 5 16IRH10 `83HS00BLGE` |
|---|---|---|
| CPU | Ryzen AI 7 350, **Krackan Point** (Zen 5, 2025), 8 ядер; R23 — 16 015 | Core i7-13620H, **Raptor Lake-H** (2023), 6P + 4E; R23 — 15 176 ([NBC](https://www.notebookcheck.net/Mobile-Processors-Benchmark-List.2436.0.html)) |
| iGPU | Radeon 860M, Time Spy **2565** | UHD 64 EU, Time Spy **1110** ([NBC](https://www.notebookcheck.net/Mobile-Graphics-Cards-Benchmark-List.844.0.html)); с 19.09.2025 драйверы legacy ([Intel](https://www.intel.com/content/www/us/en/support/articles/000101986/graphics.html)) |
| Память | 2×16 SO-DIMM DDR5-5600 ([PSREF](https://psref.lenovo.com/Detail/IdeaPad/IdeaPad_Slim_5_16AKP10?M=83HY008CGE)) | 2×16 SO-DIMM DDR5-5600 ([PSREF](https://psref.lenovo.com/Detail/IdeaPad/IdeaPad_Slim_5_16IRH10?M=83HS00BLGE)) |
| SSD | 1 ТБ + свободный M.2 2280 | 1 ТБ + свободный M.2 2280 |
| Цена idealo, 30.09.2026 | **1059,99 €** — Kaufland, маркетплейс (expert), 14 дней, одно предложение ([idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/209439304_-ideapad-slim-5-16-83hy008cge-lenovo.html)) | **993,30 €** — Kaufland, маркетплейс (McElec), 14 дней, в 17:27 и 18:47 (днём было 989,05 €); 995 € у technowelt24 и expert-technomarkt, 995,98 € у expert.de (14 дней); 7 предложений ([idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/209881995_-ideapad-slim-5-16-83hs00blge-lenovo.html)) |
| Минимум цены (idealo) | за год — 896,28 € (23.02.2026); за полгода — 897,00 € (09.07.2026) | за полгода — 899 € (27.05–07.06 и 28.08–08.09.2026, [Intel-отчёт, №1](../Intel/REPORT.md)) |
| Декод (камеры) | H.264 8 бит, HEVC 4:2:0 8/10 бит, AV1; **без 4:2:2** | то же + **HEVC 4:2:2 10 бит** (Resolve Studio, Premiere) |
| Кодирование | H.264, HEVC, **AV1** | H.264, HEVC; **AV1 нет** |
| Экран (внешнего монитора не будет — для цвета слабо у обоих) | 16" WUXGA IPS, 300 нит, 45 % NTSC (NBC: 57,6 % sRGB) | тот же: 300 нит, 45 % NTSC ([PSREF](https://psref.lenovo.com/Detail/IdeaPad/IdeaPad_Slim_5_16IRH10?M=83HS00BLGE)); у родственной 16IRH10R NBC намерил 57,7 % sRGB ([NBC](https://www.notebookcheck.com/Lenovo-IdeaPad-Slim-5-16-Laptop-im-Test-Intel-Core-i5-vs-AMD-Ryzen-5.1174964.0.html)) |
| Порты | 2× USB-C 10 Гбит/с, **HDMI 2.1**, microSD ([PSREF](https://psref.lenovo.com/Detail/IdeaPad/IdeaPad_Slim_5_16AKP10?M=83HY008CGE)) | 2× USB-C 5 Гбит/с, **HDMI 1.4b** (4K — только 30 Гц) ([PSREF](https://psref.lenovo.com/Detail/IdeaPad/IdeaPad_Slim_5_16IRH10?M=83HS00BLGE), [`candidates-lenovo-hp-dell.md`](../Intel/notes/candidates-lenovo-hp-dell.md)) |
| Нагрев | 42 дБ(A), холодный (NBC, версия с AI 5 330, [обзор](https://www.notebookcheck.net/Dual-debut-in-the-Lenovo-IdeaPad-Slim-5-16-Ryzen-AI-5-330-and-Radeon-820M-in-review.1166676.0.html)) | «runs uncomfortably hot»: 43 Вт при 96 °C ([LaptopMedia](https://laptopmedia.com/review/lenovo-ideapad-slim-5i-16-gen-10-review-a-great-laptop-held-back-by-our-bad-choices/), версия с 210H); под нагрузкой 50,4 дБ(A) ([NBC](https://www.notebookcheck.com/Lenovo-IdeaPad-Slim-5-16IRH10.1089950.0.html)) |
| Вес / батарея / гарантия | 1,85 кг / 60 Втч / 2 года | 1,85 кг / 60 Втч / 2 года |
| Оценки: Пробл. / Ремонт / Цена / Порт. / Мощн. (версия 3) | 7 / 8,5 / 6 / 7 / 5,5 (Мощн. было 6) | 6,5 / 8,5 / 7 / 7 / 5 (Мощн. было 4) |
| **Средн.** | **7** (6,8) | **7** (6,8) |

**Другие пары (idealo, 30.09.2026):**

| Класс | AMD | Intel |
|---|---|---|
| Самый дешёвый путь к 2×16 + 1 ТБ | `83HU004KGE` + SSD + зарядка — 920,54 € (AMD №2); с 1 ТБ с завода — `21MW00AYGE`, 998,99 € (Zen 3+, AMD №3) | Medion E15433 [`MD600023`](https://www.idealo.de/preisvergleich/OffersOfProduct/208688812_-e15433-md600023-medion.html) — **699,97 €** (i7-13620H, 2×16 DDR4 по [Medion](https://service.medion.com/de/product-detail/30041451), HDMI 1.4b, Wi-Fi 5); Acer Aspire Go 16 [`NX.JS9EG.005`](https://www.idealo.de/preisvergleich/OffersOfProduct/209373295_-aspire-go-16-ag16-71p-97gf-acer.html) — 849 € (i9-13900H, риск HEVC у Acer) |
| Распайка 32 ГБ, свежий CPU | Acer R2R1 `NX.JP0EG.00Z` — 1081,21 € (AI 7 350, OLED; AMD №10); Swift Air 16 OLED `NX.DL5EG.002` — 993,50 € (AI 5 330, OLED с замером; AMD №9) | ThinkPad E16 Gen 3 [`22AY003WGE`](https://www.idealo.de/preisvergleich/OffersOfProduct/209382343_-thinkpad-e16-g3-22ay003wge-lenovo.html) — 917,07 € (jacob.de, 19:22) + замена SSD 512 ГБ на Verbatim 1 ТБ 120,99 € = 1038,06 € (Core Ultra 5 228V, Arc 130V; Intel №6, средн. 6,5); HP OmniBook 7 AI 16-ay0770ng [`BM9T4EA`](https://www.idealo.de/preisvergleich/OffersOfProduct/206602335_-omnibook-7-ai-16-ay0770ng-hp.html) — **979,30 €** (Core Ultra 7 255H, Arc 140T, TB4; риск HEVC у потребительских HP; Intel №8) ([`idealo-prices.md`](../Intel/notes/idealo-prices.md)) |
| Лучшее «ждать» (справка: покупка сейчас) | ThinkBook 16 G9 AHP `21UT000RGE` — 1188,97 € (R7 250); за полгода ≤ 1100 € не был, за год мин. 1045 € | ThinkBook 16 G8 IAL [`21SK0083GE`](https://www.idealo.de/preisvergleich/OffersOfProduct/206151171_-thinkbook-16-g8-21sk0083ge-lenovo.html) — 1121,98 € (Ultra 5 225U; критик, 17:28), за полгода мин. 881,49 €, ≤ 1100 € — 173 дня; [`21SK007KGE`](https://www.idealo.de/preisvergleich/OffersOfProduct/206151089_-thinkbook-16-g8-21sk007kge-lenovo.html) — **1349,00 €** у easynotebooks (255H; критик, 17:28; днём было 1399 €, 1310,08 € — цена с купоном), 03.09 был 910 €, ≤ 1100 € — 89 дней за полгода ([`idealo-prices.md`](../Intel/notes/idealo-prices.md)) |
| Аппаратный декод 4:2:2 | Gigabyte A16 + RTX 5060 — 1286,56 € с планкой | Panther Lake: ThinkBook 16 G9 IPL [`21UR005AGE`](https://www.idealo.de/preisvergleich/OffersOfProduct/209497615_-thinkbook-16-g9-21ur005age-lenovo.html) — 1204,00 € (20:50), за полгода ≤ 1100 € не был; RTX 50 у MSI Cyborg 15 [`B2RWFKG-068`](https://www.idealo.de/preisvergleich/OffersOfProduct/206837107_-cyborg-15-b2rwfkg-068-msi.html) (Core 7 240H + RTX 5060) — 1199,00 € (Amazon, 20:50; днём 1079,10 €) + планка = 1386,56 €, дешевле него теперь AMD Gigabyte A16 (1286,56 €); Gigabyte A16 Intel [`CVHI3DE894SH`](https://www.idealo.de/preisvergleich/OffersOfProduct/206981767_-gaming-a16-cvhi3de894sh-gigabyte.html) — 1386,56 € ([`idealo-prices.md`](../Intel/notes/idealo-prices.md)) |
| Выбор на idealo (15–16", 32/1 ТБ) | 183 карточки | 589 карточек ([`notes/market-amd.md`](notes/market-amd.md)) |

Вывод по цене:
- в одном корпусе Intel дешевле примерно на 70 € (993,30 € в 17:27 или 989,05 € днём против 1059,99 €);
- в самом дешёвом классе («старый CPU + 2×16 с завода») Intel дешевле `21MW00AYGE` на 150–300 € (Acer, Medion);
- в бизнес-шасси ThinkBook AMD дешевле Intel примерно на 5–15 % ([`notes/market-amd.md`](notes/market-amd.md), § 6).

### 2. Что декодирует каждая ветка (кодек камеры неизвестен навсегда)

_Кодек не будет известен (ответ владельца 30.09, вечер). Таблица — не для выбора по камере, а чтобы видеть ширину декода: строку HEVC 4:2:2 закрывает Intel 11+, AMD — нет; H.264 4:2:2 10 бит в 1100 € не закрывает никто._

| Формат исходника | Примеры | AMD iGPU | Intel iGPU | Лучшее в 1100 € для этого формата |
|---|---|---|---|---|
| **HEVC 4:2:2 10 бит** | Sony A7 IV XAVC HS 4:2:2 ([Sony](https://helpguide.sony.net/ilc/2110/v1/en/contents/TP1000640834.html)), Canon R6 II H.265 10 бит ([Canon](https://www.canon-europe.com/cameras/eos-r6-mark-ii/specifications/)), Fujifilm H.265 4:2:2 ([Fuji](https://www.fujifilm-x.com/global/products/cameras/x-t5/specifications/)) | нет — декодирует процессор | **да**, любой Intel 11+ ([Puget, Resolve](https://www.pugetsystems.com/labs/articles/what-h-264-and-h-265-hardware-decoding-is-supported-in-davinci-resolve-studio-2122/), [Puget, Premiere](https://www.pugetsystems.com/labs/articles/what-h-264-and-h-265-hardware-decoding-is-supported-in-premiere-pro-2120/)) | **Intel** — `83HS00BLGE` (993,30 €) |
| **H.264 4:2:2 10 бит** | Sony XAVC S 10 бит и S-I, Panasonic S5II MOV 4:2:2 ([Panasonic](https://www.panasonic.com/uk/consumer/cameras-camcorders/lumix-mirrorless-cameras/lumix-s-full-frame-cameras/dc-s5m2.specs.html)), DJI Mavic 4 Pro H.264 ALL-I ([DJI](https://www.dji.com/global/mavic-4-pro/specs)) | нет | нет. Исключение — Panther Lake: декодирует в Resolve Studio 21 ([даташит Intel 872188](https://cdrdv2.intel.com/v1/dl/getContent/872188?fileName=872188-002.pdf), [readme Resolve 21](https://www.blackmagicdesign.com/support/readme/2cda7ec076ea4b25aaa007fc68a5cbfc)); Premiere и бесплатный Resolve — нет | **в 1100 € нет.** RTX 50 (AMD Gigabyte A16 — 1286,56 €, Intel MSI Cyborg 15 — 1386,56 €) или Panther Lake + Resolve Studio 21 (`21UR005AGE` — 1204 €). Иначе — прокси |
| **4:2:0** (H.264 8 бит, HEVC 8/10 бит) | смартфоны, GoPro 10 бит ([GoPro](https://community.gopro.com/s/article/10-Bit-Color-Video-Information?language=en_US)), DJI D-Log M ([DJI](https://www.dji.com/global/mini-4-pro/specs)), Sony XAVC HS 4:2:0, Panasonic H.265 | да | да | **равны**, решают цена и железо: AMD `83HY008CGE` (графика в 2,3 раза сильнее, AV1) или Intel `83HS00BLGE` (примерно на 70 € дешевле) |

- Без аппаратного декода HEVC 4:2:2 на AMD работает процессор. В экспорте Puget Bench (Resolve 20, 4K HEVC 4:2:2 10 бит) у Ryzen AI 9 HX 370 — 41,9 кадр/с, у Intel с Arc 140T — 56,3, то есть AMD медленнее примерно на 25 % ([Puget Bench](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/27/GPU/AMD%20Radeon%20890M%20Graphics/Intel%20Arc%20140T%20GPU%20%2816GB%29/)).
  Как это ощущается на живом таймлайне с несколькими дорожками 200 Мбит/с — не проверено.
- Бесплатный DaVinci Resolve под Windows открывает только профили, которые умеет Windows (H.264 8 бит, H.265 8/10 бит). Остальные профили и GPU-ускорение — в платной Studio: «More profiles and GPU acceleration in Studio» ([Blackmagic](https://documents.blackmagicdesign.com/SupportNotes/DaVinci_Resolve_21_Supported_Codec_List.pdf)). Использует ли бесплатная версия аппаратный декодер Windows (DXVA), Blackmagic не пишет — не проверено ([`notes/amd-codecs.md`](notes/amd-codecs.md)).

### 3. Тезис «Intel умеет всё то же, что AMD, плюс некоторые форматы аппаратно» — по пунктам

| Пункт | Intel | AMD | Итог |
|---|---|---|---|
| Декод H.264 8 бит, HEVC 4:2:0 8/10 бит, VP9, AV1 8/10 бит | да ([Puget](https://www.pugetsystems.com/labs/articles/what-h-264-and-h-265-hardware-decoding-is-supported-in-davinci-resolve-studio-2122/)) | да ([AMD AMF](https://github.com/GPUOpen-LibrariesAndSDKs/AMF/wiki/GPU%20and%20APU%20HW%20Features%20and%20Support)) | одинаково ✔ |
| Декод HEVC 4:2:2 10 бит | да, Intel 11+ (включая i7-13620H) ([Puget](https://www.pugetsystems.com/labs/articles/what-h-264-and-h-265-hardware-decoding-is-supported-in-premiere-pro-2120/), [Adobe](https://helpx.adobe.com/premiere/desktop/get-started/technical-requirements/supported-codecs-and-drivers-for-hardware-accelerated-decoding.html)) | нет ни в одном поколении, до RX 9000 и Radeon 800M: «All codecs are 4:2:0» ([AMD AMF](https://github.com/GPUOpen-LibrariesAndSDKs/AMF/wiki/GPU%20and%20APU%20HW%20Features%20and%20Support)) | **тезис верен** — главный «плюс» Intel |
| HEVC 4:4:4 и 12 бит (Resolve) | да | нет ([Puget](https://www.pugetsystems.com/labs/articles/what-h-264-and-h-265-hardware-decoding-is-supported-in-davinci-resolve-studio-2122/)) | верен (для камер почти неважно) |
| H.264 10 бит и 4:2:2 | нет до Arrow и Lunar Lake; Panther Lake — да, но только в Resolve Studio 21 ([даташит](https://cdrdv2.intel.com/v1/dl/getContent/872188?fileName=872188-002.pdf)) | нет | одинаково плохо; закрывает RTX 50 ([Puget](https://www.pugetsystems.com/labs/articles/what-h-264-and-h-265-hardware-decoding-is-supported-in-davinci-resolve-studio-2122/)) |
| Кодирование AV1 | Meteor и Arrow Lake — да; **Raptor Lake (i7-13620H, Core 5/7 2xxH) — нет** ([Intel media-driver](https://raw.githubusercontent.com/intel/media-driver/master/docs/media_features.md)) | Phoenix, Hawk Point и новее — да ([Linux amdgpu](https://github.com/torvalds/linux/blob/master/drivers/gpu/drm/amd/amdgpu/soc21.c)); Rembrandt (7x35, Ryzen 150/170) — нет | **тезис неверен** для лучшего Intel в бюджете |
| Графика для эффектов и цветокоррекции | Arc 130T/140T быстрее 780M/860M на 15–20 % ([Puget Bench](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/23/GPU/AMD%20Radeon%20860M%20Graphics/Intel%20Arc%20130T%20GPU%20%2816GB%29/)); UHD у Raptor Lake в 2,3 раза слабее 860M (Time Spy 1110 против 2565) | 890M быстрее Arc 140T: +15 % в Resolve 20, +18 % в Premiere ([Puget Bench](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/23/GPU/AMD%20Radeon%20890M%20Graphics/Intel%20Arc%20140T%20GPU%20%2816GB%29/)) | **зависит от модели**; в 1100 € AMD сильнее |
| Качество аппаратного кодирования | дискретный Arc — рядом с NVIDIA | RDNA 3 отстаёт ([Tom's Hardware](https://www.tomshardware.com/news/amd-intel-nvidia-video-encoding-performance-quality-tested)) | Intel лучше (iGPU отдельно не тестировали) |
| Отключение HEVC производителем | HP, Dell | HP, Dell — та же политика ([`notes/hevc-amd.md`](notes/hevc-amd.md)) | одинаково; без HEVC плохо обоим |

**Итог:** по декодированию камерных форматов тезис верен — Intel добавляет HEVC 4:2:2 (и 4:4:4/12 бит). Но «всё то же» — не так: переименованные Raptor Lake не кодируют AV1, а их графика слабее любой AMD в бюджете.
Подробно — [`notes/amd-codecs.md`](notes/amd-codecs.md), § 6.

### 4. Рекомендация

_Версия 3: камеру узнать нельзя, покупка сейчас, внешнего монитора нет. Финальный выбор — Intel HP `BM9T4EA#ABD`, запасной — Intel `83HS00BLGE`, «если главное — экран» — AMD №10 Acer R2R1 ([`../REPORT.md`](../REPORT.md), «Итог по обеим веткам» выше). Ниже — что следует для AMD по «Средн.»._
- **Ширина декода при неизвестном кодеке — в пользу Intel:** `83HS00BLGE` (993,30 €) декодирует всё, что AMD, плюс HEVC 4:2:2 и 4:4:4. Платить за это — слабой графикой, горячим корпусом и HDMI 1.4b.
- **Лучший AMD — №1 `83HY008CGE` (1059,99 €):** тот же корпус и память, графика в 2,3 раза сильнее, AV1 и HDMI 2.1; по «Средн.» — вровень с Intel №1.
  - Если предложение исчезнет — №5 `21MW007VGE` (1088,57 €) или дешёвый №2 `83HU004KGE` + SSD + зарядка (920,54 €).
  - Порты-бонус (USB4, SD, RJ45) — у ThinkBook №3, №4 и №5.
- **Экран без внешнего монитора** в AMD-бюджете — только Acer OLED: №9 Swift Air 16 (993,50 €, замер 100 % DCI-P3, но 4 ядра) или №10 Aspire 16 AI R2R1 (1081,21 €, Ryzen AI 7 350, замеров нет). В первые дни — DXVA Checker (HEVC) и проверка экрана. У Intel в бюджете хорошего экрана нет.
- **H.264 4:2:2 10 бит** (Sony XAVC S 10 бит, Panasonic MOV) в 1100 € не решается ни одной веткой — только процессор или прокси. RTX 50 (Gigabyte A16, MSI Cyborg 15) и Panther Lake `21UR005AGE` дороже потолка — это справка.

## Рынок Германии сейчас

Подробно — [`notes/market-amd.md`](notes/market-amd.md), общий рынок — [`../Intel/notes/market.md`](../Intel/notes/market.md).
- **У AMD в 3 раза меньше выбор:** 183 карточки 15–16" с 32 ГБ и 1 ТБ против 589 у Intel ([скан idealo](https://www.idealo.de/preisvergleich/ProductCategory/3751F699493-848110-1568565-2682401-7612877.html?sortKey=minPrice)).
  Фильтр AMD на idealo теряет карточки без поля «Prozessorhersteller», поэтому сканировали и без него ([`notes/candidates-idealo-sweep.md`](notes/candidates-idealo-sweep.md)).
- **Дешёвая полка AMD в 1100 € — это Zen 3+ (2022) и Zen 4 Hawk Point.** Zen 5 с 2×16 — один SKU (№1), остальные Zen 5 — с распайкой (Acer).
- **Докупать дорого:** SSD 1 ТБ подорожал за год в 3,4 раза (NV3: 42 → 142,89 €). Планка 16 ГБ DDR5 — от 187,56 €, но это одно предложение на маркетплейсе; у обычных магазинов 206,80–248,89 €.
- **Нового поколения ждать нет смысла:**
  - Hawk Point остаётся в младшем мейнстриме до второй половины 2027 года (утечка роадмапа — [Tom's Hardware](https://www.tomshardware.com/pc-components/cpus/amd-mobile-cpu-roadmap-leak-claims-zen-6-arrives-in-2027));
  - APU Medusa (Zen 6) — в 2027 году ([PC Gamer](https://www.pcgamer.com/hardware/processors/amd-confirms-next-gen-zen-6-cpus-to-launch-in-2026-and-medusa-apus-to-launch-in-2027/)).
- **Цены сейчас высокие:** №1 зимой стоил 896,28 €, №3 — 731,36 €. Ближайшие распродажи — Prime Deal Days 6–7.10 и Black Week 23–30.11 ([`../Intel/notes/market.md`](../Intel/notes/market.md)); это справка — покупка сейчас.
- **Сроки возврата (справка, не повод отбросить цену):** notebooksbilliger, Cyberport, Galaxus, coolblue, computeruniverse — 30 дней; Kaufland, expert, easynotebooks — 14 дней; у части мелких магазинов idealo срок не показывает (по закону — 14 дней) ([`notes/verify-lenovo.md`](notes/verify-lenovo.md), [`notes/verify-other-brands.md`](notes/verify-other-brands.md), [`notes/verify-gpu.md`](notes/verify-gpu.md)).

## Бренды: запчасти и надёжность

Общая оценка — [`../Intel/notes/brands.md`](../Intel/notes/brands.md). Для AMD-моделей ([`notes/brands-amd.md`](notes/brands-amd.md)):
1. **Lenovo ThinkBook / ThinkPad** — лучшая экосистема запчастей. Детали по MTM заказываются на [support.lenovo.com/de](https://support.lenovo.com/de/de/parts-lookup) ([Intel-проверка, п. 7.19](../Intel/notes/browser-check-r2r-market-brands.md)). Гарантия часто 1 год.
2. **Lenovo IdeaPad** — 2 года гарантии, запчастей и мануалов меньше.
3. **ASUS ExpertBook** — 36 месяцев гарантии (даташиты P1), но ремонт у ASUS часто дольше 14 дней.
   **ASUS Vivobook** — на AMD только схема «16 распаяно + слот».
4. **HP на AMD** — HEVC включён только у EliteBook 8 (от 1005 € за 512 ГБ); ProBook 4 / EliteBook 6 и 665/465 — выключен; у потребительских HP — риск.
5. **Dell на AMD** — HEVC отключён политикой, с 32 ГБ дороже 1600 €.
6. **Acer** — сервис-мануалов нет, риск HEVC в Германии; на AMD в 1100 € только распайка или Barcelo.
7. **Tuxedo, XMG, Framework** — хороший сервис или ремонтопригодность, но выше потолка на 390–830 €.

## Ловушки в названиях AMD

Подробно — [`notes/amd-cpu.md`](notes/amd-cpu.md).
- **Ryzen 200** = Hawk Point 2023 года: 7 260 = 8845HS, 7 250 = 8840U, **5 220 = 8540U** (2 полных ядра Zen 4 + 4 Zen 4c, 740M).
- **Ryzen 100** — смесь двух поколений: 110/130/150/160/170 — Rembrandt (Zen 3+, 2022); 125/155/165/180 — Hawk Point.
- **Серия 7000:** последняя цифра кодирует архитектуру.
  - 7x30 — Barcelo-R: Zen 3, Vega, DDR4, AV1 не декодирует;
  - 7x35 — Rembrandt-R: RDNA 2, драйверы в maintenance mode;
  - 7x20 — Mendocino: максимум 16 ГБ.
- **Ryzen 10 / Athlon 10** — Mendocino (Zen 2). **Ryzen AI 400** — те же кристаллы, что у AI 300 (Gorgon Point).
- **Цифра в имени ≠ число ядер:**
  - «7» с 6 ядрами — 7 7445HS, 7 217, AI 7 345, **AI 7 445**;
  - 4 ядра — 5 125, **AI 5 330**, AI 5 430;
  - без встроенной графики — 7435HS и 7235HS.
- **Одна планка режет 780M на 44 %** (Time Spy), а имя графики при этом не меняется ([NBC](https://www.notebookcheck.net/Testing-the-performance-of-AMD-Radeon-780M-760M-iGPUs-with-new-drivers.740311.0.html)).
- **Проверка за 30 секунд:** поле «Former Codename» на amd.com или «Prozessor Codename» в карточке idealo.

## Ловушка с отключённым HEVC

Подробно — [`notes/hevc-amd.md`](notes/hevc-amd.md).
- **HP** отключает аппаратный HEVC и на AMD: ProBook 465 G11, ProBook 4 G1a 14/16, EliteBook 665 G11, EliteBook 6 G1a 14/16 — это написано в QuickSpecs.
  У ProBook 4 G2a и EliteBook 6 G2a HEVC — «опция при заказе» (для розницы считать «нет»). У EliteBook 8 G1a/G2a — есть.
- **Потребительские HP:** у OmniBook 7 Aero 13 (AMD) в DXVA Checker нет ни одного профиля HEVC ([HP Community](https://h30434.www3.hp.com/t5/Notebook-Video-Display-and-Touch/H265-HEVC-HW-encoder-and-decoder-not-available/td-p/9431209)). У HP 255 G9 HEVC выключен ([Ars Technica](https://arstechnica.com/gadgets/2025/11/hp-and-dell-disable-hevc-support-built-into-their-laptops-cpus/)).
- **Dell** — та же политика для AMD: HEVC есть только с дискреткой, 4K, Dolby Vision или CyberLink.
- **Lenovo, ASUS, MSI, Medion, Gigabyte** — отключений не найдено; в PDF PSREF слова HEVC нет вовсе. **Acer** — риск.
- **Как выглядит на AMD:** пропадают `HEVC_VLD_Main` и `HEVC_VLD_Main10`, остаются H.264, VP9 и AV1. Профилей HEVC 4:2:2 у AMD нет и на «здоровой» машине — это ограничение AMD, а не блокировка.

## Кодеки и камера

_Кодек камеры и программа монтажа не будут известны никогда (ответ владельца 30.09, вечер) — поэтому в «Мощн.» ценится ширина аппаратного декода._


- **Ни один AMD не декодирует 4:2:2 и H.264 10 бит** — от Vega до RDNA 4 и Radeon 800M ([AMD AMF](https://github.com/GPUOpen-LibrariesAndSDKs/AMF/wiki/GPU%20and%20APU%20HW%20Features%20and%20Support), [Puget](https://www.pugetsystems.com/labs/articles/what-h-264-and-h-265-hardware-decoding-is-supported-in-davinci-resolve-studio-2122/)).
  Живой запрос VA-API к Radeon 780M на компьютере пользователя дал то же самое ([`notes/amd-codecs.md`](notes/amd-codecs.md), [LV1]).
- **Кодирование AV1** — с Phoenix и Hawk Point (VCN 4.0): это №1, 4, 7, 9, 10, 11 и 12. У Rembrandt (№2, 3, 5, 6, 8) AV1 только декодируется.
- **HandBrake** на AMD декодирует процессором, VCN использует только для кодирования ([HandBrake](https://handbrake.fr/docs/en/latest/technical/video-vcn.html)).
- **Обходы на AMD:** прокси (Premiere, Resolve), перекодирование в ProRes или DNxHR, съёмка в 4:2:0, связка с RTX 50 ([`notes/amd-codecs.md`](notes/amd-codecs.md), § 4).
- Выбор по камере — в разделе «AMD против Intel», п. 2.

## Право на ремонт

То же, что для Intel — [`../Intel/notes/right-to-repair.md`](../Intel/notes/right-to-repair.md):
- директива ЕС 2024/1799 ноутбуки пока не покрывает;
- в Германии ремонт по гарантии продлевает её на 12 месяцев (§ 475e Abs. 5 BGB);
- сменный аккумулятор обязателен только с 18.02.2027.
Запчасти пока гарантирует только добровольная политика бренда — лучше всех у ThinkPad и ThinkBook.

## Что проверить при покупке

1. **Парт-номер** в предложении совпадает с нужным. Особенно у Acer R2R1: его карточка смешана с R5H7 (16/512).
2. **В первые дни, до вскрытия корпуса:**
   - DXVA Checker: есть `HEVC_VLD_Main` и `HEVC_VLD_Main10` ([`notes/hevc-amd.md`](notes/hevc-amd.md), § 4);
   - тестовое кодирование H.265 через AMF: HandBrake, пресет «H.265 VCN 2160p 4K», или `ffmpeg -c:v hevc_amf`;
   - CPU-Z / HWiNFO: две планки, двухканальный режим;
   - LatencyMon — у IdeaPad Slim 5 16AKP10 NBC отметил «high latencies»;
   - экспорт 4K-ролика под нагрузкой: частоты, температура, шум.
3. **Для «+ SSD» и «+ планка» (№2, №6, №7, №8 и варианты `21MW009MGE`, `21UT004EGE`) — ставит владелец:** сначала проверки из п. 2, потом установка. Иначе при возврате магазин может удержать часть стоимости ([§ 357a BGB](https://www.gesetze-im-internet.de/bgb/__357a.html)).
   У ExpertBook P1 второй слот — M.2 2230, SSD 2280 в него не встанет. У V15 G6 (№8) SSD меняется — родной на 512 ГБ сохранить для сервиса ([`../Intel/REPORT.md`](../Intel/REPORT.md), «Что проверить при покупке»).
4. **№1 продаётся на маркетплейсе с одним предложением** — при заказе проверить, что это новый товар (не б/у и не B-Ware) и что указан именно `83HY008CGE`.
5. **Экран — внешнего монитора не будет, поэтому в срок возврата проверить сам экран:** равномерность, засветы, битые пиксели, мерцание на малой яркости.
   У OLED (№9, №10) — отдельно ШИМ (у №9 LaptopMedia нашёл ШИМ с малой амплитудой, у №10 не проверено) и есть ли режим sRGB. У остальных охват узкий (45 % NTSC) — это учтено в «Мощн.» ([`notes/displays.md`](notes/displays.md)).

## Вопросы к будущему владельцу

Ответы владельца 30.09 (вечер) — прежние вопросы закрыты:
1. ~~Чем снимает и в каком кодеке?~~ — **не будет известно никогда**; выбор должен быть надёжным для любых 4K-исходников (в «Мощн.» — ширина декода).
2. ~~Устраивает ли вариант «+ SSD»?~~ — **да**, планку и SSD владелец ставит сам: №2, №6, №7, №8 и варианты — полноценные.
3. ~~В какой программе будет монтаж?~~ — **неизвестно навсегда**. Справка: аппаратный декод в Resolve — только в Studio.
4. ~~Нужны ли USB4, SD-кардридер, Ethernet?~~ — **приятный бонус**, не требование (5 % «Мощн.»).
5. ~~Будет ли внешний монитор?~~ — **нет**; экран оценивается как есть (25 % «Мощн.»).
6. ~~Можно ли подождать до распродаж?~~ — **нет, покупка сейчас**; «ждать» (№11, №12) — справка.

Открытых вопросов к владельцу по критериям не осталось. Открыто у пользователя: отправлять ли вопросы продавцам (`../Intel/REPORT.md`, «Вопросы продавцам»).

## Дальше

- **Перед покупкой пересчитать цены:** 30.09 они менялись несколько раз за день. У №1 — одно предложение на маркетплейсе; планка Kingston за 187,56 € (для №6 и №7) — тоже одно ([`notes/prices-final.md`](notes/prices-final.md)).
- **Справка (покупка сейчас):** Preiswecker на idealo нужен, только если покупку отложат — `83HY008CGE`, `21UT000RGE` (≤ 1100 €), `3VHK3DE894SH` (≤ 912 €), `83HY0061GE` (новое предложение); поставить его может только пользователь.
- Итоговый выбор между Intel и AMD — [`../REPORT.md`](../REPORT.md).
- Сравнение сверено с `../Intel/REPORT.md` версии 3 (30.09.2026, вечер).
