# AMD для монтажа 4K: видеокодеки VCN и сравнение с Intel Quick Sync

_Собрано 30.09.2026 локально (компьютер пользователя, IP Германии; закрытые сайты — через Chrome пользователя).
Ссылки — в квадратных скобках, список в конце (раздел 8). «Не проверено» — первоисточник не нашёл или он не открылся; рядом написано, чем пытался.
Данные по Intel — из `../Intel/notes/intel-cpu.md` (ссылки с пометкой «Intel‑заметка»)._

## Коротко

1. **Ни один AMD не декодирует 4:2:2 и H.264 10 бит.** Это касается всех поколений VCN, от Vega до RDNA 4 (RX 9000), и свежих iGPU Radeon 800M.
   - AMD прямо пишет: «All codecs are 4:2:0», H.264 — только 8 бит [G1][G2].
   - Так же в драйвере Mesa 2026 года: H.264 выдаётся только как 8 бит 4:2:0, HEVC — только 4:2:0 8/10 бит [M1][M2].
   - Тесты это подтверждают: Puget (Resolve, Premiere, RX 9070 XT) [P1][P2][P3] и таблица VEGAS Pro 22 [VG1].
2. **Где Intel сильнее по кодекам:** HEVC 4:2:2 10 бит. Его декодирует любой Intel с 11‑го поколения, в Resolve Studio и в Premiere [P1][P2][AD1].
   Это Sony XAVC HS 4:2:2, Canon H.265 10 бит, Fujifilm H.265 4:2:2 [C1][C4][C5]. Ещё HEVC 4:4:4 и 12 бит — в Resolve [P1].
3. **Где одинаково:** H.264 8 бит, HEVC 8/10 бит 4:2:0, VP9, AV1 8/10 бит [G1][P1][P2].
   Это почти все смартфоны, GoPro, DJI и режимы 4:2:0 беззеркалок [C8–C12][C1][C6].
   H.264 4:2:2 10 бит (Sony XAVC S 10 бит, Panasonic MOV 4:2:2) не декодирует **ни AMD, ни Intel** — только NVIDIA RTX 50 [P1][P2][C3][C6].
4. **Где AMD сильнее:**
   - Phoenix/Hawk Point (Ryzen 7x40, 8x40, Ryzen 7 250/260, Ryzen 5 220 [A13]) и новее кодируют AV1 [K3][K1][LV1].
     «Переименованный» Intel Core 5/7 2xxH (Raptor Lake) AV1 не кодирует (Intel‑заметка [D2]).
   - AV1 12 бит декодируют только дискретные RX 7900 и RX 9000 [M1]. Для камер это неважно.
5. **Встроенная графика AMD не всегда сильнее Intel.** Медианы Puget Bench, 30.09.2026:
   - Radeon 890M обходит Arc 140T: +15 % в Resolve 20 и +18 % в Premiere [PB1][PB6].
   - Бюджетные 780M и 860M отстают от Arc 130T/140T: −15…−20 % в общем зачёте, −22…−34 % на эффектах [PB3][PB7][PB8].
   - Meteor Lake (Intel Arc Graphics) 780M/860M обходят на 12–13 % [PB2][PB5][PB9].
6. **HEVC 4:2:2 на AMD декодирует процессор.** В тесте Puget Bench (Resolve 20, экспорт 4K HEVC 100 Мбит/с 4:2:2 10 бит):
   Ryzen AI 9 HX 370 — 41,9 кадра/с, Intel с Arc 140T (аппаратно) — 56,3 кадра/с, то есть AMD медленнее на ~25 % [PB1].
   Для живого таймлайна с несколькими дорожками 200 Мбит/с — **не проверено**.
7. **AMD + NVIDIA RTX 50 закрывает все дыры:** RTX 50 декодирует H.264 и HEVC 4:2:2 (Resolve 20+, Premiere 25.3+) [P1][P2] (Intel‑заметка [V1][V2]).
   RTX 40 и дискретные Radeon RX 7000M этого не умеют [P1].
8. **Ловушки имён влияют и на кодеки:**
   - Ryzen 7x30 (Barcelo, Vega) не декодирует AV1 [K6][K1];
   - Ryzen 7x35/7x36 (Rembrandt‑R) и Ryzen 7x20 (Mendocino) не кодируют AV1 [K5][K1];
   - у HX‑серии (Dragon Range) iGPU — Radeon 610M на VCN 3.1 [K1].
9. **HP отключает аппаратный HEVC и на AMD:** ProBook 465 G11, EliteBook 665 G11, ProBook 4 G1a 16 — по QuickSpecs (`../Intel/notes/hevc-audit.md`).
   Без HEVC у AMD из камерных форматов остаётся только H.264 8 бит. У Intel без HEVC пропадает и HEVC 4:2:2, так что такие модели плохи для обоих (исправлено при проверке: было «для AMD важнее, чем для Intel»).
10. **Тезис «Intel умеет всё то же, что AMD, плюс некоторые форматы аппаратно»:**
    - по **декодированию** для камер — **верно**: Intel добавляет HEVC 4:2:2/4:4:4/12 бит;
    - по **AV1‑кодированию** — неверно для переименованных Raptor Lake;
    - по **силе iGPU** — зависит от модели (пункт 5). Подробно — раздел 6.
    - HEVC 4:2:2 декодирует любой Intel 11+, в том числе Raptor Lake i7‑13620H — лучший Intel из `../Intel/REPORT.md` [P1][P2]. Arrow Lake‑H сверх этого даёт AV1‑кодирование и iGPU 130T/140T (исправлено при проверке: в разделе 6 было «безопаснее Arrow Lake‑H», будто нужен именно он).

---

## 1. Какой VCN в каком чипе

VCN (Video Core Next) — аппаратный видеоблок AMD. Возможности определяет его версия, а не маркетинговое имя процессора [W1].

### 1.1. Ноутбучные и десктопные APU (Linux kernel, таблица amdgpu [K1])

| Имя в прайсе | Кодовое имя | iGPU | VCN |
|---|---|---|---|
| Ryzen 5000, Ryzen 7x30 (5625U, 7530U, 7730U) | Cezanne / Barcelo / Barcelo‑R | Vega, «Radeon Graphics» [A7] | **2.2** |
| Ryzen 6000, Ryzen 7x35 / 7x36 (7535HS, 7735HS) | Rembrandt / Rembrandt‑R | RDNA 2: 660M/680M [A6] | **3.1.1** |
| Ryzen 7x20 (7320U, 7520U) | Mendocino | RDNA 2: 610M [A8] | **3.1.1** |
| Ryzen 7x45HX | Dragon Range | RDNA 2: 610M, кристалл от десктопного Raphael | **3.1.2** |
| Ryzen 7000/9000 для десктопа (AM5) | Raphael / Granite Ridge | RDNA 2, 2 CU | **3.1.2** |
| Ryzen 7x40 (7840HS, 7640HS) | Phoenix | RDNA 3: 780M/760M/740M | **4.0.2** |
| Ryzen 8x40 (8845HS, 8645HS) | Hawk Point | RDNA 3: 780M [A10] | **4.0.2** |
| Ryzen 200: Ryzen 7 250/260, Ryzen 9 270 и др. | Hawk Point (переименование) | 780M у Ryzen 7 250 [A9] | **4.0.2** |
| Ryzen AI 9 HX 370/375, AI 9 365 | Strix Point | RDNA 3.5: 890M / 880M [A1][A2] | **4.0.5** |
| Ryzen AI 7 350, AI 5 340; AI 5 330 | Krackan Point | RDNA 3.5: 860M / 840M / 820M [A3–A5] | **4.0.5** |
| Ryzen AI Max / Max+ 3xx | Strix Halo | RDNA 3.5: 8060S у Max 395 [PB1]; 8050S/8040S — не проверено (страница amd.com не открылась) | **4.0.6** |
| Ryzen AI 400: AI 9 HX 470/475/465, AI 7 450, AI 5 440/435 | Gorgon Point | 890M у HX 470, 860M у AI 7 450 [A11][A12] | **4.0.5** |

Уточнения:
- Кодовые имена сверены с полем «Former Codename» на amd.com [A1–A12].
- Fire Range (Ryzen 9 8945HX, 9955HX3D) в таблице ядра нет. Логично ждать VCN 3.1.2, как у Granite Ridge, но это **не проверено**.
- AMF‑вики ставит Cezanne на «VCN 2.0», ядро — на 2.2 [G1][K1]. Набор кодеков у них одинаковый [K6][G1].
  Так же расходятся по Granite Ridge: в AMF‑вики «VCN 3.0», в ядре 3.1.2 (дописано при проверке). На кодеки для монтажа не влияет: у обеих версий «All codecs are 4:2:0» [G1].
- Ryzen 5 220 — тоже Hawk Point (2 Zen 4 + 4 Zen 4c, Radeon 740M) по amd.com [A13]. Значит, VCN 4.0.2, как у Ryzen 7 250 (вывод по кодовому имени).
- У Strix Halo AV1‑кодировщик работает на обоих блоках VCN. У остальных чипов — только на одном [G1].
- В ядре и Mesa уже есть VCN 5.3.0 для неанонсированного APU (GFX 11.7) [K3][M1]. В ноутбуках на 30.09.2026 — не проверено.

### 1.2. Дискретные Radeon для сравнения [K2][G1]

| Карта | Кристалл | VCN | Блоков VCN |
|---|---|---|---|
| RX 7600M (XT) / 7600S / 7700S | Navi 33 | 4.0.4 | 1 |
| RX 7700 / 7800 / 7900 | Navi 32 / Navi 31 | 4.0.0 | 2 |
| RX 9060 XT | Navi 44 | **5.0.0** | 1 |
| RX 9070 (XT) | Navi 48 | **5.0.0** | 1 по AMF‑вики [G1]; Википедия пишет о двух у старших RDNA 4 [W1] — расхождение, не проверено |

---

## 2. Кодеки по поколениям VCN

### 2.1. Что умеет железо

Источники:
- AMF‑вики AMD, 05.12.2025 [G1]; страница AMD для видеомонтажа [G2];
- таблицы кодеков в драйвере Linux amdgpu [K3–K6];
- возможности декодера в Mesa radeonsi, main‑ветка 2026 года [M1][M2].

Обозначения: D — декодирование, E — кодирование, «—» — нет.

| Кодек | VCN 2.2 (Barcelo) | VCN 3.1 (Rembrandt, Mendocino, 610M) | VCN 4.0.x (Phoenix … Gorgon Point, RX 7000) | VCN 5.0 (RX 9000) | Intel MTLx: Meteor/Arrow Lake (Intel‑заметка [D2]) |
|---|---|---|---|---|---|
| H.264 8 бит 4:2:0 | D/E | D/E | D/E | D/E | D/E |
| **H.264 10 бит** (любой) | — | — | — | — | — (только Panther Lake заявляет) |
| H.264 4:2:2 / 4:4:4 | — | — | — | — | — |
| HEVC 8/10 бит 4:2:0 | D/E | D/E | D/E | D/E | D/E |
| **HEVC 4:2:2** 8/10 бит | — | — | — | — | **D** |
| HEVC 4:4:4 | — | — | — | — | D/E |
| HEVC 12 бит | — | — | — | — | D |
| VP9 8/10 бит | D | D | D | D | D/E |
| AV1 8/10 бит | — | D | **D/E** | D/E (с B‑кадрами) | D/E (у Raptor Lake — только D) |
| AV1 12 бит | — | — | D по AMF [G1]; в Mesa — только у RX 7900 (VCN 4.0.0) [M1]; у 780M (VCN 4.0.2) в VA‑API нет [LV1] | D | — |
| VVC (H.266) | — | — | — | — | — (есть у Lunar/Panther Lake) |

Пределы разрешения:
- H.264: декод и кодирование до 4096×4096, уровень 5.2 [K3–K6][M1];
- HEVC и VP9: до 8192×4352 начиная с VCN 2 [K3–K6];
- HEVC‑кодирование на VCN 2.x — до 4K [G1].

**Два вопроса задания, по пунктам:**
- **Декодирует ли AMD H.264 10 бит?** Нет, ни одно поколение.
  - AMD: «AVC … 8b: 4K» для VCN 2.0–5.0 [G1];
  - таблица AMD: H.264 — только 4:2:0 8 бит [G2];
  - Mesa: у H.264 только формат NV12, то есть 8 бит 4:2:0; профилей High 10 и High 4:2:2 в списке нет [M1][M2];
  - живая проверка на Radeon 780M (Hawk Point, Mesa 26.2.3): H.264 Baseline/Main/High — только YUV420 8 бит; HEVC Main/Main10 — только 4:2:0 [LV1];
  - Puget: у Radeon и Ryzen H.264 10 бит — «нет» [P1][P2].
- **Нет ли HEVC 4:2:2 в RDNA 3.5 или RDNA 4?** Нет. Свежие данные 2025–2026:
  - AMF‑вики, 05.12.2025: «All codecs are 4:2:0» [G1];
  - Mesa main, 2026: HEVC‑декодер отдаёт только NV12/P010, поддержан профиль Main 10, профилей RExt (4:2:2/4:4:4) нет [M1][M2];
  - Puget о RX 9070 XT, 31.03.2025: в 4:2:2 10 бит карта «half as fast due to a lack of acceleration support» [P3];
  - VEGAS Pro 22: у AMF 4:2:2 — ✗ во всех строках [VG1];
  - Adobe, 07.01.2026: HEVC 4:2:2 10 бит упомянут только для Intel [AD1].

**Кодирование — что менялось:**
- VCN 3.0 вернул B‑кадры в H.264. VCN 4.0 добавил кодирование AV1 [W1].
- VCN 5.0 (RDNA 4), по заявлению AMD:
  - качество H.264 +25 % в режиме low‑latency (стриминг), HEVC +11 % (исправлено при проверке: в [T2] «+25 %» относится к «H.264 low-latency encode quality»);
  - B‑кадры в AV1 [T2].

  В Mesa у VCN 5.0 действительно появились двунаправленные ссылки в AV1 и преобразование 8×8 в H.264 [M1].
- Все ноутбучные APU, включая Radeon 800M, — это VCN 4.0.x, а не 5.0 [K1]. Улучшения RDNA 4 им не достались (вывод по версии блока).

### 2.2. Что реально работает в программах (Windows)

**DaVinci Resolve Studio** — тест Puget Systems, обновлён 17.06.2025 [P1]:

| Формат | Ryzen 7000/9000 iGPU (VCN 3.1.2) | Radeon 5000–7000 | Intel 11–14 / Core Ultra 2 | RTX 20/30/40 | RTX 50 (Resolve 20+) |
|---|---|---|---|---|---|
| H.264 8 бит 4:2:0 | да | да | да | да | да |
| H.264 10 бит 4:2:0 | нет | нет | нет | нет | да |
| H.264 8/10 бит 4:2:2 | нет | нет | нет | нет | да |
| HEVC 8/10 бит 4:2:0 | да | да | да | да | да |
| **HEVC 8/10 бит 4:2:2** | **нет** | **нет** | **да** | нет | да |
| HEVC 4:4:4 (8/10 бит) | нет | нет | да | да | да |
| HEVC 12 бит 4:2:0 | нет | нет | да | да | да |
| HEVC 12 бит 4:2:2 | нет | нет | да | нет | да |

**Adobe Premiere Pro** — тест Puget Systems, обновлён 12.06.2025 [P2]:

| Формат | Ryzen 7000/9000 iGPU | Radeon 5000–7000 | Intel 11–14 / Core Ultra 2 | RTX 20/30/40 | RTX 50 (Premiere 25.3+) |
|---|---|---|---|---|---|
| H.264 8 бит 4:2:0 | да | да | да | да | да |
| H.264 10 бит 4:2:0 и 4:2:2 | нет | нет | нет | нет | да |
| HEVC 8/10 бит 4:2:0 | да | да | да | да | да |
| **HEVC 10 бит 4:2:2** | **нет** | **нет** | **да** | нет | да |
| HEVC 8 бит 4:2:2, 4:4:4, 12 бит | нет | нет | нет | нет | нет |

Уточнения:
- Ноутбучные Radeon 780M/800M Puget отдельно не тестировал.
  Набор кодеков у них тот же, «все 4:2:0» [G1], поэтому ждём тех же «да/нет» — это вывод, а не отдельный тест.
- **RX 9070 XT (RDNA 4), Puget, 31.03.2025 [P3]:**
  - в Resolve в 4:2:2 10 бит карта «half as fast due to a lack of acceleration support»;
  - в остальных H.264/HEVC она быстрее RTX 5080 на кодировании и примерно на 20 % медленнее на обработке.
- **Adobe [AD1][AD3]:**
  - на странице о кодеках, 07.01.2026, аппаратный HEVC 4:2:2 10 бит назван только для Intel [AD1];
  - в рекомендуемых требованиях: «Intel 11th Gen or newer CPU with Quick Sync – or AMD Ryzen 3000 Series», а для 4K — «32 GB or more» памяти [AD3];
  - аппаратное кодирование в Premiere — H.264 8 бит и HEVC 4:2:0 8/10 бит [AD4].
- **Resolve (бесплатный) под Windows:** декодирует только профили, которые поддерживает сама ОС (H.264 8 бит, H.265 8/10 бит). Дальше — «More profiles and GPU acceleration in Studio» [R1].
  То есть GPU‑ускорение декодирования на AMD, как и на Intel, — только в Studio.
  Использует ли встроенный декодер Windows в бесплатной версии DXVA, Blackmagic не пишет — **не проверено** (уточнено при проверке).
- **Выбор декодера в Resolve Studio:** в Preferences → Decode Options можно включить Intel, NVIDIA или AMD по отдельности [P4].
  Это важно для связки AMD + RTX 50.
- **VEGAS Pro 22 [VG1]:**
  - AMF декодирует H.264 только 8 бит 4:2:0 до 4K и HEVC 4:2:0 8/10 бит до 8K;
  - HEVC 4:2:2 декодирует только Intel 11+ («Intel HW»);
  - NVDEC в таблице без 4:2:2 — таблица, похоже, написана до RTX 50 (не проверено).
- **HandBrake:** VCN используется только для кодирования, «does NOT support the hardware decoder» — декодирует процессор [HB1].
- **CapCut, PowerDirector:** что они декодируют на AMD — **не проверено**.
  Спецификация PowerDirector деталей не даёт [PD1], страница требований CapCut через curl пустая.

### 2.3. Качество кодирования: AMF против Quick Sync и NVENC

- **Tom's Hardware, 10.03.2023, ffmpeg, VMAF [T1]:**
  - по качеству лидирует NVIDIA, Intel Arc «right behind». Это дискретные Arc A; iGPU Intel в тесте — только UHD 770, iGPU Meteor/Arrow Lake не тестировали (уточнено при проверке);
  - AMD «continue to lag behind»: RDNA 3 — лучшее у AMD, но на уровне GTX 10‑й серии;
  - у RDNA 2 и RDNA 3 одинаковое качество H.264.
- **RDNA 4 (VCN 5.0):** AMD заявляет заметный рост качества (+25 % H.264 low‑latency, +11 % HEVC) [T2].
  Независимого VMAF‑теста RDNA 4 против Intel/NVIDIA не нашёл — **не проверено**.
- **Для ноутбучных APU** (VCN 4.0.x) ближе данные RDNA 3 из [T1]. Именно iGPU Radeon 800M никто не тестировал — **не проверено**.
- Тесты [T1] шли на низких битрейтах (1080p на 3–8 Мбит/с, 4K на 8–16 Мбит/с) — это сценарий стриминга.
  Как отличаются кодировщики на монтажном экспорте 4K 50–100 Мбит/с — **не проверено**.

### 2.4. Эффекты и цветокоррекция: iGPU AMD против Intel

Источник — публичная база Puget Bench, медианы по GPU, сняты 30.09.2026 [PB1–PB9]. В выборку попали только системы без дискретной карты.

**Resolve Studio 20.0–20.3, Puget Bench 1.2:**

| Показатель | Radeon 890M | Arc 140T | Разница |
|---|---|---|---|
| Общий балл (Standard) | 2872 | 2489 | AMD +15 % |
| GPU Effects | 12,1 | 10,7 | AMD +13 % |
| Color Node ×30, кадр/с | 10,4 | 8,8 | AMD +18 % |
| AI (Extended) | 13,7 | 17,3 | **Intel +26 %** |
| Кодирование HEVC 10 бит UHD, кадр/с | 70,9 | 52,4 | AMD +35 % |
| **Обработка 4K HEVC 4:2:2 10 бит, кадр/с** | **41,9** | **56,3** | **Intel +34 %** |

Источник — [PB1]. Radeon 860M против Intel Arc Graphics (Meteor Lake): общий балл 2402 против 2151 (+12 %), GPU Effects 10,4 против 10,0 [PB2].

**Resolve Studio 18.6–19.1, Puget Bench 1.0–1.2:**

| Показатель | 780M | 890M | Arc 140T | Intel Arc Graphics |
|---|---|---|---|---|
| Общий балл (Standard) | 2245 | 2500 | 2701 | 1990 |
| GPU Effects | 9,7 | 11,5 | 12,4 | 9,6 |
| 4K HEVC 4:2:2 10 бит, кадр/с | 50,0 | 48,3 | 55,7 | 48,7 |

Источники — [PB3][PB4][PB5].

**Premiere Pro 25.1–25.2, Puget Bench 1.x:**

| Показатель | 890M | Arc 140T | 780M | 860M | Arc 130T | Intel Arc Graphics |
|---|---|---|---|---|---|---|
| Общий балл (Standard) | 4326 | 3661 | 3038 | 2882 | 3591 | 2694 |
| GPU Effects | 32,6 | 13,9 | 9,4 | 10,2 | 14,3 | 10,9 |
| Lumetri ×40, кадр/с | 17,8 | 18,2 | 11,0 | 11,9 | 18,9 | 13,7 |

Источники — [PB6–PB9].

Выводы:
- **890M (Strix Point) ≥ Arc 140T:** +15 % в Resolve 20 и +18 % в Premiere. В Resolve 19 — −7 %.
- **780M/860M < Arc 130T/140T:** −15…−20 % в общем зачёте, −22…−34 % на эффектах. Lumetri ×40 у Arc 130T быстрее на 58–71 % (18,9 против 11,9 и 11,0 кадра/с) [PB7][PB8].
- **780M/860M > Meteor Lake (Intel Arc Graphics):** +12–13 % в общем зачёте. На эффектах поровну в Resolve (9,7 против 9,6; 10,4 против 10,0), в Premiere Intel чуть впереди (10,9 против 9,4) [PB2][PB5][PB9].
- **Оговорки:**
  - это публичные загрузки: разные ноутбуки, лимиты мощности и память;
  - у 890M в выборке много LPDDR5X‑7500/8000 (распайка), у 140T часто 2×16 DDR5‑5600 [PB1];
  - на SO‑DIMM DDR5‑5600 результат 890M, скорее всего, ниже — **не проверено**;
  - выборки по 18–70 результатов;
  - Notebookcheck PugetBench не публикует; других цифр по iGPU в Resolve/Premiere не нашёл.

---

## 3. Камеры: что пишут и что декодирует AMD

### 3.1. Форматы популярных камер (по данным производителей)

| Камера | Формат | Кодек, бит, цвет | Источник |
|---|---|---|---|
| iPhone 17 Pro | HEVC, H.264, ProRes, ProRes RAW; 4K Dolby Vision; Apple Log 2 | Dolby Vision — 10 бит; субдискретизацию Apple не пишет — не проверено | [C8] |
| Android | HEVC / H.264 | не проверено (зависит от модели), смотрите MediaInfo | — |
| GoPro HERO11/12 | 10 бит | «GoPro 10‑Bit Video uses 4:2:0 color sampling» | [C9] |
| DJI Mini 4 Pro / Mini 5 Pro | H.264/H.265 | обычный режим — 8 бит 4:2:0; HLG/D‑Log M — 10 бит 4:2:0 (H.265) | [C10][C11] |
| DJI Mavic 4 Pro | H.264 Standard, H.265, **H.264 ALL‑I** (Creator Combo) | H.264 8 бит 4:2:0; H.265 10 бит 4:2:0; **H.264 ALL‑I 10 бит 4:2:2** | [C12] |
| DJI Osmo Action 5 Pro / Pocket 3 | MP4 (HEVC) / MP4 (H.264/HEVC) | битность и цвет на странице не указаны — не проверено | [C13][C14] |
| Sony A7 IV: XAVC S 4K | H.264, Long GOP | **8 бит — всегда 4:2:0; 10 бит — всегда 4:2:2** (например, 200M 4:2:2 10bit) | [C1] |
| Sony A7 IV: XAVC HS 4K | HEVC, Long GOP | 4:2:0 10 бит **или** 4:2:2 10 бит (200M/100M/50M) | [C1][C2] |
| Sony A7 IV: XAVC S‑I 4K | H.264 Intra | только 4:2:2 10 бит, 240–600 Мбит/с | [C3] |
| Canon EOS R6 Mark II | MP4 H.264 / MP4 H.265 | H.264 — 4:2:0 8 бит; **H.265 (Canon Log / HDR PQ) — 4:2:2 10 бит** | [C4] |
| Fujifilm X‑T5, X‑S20 | MOV/MP4 | H.265 4:2:2 10 бит **или** 4:2:0 10 бит (Long GOP и All‑Intra); H.264 — 4:2:0 8 бит | [C5][C5b] |
| Panasonic Lumix S5II | MOV / MP4 | MOV: **H.264 4:2:2 10 бит** (4K до 200 Мбит/с) или H.265 4:2:0 10 бит; MP4: H.265 4:2:0 10 бит, H.264 4:2:0 8 бит | [C6] |
| Nikon Z6III | H.265 8/10 бит, H.264 8 бит, ProRes 422 HQ 10 бит, ProRes RAW, N‑RAW | субдискретизацию H.265 10 бит Nikon на странице не указывает — не проверено | [C7] |

Уточнения:
- В режиме по умолчанию A7 IV пишет XAVC S 4K 4:2:0 8 бит [C3]. Sony прямо предупреждает: у 4:2:2 10 бит «The playback environment … is limited» [C1].
- Другие модели Sony, Canon, Nikon здесь не проверены. Схема может отличаться — смотрите Help Guide модели и MediaInfo.

### 3.2. Файл камеры → кто декодирует аппаратно (Resolve Studio / Premiere)

| Файл | AMD iGPU (любой Ryzen) | Intel iGPU 11+ / Core Ultra | RTX 50 | RTX 40 |
|---|---|---|---|---|
| H.264 8 бит 4:2:0 (XAVC S 8 бит, Canon H.264, Fuji H.264, DJI/GoPro обычный, iPhone «Most Compatible») | да | да | да | да |
| HEVC 8/10 бит 4:2:0 (iPhone HDR*, GoPro 10 бит, DJI D‑Log M, XAVC HS 4:2:0, Fuji и Panasonic H.265 4:2:0) | да | да | да | да |
| **HEVC 10 бит 4:2:2** (XAVC HS 4:2:2, Canon H.265 10 бит, Fuji H.265 4:2:2) | **нет** | **да** | да | нет |
| HEVC 8 бит 4:2:2 | нет | Resolve — да, Premiere — нет | Resolve — да, Premiere — нет | нет |
| HEVC 4:4:4, 12 бит | нет | Resolve — да | Resolve — да | Resolve — 4:4:4 да, 12 бит 4:2:2 нет |
| **H.264 10 бит 4:2:2 Long GOP** (XAVC S 10 бит, Panasonic MOV 4:2:2) | нет | **нет** | **да** | нет |
| H.264 10 бит 4:2:2 Intra (XAVC S‑I, Mavic 4 Pro ALL‑I) | нет | нет | не проверено: Puget не уточняет, Intra или Long GOP | нет |
| ProRes 422 HQ / ProRes RAW / N‑RAW | нет аппаратного ProRes ни у кого из них (в таблицах AMD/Intel/NVIDIA ProRes нет) — декодирует процессор | | | |

\* 4:2:0 у iPhone — предположение, не проверено (см. 3.1).

Источники таблицы: Puget [P1][P2], AMD [G1], камеры [C1–C12]; NVIDIA — Intel‑заметка [V1][V2].

**Где AMD проигрывает Intel:**
- HEVC 4:2:2 10 бит — главный случай: Sony XAVC HS 4:2:2, Canon 10 бит, Fujifilm 4:2:2;
- HEVC 4:4:4 и 12 бит — в Resolve.

**Где равны:**
- всё 4:2:0: смартфоны, GoPro, DJI, 8‑битные режимы беззеркалок;
- H.264 10 бит 4:2:2 — его не умеют оба; это Sony XAVC S 10 бит, XAVC S‑I, Panasonic MOV 4:2:2, DJI ALL‑I;
- ProRes — аппаратно не декодирует ни AMD, ни Intel, ни NVIDIA.

**Важно для «камера неизвестна»:**
- у Canon EOS R6 Mark II 10 бит = HEVC 4:2:2: «YCbCr4:2:0 8-bit or YCbCr4:2:2 10bit», H.265 — для Canon Log / HDR PQ [C4]. С этой камерой AMD без RTX 50 хуже Intel.
  Другие модели Canon — **не проверено** (исправлено при проверке: было «у Canon 10 бит = 4:2:2 … всегда», а проверена одна камера);
- у Sony и Fujifilm можно выбрать 4:2:0 10 бит (HEVC), и тогда AMD равен Intel [C1][C5];
- у Panasonic S5II 10‑битный HEVC — только 4:2:0, и AMD его декодирует [C6].

---

## 4. Обходные пути для AMD

1. **Прокси.**
   - Premiere: Proxy → Create Proxies. По умолчанию — половина разрешения и ProRes Proxy [AD5].
   - Panasonic S5II пишет прокси прямо в камере (Proxy Rec, прошивка 3.0+) [C6].
   - В Resolve есть свои прокси и оптимизированные медиа. Документацию Blackmagic по ним не открывал — не проверено.
2. **Перекодировать в монтажный кодек.** Resolve 21.1 под Windows кодирует ProRes 422/HQ/LT/Proxy/4444 и DNxHR [R1].
   Интра‑кодеки процессор декодирует легко. В Puget Bench обработка 4K ProRes 422 — около 100 кадров/с и на 890M, и на Arc 140T [PB1].
3. **Программное декодирование процессором.**
   - Puget Bench, Resolve 20, экспорт 4K HEVC 100 Мбит/с 4:2:2 10 бит [PB1][PB2]:
     - Ryzen AI 9 HX 370 (12 ядер: 4 Zen 5 + 8 Zen 5c [A1]) — 41,9 кадра/с;
     - Ryzen AI 7 350 (8 ядер [A3]) — 43,4 кадра/с;
     - Intel с аппаратным декодом: Arc 140T — 56,3, «Intel Arc Graphics» — 41,7 кадра/с.
   - В Resolve 19 [PB3][PB5]: системы с 780M (Phoenix/Hawk Point, например 8‑ядерный Ryzen 7 8845HS [A10]) — 50,0 кадра/с; Arc 140T — 55,7.
   - **Оговорка.** Это экспорт одной дорожки при 100 Мбит/с. В тесте упор идёт и в GPU, поэтому он плохо отделяет декодирование.
     Пример: Meteor Lake с аппаратным декодом (41,7) не быстрее 860M, у которого декодирует процессор (43,4) [PB2] (дописано при проверке).
     Сколько кадров/с 8‑ядерный Zen 4/Zen 5 даёт при воспроизведении таймлайна 4K60 200 Мбит/с 4:2:2 — **не проверено** (отдельного теста не нашёл).
   - Отзыв владельца Framework 16 (Ryzen 7040): Sony 4K 10 бит 4:2:2 в Resolve монтируется «just fine», но вентилятор «really cranked» [F1].
     Это единичный отзыв, не тест.
4. **Снимать в 4:2:0.** Sony XAVC HS 4:2:0 10 бит, Fujifilm H.265 4:2:0 10 бит, Panasonic H.265 4:2:0 10 бит — всё это AMD декодирует аппаратно [C1][C5][C6][P1].
5. **AMD + NVIDIA RTX 50.**
   - Blackwell декодирует H.264 4:2:0 10 бит, H.264 4:2:2 8/10 бит и HEVC 4:2:2 (Intel‑заметка [V1][V2]).
   - В программах: Resolve Studio 20+ и Premiere 25.3+ [P1][P2]. В Resolve нужно включить декодер NVIDIA в Decode Options [P4].
   - Есть ли RTX 5050/5060 Laptop в матрице NVIDIA — не проверено (см. Intel‑заметку).
   - RTX 40 4:2:2 не декодирует [P1]. Дискретные Radeon RX 7000M тоже [P1][G1]. Для 4:2:2 годится только RTX 50.
   - Такие связки существуют: в базе Puget есть, например, «RTX 5060 Laptop GPU & AMD Radeon 780M» [PB1] (список GPU на странице).
     Цены — в `notes/market-amd.md`.

---

## 5. Как проверить ноутбук и файлы

- **Файл камеры:** MediaInfo в подробном виде (Tree). Смотрите Format profile, Chroma subsampling и Bit depth [P1].
  4:2:0 — AMD подходит. HEVC 4:2:2 — Intel или RTX 50. H.264 4:2:2 10 бит — только RTX 50.
- **Не отключён ли HEVC** (HP, Dell, Acer): DXVA Checker, профиль HEVC_VLD_Main10. Подробно — `../Intel/notes/hevc-audit.md`.
  Это важно для обоих: у AMD без HEVC из камерных форматов остаётся только H.264 8 бит, у Intel пропадает и главное преимущество — HEVC 4:2:2 (исправлено при проверке: было «для AMD важнее»).
- **Версия VCN** — по кодовому имени процессора, раздел 1.1 [K1].

---

## 6. Итог: «Intel умеет всё то же, что AMD, плюс некоторые форматы аппаратно»

| Пункт | Intel | AMD | Вывод |
|---|---|---|---|
| Декод H.264 8 бит, HEVC 4:2:0 8/10 бит, VP9, AV1 8/10 бит | да (Intel‑заметка [D2]) [P1] | да [G1][P1] | **одинаково** |
| Декод HEVC 4:2:2 10 бит (Sony HS 4:2:2, Canon, Fuji) | да, 11‑е поколение и новее [P1][P2] | нет [G1][P3] | **Intel лучше** — тезис верен |
| HEVC 4:4:4, 12 бит | да (Resolve) [P1] | нет | Intel лучше |
| H.264 10 бит и 4:2:2 | нет (до Panther Lake) | нет | одинаково плохо: нужна RTX 50 |
| Кодирование AV1 | Meteor/Arrow Lake — да; Raptor Lake и Core 5/7 2xxH — **нет** (Intel‑заметка [D2]) | Phoenix/Hawk Point и новее — да [K3] | AMD лучше старых Intel; с Arrow Lake — поровну |
| Кодирование VP9, HEVC 4:2:2/4:4:4 | да (Intel‑заметка [D2]) | нет [G1] | Intel лучше (для монтажа неважно) |
| Качество аппаратного кодирования | дискретный Arc близок к NVIDIA [T1]; iGPU Meteor/Arrow Lake не тестировали | дискретные RDNA 3 отстают [T1], APU не тестировали (уточнено при проверке); RDNA 4 — заявлен рост [T2] | Intel лучше |
| AV1 12 бит, декод | нет (Intel‑заметка [D2]) | RX 7900 и RX 9000 [M1] | AMD, но для камер неважно |
| iGPU: эффекты и цветокор | Arc 130T/140T | 890M сильнее 140T; 780M/860M слабее 130T/140T; сильнее Meteor Lake [PB1–PB9] | **зависит от модели** |
| Linux: VA‑API | есть (Intel‑заметка [D1]) | есть, без 4:2:2 [M2] | одинаково; Resolve под Linux не использует ни тот, ни другой [R1] |

**Ответ пользователю:**
- **По декодированию** тезис **верен**. Intel декодирует всё, что декодирует AMD, плюс HEVC 4:2:2 и 4:4:4/12 бит. Для камер из этого важен HEVC 4:2:2 10 бит.
- **Неверно, что «плюс» только у Intel:**
  - AMD Hawk Point и новее кодирует AV1, а переименованные Intel Core 5/7 2xxH — нет;
  - iGPU 890M быстрее Arc 140T в Resolve 20 и Premiere.
- **Где у AMD на деле преимущества нет:**
  - бюджетные 780M/860M уступают Arc 130T/140T;
  - H.264 4:2:2 10 бит не умеет ни одна сторона.
- **Для «камера неизвестна» без дискретки** безопаснее Intel. По декодированию хватает любого Intel 11+, в том числе Raptor Lake i7‑13620H из `../Intel/REPORT.md` [P1][P2].
  Arrow Lake‑H сверх этого даёт AV1‑кодирование и iGPU 130T/140T (исправлено при проверке: было «Intel Arrow Lake‑H — более безопасный выбор», будто для HEVC 4:2:2 нужен именно он).
- **AMD равен Intel,** если камера пишет 4:2:0 или в ноутбуке есть RTX 50.

---

## 7. Linux (пользователь на Arch)

- **VA‑API на AMD** — драйвер radeonsi в Mesa [L1]. Что декодирует, по коду Mesa main [M2][M1]:
  - H.264 — профили Baseline/Main/High, только 8 бит 4:2:0;
  - HEVC — Main и Main 10;
  - VP9 — профили 0 и 2;
  - AV1 — Main; Profile 2 (12 бит) — только VCN 4.0.0 и 5.x.
  - 4:2:2 и H.264 10 бит на AMD под Linux декодирует процессор (ffmpeg), как и под Windows.
  - Проверено вживую на компьютере пользователя (Radeon 780M, Hawk Point, radeonsi, Mesa 26.2.3, ядро 7.2.6), 30.09.2026 [LV1]:
    - H.264 ConstrainedBaseline/Main/High — декод и кодирование, только YUV420 8 бит;
    - HEVC Main/Main10 — декод и кодирование, YUV420 8/10 бит;
    - VP9 Profile 0/2 — только декод; AV1 Profile 0 — декод и кодирование; AV1 Profile 2 (12 бит) нет.
  - Исходники Mesa на gitlab.freedesktop.org при проверке не открылись (Anubis через curl, «Verification Required» в Chrome). Выводы [M1][M2] подтверждены только этим живым запросом и только для VCN 4.0.2.
- **Пакеты в Arch:**
  - `mesa` 26.2.3 собран с `-D video-codecs=all`, так что H.264/HEVC в VA‑API включены [M3];
  - VDPAU из radeonsi удалён в Mesa 25.3 — нужен VA‑API или прослойка [L1];
  - Vulkan Video в `vulkan-radeon` включён по умолчанию для VCN 2+ с Mesa 25 [L1];
  - AMF для RDNA 3 и новее — пакет AUR `amf-amdgpu` на открытом стеке [L1][HB1].
- **DaVinci Resolve под Linux на AMD:**
  - GPU‑расчёты идут через OpenCL: ROCm или Mesa Rusticl (`RUSTICL_ENABLE=radeonsi`) [L2];
  - H.264/H.265 — только в Studio, и GPU‑ускорение в документе Blackmagic указано только для NVIDIA [R1]. На AMD декодирует процессор;
  - AAC‑звук Resolve под Linux не читает ни во Free, ни в Studio [L2];
  - бесплатный Resolve H.264/H.265 не декодирует вообще [L2][R1].
- Поддерживает ли ROCm конкретные iGPU (780M, 890M) — **не проверено**. Страница требований ROCm отсылает к отдельному документу «ROCm on Radeon and Ryzen» [L3].

---

## 8. Источники

**AMD, драйверы, спецификации**
- [G1] AMD GPUOpen, AMF Wiki «GPU and APU HW Features and Support» (правка 05.12.2025): <https://github.com/GPUOpen-LibrariesAndSDKs/AMF/wiki/GPU%20and%20APU%20HW%20Features%20and%20Support>
- [G2] AMD, Video Production Advanced by AMD Radeon Graphics (таблица «Supported Video Formats»): <https://www.amd.com/en/products/graphics/radeon-for-creators/video-editing.html>
- [K1] Linux kernel, amdgpu: таблица APU (версии VCN): <https://raw.githubusercontent.com/torvalds/linux/master/Documentation/gpu/amdgpu/apu-asic-info-table.csv> (в документации: <https://docs.kernel.org/gpu/amdgpu/amd-hardware-list-info.html>)
- [K2] Linux kernel, amdgpu: таблица дискретных GPU: <https://raw.githubusercontent.com/torvalds/linux/master/Documentation/gpu/amdgpu/dgpu-asic-info-table.csv>
- [K3] Linux kernel, soc21.c — кодеки VCN 4.0.x и 5.3 (ветка master, 7.3‑rc5): <https://github.com/torvalds/linux/blob/master/drivers/gpu/drm/amd/amdgpu/soc21.c>
- [K4] Linux kernel, soc24.c — кодеки VCN 5.0: <https://github.com/torvalds/linux/blob/master/drivers/gpu/drm/amd/amdgpu/soc24.c>
- [K5] Linux kernel, nv.c — кодеки VCN 2.x/3.x (Navi, Rembrandt): <https://github.com/torvalds/linux/blob/master/drivers/gpu/drm/amd/amdgpu/nv.c>
- [K6] Linux kernel, soc15.c — кодеки Raven/Renoir (VCN 1.0/2.2): <https://github.com/torvalds/linux/blob/master/drivers/gpu/drm/amd/amdgpu/soc15.c>
- [M1] Mesa, src/amd/common/ac_video.c (возможности VCN: форматы, профили): <https://gitlab.freedesktop.org/mesa/mesa/-/blob/main/src/amd/common/ac_video.c>
- [M2] Mesa, radeonsi/mm/si_mm_screen.c (список профилей декодирования и кодирования): <https://gitlab.freedesktop.org/mesa/mesa/-/blob/main/src/gallium/drivers/radeonsi/mm/si_mm_screen.c>
- [M3] Arch Linux, PKGBUILD пакета mesa 26.2.3: <https://gitlab.archlinux.org/archlinux/packaging/packages/mesa/-/blob/main/PKGBUILD>
- [W1] Wikipedia, Video Core Next (навигация): <https://en.wikipedia.org/wiki/Video_Core_Next>

**amd.com, страницы процессоров** (поля Former Codename, Graphics Model, # of CPU Cores)
- [A1] Ryzen AI 9 HX 370: <https://www.amd.com/en/products/processors/laptop/ryzen/ai-300-series/amd-ryzen-ai-9-hx-370.html>
- [A2] Ryzen AI 9 365: <https://www.amd.com/en/products/processors/laptop/ryzen/ai-300-series/amd-ryzen-ai-9-365.html>
- [A3] Ryzen AI 7 350: <https://www.amd.com/en/products/processors/laptop/ryzen/ai-300-series/amd-ryzen-ai-7-350.html>
- [A4] Ryzen AI 5 340: <https://www.amd.com/en/products/processors/laptop/ryzen/ai-300-series/amd-ryzen-ai-5-340.html>
- [A5] Ryzen AI 5 330: <https://www.amd.com/en/products/processors/laptop/ryzen/ai-300-series/amd-ryzen-ai-5-330.html>
- [A6] Ryzen 5 7535HS: <https://www.amd.com/en/products/processors/laptop/ryzen/7000-series/amd-ryzen-5-7535hs.html>
- [A7] Ryzen 5 7530U: <https://www.amd.com/en/products/processors/laptop/ryzen/7000-series/amd-ryzen-5-7530u.html>
- [A8] Ryzen 3 7320U: <https://www.amd.com/en/products/processors/laptop/ryzen/7000-series/amd-ryzen-3-7320u.html>
- [A9] Ryzen 7 250: <https://www.amd.com/en/products/processors/laptop/ryzen/200-series/amd-ryzen-7-250.html>
- [A10] Ryzen 7 8845HS: <https://www.amd.com/en/products/processors/laptop/ryzen/8000-series/amd-ryzen-7-8845hs.html>
- [A11] Ryzen AI 9 HX 470: <https://www.amd.com/en/products/processors/laptop/ryzen/ai-400-series/amd-ryzen-ai-9-hx-470.html>
- [A12] Ryzen AI 7 450: <https://www.amd.com/en/products/processors/laptop/ryzen/ai-400-series/amd-ryzen-ai-7-450.html>
- [A13] Ryzen 5 220 (открыто в Chrome при проверке): <https://www.amd.com/en/products/processors/laptop/ryzen/200-series/amd-ryzen-5-220.html>

**Puget Systems**
- [P1] What H.264 and H.265 Hardware Decoding is Supported in DaVinci Resolve Studio (обн. 17.06.2025): <https://www.pugetsystems.com/labs/articles/what-h-264-and-h-265-hardware-decoding-is-supported-in-davinci-resolve-studio-2122/>
- [P2] То же для Premiere Pro (обн. 12.06.2025): <https://www.pugetsystems.com/labs/articles/what-h-264-and-h-265-hardware-decoding-is-supported-in-premiere-pro-2120/>
- [P3] AMD Radeon RX 9070 XT Content Creation Review (31.03.2025): <https://www.pugetsystems.com/labs/articles/amd-radeon-rx-9070-xt-content-creation-review/>
- [P4] Is Your Footage Hardware Accelerated in DaVinci Resolve? (10.02.2025): <https://www.pugetsystems.com/blog/2025/02/10/is-your-footage-hardware-accelerated-in-davinci-resolve/>

**Puget Bench, публичная база, медианы по GPU** (сняты 30.09.2026)
- [PB1] Resolve 20.0–20.3 (PB 1.2), 890M vs Arc 140T: <https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/27/GPU/AMD%20Radeon%20890M%20Graphics/Intel%20Arc%20140T%20GPU%20%2816GB%29/>
- [PB2] Resolve 20.0–20.3, 860M vs Intel Arc Graphics: <https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/27/GPU/AMD%20Radeon%20860M%20Graphics/Intel%20Arc%20Graphics/>
- [PB3] Resolve 18.6–19.1, 780M vs Arc 140T: <https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/17/GPU/AMD%20Radeon%20780M%20Graphics/Intel%20Arc%20140T%20GPU%20%2816GB%29/>
- [PB4] Resolve 18.6–19.1, 890M vs Arc 140T: <https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/17/GPU/AMD%20Radeon%20890M%20Graphics/Intel%20Arc%20140T%20GPU%20%2816GB%29/>
- [PB5] Resolve 18.6–19.1, 780M vs Intel Arc Graphics: <https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/17/GPU/AMD%20Radeon%20780M%20Graphics/Intel%20Arc%20Graphics/>
- [PB6] Premiere 25.1–25.2, 890M vs Arc 140T: <https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/23/GPU/AMD%20Radeon%20890M%20Graphics/Intel%20Arc%20140T%20GPU%20%2816GB%29/>
- [PB7] Premiere 25.1–25.2, 780M vs Arc 130T: <https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/23/GPU/AMD%20Radeon%20780M%20Graphics/Intel%20Arc%20130T%20GPU%20%2816GB%29/>
- [PB8] Premiere 25.1–25.2, 860M vs Arc 130T: <https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/23/GPU/AMD%20Radeon%20860M%20Graphics/Intel%20Arc%20130T%20GPU%20%2816GB%29/>
- [PB9] Premiere 25.1–25.2, 780M vs Intel Arc Graphics: <https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/23/GPU/AMD%20Radeon%20780M%20Graphics/Intel%20Arc%20Graphics/>

**Программы**
- [AD1] Adobe, Supported codecs and drivers for hardware‑accelerated decoding (07.01.2026, открыто в Chrome): <https://helpx.adobe.com/premiere/desktop/get-started/technical-requirements/supported-codecs-and-drivers-for-hardware-accelerated-decoding.html>
- [AD2] Adobe, Hardware‑accelerated decoding and encoding (07.01.2026): <https://helpx.adobe.com/premiere/desktop/get-started/technical-requirements/hardware-accelerated-decoding-and-encoding.html>
- [AD3] Adobe, Premiere system requirements (вкладка Windows): <https://helpx.adobe.com/premiere/desktop/get-started/technical-requirements/adobe-premiere-pro-technical-requirements.html>
- [AD4] Adobe, Enable hardware encoding (07.01.2026): <https://helpx.adobe.com/premiere/desktop/get-started/technical-requirements/enable-hardware-encoding-support.html>
- [AD5] Adobe, Create proxies in Premiere (по выдаче поиска; страницу целиком не открывал): <https://helpx.adobe.com/premiere/desktop/organize-media/ingest-proxy-workflow/create-proxies.html>
- [R1] Blackmagic, DaVinci Resolve 21.1 Supported Formats and Codecs (сентябрь 2026): <https://documents.blackmagicdesign.com/SupportNotes/DaVinci_Resolve_21_Supported_Codec_List.pdf>
- [VG1] VEGAS Pro 22, Video Codec Overview: <https://help.magix-hub.com/video/vegas/22/en/content/topics/13-appendix/codecoverview.htm>
- [HB1] HandBrake Documentation, AMD VCN: <https://handbrake.fr/docs/en/latest/technical/video-vcn.html>
- [PD1] CyberLink PowerDirector, спецификация: <https://www.cyberlink.com/products/powerdirector-video-editing-software/spec_en_US.html>
- [T1] Tom's Hardware, Video Encoding Tested: AMD GPUs Still Lag Behind Nvidia, Intel (10.03.2023): <https://www.tomshardware.com/news/amd-intel-nvidia-video-encoding-performance-quality-tested>
- [T2] TechSpot, AMD's RDNA 4 GPUs bring major encoding and ray tracing upgrades (2025): <https://www.techspot.com/news/106986-amd-rdna-4-gpus-bring-major-encoding-ray.html>
- [F1] Framework Community, «4:2:2 video on AMD» (февраль 2025): <https://community.frame.work/t/42-video-on-amd/64502>

**Камеры**
- [C1] Sony ILCE‑7M4 Help Guide, Movie Settings: <https://helpguide.sony.net/ilc/2110/v1/en/contents/TP1000640834.html>
- [C2] Sony ILCE‑7M4 Help Guide, File Format (movie): <https://helpguide.sony.net/ilc/2110/v1/en/contents/TP1000640835.html>
- [C3] Sony ILCE‑7M4 Help Guide, List of default setting values: <https://helpguide.sony.net/ilc/2110/v1/en/contents/TP1001803633.html>
- [C4] Canon EOS R6 Mark II, Specifications (открыто в Chrome): <https://www.canon-europe.com/cameras/eos-r6-mark-ii/specifications/>
- [C5] Fujifilm X‑T5, Specifications: <https://www.fujifilm-x.com/global/products/cameras/x-t5/specifications/>
- [C5b] Fujifilm X‑S20, Specifications: <https://www.fujifilm-x.com/global/products/cameras/x-s20/specifications/>
- [C6] Panasonic Lumix S5II (DC‑S5M2), Specs (открыто в Chrome; curl — 403): <https://www.panasonic.com/uk/consumer/cameras-camcorders/lumix-mirrorless-cameras/lumix-s-full-frame-cameras/dc-s5m2.specs.html>
- [C7] Nikon Z6III, страница модели: <https://imaging.nikon.com/imaging/lineup/mirrorless/z6_3/>
- [C8] Apple, iPhone 17 Pro Tech Specs: <https://support.apple.com/en-us/125090>
- [C9] GoPro, 10‑Bit Color Video Information (открыто в Chrome): <https://community.gopro.com/s/article/10-Bit-Color-Video-Information?language=en_US>
- [C10] DJI Mini 5 Pro, Specs: <https://www.dji.com/global/mini-5-pro/specs>
- [C11] DJI Mini 4 Pro, Specs: <https://www.dji.com/global/mini-4-pro/specs>
- [C12] DJI Mavic 4 Pro, Specs: <https://www.dji.com/global/mavic-4-pro/specs>
- [C13] DJI Osmo Action 5 Pro, Specs: <https://www.dji.com/global/osmo-action-5-pro/specs>
- [C14] DJI Osmo Pocket 3, Specs: <https://www.dji.com/global/osmo-pocket-3/specs>

**Linux**
- [L1] ArchWiki, Hardware video acceleration: <https://wiki.archlinux.org/title/Hardware_video_acceleration>
- [L2] ArchWiki, DaVinci Resolve: <https://wiki.archlinux.org/title/DaVinci_Resolve>
- [L3] ROCm, System requirements (Linux): <https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html>
- [LV1] Локальная проверка 30.09.2026: запрос `vaQueryConfigProfiles` / `vaGetConfigAttributes(VAConfigAttribRTFormat)` через libva 1.24 к `/dev/dri/renderD128` на компьютере пользователя.
  Драйвер: «Mesa Gallium driver 26.2.3-arch1.1 for AMD Radeon 780M Graphics (radeonsi, phoenix …)». API libva: <https://intel.github.io/libva/group__api__core.html>

**Из Intel‑заметки** (`../Intel/notes/intel-cpu.md`): [D1][D2] Intel media‑driver; [V1] матрица NVIDIA NVDEC/NVENC; [V2] whitepaper NVIDIA Blackwell. Ссылки — в её разделе 6.

## Проверка (скептик, 30.09.2026)

Проверял на компьютере пользователя: curl с браузерным User-Agent, Chrome пользователя (своя вкладка, закрыта), живой запрос VA-API к Radeon 780M.
Не открылись: gitlab.freedesktop.org (Mesa) и gitlab.archlinux.org (PKGBUILD) — Anubis через curl, «Verification Required» в Chrome; проверку не проходил.

| # | Утверждение | Вердикт | Чем проверено |
|---|---|---|---|
| 1 | Версии VCN по кодовым именам (таблица 1.1): Barcelo 2.2, Rembrandt и Mendocino 3.1.1, Raphael/Granite Ridge/Dragon Range 3.1.2, Phoenix/Hawk Point 4.0.2, Strix/Krackan/Gorgon Point 4.0.5, Strix Halo 4.0.6 | **подтверждено** | CSV ядра, скачан 30.09.2026 — все строки совпали; Dragon Range и Gorgon Point там есть [K1]. RX 9070/9060 XT — VCN 5.0.0, RX 7600M/7700S — 4.0.4 [K2] |
| 2 | Кодовые имена на amd.com: Ryzen 7 250 — Hawk Point, AI 7 350 — Krackan Point, AI 9 HX 370 — Strix Point, AI 9 HX 470 и AI 7 450 — Gorgon Point, 7530U — Barcelo R, 7320U — Mendocino | **подтверждено** | Поле «Former Codename» в Chrome [A1][A3][A7][A8][A9][A11][A12]. Графика и ядра тоже совпали: 780M/8, 860M/8, 890M/12, 890M/12, 860M/8, Radeon Graphics/6, 610M/4. Дополнительно: Ryzen 5 220 — Hawk Point, 740M [A13] |
| 3 | AMF‑вики: «All codecs are 4:2:0», AVC‑декод «8b: 4K» у VCN 2.0–5.0, AV1 12 бит на VCN 4.0/5.0, AV1‑кодировщик на двух блоках только у Strix Halo; правка 05.12.2025 | **подтверждено** | Страница вики, дата правки 2025‑12‑05 [G1]. Там же Navi48 — 1 блок VCN. Новое: Granite Ridge указан как «VCN 3.0» (в ядре — 3.1.2), дописано в 1.1 |
| 4 | H.264 у AMD — только 8 бит 4:2:0; HEVC — только 4:2:0 8/10 бит (Mesa) | **подтверждено** (для VCN 4.0.2) | Живой запрос VA-API на 780M: H.264 CB/Main/High — только YUV420; HEVC Main/Main10 — YUV420 и YUV420_10; профилей High10, High422 и HEVC RExt нет [LV1]. Исходник Mesa [M1][M2] не открылся |
| 5 | AV1 12 бит в Mesa — только у VCN 4.0.0 и 5.x | **частично подтверждено** | У 780M (VCN 4.0.2) профиля AV1 Profile 2 нет [LV1]. RX 7900 и RX 9000 не проверял: исходник Mesa не открылся. Для камер неважно |
| 6 | Puget, Resolve Studio (обн. 17.06.2025): у Ryzen iGPU и Radeon 5000–7000 нет HEVC 4:2:2 и H.264 10 бит; у Intel 11+ есть HEVC 4:2:2/4:4:4/12 бит; у RTX 40 есть HEVC 4:4:4 и 12 бит 4:2:0, но нет 4:2:2; RTX 50 — всё (Resolve 20) | **подтверждено** | Все ячейки таблицы 2.2 сверены со значками на странице [P1]. Сноска «* Added in DaVinci Resolve Studio 20» есть |
| 7 | Puget, Premiere (обн. 12.06.2025): из 4:2:2 декодируется только HEVC 10 бит 4:2:2 (Intel 11+, RTX 50 с 25.3); H.264 10 бит — только RTX 50 | **подтверждено** | Таблица [P2]; сноска «*Added in Premiere Pro 25.3». H.264 8 бит 4:2:2 в Premiere не декодирует даже RTX 50 — в заметке так и есть (3.2) |
| 8 | Puget о RX 9070 XT: в 4:2:2 10 бит «half as fast due to a lack of acceleration support» | **подтверждено** | Цитата есть, статья обновлена 31.03.2025 [P3] |
| 9 | Puget Bench, Resolve 20: 890M против Arc 140T — 2872 против 2489, эффекты 12,1 против 10,7, HEVC 4:2:2 10 бит 41,9 против 56,3 кадра/с, AI — Intel +26 % | **подтверждено** | Страница [PB1], снято 30.09.2026: 2872 / 2488,92; 12,1 / 10,71; 41,93 / 56,29; AI 13,65 / 17,26; кодирование HEVC 60 Мбит/с 10 бит — 70,89 / 52,43. Это медиана по GPU 890M (системы на HX 370), а не по одному ноутбуку |
| 10 | 780M/860M хуже Arc 130T/140T (−15…−20 % общий балл, −22…−34 % эффекты), лучше Meteor Lake (+12–13 %); 890M в Premiere +18 % | **подтверждено** | Resolve 19: 780M 2244,67 против 140T 2700,63; эффекты 9,69 против 12,39 [PB3]. Premiere: 780M 3038 и 860M 2882 против 130T 3591; эффекты 9,38 и 10,23 против 14,25; Lumetri 11,0 и 11,9 против 18,85 [PB7][PB8]. 890M 4326 против 140T 3661 [PB6]. 860M против Meteor Lake 2401,64 против 2150,5; HEVC 4:2:2 — 43,35 против 41,74 [PB2]. Оговорка: 860M сравнивали со 130T только в Premiere |
| 11 | Камеры: Sony A7 IV XAVC S 4K 10 бит — всегда 4:2:2, XAVC HS — 4:2:0 или 4:2:2, S‑I — 4:2:2; GoPro 10 бит = 4:2:0; DJI Mini 4 Pro D‑Log M = 10 бит 4:2:0; Mavic 4 Pro H.264 ALL‑I = 10 бит 4:2:2; Panasonic S5II H.265 — только 4:2:0, H.264 MOV — 4:2:2 10 бит; Fujifilm X‑T5 H.265 — 4:2:2 или 4:2:0 10 бит | **подтверждено** | Help Guide Sony [C1][C3]; GoPro [C9] и Panasonic [C6] — в Chrome (в спецификации S5II у H.265 только «4:2:0 10-bit», у H.264 «4:2:2 10-bit LongGOP» и «4:2:0 8-bit»); DJI [C11][C12] (ALL‑I — только Mavic 4 Pro 512GB Creator Combo); Fujifilm [C5] |
| 12 | «У Canon 10 бит — всегда 4:2:2» (итог автора; в 3.2 — «с Canon AMD всегда хуже») | **исправлено** | Подтверждено только для EOS R6 Mark II: «YCbCr4:2:0 8-bit or YCbCr4:2:2 10bit», H.265 — для Canon Log / HDR PQ [C4]. Другие Canon не проверены — обобщение снято |
| 13 | HP отключает аппаратный HEVC на ProBook 465 G11, EliteBook 665 G11, ProBook 4 G1a 16 | **подтверждено** | Текущие QuickSpecs, скачаны 30.09.2026: «Hardware acceleration for CODEC H.265/HEVC … is disabled on this platform» — [c08908497](https://www8.hp.com/h20195/V2/GetPDF.aspx/c08908497), [c08927104](https://www8.hp.com/h20195/V2/GetPDF.aspx/c08927104), [c09111176](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09111176) |
| 14 | «Без HEVC — для AMD важнее, чем для Intel» | **исправлено** | Это вывод, а не факт. У Intel без HEVC пропадает и HEVC 4:2:2 — главный плюс Intel [P1][P2]. Отключённый HEVC плох для обоих |
| 15 | Resolve 21.1 (сентябрь 2026): бесплатный под Windows — «8-bit OS-supported profiles» (H.264), «8/10-bit» (H.265), «More profiles and GPU acceleration in Studio»; под Linux H.264/H.265 — «Studio only», «GPU accelerated on Nvidia graphics» | **подтверждено** | PDF Blackmagic, на титуле «September 2026» [R1]. Уточнение: использует ли декодер Windows в бесплатной версии DXVA — Blackmagic не пишет, не проверено |
| 16 | HandBrake: VCN только для кодирования; VEGAS Pro 22: у AMF нет 4:2:2, HEVC 4:2:2 — только «Intel HW» 11+ | **подтверждено** | «supports the AMD VCN hardware encoder but does NOT support the hardware decoder» [HB1]. Таблица VEGAS: у AMF H.264 — только 4:2:0 8 бит, у HEVC 4:2:2 8/10 бит (REXT) — ✓ только у Intel HW [VG1] |
| 17 | Adobe (07.01.2026): HEVC 4:2:2 10 бит упомянут только для Intel | **подтверждено** | «support HEVC 4:2:2 10-bit decoding on Intel platforms», «Last updated on Jan 7, 2026» — в Chrome [AD1] |
| 18 | Качество AMF: Tom's Hardware (10.03.2023) — AMD отстаёт, Arc «right behind» NVIDIA; RDNA 4 — «+25 % H.264, +11 % HEVC» | **уточнено** | Цитаты [T1] есть. Но Arc у Tom's — дискретный; из iGPU Intel там только UHD 770, iGPU Meteor/Arrow Lake не тестировали. У TechSpot «+25 %» — это «H.264 low-latency encode quality» [T2]. Исправлено в 2.1, 2.3 и в таблице 6 |
| 19 | Итог: «для „камера неизвестна“ без дискретки безопаснее Intel Arrow Lake‑H» | **исправлено** | Вывод сильнее данных. HEVC 4:2:2 в Resolve и Premiere декодирует любой Intel 11+ [P1][P2], в том числе Raptor Lake i7‑13620H — лучший вариант из `../Intel/REPORT.md`. Arrow Lake‑H добавляет только AV1‑кодирование и более сильную iGPU |
| 20 | Arch: `mesa` 26.2.3, H.264/HEVC в VA‑API включены | **подтверждено** (строку `video-codecs=all` не видел) | `pacman -Qi mesa` — 1:26.2.3-1; VA‑API выдаёт H.264 и HEVC [LV1]. PKGBUILD [M3] не открылся (Anubis) |
| 21 | Отзыв Framework: Sony 4K 10 бит 4:2:2 в Resolve на FW 16 — «just fine», вентилятор «really cranked» | **подтверждено** (как единичный отзыв) | JSON темы, пост от 13.02.2025 [F1] |

**Итог проверки:**
- Факты о железе, кодеках, тестах Puget и камерах подтвердились. Неверных кодовых имён и перепутанных поколений не нашёл.
- Исправлены четыре места, где вывод сильнее данных: обобщение по Canon, «Arrow Lake‑H» в итоге, «HEVC для AMD важнее» и контекст цифр качества кодирования (Tom's, TechSpot).
- Цен и парт‑номеров в заметке нет, проверять было нечего.
- Про память (SO‑DIMM или распайка) заметка ничего не утверждает. На amd.com у Hawk Point, Krackan, Strix и Gorgon Point указаны и DDR5, и LPDDR5X, так что тип памяти решает конкретный ноутбук — см. `notes/amd-cpu.md`.
