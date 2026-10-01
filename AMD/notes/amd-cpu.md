# AMD Ryzen для монтажа 4K: имена, кремний, память, ловушки

_Собрано 30.09.2026 на компьютере пользователя (curl с IP в Германии). Ссылки — в квадратных скобках, список в разделе «Источники».
Спецификации — со страниц моделей на amd.com (поля Former Codename, Processor Architecture, System Memory Type, Memory Channels, Max. Memory, Graphics Model, NPU TOPS).
Список моделей — из карты сайта AMD [AS]: там 143 страницы мобильных Ryzen/Athlon, все скачаны и разобраны.
Бенчмарки — Notebookcheck (NBC). «Не проверено» — первоисточника не нашёл.
Кодеки здесь не разбираю: только строка «какой VCN». Подробно — `amd-codecs.md`._

## Коротко

1. **Старый кремний под новыми именами — у AMD его больше, чем у Intel:**
   - **Ryzen 200** (2025–2026) — это Hawk Point, то есть Ryzen 8040 2023 года.
     Ryzen 7 260 = 8845HS = 7840HS, у 7840HS только NPU медленнее [N6][N7]. Ryzen 7 250 = 8840U [N8]. Ryzen 5 220 = 8540U = 7545U [N9].
   - **Ryzen 100** (с 01.10.2025) — смесь двух поколений:
     - 110/130/150/160/170 — Rembrandt, Zen 3+ 2022 года [A9];
     - 125/155/165/180 — Hawk Point, Zen 4, с 02.06.2026 [A10][A11].
   - **Ryzen 10 и Athlon 10** (Ryzen 3 30, Ryzen 5 40, Athlon Silver 10, Athlon Gold 20; 01.10.2025) — Mendocino, Zen 2 [A2][A3].
   - **Ryzen AI 400** (Gorgon Point, 05.01.2026) — те же кристаллы, что у Ryzen AI 300. По таблице драйвера Linux версии блоков у них совпадают [K1].
     Строки есть только для AI 9 475/470/465, AI 7 450 и AI 5 440/435; для AI 5 430 и AI 7 445 — **не проверено** (проверка 30.09.2026).
     Ryzen AI 7 450 отличается от AI 7 350 только частотой (+100 МГц) и поддержкой LPDDR5X‑8533 [N11].
   - **Ryzen 400 без «AI»** (Ryzen 5 439, Ryzen 7 449; анонс 07.08.2026 по NBC) — Gorgon Point без NPU [A33][N10].
   - На amd.com у Ryzen 3 3100U и Ryzen 5 3501U (Picasso, Zen+, 12 нм, поколение 2019 года) стоит дата выхода «Q2 2026» [A35].
2. **Где 2×16 ГБ SO‑DIMM невозможны:**
   - **Mendocino** (7x20U, Ryzen 10, Athlon): только LPDDR5 и **максимум 16 ГБ** — 32 ГБ не будет вообще [A1][A2][A3].
   - **Strix Halo** (Ryzen AI Max/Max+): только распаянная LPDDR5X, шина 256 бит (у Max PRO 380 — 128 бит) [A28][A29].
   - Остальные семейства по спецификации AMD работают с DDR5 SO‑DIMM (Barcelo‑R — с DDR4).
     Но ставить ли слоты, решает производитель ноутбука.
     Ноутбуки на Strix/Krackan Point часто выходят с распайкой LPDDR5X: TUF A16 2024 [N24], Zenbook S 16, ProArt [N5], Swift Go 16 AI [N26].
3. **Одна планка режет iGPU почти вдвое.** Radeon 780M в HP EliteBook 845 G10 в 3DMark Time Spy Graphics:
   2659 баллов с двумя планками, 1496 с одной (−44 %). С одной планкой 780M лишь чуть быстрее старой Vega 8 [N3].
   У AMD, в отличие от Intel, iGPU при этом **не меняет имя** — по названию одноканал не видно.
4. **Ловушки в номерах внутри новых серий:**
   - «Ryzen 7» с 6 ядрами: 7 7445HS, 7 217 [A14][AS]. «Ryzen AI 7» с 6 ядрами: AI 7 345, AI 7 445 [A27][A32].
   - 4 ядра: Ryzen 5 125, AI 5 330, AI 5 430 [A11][A26][AS].
   - Ryzen 7 7435HS и Ryzen 5 7235HS **без встроенной графики** [A8].
   - В сериях 100/200/400 нет буквы U/HS: 250 — 28‑ваттный (бывший U), 260 — 45‑ваттный (бывший HS) [A17][A39].
5. **Драйверы:**
   - Radeon на RDNA 1/2 с Adrenalin 25.10.2 (страница AMD обновлена 29.10.2025) переведены в «maintenance mode» [AR1][T4].
     Это касается и iGPU 610M/660M/680M, то есть Ryzen 7x20, 7x35, Rembrandt в Ryzen 100, Dragon Range и Fire Range.
     03.11.2025 AMD уточнила: новые игры, оптимизации и исправления для них будут, а новые функции — только для RDNA 3/4 [T3][T5].
   - Vega (Ryzen 7x30) с 2023 года получает только критичные исправления, отдельным пакетом [T6][T7][AR3].
   - AMD прямо рекомендует для ноутбуков драйверы производителя [AR1][AR2].
6. **iGPU AMD больше не лучше Intel.** Средние значения Time Spy Graphics по NBC:
   - Arc 140T (Core Ultra 7 255H) — 3843, Radeon 890M — 3331, 860M — 2565;
   - Arc 8‑core (Core Ultra 7 155H) — 3270, Radeon 780M — 2808 [N2].
   Это 3D‑тест (игры); для монтажа важнее медиадвижок — см. `amd-codecs.md`.
   По процессору (Cinebench R23 Multi, медиана NBC) — паритет: Ryzen 7 260 — 17 212, Core Ultra 7 255H — 17 845, Core Ultra 7 155H — 15 028 [N1].
7. **Лимит мощности важнее имени.** HX 370 в Cinebench R23: 16 522 в Zenbook S 16 (28 Вт) и 23 902 в ROG Zephyrus G14 (80 Вт), разница +45 % [N20].
8. **Выбор на ~1100 € с 2×16 SO‑DIMM:**
   - лучше всего — Ryzen AI 7 350/450, AI 9 365 или HX 370/470 со слотами, но такие SKU редки;
   - реалистично — Ryzen 7 260/250, 8845HS или 7840HS с двумя слотами;
   - с RTX 50 — любой Zen 4/5, включая HX.
   - Не брать: Mendocino (32 ГБ невозможно), Barcelo‑R, Picasso, урезанные AI 5 330/430, Ryzen 5 125, Ryzen 5 220, Ryzen 3 205.
   - Rembrandt (7x35 и Ryzen 100 на Zen 3+) — только если очень дёшево.
9. **VCN по семействам** [K1]:
   - 7x30 — VCN 2.2;
   - 7x20 и 7x35 — 3.1.1;
   - Dragon Range — 3.1.2;
   - Phoenix и Hawk Point (7x40, 8x40, 200) — 4.0.2;
   - Strix, Krackan, Gorgon — 4.0.5;
   - Strix Halo — 4.0.6.
   Что это даёт для кодеков — в `amd-codecs.md`.

---

## 1. Имя → кремний

### 1.1. Имя в прайсе → что внутри → год

Всё, что есть в карте сайта AMD в разделе мобильных процессоров [AS], плюс Athlon 7x20U: их страниц на amd.com уже нет (404), данные — по NBC [N28].

| Имя в прайсе | Что внутри (Former Codename) | Ядра | iGPU | Выход |
|---|---|---|---|---|
| Athlon Silver 7120U, Athlon Gold 7220U | Mendocino, Zen 2 | 2/2, 2/4 | 610M | 20.09.2022 [N28] |
| **Athlon Silver 10, Athlon Gold 20** («Athlon 10 Series») | Mendocino, Zen 2 = 7120U/7220U (3,5/3,7 ГГц, L3 2/4 МБ) | 2/2, 2/4 | 610M | 01.10.2025 [A3][AS][N28] |
| Ryzen 3 7320U, Ryzen 5 7520U (и 7320C/7520C для Chromebook) | Mendocino, Zen 2 | 4/8 | 610M | 20.09.2022 [A1] |
| **Ryzen 3 30, Ryzen 5 40** («Ryzen 10 Series») | Mendocino, Zen 2 = 7320U/7520U (4,1/4,3 ГГц) | 4/8 | 610M | 01.10.2025 [A2][N19] |
| Ryzen 5 7525U | кодовое имя на amd.com не указано; Zen 2 + RDNA 2, 8 CU | 4/8 | «Radeon Graphics» | **не проверено** [A36] |
| Ryzen 3 7330U, 5 7430U, 5 7530U, 7 7730U | Barcelo‑R, Zen 3 (по сути Cezanne 2021; 7530U = 5625U +200 МГц) | 4–8 | Vega, 6–8 CU | Q1 2023 (7430U — Q4 2023) [A4][A5][N17] |
| Ryzen 3 7335U, 5 7535U/7535HS/7533HS, 7 7735U/7735HS/7736U | Rembrandt‑R, Zen 3+ (= Ryzen 6000) | 4–8 | 660M / 680M | Q1–Q2 2023 (7533HS — Q3 2024) [A6][A7][A37] |
| Ryzen 5 7235HS, Ryzen 7 7435HS | Rembrandt‑R, Zen 3+ | 4, 8 | **нет** («Discrete Graphics Card Required») | [A8] |
| **Ryzen 3 110, 5 130, 5 150, 7 160, 7 170** («Ryzen 100») | Rembrandt, Zen 3+ = 7335U, 7535U, 7535HS, 7735U, 7735HS | 4–8 | 660M / 680M | 01.10.2025 [A9][N16] |
| **Ryzen 5 125, 7 155, 7 165, 9 180** («Ryzen 100») | Hawk Point (у NBC — Hawk Point Refresh), Zen 4 | 4–8 | 740M / 760M / 780M | 02.06.2026 [A10][A11][N14][N15] |
| Ryzen 3 7440U, 5 7540U, 5 7545U, 7 7445HS | Phoenix (у 7440U, 7545U и 7445HS — Zen 4 + Zen 4c, у NBC — Phoenix 2) | 4–6 | 740M | 2023 [A13][A14] |
| Ryzen 5 7640U/7640HS, 7 7840U/7840HS, 9 7940HS | Phoenix, Zen 4 | 6–8 | 760M / 780M | 2023 [A12] |
| Ryzen 3 8440U, 5 8540U | Hawk Point, Zen 4 + Zen 4c | 4–6 | 740M | дата на amd.com не указана; семейство — с 12.2023 [A16][A15] |
| Ryzen 5 8640U/8640HS/8645HS, 7 8840U/8840HS/8845HS/8745HS, 9 8945HS | Hawk Point, Zen 4 | 6–8 | 760M / 780M | с 06.12.2023 (8745HS — 18.06.2024) [A15] |
| **Ryzen 3 210, 5 220, 5 230, 5 240, 7 250, 7 260, 9 270** («Ryzen 200») | Hawk Point = 8440U, 8540U, 8640U, 8645HS, 8840U, 8845HS, 8945HS | 4–8 | 740M / 760M / 780M | 18.02.2025 [A17][A18][A38][A39] |
| **Ryzen 3 205, 5 216, 5 224, 5 225, 7 217, 7 249, 7 253** («Ryzen 200», добавлены) | Hawk Point, пониженные частоты | 4–8 | 740M / 760M / 780M | 02.06.2026 [A19][AS] |
| Ryzen 5 7645HX, 7 7745HX, 9 7845HX, 9 7945HX, 9 7945HX3D; 7 7840HX, 9 7940HX | Dragon Range, Zen 4 (чиплеты от десктопа) | 6–16 | 610M | 28.02.2023; 7840HX/7940HX — 17.01.2024 [A20] |
| Ryzen 7 8745HX, 7 8840HX, 9 8940HX, 9 8945HX | Dragon Range (у NBC — Dragon Range refresh), Zen 4 | 8–16 | 610M | 23.04.2025 [A21] |
| Ryzen 9 9850HX, 9 9955HX, 9 9955HX3D | Fire Range, Zen 5 (чиплеты от десктопа) | 12–16 | 610M | CES 2025 [A22][N23] |
| Ryzen AI 9 HX 370/375, AI 9 365, AI 7 PRO 360 | Strix Point, Zen 5 + Zen 5c | 8–12 | 880M / 890M | анонс в июне 2024 (NBC) [A23][A24][N20] |
| Ryzen AI 7 350, AI 7 345, AI 5 340 | Krackan Point, Zen 5 + Zen 5c | 6–8 | 840M / 860M | 15.01–18.02.2025 [A25][A27] |
| Ryzen AI 5 330 | Krackan Point 2 (NBC), 1× Zen 5 + 3× Zen 5c | 4 | 820M | 30.07.2025 [A26][N13] |
| Ryzen AI Max 385/390, Max+ 395; Max PRO 380 | Strix Halo, Zen 5 | 6–16 | 8040S / 8050S / 8060S | не позже 07.2025 (дата на amd.com не указана) [A28][A29][AR4] |
| Ryzen AI Max+ 388, Max+ 392 | Strix Halo | 8, 12 | 8060S | январь 2026 (NBC) [AS][N22] |
| Ryzen AI 5 430/435, AI 5 PRO 440, AI 7 445/450, AI 9 465, AI 9 HX 470/475 | Gorgon Point, Zen 5 + Zen 5c — кристаллы Strix/Krackan | 4–12 | 840M … 890M | 05.01.2026 [A30][A31][A32][K1] |
| **Ryzen 5 439, Ryzen 7 449** («Ryzen 400», без «AI») | Gorgon Point без NPU | 6, 8 | 840M / 860M | анонс 07.08.2026 (NBC) [A33][N10] |
| Ryzen AI Max PRO 485/490, Max+ PRO 495 | Gorgon Halo, Zen 5 | 8–16 | 8050S / 8065S | 2026 (дата на amd.com не указана) [A34][AR5][W1] |
| Ryzen 3 3100U, Ryzen 5 3501U | Picasso, Zen+ | 2, 4 | Vega 8 | на amd.com — «Q2 2026» [A35] |

Замечания:
- На странице Ryzen AI 9 HX 370 amd.com указывает дату выхода 28.07.2025 [A23], а NBC пишет, что чип «debuted in June 2024» [N20]. Похоже на ошибку в поле страницы AMD.
- Страница `amd-ryzen-5-7600` в разделе ноутбуков на деле описывает Ryzen 3 7320C (ошибка сайта AMD) — в таблицу не включал.
- У NBC Ryzen 7 165 технически близок к 8640U, а Ryzen 9 180 — к 8745H [N14][N15].
- Процессоры для рынка Китая (NBC упоминает «Ryzen 7 H 255», «Ryzen AI 7 H 450» [N11][N15]) в Германии не встречал — не проверено.

### 1.2. Правило расшифровки серии 7000 и почему новые серии его ломают

**Серия 7000 (с 2023 года), четыре цифры и буква** [T1][T2]:

| Позиция | Что значит | Пример: Ryzen 7 **7735**HS |
|---|---|---|
| 1‑я цифра | «год портфеля»: 7 = 2023, 8 = 2024 | 7 |
| 2‑я | сегмент: 1 — Athlon Silver, 2 — Athlon Gold (по именам 7120U/7220U [N28]), 3–4 — Ryzen 3, 5–6 — Ryzen 5, 7–8 — Ryzen 7, 8–9 — Ryzen 9 | 7 |
| 3‑я | **архитектура:** 2 — Zen 2, 3 — Zen 3/3+, 4 — Zen 4, 5 — Zen 5 | 3 |
| 4‑я | 0 — младшая версия, 5 — старшая (для Zen 3: 0 — Zen 3 и Vega, 5 — Zen 3+ и RDNA 2) | 5 |
| буква | U — 15–28 Вт, HS — 35–54 Вт [A6], HX — 55 Вт и выше, C — Chromebook, e — ≤9 Вт | HS |

На практике: 7x20 — Mendocino, 7x30 — Barcelo‑R, 7x35 — Rembrandt‑R, 7x40 — Phoenix, 7x45HX — Dragon Range (таблица 1.1).

**Где правило ломается:**
- **Год ничего не значит.** Hawk Point (8x40) — тот же кристалл, что Phoenix 2023 года [N7][K1]. Ryzen 8x45HX вышли 23.04.2025, но это Dragon Range 2023 года [A21].
- **Серия 200** — три цифры, без архитектуры и без U/HS.
  - Под номером 2xx весь 2025–2026 год продаётся только Zen 4 Hawk Point [A17][A18][A19].
  - 28‑ваттный 250 и 45‑ваттный 260 различаются только последней цифрой [A39][A17].
- **Серия 100** — одна серия, две архитектуры:
  - Ryzen 7 160 — Zen 3+ (Rembrandt), а Ryzen 7 165 — Zen 4 (Hawk Point) [A9][A10][AS];
  - по номеру их не отличить.
- **Серии 10 и Athlon 10** — две цифры. Это Mendocino, 2022 год [A2][A3].
- **Ryzen AI 300 и 400** — номер кодирует только поколение продукта и уровень.
  400 — не новая архитектура, а те же кристаллы Strix/Krackan [K1][N11][N12].
- **Ryzen 400 без «AI»** — тот же Gorgon Point, только без NPU [A33][N10].

### 1.3. Семейства: ядра, техпроцесс, iGPU, NPU, память, вердикт

| Семейство (примеры) | Ядра | Техпроцесс | iGPU: CU, архитектура | VCN [K1] | NPU | Память (amd.com) | Вердикт |
|---|---|---|---|---|---|---|---|
| **Mendocino**: 7520U, 7320U, Ryzen 5 40, Athlon Gold 20 [A1][A2][A3] | Zen 2, 2–4 | TSMC 6 нм | 610M, 2 CU, RDNA 2 [N2] | 3.1.1 | нет | **только LPDDR5‑5500, макс. 16 ГБ** | **ловушка: 32 ГБ невозможно** |
| **Barcelo‑R**: 7530U, 7730U [A4][A5] | Zen 3, 4–8 | TSMC 7 нм | Vega, 6–8 CU, GCN 5 [W1] | 2.2 | нет | DDR4‑3200 или LPDDR4X‑4267, до 64 ГБ | **ловушка:** кремний 2021 года, DDR4, драйвер Vega |
| **Rembrandt‑R** и Rembrandt в Ryzen 100: 7735HS, 7535HS, 7335U, Ryzen 7 170 [A6][A7][A9] | Zen 3+, 4–8 | TSMC 6 нм | 660M (4–6 CU) или 680M (12 CU), RDNA 2 | 3.1.1 | нет | DDR5‑4800 SO‑DIMM или LPDDR5‑6400, до 64 ГБ; у 7736U — только LPDDR5 [A37] | старый (2022); брать только очень дёшево |
| Rembrandt‑R без iGPU: 7435HS, 7235HS [A8] | Zen 3+, 4–8 | TSMC 6 нм | **нет** | — | нет | DDR5‑4800 | только с дискреткой |
| **Phoenix**: 7840HS, 7640HS, 7840U; Phoenix 2: 7545U, 7440U, 7445HS [A12][A13][A14] | Zen 4 (у Phoenix 2 — Zen 4 + Zen 4c), 4–8 | TSMC 4 нм | 740M (4 CU), 760M (8), 780M (12), RDNA 3 | 4.0.2 | 10 TOPS у 7640U/7840U; у Phoenix 2 поля NPU нет | DDR5‑5600 SO‑DIMM или LPDDR5X‑7500 | **ок** |
| **Hawk Point**: 8845HS, 8840U, Ryzen 7 260/250, Ryzen 9 270, Ryzen 5 240/230; Ryzen 100 Zen 4 [A15][A17][A38][A39][A10] | Zen 4, 6–8; у 8540U, 8440U, Ryzen 5 220, Ryzen 3 210 — Zen 4 + Zen 4c, 4–6 | TSMC 4 нм | 740M / 760M / 780M, RDNA 3 | 4.0.2 | 16 TOPS; у 8540U, 8440U, 5 220, 3 210, 8745HS — нет | DDR5‑5600 SO‑DIMM или LPDDR5X‑7500; у Ryzen 100 на Zen 4 — DDR5‑4800 (FP7r2): в поле «System Memory Type» только DDR5, а в «Max Memory Speed» указан и LPDDR5x‑7500 — противоречие на странице AMD (уточнено при проверке, [A10][A11]) | **ок, лучший по цене:** 8 ядер + 780M + слоты |
| **Dragon Range**: 7845HX, 7945HX, 8945HX [A20][A21] | Zen 4, 6–16 | TSMC 5 нм + I/O 6 нм | 610M, 2 CU | 3.1.2 | нет | **только DDR5‑5200 SO‑DIMM**, до 64 ГБ | ок **только с дискреткой** |
| **Fire Range**: 9955HX, 9955HX3D, 9850HX [A22] | Zen 5, 12–16 | TSMC 4 нм + I/O 6 нм | 610M, 2 CU | в таблице драйвера нет — **не проверено** | нет | только DDR5‑5600 SO‑DIMM, до 96 ГБ | ок только с дискреткой |
| **Strix Point**: AI 9 HX 370/375, AI 9 365 [A23][A24] | Zen 5 + Zen 5c, 10–12 | TSMC 4 нм | 880M (12 CU), 890M (16 CU), RDNA 3.5 | 4.0.5 | 50 TOPS (HX 375 — 55) | DDR5‑5600 SO‑DIMM или LPDDR5X‑8000, до 256 ГБ | **лучший**, если в ноутбуке слоты |
| **Krackan Point**: AI 7 350, AI 5 340; AI 7 345; AI 5 330 [A25][A27][A26] | Zen 5 + Zen 5c, 4–8 | TSMC 4 нм | 860M (8 CU), 840M (4), 820M (2), RDNA 3.5 | 4.0.5 | 50 TOPS | DDR5‑5600 SO‑DIMM или LPDDR5X‑8000 | **AI 7 350 — ок/лучший**; AI 5 330 — ловушка |
| **Gorgon Point**: AI 9 HX 470/475, AI 9 465, AI 7 450/445, AI 5 435/430; Ryzen 7 449, Ryzen 5 439 [A30][A31][A32][A33] | как у Strix/Krackan [K1] | TSMC 4 нм | 840M … 890M, RDNA 3.5 | 4.0.5 | 50–60 TOPS; у 439/449 NPU нет [N10] | DDR5‑5600 SO‑DIMM или LPDDR5X‑8000/8533 | ок (= AI 300, выше частоты) |
| **Strix Halo**: AI Max+ 395/392/388, Max 390/385, Max PRO 380 [A28][A29] | Zen 5, 6–16 | TSMC 4 нм | 8060S (40 CU), 8050S (32), 8040S (16), RDNA 3.5 [N2] | 4.0.6 | 50 TOPS | **только LPDDR5X‑8000**, 256 бит (у 380 — 128 бит), до 128 ГБ | **2×16 невозможно** |
| **Gorgon Halo**: AI Max+ PRO 495, Max PRO 490/485 [A34] | Zen 5, 8–16 | TSMC 4 нм | 8065S (40 CU), 8050S (32) | не проверено | 55 TOPS у 495 | только LPDDR5X‑8533, 256 бит, до 192 ГБ | 2×16 невозможно |
| **Picasso**: 3100U, 3501U [A35] | Zen+, 2–4 | 12 нм | Vega 8 | 1.0 | нет | до 2400 МТ/с | **ловушка** |

Проверка по amd.com (поле «System Memory Type»):
- **Только распаянная память:** Mendocino (LPDDR5), Ryzen 7 7736U (LPDDR5), Strix Halo и Gorgon Halo (LPDDR5X) [A1][A37][A28][A34].
- **Только SO‑DIMM:** Dragon Range и Fire Range (DDR5) [A20][A22].
- **Оба варианта:** все остальные.
  Страница AMD называет ещё и тип корпуса: DDR5 (FP7r2 или FP8) и LPDDR5X (FP7 или FP8) [A15][A23]. Будет ли слот, решает производитель ноутбука.

### 1.4. Карта переименований

Совпадают ядра, частота, кеш, iGPU, TDP и NPU (данные amd.com; сверку «один в один» делал я по полям страниц).

| Новое имя | = 8000 / 7000 | Ядра, iGPU, TDP, частота | Источник |
|---|---|---|---|
| Ryzen 9 270 | 8945HS | 8 Zen 4, 780M, 45 Вт, 5,2 ГГц | [A40][A41] |
| Ryzen 7 260 | 8845HS ≈ 7840HS | 8 Zen 4, 780M, 45 Вт, 5,1 ГГц, NPU 16 TOPS | [A17][A15][A12][N6] |
| Ryzen 7 250 | 8840U / 8840HS | 8 Zen 4, 780M, 28 Вт, 5,1 ГГц | [A39][N8] |
| Ryzen 5 240 | 8645HS | 6 Zen 4, 760M, 45 Вт, 5,0 ГГц | [A38] |
| Ryzen 5 230 | 8640U / 8640HS | 6 Zen 4, 760M, 28 Вт, 4,9 ГГц | [AS] |
| Ryzen 5 220 | 8540U = 7545U | 2 Zen 4 + 4 Zen 4c, 740M, 28 Вт, 4,9 ГГц, без NPU | [A18][A16][A13][N9] |
| Ryzen 3 210 | 8440U ≈ 7440U | 1 Zen 4 + 3 Zen 4c, 740M, 4,7 ГГц | [AS] |
| Ryzen 7 170 / 160 | 7735HS / 7735U | 8 Zen 3+, 680M, 45 / 28 Вт, 4,75 ГГц | [A9][A6][N16] |
| Ryzen 5 150 / 130 | 7535HS / 7535U | 6 Zen 3+, 660M 6 CU, 45 / 28 Вт, 4,55 ГГц | [AS][A7] |
| Ryzen 3 110 | 7335U | 4 Zen 3+, 660M 4 CU, 4,3 ГГц | [AS] |
| Ryzen 5 40 / Ryzen 3 30 | 7520U / 7320U | 4 Zen 2, 610M, 15 Вт, 4,3 / 4,1 ГГц | [A2][A1][N19] |
| Athlon Gold 20 / Silver 10 | Athlon Gold 7220U / Silver 7120U | 2 Zen 2, 610M, 3,7 / 3,5 ГГц, L3 4 / 2 МБ | [A3][AS][N28] |
| Ryzen AI 7 450 | AI 7 350 | 4 Zen 5 + 4 Zen 5c, 860M; +100 МГц, LPDDR5X‑8533 | [A30][A25][N11] |
| Ryzen AI 7 445 | ≈ AI 5 340 (по NBC) | 2 Zen 5 + 4 Zen 5c, 840M, 8 МБ L3 | [A32][N12] |
| Ryzen AI 9 HX 470 / 465 | HX 370 / 365 | тот же кристалл Strix Point [K1] | [A31][A23] |
| Ryzen AI 5 435 / PRO 440 | кристалл AI 5 330 (Krackan Point 2), но **не копия** | тот же кристалл [K1]; конфигурация другая: 435 — 2 Zen 5 + 4 Zen 5c, PRO 440 — 3 + 3, обе 840M 4 CU; у AI 5 330 — 1 + 3 и 820M 2 CU (исправлено при проверке: было «= AI 5 330») | [K1][A26][A42][A43] |
| Ryzen 7 449 | AI 7 450 без NPU, частоты ниже | 8 ядер, 860M | [A33][N10] |

Сверка «один в один» по кристаллам: таблица APU драйвера Linux даёт одинаковые версии блоков (GC, VCN, DCN, SDMA) [K1]:
- у Phoenix и Hawk Point;
- у Strix Point и Ryzen AI 9 HX 475/470/465;
- у Krackan Point 350 и AI 7 450;
- у Krackan Point 330 и AI 5 440/435.

---

## 2. Память и встроенная графика

### 2.1. iGPU Radeon: CU и скорость

Time Spy Graphics — среднее NBC по всем тестам, n — число тестов [N2]. Архитектура — по NBC и amd.com.

| iGPU | CU | Архитектура | Где стоит | Time Spy Graphics |
|---|---|---|---|---|
| Radeon 610M | 2 | RDNA 2 | Mendocino, Dragon Range, Fire Range | 515 (n7) |
| Vega («Radeon Graphics») | 6–8 | GCN 5 (Vega) | Barcelo‑R 7x30 | Vega 8: 738 (n6) |
| Radeon 660M | 4–6 | RDNA 2 | 7x35 Ryzen 3/5, Ryzen 100 (Zen 3+) | 1535 (n13) |
| Radeon 680M | 12 | RDNA 2 | 7x35 Ryzen 7, Ryzen 7 160/170 | 2303 (n41) |
| Radeon 740M | 4 | RDNA 3 | 7440U/7540U/7545U, 8540U, Ryzen 5 220 и т. п. | 1527 (n5) |
| Radeon 760M | 8 | RDNA 3 | 7640HS, 8640HS/8645HS, Ryzen 5 230/240 | 2281 (n5) |
| Radeon 780M | 12 | RDNA 3 | 7840HS, 8845HS, Ryzen 7 250/260, Ryzen 9 270 | 2808 (n81) |
| Radeon 820M | 2 | RDNA 3.5 | AI 5 330 | 786 (n1) |
| Radeon 840M | 4 | RDNA 3.5 | AI 5 340, AI 7 345/445, AI 5 430/435, Ryzen 5 439 | 1415 (n7) |
| Radeon 860M | 8 | RDNA 3.5 | AI 7 350/450, Ryzen 7 449 | 2565 (n23) |
| Radeon 880M | 12 | RDNA 3.5 | AI 9 365/465, AI 7 PRO 360 | 3335 (n8) |
| Radeon 890M | 16 | RDNA 3.5 | AI 9 HX 370/375/470/475 | 3331 (n33) |
| Radeon 8040S | 16 | RDNA 3.5 | AI Max PRO 380 | 4033 (n1) |
| Radeon 8050S | 32 | RDNA 3.5 | AI Max 385/390, Max PRO 485/490 | 9502 (n2) |
| Radeon 8060S | 40 | RDNA 3.5 | AI Max+ 388/392/395 | 11 018 (n13) |
| Radeon 8065S | 40 | RDNA 3.5 | AI Max+ PRO 495 | тестов у NBC нет |

Для сравнения по тому же списку: Intel Arc 140T — 3843, Arc 8‑core (155H) — 3270, Arc 140V — 4044, UHD 64 EU (i7‑13620H) — 1110,
RTX 4050 Laptop — 8125, RTX 5060 Laptop — 11 937 [N2].

### 2.2. Одноканал режет iGPU

- **Замер NBC** — один и тот же HP EliteBook 845 G10 (Ryzen 9 PRO 7940HS, Radeon 780M), с одной планкой и с двумя, 11.08.2023 [N3]:

  | Тест | 2 планки | 1 планка | Потеря |
  |---|---|---|---|
  | 3DMark Time Spy Graphics | 2659 | 1496 | −44 % |
  | 3DMark Fire Strike Graphics | 7800 | 4550 | −42 % |
  | 3DMark 11 GPU | 11 811 | 7868 | −33 % |

  Вывод NBC: с одной планкой 780M чаще медленнее Iris Xe G7 96 EU и лишь немного быстрее старой Vega 8 [N3].
- **Рейтинг всех ноутбуков с 780M** (NBC, 20.03.2025): самые медленные — на 40–50 % ниже среднего.
  Одна из двух причин — одна планка SO‑DIMM у тестовых EliteBook [N4].
- **Radeon 680M и 890M** отдельно в одноканале — отдельного замера **не нашёл** (не проверено).
  Механизм тот же: iGPU берёт память из общей ОЗУ.
- **DDR5 SO‑DIMM против LPDDR5X у Strix/Krackan:**
  - AMD даёт DDR5‑5600 или LPDDR5X‑8000 [A23];
  - при двух каналах (128 бит) это ≈ 89,6 против ≈ 128 ГБ/с — мой расчёт (МТ/с × 16 байт).
  - Значит, 890M/860M со слотами будет медленнее, чем в тестах с LPDDR5X. Замера «один и тот же чип, DDR5 против LPDDR5X» не нашёл — не проверено.
- **UMA / Variable Graphics Memory:**
  - «Выделенная» видеопамять iGPU — это кусок ОЗУ, отрезанный в BIOS. Для системы он пропадает [AR4].
  - AMD Variable Graphics Memory (Ryzen AI 300 и новее) задаётся в Adrenalin; нужна перезагрузка [AR4].
  - В BIOS Framework 13 (Ryzen AI 300) есть настройка «iGPU Memory Size»; в журнале BIOS упомянуто значение 1/4 ОЗУ [F3].
  - Практически: при 32 ГБ и 8 ГБ под iGPU Windows увидит ~24 ГБ — это мой вывод из [AR4], не замер. Ещё один довод за 32 ГБ.

### 2.3. Что с памятью в реальных ноутбуках (примеры)

| Ноутбук | Процессор | Память | Источник |
|---|---|---|---|
| ASUS TUF Gaming A16 FA608WV (2024) | AI 9 HX 370 | 16 ГБ LPDDR5X‑7500 распаяно | NBC, 05.03.2025 [N24] |
| ASUS TUF Gaming A16 (2025, FA608UP и др.) | Ryzen 7 260 | **два слота SO‑DIMM** | NBC, 28.09.2025 [N25] |
| ASUS Zenbook S 16, ProArt PX13, ProArt P16 | HX 370 | LPDDR5X‑7500 | NBC, 29.07.2024 [N5] |
| Acer Swift Go 16 AI SFG16‑61‑R5Y5 | AI 7 350 | 16 ГБ LPDDR5X | NBC, 25.11.2025 [N26] |
| Framework Laptop 13 (AI 5 340 / AI 7 350 / HX 370) | Krackan/Strix | «up to 96GB DDR5‑5600 or bring your own» | frame.work [F4] |
| Framework Laptop 16 (те же CPU) | Krackan/Strix | «2x SO‑DIMM sockets», DDR5‑5600, до 96 ГБ | frame.work [F5] |
| Lenovo ThinkPad E16 Gen 3 AMD 21ST004GGE / 21ST001YGE | Ryzen 5 220 / Ryzen 7 250 | два слота, но с завода **1×32 ГБ** | PSREF [L1][L2] |
| Lenovo Legion 5 15AHP10 | Ryzen 7 260 + RTX 5050 | 24 ГБ DDR5‑5600 (слоты не проверены) | NBC, 12.10.2025 [N27] |

---

## 3. Известные проблемы

**Драйверы RDNA 1/2 в «maintenance mode» (осень 2025)**
- В примечаниях к Adrenalin 25.10.2 (на странице только «Last Updated: October 29th 2025», дата выпуска не указана [AR1]; исправлено при проверке: было «выпуск 29.10.2025») новые игровые оптимизации обещали только RX 7000/9000 [T4]. В текущей версии страницы [AR1] этой фразы уже нет.
  heise: из‑за этого формально «устарели» бы и RDNA 2 в ноутбуках и SoC [T4].
- **Уточнение AMD (03.11.2025):** RX 5000/6000 будут получать поддержку новых игр, оптимизации, исправления стабильности и безопасности.
  Код разделён на две ветки: RDNA 1/2 и RDNA 3/4 [T3].
  Новые функции (например, FSR 4) — только для RDNA 3/4 [T5].
- **Что это значит для ноутбуков:**
  - RDNA 2 стоит в 610M (Mendocino 7x20, Ryzen 10, Athlon 10; iGPU Dragon Range и Fire Range), 660M/680M (7x35, Ryzen 100 на Zen 3+) [N2][A1][A6][A20][A22][T5].
    Драйвер будет, но с меньшим приоритетом.
  - Для монтажа это минус, но не приговор: исправления ошибок AMD обещает «as required by market needs» [T3]. Будут ли так же чинить медиадвижок — моя оценка, **не проверено**.
  - RDNA 3/3.5 (740M–890M, 8040S–8060S) — в основной ветке.
- **Vega (Ryzen 7x30):**
  - с осени 2023 года Polaris и Vega получают только исправления, без новых функций; по Tom’s Hardware, Vega стоит в Ryzen 7030 [T6];
  - отдельный пакет «Adrenalin 26.5.2 for Polaris & Vega» (21.05.2026): одно исправление, версия драйвера 23.19 — ветка 2023 года [AR3][T7];
  - в списке совместимости есть «AMD Ryzen Processors with Radeon Graphics» (Mobile), но какие именно модели — на странице не видно (**не проверено**) [AR3].
  - Tom’s Hardware пишет, что Vega стоит и в 7020 [T6]. Это ошибка: у 7x20 iGPU 610M на RDNA 2 [A1][N2].

**Драйверы производителя против Adrenalin**
- Для ноутбуков AMD прямо рекомендует драйверы производителя: «customized and validated for their system‑specific features».
  Adrenalin для мобильных Radeon — «reference graphics driver with limited support for system vendor specific features» [AR1][AR2].
- В Adrenalin 25.10.2 появилась «magic string» в SBIOS: по ней драйвер отключает HEVC, H.264, VP9 или AV1.
  Написано про «Radeon RX 7000 and 9000 series graphics products» [AR1].
  Это механизм для производителя ноутбука. Подробно — в `hevc-amd.md`; касается ли он iGPU — **не проверено**.

**Strix Point / Krackan Point (Ryzen AI 300) и Gorgon Point**
- **Распаянная память** в большинстве популярных моделей (раздел 2.3). Слоты есть у Framework и части игровых/бизнес‑моделей — проверять даташит.
- **Прошивка:**
  - Framework Laptop 16 (AI 300), BIOS 4.01, известная проблема: «Intermittent CPU frequency lock at 600MHz following S3/Modern Standby resume» [F1];
  - там же исправлен внезапный лимит CPU 35 Вт [F1];
  - у Framework 13 (AI 300) в журнале BIOS — исправления безопасности, в том числе CVE‑2024‑36347 (проверка подписи микрокода AMD) [F3].
  - Вывод: у AMD многое решает BIOS конкретного производителя. Смотрите, как часто бренд его обновляет.
- **USB4:** на Framework Desktop (Ryzen AI Max 300, Strix Halo) SSD‑боксы USB4 определялись как USB 3.2 и работали на 800–1000 МБ/с вместо 3,2–3,5 ГБ/с (issue #260) [F2].
  Для ноутбуков на Strix/Krackan массовых сообщений не нашёл — **не проверено**.
- **Потребление в простое и Modern Standby:** систематических данных по семейству не нашёл — **не проверено**. Смотрите обзор конкретного SKU (NBC меряет простой).
- **Урезанные модели:** AI 5 330 — 4 ядра и 820M с 2 CU [A26][N13]; AI 7 345 и AI 7 445 — 6 ядер и 840M [A27][A32]. Название «AI 7» не гарантирует 8 ядер.

**Phoenix / Hawk Point (7x40, 8x40, Ryzen 200, Ryzen 100 на Zen 4)**
- Кристалл 2023 года; под номерами 2025–2026 годов — ребрендинг (раздел 1.4).
- Малый вариант (Phoenix 2: 7545U, 8540U, Ryzen 5 220, Ryzen 3 210) — 2 или 1 полноценных ядра Zen 4 плюс Zen 4c, iGPU 740M с 4 CU, без NPU [A13][A16][A18][L1].
- Бизнес‑ноутбуки на них продают с одной планкой: EliteBook 845 G10 [N3], ThinkPad E16 Gen 3 AMD с 1×32 ГБ [L1][L2].
- Другие систематические проблемы (прошивка, USB4) — не нашёл, **не проверено**.

**Нагрев и лимит мощности**
- Одинаковый процессор в разных ноутбуках даёт очень разный результат (Cinebench R23 Multi, тесты NBC):

  | Процессор | Слабый ноутбук | Сильный ноутбук | Разница |
  |---|---|---|---|
  | Ryzen 7 8845HS | 14 895 — Lenovo IdeaPad 5 2‑in‑1 14AHP9 (36 Вт длительно) | 18 037 — XMG Core 15 (80 Вт) | +21 % [N7] |
  | Ryzen AI 7 350 | 12 647 — ASUS Zenbook 14 UM3406K (32 Вт) | 18 243 — Lenovo IdeaPad Pro 5 14AKP G10 (65 Вт) | +44 % [N21] |
  | Ryzen AI 9 HX 370 | 16 522 — ASUS Zenbook S 16 (28 Вт) | 23 902 — ROG Zephyrus G14 2025 (80 Вт) | +45 % [N20] |

- Тонкий корпус с «45‑ваттным» чипом часто держит 28–36 Вт. Для рендера 4K это те же −20…−45 %.
  Смотрите в обзоре SKU длительную мощность (PL1) и Cinebench в цикле.

---

## 4. Карта AMD ↔ Intel по классу

- CPU — Cinebench R23 Multi, медиана по списку NBC [N1].
- CB 2024 — Cinebench 2024 Multi: медиана тестов со страницы процессора на NBC, n — число тестов (считал сам) [N6][N7][N20][N21][NI].
- iGPU — 3DMark Time Spy Graphics, среднее NBC [N2].

| Класс | AMD | R23 | CB 2024 | iGPU TS | Intel | R23 | CB 2024 | iGPU TS |
|---|---|---|---|---|---|---|---|---|
| Дешёвый 4‑ядерный | Ryzen 5 7520U / Ryzen 5 40 (610M) | 5149 / 4841 | 281 (n1, у 40) | 515 | Core i3‑N305 (на странице 7520U у NBC) | 5049 | — | — [N18] |
| Zen 3+ 45 Вт | Ryzen 7 7735HS = Ryzen 7 170 (680M) | 13 106 | 620 (n5) | 2303 | i5‑13420H / Core 5 210H | 11 084 / 11 830 | 502 / 686 | UHD 48 EU — в списке NBC нет (UHD 64 EU у 13620H — 1110) |
| 6 ядер Zen 4 | Ryzen 5 240 / 8645HS / 7640HS (760M) | 13 013 / 13 220 / 12 554 | 654 / 727 (n1) | 2281 | Core Ultra 5 125H | 12 805 | 564 (n5) | 2940 (Arc 7‑core) |
| 8 ядер Zen 4, 28 Вт | Ryzen 7 250 / 8840U (780M) | 14 676 / 12 972 | 831 (n3) | 2808 | Core Ultra 5 225H | 14 630 | 720 (n2) | 2378 (Arc 130T) |
| **8 ядер Zen 4, 45 Вт** | **Ryzen 7 260 / 8845HS / 7840HS** (780M) | 17 212 / 16 192 / 16 156 | 962 (n4) / 912 (n9) / 913 (n5) | 2808 | **Core Ultra 7 155H**; i7‑13620H; Core 7 240H | 15 028; 15 953; 15 225 | 848 (n27); 696 (n3); 832 (n4) | 3270 (Arc 8‑core); 1110; — |
| 6 ядер Zen 5 | Ryzen AI 5 340 (840M) | 12 532 | 668 (n2) | 1415 | Core Ultra 5 125H; Core Ultra 5 226V | 12 805; 9850 | 564; — | 2940; 3401 (Arc 130V) |
| **8 ядер Zen 5** | **Ryzen AI 7 350** / AI 7 450 (860M) | 16 015 / 17 302 | 903 (n14) / 921 (n2) | 2565 | **Core Ultra 7 255H**; Core Ultra 7 258V; Core Ultra 7 356H | 17 845; 10 301; 18 395 | 1053 (n13); 574 (n18); 1044 (n5) | 3843 (Arc 140T); 4044 (Arc 140V); 2903 (4 Xe3) |
| 10–12 ядер Zen 5 | AI 9 365 (880M); HX 370 / HX 470 (890M) | 18 698; 21 761 / 23 208 | 1029 (n5); 1193 (n22) / 1131 (n7) | 3335; 3331 | Core Ultra 9 285H | 20 782 | — | 3843 (Arc 140T) |
| HX + дискретка | Ryzen 9 7845HX; 9955HX | 26 876; 37 159 | —; 2025 (n7) | 610M | i7‑14650HX; Core Ultra 9 285HX | 20 454; 36 430 | 1035 (n2); — | — |
| Большая iGPU | Ryzen AI Max+ 395 (8060S) | 35 314 | — | 11 018 | аналога нет; по iGPU ≈ RTX 5060 Laptop | — | — | 11 937 (RTX 5060) |

Вывод для отчёта:
- **По процессору — паритет.** Ryzen 7 260/8845HS ≈ Core Ultra 7 155H / i7‑13620H. Ryzen AI 7 350 ≈ Core Ultra 5 225H … Ultra 7 255H. HX 370 ≈ Core Ultra 9 285H [N1].
- **По iGPU Intel сейчас впереди:** Arc 140T (255H) быстрее 890M, Arc 8‑core (155H) быстрее 780M [N2].
  AMD выигрывает только у старых Intel с UHD (13‑е поколение и Core 2xxH), и выигрывает сильно.
- Числа — медианы по разным ноутбукам с разными лимитами. Разброс внутри одной модели процессора ±20–45 % (раздел 3).

---

## 5. Рекомендация на ~1100 € (2×16 ГБ SO‑DIMM, монтаж 4K)

**Брать — по убыванию:**
1. **Ryzen AI 9 365 / HX 370, AI 9 465 / HX 470** (Strix Point, Gorgon Point) [A23][A24][A31]:
   - 10–12 ядер Zen 5, 880M/890M;
   - VCN 4.0.5 [K1];
   - DDR5‑5600 SO‑DIMM по спецификации.
   Со слотами и в бюджете такие ноутбуки редки — искать в `market-amd.md`.
2. **Ryzen AI 7 350 / AI 7 450 / Ryzen 7 449** (Krackan Point, Gorgon Point) [A25][A30][A33]:
   - 8 ядер Zen 5, 860M;
   - по CPU на уровне 8845HS (раздел 4).
   Большинство моделей с распайкой — проверять даташит.
3. **Ryzen 7 260 / 250, Ryzen 9 270, 8845HS / 8840HS, 7840HS** (Hawk Point, Phoenix) [A17][A39][A15][A12]:
   - самый дешёвый путь к 8 ядрам, 780M и двум слотам;
   - по CPU почти как AI 7 350;
   - в игровых ноутбуках идёт в паре с RTX 5050/5060. Это ещё и путь к декоду 4:2:2 — см. `amd-codecs.md`.
4. **6 ядер:** Ryzen 5 240/230, 8645HS/8640HS, 7640HS, AI 5 340, Ryzen 5 439 — если заметно дешевле. 760M/840M слабее 780M [N2].
5. **HX (Dragon Range, Fire Range) — только с RTX 50.** CPU сильный, iGPU 610M слабая, DDR5 SO‑DIMM всегда [A20][A22].

**Не брать:**
- **Mendocino** (7x20U, Ryzen 3 30 / 5 40, Athlon 7x20U / Silver 10 / Gold 20) — максимум 16 ГБ LPDDR5 [A1][A2][A3].
- **Barcelo‑R** (7x30U) — Zen 3 2021 года, DDR4, Vega в ветке «только критичные исправления» [A4][T6].
- **Picasso** (Ryzen 3 3100U, 5 3501U) — Zen+ 2019 года, хоть и «Q2 2026» на amd.com [A35].
- **Rembrandt / Rembrandt‑R** (7x35, Ryzen 3 110 / 5 130 / 5 150 / 7 160 / 7 170):
  - Zen 3+, DDR5‑4800;
  - RDNA 2 в maintenance mode [T3];
  - VCN 3.1.1 — старый медиаблок [K1].
  Только если цена как у старого железа.
- **Урезанные:** Ryzen 5 220 / 3 210 / 3 205 / 5 216, 8540U, 7545U, 7 7445HS, Ryzen 7 217 (740M 4 CU); Ryzen 5 125; AI 5 330 / 430 (4 ядра); AI 7 345 / 445 (6 ядер под именем «7»).
- **7435HS / 7235HS** — без iGPU [A8].
- **Strix Halo (AI Max)** и Gorgon Halo — только распаянная LPDDR5X [A28][A34]. Годятся лишь для списка «распайка 32 ГБ», если будет цена.

### Проверка имени Ryzen за 30 секунд

1. **Есть «AI»?**
   - `AI 5/7/9 3xx` → Strix или Krackan Point (2024–2025). Исключения: `AI 5 330` — 4 ядра и 820M, `AI 7 345` — 6 ядер.
   - `AI 5/7/9 4xx` → Gorgon Point, тот же кремний, что 3xx. `AI 7 445` — 6 ядер, `AI 5 430` — 4 ядра.
   - `AI Max` / `Max+` → Strix Halo: только LPDDR5X, 2×16 невозможно.
2. **Нет «AI», три цифры?**
   - `4xx` (439, 449) → Gorgon Point без NPU — нормальный Zen 5.
   - `2xx` → Hawk Point, Zen 4 2023 года:
     - 205 / 210 / 216 / 217 / 220 — 740M и Zen 4c;
     - 224 / 225 / 230 / 240 — 6 ядер, 760M;
     - 249 / 250 / 253 / 260 / 270 — 8 ядер, 780M.
   - `1xx` → ловушка:
     - 110 / 130 / 150 / 160 / 170 — Zen 3+ 2022 года;
     - 125 / 155 / 165 / 180 — Zen 4.
3. **Две цифры** (Ryzen 3 30, Ryzen 5 40, Athlon Silver 10, Athlon Gold 20) → Mendocino, максимум 16 ГБ.
4. **Четыре цифры** → третья цифра — архитектура, четвёртая — младшая (0) или старшая (5) версия:
   - `7x20` Mendocino, `7x30` Barcelo‑R (Vega), `7x35` Rembrandt‑R, `7x40` Phoenix;
   - `8x40` Hawk Point, `7x45HX` и `8x45HX` Dragon Range, `9x5xHX` Fire Range;
   - `3xxxU` Picasso.
5. **Страница модели на amd.com**, поля:
   - «Former Codename»;
   - «System Memory Type» — нужна **DDR5**, без неё SO‑DIMM не бывает;
   - «Memory Channels» — 2;
   - «Max. Memory» — у Mendocino 16 GB;
   - «Graphics Model» — у 7435HS там «Discrete Graphics Card Required».
6. **Даташит ноутбука:** два слота SO‑DIMM и установлены 2×16, а не 1×32 (ThinkPad E16 Gen 3 AMD [L1]).
7. **Свои файлы — в MediaInfo.** Что AMD декодирует аппаратно — `amd-codecs.md`.

---

## 6. Кандидаты‑зацепки (для `candidates-*.md`)

| Модель / P/N | CPU | Память | Цена | Замечание |
|---|---|---|---|---|
| Lenovo ThinkPad E16 Gen 3 AMD **21ST004GGE** | Ryzen 5 220 | 1×32 ГБ DDR5‑5600, два слота; 1 ТБ [L1] | idealo 1149,00 € — notebooksbilliger.de (1157,99 € с доставкой, возврат 30 дней), 30.09.2026 [ID1] (перепроверено при проверке) | ловушка 1×32, выше бюджета, CPU урезанный |
| Lenovo ThinkPad E16 Gen 3 AMD **21ST001YGE** | Ryzen 7 250 | 1×32 ГБ, два слота; 1 ТБ [L2] | idealo 30.09.2026 [ID2]: «ab 1194,65 €» — цена «inkl. Gutschein» (technikdeals24.de); 1194,84 € — тоже с купоном (heinzsoft-shop.de). Без условий — **1199,64 €** (klarsicht-it.de) (исправлено при проверке: было «ab 1194,84 €» без магазина) | нужна перестановка на 2×16; выше бюджета |
| ASUS TUF Gaming A16 (2025) FA608UP / FA608UM / FA608UH | Ryzen 7 260 + RTX 5070/5060/5050 | два слота SO‑DIMM [N25] — у NBC проверен только FA608UP (Ryzen 7 260 + RTX 5070) [N25][N29]; FA608UM/FA608UH и их GPU — **не проверено** | FA608UP (RTX 5070) в тесте NBC ~2200 € (не idealo) [N25]; остальные — не проверено | искать SKU с RTX 5050/5060 |
| Lenovo Legion 5 15AHP10 | Ryzen 7 260 + RTX 5050 | 24 ГБ DDR5‑5600 в тесте NBC [N27] | не проверено | слоты и SKU для DE не проверены |
| HP HyperX Omen 15 **15-gb0057ng** | Ryzen 5 240 + RTX 5060 | 16 ГБ, 512 ГБ | 999 € — Alternate, «Wochendeal», по PCGH 12.09.2026 [P1]; не idealo, на 30.09.2026 — **не проверено** | память и слоты не проверены; SSD 512 |
| Framework Laptop 16 (AI 5 340 / AI 7 350 / HX 370) | Krackan/Strix | «2x SO‑DIMM sockets», DDR5‑5600, до 96 ГБ [F5] | DIY от 1409 €, готовый от 2069 € (frame.work, 30.09.2026; не idealo) [F5] — при проверке цены на странице не видны (curl — 403, в Chrome без конфигуратора цен нет): **не проверено**; «dual DDR5 SO‑DIMM, up to 96GB» подтверждено | выше бюджета; известная проблема BIOS 4.01 [F1] |
| Asus Vivobook 16 M1606K | AI 7 350 | не проверено | не проверено | есть тест NBC (R23 14 383) [N21] |

---

## Источники

**AMD — страницы моделей** (база `https://www.amd.com/en/products/processors/laptop/`; поля Former Codename, System Memory Type, Memory Channels, Max. Memory, Graphics Model, NPU TOPS, Launch Date; скачано 30.09.2026)
- [AS] Карта сайта AMD, раздел мобильных процессоров (143 страницы): <https://www.amd.com/en.sitemap.xml>.
  Модели, у которых ниже нет своего номера, взяты со страниц по тому же шаблону: `…/laptop/ryzen/<серия>/amd-ryzen-<n>-<модель>.html`.
  Например, Ryzen 5 230 — `…/ryzen/200-series/amd-ryzen-5-230.html`, Ryzen 3 110 — `…/ryzen/100-series/amd-ryzen-3-110.html`.
- [A1] Ryzen 5 7520U: <https://www.amd.com/en/products/processors/laptop/ryzen/7000-series/amd-ryzen-5-7520u.html>
- [A2] Ryzen 5 40: <https://www.amd.com/en/products/processors/laptop/ryzen/10-series/amd-ryzen-5-40.html>
- [A3] Athlon Gold 20: <https://www.amd.com/en/products/processors/laptop/athlon/10-series/amd-athlon-gold-20.html>
- [A4] Ryzen 7 7730U: <https://www.amd.com/en/products/processors/laptop/ryzen/7000-series/amd-ryzen-7-7730u.html>
- [A5] Ryzen 5 7530U: <https://www.amd.com/en/products/processors/laptop/ryzen/7000-series/amd-ryzen-5-7530u.html>
- [A6] Ryzen 7 7735HS: <https://www.amd.com/en/products/processors/laptop/ryzen/7000-series/amd-ryzen-7-7735hs.html>
- [A7] Ryzen 5 7535HS: <https://www.amd.com/en/products/processors/laptop/ryzen/7000-series/amd-ryzen-5-7535hs.html>
- [A8] Ryzen 7 7435HS: <https://www.amd.com/en/products/processors/laptop/ryzen/7000-series/amd-ryzen-7-7435hs.html>
- [A9] Ryzen 7 170: <https://www.amd.com/en/products/processors/laptop/ryzen/100-series/amd-ryzen-7-170.html>
- [A10] Ryzen 9 180: <https://www.amd.com/en/products/processors/laptop/ryzen/100-series/amd-ryzen-9-180.html>
- [A11] Ryzen 5 125 (адрес страницы — ryzen‑7‑125, имя на странице — Ryzen 5 125): <https://www.amd.com/en/products/processors/laptop/ryzen/100-series/amd-ryzen-7-125.html>
- [A12] Ryzen 7 7840HS: <https://www.amd.com/en/products/processors/laptop/ryzen/7000-series/amd-ryzen-7-7840hs.html>
- [A13] Ryzen 5 7545U: <https://www.amd.com/en/products/processors/laptop/ryzen/7000-series/amd-ryzen-5-7545u.html>
- [A14] Ryzen 7 7445HS: <https://www.amd.com/en/products/processors/laptop/ryzen/7000-series/amd-ryzen-7-7445hs.html>
- [A15] Ryzen 7 8845HS: <https://www.amd.com/en/products/processors/laptop/ryzen/8000-series/amd-ryzen-7-8845hs.html>
- [A16] Ryzen 5 8540U: <https://www.amd.com/en/products/processors/laptop/ryzen/8000-series/amd-ryzen-5-8540u.html>
- [A17] Ryzen 7 260: <https://www.amd.com/en/products/processors/laptop/ryzen/200-series/amd-ryzen-7-260.html>
- [A18] Ryzen 5 220: <https://www.amd.com/en/products/processors/laptop/ryzen/200-series/amd-ryzen-5-220.html>
- [A19] Ryzen 7 253: <https://www.amd.com/en/products/processors/laptop/ryzen/200-series/amd-ryzen-7-253.html>
- [A20] Ryzen 9 7945HX: <https://www.amd.com/en/products/processors/laptop/ryzen/7000-series/amd-ryzen-9-7945hx.html>
- [A21] Ryzen 9 8945HX: <https://www.amd.com/en/products/processors/laptop/ryzen/8000-series/amd-ryzen-9-8945hx.html>
- [A22] Ryzen 9 9955HX: <https://www.amd.com/en/products/processors/laptop/ryzen/9000-series/amd-ryzen-9-9955hx.html>
- [A23] Ryzen AI 9 HX 370: <https://www.amd.com/en/products/processors/laptop/ryzen/ai-300-series/amd-ryzen-ai-9-hx-370.html>
- [A24] Ryzen AI 9 365: <https://www.amd.com/en/products/processors/laptop/ryzen/ai-300-series/amd-ryzen-ai-9-365.html>
- [A25] Ryzen AI 7 350: <https://www.amd.com/en/products/processors/laptop/ryzen/ai-300-series/amd-ryzen-ai-7-350.html>
- [A26] Ryzen AI 5 330: <https://www.amd.com/en/products/processors/laptop/ryzen/ai-300-series/amd-ryzen-ai-5-330.html>
- [A27] Ryzen AI 7 345: <https://www.amd.com/en/products/processors/laptop/ryzen/ai-300-series/amd-ryzen-ai-7-345.html>
- [A28] Ryzen AI Max+ 395: <https://www.amd.com/en/products/processors/laptop/ryzen/ai-300-series/amd-ryzen-ai-max-plus-395.html>
- [A29] Ryzen AI Max PRO 380: <https://www.amd.com/en/products/processors/laptop/ryzen-pro/ai-max-pro-300-series/amd-ryzen-ai-max-pro-380.html>
- [A30] Ryzen AI 7 450: <https://www.amd.com/en/products/processors/laptop/ryzen/ai-400-series/amd-ryzen-ai-7-450.html>
- [A31] Ryzen AI 9 HX 470: <https://www.amd.com/en/products/processors/laptop/ryzen/ai-400-series/amd-ryzen-ai-9-hx-470.html>
- [A32] Ryzen AI 7 445: <https://www.amd.com/en/products/processors/laptop/ryzen/ai-400-series/amd-ryzen-ai-7-445.html>
- [A33] Ryzen 7 449: <https://www.amd.com/en/products/processors/laptop/ryzen/400-series/amd-ryzen-7-449.html>
- [A34] Ryzen AI Max+ PRO 495: <https://www.amd.com/en/products/processors/laptop/ryzen-pro/ai-max-pro-400-series/amd-ryzen-ai-max-plus-pro-495.html>
- [A35] Ryzen 5 3501U: <https://www.amd.com/en/products/processors/laptop/ryzen/3000-series/amd-ryzen-5-3501u.html>
- [A36] Ryzen 5 7525U: <https://www.amd.com/en/products/processors/laptop/ryzen/7000-series/amd-ryzen-5-7525u.html>
- [A37] Ryzen 7 7736U: <https://www.amd.com/en/products/processors/laptop/ryzen/7000-series/amd-ryzen-7-7736u.html>
- [A38] Ryzen 5 240: <https://www.amd.com/en/products/processors/laptop/ryzen/200-series/amd-ryzen-5-240.html>
- [A39] Ryzen 7 250: <https://www.amd.com/en/products/processors/laptop/ryzen/200-series/amd-ryzen-7-250.html>
- [A40] Ryzen 9 270: <https://www.amd.com/en/products/processors/laptop/ryzen/200-series/amd-ryzen-9-270.html>
- [A41] Ryzen 9 8945HS: <https://www.amd.com/en/products/processors/laptop/ryzen/8000-series/amd-ryzen-9-8945hs.html>
- [A42] Ryzen AI 5 435 (добавлено при проверке): <https://www.amd.com/en/products/processors/laptop/ryzen/ai-400-series/amd-ryzen-ai-5-435.html>
- [A43] Ryzen AI 5 PRO 440 (добавлено при проверке): <https://www.amd.com/en/products/processors/laptop/ryzen-pro/ai-400-series/amd-ryzen-ai-5-pro-440.html>

**AMD — драйверы и статьи**
- [AR1] Adrenalin 25.10.2, Release Notes (обн. 29.10.2025): <https://www.amd.com/en/resources/support-articles/release-notes/RN-RAD-WIN-25-10-2.html>
- [AR2] Adrenalin 26.9.1, Release Notes (03.09.2026): <https://www.amd.com/en/resources/support-articles/release-notes/RN-RAD-WIN-26-9-1.html>
- [AR3] Adrenalin 26.5.2 for Polaris & Vega, Release Notes: <https://www.amd.com/en/resources/support-articles/release-notes/RN-RAD-WIN-26-5-2-POLARIS-VEGA.html>
- [AR4] AMD Blog, FAQs: AMD Variable Graphics Memory (29.07.2025): <https://www.amd.com/en/blogs/2025/faqs-amd-variable-graphics-memory-vram-ai-model-sizes-quantization-mcp-more.html>
- [AR5] AMD Blog 2026, Ryzen AI Max PRO 400 Series: <https://www.amd.com/en/blogs/2026/how-amd-ryzen-ai-max-pro-400-series-processors-bring-local-agentic-ai-to-business-customers.html>

**Linux**
- [K1] Linux kernel, amdgpu APU ASIC info table (версии DCN/GC/VCN по кодовым именам): <https://github.com/torvalds/linux/blob/master/Documentation/gpu/amdgpu/apu-asic-info-table.csv>

**Notebookcheck**
- [N1] Mobile Processors — Benchmark List (Cinebench R23 Multi, медианы): <https://www.notebookcheck.net/Mobile-Processors-Benchmark-List.2436.0.html>
- [N2] Mobile Graphics Cards — Benchmark List (Time Spy Graphics, средние): <https://www.notebookcheck.net/Mobile-Graphics-Cards-Benchmark-List.844.0.html>
- [N3] Testing the performance of Radeon 780M & 760M with new drivers — раздел «Single‑channel vs. dual‑channel» (11.08.2023): <https://www.notebookcheck.net/Testing-the-performance-of-AMD-Radeon-780M-760M-iGPUs-with-new-drivers.740311.0.html>
- [N4] We rank every Radeon 780M laptop… (20.03.2025): <https://www.notebookcheck.net/We-rank-every-Radeon-780M-laptop-reviewed-from-slowest-to-fastest-according-to-3DMark.982638.0.html>
- [N5] Zen 5 Strix Point iGPU analysis (29.07.2024): <https://www.notebookcheck.net/AMD-Zen-5-Strix-Point-iGPU-analysis-Radeon-890M-versus-Intel-Arc-Graphics-Apple-M3-and-Qualcomm-Adreno-X1-85.868475.0.html>
- [N6] Ryzen 7 260: <https://www.notebookcheck.net/AMD-Ryzen-7-260-Processor-Benchmarks-and-Specs.945912.0.html>
- [N7] Ryzen 7 8845HS: <https://www.notebookcheck.net/AMD-Ryzen-7-8845HS-Processor-Benchmarks-and-Specs.780991.0.html>
- [N8] Ryzen 7 250: <https://www.notebookcheck.net/AMD-Ryzen-7-250-Processor-Benchmarks-and-Specs.945901.0.html>
- [N9] Ryzen 5 220: <https://www.notebookcheck.net/AMD-Ryzen-5-220-Processor-Benchmarks-and-Specs.946309.0.html>
- [N10] Ryzen 7 449: <https://www.notebookcheck.net/AMD-Ryzen-7-449-Processor-Benchmarks-and-Specs.1364527.0.html>
- [N11] Ryzen AI 7 450: <https://www.notebookcheck.net/AMD-Ryzen-AI-7-450-Processor-Benchmarks-and-Specs.1197762.0.html>
- [N12] Ryzen AI 7 445: <https://www.notebookcheck.net/AMD-Ryzen-AI-7-445-Processor-Benchmarks-and-Specs.1197764.0.html>
- [N13] Ryzen AI 5 330: <https://www.notebookcheck.net/AMD-Ryzen-AI-5-330-Processor-Benchmarks-and-Specs.1049553.0.html>
- [N14] Ryzen 7 165: <https://www.notebookcheck.net/AMD-Ryzen-7-165-Processor-Benchmarks-and-Specs.1354528.0.html>
- [N15] Ryzen 9 180: <https://www.notebookcheck.net/AMD-Ryzen-9-180-Processor-Benchmarks-and-Specs.1354506.0.html>
- [N16] Ryzen 7 170: <https://www.notebookcheck.net/AMD-Ryzen-7-170-Processor-Benchmarks-and-Specs.1148247.0.html>
- [N17] Ryzen 5 7530U: <https://www.notebookcheck.net/AMD-Ryzen-5-7530U-Processor-Benchmarks-and-Specs.681702.0.html>
- [N18] Ryzen 5 7520U: <https://www.notebookcheck.net/AMD-Ryzen-5-7520U-Processor-Benchmarks-and-Specs.654934.0.html>
- [N19] Ryzen 5 40: <https://www.notebookcheck.net/AMD-Ryzen-5-40-Processor-Benchmarks-and-Specs.1149121.0.html>
- [N20] Ryzen AI 9 HX 370: <https://www.notebookcheck.net/AMD-Ryzen-AI-9-HX-370-Processor-Benchmarks-and-Specs.836729.0.html>
- [N21] Ryzen AI 7 350: <https://www.notebookcheck.net/AMD-Ryzen-AI-7-350-Processor-Benchmarks-and-Specs.949825.0.html>
- [N22] Ryzen AI Max+ 392: <https://www.notebookcheck.net/AMD-Ryzen-AI-Max-392-Processor-Benchmarks-and-Specs.1197727.0.html>
- [N23] Ryzen 9 9850HX: <https://www.notebookcheck.net/AMD-Ryzen-9-9850HX-Processor-Benchmarks-and-Specs.941946.0.html>
- [N24] ASUS TUF Gaming A16 FA608WV, обзор (05.03.2025): <https://www.notebookcheck.net/Asus-TUF-Gaming-A16-Review-Cool-quiet-and-affordable-gaming-laptop-with-a-prominent-but-workable-weakness.970334.0.html>
- [N25] ASUS TUF Gaming A16 2025 — «replaceable RAM», два слота SO‑DIMM (28.09.2025): <https://www.notebookcheck.net/Asus-equips-the-new-TUF-Gaming-A16-with-an-improved-165-Hz-display-and-replaceable-RAM.1123936.0.html>
- [N26] Acer Swift Go 16 AI, обзор (25.11.2025): <https://www.notebookcheck.net/Solid-performance-and-colorful-OLED-Acer-Swift-Go-16-AI-review.1168834.0.html>
- [N27] Lenovo Legion 5 15AHP10, Ryzen 7 260 + RTX 5050 (12.10.2025): <https://www.notebookcheck.net/Lenovo-Legion-5-15AHP10-Ryzen-7-260-RTX-5050.1136819.0.html>
- [N28] Athlon Silver 7120U: <https://www.notebookcheck.net/AMD-Athlon-Silver-7120U-Processor-Benchmarks-and-Specs.722235.0.html>; Athlon Gold 7220U: <https://www.notebookcheck.net/AMD-Athlon-Gold-7220U-Processor-Benchmarks-and-Specs.655023.0.html>
- [N29] ASUS TUF Gaming A16 FA608UP (Ryzen 7 260 + RTX 5070), обзор (добавлено при проверке): <https://www.notebookcheck.net/Asus-TUF-Gaming-A16-Laptop-Review-A-EUR2-200-gamble-for-Zen-4-Hawk-Point-RTX-5070.1122766.0.html>
- [NI] Страницы Intel у NBC (Cinebench 2024): Core Ultra 7 155H <https://www.notebookcheck.net/Intel-Core-Ultra-7-155H-Processor-Benchmarks-and-Specs.783323.0.html>; Core Ultra 7 255H <https://www.notebookcheck.net/Intel-Core-Ultra-7-255H-Processor-Benchmarks-and-Specs.944139.0.html>; Core Ultra 5 225H <https://www.notebookcheck.net/Intel-Core-Ultra-5-225H-Processor-Benchmarks-and-Specs.944682.0.html>; Core Ultra 7 258V <https://www.notebookcheck.net/Intel-Core-Ultra-7-258V-Processor-Benchmarks-and-Specs.892883.0.html>; Core Ultra 7 356H <https://www.notebookcheck.net/Intel-Core-Ultra-7-356H-Processor-Benchmarks-and-Specs.1196617.0.html>; i7‑13620H <https://www.notebookcheck.net/Intel-Core-i7-13620H-Processor-Benchmarks-and-Specs.677505.0.html>; Core 7 240H <https://www.notebookcheck.net/Intel-Core-7-240H-Processor-Benchmarks-and-Specs.936272.0.html>; Core 5 210H <https://www.notebookcheck.net/Intel-Core-5-210H-Processor-Benchmarks-and-Specs.936302.0.html>; i5‑13420H <https://www.notebookcheck.net/Intel-Core-i5-13420H-Processor-Benchmarks-and-Specs.677510.0.html>; Core Ultra 5 125H <https://www.notebookcheck.net/Intel-Core-Ultra-5-125H-Processor-Benchmarks-and-Specs.783325.0.html>; i7‑14650HX <https://www.notebookcheck.net/Intel-Core-i7-14650HX-Processor-Benchmarks-and-Specs.790780.0.html>

**Даташиты**
- [L1] Lenovo PSREF, ThinkPad E16 Gen 3 AMD 21ST004GGE: <https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=21ST004GGE&country_code=DE>
- [L2] Lenovo PSREF, 21ST001YGE: <https://psref.lenovo.com/api/model/pdfexport/singleModel?model_code=21ST001YGE&country_code=DE>
- [F1] Framework Laptop 16 AMD Ryzen AI 300, BIOS 4.01 (Known Issues): <https://resources.frame.work/downloads/laptop-16/amd-ryzen-ai-300-series/4.01/>
- [F2] Framework, issue #260 «[Desktop — AMD Ryzen AI 300] USB4 ports wrong behavior»: <https://github.com/FrameworkComputer/SoftwareFirmwareIssueTracker/issues/260>
- [F3] Framework Laptop 13 AMD Ryzen AI 300, BIOS и драйверы: <https://resources.frame.work/downloads/laptop-13/amd-ryzen-ai-300-series/>
- [F4] Framework Laptop 13 (DE), варианты CPU и память: <https://frame.work/de/en/laptop13>
- [F5] Framework Laptop 16 (DE), память, CPU и цены (30.09.2026): <https://frame.work/de/en/laptop16>

**Пресса**
- [T1] Tom’s Hardware, новая схема номеров мобильных Ryzen (07.09.2022): <https://www.tomshardware.com/news/amd-updates-mobile-cpu-numbers>
- [T2] PC Perspective, AMD’s New Model Numbers for 2023 and Later Mobile Processors (09.2022): <https://pcper.com/2022/09/amds-new-model-numbers-for-2023-and-later-mobile-processors/>
- [T3] Tom’s Hardware, AMD clarifies its clarifications on RDNA 1 and 2 (03.11.2025): <https://www.tomshardware.com/pc-components/gpu-drivers/amd-clarifies-its-clarifications-on-controversial-rdna-1-and-2-driver-note-company-will-continue-game-optimization-support-after-all>
- [T4] heise, Confusion over AMD’s graphics drivers for RDNA 1 and 2 in maintenance mode (01.11.2025): <https://www.heise.de/en/news/Confusion-over-AMD-s-graphics-drivers-for-RDNA-1-and-2-in-maintenance-mode-10966044.html>
- [T5] PC Guide, All the relevant RDNA 2 hardware going into «maintenance mode» (04.11.2025): <https://www.pcguide.com/news/all-the-relevant-rdna-2-hardware-going-into-maintenance-mode-following-driver-changes/>
- [T6] Tom’s Hardware, It’s Curtains for Polaris and Vega (08.11.2023): <https://www.tomshardware.com/pc-components/gpus/its-curtains-for-polaris-and-vega-as-amd-reduces-driver-support>
- [T7] VideoCardz, AMD updates Polaris and Vega GPUs driver (21.05.2026): <https://videocardz.com/newz/amd-updates-polaris-and-vega-gpus-driver-after-long-pause>
- [W1] Wikipedia, List of AMD Ryzen processors (навигация): <https://en.wikipedia.org/wiki/List_of_AMD_Ryzen_processors>
- [P1] PCGH, RTX‑5060‑ноутбуки за 999 € у Alternate/Amazon (12.09.2026): <https://www.pcgameshardware.de/Notebook_Laptop-Hardware-201330/News/Gaming-Laptop-Geforce-RTX-5060-HP-Ryzen-5-240-MSI-Core-i5-13420H-Tulpar-Core-i7-14700HX-guenstig-kaufen-Amazon-Alternate-Angebot-Deal-Check-1553573/>

**idealo (Chrome пользователя, 30.09.2026, добавлено при проверке)**
- [ID1] ThinkPad E16 G3 21ST004GGE: <https://www.idealo.de/preisvergleich/OffersOfProduct/207096771_-thinkpad-e16-g3-21st004gge-lenovo.html>
- [ID2] ThinkPad E16 G3 21ST001YGE: <https://www.idealo.de/preisvergleich/OffersOfProduct/206556600_-thinkpad-e16-g3-21st001yge-lenovo.html>

---

## Проверка (скептик, 30.09.2026)

Метод: заново скачал первоисточники (amd.com через curl, таблицу ядра Linux, страницы NBC, PSREF PDF), idealo — в своей вкладке Chrome пользователя.
Страницы AMD — поля Former Codename, Processor Architecture, System Memory Type, Max. Memory, Max Memory Speed, Graphics Model, NPU TOPS.

| # | Утверждение | Вердикт | Чем проверено |
|---|---|---|---|
| 1 | Ryzen 7 260 / 5 220 / 7 250 — Hawk Point, выход 18.02.2025; 260 — 8 Zen 4, 45 Вт, 5,1 ГГц, 780M, 16 TOPS; 220 — 2 Zen 4 + 4 Zen 4c, 740M, без NPU | подтверждено | [A17][A18][A39]; NBC: 260 «identical to the old Ryzen 7 8845HS and therefore also the 7840HS» [N6] |
| 2 | Ryzen 5 220 = 8540U = 7545U | подтверждено | у всех трёх 2 Zen 4 + 4 Zen 4c, 740M 4 CU, 28 Вт [A18][A16][A13] |
| 3 | Добавленные 02.06.2026 Ryzen 200 (205/216/217/224/225/249/253) — Hawk Point, частоты ниже; 217 — «Ryzen 7» с 6 ядрами и 740M | подтверждено | на amd.com: 205 — 1+3 ядра; 216 и 217 — 2+4, 740M; 224/225 — 6 Zen 4, 760M; 249/253 — 8 ядер, 780M, 4,9 ГГц против 5,1 у 250/260 |
| 4 | Ryzen 100: 170 — Rembrandt, Zen 3+ (01.10.2025); 125 и 180 — Hawk Point, Zen 4 (02.06.2026); 125 — 4 ядра | подтверждено | [A9][A10][A11]; 165 — «Hawk Point Refresh» у NBC [N14]. Уточнение про память — в таблице 1.3 |
| 5 | Mendocino (7520U, Ryzen 5 40, Athlon Gold 20): только LPDDR5, максимум 16 ГБ | подтверждено | [A1][A2][A3]: LPDDR5, Max. Memory 16 GB, у 7520U LPDDR5‑5500 |
| 6 | Strix Halo и Gorgon Halo — только LPDDR5X; у Max PRO 380 — 128 бит | подтверждено | Max+ 395: «256‑bit LPDDR5x», 128 ГБ; PRO 380: «128‑bit LPDDR5x», 64 ГБ; Max+ PRO 495: 256 бит, LPDDR5x‑8533, 192 ГБ [A28][A29][A34] |
| 7 | Dragon Range и Fire Range — только DDR5 SO‑DIMM | подтверждено | 7945HX: DDR5, SO‑DIMM, DDR5‑5200, 64 ГБ; 9955HX: DDR5, SO‑DIMM, 96 ГБ [A20][A22] |
| 8 | Ryzen AI 400 — кристаллы Strix/Krackan | подтверждено частично | [K1]: у 475/470/465 блоки как у Strix Point, у 450 — как у Krackan 350, у 440/435 — как у Krackan 330. Для AI 5 430 и AI 7 445 строк нет — не проверено |
| 9 | «AI 5 435/440 = AI 5 330» | **исправлено** | кристалл тот же [K1], конфигурация другая: 435 — 2+4 ядра, PRO 440 — 3+3, обе 840M 4 CU; у 330 — 1+3 и 820M 2 CU [A42][A43][A26] |
| 10 | Ryzen 5 439 / 7 449 — Gorgon Point без NPU; 449 ≈ AI 7 450 с частотами ниже; анонс 07.08.2026 | подтверждено | на amd.com поля NPU нет, 449 — 4+4 ядра, 5,0 ГГц (у 450 — 5,1), 860M; 439 — 3+3, 840M [A33]. У NBC «Announcement Date 08/07/2026» [N10]; при этом NBC пишет у 449 5,1 ГГц — расходится с amd.com |
| 11 | Picasso 3100U / 3501U: на amd.com дата выхода «Q2 2026» | подтверждено | обе страницы — «Launch Date: Q2 2026» [A35]; вероятно, ошибка или перевыпуск в каталоге AMD |
| 12 | 7435HS без iGPU | подтверждено | «Discrete Graphics Card Required» [A8] |
| 13 | VCN: 7x30 — 2.2; 7x20 и 7x35 — 3.1.1; Dragon Range — 3.1.2; Phoenix/Hawk Point — 4.0.2; Strix/Krackan/Gorgon — 4.0.5; Strix Halo — 4.0.6; Fire Range в таблице нет | подтверждено | [K1], текущая master‑ветка |
| 14 | Одна планка: 780M в EliteBook 845 G10 — 2659 → 1496 в Time Spy Graphics (−44 %), Fire Strike 7800 → 4550, 3DMark 11 11 811 → 7868 | подтверждено | [N3], 11.08.2023; NBC: с одной планкой 780M «only runs slightly faster than the old RX Vega 8» |
| 15 | Time Spy Graphics (NBC): 140T 3843, 890M 3331, 860M 2565, Arc 8‑core 3270, 780M 2808, 140V 4044 | подтверждено | [N2]: 3843n20, 3331n33, 2565n23, 3270n48, 2808n81, 4044n42. Вывод «Intel впереди» верен для 3D; для монтажа — не про это (добавил оговорку) |
| 16 | R23 Multi (медиана NBC): Ryzen 7 260 — 17 212, 255H — 17 845, 155H — 15 028, HX 370 — 21 761, 285H — 20 782 | подтверждено | [N1]: 17211.5 (n6), 17845 (n20), 15028 (n52), 21761 (n32), 20781.5 (n12). У Ryzen 7 260 всего 6 тестов |
| 17 | HX 370: 16 522 в Zenbook S 16 (28 Вт) и 23 902 в Zephyrus G14 2025 (80 Вт), +45 % | подтверждено | [N20]: UM5606 «33 W / 28 W» — 16 522; GA403WW «80 W / 80 W» — 23 902 |
| 18 | TUF A16 FA608WV (2024) — 16 ГБ распаяно; TUF A16 2025 — два SO‑DIMM | подтверждено | [N24] «the 16 GB RAM is soldered in»; [N25] «two SO‑DIMM slots»; FA608UP — Ryzen 7 260 [N29]. FA608UM/UH — не проверено |
| 19 | Adrenalin 25.10.2: RDNA 1/2 — maintenance mode; «magic string» в SBIOS отключает HEVC/H.264/VP9/AV1 на RX 7000/9000; AMD советует драйверы OEM | подтверждено, дата **уточнена** | [AR1]: «Last Updated: October 29th 2025» — это дата обновления, не выпуска; [T3] 03.11.2025 — «as required by market needs»; [T4] heise — 01.11.2025 |
| 20 | Vega: пакет «26.5.2 for Polaris & Vega», 21.05.2026, одно исправление, ветка 23.19 | подтверждено | [AR3]: «Date: May 21st, 2026», Driver Version 23.19.25.01, одно исправление (Apex Legends на RX 400/500) |
| 21 | ThinkPad E16 Gen 3 AMD 21ST004GGE / 21ST001YGE: Ryzen 5 220 / Ryzen 7 250, 1×32 ГБ DDR5‑5600, два слота, 1 ТБ | подтверждено | PSREF DE [L1][L2]: «Two DDR5 SODIMM slots, dual‑channel capable», «1x 32GB SODIMM DDR5‑5600» |
| 22 | Цены idealo E16: «ab 1149 €» и «ab 1194,84 €» | **исправлено** | [ID1]: 1149,00 € — notebooksbilliger.de. [ID2]: минимум 1194,65 € и 1194,84 € — «inkl. Gutschein», без условий — 1199,64 € (klarsicht-it.de). В `../Intel/notes/idealo-prices.md` было 1194,83 €, в `../MEMORY.md` — 1194,84 €: цифры расходятся |
| 23 | Omen 15 за 999 € | уточнено | P/N 15-gb0057ng, Alternate, «Wochendeal» [P1] (12.09.2026); на 30.09 — не проверено |
| 24 | Framework 16: цены DIY 1409 € / готовый 2069 € | не проверено | curl — 403; в Chrome цен в тексте страницы нет. Два слота DDR5 SO‑DIMM, до 96 ГБ — подтверждено [F5] |

Что **не** опроверг: карту имён → кремний, ограничения по памяти, VCN и все проверенные бенчмарки.
Итоговая рекомендация (раздел 5) опирается на подтверждённые факты. Оговорка: пункт 1 «лучше всего — AI 9 / HX 370 со слотами» — ранжирование по CPU/iGPU.
Для монтажа 4K решают кодеки (`amd-codecs.md`), а ноутбуков со слотами в бюджете пока нет в списке — это вывод, не проверенный рынком.
