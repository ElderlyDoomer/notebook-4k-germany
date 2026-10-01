# Intel для монтажа 4K: ловушки имён и кодеки Quick Sync

_Собрано 2026-09-30 (UTC). Ссылки на источники — в квадратных скобках, список в конце (раздел 6).
«Не проверено» — не нашёл первоисточник или он недоступен из облака._
_Локальная проверка 30.09.2026: 22 ключевых утверждения перепроверены по Intel ARK (в Chrome пользователя), даташитам Intel EDC, media-driver, Puget, NVIDIA, Adobe, Blackmagic. Итог — раздел «Локальная проверка (30.09.2026)» в конце._

## 0. Коротко

1. **Старый кремний под новыми именами — главные ловушки:**
   - **Core 5/7/9 2xxH** («Series 2», 2025) — это Raptor Lake‑H 2023 года: i5‑13420H, i5‑13500H, i7‑13620H, i7‑13700H, i9‑13900H с частотой выше на 200–400 МГц.
     Intel сам пишет «Products formerly Raptor Lake», техпроцесс Intel 7 [A1–A5].
     Notebookcheck называет их «Raptor Lake‑H (Alder Lake architecture)», ядра Golden Cove [N1–N3].
   - **Core 3/5/7 1xxU** (Series 1, 2024) и **Core 5/7 2xxU** (Series 2, 2025) — это Raptor Lake‑U (i3‑1315U, i5‑1335U, i7‑1355U).
     У Core 7 250U и Core 7 150U одинаковые ядра, частоты, кеш и iGPU; разница только в поддержке LPDDR5X (6400 против 5200) [A6][A7][W1].
   - **Core Ultra 5/7 2xxU** — по сути обновлённый Meteor Lake на Intel 3 [W4][A13] (исправлено при локальной проверке 30.09.2026: официально Intel называет его **Arrow Lake** — в ARK у 255U «Products formerly Arrow Lake», у Notebookcheck «Arrow Lake‑U». Но ядра Redwood Cove / Crestmont и iGPU 4 Xe — как у Meteor Lake‑U [A13][N5]. Поэтому проверка по полю Code Name эту ловушку не ловит — смотрите букву U).
   - **14‑е поколение в ноутбуках есть только в серии HX** — это Raptor Lake‑HX Refresh 2024 года, тот же кристалл, что у 13‑х HX.
     Часть 13‑х HX сделана вообще на кристалле Alder Lake [W1].
   - **Core 3/5/7 3xx без буквы** (Core Series 3, Wildcat Lake, 2026) — кремний новый, но **один канал памяти** и 2 P‑ядра [A21]. Для монтажа это ловушка.
   - **Core 3 N355, Intel N150/N250** (Twin Lake) — только E‑ядра, 1 канал, до 16 ГБ [A22].
2. **Ноутбук не соберёшь на 2×16 ГБ SO‑DIMM**, если в нём:
   - Lunar Lake (Core Ultra 2xxV) — память на корпусе процессора, 16 или 32 ГБ [A16][W5];
   - Panther Lake **X7/X9** или **Core Ultra 5 338H** — поддерживают только LPDDR5X [A17][A19][W6];
   - Wildcat Lake — у него один канал памяти [A21].
3. **Кодеки:**
   - **HEVC 4:2:2 10 бит** аппаратно декодирует любой Intel начиная с 11‑го поколения, включая «старый» Raptor Lake. Это работает и в Resolve Studio, и в Premiere [P1][P2].
   - **H.264 10 бит, в том числе H.264 4:2:2 10 бит, не декодирует ни один Intel до Panther Lake** [D1][D2][P1].
     Из видеокарт это умеет только **NVIDIA RTX 50 (Blackwell)** [V1][V2].
   - Panther Lake и Wildcat Lake (Xe3) заявляют «AVC 10‑bit» и форматы Sony XAVC‑S/HS/H [C1][C2][C4].
     Есть ли там 4:2:2 и поддерживают ли это программы — **не проверено**. → проверено в браузере 30.09.2026: (п. 5.13) МЕНЯЕТ ВЫВОД: даташит Intel Core Ultra Series 3 (872188, табл. 77) — Panther Lake аппаратно декодирует H.264 4:2:0 8/10 бит и 4:2:2 10 бит; Resolve Studio 21 — «Intel QuickSync H.264 10-bit 4:2:0 and 4:2:2 decode support»; Premiere и бесплатный Resolve — нет; независимых тестов нет ([cdrdv2.intel.com](https://cdrdv2.intel.com/v1/dl/getContent/872188?fileName=872188-002.pdf)).
4. **Linux:**
   - Resolve открывает H.264/H.265 только в Studio, а GPU‑ускорение в документе Blackmagic для Linux указано только для NVIDIA. Intel Quick Sync там не упоминается [R1].
   - Бесплатный Resolve под Linux H.264/H.265 не открывает вообще [R1].
5. **Выбор на ~1100 €:**
   - Лучший вариант — **Core Ultra 5 225H/235H или Core Ultra 7 255H** (Arrow Lake‑H) с двумя слотами SO‑DIMM.
   - Дешевле — **Core Ultra 5 125H/135H или Core Ultra 7 155H** (Meteor Lake): у них тот же медиаблок.
   - Если берёте дискретку ≥8 ГБ — только **RTX 50**, не RTX 40: декодировать H.264 4:2:2 умеет только Blackwell.
     Процессор при такой видеокарте может быть и «старым» (i7‑14650HX, Core 7 240H), но платить за него как за новинку не нужно.

---

## 1. Имя → кремний

### 1.1. Расшифровка имени

| Имя в прайсе | Что внутри | Выход |
|---|---|---|
| i3/i5/i7/i9‑12xxxH/P/U | Alder Lake | Q1 2022 [A8][W2] |
| i5/i7/i9‑12xxxHX | Alder Lake‑HX, кристалл от десктопа | май 2022 [W2] |
| i3/i5/i7/i9‑13xxxH/P/U | Raptor Lake‑H/P/U; у Notebookcheck — «на архитектуре Alder Lake» | Q1 2023 [A9][N4] |
| i5/i7/i9‑13xxxHX | Raptor Lake‑HX; часть моделей на кристалле Alder Lake | Q1 2023 [W1][A10] |
| i5/i7/i9‑14xxxHX | Raptor Lake‑HX Refresh | янв 2024 [W1][A11] |
| Core 3/5/7 1xxU (Series 1) | Raptor Lake‑U Refresh | Q1 2024 [A6][W1] |
| Core 5/7 2xxU, Core 5/7/9 2xxH (Series 2) | Raptor Lake‑U/H «Re‑refresh» | Q4 2024 – Q1 2025 [A1–A5][A7] |
| Core Ultra 5/7/9 1xxH/U | Meteor Lake | дек 2023 [A12][W3] |
| Core Ultra 5/7 2xxU | Meteor Lake‑refresh (Arrow Lake‑U), Intel 3; в ARK — «Arrow Lake», Q1'25 | янв 2025 [A13][W4][N5] |
| Core Ultra 5/7/9 2xxH | Arrow Lake‑H | янв 2025 [A14][A15] |
| Core Ultra 5/7/9 2xxHX | Arrow Lake‑HX, кристалл от десктопа | янв 2025 [A23][W4] |
| Core Ultra 7 251HX; 270HX Plus, 290HX Plus | Arrow Lake‑HX (добавлены в 2026) | Q1 2026 [A24][W4] |
| Core 7 245HX (без «Ultra») | Arrow Lake‑HX по Википедии; страница ARK отдаёт 404, **не проверено** | Q1 2026 [W4] |
| Core Ultra 5/7/9 2xxV | Lunar Lake | сен 2024 [A16][W5] |
| Core Ultra 5/7/9 3xxH, Core Ultra X7/X9 3xxH, Core Ultra 5/7 3xx | Panther Lake | янв 2026 [A17–A20][W6] |
| Core 3/5/7 3xx (без «Ultra» и без буквы) | Wildcat Lake (Core Series 3) | апр 2026 [A21][W6][O1] |
| Core 3 N3xx, Intel N1xx/N2xx | Twin Lake / Alder Lake‑N, только E‑ядра | 2023–2025 [A22][W2] |

### 1.2. Архитектура, техпроцесс, iGPU

| Семейство | P / E ядра | Техпроцесс | iGPU |
|---|---|---|---|
| Alder Lake H/P/U | Golden Cove / Gracemont | Intel 7 | Xe‑LP, до 96 EU [W2] |
| Raptor Lake H/P/U, Core 1xxU/2xxU/2xxH | Raptor Cove по Intel, Golden Cove по Notebookcheck / Gracemont | Intel 7 | Xe‑LP, 48–96 EU [W1][N1–N4] |
| Raptor Lake‑HX (13/14) | Raptor Cove (у части моделей кристалл Alder Lake) / Gracemont | Intel 7 | Xe‑LP UHD, 16–32 EU [W1][A11] |
| Meteor Lake H/U | Redwood Cove / Crestmont (+2 LP‑E) | Intel 4 + TSMC N5/N6 | Xe‑LPG, 3–8 Xe [W3][A12] |
| Arrow Lake‑U | Redwood Cove / Crestmont (+2 LP‑E) | Intel 3 | Xe‑LPG, 4 Xe [W4][A13] |
| Arrow Lake‑H | Lion Cove / Skymont (+2 LP‑E Crestmont) | TSMC N3B | Xe‑LPG+ (Arc 130T/140T), 7–8 Xe [W4][A14][A15] |
| Arrow Lake‑HX | Lion Cove / Skymont | TSMC N3B | Xe‑LPG, 3–4 Xe [W4][A23] |
| Lunar Lake | Lion Cove / Skymont (LP‑E) | TSMC N3B + N6 | Xe2 (Arc 130V/140V), 7–8 Xe [W5][A16] |
| Panther Lake | Cougar Cove / Darkmont | Intel 18A; GPU — Intel 3 (4 Xe) или TSMC N3E (10–12 Xe) | Xe3: 4 Xe, Arc B370 10 Xe, Arc B390 12 Xe [W6][A17–A20] |
| Wildcat Lake | Cougar Cove / Darkmont (LP‑E) | Intel 18A | Xe3, 1–2 Xe [W6][A21] |
| Twin Lake N | только Gracemont | Intel 7 | Xe‑LP UHD, 24–32 EU [W2][A22] |

Как названа iGPU, зависит от памяти:
- **Iris Xe** работает только при двухканальной памяти; при одном канале это «UHD Graphics» [I2].
- **Arc** у Meteor Lake и Arrow Lake‑H включается при ≥16 ГБ в двух каналах [A12][A14].
- **Arc B390/B370** у Panther Lake требует LPDDR5X не медленнее 7467 МТ/с, иначе iGPU называется «Intel Graphics» [W6]. (Локальная проверка 30.09.2026: в сноске ARK у X7 358H этого условия нет, там только «≥16 ГБ в двух каналах» — порог 7467 **не проверено** по Intel.) → проверено в браузере 30.09.2026: (п. 5.15) Порога 7467 МТ/с у Intel нет: в Quick Reference Guide Series 3 условие — «minimum Xe core requirement»; цифра 7467 — от инсайдера (VideoCardz, 01.02.2026) ([cdrdv2-public.intel.com](https://cdrdv2-public.intel.com/871380/Intel%20Core%20Ultra%20Series%203%20Processors%20-%20Quick%20Reference%20Guide%20v1.pdf)).

### 1.3. Ядра, NPU, память, вердикт

| Семейство (примеры) | Ядра / потоки | NPU | Память | Вердикт |
|---|---|---|---|---|
| 12‑е H: i5‑12450H, i7‑12650H, i7‑12700H | 4+4 … 6+8 / 12–20 | нет | DDR5‑4800 или DDR4 SO‑DIMM, LPDDR5 [A8] | старый кремний (2022) |
| 13‑е H/P/U: i5‑13420H, i7‑13620H, i7‑13700H, i5‑1335U | 2+8 … 6+8 / 12–20 | нет | DDR5‑5200 SO‑DIMM, DDR4, LPDDR5/5X [A9] | старый кремний (2023) |
| 13/14‑е HX: i5‑13450HX, i7‑14650HX, i9‑14900HX | 6+4 … 8+16 / 16–32 | нет | DDR5‑4800/5600, DDR4 SO‑DIMM [A10][A11] | старый кремний: мощный CPU, слабая iGPU |
| Core 3/5/7 1xxU и Core 5/7 2xxU | 2+8 (100U: 2+4) / 12 | нет | DDR5‑5200 SO‑DIMM, LPDDR5/5X [A6][A7] | переименованный старый кремний; **2xxU — ловушка** |
| Core 5/7/9 2xxH: 210H, 220H, 240H, 250H, 270H | 4+4 … 6+8 / 12–20 | нет | DDR5‑5200/6400 SO‑DIMM, LPDDR5/5X [A1–A5] | **переименованный старый кремний — ловушка** |
| Core Ultra 1xxH: 125H, 135H, 155H, 165H, 185H | 4+8+2 … 6+8+2 / 18–22 | 11 TOPS | DDR5‑5600 SO‑DIMM или LPDDR5X‑7467 [A12] | современный (дек 2023) |
| Core Ultra 1xxU: 125U, 135U, 155U, 165U | 2+8+2 / 14 | 11 TOPS | DDR5‑5600 или LPDDR5X; 9‑ваттные 134U/164U — только LPDDR [W3] | современный, но слаб для 4K |
| Core Ultra 2xxU: 225U, 235U, 255U, 265U | 2+8+2 / 14 | 12 TOPS | DDR5‑6400 или LPDDR5X‑8400 [A13] | **ловушка имени: по ядрам это Meteor Lake** (в ARK — Arrow Lake) |
| Core Ultra 2xxH: 225H, 235H, 255H, 265H, 285H | 4+8+2 … 6+8+2 / 14–16 | 13 TOPS | DDR5‑6400 SO‑DIMM или LPDDR5X‑8400 [A14][A15] | **современный ✔** |
| Core Ultra 2xxHX: 235HX … 285HX, 251HX | 6+8 … 8+16 / 14–24 | 13 TOPS | DDR5‑6400 SO‑DIMM [A23][A24] | современный, для игровых и мощных машин |
| Core Ultra 2xxV: 226V … 288V | 4+4 / 8 | 40–48 TOPS | только LPDDR5X‑8533 на корпусе, 16/32 ГБ [A16][W5] | современный, но **2×16 невозможно** |
| Core Ultra X7/X9 3xxH: 358H, 368H, 378H, 388H; Core Ultra 5 338H | 4+8+4 (у 338H 4+4+4) / 12–16 | 47–50 TOPS | **только LPDDR5X** 8533/9600, распаяна [A17][A19][W6] | современный, но **2×16 SO‑DIMM невозможно** |
| Core Ultra 3xxH без X: 336H, 356H, 366H, 386H | 4+4+4 … 4+8+4 / 12–16 | 47–50 TOPS | DDR5‑7200 SO‑DIMM или LPDDR5X‑8533 [A18][A20][W6] | **современный ✔**, если производитель поставил слоты |
| Core Ultra 3xx без буквы: 322, 325, 332, 335, 355, 365 | 2–4 P + 4 LP‑E / 6–8 | 46–49 TOPS | DDR5‑6400 или LPDDR5X‑7467 [A25][W6] | современный, но слаб для 4K: нет обычных E‑ядер |
| Core 3/5/7 3xx (Wildcat Lake): 304 … 360 | 1–2 P + 4 LP‑E / 5–6 | 15–17 TOPS | **1 канал**, DDR5‑6400 или LPDDR5X‑7467, до 64 ГБ [A21][W6] | **ловушка для монтажа** |
| Core 3 N355, Intel N150/N250 (Twin Lake) | 8 или 4 E / 8 или 4 | нет | **1 канал**, до 16 ГБ (у N355 по ARK) [A22] | **ловушка** |

В таблице — примеры моделей; полные списки SKU — в [W1–W6].

### 1.4. Карта переименований

Частоты — максимальный Turbo P‑ядер: новый / 13‑е поколение / 12‑е поколение.

| Новое имя | = 13‑е поколение | ≈ 12‑е поколение | Конфигурация | Turbo, ГГц |
|---|---|---|---|---|
| Core 5 210H | i5‑13420H | i5‑12450H | 4P+4E, 48 EU, 12 МБ | 4.8 / 4.6 / 4.4 |
| Core 5 220H | i5‑13500H | i5‑12500H | 4P+8E, 80 EU, 18 МБ | 4.9 / 4.7 / 4.5 |
| Core 7 240H | i7‑13620H | i7‑12650H | 6P+4E, 64 EU, 24 МБ | 5.2 / 4.9 / 4.7 |
| Core 7 250H | i7‑13700H | i7‑12700H | 6P+8E, 96 EU, 24 МБ | 5.4 / 5.0 / 4.7 |
| Core 9 270H | i9‑13900H | i9‑12900H | 6P+8E, 96 EU, 24 МБ | 5.8 / 5.4 / 5.0 |
| Core 7 150U ≈ Core 7 250U | i7‑1355U / 1365U | i7‑1255U / 1265U | 2P+8E, 96 EU, 12 МБ | 5.4 / 5.0–5.2 / 4.7–4.8 |
| Core 5 120U ≈ Core 5 220U | i5‑1335U | i5‑1235U | 2P+8E, 80 EU, 12 МБ | 5.0 / 4.6 / 4.4 |
| Core 3 100U | i3‑1315U | i3‑1215U | 2P+4E, 64 EU, 10 МБ | 4.7 / 4.5 / 4.4 |

Источники таблицы: ARK [A1–A9], Википедия [W1][W2], Notebookcheck [N1–N4].
Core 7 250U отличается от 150U только поддержкой LPDDR5X‑6400 вместо 5200 [A6][A7]. Core 5 220U и 120U совпадают по таблице Википедии [W1]; по ARK не сверял.
Notebookcheck прямо пишет, что Core 7 250H — это «similar i7‑13700H» с «+400 MHz boost» [N1],
Core 7 240H — улучшенный i7‑13620H [N2], а Core 5 210H — «old Core i5‑13420H» с «+200 MHz» [N3].

**HX‑серия, 14 → 13 поколение** (совпадение по ядрам и кешу, [W1][A10][A11]):

| 14‑е HX | ≈ 13‑е HX | Конфигурация | Turbo, ГГц |
|---|---|---|---|
| i5‑14450HX | i5‑13450HX (кристаллы и Alder, и Raptor Lake) | 6P+4E | 4.8 / 4.6 |
| i5‑14500HX | i5‑13500HX (кристалл Alder Lake) | 6P+8E, 24 МБ | 4.9 / 4.7 |
| i7‑14650HX | i7‑13700HX (кристаллы и Alder, и Raptor Lake) | 8P+8E, 30 МБ | 5.2 / 5.0 |
| i7‑14700HX | ≈ i7‑13850HX | 8P+12E | 5.5 / 5.3 |
| i9‑14900HX | ≈ i9‑13980HX / 13950HX | 8P+16E, 36 МБ | 5.8 / 5.6 |

Какой кристалл стоит у конкретных 14‑х HX, **не проверено**: пометка «Alder Lake» в [W1] есть только у 13‑х моделей. → проверено в браузере 30.09.2026: (п. 5.16) Все 14-е HX — кристалл Raptor Lake B-0, 8P+16E (даташит 743844, CPUID; ARK Ordering: 14900HX…14450HX — B0) ([edc.intel.com](https://edc.intel.com/content/www/us/en/design/products/platforms/details/raptor-lake-s/13th-generation-core-processors-datasheet-volume-1-of-2/cpuid/)).

**Core Ultra 200U = Meteor Lake‑U** [W3][W4][A13] (по ядрам и iGPU; официальное кодовое имя в ARK — Arrow Lake [A13][N5]):

| Новое | ≈ Старое | Конфигурация | Turbo, ГГц |
|---|---|---|---|
| Core Ultra 7 265U / 255U | Core Ultra 7 165U / 155U | 2P+8E+2LP, 4 Xe | 5.3 / 4.9; 5.2 / 4.8 |
| Core Ultra 5 235U / 225U | Core Ultra 5 135U / 125U | 2P+8E+2LP, 4 Xe | 4.9 / 4.4; 4.8 / 4.3 |

Отличие одно: техпроцесс Intel 3 вместо Intel 4.

---

## 2. Кодеки Quick Sync по поколениям

### 2.1. Что умеет железо (драйвер Intel media-driver, Linux VA‑API)

Источник — таблицы Intel в README [D1] и `docs/media_features.md` [D2].

Как Intel группирует платформы:
- **TGLx** — Tiger Lake, Rocket Lake, **Alder Lake, Raptor Lake**: 12–14‑е поколение и Core Series 1/2;
- **MTLx** — **Meteor Lake, Arrow Lake‑S/H**;
- **LNL** — Lunar Lake;
- **PTL** — Panther Lake;
- **NVL** — Nova Lake (есть в драйвере; в ноутбуках на 30.09.2026 — не проверено).

Обозначения: D — аппаратное декодирование, E — аппаратное кодирование (VDEnc), Es — кодирование через PAK и шейдеры.

| Кодек | TGLx (12–14) | MTLx (MTL/ARL) | LNL | PTL |
|---|---|---|---|---|
| H.264 | D/E | D/E | D/E | D/E |
| HEVC 8/10 бит 4:2:0 | D/E | D/E | D/E | D/E |
| HEVC 8/10 бит 4:2:2 | D, Es | **только D** (в Linux; по даташиту Intel есть и E — см. ниже) | D/E | D/E |
| HEVC 8/10 бит 4:4:4 | D/E | D/E | D/E | D/E |
| HEVC 12 бит | D | D | D | D |
| VP9 8/10 бит | D/E | D/E | только D | D/E |
| AV1 8/10 бит | **только D** | D/E | D/E | D/E |
| VVC (H.266) 8/10 бит | — | — | D | D |

Важные детали из [D2]:
- **H.264 декодируется только в NV12, то есть 8 бит 4:2:0, до 4K, на всех платформах, включая PTL и NVL.**
  Значит, H.264 10 бит и H.264 4:2:2 драйвер Intel под Linux аппаратно не декодирует нигде.
  Документ Intel oneVPL для 11–13‑го поколения тоже даёт для AVC только «8‑bit, 4:2:0» [I1].
- HEVC 10 бит выдаётся как P010/Y210/Y410, то есть 4:2:0/4:2:2/4:4:4. Предел — 8K на TGLx и 16K на MTLx и новее.
- **Кодирование AV1 появилось только в MTLx.** У 12–14‑го поколения и у Core 1xxU/2xxH его нет.
- VVC есть только на декодирование, начиная с Lunar Lake (Xe2) и Panther Lake (Xe3). У Arrow Lake его нет.

**Даташиты Intel EDC (от ОС не зависят; добавлено при локальной проверке 30.09.2026)** [E1–E4]:
- Raptor Lake (13‑е поколение S/H/P/HX/U, ред. 30.05.2025), декод: AVC — High/Main, **только 4:2:0 8 бит**; HEVC — вплоть до Main 4:2:2 10/12 и 4:4:4; AV1 — декод. Кодирование: AVC, HEVC (в т. ч. Main 4:2:2 10), VP9 — **AV1‑кодирования нет** [E1][E2].
- Meteor Lake‑U/P (ред. 09.05.2025), декод: AVC — **только 4:2:0 8 бит**; HEVC 4:2:0/4:2:2/4:4:4 8/10/12 бит. Кодирование: AV1 8/10 бит, **HEVC Main10 4:2:2 8/10 бит до 4K@60** [E3][E4].
- (исправлено при локальной проверке 30.09.2026: пометка «HEVC 4:2:2 у MTLx только D» верна только для Linux‑драйвера [D1]; по даташиту Intel аппаратное кодирование HEVC 4:2:2 у Meteor Lake есть [E4]. На выбор ноутбука не влияет: для монтажа важен декод.)
- Media-driver обновлён 22.06.2026 (добавлен NVL, дописан PTL): у PTL и NVL для AVC по‑прежнему только NV12 [D2].

**Panther Lake и Wildcat Lake (Xe3): что заявлено сверх таблицы**
- Chips and Cheese, 14.10.2025: «The Media Engine now supporting AVC 10b decode and encode» [C1].
- Wccftech, 09.10.2025, пересказ Intel Tech Tour: «Some new additions include AVC 10‑bit support, and Sony XAVC‑H, XAVC‑HS, and XAVC‑S support» [C2].
- Notebookcheck (Wildcat Lake Xe3): «AV1 encoding and decoding, VVC decode, AVC 10‑bit and VP9 enc/dec» [C4]. То же пишет про Panther Lake [C3].
- ASUS добавляет «AV1 4:4:4 encode and decode» [C5].
- **Декодирует ли Xe3 именно H.264 4:2:2 10 бит и есть ли это в Resolve/Premiere — не проверено.** В Linux‑драйвере у PTL для AVC пока только NV12 [D2]. → проверено в браузере 30.09.2026: (п. 5.13) см. строку 29 ([cdrdv2.intel.com](https://cdrdv2.intel.com/v1/dl/getContent/872188?fileName=872188-002.pdf)).
- Локальная проверка 30.09.2026: Phoronix (09.10.2025, Intel Tech Tour) подтверждает формулировку Intel — «10-bit AVC encode/decode» и XAVC‑H/HS/S [PH1]; про 4:2:2 Intel не пишет. → проверено в браузере 30.09.2026: (п. 5.13) см. строку 29 ([cdrdv2.intel.com](https://cdrdv2.intel.com/v1/dl/getContent/872188?fileName=872188-002.pdf)).
  Тестов H.264 10 бит / 4:2:2 на Panther Lake в Resolve или Premiere не нашёл: у Puget таблицы не обновлялись с июня 2025 [P1][P2], страница Adobe (07.01.2026) называет для Intel только HEVC 4:2:2 10 бит [AD1]. **По‑прежнему не проверено.** → проверено в браузере 30.09.2026: (п. 5.13) см. строку 29 ([cdrdv2.intel.com](https://cdrdv2.intel.com/v1/dl/getContent/872188?fileName=872188-002.pdf)).

### 2.2. Что реально работает в программах (Windows)

**DaVinci Resolve Studio** — тест Puget Systems, обновлено 17.06.2025 [P1]:

| Формат | Intel 11–14 | Core Ultra 200 | RTX 20/30/40 | RTX 50 (Resolve 20+) | Radeon 5000–7000 |
|---|---|---|---|---|---|
| H.264 8 бит 4:2:0 | да | да | да | да | да |
| H.264 10 бит 4:2:0 | нет | нет | нет | да | нет |
| H.264 8/10 бит 4:2:2 | нет | нет | нет | да | нет |
| HEVC 8/10 бит 4:2:0 | да | да | да | да | да |
| HEVC 8/10 бит 4:2:2 | **да** | **да** | нет | да | нет |
| HEVC 4:4:4, 12 бит | да | да | 4:4:4 да, 12 бит 4:2:2 нет | да | нет |

**Adobe Premiere Pro** — тест Puget Systems, обновлено 12.06.2025 [P2]:

| Формат | Intel 11–14 | Core Ultra 200 | RTX 20/30/40 | RTX 50 (Premiere 25.3+) |
|---|---|---|---|---|
| H.264 8 бит 4:2:0 | да | да | да | да |
| H.264 10 бит 4:2:0 и 4:2:2 | нет | нет | нет | да |
| H.264 8 бит 4:2:2 | нет | нет | нет | нет |
| HEVC 8/10 бит 4:2:0 | да | да | да | да |
| HEVC 10 бит 4:2:2 | **да** | **да** | нет | да |
| HEVC 8 бит 4:2:2, 4:4:4, 12 бит | нет | нет | нет | нет |

Уточнения:
- «Core Ultra 200» у Puget — вероятно, десктопный Arrow Lake‑S: в той же таблице десктопные Ryzen 7000/9000. Медиаблок у него тот же, что у Meteor Lake и Arrow Lake‑H (группа MTLx [D1]).
  Lunar Lake и Panther Lake Puget не тестировал (локальная проверка 30.09.2026: обе статьи Puget последний раз обновлены 17.06.2025 и 12.06.2025, колонок LNL/PTL нет; других тестов не нашёл).
- Дискретные Intel Arc A/B в Resolve декодируют HEVC 10 бит 4:2:2, но не 8 бит 4:2:2 и не 4:4:4 [P1].
- У HX‑серии iGPU маленькая (16–32 EU), но кристалл тот же, что у десктопных Raptor Lake‑S. В драйвере Intel это одна группа TGLx (RPL‑S) [D1], а десктопные 13/14‑е Puget и тестировал [P1].
  Отсюда вывод: Quick Sync у HX декодирует так же. Это вывод, отдельным тестом не проверено.

### 2.3. NVIDIA и AMD для сравнения

- **RTX 40 (Ada, NVDEC 5‑го поколения):**
  - H.264 — только 8 бит 4:2:0;
  - HEVC 4:2:0 и 4:4:4 — до 12 бит; **HEVC 4:2:2 — нет**;
  - NVENC 8‑го поколения 4:2:2 не кодирует [V1].
- **RTX 50 (Blackwell, NVDEC 6‑го поколения):**
  - «4:2:2 H.264 and HEVC decode support»; NVENC 9‑го поколения «adds support for 4:2:2 H.264 and HEVC encoding» [V2];
  - по матрице NVIDIA — H.264 4:2:0 10 бит, H.264 4:2:2 8/10 бит, HEVC 4:2:2 8/10/12 бит [V1].
  - RTX 5050/5060 Laptop в матрице не перечислены, есть 5070 Laptop и старше. Поддержку у 5050/5060 Laptop логично ожидать, но это **не проверено**. → проверено в браузере 30.09.2026: (п. 5.14) Строк RTX 5050/5060 Laptop в матрице NVIDIA по-прежнему нет, но у них NVDEC 6-го поколения (NVIDIA, сравнение ноутбучных GPU) — это он даёт «4:2:2 H.264 and HEVC decode» (whitepaper Blackwell) ([nvidia.com](https://www.nvidia.com/en-us/geforce/laptops/compare/)).
    Локальная проверка 30.09.2026: строк 5050/5060 Laptop в матрице по‑прежнему нет; при этом десктопные RTX 5050/5060 и младшие мобильные RTX PRO 500/1000 Blackwell указаны с полным набором (H.264 4:2:2 8/10, HEVC 4:2:2 8/10/12) [V1]. У RTX 4060 Laptop: H.264 10 бит — NO, H.264 4:2:2 — NO, HEVC 4:2:2 — NO [V1]. → проверено в браузере 30.09.2026: (п. 5.14) см. строку 241 ([nvidia.com](https://www.nvidia.com/en-us/geforce/laptops/compare/)).
  - У RTX 5050 и 5060 Laptop по 8 ГБ GDDR7 [V3].
- **Windows‑плееры:** по данным issue [V4], D3D11/DXVA в Windows не даёт профиль H.264 High 4:2:2 10 бит. Поэтому, например, LAV Filters не декодирует его даже на RTX 50.
  Монтажные программы работают через API производителей — см. таблицы выше.
- **AMD** (Radeon 5000–7000 и iGPU Ryzen 7000/9000): 4:2:2 не декодирует ни в H.264, ни в HEVC [P1][P2]. Radeon RX 9000 в таблицах Puget нет — не проверено. → проверено в браузере 30.09.2026: (п. 5.17) В таблицах Puget RX 9000 нет (обновлены 06.2025); по обзорам Puget RDNA4 4:2:2 10 бит в Resolve не ускоряет ([pugetsystems.com](https://www.pugetsystems.com/labs/articles/amd-radeon-rx-9070-xt-content-creation-review/)).

### 2.4. Что это значит для файлов с камеры

- У Sony: **XAVC S** — это H.264, **XAVC HS** — HEVC 10 бит. XAVC бывает 8/10/12 бит и 4:2:0/4:2:2/4:4:4 [K1].
- Итог по Intel:
  - HEVC 4:2:2 10 бит (XAVC HS и HEVC‑режимы других камер) — Intel 11‑го поколения и новее декодирует аппаратно;
  - H.264 4:2:2 10 бит (часто XAVC S / XAVC S‑I в 10‑битных режимах) — Intel аппаратно не декодирует. Для таких файлов нужны RTX 50, мощный CPU или прокси.
- Что именно пишет ваша камера, проверяйте в **MediaInfo** (подробный вид, «Tree») — так советует и Puget [P1].
- Какие кодеки у конкретных моделей Canon, Panasonic и Fujifilm — не проверено, смотрите MediaInfo. → проверено в браузере 30.09.2026: (п. 5.29) Браузер не закроет: какие кодеки у камеры, покажет MediaInfo по исходному файлу — вопрос владельцу. Теперь это важнее: H.264 4:2:2 10 бит → RTX 50 или Panther Lake + Resolve Studio 21 (п. 5.13) (вопрос пользователю).

---

## 3. Программы монтажа: кто использует iGPU Intel

| Программа | Windows | Linux |
|---|---|---|
| **Resolve Studio** | Декодирует на Intel iGPU HEVC до 4:2:2/4:4:4, H.264 — только 8 бит 4:2:0 [P1] | H.264/H.265: «Studio only (GPU accelerated on Nvidia graphics)», **Intel в документе не указан** [R1] |
| **Resolve (бесплатный)** | Только профили, которые умеет Windows (H.264 8 бит, H.265 8/10 бит); «More profiles and GPU acceleration in Studio» [R1] | **H.264/H.265 не поддерживаются** [R1][R2] |
| **Premiere Pro** | Декодирует на Intel iGPU HEVC 10 бит 4:2:2 (11‑е поколение и новее) [P2] | Linux‑версии нет (сайт Adobe из облака недоступен — не проверено) |
| **Kdenlive 26.08** | — | Аппаратный экспорт: пресеты «Hardware Accelerated (experimental)», в том числе «VAAPI Intel H264». Про аппаратное декодирование в документации ничего нет [K2] |
| **Shotcut** | Аппаратное декодирование (если включено) — только до 1080p или с preview scaling; аппаратный экспорт — опция [K3] | то же [K3] |

Подробности:
- **Resolve.**
  - Аппаратное декодирование включается в Preferences → Decode Options [P1].
  - AAC‑звук Resolve под Linux не читает ни в Free, ни в Studio [R2].
  - В сноске Blackmagic сказано: «Encoding video resolutions ≥ 4K is only supported with DaVinci Resolve Studio» [R1].
    При этом страница продукта обещает в бесплатной версии выпуск до UHD 3840×2160 60p [R3]. Формулировки расходятся — **не проверено**.
  - Для HEVC 4:2:2 10 бит закладывайтесь на Studio.
- **Kdenlive и Shotcut под Linux:** реальный путь для 4K 10 бит — прокси или промежуточный кодек. Аппаратное декодирование 4K в таймлайне там не заявлено [K2][K3].

---

## 4. Известные проблемы

**Raptor Lake: деградация («Vmin Shift Instability»)**
- Intel называет причиной высокое напряжение в цепи тактирования ядра. Затронуты десктопные 13/14‑е поколения; исправлялось микрокодами 0x125, 0x129, 0x12B и 0x12F [W1].
- **Мобильные 13/14‑е, включая HX, по заявлению Intel не затронуты**; Arrow Lake и Lunar Lake — тоже [H1]. Подтверждено первоисточником при локальной проверке 30.09.2026: блог Intel от 25.09.2024 — 13th/14th Gen mobile и Lunar Lake / Arrow Lake «are unaffected» [I4].
  Жалобы на вылеты ноутбуков с HX были (например, от Alderon Games). Intel ответила, что это «common symptoms» других проблем, а не тот же баг [T1].
- Отдельные сообщения о BSOD на i9‑14900HX есть на форуме Intel [F1] — **официально не подтверждено**.

**Драйверы iGPU 11–14‑го поколения — в режиме legacy**
- С 19.09.2025 для них выходят только квартальные драйверы: «Only critical fixes and security vulnerabilities», без Day‑0 поддержки игр [I3].
- Core Series 1/2 (тот же Xe‑LP) в статье прямо не названы. Что их это тоже касается — **не проверено, но вероятно**.
  (исправлено при локальной проверке 30.09.2026: статья перечисляет кодовые имена «Tiger Lake, Rocket Lake, Alder Lake, Twin Lake, Raptor Lake, Raptor Lake Refresh», в том числе «Raptor Lake‑H Refresh, Raptor Lake‑U Refresh». В ARK у Core 5/7/9 2xxH, Core 7 150U и 250U кодовое имя — Raptor Lake [A1–A7]. Значит, legacy касается и их, и N‑серии (Twin Lake). Названия «Series 1/2» Intel не пишет, но по кодовому имени это **подтверждено**. Статья пересмотрена 23.10.2025; Day‑0 для игр больше нет [I3].)

**Lunar Lake (Core Ultra 2xxV)**
- Память LPDDR5X‑8533 на корпусе, 16 или 32 ГБ. Заменить или расширить нельзя [W5][A16].

**Panther Lake**
- X7/X9 и Core Ultra 5 338H работают только с LPDDR5X [A17][A19].
- Без LPDDR5X‑7467+ iGPU теряет имя Arc B390/B370 [W6].
- Платформа новая. Готовность Linux (драйвер xe, media‑driver) для конкретного ноутбука — **не проверено**. → проверено в браузере 30.09.2026: (п. 5.18) xe включает PTL по умолчанию с Linux 6.17, Mesa 25.2 — тоже; но AVC в VA-API у PTL только NV12 (8 бит 4:2:0). Конкретного PTL-ноутбука нет — не проверяли ([phoronix.com](https://www.phoronix.com/news/Intel-Panther-Lake-Mesa-Default)).

**Wildcat Lake**
- Один канал памяти [A21], два P‑ядра. Для монтажа 4K не подходит.

**Meteor Lake и Arrow Lake‑H**
- При одном канале памяти или <16 ГБ iGPU работает как «Intel Graphics», а не Arc [A12][A14].
- **Одна планка 1×32 ГБ режет iGPU** (Arc → «Intel Graphics», Iris Xe → UHD) [A12][I2]. Это ещё один довод за 2×16.

**Нагрев тонких ноутбуков с H/HX** — общая проблема, но конкретных данных по моделям здесь нет (не проверено). Смотрите обзоры конкретного SKU на Notebookcheck.

---

## 5. Рекомендация на ~1100 € (2×16 ГБ SO‑DIMM, 4K)

**Брать — по убыванию:**
1. **Core Ultra 5 225H / 235H, Core Ultra 7 255H** (Arrow Lake‑H, 2025) [A14][A15]:
   - два канала DDR5‑6400 SO‑DIMM;
   - Arc 130T/140T;
   - AV1‑энкодер;
   - аппаратный декод HEVC 4:2:2 10 бит;
   - NPU 13 TOPS.

   Проверьте в даташите ноутбука, что стоят **два слота**, а не распайка.
2. **Core Ultra 5 125H/135H, Core Ultra 7 155H** (Meteor Lake, дек 2023) [A12]:
   - медиаблок тот же, что у Arrow Lake (MTLx) [D1];
   - DDR5‑5600 SO‑DIMM.

   Хороший вариант, если заметно дешевле.
3. **Panther Lake без X: Core Ultra 5 336H, Core Ultra 7 356H/366H** с DDR5 SO‑DIMM [A18][A20]:
   - самый свежий кремний;
   - заявлены AVC 10 бит и Sony XAVC [C1][C2].

   Есть ли такие ноутбуки со слотами за ~1100 € — **не проверено**, смотрите `market.md`. → проверено в браузере 30.09.2026: (п. 1.20) МЕНЯЕТ ВЫВОД (B-список): Core Ultra H + 2×16 SO-DIMM + 1 ТБ ≤ 1100 € на idealo нет. Новое: HP OmniBook 7 AI 16-ay0770ng (BM9T4EA, 255H, 32 ГБ распайка, 1 ТБ) — 979,30 € (hp.com). X1607CA-MB120 32/1 ТБ — 1069,99 € (OTTO MP; у one.de 1039 €); AG16-71P-7607 — Core 7 150U (ловушка), 939,64 €; Aspire 16 AI 288V: -984U 1599 €, -916J от 1308,26 €, -92UY от 1348 €; Panther Lake со слотами ≤ 1100 € нет (21UR005AGE — 1205 €) ([idealo.de](https://www.idealo.de/preisvergleich/OffersOfProduct/206602335.html)).
4. **С дискретной картой ≥8 ГБ — только RTX 50** (5050/5060/5070 Laptop).
   - ~~Только Blackwell декодирует H.264 4:2:2 10 бит~~ Из видеокарт H.264 4:2:2 10 бит декодирует только Blackwell [V1][V2][P1][P2]; из iGPU — Panther Lake (Xe3), в Resolve Studio 21 (проверено в браузере 30.09.2026, [даташит Intel 872188](https://cdrdv2.intel.com/v1/dl/getContent/872188?fileName=872188-002.pdf)).
   - iGPU Intel при этом остаётся вторым декодером для HEVC 4:2:2.
   - С RTX 50 допустим и «старый» CPU: i7‑14650HX, Core 7 240H/250H. Но цена должна быть как у старого железа.
   - RTX 4060 4:2:2 не декодирует [V1] — для 10‑битного 4:2:2 это минус.

**Не брать:**
- Lunar Lake (2xxV) — 2×16 невозможно.
- Panther Lake X7/X9 и 338H — только распаянная LPDDR5X. Годятся лишь для альтернативного списка с распаянными 32 ГБ.
- Wildcat Lake (Core 3/5/7 3xx) и Twin Lake (N‑серия) — один канал памяти.
- Core 5/7 1xxU и 2xxU — Raptor Lake‑U с 2 P‑ядрами.
- Core Ultra 2xxU — Meteor Lake‑U под новым именем (в ARK значится Arrow Lake).
- 12‑е поколение — 2022 год, DDR5‑4800.
- **Core 5/7/9 2xxH** — не «новинка 2025», а 13‑е поколение. Брать, только если цена как у старого железа и в паре есть RTX 50.

### Проверка имени процессора за 30 секунд

1. **Есть «Ultra»?**
   - `1xx` → Meteor Lake;
   - `2xxH`/`2xxHX` → Arrow Lake;
   - `2xxU` → Meteor Lake под новым именем (ARK при этом пишет «Arrow Lake» — ориентируйтесь на букву U);
   - `2xxV` → Lunar Lake (память на корпусе);
   - `3xx` → Panther Lake; приставка **X** → только LPDDR5X.
2. **Нет «Ultra»?**
   - `Core 3/5/7 1xxU`, `2xxU`, `2xxH` → Raptor Lake 2023 года;
   - `Core 3/5/7 3xx` без буквы → Wildcat Lake, один канал;
   - `N…` → только E‑ядра;
   - `i5/i7/i9‑12/13/14xxx` → Alder/Raptor Lake.
3. **Откройте страницу модели в Intel ARK** (ark.intel.com) и посмотрите поля:
   - «Code Name» (Products formerly …); исключение — Core Ultra 2xxU: там «Arrow Lake», хотя ядра от Meteor Lake;
   - «Launch Date»;
   - «Max # of Memory Channels» — нужно **2**;
   - «Memory Types» — есть ли **DDR5**, без неё SO‑DIMM не бывает.
4. **В даташите ноутбука:** два слота SO‑DIMM и установлены 2×16. iGPU должна называться Arc или Iris Xe, а не «Intel/UHD Graphics».
5. **Проверьте свои файлы в MediaInfo:**
   - HEVC 4:2:2 → подходит любой Intel 11+;
   - H.264 4:2:2 10 бит → нужна RTX 50 (или прокси). → проверено в браузере 30.09.2026: или Panther Lake + Resolve Studio 21 (п. 5.13, [readme Resolve 21](https://www.blackmagicdesign.com/support/readme/2cda7ec076ea4b25aaa007fc68a5cbfc)).

---

## 6. Источники

**Кодеки и драйверы**
- [D1] Intel media-driver README: <https://raw.githubusercontent.com/intel/media-driver/master/README.md>
- [D2] Intel media-driver, media_features.md: <https://raw.githubusercontent.com/intel/media-driver/master/docs/media_features.md>
- [I1] Intel oneVPL, Media Capabilities Supported by Intel Hardware, v1.1 (03.2024): <https://www.intel.com/content/www/us/en/docs/onevpl/developer-reference-media-intel-hardware/1-1/overview.html>
- [I2] Intel: Iris Xe требует двухканальную память: <https://www.intel.com/content/www/us/en/support/articles/000094617/graphics.html>
- [I3] Intel: Graphics Driver Support Update for 11th–14th Gen (19.09.2025): <https://www.intel.com/content/www/us/en/support/articles/000101986/graphics.html>
- [P1] Puget Systems, HW decode в Resolve Studio (обн. 17.06.2025): <https://www.pugetsystems.com/labs/articles/what-h-264-and-h-265-hardware-decoding-is-supported-in-davinci-resolve-studio-2122/>
- [P2] Puget Systems, HW decode в Premiere Pro (обн. 12.06.2025): <https://www.pugetsystems.com/labs/articles/what-h-264-and-h-265-hardware-decoding-is-supported-in-premiere-pro-2120/>
- [V1] NVIDIA Video Encode and Decode GPU Support Matrix: <https://developer.nvidia.com/video-encode-and-decode-gpu-support-matrix-new>
- [V2] NVIDIA RTX Blackwell GPU Architecture (whitepaper), с. 27–30: <https://images.nvidia.com/aem-dam/Solutions/geforce/blackwell/nvidia-rtx-blackwell-gpu-architecture.pdf>
- [V3] NVIDIA, GeForce RTX 50 Laptops (объём VRAM): <https://www.nvidia.com/en-us/geforce/laptops/50-series/>
- [V4] LAV Filters issue #712 (H.264 4:2:2 10 бит и D3D11): <https://github.com/Nevcairiel/LAVFilters/issues/712>
- [C1] Chips and Cheese, Panther Lake’s Reveal at ITT 2025 (14.10.2025): <https://chipsandcheese.com/p/panther-lakes-reveal-at-itt-2025>
- [C2] Wccftech, Intel Xe3 Graphics Official (09.10.2025): <https://wccftech.com/intel-xe3-graphics-official-50-percent-faster-than-xe2-xe3p-next-gen-arc-family/>
- [C3] Notebookcheck, Intel Graphics 4 Xe3 (Panther Lake): <https://www.notebookcheck.net/Intel-Graphics-4-Xe3-Panther-Lake-Benchmarks-and-Specs.1193658.0.html>
- [C4] Notebookcheck, Intel Graphics 2‑Core Xe3 (Wildcat Lake): <https://www.notebookcheck.net/Intel-Graphics-2-Core-Xe3-Wildcat-Lake-iGPU-Benchmarks-and-Specs.1302173.0.html>
- [C5] ASUS blog, Panther Lake iGPU (13.02.2026): <https://www.asus.com/blog/intel-panther-lake-igpu-in-asus-laptops-a-leap-forward-for-gamers-and-creators/>
- [K1] Wikipedia, XAVC: <https://en.wikipedia.org/wiki/XAVC>

**Программы**
- [R1] Blackmagic, DaVinci Resolve 21.1 Supported Formats and Codecs (сентябрь 2026): <https://documents.blackmagicdesign.com/SupportNotes/DaVinci_Resolve_21_Supported_Codec_List.pdf>
- [R2] XDA, Resolve на Linux: нет H.264/H.265 в Free, нет AAC (27.03.2026): <https://www.xda-developers.com/davinci-resolve-fixed-biggest-problem-linux-run-out-reasons-keep-windows/>
- [R3] Blackmagic, DaVinci Resolve Studio / сравнение версий: <https://www.blackmagicdesign.com/products/davinciresolve/studio>
- [K2] Kdenlive 26.08 Manual, Rendering: <https://docs.kdenlive.org/en/exporting/render.html>
- [K3] Shotcut FAQ: <https://www.shotcut.org/FAQ/>

**Процессоры (Wikipedia)**
- [W1] Raptor Lake (в т. ч. Core Series 1/2, HX и раздел про нестабильность): <https://en.wikipedia.org/wiki/Raptor_Lake>
- [W2] Alder Lake (в т. ч. Alder Lake‑N и Twin Lake): <https://en.wikipedia.org/wiki/Alder_Lake>
- [W3] Meteor Lake: <https://en.wikipedia.org/wiki/Meteor_Lake>
- [W4] Arrow Lake (в т. ч. Arrow Lake‑U и Refresh 2026): <https://en.wikipedia.org/wiki/Arrow_Lake_(microprocessor)>
- [W5] Lunar Lake: <https://en.wikipedia.org/wiki/Lunar_Lake>
- [W6] Panther Lake + Wildcat Lake: <https://en.wikipedia.org/wiki/Panther_Lake_(microprocessor)>

**Intel ARK** (поля Code Name, Launch Date, Memory Types, Max # of Memory Channels)
- [A1] Core 5 210H: <https://www.intel.com/content/www/us/en/products/sku/241652/intel-core-5-processor-210h-12m-cache-up-to-4-80-ghz/specifications.html>
- [A2] Core 5 220H: <https://www.intel.com/content/www/us/en/products/sku/241654/intel-core-5-processor-220h-18m-cache-up-to-4-90-ghz/specifications.html>
- [A3] Core 7 240H: <https://www.intel.com/content/www/us/en/products/sku/241653/intel-core-7-processor-240h-24m-cache-up-to-5-20-ghz/specifications.html>
- [A4] Core 7 250H: <https://www.intel.com/content/www/us/en/products/sku/241651/intel-core-7-processor-250h-24m-cache-up-to-5-40-ghz/specifications.html>
- [A5] Core 9 270H: <https://www.intel.com/content/www/us/en/products/sku/241947/intel-core-9-processor-270h-24m-cache-up-to-5-80-ghz/specifications.html>
- [A6] Core 7 150U: <https://www.intel.com/content/www/us/en/products/sku/236795/intel-core-7-processor-150u-12m-cache-up-to-5-40-ghz/specifications.html>
- [A7] Core 7 250U: <https://www.intel.com/content/www/us/en/products/sku/238771/intel-core-7-processor-250u-12m-cache-up-to-5-40-ghz/specifications.html>
- [A8] i7‑12650H: <https://www.intel.com/content/www/us/en/products/sku/226066/intel-core-i712650h-processor-24m-cache-up-to-4-70-ghz/specifications.html>
- [A9] i7‑13620H: <https://www.intel.com/content/www/us/en/products/sku/232130/intel-core-i713620h-processor-24m-cache-up-to-4-90-ghz/specifications.html>
- [A10] i5‑13450HX: <https://www.intel.com/content/www/us/en/products/sku/232132/intel-core-i513450hx-processor-20m-cache-up-to-4-60-ghz/specifications.html>
- [A11] i7‑14650HX: <https://www.intel.com/content/www/us/en/products/sku/235996/intel-core-i7-processor-14650hx-30m-cache-up-to-5-20-ghz/specifications.html>
- [A12] Core Ultra 7 155H: <https://www.intel.com/content/www/us/en/products/sku/236847/intel-core-ultra-7-processor-155h-24m-cache-up-to-4-80-ghz/specifications.html>
- [A13] Core Ultra 7 255U: <https://www.intel.com/content/www/us/en/products/sku/241860/intel-core-ultra-7-processor-255u-12m-cache-up-to-5-20-ghz/specifications.html>
- [A14] Core Ultra 7 255H: <https://www.intel.com/content/www/us/en/products/sku/241751/intel-core-ultra-7-processor-255h-24m-cache-up-to-5-10-ghz/specifications.html>
- [A15] Core Ultra 5 225H: <https://www.intel.com/content/www/us/en/products/sku/241749/intel-core-ultra-5-processor-225h-18m-cache-up-to-4-90-ghz/specifications.html>
- [A16] Core Ultra 7 258V: <https://www.intel.com/content/www/us/en/products/sku/240957/intel-core-ultra-7-processor-258v-12m-cache-up-to-4-80-ghz/specifications.html>
- [A17] Core Ultra X7 358H: <https://www.intel.com/content/www/us/en/products/sku/245527/intel-core-ultra-x7-processor-358h-18m-cache-up-to-4-80-ghz/specifications.html>
- [A18] Core Ultra 7 356H: <https://www.intel.com/content/www/us/en/products/sku/245532/intel-core-ultra-7-processor-356h-18m-cache-up-to-4-70-ghz/specifications.html>
- [A19] Core Ultra 5 338H: <https://www.intel.com/content/www/us/en/products/sku/245531/intel-core-ultra-5-processor-338h-18m-cache-up-to-4-70-ghz/specifications.html>
- [A20] Core Ultra 5 336H: <https://www.intel.com/content/www/us/en/products/sku/245533/intel-core-ultra-5-processor-336h-18m-cache-up-to-4-60-ghz/specifications.html>
- [A21] Core 5 320 (Wildcat Lake): <https://www.intel.com/content/www/us/en/products/sku/246018/intel-core-5-processor-320-6m-cache-up-to-4-60-ghz/specifications.html>
- [A22] Core 3 N355 (Twin Lake): <https://www.intel.com/content/www/us/en/products/sku/241639/intel-core-3-processor-n355-6m-cache-up-to-3-90-ghz/specifications.html>
- [A23] Core Ultra 7 255HX: <https://www.intel.com/content/www/us/en/products/sku/242292/intel-core-ultra-7-processor-255hx-30m-cache-up-to-5-20-ghz/specifications.html>
- [A24] Core Ultra 7 251HX: <https://www.intel.com/content/www/us/en/products/sku/245959/intel-core-ultra-7-processor-251hx-30m-cache-up-to-5-10-ghz/specifications.html>
- [A25] Core Ultra 7 355: <https://www.intel.com/content/www/us/en/products/sku/245722/intel-core-ultra-7-processor-355-12m-cache-up-to-4-70-ghz/specifications.html>

**Notebookcheck и прочее**
- [N1] Notebookcheck, Core 7 250H: <https://www.notebookcheck.net/Intel-Core-7-250H-Processor-Benchmarks-and-Specs.936248.0.html>
- [N2] Notebookcheck, Core 7 240H: <https://www.notebookcheck.net/Intel-Core-7-240H-Processor-Benchmarks-and-Specs.936272.0.html>
- [N3] Notebookcheck, Core 5 210H: <https://www.notebookcheck.net/Intel-Core-5-210H-Processor-Benchmarks-and-Specs.936302.0.html>
- [N4] Notebookcheck, i7‑13620H: <https://www.notebookcheck.net/Intel-Core-i7-13620H-Processor-Benchmarks-and-Specs.677505.0.html>
- [O1] CNX Software, запуск Wildcat Lake (17.04.2026): <https://www.cnx-software.com/2026/04/17/intel-core-series-3-wildcat-lake-processor-family-launched-for-entry-level-laptops-and-edge-ai-systems/>
- [H1] HotHardware, «Arrow Lake и мобильные 13/14 не затронуты» (02.09.2024): <https://hothardware.com/news/arrow-lake-and-mobile-immune-crashing-issue>
- [T1] Tom’s Hardware, мобильные вылеты — «не тот же баг» (20.07.2024): <https://www.tomshardware.com/pc-components/cpus/intel-says-13th-and-14th-gen-mobile-cpus-are-crashing-but-not-due-to-the-same-bug-as-desktop-chips-chipmaker-blames-common-software-and-hardware-issues>
- [F1] Форум Intel, тема про BSOD на i9‑14900HX (ссылка из поиска; из облака страница отдаёт 403): <https://community.intel.com/t5/Mobile-and-Desktop-Processors/i9-14900HX-mobile-clock-dependent-single-bit-errors-BSODs-is/td-p/1754233>

**Добавлено при локальной проверке 30.09.2026**
- [E1] Intel EDC, 13th Gen Core Datasheet Vol. 1 (743844, ред. 30.05.2025), Hardware Accelerated Video Decode: <https://edc.intel.com/content/www/us/en/design/products/platforms/details/raptor-lake-s/13th-generation-core-processors-datasheet-volume-1-of-2/hardware-accelerated-video-decode/>
- [E2] То же, Hardware Accelerated Video Encode: <https://edc.intel.com/content/www/us/en/design/products/platforms/details/raptor-lake-s/13th-generation-core-processors-datasheet-volume-1-of-2/hardware-accelerated-video-encode/>
- [E3] Intel EDC, Core Ultra (Meteor Lake‑U/P) Datasheet Vol. 1 (792044, ред. 09.05.2025), Video Decode: <https://edc.intel.com/content/www/us/en/design/products/platforms/details/meteor-lake-u-p/core-ultra-processor-datasheet-volume-1-of-2/hardware-accelerated-video-decode/>
- [E4] То же, Video Encode: <https://edc.intel.com/content/www/us/en/design/products/platforms/details/meteor-lake-u-p/core-ultra-processor-datasheet-volume-1-of-2/hardware-accelerated-video-encode/>
- [I4] Intel Community blog, Intel Core 13th and 14th Gen Desktop Instability Root Cause Update (25.09.2024): <https://community.intel.com/t5/Blogs/Tech-Innovation/Client/Intel-Core-13th-and-14th-Gen-Desktop-Instability-Root-Cause/post/1633239>
- [AD1] Adobe, Supported codecs and drivers for hardware-accelerated decoding (обн. 07.01.2026): <https://helpx.adobe.com/premiere/desktop/get-started/technical-requirements/supported-codecs-and-drivers-for-hardware-accelerated-decoding.html>
- [PH1] Phoronix, Intel Showcased Panther Lake & Xe3 Graphics At Tech Tour Arizona 2025 (09.10.2025): <https://www.phoronix.com/review/intel-panther-lake/2>
- [N5] Notebookcheck, Core Ultra 7 255U: <https://www.notebookcheck.net/Intel-Core-Ultra-7-255U-Processor-Benchmarks-and-Specs.943065.0.html>
- [A26] ARK i5‑13420H: <https://www.intel.com/content/www/us/en/products/sku/232173/intel-core-i513420h-processor-12m-cache-up-to-4-60-ghz/specifications.html>
- [A27] ARK i5‑13500H: <https://www.intel.com/content/www/us/en/products/sku/232147/intel-core-i513500h-processor-18m-cache-up-to-4-70-ghz/specifications.html>
- [A28] ARK i7‑13700H: <https://www.intel.com/content/www/us/en/products/sku/232128/intel-core-i713700h-processor-24m-cache-up-to-5-00-ghz/specifications.html>
- [A29] ARK i9‑13900H: <https://www.intel.com/content/www/us/en/products/sku/232135/intel-core-i913900h-processor-24m-cache-up-to-5-40-ghz/specifications.html>
- [A30] ARK i7‑1355U: <https://www.intel.com/content/www/us/en/products/sku/232160/intel-core-i71355u-processor-12m-cache-up-to-5-00-ghz/specifications.html>
- [A31] ARK, серия Core i7 (14th gen): <https://www.intel.com/content/www/us/en/ark/products/series/236170/intel-core-i7-processors-14th-gen.html>

---

## Локальная проверка (30.09.2026)

Как проверял: страницы Intel ARK и intel.com (из облака отдавали 403) открыты в Chrome пользователя, в своей вкладке; поля взяты из таблицы спецификаций.
Media-driver, Puget, NVIDIA, Blackmagic, EDC, Notebookcheck скачаны напрямую; Adobe и Phoronix — через Chrome. Капч и входов не было.
Задача была попытаться опровергнуть каждое утверждение. Итог: **опровергнуто 0 выводов, уточнено 3, не проверено 3.**

| № | Утверждение | Вердикт | Что показал первоисточник |
|---|---|---|---|
| 1 | Core 5 210H / 220H / 240H / 250H / 270H = i5‑13420H / i5‑13500H / i7‑13620H / i7‑13700H / i9‑13900H | **подтверждено** | ARK: у обеих сторон кодовое имя «Raptor Lake», Intel 7. Совпадают ядра, кеш и EU: 4P+4E/12 МБ/48 EU; 4P+8E/18 МБ/80 EU; 6P+4E/24 МБ/64 EU; 6P+8E/24 МБ/96 EU (у 250H и 270H). Turbo выше на 0,2–0,4 ГГц. Дата выхода Q4'24 против Q1'23 [A1–A5][A9][A26–A29]. Notebookcheck: «similar i7-13700H … +400 MHz», «old Core i5-13420H … +200 MHz» [N1][N3] |
| 2 | Память у Core 2xxH: DDR5‑5200 (210H, 220H) или 6400 (240H, 250H, 270H), 2 канала | **подтверждено** | ARK [A1–A5] |
| 3 | Core 7 250U отличается от 150U только поддержкой LPDDR5X (6400 против 5200); оба Raptor Lake | **подтверждено** | ARK: 2P+8E, 12 МБ, 96 EU, 5,4 ГГц, DDR5‑5200 у обоих; LPDDR5/X 6400 против 5200; Q1'25 против Q1'24. У i7‑1355U те же 2P+8E, 12 МБ, 96 EU, 5,0 ГГц [A6][A7][A30] |
| 4 | Core Ultra 2xxU — «не Arrow Lake, а Meteor Lake refresh» | **уточнено** | ARK: у 255U кодовое имя «Arrow Lake», Intel 3, 2P+8E+2LPE, 4 Xe, NPU 12 TOPS [A13]. Notebookcheck: «Arrow Lake U series … similar to the Meteor Lake U», ядра Redwood Cove / Crestmont [N5]. Вывод «ловушка» остаётся, но по ARK её не видно |
| 5 | 14‑е поколение Core i в ноутбуках — только HX (refresh 13‑го) | **подтверждено** (для i7) | ARK, серия Core i7 14th gen: из мобильных только 14650HX и 14700HX [A31]. У 14650HX кодовое имя Raptor Lake, Q1'24 [A11]. Core i5/i9 не проверял |
| 6 | Lunar Lake: только распаянная LPDDR5X, до 32 ГБ | **подтверждено** | ARK 258V: «LPDDR5X 8533», Max Memory 32 GB [A16] |
| 7 | Panther Lake X7/X9 и Core Ultra 5 338H — только LPDDR5X | **подтверждено** | ARK: 358H — только LPDDR5X‑9600, 338H — только LPDDR5X‑8533 [A17][A19] |
| 8 | Panther Lake без X (336H, 356H) поддерживает DDR5 SO‑DIMM | **подтверждено** | ARK: LPDDR5X‑8533 и DDR5‑7200, 2 канала, iGPU 4 Xe [A18][A20]. Core Ultra 7 355 (без буквы): 4P+0E+4LPE, DDR5‑6400 [A25] |
| 9 | Wildcat Lake (Core 5 320) — один канал памяти, 2 P‑ядра | **подтверждено** | ARK: Max # of Memory Channels = 1, 2P+0E+4LPE, до 64 ГБ, Intel 18A, Q2'26 [A21] |
| 10 | Twin Lake (Core 3 N355) — один канал, до 16 ГБ | **подтверждено** | ARK: 1 канал, Max Memory 16 GB [A22] |
| 11 | Arc у Meteor Lake и Arrow Lake‑H включается только при ≥16 ГБ в двух каналах; Iris Xe — только в двух каналах | **подтверждено** | Сноска ARK у 155H и 255H: «at least 16GB of system memory in a dual-channel configuration» [A12][A14]. Статья Intel: при одном канале Iris Xe работает как UHD [I2] |
| 12 | HEVC 4:2:2 10 бит аппаратно декодирует любой Intel с 11‑го поколения — в Resolve Studio и Premiere | **подтверждено** | Puget: «11/12/13/14th Gen» и «Core Ultra 2» — Y в обеих программах, у 10‑го поколения — n [P1][P2]. Adobe (07.01.2026): «support HEVC 4:2:2 10-bit decoding on Intel platforms» [AD1]. Даташиты Intel: HEVC Main 4:2:2 10 в декоде у Raptor Lake и Meteor Lake [E1][E3] |
| 13 | H.264 10 бит и H.264 4:2:2 не декодирует ни один Intel до Lunar Lake включительно | **подтверждено** | Даташиты Intel: AVC декод — только «4:2:0 8bit» у Raptor Lake и Meteor Lake [E1][E3]. Media-driver: для AVC только NV12 у всех платформ, включая LNL, PTL и NVL (ред. 22.06.2026) [D2]. Puget: n у всех Intel и Arc [P1][P2] |
| 14 | Кодирование AV1 появилось только с Meteor Lake; у Raptor Lake (в том числе Core 1xxU/2xxH) его нет | **подтверждено** | Даташит Raptor Lake: кодирование AVC, HEVC, VP9, без AV1 [E2]. Meteor Lake: «AV1 Main 4:2:0 8b, 10b» [E4]. Media-driver: у TGLx AV1 — только D [D1] |
| 15 | У MTLx HEVC 4:2:2 — «только D» | **уточнено** | Это верно для Linux‑драйвера [D1]. По даташиту Intel у Meteor Lake есть кодирование «HEVC Main10 422 8b/10b, 4K@60» [E4]. На выбор не влияет |
| 16 | RTX 50 декодирует H.264 10 бит, H.264 4:2:2 и HEVC 4:2:2; RTX 40 — нет | **подтверждено** | Матрица NVIDIA: у RTX 5070 Laptop и старше — YES; у RTX 4060 Laptop — NO по всем трём [V1]. Puget: RTX 50 — Resolve 20+ и Premiere 25.3+; в Premiere H.264 8 бит 4:2:2 не декодируется даже на RTX 50 [P1][P2] |
| 17 | То же у RTX 5050/5060 Laptop | **не проверено** | В матрице этих строк нет. Есть десктопные 5050/5060 и RTX PRO 500/1000 Blackwell Laptop — у них YES [V1] → проверено в браузере 30.09.2026: (п. 5.14) см. строку 241 ([nvidia.com](https://www.nvidia.com/en-us/geforce/laptops/compare/)). |
| 18 | С 19.09.2025 драйверы iGPU 11–14‑го поколений — legacy: раз в квартал, только критические исправления | **подтверждено; уточнено по Core Series 1/2** | Статья Intel 000101986 (пересмотрена 23.10.2025): «critical fixes and security vulnerabilities only», квартальные выпуски, нет Day‑0 для игр. Среди кодовых имён — Raptor Lake, Raptor Lake‑H/U Refresh и Twin Lake [I3], так что Core 1xxU/2xxU/2xxH и N‑серия тоже попадают |
| 19 | Panther Lake: AVC 10 бит заявлен; есть ли 4:2:2 и поддержка в программах | **не проверено** | Intel (через Phoronix): «10-bit AVC encode/decode», XAVC‑H/HS/S [PH1]; про 4:2:2 ни слова. В Linux‑драйвере AVC у PTL только NV12 [D2]. Тестов Puget нет (таблицы от июня 2025) [P1][P2]; у Adobe для Intel упомянут только HEVC 4:2:2 [AD1]; даташит PTL на EDC не нашёл → проверено в браузере 30.09.2026: (п. 5.13) см. строку 29 ([cdrdv2.intel.com](https://cdrdv2.intel.com/v1/dl/getContent/872188?fileName=872188-002.pdf)). |
| 20 | Мобильные 13/14‑е поколения, Arrow Lake и Lunar Lake не затронуты деградацией Vmin | **подтверждено** | Блог Intel от 25.09.2024: «13th and 14th Gen mobile processors … Lunar Lake and Arrow Lake … are unaffected» [I4] |
| 21 | Бесплатный Resolve под Windows: H.264 — только 8 бит (профили ОС), H.265 — 8/10 бит; остальное — в Studio | **подтверждено** | Blackmagic, Resolve 21.1 Supported Formats (сентябрь 2026), Windows: H.264 — «8-bit OS-supported profiles. More profiles and GPU acceleration in Studio», H.265 — «8/10-bit OS-supported profiles» [R1] |
| 22 | Arc B390/B370 требует LPDDR5X ≥7467 | **не проверено** | В ARK (358H) такого условия нет; источник только Википедия [W6] → проверено в браузере 30.09.2026: (п. 5.15) см. строку 84 ([cdrdv2-public.intel.com](https://cdrdv2-public.intel.com/871380/Intel%20Core%20Ultra%20Series%203%20Processors%20-%20Quick%20Reference%20Guide%20v1.pdf)). |

**Новые данные за последние месяцы:**
- Media-driver обновлён 22.06.2026: добавлен NVL, дописан PTL. H.264 по‑прежнему только 8 бит 4:2:0.
- Adobe (07.01.2026) по‑прежнему называет для Intel только HEVC 4:2:2 10 бит.
- Puget не обновлял таблицы декодирования с июня 2025. Lunar Lake и Panther Lake не тестировал.
- Независимых тестов H.264 10 бит / 4:2:2 на Panther Lake в Resolve или Premiere не нашёл.
- Выводы отчёта для кандидатов на Raptor Lake, Meteor Lake и Arrow Lake от этого не меняются.
