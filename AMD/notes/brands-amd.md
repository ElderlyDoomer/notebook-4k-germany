# AMD-линейки брендов в Германии (15–16", 2024–2026): процессоры, память, болячки

_Обновлено 2026-09-30. Каждый факт — со ссылкой. «не проверено» — первоисточник не найден._
_Общая оценка брендов (запчасти, сервис, надёжность, гарантия, право на ремонт) — в [`../../Intel/notes/brands.md`](../../Intel/notes/brands.md). Здесь — только то, что касается AMD-моделей._
_Карта имён процессоров подробно — в `amd-cpu.md`, кодеки — в `amd-codecs.md`, HEVC — в `hevc-amd.md` (другие заметки этого шага)._
_Доступ: PSREF, HP QuickSpecs/MSG, dl.dell.com, asus.com, amd.com, Icecat, notebookcheck, billiger.de — через curl; dell.com (страницы) и frame.work — через WebFetch. Модельный API PSREF (`pdfexport/singleModel`) в конце сессии отвечал ошибкой — раскладку памяти по MTM брал из Icecat._

## Коротко

1. **Заводские 2×16 ГБ + 1 ТБ на AMD до 1100 € нашёл только у ThinkBook 16.**
   - `21MW00AYGE`: ThinkBook 16 G7 ARP, Ryzen 5 7535HS, **2×16** — **998,99 €** (Easynotebooks).
   - `21UT004QGE`: ThinkBook 16 G9 AHP, Ryzen 5 220, **2×16** — **1073 €** (c-nw).
   - Раскладка — по Icecat, цены — billiger.de, 30.09.2026 ([Icecat G7](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Lenovo&ProductCode=21MW00AYGE), [Icecat G9](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Lenovo&ProductCode=21UT004QGE)).
   - Минус обоих: базовый экран 45 % NTSC ([PSREF G7](https://psref.lenovo.com/syspool/Sys/PDF/ThinkBook/ThinkBook_16_G7_ARP/ThinkBook_16_G7_ARP_Spec.PDF), [PSREF G9](https://psref.lenovo.com/syspool/Sys/PDF/ThinkBook/ThinkBook_16_G9_AHP/ThinkBook_16_G9_AHP_Spec.PDF)).
2. **Ловушка: ThinkPad E16 Gen 3 AMD с 32 ГБ — это одна планка 1×32.** Касается `21ST004GGE` (1149 €, из MEMORY.md) и `21ST001YGE`. Слотов два, но с завода работает один канал ([Icecat 004G](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Lenovo&ProductCode=21ST004GGE), [Icecat 001Y](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Lenovo&ProductCode=21ST001YGE)).
3. **HP для бизнеса на AMD: два слота есть, но HEVC у дешёвых серий выключен.**
   - HEVC выключен: ProBook 465 G11, EliteBook 665 G11, ProBook 4 G1a 16, EliteBook 6 G1a 16.
   - HEVC включён только у EliteBook 8 G1a 16, а он с 32/1 ТБ стоит от 1299 € (QuickSpecs, см. раздел HP).
4. **У потребительских линеек почти всё — ловушки.**
   - «8 ГБ распайки + 1 слот»: IdeaPad Slim 3, старые Vivobook 15/16.
   - Один слот и максимум 16 ГБ: Dell 15 DC15255, Inspiron 15 3535.
   - Mendocino с распайкой: V15 AMN, Vivobook Go, Dell Pro 15 Essential.
   - Только распайка: IdeaPad Pro 5, Yoga, Zenbook, Swift, Aspire 16 AI, Dell 16 Plus, OmniBook 5, Pavilion.
5. **Старые ядра под новыми именами** (по полю «Former Codename» на amd.com):
   - Ryzen 5 40 и 3 30 — Mendocino (Zen 2);
   - Ryzen 5 150, 7 170, 5 130, 7 160 — Rembrandt (Zen 3+);
   - Ryzen 7x30U — Barcelo R (Zen 3, графика «Radeon Graphics»);
   - Ryzen 200 — Hawk Point (Zen 4).
   Магазины продают 32 ГБ именно на Barcelo R: Medion Avantum 15 E1, Acer Extensa 15, Aspire Go 15.
6. **Хорошие AMD-платформы с 2× SO-DIMM есть, но в DE их продают с 16 ГБ (2×8) или с 1×32:**
   - IdeaPad Slim 5 16 (AKP10 / AHP11 / AGP11);
   - Dell 16 DC16255, Dell Pro 16 PC16255, Inspiron 16 5645;
   - ASUS ExpertBook P1 / BM1 / P3 / B3 G2 / P5 G2;
   - LOQ / Legion 5, TUF A15/A16 2025, MSI Venture A16, Gigabyte Gaming A16;
   - Tuxedo InfinityBook Pro 15 Gen10 AMD, Framework 16, XMG Core.
7. **«16 ГБ распайки + слот» (список 3 критериев): Vivobook 16 M1607 и Vivobook S16 M3607.** С планкой 16 ГБ получаются симметричные 16+16 в двухканале ([asus M1607](https://www.asus.com/Laptops/For-Home/Vivobook/ASUS-Vivobook-16-M1607/techspec/), [asus M3607](https://www.asus.com/Laptops/For-Home/Vivobook/ASUS-Vivobook-S16-M3607/techspec/)). Но планка DDR5-5600 16 ГБ сейчас стоит ~237 € ([Intel sweep](../../Intel/notes/sweep-16gb-plus-stick.md)).
8. **AMD + RTX 50 (аппаратный 4:2:2 через NVIDIA) в бюджет не влезает.** Gigabyte GAMING A16 3VH: Ryzen 7 260 + RTX 5060, 1×16 + свободный слот, 1099 €. С планкой получается ≈ 1336 € ([billiger](https://www.billiger.de/pricelist/5372928568-gigabyte-gaming-a16-3vh-amd-ryzen-7-260-16), [Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&GTIN=4719331766764)).
9. **Порты — главное отличие AMD-версий.**
   - У потребительских AMD часто нет USB4 и стоит HDMI 1.4 (Dell 16 DC16255, Inspiron 16 5645, IdeaPad Slim 5 16, Vivobook 16).
   - У бизнес-AMD есть USB4, а у ThinkPad L16/T16/P16s AMD и EliteBook 6/8 G1a порты даже сертифицированы как Thunderbolt 4 (PSREF, QuickSpecs).
10. **Тестовые и магазинные AMD-ноутбуки часто работают в одноканале.** Notebookcheck записывает это в минусы у LOQ 15AHP10, ThinkPad T16 Gen 5 AMD, ExpertBook PM3 и PM5 G2, HP Omen 16 и EliteBook 865 G10 (ссылки ниже). Проверять раскладку по парт-номеру.

## Главная таблица: линейка → CPU → память → годится ли под 2×16 SO-DIMM

Что значат оценки в колонке «2×16?»:
- «да» — два слота SO-DIMM, 32 ГБ в двухканале штатно;
- «16+слот» — 16 ГБ распайки и один слот;
- «распайка» — только допустимый список 3 критериев, при 32 ГБ;
- «нет» — не подходит.

Кодовые имена — с amd.com (см. «Карта имён» ниже) или из спецификаций в тестах notebookcheck.

| Линейка (год) | CPU (кодовое имя) | Память | 2×16? | Даташит |
|---|---|---|---|---|
| **Lenovo** | | | | |
| ThinkPad E16 Gen 2 AMD (2024) | Ryzen 7x35U/HS (Rembrandt R), 150/170 (Rembrandt) | 2× DDR5 SO-DIMM, до 64 | да | [PSREF](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_E16_Gen_2_AMD/ThinkPad_E16_Gen_2_AMD_Spec.PDF) |
| ThinkPad E16 Gen 3 AMD (2025) | Ryzen 3 210 … 7 250 (Hawk Point) | 2× SO-DIMM, до 64 | да, **но SKU 32 ГБ = 1×32** | [PSREF](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_E16_Gen_3_AMD/ThinkPad_E16_Gen_3_AMD_Spec.PDF) |
| ThinkPad E16 Gen 4 AMD (2026) | Ryzen AI 5 330 (Krackan), AI 5/7 4xx (Gorgon) | 2× SO-DIMM, до 64 | да | [PSREF](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_E16_Gen_4_AMD/ThinkPad_E16_Gen_4_AMD_Spec.PDF) |
| ThinkPad L16 Gen 1 / 2 / 3 AMD | 7x35U PRO / PRO 2xx + AI 3xx / AI 4xx | 2× SO-DIMM, до 64 | да | [G1](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_L16_Gen_1_AMD/ThinkPad_L16_Gen_1_AMD_Spec.PDF), [G2](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_L16_Gen_2_AMD/ThinkPad_L16_Gen_2_AMD_Spec.PDF), [G3](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_L16_Gen_3_AMD/ThinkPad_L16_Gen_3_AMD_Spec.PDF) |
| ThinkPad T16 Gen 2 AMD (2023) | Ryzen 7x40U (Phoenix) | распайка LPDDR5x 8–64 | распайка | [PSREF](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_T16_Gen_2_AMD/ThinkPad_T16_Gen_2_AMD_Spec.PDF) |
| ThinkPad T16 Gen 4 / Gen 5 AMD | AI PRO 3xx / PRO 2xx + AI PRO 4xx | 2× SO-DIMM, до 64/96 | да | [G4](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_T16_Gen_4_AMD/ThinkPad_T16_Gen_4_AMD_Spec.PDF), [G5](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_T16_Gen_5_AMD/ThinkPad_T16_Gen_5_AMD_Spec.PDF) |
| ThinkPad P16s Gen 4 AMD (2025) | AI PRO 340/350, AI 9 HX PRO 370 | 2× SO-DIMM, до 96 | да | [PSREF](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_P16s_Gen_4_AMD/ThinkPad_P16s_Gen_4_AMD_Spec.PDF) |
| ThinkPad P16s Gen 5 AMD (2026) | AI PRO 440/450, HX PRO 470 | **1× LPCAMM2**, двухканал, до 96 | функционально да (1 модуль) | [PSREF](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_P16s_Gen_5_AMD/ThinkPad_P16s_Gen_5_AMD_Spec.PDF) |
| ThinkBook 16 G6 ABP (2023) | Ryzen 7x30U (Barcelo R) | 2× DDR4 SO-DIMM, до 64 | да, но CPU старый | [PSREF](https://psref.lenovo.com/syspool/Sys/PDF/ThinkBook/ThinkBook_16_G6_ABP/ThinkBook_16_G6_ABP_Spec.PDF) |
| **ThinkBook 16 G7 ARP (2024)** | 7535HS/7735HS (Rembrandt R), 150/170 | 2× DDR5-4800 SO-DIMM, до 64 | **да** | [PSREF](https://psref.lenovo.com/syspool/Sys/PDF/ThinkBook/ThinkBook_16_G7_ARP/ThinkBook_16_G7_ARP_Spec.PDF) |
| ThinkBook 16 G7+ ASP (2024) | Ryzen AI 9 365 (Strix Point) | распайка 32 LPDDR5x | распайка | [PSREF](https://psref.lenovo.com/syspool/Sys/PDF/ThinkBook/ThinkBook_16_G7plus_ASP/ThinkBook_16_G7plus_ASP_Spec.PDF) |
| **ThinkBook 16 G9 AHP (11/2025)** | Ryzen 3 205 … 7 250 (Hawk Point) | 2× DDR5-5600 SO-DIMM, до 64 | **да** | [PSREF](https://psref.lenovo.com/syspool/Sys/PDF/ThinkBook/ThinkBook_16_G9_AHP/ThinkBook_16_G9_AHP_Spec.PDF) |
| ThinkBook 16p G6 ADR (2025) | Ryzen 9 8940HX/8945HX (Dragon Range) | 2× SO-DIMM, до 64 | да (дорого) | [PSREF](https://psref.lenovo.com/syspool/Sys/PDF/ThinkBook/ThinkBook_16p_G6_ADR/ThinkBook_16p_G6_ADR_Spec.PDF) |
| IdeaPad Slim 3 15ABR8 / 16ABR8 | 5x25U, 7x30U (Barcelo / Barcelo R) | распайка DDR4 8–16 | **нет** | [PSREF](https://psref.lenovo.com/syspool/Sys/PDF/IdeaPad/IdeaPad_Slim_3_15ABR8/IdeaPad_Slim_3_15ABR8_Spec.PDF) |
| IdeaPad Slim 3 15AMN8 | 7320U/7520U (Mendocino) | распайка LPDDR5 4–16 | **нет** | [PSREF](https://psref.lenovo.com/syspool/Sys/PDF/IdeaPad/IdeaPad_Slim_3_15AMN8/IdeaPad_Slim_3_15AMN8_Spec.PDF) |
| IdeaPad Slim 3 15/16ARP10 (2025) | 150/170, 7533HS/7535HS/7735HS | **8 распайки + 1 SO-DIMM, до 24** | **нет** | [15](https://psref.lenovo.com/syspool/Sys/PDF/IdeaPad/IdeaPad_Slim_3_15ARP10/IdeaPad_Slim_3_15ARP10_Spec.PDF), [16](https://psref.lenovo.com/syspool/Sys/PDF/IdeaPad/IdeaPad_Slim_3_16ARP10/IdeaPad_Slim_3_16ARP10_Spec.PDF) |
| IdeaPad Slim 3 15/16AHP10 | 8540U/8640HS/8840HS (Hawk Point), 125/155 | **8 распайки + 1 SO-DIMM, до 24** | **нет** | [15](https://psref.lenovo.com/syspool/Sys/PDF/IdeaPad/IdeaPad_Slim_3_15AHP10/IdeaPad_Slim_3_15AHP10_Spec.PDF), [16](https://psref.lenovo.com/syspool/Sys/PDF/IdeaPad/IdeaPad_Slim_3_16AHP10/IdeaPad_Slim_3_16AHP10_Spec.PDF) |
| IdeaPad Slim 5 15ARP10 (15,3") | 7535HS/7735HS | распайка LPDDR5x 16/32 | распайка | [PSREF](https://psref.lenovo.com/syspool/Sys/PDF/IdeaPad/IdeaPad_Slim_5_15ARP10/IdeaPad_Slim_5_15ARP10_Spec.PDF) |
| IdeaPad Slim 5 16ARP10 | 7533HS/7535HS/7735HS | 2× SO-DIMM, «до 32 offering» | да | [PSREF](https://psref.lenovo.com/syspool/Sys/PDF/IdeaPad/IdeaPad_Slim_5_16ARP10/IdeaPad_Slim_5_16ARP10_Spec.PDF) |
| **IdeaPad Slim 5 16AKP10 (2025)** | AI 5 330/340, AI 7 350 (Krackan) | 2× SO-DIMM, до 32 | да | [PSREF](https://psref.lenovo.com/syspool/Sys/PDF/IdeaPad/IdeaPad_Slim_5_16AKP10/IdeaPad_Slim_5_16AKP10_Spec.PDF) |
| **IdeaPad Slim 5 16AHP11 (2026)** | Ryzen 5 240 / 7 260 (Hawk Point) | 2× SO-DIMM, до 32 | да | [PSREF](https://psref.lenovo.com/syspool/Sys/PDF/IdeaPad/IdeaPad_Slim_5_16AHP11/IdeaPad_Slim_5_16AHP11_Spec.PDF) |
| **IdeaPad Slim 5 16AGP11 (2026)** | AI 5 430, AI 7 445/450 (Gorgon) | 2× SO-DIMM, до 32 | да | [PSREF](https://psref.lenovo.com/syspool/Sys/PDF/IdeaPad/IdeaPad_Slim_5_16AGP11/IdeaPad_Slim_5_16AGP11_Spec.PDF) |
| IdeaPad Pro 5 16 AHP9/AKP10/ASP10/AGP11 | 8x45HS / AI 3xx / AI 9 365 / AI 4xx | распайка LPDDR5x 16–32 | распайка | [AKP10](https://psref.lenovo.com/syspool/Sys/PDF/IdeaPad/IdeaPad_Pro_5_16AKP10/IdeaPad_Pro_5_16AKP10_Spec.PDF), [AGP11](https://psref.lenovo.com/syspool/Sys/PDF/IdeaPad/IdeaPad_Pro_5_16AGP11/IdeaPad_Pro_5_16AGP11_Spec.PDF) |
| IdeaPad Vibe 15AKP12 (анонс 28.09.2026) | Ryzen AI 5 330 | 2× SO-DIMM, до 32 | да, но порты слабые | [PSREF](https://psref.lenovo.com/syspool/Sys/PDF/IdeaPad/IdeaPad_Vibe_15AKP12/IdeaPad_Vibe_15AKP12_Spec.PDF) |
| IdeaPad 5 2-in-1 16AKP10 | AI 5 340 / AI 7 350 | распайка 16 | **нет** | [PSREF](https://psref.lenovo.com/syspool/Sys/PDF/IdeaPad/IdeaPad_5_2_in_1_16AKP10/IdeaPad_5_2_in_1_16AKP10_Spec.PDF) |
| V15 G4 AMN / V15 G6 AMN | 7320U/7520U; Athlon Silver 10, Ryzen 3 30, **Ryzen 5 40** (Mendocino) | распайка LPDDR5 8/16 | **нет** | [G4](https://psref.lenovo.com/syspool/Sys/PDF/Lenovo/Lenovo_V15_G4_AMN/Lenovo_V15_G4_AMN_Spec.PDF), [G6](https://psref.lenovo.com/syspool/Sys/PDF/Lenovo/Lenovo_V15_G6_AMN/Lenovo_V15_G6_AMN_Spec.PDF) |
| V15 G4 ABP | 5x00U/5x25U, 7x30U | 8 DDR4 распайки + 1 слот, до 16 | **нет** | [PSREF](https://psref.lenovo.com/syspool/Sys/PDF/Lenovo/Lenovo_V15_G4_ABP/Lenovo_V15_G4_ABP_Spec.PDF) |
| V15 G6 ARP (11/2025) | Ryzen 3 110, 5 150, 7 170 (Rembrandt) | 2× DDR5-4800 SO-DIMM, до 32 | да, но CPU старый | [PSREF](https://psref.lenovo.com/syspool/Sys/PDF/Lenovo/Lenovo_V15_G6_ARP/Lenovo_V15_G6_ARP_Spec.PDF) |
| Yoga 7 2-in-1 16 AKP10/AGP11; Yoga Pro 7 15ASH11 | AI 3xx / AI 4xx / AI Max 300 (Strix Halo) | распайка LPDDR5x | распайка | [AGP11](https://psref.lenovo.com/syspool/Sys/PDF/Yoga/Yoga_7_2_in_1_16AGP11/Yoga_7_2_in_1_16AGP11_Spec.PDF), [15ASH11](https://psref.lenovo.com/syspool/Sys/PDF/Yoga/Yoga_Pro_7_15ASH11/Yoga_Pro_7_15ASH11_Spec.PDF) |
| LOQ 15ARP9 / 15AHP9 / 15AHP10 / 15ARP10E / 15AHP11 | 7x35HS / 8x45HS / 220, 250 / 150, 170 / 216 … 253 | 2× SO-DIMM, до 32 (ARP10E — «до 16 offering») | да (+RTX) | [AHP10](https://psref.lenovo.com/syspool/Sys/PDF/LOQ/LOQ_15AHP10/LOQ_15AHP10_Spec.PDF), [ARP10E](https://psref.lenovo.com/syspool/Sys/PDF/LOQ/LOQ_15ARP10E/LOQ_15ARP10E_Spec.PDF), [AHP11](https://psref.lenovo.com/syspool/Sys/PDF/LOQ/LOQ_15AHP11/LOQ_15AHP11_Spec.PDF) |
| Legion 5 15AHP10 / 15AKP10 / 15AHP11 / 15AGP11 | 260 / AI 7 350 / 250, 253 / AI 7 450, AI 9 465 | 2× SO-DIMM, до 32 | да (дорого) | [AHP10](https://psref.lenovo.com/syspool/Sys/PDF/Legion/Legion_5_15AHP10/Legion_5_15AHP10_Spec.PDF), [AGP11](https://psref.lenovo.com/syspool/Sys/PDF/Legion/Legion_5_15AGP11/Legion_5_15AGP11_Spec.PDF) |
| **HP** | | | | |
| HP 255 G10 (15,6") | 7330U/7530U/7730U (Barcelo R); 7120U/7320U/7520U (Mendocino) | Barcelo R: 2 SODIMM DDR4, до 32, «non-accessible»; Mendocino: LPDDR5 onboard | Barcelo R — формально да, но CPU старый; Mendocino — нет | [QuickSpecs c08479497](https://www8.hp.com/h20195/V2/GetPDF.aspx/c08479497) |
| HP 255R G10 (15,6") | 7335U/7535U/7735U (Rembrandt R); 7320U/7520U | 2 SODIMM DDR5-4800, «customer non-accessible», макс. указан как 1×32 | формально да | [QuickSpecs c09053765](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09053765) |
| ProBook 465 G11 (16") | 7335U/7535U/7735U (Rembrandt R) | 2 SODIMM | да, **HEVC выкл.** | [QuickSpecs c08908497](https://www8.hp.com/h20195/V2/GetPDF.aspx/c08908497) |
| EliteBook 665 G11 (16") | 7x35U (+PRO) | 2 SODIMM | да, **HEVC выкл.** | [QuickSpecs c08927104](https://www8.hp.com/h20195/V2/GetPDF.aspx/c08927104) |
| **ProBook 4 G1a 16** | Ryzen 3 210 … 7 250, 7 255H (Hawk Point) | 2 SODIMM | да, **HEVC выкл.** | [QuickSpecs c09111176](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09111176) |
| EliteBook 6 G1a 16 | Ryzen 3 210 … 7 PRO 250, 255H | 2 SODIMM | да, **HEVC выкл.** | [QuickSpecs c09111179](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09111179) |
| **EliteBook 8 G1a 16** | 224/230/249/250 (+PRO); AI 5/7 (PRO) 340/350 | 2 SODIMM | да, **HEVC есть** | [c09120200](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09120200), [c09120201](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09120201) |
| EliteBook 8 G2a 16 (2026) | Ryzen AI 4xx (Gorgon) | распайка LPDDR5 | распайка | [NBC](https://www.notebookcheck.net/Surprisingly-fast-with-32-GB-RAM-and-Ryzen-7-HP-EliteBook-8-G2a-16-laptop-review.1358548.0.html) |
| OmniBook 3 16 (AMD 16-by0xxx, 2026) | 130/160 (Rembrandt), 230/250/255 (Hawk Point), AI 5 430 / AI 7 445 (Gorgon) | «Memory is not accessible or upgradeable» | не проверено (скорее нет) | [MSG](https://kaas.hpcloud.hp.com/pdf-public/pdf_13159558_en-US-1.pdf) |
| OmniBook 5 16 Next Gen (AMD 16-bp0xxx) | 230/250, AI 5 330/430, AI 7 445, AI 9 465 | LPDDR5x-7500, 16/32 распайка | распайка | [MSG](https://kaas.hpcloud.hp.com/pdf-public/pdf_13052194_en-US-1.pdf) |
| Pavilion 16-ag0 | Ryzen 5 8540U (Hawk Point) | распайка LPDDR5 | **нет** (16) | [NBC](https://www.notebookcheck.net/HP-Pavilion-16-review-Budget-AMD-CPU-in-a-stylish-laptop.959151.0.html) |
| Envy x360 16 AMD | Ryzen 7 8840HS | распайка LPDDR5 | распайка | [NBC](https://www.notebookcheck.net/HP-Envy-x360-2-in-1-16-review-Ryzen-7-8840HS-beats-Core-Ultra-7-155U.837856.0.html) |
| Victus 16 (16-s0xxx) | 7640HS/7840HS (+PRO) | 2 SODIMM DDR5-5600, 32 = 16×2 | да (+RTX) | [MSG](https://kaas.hpcloud.hp.com/pdf-public/pdf_7911438_en-US-1.pdf) |
| Victus 15 AMD (15-fb2/fb3), HP 15-fc | 8845HS, 240, AI 7 350 / 7x20U, 7x30U | не проверено | не проверено | — |
| **Dell** | | | | |
| Dell 15 DC15255 | 7530U/7730U (Barcelo R); 7320U/7520U (Mendocino) | **1 SO-DIMM DDR4 (одноканал)** или LPDDR5 onboard, до 16 | **нет** | [Owner's Manual](https://dl.dell.com/content/manual20023858-dell-15-dc15255-owner-s-manual.pdf?language=en-us) |
| **Dell 16 DC16255** | Ryzen 5 220 / 7 250 (Hawk Point) | 2× SO-DIMM DDR5-5600, «макс. 32»; 32 ГБ продаётся как 1×32 | да (2×16 самому) | [Setup & Specs](https://dl.dell.com/content/manual20191269-dell-16-dc16255-p-setup-and-specifications.pdf?language=en-us) |
| Dell 16 Plus DB16255 | AI 5 340 / AI 7 350 (Krackan) | распайка LPDDR5x-7500, 16/32 | распайка | [Owner's Manual](https://dl.dell.com/content/manual23366300-dell-16-plus-db16255-owner-s-manual.pdf?language=en-us) |
| **Dell Pro 16 PC16255** | 210/220, PRO 215–250, AI 5 PRO 340, AI 7 (PRO) 350 | 2× SO-DIMM, до 64; есть 2×16 и 1×32 | да | [Owner's Manual](https://dl.dell.com/content/manual33305221-dell-pro-16-pc16255-owner-s-manual.pdf?language=en-us) |
| Dell Pro 15 Essential PV15255 | 7320U / 7520U (Mendocino) | onboard LPDDR5, до 16 | **нет** | [Owner's Manual](https://dl.dell.com/content/manual33819502-dell-pro-15-essential-pv15255-owner-s-manual.pdf?language=en-us) |
| Dell Pro 16 Essential AMD | — | такой модели на dell.com не нашёл | — | — |
| Inspiron 15 3535 | 7x20U onboard; 7330U/7530U/7730U | 2× DDR4 SO-DIMM, **макс. 16** | **нет** | [Owner's Manual](https://dl.dell.com/content/manual32008171-inspiron-15-3535-owner-s-manual.pdf?language=en-us) |
| **Inspiron 16 5645** | Ryzen 5 8540U / 7 8840U (Hawk Point) | 2× SO-DIMM DDR5-5600, до 32, есть 2×16 | да | [Owner's Manual](https://dl.dell.com/content/manual18275235-inspiron-16-5645-owner-s-manual.pdf?language=en-us) |
| G15 5535 | 7x40HS (Phoenix) | не проверено | не проверено | — |
| **ASUS** | | | | |
| Vivobook 15 M1502 / 15 OLED M1505 / 15X M3504 / 16X M3604 | 7x30U, 5825U и др. (Barcelo R / Barcelo) | **8 DDR4 onboard + 1 SO-DIMM, до 16** | **нет** | [M1502](https://www.asus.com/Laptops/For-Home/Vivobook/vivobook-15-m1502/techspec/), [M1505](https://www.asus.com/Laptops/For-Home/Vivobook/ASUS-Vivobook-15-OLED-M1505/techspec/) |
| Vivobook 16 M1605 | 7x30U, 5x25U, 7940HS, 7640HS | 8 onboard + 1 SO-DIMM, до 16/24 | **нет** | [asus](https://www.asus.com/Laptops/For-Home/Vivobook/ASUS-Vivobook-16-OLED-M1605/techspec/) |
| **Vivobook 16 M1607** | AI 5 330/340, AI 7 350 (Krackan), AI 7 445 (Gorgon) | **16 DDR5 onboard + 1 SO-DIMM, до 32** | 16+слот | [asus](https://www.asus.com/Laptops/For-Home/Vivobook/ASUS-Vivobook-16-M1607/techspec/) |
| **Vivobook S16 M3607** | 220, 260, 270 (Hawk Point), AI 5 330, AI 7 350, AI 9 465 | 16 onboard + 1 SO-DIMM, до 32 | 16+слот | [asus](https://www.asus.com/Laptops/For-Home/Vivobook/ASUS-Vivobook-S16-M3607/techspec/) |
| Vivobook S16 OLED M5606 | 7535HS, 8x45HS, AI 9 HX 370/365, AI 7 350, AI 5 340 | LPDDR5X onboard 16/24/32 | распайка | [asus](https://www.asus.com/Laptops/For-Home/Vivobook/ASUS-Vivobook-S-16-OLED-M5606/techspec/) |
| Vivobook Go 15 E1504F | Athlon Gold 7220U, 7320U/7520U (Mendocino) | LPDDR5 onboard | **нет** | [asus](https://www.asus.com/Laptops/For-Home/Vivobook/Vivobook-Go-15-OLED-E1504F/techspec/) |
| Zenbook S16 UM5606; ProArt P16 H7606 | AI 9 365 / HX 370, AI 9 465 | распайка LPDDR5x | распайка | [NBC S16](https://www.notebookcheck.net/The-perfect-everyday-laptop-with-AMD-Ryzen-400-Asus-Zenbook-S16-OLED-review.1221965.0.html), [NBC P16](https://www.notebookcheck.net/4K-OLED-is-replaced-by-120-Hz-2-8K-OLED-Asus-ProArt-P16-with-RTX-5070-Laptop-review.1026301.0.html) |
| **ExpertBook P1 PM1503 / BM1 BM1503** (15,6") | 150/170 (Rembrandt), 7535HS/7735HS, 7x35U | 2× DDR5 SO-DIMM, до 64 | да, но CPU старый | [PM1503](https://www.asus.com/Laptops/For-Work/ExpertBook/ASUS-ExpertBook-P1-PM1503/techspec/), [BM1503](https://www.asus.com/Laptops/For-Work/ExpertBook/ASUS-ExpertBook-BM1-BM1503/techspec/) |
| **ExpertBook P3 PM3606** (16") | AI 5 330, AI 7 350 (Krackan) | 2× DDR5 SO-DIMM, до 64 | да | [asus](https://www.asus.com/Laptops/For-Work/ExpertBook/ASUS-ExpertBook-P3-PM3606/techspec/) |
| ExpertBook P3 G2 / B3 G2 / P5 G2 16 AMD (2026) | 260/8840HS; 210–260 + AI 4xx; AI 3xx/4xx | 2× DDR5 SO-DIMM, до 96 | да | [P3 G2](https://www.asus.com/Laptops/For-Work/ExpertBook/ASUS-ExpertBook-P3-G2-16-AMD/techspec/), [B3 G2](https://www.asus.com/Laptops/For-Work/ExpertBook/ASUS-ExpertBook-B3-G2-16-AMD/techspec/), [P5 G2](https://www.asus.com/Laptops/For-Work/ExpertBook/ASUS-ExpertBook-P5-G2-16-AMD/techspec/) |
| TUF A15 (2024) | 8845HS/8945H (Hawk Point) | 2× SO-DIMM, до 32 | да (+RTX) | [asus](https://www.asus.com/Laptops/For-Gaming/TUF-Gaming/ASUS-TUF-Gaming-A15-2024/techspec/) |
| TUF A16 (2025) | 253/260/270, 7845HX/8745HX/8940HX, AI 9 HX 370 | 2× SO-DIMM, до 64 | да (+RTX) | [asus](https://www.asus.com/Laptops/For-Gaming/TUF-Gaming/ASUS-TUF-Gaming-A16-2025/techspec/) |
| TUF A16 (2024) FA608 | AI 9 HX 370 | LPDDR5X onboard 16/32 | распайка | [asus](https://www.asus.com/Laptops/For-Gaming/TUF-Gaming/ASUS-TUF-Gaming-A16-2024-FA608/techspec/) |
| **Acer** | | | | |
| Aspire Go 15 AG15-42P | Ryzen 7 5825U (Barcelo) | DDR4, 1×8 с завода, «макс. 32» (слоты — не проверено) | CPU — ловушка | [Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&GTIN=4711474910431) |
| Extensa 15 AMD | 7430U / 7730U (Barcelo R) | не проверено | CPU — ловушка | — |
| Aspire 3 A315-24P | 7320U/7520U (Mendocino) | не проверено | CPU — ловушка | [NBC](https://www.notebookcheck.net/Acer-Aspire-3-Laptop-Review-An-affordable-Mendocino-offering-with-excellent-battery-life-and-a-sub-par-screen.704064.0.html) |
| Aspire 16 AI A16-61M | Ryzen AI 7 350 | LPDDR5x-8533 32, распайка | распайка | [Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&GTIN=4711474850324) |
| Swift Air 16 SFA16-61M | Ryzen AI 5 330 | LPDDR5 32, распайка | распайка | [Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&GTIN=4711474856227) |
| Swift Go 16 AI SFG16-61 | AI 5 PRO 340, AI 7 350 | LPDDR5x распайка | распайка | [Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&GTIN=4711474416001) |
| Nitro V 16 (AI) ANV16-41 / 42 | 8845HS / 240, 260 (Hawk Point) | 2× SO-DIMM (2×8), до 32 | да (+RTX) | [Icecat R860](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&GTIN=4711474531131), [NBC](https://www.notebookcheck.net/Acer-Nitro-V-16-AI-Review-Affordable-gaming-laptop-with-great-battery-life.1156010.0.html) |
| TravelMate AMD, Nitro V 15 ANV15-41, Nitro 16 AN16-4x | — | не проверено | не проверено | — |
| **MSI** | | | | |
| Venture A16 AI+ A3HMG | Ryzen AI 5 340 (Krackan) | 2× SO-DIMM (2×8), до 96 | да (замена обеих) | [Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&GTIN=4711377358880) |
| Katana A15 AI B8V | 8945HS | 2× SO-DIMM (2×8) | да (+RTX) | [NBC](https://www.notebookcheck.net/MSI-Katana-A15-AI-laptop-review-RTX-4070-gamer-hurt-by-cost-saving-measures.936689.0.html) |
| Prestige / Summit A16 AI+ | AI 9 365 | LPDDR5X распайка | распайка | [NBC Prestige](https://www.notebookcheck.net/MSI-Prestige-A16-AI-review-Multimedia-laptop-with-powerful-Ryzen-9-365.949210.0.html) |
| Modern 15 B7M, Bravo 15, Thin A15, Cyborg AMD | 7x30U / 7x35HS | не проверено | не проверено | — |
| **Прочие** | | | | |
| Medion Avantum 15 E1 | Ryzen 5 7430U (Barcelo R) | 2×16 DDR4 (Icecat) | память да, CPU — ловушка | [Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&GTIN=4061275237580) |
| Gigabyte GAMING A16 (3VH/3WH) | Ryzen 7 260 (Hawk Point) + RTX 5060/5070 | 2× SO-DIMM, 1×16, до 64 | 16+слот (+RTX) | [Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&GTIN=4719331766764) |
| Gigabyte Aero X16 | Ryzen AI 7 350 + RTX 5060/5070 | 2× SO-DIMM, до 64 | да (дорого) | [NBC](https://www.notebookcheck.net/Gigabyte-Aero-X16-Review-Sleek-AMD-Zen-5-gaming-machine-with-Nvidia-RTX-5070-Laptop-and-upgradeable-RAM.1022304.0.html) |
| Framework Laptop 16 | Ryzen AI 300 (AI 5 340, AI 7 350, AI 9 HX 370) | 2× DDR5 SO-DIMM, до 96 | да (дорого) | [frame.work](https://frame.work/de/en/laptop16) |
| Tuxedo InfinityBook Pro 15 Gen10 AMD | Ryzen AI 300 | 2× DDR5-5600 SO-DIMM, до 128 | да (цена не проверена) | [tuxedo](https://www.tuxedocomputers.com/de/TUXEDO-InfinityBook-Pro-15-Gen10-AMD.tuxedo) |
| XMG Core 15 / Core 16 / Core 16 VE (M25) | AI 7 350 / AI 9 HX 370 / Ryzen 7 255 | 2× SO-DIMM | да (от 1479 €) | NBC, см. ниже |
| Fujitsu, Samsung, Microsoft AMD 15–16" | — | в продаже в DE не нашёл | — | — |
| LG gram 15Z80T (2025) | Ryzen AI 7 350 | не проверено | не проверено | [NBC-сборник](https://www.notebookcheck.net/LG-gram-15Z80T-2025.1175186.0.html) |

## Карта кодовых имён (amd.com, поле «Former Codename»)

Нужна, чтобы читать таблицу выше. Полная карта — в `amd-cpu.md`.

| Имя в продаже | Кодовое имя | Ядра | iGPU | Источник |
|---|---|---|---|---|
| Ryzen 5 7520U, Ryzen 5 40, Ryzen 3 30 | Mendocino | Zen 2 | Radeon 610M | [7520U](https://www.amd.com/en/products/processors/laptop/ryzen/7000-series/amd-ryzen-5-7520u.html), [5 40](https://www.amd.com/en/products/processors/laptop/ryzen/10-series/amd-ryzen-5-40.html), [3 30](https://www.amd.com/en/products/processors/laptop/ryzen/10-series/amd-ryzen-3-30.html) |
| Ryzen 5 7430U / 7530U, Ryzen 7 7730U | Barcelo R | Zen 3 | «AMD Radeon Graphics» (у NBC — Vega 7/8) | [7430U](https://www.amd.com/en/products/processors/laptop/ryzen/7000-series/amd-ryzen-5-7430u.html), [7530U](https://www.amd.com/en/products/processors/laptop/ryzen/7000-series/amd-ryzen-5-7530u.html), [7730U](https://www.amd.com/en/products/processors/laptop/ryzen/7000-series/amd-ryzen-7-7730u.html) |
| Ryzen 5 7535HS, Ryzen 7 7735HS | Rembrandt R | Zen 3+ | 660M / 680M | [7535HS](https://www.amd.com/en/products/processors/laptop/ryzen/7000-series/amd-ryzen-5-7535hs.html), [7735HS](https://www.amd.com/en/products/processors/laptop/ryzen/7000-series/amd-ryzen-7-7735hs.html) |
| Ryzen 5 130 / 150, Ryzen 7 160 / 170 | Rembrandt | Zen 3+ | 660M / 680M | [130](https://www.amd.com/en/products/processors/laptop/ryzen/100-series/amd-ryzen-5-130.html), [150](https://www.amd.com/en/products/processors/laptop/ryzen/100-series/amd-ryzen-5-150.html), [160](https://www.amd.com/en/products/processors/laptop/ryzen/100-series/amd-ryzen-7-160.html), [170](https://www.amd.com/en/products/processors/laptop/ryzen/100-series/amd-ryzen-7-170.html) |
| Ryzen 3 210, 5 220, 5 230, 5 240, 7 250, 7 260; 5 8540U | Hawk Point | Zen 4 (у 210/220/8540U — Zen 4 + Zen 4c) | 740M / 760M / 780M | [210](https://www.amd.com/en/products/processors/laptop/ryzen/200-series/amd-ryzen-3-210.html), [220](https://www.amd.com/en/products/processors/laptop/ryzen/200-series/amd-ryzen-5-220.html), [230](https://www.amd.com/en/products/processors/laptop/ryzen/200-series/amd-ryzen-5-230.html), [240](https://www.amd.com/en/products/processors/laptop/ryzen/200-series/amd-ryzen-5-240.html), [250](https://www.amd.com/en/products/processors/laptop/ryzen/200-series/amd-ryzen-7-250.html), [260](https://www.amd.com/en/products/processors/laptop/ryzen/200-series/amd-ryzen-7-260.html), [8540U](https://www.amd.com/en/products/processors/laptop/ryzen/8000-series/amd-ryzen-5-8540u.html) |
| Ryzen AI 5 330 / 340, Ryzen AI 7 350 | Krackan Point | Zen 5 + Zen 5c | 820M / 840M / 860M | [330](https://www.amd.com/en/products/processors/laptop/ryzen/ai-300-series/amd-ryzen-ai-5-330.html), [340](https://www.amd.com/en/products/processors/laptop/ryzen/ai-300-series/amd-ryzen-ai-5-340.html), [350](https://www.amd.com/en/products/processors/laptop/ryzen/ai-300-series/amd-ryzen-ai-7-350.html) |
| Ryzen AI 5 430, Ryzen AI 7 445 / 450 | Gorgon Point | Zen 5 + Zen 5c | 840M / 860M | [430](https://www.amd.com/en/products/processors/laptop/ryzen/ai-400-series/amd-ryzen-ai-5-430.html), [445](https://www.amd.com/en/products/processors/laptop/ryzen/ai-400-series/amd-ryzen-ai-7-445.html), [450](https://www.amd.com/en/products/processors/laptop/ryzen/ai-400-series/amd-ryzen-ai-7-450.html) |

- Все перечисленные на amd.com — двухканальные: «Memory Channels 2».
- Ryzen 3 110, 5 216, 7 217, 7 253, 7 255, 5 224, 7 249 на amd.com не проверял. У NBC Ryzen 7 255 значится как «Hawk Point-H» ([NBC XMG Core 16 VE](https://www.notebookcheck.net/Challenge-to-the-Lenovo-Legion-XMG-Core-16-VE-M25-gaming-laptop-review.1202743.0.html)).
- Notebookcheck о Gorgon Point: «debuts with only minor improvements» ([NBC, 26.01.2026](https://www.notebookcheck.net/AMD-Ryzen-AI-400-Performance-Analysis-Gorgon-Point-debuts-with-only-minor-improvements.1211982.0.html)).

## Ловушки, найденные для AMD

1. **1×32 ГБ вместо 2×16.**
   - ThinkPad E16 Gen 3 AMD `21ST004GGE` и `21ST001YGE`: «Speicherlayout 1 x 32 GB» ([Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Lenovo&ProductCode=21ST004GGE)).
   - Dell 16 DC16255: среди конфигураций 32 ГБ только «1 x 32 GB … single-channel» ([Dell](https://dl.dell.com/content/manual20191269-dell-16-dc16255-p-setup-and-specifications.pdf?language=en-us)).
   - HP 255R G10: максимум указан как «32GB DDR5-4800 (1 x 32GB)» ([QuickSpecs](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09053765)).
2. **«8 ГБ распайки + 1 слот» — 2×16 не собрать.**
   - IdeaPad Slim 3 15/16 ARP10 и AHP10: «One memory soldered … one DDR5 SODIMM slot», «Up to 24GB» (PSREF, см. таблицу). Подтверждение по Icecat у `83K800CGGE`: «1x SO-DIMM», максимум 24 ГБ ([Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&GTIN=0199274450397)).
   - ASUS Vivobook 15/16 M1502, M1505, M1605, M3504, M3604 — «8GB DDR4 on board + SO-DIMM», максимум 16–24 ГБ.
   - Lenovo V15 G4 ABP — 8 + 8, максимум 16.
3. **Всего один слот или потолок 16 ГБ.**
   - Dell 15 DC15255: «SoDIMM slot», конфигурации только «single-channel», максимум 16 ГБ ([Dell](https://dl.dell.com/content/manual20023858-dell-15-dc15255-owner-s-manual.pdf?language=en-us)).
   - Inspiron 15 3535: два слота DDR4, но «Maximum memory configuration 16 GB» ([Dell](https://dl.dell.com/content/manual32008171-inspiron-15-3535-owner-s-manual.pdf?language=en-us)).
4. **Mendocino (Zen 2, 610M) под новыми именами.** Ryzen 5 40 / Ryzen 3 30 / Athlon Silver 10 стоят в Lenovo V15 G6 AMN ([PSREF](https://psref.lenovo.com/syspool/Sys/PDF/Lenovo/Lenovo_V15_G6_AMN/Lenovo_V15_G6_AMN_Spec.PDF)) и HP OmniBook 3 16-by0655ng (649,83 €, [billiger](https://www.billiger.de/pricelist/5734811234-hp-omnibook-3-16-by0655n)). Везде только распайка.
5. **32 ГБ на старом Barcelo R (Zen 3, графика уровня Vega).**
   - Medion Avantum 15 E1 (7430U, 2×16 DDR4) — 719,99 €;
   - Acer Extensa 15 (7430U/7730U, 32 ГБ) — 879–889 €;
   - Acer Aspire Go 15 (5825U, 32 ГБ) — 799 €.
   Цены — billiger.de, 30.09.2026, см. «Кандидаты». У «Aspire Go 15 … 32 GB» EAN начинается на 426 (немецкий префикс GS1), а у SKU от Acer — на 4711/4710 ([Icecat Acer](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&GTIN=4711474910431)). Скорее всего, это сборка магазина («aufgerüstet») — вывод по EAN, не проверено.
6. **Rembrandt (Zen 3+, 2022) под «новыми» именами Ryzen 5 150 / 7 170** — в новых моделях 2025 года: V15 G6 ARP, IdeaPad Slim 3 ARP10, ThinkBook 16 G7 ARP, ExpertBook P1/BM1, LOQ 15ARP10E.
7. **HEVC выключен у HP AMD** в ProBook 465 G11, EliteBook 665 G11, ProBook 4 G1a 16 и EliteBook 6 G1a 16: «Hardware acceleration for CODEC H.265/HEVC … is disabled on this platform». У EliteBook 8 G1a 16 — «HEVC (H.265) CODEC is supported» (QuickSpecs, см. раздел HP). Для Dell — политика «HEVC только в части конфигураций», см. [`hevc-audit.md`](../../Intel/notes/hevc-audit.md).
8. **HP: слоты «customer non-accessible».**
   - HP 255 G10 и 255R G10: «All slots are … non-accessible / non-upgradeable» ([255 G10](https://www8.hp.com/h20195/V2/GetPDF.aspx/c08479497), [255R G10](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09053765)).
   - OmniBook 3 16 (2026): «Memory is not accessible or upgradeable» ([MSG](https://kaas.hpcloud.hp.com/pdf-public/pdf_13159558_en-US-1.pdf)).
   Докупать планку туда рискованно: гарантия и доступ к слотам — не проверено.
9. **Одноканал в тестах и в продаже.** Notebookcheck записывает его в минусы:
   - LOQ 15AHP10 — «single-channel RAM» ([NBC](https://www.notebookcheck.net/Lenovo-LOQ-15-laptop-review-The-mobile-RTX-5060-celebrates-its-debut.1050248.0.html));
   - HP Omen 16 (8940HX) — «Single-channel RAM» ([NBC](https://www.notebookcheck.net/The-best-budget-gamer-HP-Omen-16-laptop-review.1135455.0.html));
   - ExpertBook PM3 — «only with single-channel RAM in the test device» ([NBC](https://www.notebookcheck.net/Asus-ExpertBook-PM3-Review-Office-laptop-with-AMD-long-battery-life-and-Copilot.1200511.0.html));
   - EliteBook 865 G10 ([NBC](https://www.notebookcheck.net/HP-EliteBook-865-G10-laptop-review-Capable-business-laptop-ruined-by-Sure-View.809651.0.html)).
   С одной планкой пришли и ThinkPad T16 Gen 5 AMD, ExpertBook PM5 G2, Dynabook Tecra A65-M (ссылки в разделах брендов).
10. **16 ГБ «2×8» — не путь «16 + слот».** Добрать до 32 ГБ здесь можно только заменой обеих планок. Касается IdeaPad Slim 5 16AGP11 `83S2003GGE` / `83S2000BGE` ([Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&GTIN=0199274450946)), MSI Venture A16 AI+, Acer Nitro V 16 AI.
11. **«Up to 32 GB offering»** у IdeaPad Slim 5 16, LOQ и Legion 5 — это то, что продаёт Lenovo, а не технический предел (PSREF, сноска «test results with current Lenovo memory offerings»). 2×16 укладываются в любом случае.
12. **Потребительские AMD часто без USB4 и с HDMI 1.4.**
    - Dell 16 DC16255: HDMI 1.4, USB-C 10 Gbps.
    - Dell Pro 15 Essential: HDMI 1.4 «1920 x 1080 at 60 Hz».
    - ExpertBook P1: «HDMI 1.4, up to 3840x2160p/30Hz».
    - IdeaPad Vibe 15AKP12: HDMI 1.4, USB-C 5 Gbps.
    Для 4K-монитора остаются USB-C/DP (даташиты в таблице).

## Бренды

### Lenovo — ThinkPad, ThinkBook, IdeaPad, V, Yoga, LOQ/Legion

Общее (запчасти, FRU, гарантия, сервис) — в [`brands.md` → Lenovo](../../Intel/notes/brands.md). Для AMD дополнительно:

**ThinkPad E16 AMD**
- **Gen 2 AMD (2024).** Rembrandt R/Rembrandt, 2× SO-DIMM, 2× M.2 (2242 + 2280), HDMI 2.1, **без USB4**, гарантия 1 год ([PSREF](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_E16_Gen_2_AMD/ThinkPad_E16_Gen_2_AMD_Spec.PDF)).
  - Notebookcheck (21M5002VGE, 7535HS, 2×16, 935 €, 11.10.2024): тихий, прочный, свободный слот SSD; минусы — слабый экран и «no USB4» ([NBC](https://www.notebookcheck.net/Lenovo-ThinkPad-E16-Gen-2-AMD-laptop-review-Cuts-corners-mostly-in-the-right-places.899320.0.html)).
- **Gen 3 AMD (2025).** Hawk Point, 2× SO-DIMM (64 ГБ — «special bid only»), 2× M.2, **1× USB4 40 Gbps** + 1× USB-C 5 Gbps, RJ45, без кардридера, 1 год ([PSREF](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_E16_Gen_3_AMD/ThinkPad_E16_Gen_3_AMD_Spec.PDF)).
  - SKU с 32 ГБ — одной планкой (см. «Ловушки»).
- **Gen 4 AMD (05/2026).** Krackan/Gorgon, 2× SO-DIMM, **2× USB4** ([PSREF](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_E16_Gen_4_AMD/ThinkPad_E16_Gen_4_AMD_Spec.PDF)). С 32/1 ТБ — от 1326 € (`21Y4006CGE`, AI 5 330; [billiger](https://www.billiger.de/pricelist/5745884576-lenovo-thinkpad-e16-g4-amd-ryzen-), 30.09.2026), то есть выше потолка.
- **AMD против Intel той же модели.**
  - E16 Gen 3 Intel: «USB-C (Thunderbolt 4 / USB4 40Gbps)» ([PSREF](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_E16_Gen_3_Intel/ThinkPad_E16_Gen_3_Intel_Spec.PDF)); у AMD — USB4 без сертификации TB.
  - E16 Gen 4 Intel: 2× Thunderbolt 4 ([PSREF](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_E16_Gen_4_Intel/ThinkPad_E16_Gen_4_Intel_Spec.PDF)); у AMD — 2× USB4.
  - У Intel Gen 4 на Wildcat Lake только один слот. AMD Gen 4 такой ловушки не имеет — оба слота во всех CPU (PSREF).

**ThinkPad L16 / T16 / P16s AMD**
- **L16 Gen 2 AMD (2025).** 2× SO-DIMM, один M.2 2280, «2x USB-C (Thunderbolt 4 / USB4 40Gbps)» — AMD-порты с сертификацией TB4 ([PSREF](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_L16_Gen_2_AMD/ThinkPad_L16_Gen_2_AMD_Spec.PDF)).
  - Notebookcheck (21SC0029GE, PRO 215, 2×16, 1090 €, 22.02.2026): «highly repairable», «32 GB RAM for relatively low price»; минусы — батарея, цвета экрана, 12 мес. гарантии у тестового ([NBC](https://www.notebookcheck.net/This-affordable-laptop-has-32-GB-RAM-for-cheap-Lenovo-ThinkPad-L16-Gen-2-AMD-review.1144661.0.html)).
  - Сейчас с 32/1 ТБ — от 1232 € (`21SC002AGE`, [billiger](https://www.billiger.de/pricelist/5328062804-lenovo-thinkpad-l16-g2-amd-), 30.09.2026).
- **L16 Gen 3 AMD (2026).** Gorgon, 2× SO-DIMM, 2× TB4 ([PSREF](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_L16_Gen_3_AMD/ThinkPad_L16_Gen_3_AMD_Spec.PDF)). От 1535 € (`21XC002DGE`, [billiger](https://www.billiger.de/pricelist/5747737347-lenovo-thinkpad-l1), 30.09.2026).
- **L16 Gen 1 AMD** (7x35U PRO): NBC — 2×16, USB4, вентиляторы шумноваты ([NBC, 16.10.2024](https://www.notebookcheck.net/Lenovo-ThinkPad-L16-Gen-1-AMD-laptop-review-Powerful-hardware-in-a-modest-guise.901298.0.html)). Модель снята с производства (PSREF Withdraw).
- **T16 Gen 4 AMD.** 2× SO-DIMM, 2× TB4, один M.2 ([PSREF](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_T16_Gen_4_AMD/ThinkPad_T16_Gen_4_AMD_Spec.PDF)). NBC: горячий под нагрузкой, один слот SSD, 1349 € (студенческая цена, 21.11.2025) ([NBC](https://www.notebookcheck.net/Large-business-laptop-with-AMD-Ryzen-Pro-impresses-Lenovo-ThinkPad-T16-Gen-4-review.1167534.0.html)).
- **T16 Gen 5 AMD.** Hawk Point или Gorgon; с Gorgon — до 96 ГБ ([PSREF](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_T16_Gen_5_AMD/ThinkPad_T16_Gen_5_AMD_Spec.PDF)). NBC (22AN001WGE, PRO 215, 16 ГБ single-channel, 1640 €): «budget IPS screen with 60 % sRGB», «old CPU architecture» ([NBC, 10.06.2026](https://www.notebookcheck.net/Premium-business-laptop-with-a-budget-display-Lenovo-ThinkPad-T16-Gen-5-AMD-Review.1307940.0.html)).
- **T16 Gen 2 AMD** — распайка LPDDR5x ([PSREF](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_T16_Gen_2_AMD/ThinkPad_T16_Gen_2_AMD_Spec.PDF)).
- **P16s Gen 4 AMD.** 2× SO-DIMM до 96 ГБ ([PSREF](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_P16s_Gen_4_AMD/ThinkPad_P16s_Gen_4_AMD_Spec.PDF)). NBC: «highly upgradeable», громкий и горячий, нет SD ([NBC, 17.12.2025](https://www.notebookcheck.net/This-is-the-most-powerful-16-inch-AMD-ThinkPad-laptop-Lenovo-ThinkPad-P16s-Gen-4-review-with-Ryzen-AI-9-HX.1135080.0.html)).
- **P16s Gen 5 AMD** — один разъём LPCAMM2 (двухканальный). Установленная LPDDR5X-8533 работает на 7500 ([PSREF](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_P16s_Gen_5_AMD/ThinkPad_P16s_Gen_5_AMD_Spec.PDF)).
- Все эти ThinkPad выходят за 1100 €, кроме L16 Gen 2 в редкие моменты.

**ThinkBook 16 AMD**
- **G7 ARP (2024)** — главный AMD-кандидат по памяти ([PSREF](https://psref.lenovo.com/syspool/Sys/PDF/ThinkBook/ThinkBook_16_G7_ARP/ThinkBook_16_G7_ARP_Spec.PDF)):
  - 2× DDR5-4800 SO-DIMM, 2× M.2 2280 PCIe 4.0;
  - 1× USB4 40 Gbps + 1× USB-C 10 Gbps, HDMI 2.1, полноразмерный SD, RJ45;
  - экран WUXGA IPS 300 нит: 45 % NTSC или 100 % sRGB;
  - батарея 45 или 71 Втч, гарантия 1 или 2 года.
  - У `21MW00AYGE` и `21MW007VGE`: 2×16, панель 300 нит «NTSC» (то есть 45 %), батарея 45 Втч ([Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Lenovo&ProductCode=21MW007VGE)).
  - Процессор — Rembrandt R (Zen 3+, 2022).
  - Отдельного теста NBC нет, только сборник внешних обзоров ([NBC](https://www.notebookcheck.net/Lenovo-ThinkBook-16-G7-ARP.1187767.0.html), 17.12.2025).
- **G9 AHP (11/2025)** ([PSREF](https://psref.lenovo.com/syspool/Sys/PDF/ThinkBook/ThinkBook_16_G9_AHP/ThinkBook_16_G9_AHP_Spec.PDF), редакция 17.09.2026):
  - Hawk Point, 2× DDR5-5600 SO-DIMM;
  - **2× USB4**, HDMI 2.1, SD, RJ45;
  - экраны: WUXGA 400 нит 45 % NTSC 60 Гц, WUXGA 100 % sRGB 120 Гц, WQXGA 100 % 120 Гц;
  - батарея 48 или 71 Втч, гарантия 1 или 2 года.
  - У `21UT004QGE` и `21UT000RGE`: 2×16, 400 нит «NTSC», 60 Гц, 48 Втч ([Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Lenovo&ProductCode=21UT000RGE)).
  - Тестов NBC нет — не проверено.
- **G6 ABP** — Barcelo R + DDR4 (NBC: «inexpensive multimedia laptop», 749 €, 28.11.2023, [NBC](https://www.notebookcheck.net/Lenovo-ThinkBook-16-G6-review-The-inexpensive-multimedia-laptop-with-a-Ryzen-7000.774481.0.html)). Снят с производства.
- **G7+ ASP** — распайка 32 ГБ, снят с производства ([PSREF](https://psref.lenovo.com/syspool/Sys/PDF/ThinkBook/ThinkBook_16_G7plus_ASP/ThinkBook_16_G7plus_ASP_Spec.PDF)).
- **G8 на AMD в PSREF нет.** Поиск PSREF по «ThinkBook 16 G8 A…» выдаёт только G6/G7/G9 AMD.
- AMD против Intel: у ThinkBook 16 G8 IAL (Intel) тоже 2× SO-DIMM ([`brands.md`](../../Intel/notes/brands.md)). Порты TB у Intel-версии в этой сессии не сверял.

**IdeaPad Slim 5 16 AMD (2× SO-DIMM) и Slim 3 (ловушка)**
- **Slim 5 16AKP10** ([PSREF](https://psref.lenovo.com/syspool/Sys/PDF/IdeaPad/IdeaPad_Slim_5_16AKP10/IdeaPad_Slim_5_16AKP10_Spec.PDF)):
  - 2× SO-DIMM;
  - второй M.2 — только у моделей с AI 5 340 / AI 7 350;
  - 2× USB-C 10 Gbps (**USB4 нет**), HDMI 2.1, microSD;
  - гарантия 1, 2 или 3 года.
  - NBC (AI 5 330, 2×8, от ~700 € в Cyberport, 21.11.2025): «Radeon 820M is very slow», «small colour gamut», «high latencies»; 24 мес. гарантии у тестового ([NBC](https://www.notebookcheck.net/Dual-debut-in-the-Lenovo-IdeaPad-Slim-5-16-Ryzen-AI-5-330-and-Radeon-820M-in-review.1166676.0.html)).
- **Slim 5 16AHP11 (Hawk Point) и 16AGP11 (Gorgon)** — тоже 2× SO-DIMM, USB-C 10 Gbps. У AGP11 второй M.2 — только с AI 7 450 ([AHP11](https://psref.lenovo.com/syspool/Sys/PDF/IdeaPad/IdeaPad_Slim_5_16AHP11/IdeaPad_Slim_5_16AHP11_Spec.PDF), [AGP11](https://psref.lenovo.com/syspool/Sys/PDF/IdeaPad/IdeaPad_Slim_5_16AGP11/IdeaPad_Slim_5_16AGP11_Spec.PDF)).
  - В DE: `83S2003GGE` (AI 5 430, 16/1 ТБ, **2×8**, OLED 300 нит DCI-P3, 60 Втч) — 849 € (coolblue).
  - `83S2000BGE` (AI 7 445, 16/1 ТБ, 2×8) — 889 € (Galaxus).
  - Источники: [Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&GTIN=0199274450946), [billiger](https://www.billiger.de/pricelist/5669521610-lenovo-ideapad-slim-5-16-amd-ryzen-ai-5-4), 30.09.2026.
  - Замена на 2×16 обойдётся дорого (комплект — см. `market.md` в Intel).
- **Slim 5 15ARP10 (15,3")** — распайка. NBC: «RAM is soldered on», «no USB 4», экран 100 % sRGB ([NBC, 12.01.2025](https://www.notebookcheck.net/Lenovo-IdeaPad-Slim-5-15-laptop-review-Great-value-for-money-with-an-AMD-SoC-and-an-aluminum-case.945877.0.html)).
- **AMD против Intel.** Лучший Intel-кандидат из `REPORT.md` — IdeaPad Slim 5 16IRH10 `83HS00BLGE` (2×16, ~995 €). У AMD-сестёр 16AKP10/AHP11/AGP11 тоже 2× SO-DIMM, но AMD-SKU с 32/1 ТБ на billiger не нашёл — только 16 ГБ (2×8).
- **Slim 3 15/16 ARP10/AHP10** — «8 + слот», максимум 24 ГБ (см. «Ловушки»). **Slim 3 15AMN8/ABR8** — только распайка.
- **IdeaPad Vibe 15AKP12** (в PSREF с 28.09.2026) ([PSREF](https://psref.lenovo.com/syspool/Sys/PDF/IdeaPad/IdeaPad_Vibe_15AKP12/IdeaPad_Vibe_15AKP12_Spec.PDF)):
  - 2× SO-DIMM (до 32 offering), 2× M.2 2242;
  - порты слабые: HDMI 1.4, USB-C 5 Gbps с DP 1.2.
  - Цены в DE — не проверено.

**IdeaPad Pro 5, Yoga, IdeaPad 5 2-in-1** — только распайка (таблица).
- Yoga 7 2-in-1 16AGP11, NBC: «does not support M.2 2280 SSDs», «no Thunderbolt support», «refresh lags behind Intel» ([NBC, 27.03.2026](https://www.notebookcheck.net/Lenovo-Yoga-7-2-in-1-16AGP11-review-Latest-AMD-Ryzen-AI-7-refresh-lags-behind-Intel.1257880.0.html)).
- Исключение — 15,3-дюймовый IdeaPad 5 2-in-1 15AGP11: у него 2× SODIMM и 2× SSD ([NBC, 14.04.2026](https://www.notebookcheck.net/Lenovo-IdeaPad-5-2-in-1-15-review-Ryzen-AI-5-430-performance-debut.1270312.0.html)). С 32/1 ТБ — от 1267,07 € (`83UM002BGE`, [billiger](https://www.billiger.de/pricelist/5781548420-lenovo-ideap), 30.09.2026).

**Lenovo V15 AMD**
- **G6 ARP** — Rembrandt (Ryzen 3 110 / 5 150 / 7 170) ([PSREF](https://psref.lenovo.com/syspool/Sys/PDF/Lenovo/Lenovo_V15_G6_ARP/Lenovo_V15_G6_ARP_Spec.PDF)):
  - 2× SO-DIMM;
  - HDMI 1.4b, USB-C 10 Gbps с DP 1.2;
  - гарантия 1 или 2 года.
- **AMN** (Mendocino) и **G4 ABP** — ловушки.
- **V16 на AMD в PSREF не нашёл** (поиск «V16 G…» выдал только V15).

**LOQ / Legion 5 AMD** (все с 2× SO-DIMM и RTX; дороже 1100 € при 16 ГБ и выше)
- **LOQ 15AHP10** (220/250) ([PSREF](https://psref.lenovo.com/syspool/Sys/PDF/LOQ/LOQ_15AHP10/LOQ_15AHP10_Spec.PDF)):
  - USB4 нет: USB-C 10 Gbps;
  - HDMI 2.1;
  - гарантия 1, 2 или 3 года.
  - NBC: одна планка (одноканал), троттлинг SSD под длительной нагрузкой ([NBC, 04.07.2025](https://www.notebookcheck.net/Lenovo-LOQ-15-laptop-review-The-mobile-RTX-5060-celebrates-its-debut.1050248.0.html)).
- **LOQ 15AHP11:** USB4 есть ([PSREF](https://psref.lenovo.com/syspool/Sys/PDF/LOQ/LOQ_15AHP11/LOQ_15AHP11_Spec.PDF)). NBC: «occasional SSD throttling», от ~1500 € (Galaxus, 11.07.2026) ([NBC](https://www.notebookcheck.net/Eyesore-or-eye-catcher-Lenovo-LOQ-15-gaming-laptop-review.1338691.0.html)).
- **LOQ 15ARP10E:** «Up to 16GB … offering», USB-C 5 Gbps ([PSREF](https://psref.lenovo.com/syspool/Sys/PDF/LOQ/LOQ_15ARP10E/LOQ_15ARP10E_Spec.PDF)).
- **Legion 5 15AHP10** (Ryzen 7 260): 2 слота, USB4, «PWM flickering», 1449 € ([NBC, 01.07.2025](https://www.notebookcheck.net/The-best-mainstream-gamer-in-2025-Lenovo-Legion-5-15-Laptop-Review.1047975.0.html)).
- **Legion 5 15AGP11** (AI 7 450): 2×16 SO-DIMM, OLED с ШИМ, 1899 € в ok1.de только для студентов ([NBC, 14.07.2026](https://www.notebookcheck.net/OLED-AMD-gamer-with-32-GB-RAM-Lenovo-Legion-5-15AGP11-laptop-review.1333407.0.html)).
- На billiger LOQ 15 AMD с RTX 5060 — от 1309 € ([billiger](https://www.billiger.de/pricelist/5927717905-lenovo-loq-15-amd-ryzen-7-250-8-gb-ram-1-tb-ssd-), 30.09.2026).

**Вердикт Lenovo (AMD).**
- Сейчас реальны только ThinkBook 16 G7 ARP / G9 AHP с заводскими 2×16 (≤ 1100 €).
- ThinkPad E16 Gen 3 AMD — только если найдётся SKU 2×16. Иначе цена второй планки ломает бюджет: 1×32 плюс ещё 1×32 — не наш вариант.
- IdeaPad Slim 5 16 AMD — хорошая платформа, но продаётся 2×8.

### HP — ProBook/EliteBook (G11, G1a), HP 255, OmniBook, Pavilion/Envy, Victus

Общее — в [`brands.md` → HP](../../Intel/notes/brands.md). Для AMD дополнительно:

**Бизнес (QuickSpecs, скачаны 30.09.2026)**
- **ProBook 4 G1a 16** (v15 от 16.06.2026) ([QuickSpecs](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09111176)):
  - Ryzen 3 210, 5 220, 5 230, 7 250, 7 250H, 7 255H;
  - «2 SODIMM», «Supports Dual Channel Memory»;
  - **HEVC выключен**;
  - аккумулятор «not replaceable by customer»;
  - запчасти «up to 5 years», гарантия 1 год («options depending on country»).
- **EliteBook 6 G1a 16** (v17 от 15.09.2026) ([QuickSpecs](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09111179)):
  - Ryzen 3 210 … 7 PRO 250, 7 255H;
  - 2 SODIMM;
  - **HEVC выключен**;
  - «2 x Thunderbolt 4 with USB Type-C 40Gbps».
- **EliteBook 8 G1a 16:**
  - c09120200 (v21 от 11.09.2026): Ryzen 5 224/230, 7 249/250 (+PRO), «2 SODIMM», «Dual Channel Memory (optional)», **«HEVC (H.265) CODEC is supported»**, Thunderbolt 4 ([QuickSpecs](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09120200)).
  - c09120201 (v19 от 02.09.2026): Ryzen AI 5/7 (PRO) 340/350, HEVC тоже есть ([QuickSpecs](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09120201)).
  - NBC (AI 7 PRO 350): 32 ГБ в двухканале, тихий; минусы — «DPC latency issues» (важно для звука при монтаже), только 1200p 60 Гц, 36 мес. гарантии (США) ([NBC, 09.09.2025](https://www.notebookcheck.net/HP-EliteBook-8-G1a-16-AI-laptop-review-Redesigned-inside-and-out.1103659.0.html)).
- **ProBook 465 G11 / EliteBook 665 G11** (Rembrandt R): 2 SODIMM, HEVC выключен ([465](https://www8.hp.com/h20195/V2/GetPDF.aspx/c08908497), [665](https://www8.hp.com/h20195/V2/GetPDF.aspx/c08927104)). У 665 G11 — «2 USB4 Type-C 40 Gbps».
- **EliteBook 8 G2a 16 (2026)** — распайка LPDDR5-7500 32 ГБ, «loud fans under load», ~1960 $ ([NBC, 21.09.2026](https://www.notebookcheck.net/Surprisingly-fast-with-32-GB-RAM-and-Ryzen-7-HP-EliteBook-8-G2a-16-laptop-review.1358548.0.html)).
- **AMD против Intel.**
  - ProBook 4 G1i и EliteBook 6 G1i (Intel) — тоже HEVC выключен.
  - EliteBook 8 G1i — HEVC есть ([`hevc-audit.md`](../../Intel/notes/hevc-audit.md)). То есть у HP разница не AMD/Intel, а «серия 4/6 против серии 8».
  - У AMD G1a порты TB4 сертифицированы так же, как у Intel (QuickSpecs 6/8 G1a).

**Бюджетные HP 255**
- **255 G10** (v12 от 07.05.2025) ([QuickSpecs](https://www8.hp.com/h20195/V2/GetPDF.aspx/c08479497)):
  - Barcelo R: «2 SODIMM (BCL-R only)», DDR4-3200, до 32 ГБ;
  - Mendocino: «4GB/8GB LPDDR5-5500 (onboard)»;
  - «All slots are non-accessible / non-upgradeable».
  - NBC (C07Q0ES, Athlon Silver 7120U, 8 ГБ LPDDR5, 482 €, 12 мес.): «Small budget, low performance» ([NBC, 10.05.2026](https://www.notebookcheck.net/HP-255-G10-with-7120U-review-Small-budget-low-performance.1293092.0.html)).
- **255R G10** (v7 от 06.03.2026) ([QuickSpecs](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09053765)):
  - Rembrandt R 7335U/7535U/7735U: «2 SODIMM (RMB-UR only)», DDR5-4800;
  - «customer non-accessible».
  - В DE: CU0R4ES (R5 7535U, 16/512) — 444 € ([billiger](https://www.billiger.de/pricelist/5724552928-hp-255r-g10-15-6-amd-ryzen-5-7535u-16-g), 30.09.2026).
- **255 G11** на billiger не нашёл — не проверено. HEVC в QuickSpecs 255 G10 и 255R G10 не упоминается — статус не проверено (см. `hevc-amd.md`).

**Потребительские HP**
- **OmniBook 3 16 (AMD 16-by0xxx, 2026)** ([MSG, 2-я редакция 06/2026](https://kaas.hpcloud.hp.com/pdf-public/pdf_13159558_en-US-1.pdf)):
  - в MSG: «Memory is not accessible or upgradeable»;
  - при этом есть процедура «Memory modules (select products only)»;
  - HDMI 1.4b — только у Intel Core, у AMD — HDMI 2.1 (по той же таблице — не проверено).
  - С 32/1 ТБ: `16-bv0074ng` (AI 7 445) — от 1130,23 € ([billiger](https://www.billiger.de/pricelist/5696995909-hp-omnibook-3-ngai-16-bv0074ng-amd-ryzen-ai-7-445-32-gb-ram-1-tb-ssd-win11-home), 30.09.2026). Раскладка — не проверено.
- **OmniBook 5 16 Next Gen (AMD 16-bp0xxx)** — «LPDDR», 16 или 32 ГБ одним модулем → распайка ([MSG](https://kaas.hpcloud.hp.com/pdf-public/pdf_13052194_en-US-1.pdf)).
- **Pavilion 16-ag0057ng** (8540U): «soldered RAM», «single M.2 slot», 12 мес., ~730 € ([NBC, 11.02.2025](https://www.notebookcheck.net/HP-Pavilion-16-review-Budget-AMD-CPU-in-a-stylish-laptop.959151.0.html)).
- **Envy x360 16 (8840HS):** распайка; «no Thunderbolt or USB4 support on AMD SKUs» — прямое отличие AMD от Intel ([NBC, 22.05.2024](https://www.notebookcheck.net/HP-Envy-x360-2-in-1-16-review-Ryzen-7-8840HS-beats-Core-Ultra-7-155U.837856.0.html)).
- **Victus 16 (16-s0xxx, Phoenix):** «Two SODIMM slots, dual-channel», 32 ГБ = 16×2 ([MSG](https://kaas.hpcloud.hp.com/pdf-public/pdf_7911438_en-US-1.pdf)).
  - Victus 15 AMD (15-fb2/fb3) — не проверено. NBC тестировал Intel-версию 15-fa2: два слота, один пустой ([NBC](https://www.notebookcheck.net/A-budget-gamer-for-1-200-HP-Victus-15-RTX-5050-laptop-review.1147790.0.html)).
- **Omen 16 (8940HX)**, NBC: 1×16 (одноканал), нет USB4/TB/SD, 999 € в notebooksbilliger ([NBC, 13.10.2025](https://www.notebookcheck.net/The-best-budget-gamer-HP-Omen-16-laptop-review.1135455.0.html)).
- **HP 15-fc** (AMD 15,6") — раскладку не проверял.

**Вердикт HP (AMD).**
- ProBook 4 G1a 16 — дёшево и 2 слота, но без аппаратного HEVC; для монтажа это минус (см. `amd-codecs.md`).
- EliteBook 8 G1a 16 — правильная модель с HEVC, но дороже потолка.
- Потребительские HP — распайка или «non-accessible».

### Dell — Dell 15/16, Dell 16 Plus, Dell Pro 16, Inspiron, G15

Общее — в [`brands.md` → Dell](../../Intel/notes/brands.md). Для AMD дополнительно (все PDF — dl.dell.com, 07–09.2026):
- **Dell 16 DC16255** (Rev. A01, PDF от 01.09.2026) ([Setup & Specs](https://dl.dell.com/content/manual20191269-dell-16-dc16255-p-setup-and-specifications.pdf?language=en-us)):
  - Ryzen 5 220 (740M) / Ryzen 7 250 (780M);
  - «Two SODIMM slots», DDR5-5600, «Maximum memory configuration 32 GB»;
  - в списке конфигураций 32 ГБ только «1 x 32 GB … single-channel»;
  - один M.2 **2230**;
  - HDMI 1.4, USB-C 10 Gbps с DP 1.4;
  - 1,89–2,14 кг.
  - AMD против Intel: у Dell 16 DC16250 (Intel) на dell.de базовая конфигурация 2×8 ([`brands.md`](../../Intel/notes/brands.md)).
- **Dell 15 DC15255** — ловушка: 1 слот / onboard, максимум 16 ГБ ([Owner's Manual, 19.08.2026](https://dl.dell.com/content/manual20023858-dell-15-dc15255-owner-s-manual.pdf?language=en-us)).
- **Dell 16 Plus DB16255** (AI 5 340 / AI 7 350): «Onboard», LPDDR5x-7500, 16 или 32 ГБ, HDMI 1.4 ([Owner's Manual, 20.09.2026](https://dl.dell.com/content/manual23366300-dell-16-plus-db16255-owner-s-manual.pdf?language=en-us)).
- **Dell Pro 16 PC16255** ([Owner's Manual, 08.07.2026](https://dl.dell.com/content/manual33305221-dell-pro-16-pc16255-owner-s-manual.pdf?language=en-us)):
  - «Two SODIMM slots», до 64 ГБ;
  - в конфигурациях есть и «2 x 16 GB … dual-channel», и «1 x 32 GB … single-channel»;
  - 2× «USB 40 Gbps» с DP (DP 2.1 у Ryzen AI 300, DP 1.4a у Ryzen 200), HDMI 2.1;
  - SSD M.2 2230.
  - AMD против Intel: у Intel PC16250 — Thunderbolt 4 ([`hevc-audit.md`](../../Intel/notes/hevc-audit.md), брошюра Dell Pro 14/16); у AMD в мануале — «USB 40 Gbps».
  - HEVC у Dell Pro 14/16: воспроизведение — только в части конфигураций (сноска брошюры, см. [`hevc-audit.md`](../../Intel/notes/hevc-audit.md)). Для PC16255 отдельно — не проверено.
  - Цены AMD-версии в DE — не проверено.
- **Dell Pro 5 16 P516265** (HX PRO 470): «removable DDR5 SODIMM modules», «does not support full-length M.2 2280», «CAMM options only for Intel SKUs», от ~2000 $ ([NBC, 31.07.2026](https://www.notebookcheck.net/Dell-Pro-5-16-P516265-review-Traditional-and-reliable.1342884.0.html)).
- **Dell Pro 15 Essential PV15255** — Mendocino, onboard, максимум 16; HDMI 1.4 до 1080p60 ([Owner's Manual, 03.09.2026](https://dl.dell.com/content/manual33819502-dell-pro-15-essential-pv15255-owner-s-manual.pdf?language=en-us)).
- **Dell Pro 16 Essential на AMD** (PV16255) на dell.com не нашёл — страница поддержки пустая.
- **Inspiron 16 5645** (Ryzen 5 8540U / 7 8840U) ([Owner's Manual, 14.08.2026](https://dl.dell.com/content/manual18275235-inspiron-16-5645-owner-s-manual.pdf?language=en-us)):
  - 2× SO-DIMM, «32 GB: 2 x 16 GB … dual-channel» есть в списке;
  - HDMI 1.4, USB-C 10 Gbps.
  - Цены в DE — не проверено.
- **Inspiron 15 3535** — максимум 16 ГБ ([Owner's Manual](https://dl.dell.com/content/manual32008171-inspiron-15-3535-owner-s-manual.pdf?language=en-us)).
- **G15 5535** — не проверено. **Alienware 15 DA15265 (2026, Ryzen 7 260)** есть в сборнике NBC ([NBC](https://www.notebookcheck.net/Alienware-15-DA15265-2026-Reviews-and-Specs.1403282.0.html)); раскладка — не проверено.
- **Вердикт Dell (AMD).**
  - Dell 16 DC16255 и Dell Pro 16 PC16255 — годные платформы; у DC16255 память и SSD 2230 надо брать самим (32 ГБ продаётся 1×32).
  - Dell 15, Inspiron 15 3535, Dell Pro 15 Essential — нет.

### ASUS — Vivobook, ExpertBook, TUF, Zenbook/ProArt

Общее — в [`brands.md` → ASUS](../../Intel/notes/brands.md). Для AMD дополнительно (techspec на asus.com, 30.09.2026):
- **Vivobook 15/16 до 2024 (M1502, M1505, M1605, M3504, M3604)** — «on board + SO-DIMM», максимум 16–24 ГБ → ловушки. HDMI 1.4, USB 5 Gbps.
- **Vivobook 16 M1607 (2025)** ([asus](https://www.asus.com/Laptops/For-Home/Vivobook/ASUS-Vivobook-16-M1607/techspec/)):
  - «16GB DDR5 on board + 16GB DDR5 SO-DIMM, Max 32GB»;
  - «Dual-channel memory support requires at least one SO-DIMM module»;
  - USB только 5 Gbps, HDMI 2.1 TMDS.
  - NBC (M1606K, AI 7 350): «all USB ports only 5Gb/s», «display bezel detaches quite easily», «cooling system not very balanced», 24 мес. ([NBC, 28.02.2025](https://www.notebookcheck.net/Asus-Vivobook-16-laptop-review-AI-features-at-the-forefront-genuine-productivity-boost-or-marketing-hype.971144.0.html)).
- **Vivobook S16 M3607 (2025)** — та же схема «16 + SO-DIMM, до 32», USB 5 Gbps. CPU от Hawk Point до Gorgon ([asus](https://www.asus.com/Laptops/For-Home/Vivobook/ASUS-Vivobook-S16-M3607/techspec/)).
- **Vivobook S16 OLED M5606** — LPDDR5X onboard; USB4 есть в части конфигураций ([asus](https://www.asus.com/Laptops/For-Home/Vivobook/ASUS-Vivobook-S-16-OLED-M5606/techspec/)).
- **ExpertBook P1 PM1503 / BM1 BM1503** (15,6"):
  - 2× SO-DIMM, до 64, M.2 2280 + M.2 2230;
  - «HDMI 1.4, up to 3840x2160p/30Hz», USB-C 10 Gbps.
  - CPU Rembrandt (150/170) или Rembrandt R.
  - С 32/1 ТБ на billiger: BM1 (Ryzen 7 170) — от 1119 € ([billiger](https://www.billiger.de/pricelist/5547669491-asus-expertbook-bm1-15-6-amd-ryzen-7-170-32-gb-ram-1-tb-ssd-win11-pro)), PM1 (Ryzen 5 150) — от 1169 € ([billiger](https://www.billiger.de/pricelist/5769549203-asus-expertbook-pm1-15-6)), 30.09.2026. Раскладка — не проверено.
  - NBC (B1 BM1503CDA, 7535U, 2×8): «3-year warranty», дешёвый пластик, узкий цветовой охват ([NBC, 10.03.2025](https://www.notebookcheck.net/Asus-ExpertBook-B1-review-The-business-laptop-with-Win-11-Pro-and-a-3-year-warranty-for-750.975913.0.html)).
- **ExpertBook P3 PM3606 (16")** ([asus](https://www.asus.com/Laptops/For-Work/ExpertBook/ASUS-ExpertBook-P3-PM3606/techspec/)):
  - Ryzen AI 5 330 / AI 7 350, 2× SO-DIMM, в том числе «16GB DDR5 SO-DIMM x 2» и «32GB … x 2»;
  - USB-C 10 Gbps, HDMI 2.1, RJ45.
  - NBC тестировал 14-дюймовую сестру PM3: «three-year warranty/5-year software updates», одноканал, «no USB4/Thunderbolt 4», 979 € ([NBC](https://www.notebookcheck.net/Asus-ExpertBook-PM3-Review-Office-laptop-with-AMD-long-battery-life-and-Copilot.1200511.0.html)).
- **ExpertBook P3 G2 / B3 G2 / P5 G2 16 AMD (2026)** — 2× SO-DIMM до 96, 1× USB4 ([P3 G2](https://www.asus.com/Laptops/For-Work/ExpertBook/ASUS-ExpertBook-P3-G2-16-AMD/techspec/), [B3 G2](https://www.asus.com/Laptops/For-Work/ExpertBook/ASUS-ExpertBook-B3-G2-16-AMD/techspec/), [P5 G2](https://www.asus.com/Laptops/For-Work/ExpertBook/ASUS-ExpertBook-P5-G2-16-AMD/techspec/)).
  - NBC PM5 G2 (HX 470): одноканал в тесте, «loose hinges», «three-year warranty», в DE ~1800–2250 € ([NBC, 19.08.2026](https://www.notebookcheck.net/AMD-business-laptop-with-a-great-144-Hz-IPS-display-Asus-ExpertBook-PM5-G2-review.1368549.0.html)).
- **TUF A16 (2025)** — 2× SO-DIMM (в 2024 была распайка) ([asus 2025](https://www.asus.com/Laptops/For-Gaming/TUF-Gaming/ASUS-TUF-Gaming-A16-2025/techspec/), [asus 2024](https://www.asus.com/Laptops/For-Gaming/TUF-Gaming/ASUS-TUF-Gaming-A16-2024-FA608/techspec/)).
  - NBC (FA608UP, Ryzen 7 260): «neither USB 4.0 nor Wi-Fi 7», «very loud in Turbo mode», 2199 € ([NBC, 25.09.2025](https://www.notebookcheck.net/Asus-TUF-Gaming-A16-Laptop-Review-A-EUR2-200-gamble-for-Zen-4-Hawk-Point-RTX-5070.1122766.0.html)).
  - На asus.com USB4 указан только для части конфигураций.
  - На billiger: TUF A16 Ryzen 7 170 32/1 ТБ RTX 4050 — от 1419,99 € ([billiger](https://www.billiger.de/pricelist/5878659522-asus-tuf-gaming-a16-amd-ry), 30.09.2026).
- **TUF A15 (2024)** — 2× SO-DIMM (до 32), USB4 ([asus](https://www.asus.com/Laptops/For-Gaming/TUF-Gaming/ASUS-TUF-Gaming-A15-2024/techspec/), [NBC, 20.07.2024](https://www.notebookcheck.net/Asus-TUF-Gaming-A15-2024-review-RTX-4060-power-moderate-price-long-battery-life.864614.0.html)).
- **Zenbook S16, ProArt P16** — распайка; у обоих NBC отмечает ШИМ ([S16](https://www.notebookcheck.net/The-perfect-everyday-laptop-with-AMD-Ryzen-400-Asus-Zenbook-S16-OLED-review.1221965.0.html), [P16](https://www.notebookcheck.net/4K-OLED-is-replaced-by-120-Hz-2-8K-OLED-Asus-ProArt-P16-with-RTX-5070-Laptop-review.1026301.0.html)).
- **Вердикт ASUS (AMD).**
  - ExpertBook P3/B3 G2 16 AMD — лучшие AMD-платформы ASUS по памяти (2 слота, 3 года гарантии), но цен ≤ 1100 € с 32/1 ТБ не нашёл.
  - Vivobook 16 M1607 — только путь «16 + 16 распайка/слот».

### Acer — Aspire, Swift, Extensa, TravelMate, Nitro

Общее — в [`brands.md` → Acer](../../Intel/notes/brands.md). Для AMD дополнительно (раскладка — Icecat по EAN):
- **Aspire 16 AI A16-61M** (Ryzen AI 7 350): LPDDR5x-8533 32 ГБ распайка, 2× USB4, 1,55 кг ([Icecat R2R1](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&GTIN=4711474850324), [Icecat R8T1](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&GTIN=4711474665621)).
  - `NX.JP0EG.00Z` (R2R1, OLED) — 1015,86 € (Galaxus).
  - `NX.JLLEG.009` (R8T1) — 1080,25 € (TECHNIKdirekt). Обе цены — billiger, 30.09.2026.
- **Swift Air 16 SFA16-61M-R1FY** (AI 5 330): LPDDR5 32 ГБ, 1,1 кг, 2 года гарантии; `NX.DL5EG.002` — 986,51 € (Expert, billiger, 30.09.2026) ([Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&GTIN=4711474856227)).
- **Swift Go 16 AI** — LPDDR5x распайка, 2× USB4 ([Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&GTIN=4711474416001)). NBC: «loud fans», «hot air on the OLED panel» ([NBC, 25.11.2025](https://www.notebookcheck.net/Solid-performance-and-colorful-OLED-Acer-Swift-Go-16-AI-review.1168834.0.html)).
- **Aspire Go 15 AG15-42P** (5825U, Barcelo), **Extensa 15 AMD** (7x30U), **Aspire 3 A315-24P** (Mendocino) — CPU-ловушки, см. таблицу.
  - Офиц. сервис-мануалов у Acer нет ([`brands.md`](../../Intel/notes/brands.md)), поэтому слоты Extensa 15 AMD — не проверено.
- **Nitro V 16 AI ANV16-42** (Ryzen 5 240 / 7 260 + RTX 5050–5070):
  - 2× SO-DIMM и 2× M.2, USB4 ([NBC, 07.11.2025](https://www.notebookcheck.net/Acer-Nitro-V-16-AI-Review-Affordable-gaming-laptop-with-great-battery-life.1156010.0.html)).
  - `NH.QYWEG.002` (R860): 2×8, до 32 ГБ ([Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&GTIN=4711474531131)); от 1249 € на billiger (30.09.2026).
  - NBC к ANV16-41 (8845HS): «poor fan control, too loud under load», «case is a little rickety» ([NBC, 06.12.2024](https://www.notebookcheck.net/Acer-Nitro-V-16-ANV16-41-review-An-affordable-gaming-laptop-with-a-hitch.928048.0.html)).
- **TravelMate AMD, Nitro V 15 ANV15-41, Nitro 16 AN16-4x** — не проверено.
- **Вердикт Acer (AMD).** Всё, что ≤ 1100 € с 32 ГБ, — либо распайка (Aspire 16 AI, Swift), либо Barcelo/Mendocino.

### MSI — Venture/Modern, Katana, Prestige/Summit

- **Venture A16 AI+ A3HMG-036DE** (AI 5 340, 16"): 2×8 DDR5-5600 в 2× SO-DIMM, до 96 ГБ ([Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&GTIN=4711377358880)). От 859 € ([billiger](https://www.billiger.de/products/5310785148-msi-venturepro-a16-ai-amd-ry), 30.09.2026; продавец не определён).
- **Katana A15 AI B8VG** (8945HS): «two RAM and two SSD slots»; минусы — «case rattles», слабый экран, «no USB 4, no card reader» ([NBC, 04.01.2025](https://www.notebookcheck.net/MSI-Katana-A15-AI-laptop-review-RTX-4070-gamer-hurt-by-cost-saving-measures.936689.0.html)).
- **Prestige A16 AI+** (AI 9 365): LPDDR5X; «case crackles strongly when twisted», 1599 € ([NBC, 26.01.2025](https://www.notebookcheck.net/MSI-Prestige-A16-AI-review-Multimedia-laptop-with-powerful-Ryzen-9-365.949210.0.html)).
- **Modern 15 B7M, Bravo 15, Thin A15, Cyborg AMD** — на billiger сейчас нет, раскладку не проверял.
- Сайт MSI через curl отдаёт 403. Прочее по бренду — в [`brands.md` → MSI](../../Intel/notes/brands.md).

### Medion

- **Avantum 15 E1** `30039298` (Ryzen 5 7430U): 2×16 DDR4-3200 в двухканале, 1 ТБ, 1,81 кг ([Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&GTIN=4061275237580)). 719,99 € в expert ([billiger](https://www.billiger.de/pricelist/5156655964-medion-avantum-15-e1-15-6-amd-ryzen-5-7430u-32-gb-ram-1-tb-ssd-win11-home), 30.09.2026).
  - Память — эталон, но CPU — Barcelo R (Zen 3, 2021).
- Других AMD-моделей Medion 15–16" на billiger не нашёл. Гарантия и сервис — [`brands.md` → Medion](../../Intel/notes/brands.md).

### Gigabyte

- **GAMING A16 3VH** `GAMING A16 3VHK3DE894SH` ([Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&GTIN=4719331766764)):
  - Ryzen 7 260 + RTX 5060 8 ГБ GDDR7;
  - 1×16 DDR5-5200 в 2× SO-DIMM, до 64;
  - 1 ТБ, 2,2 кг, 2 года гарантии.
  - Цена 1099 € (computeruniverse, MediaMarkt, Cyberport, coolblue, Alternate; [billiger](https://www.billiger.de/pricelist/5372928568-gigabyte-gaming-a16-3vh-amd-ryzen-7-260-16), 30.09.2026).
  - Это единственный AMD + RTX 50 с «16 + свободный слот» около 1100 €.
  - NBC тестировал Intel-сестру GA6H (i7-13620H): «pretty loud under load», «screen bleeding», «no USB 4» ([NBC](https://www.notebookcheck.net/An-affordable-RTX-5070-laptop-Gigabyte-Gaming-A16-review.1072350.0.html)).
- **Aero X16** (AI 7 350): 2 слота до 64 ГБ, 2× M.2 2280, IPS без ШИМ; от 1499 € ([NBC](https://www.notebookcheck.net/Gigabyte-Aero-X16-Review-Sleek-AMD-Zen-5-gaming-machine-with-Nvidia-RTX-5070-Laptop-and-upgradeable-RAM.1022304.0.html), [billiger](https://www.billiger.de/pricelist/5291496054-gigabyte-aero-x16-amd-ryzen-ai-7-35), 30.09.2026).

### Framework Laptop 16 (AMD, DIY)

- Ryzen AI 300, «two DDR5 SO-DIMM slots», до 96 ГБ, два SSD, опционально RTX 5070 или RX 7700S ([frame.work](https://frame.work/de/en/laptop16)).
- DIY Edition: от **1409 €** (AI 5 340), 1754 € (AI 7 350), 2094 € (AI 9 HX 370) ([frame.work](https://frame.work/de/en/products/laptop16-diy-amd-ai300)). Память и SSD в эти цены, видимо, не входят — не проверено.
- → Вне бюджета. Ремонтопригодность и гарантия — [`brands.md` → Framework](../../Intel/notes/brands.md).

### Tuxedo (Аугсбург)

- **InfinityBook Pro 15 Gen10 AMD** ([tuxedo](https://www.tuxedocomputers.com/de/TUXEDO-InfinityBook-Pro-15-Gen10-AMD.tuxedo)):
  - Ryzen AI 300, «zwei aufrüstbare RAM-Steckplätze», до 128 ГБ DDR5-5600, 2× PCIe 4.0 SSD;
  - USB4, HDMI 2.0;
  - 15,3" 2560×1600, 500 кд/м², 100 % sRGB;
  - 99 Втч, 1,75 кг;
  - гарантия 2 года Pick-Up & Return, опционально до 5 лет.
- **InfinityBook Max 15 Gen10 AMD** — AI 9 HX 370 + RTX 5070, 2 слота, 1,95 кг ([tuxedo](https://www.tuxedocomputers.com/de/TUXEDO-InfinityBook-Max-15-Gen10-AMD.tuxedo)).
- Цены: конфигуратор на JS, цену через curl не получил — не проверено. По [`REPORT.md`](../../Intel/REPORT.md) Tuxedo/XMG с 32/1 ТБ — от ~1770 €.
- Pulse 15/16 и Aura 15 с AMD в текущей линейке не нашёл. Aura 15 Gen1 (4700U) — в архиве ([tuxedo](https://www.tuxedocomputers.com/en/Linux-Hardware/Linux-Notebooks/15-16-inch/TUXEDO-Aura-15-Gen1.tuxedo)).

### XMG / Schenker (bestware)

- **Core 15 M25** (AI 7 350, 15,3"): «two slots each for SSDs and RAM», «quite expensive» ([NBC, 28.09.2025](https://www.notebookcheck.net/German-competitor-to-the-Legion-5-XMG-Core-15-M25-gaming-laptop-review.1126351.0.html)). На billiger `M25wyh` (16/1 ТБ, RTX 5060) — 2129 € ([billiger](https://www.billiger.de/pricelist/5389881379-xmg-core-15-m25wyh-15-3-am), 30.09.2026).
- **Core 16 M25** (AI 9 HX 370) — 2 слота, от 1579 € ([NBC, 07.10.2025](https://www.notebookcheck.net/XMG-Core-16-M25-review-AMD-gaming-laptop-with-300-Hz-display-and-RTX-5070.1132775.0.html)).
- **Core 16 VE M25** (Ryzen 7 255) — 2 слота, от 1479 € ([NBC, 18.01.2026](https://www.notebookcheck.net/Challenge-to-the-Lenovo-Legion-XMG-Core-16-VE-M25-gaming-laptop-review.1202743.0.html)).
- **Core 15 M24** (8845HS): 2×16, «no Thunderbolt» ([NBC, 19.06.2024](https://www.notebookcheck.net/SCHENKER-XMG-Core-15-M24-laptop-review-A-premium-metal-cased-gaming-machine-from-Germany.848771.0.html)).
- Apex 16 Max и Neo 16 A25 (9955HX/HX3D) — от 2800 € ([NBC](https://www.notebookcheck.net/AMD-Ryzen-9-9955HX-RTX-5070-Ti-and-mini-LED-XMG-Apex-16-Max-gaming-laptop-review.1206725.0.html)).
- → Вне бюджета. Сервис — [`brands.md` → XMG](../../Intel/notes/brands.md).

### Fujitsu, Samsung, LG, Microsoft, Dynabook

- **Fujitsu Lifebook AMD 15–16"** — на billiger поиск «Fujitsu Lifebook Ryzen» пуст (30.09.2026). Статус бренда — в [`brands.md`](../../Intel/notes/brands.md).
- **Samsung Galaxy Book на AMD** — в DE не нашёл (billiger пуст).
- **LG:** gram 15Z80T (2025, Ryzen AI 7 350) есть в сборнике NBC ([NBC](https://www.notebookcheck.net/LG-gram-15Z80T-2025.1175186.0.html), 29.08.2025). Раскладка и продажа в DE — не проверено (на billiger не нашёл).
- **Microsoft:** последний 15" на AMD — Surface Laptop 4 15 (Ryzen 7 4980U, 2021) по сборнику NBC ([NBC-список](https://www.notebookcheck.net/Laptop-Search.8223.0.html)); сейчас 15" — Snapdragon ([`brands.md`](../../Intel/notes/brands.md)). → нет.
- **Dynabook Tecra A65-M** (Ryzen 7 250): 16 ГБ single-channel в тесте, один M.2, 36 мес. гарантии, ~1300 € ([NBC, 22.01.2026](https://www.notebookcheck.net/Dynabook-Tecra-A65-M-laptop-review-Suitable-ThinkPad-E-or-EliteBook-alternative.1202807.0.html)). На billiger не нашёл.

## AMD против Intel в одной модели (что меняется)

| Модель | AMD | Intel | Источник |
|---|---|---|---|
| ThinkPad E16 Gen 3 | 1× USB4 40G, 2× SO-DIMM во всех CPU | 1× TB4/USB4; на Lunar Lake — распайка | [PSREF AMD](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_E16_Gen_3_AMD/ThinkPad_E16_Gen_3_AMD_Spec.PDF), [PSREF Intel](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_E16_Gen_3_Intel/ThinkPad_E16_Gen_3_Intel_Spec.PDF) |
| ThinkPad E16 Gen 4 | 2× USB4, 2 слота во всех CPU | 2× TB4; Wildcat Lake — 1 слот | [PSREF AMD](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_E16_Gen_4_AMD/ThinkPad_E16_Gen_4_AMD_Spec.PDF), [PSREF Intel](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_E16_Gen_4_Intel/ThinkPad_E16_Gen_4_Intel_Spec.PDF) |
| ThinkPad L16 Gen 2/3, T16 Gen 4/5, P16s Gen 4 | порты TB4 сертифицированы и у AMD | TB4 | PSREF (таблица) |
| HP ProBook 4 / EliteBook 6 (G1a vs G1i) | 2 SODIMM, HEVC выкл. | 2 SODIMM, HEVC выкл. | [c09111176](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09111176), [`hevc-audit.md`](../../Intel/notes/hevc-audit.md) |
| HP EliteBook 8 16 (G1a vs G1i) | HEVC есть, TB4 | HEVC есть | [c09120200](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09120200), [`hevc-audit.md`](../../Intel/notes/hevc-audit.md) |
| HP Envy x360 16 | «no Thunderbolt or USB4 support on AMD SKUs» | — | [NBC](https://www.notebookcheck.net/HP-Envy-x360-2-in-1-16-review-Ryzen-7-8840HS-beats-Core-Ultra-7-155U.837856.0.html) |
| Dell Pro 16 (PC16255 vs PC16250) | 2× USB 40 Gbps (USB4) | TB4 | [Dell AMD](https://dl.dell.com/content/manual33305221-dell-pro-16-pc16255-owner-s-manual.pdf?language=en-us), [`hevc-audit.md`](../../Intel/notes/hevc-audit.md) |
| Dell Pro 5 16 | только SODIMM | есть CAMM | [NBC](https://www.notebookcheck.net/Dell-Pro-5-16-P516265-review-Traditional-and-reliable.1342884.0.html) |
| Dell 16 (DC16255 vs DC16250) | 2 SODIMM, «макс. 32», SSD 2230 | 2 SODIMM, база 2×8 | [Dell](https://dl.dell.com/content/manual20191269-dell-16-dc16255-p-setup-and-specifications.pdf?language=en-us), [`brands.md`](../../Intel/notes/brands.md) |
| Gigabyte Gaming A16 | Ryzen 7 260 (Hawk Point) | i7-13620H (Raptor Lake) | [Icecat](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&GTIN=4719331766764), [NBC Intel](https://www.notebookcheck.net/An-affordable-RTX-5070-laptop-Gigabyte-Gaming-A16-review.1072350.0.html) |

- Главное отличие для монтажа — не порты, а кодеки: встроенная графика Ryzen не декодирует 4:2:2 (по Puget, см. [`intel-cpu.md`](../../Intel/notes/intel-cpu.md) §2.3). Проверка для Radeon 800M — в `amd-codecs.md`.

## Кандидаты-зацепки (для шага «кандидаты»)

Цены — billiger.de, 30.09.2026. Если продавец указан — это минимальное предложение на странице товара. Раскладка — по Icecat, если не сказано иное.

| Парт-номер | Модель, CPU | Память / 1 ТБ | Цена | Замечания |
|---|---|---|---|---|
| **21MW00AYGE** | ThinkBook 16 G7 ARP, Ryzen 5 7535HS | **2×16** DDR5-4800 / 1 ТБ | **998,99 €**, Easynotebooks ([billiger](https://www.billiger.de/products/5349474817-lenovo-thinkbook-16-g7-arp-amd-ryzen-5-7535hs-32-gb-ram-1-tb-ssd-win11-pro-arctic-grey-21mw00ayge)) | Zen 3+; экран 300 нит 45 % NTSC; 45 Втч; 1× USB4 |
| **21UT004QGE** | ThinkBook 16 G9 AHP, Ryzen 5 220 | **2×16** DDR5-5600 / 1 ТБ | **1073 €**, c-nw ([billiger](https://www.billiger.de/products/5510914032-lenovo-thinkbook-16-g9-amd-ryzen-5-220-32-gb-ram-1-tb-ssd-win11-pro-21ut004qge)) | Hawk Point, 740M; 2× USB4; 400 нит 45 % NTSC |
| 21MW007VGE | ThinkBook 16 G7 ARP, Ryzen 7 7735HS | 2×16 / 1 ТБ | ab 1092 € (листинг, продавец не определён) | 680M |
| 21UT000RGE | ThinkBook 16 G9 AHP, Ryzen 7 250 | 2×16 / 1 ТБ | ab 1188 € (листинг) | выше потолка |
| 21ST004GGE | ThinkPad E16 Gen 3 AMD, Ryzen 5 220 | **1×32** / 1 ТБ | 1149 €, notebooksbilliger ([billiger](https://www.billiger.de/products/5334168438-lenovo-thinkpad-e16-g3-amd-ryzen-5-220-32-gb-ram-1-tb-ssd-21st004gge)) | ловушка: одноканал |
| 21ST001YGE | ThinkPad E16 Gen 3 AMD, Ryzen 7 250 | **1×32** / 1 ТБ | ab 1199,83 € | ловушка |
| 21SC002AGE | ThinkPad L16 Gen 2 AMD, Ryzen 5 PRO 215 | 32 / 1 ТБ (раскладка не проверена; NBC 21SC0029GE — 2×16) | ab 1232 € | TB4, выше потолка |
| C7SP9ES | HP ProBook 4 G1a 16, Ryzen 5 230 | 32 / 1 ТБ (раскладка не проверена) | ab 899 € (только в листинге; страница товара без предложений) | **HEVC выкл.** |
| C7SQ0ES | HP ProBook 4 G1a 16, Ryzen 5 230 | 32 / 1 ТБ | 1129 €, notebooksbilliger ([billiger](https://www.billiger.de/products/5406906476-hp-probook-4-g1a-16-amd-ryzen-5-230-32-gb-ram-1-tb-ssd-c7sq0es)) | HEVC выкл. |
| EAN 0199764423627 | HP EliteBook 8 G1a 16, Ryzen 7 250, FreeDOS | 32 / 1 ТБ | 1299 €, notebooksbilliger ([billiger](https://www.billiger.de/products/5460257445-hp-elitebook-8-g1a-16-amd-ryzen-7-250-32-gb-ram-1-tb-ssd-radeon-780m-freedos-silber)) | **HEVC есть**, TB4; дороже потолка |
| GAMING A16 3VHK3DE894SH | Gigabyte, Ryzen 7 260 + RTX 5060 | 1×16 + слот / 1 ТБ | 1099 €, computeruniverse ([billiger](https://www.billiger.de/pricelist/5372928568-gigabyte-gaming-a16-3vh-amd-ryzen-7-260-16)) | с планкой ~1336 € |
| 30039298 | Medion Avantum 15 E1, Ryzen 5 7430U | 2×16 DDR4 / 1 ТБ | 719,99 €, expert | CPU-ловушка (Barcelo R) |
| NX.JP0EG.00Z | Acer Aspire 16 AI A16-61M-R2R1, AI 7 350 | 32 LPDDR5x распайка / 1 ТБ | 1015,86 €, Galaxus | список 3 (распайка) |
| NX.JLLEG.009 | Acer Aspire 16 AI A16-61M-R8T1, AI 7 350 | 32 распайка / 1 ТБ | 1080,25 €, TECHNIKdirekt | список 3 |
| NX.DL5EG.002 | Acer Swift Air 16 SFA16-61M-R1FY, AI 5 330 | 32 LPDDR5 распайка / 1 ТБ | 986,51 €, Expert | список 3; 820M слабая |
| 83S2003GGE | IdeaPad Slim 5 16AGP11, AI 5 430 | 2×8 / 1 ТБ, OLED | 849 €, coolblue | нужна замена обеих планок |
| 83S2000BGE | IdeaPad Slim 5 16AGP11, AI 7 445 | 2×8 / 1 ТБ | 889 €, Galaxus | то же |
| VENTURE A16 AI+ A3HMG-036DE | MSI, AI 5 340 | 2×8 / 512 ГБ | ab 859 € | замена планок и SSD |
| NH.QYWEG.002 | Acer Nitro V 16 AI ANV16-42-R860, Ryzen 5 240 + RTX 5050 | 2×8 / 1 ТБ | ab 1249 € | выше потолка |
| — | ASUS ExpertBook BM1 BM1503, Ryzen 7 170 | 32 / 1 ТБ (раскладка не проверена) | ab 1119 € | Rembrandt, HDMI 1.4 |
| 16-bv0074ng | HP OmniBook 3 NGAI 16, AI 7 445 | 32 / 1 ТБ («not accessible», раскладка не проверена) | ab 1130,23 € | — |

## Что не удалось проверить

- Раскладку памяти HP ProBook 4 G1a 16 C7SP9ES/C7SQ0ES: в Icecat их нет, а страница billiger для C7SP9ES пустая.
- PSREF по конкретным MTM: API `singleModel` отвечал «Error generating PDF», поэтому использовал Icecat.
- HP Victus 15 AMD (15-fb2/fb3), HP 15-fc, HP 255 G11, Acer Extensa 15 / TravelMate / Nitro V 15 AMD, MSI Modern 15 B7M / Bravo 15, Dell G15 5535 — слоты не проверены.
- Цены Dell Pro 16 PC16255, Inspiron 16 5645, Dell 16 DC16255, ExpertBook P3 PM3606 в DE (на billiger поиск их не выдал).
- Цены Tuxedo InfinityBook Pro 15 Gen10 AMD с 32/1 ТБ (конфигуратор на JS).
- LG gram AMD в DE; Fujitsu AMD; Samsung AMD.
- Коды amd.com для Ryzen 3 110, 5 216, 7 217, 7 253, 7 255, 5 224, 7 249.
- HEVC у Lenovo, ASUS, Acer, MSI на AMD и у HP 255 G10/255R G10 — передано в `hevc-amd.md`.
- Кодеки Radeon 800M (4:2:2) — в `amd-codecs.md`.

## Источники

**Lenovo PSREF** (`psref.lenovo.com/syspool/Sys/PDF/…`):
- ThinkPad:
  - [E16 Gen 2 AMD](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_E16_Gen_2_AMD/ThinkPad_E16_Gen_2_AMD_Spec.PDF), [E16 Gen 3 AMD](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_E16_Gen_3_AMD/ThinkPad_E16_Gen_3_AMD_Spec.PDF), [E16 Gen 4 AMD](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_E16_Gen_4_AMD/ThinkPad_E16_Gen_4_AMD_Spec.PDF), [E16 Gen 3 Intel](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_E16_Gen_3_Intel/ThinkPad_E16_Gen_3_Intel_Spec.PDF), [E16 Gen 4 Intel](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_E16_Gen_4_Intel/ThinkPad_E16_Gen_4_Intel_Spec.PDF);
  - [L16 Gen 1 AMD](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_L16_Gen_1_AMD/ThinkPad_L16_Gen_1_AMD_Spec.PDF), [L16 Gen 2 AMD](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_L16_Gen_2_AMD/ThinkPad_L16_Gen_2_AMD_Spec.PDF), [L16 Gen 3 AMD](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_L16_Gen_3_AMD/ThinkPad_L16_Gen_3_AMD_Spec.PDF);
  - [T16 Gen 2 AMD](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_T16_Gen_2_AMD/ThinkPad_T16_Gen_2_AMD_Spec.PDF), [T16 Gen 4 AMD](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_T16_Gen_4_AMD/ThinkPad_T16_Gen_4_AMD_Spec.PDF), [T16 Gen 5 AMD](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_T16_Gen_5_AMD/ThinkPad_T16_Gen_5_AMD_Spec.PDF);
  - [P16s Gen 4 AMD](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_P16s_Gen_4_AMD/ThinkPad_P16s_Gen_4_AMD_Spec.PDF), [P16s Gen 5 AMD](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_P16s_Gen_5_AMD/ThinkPad_P16s_Gen_5_AMD_Spec.PDF).
- ThinkBook: [16 G6 ABP](https://psref.lenovo.com/syspool/Sys/PDF/ThinkBook/ThinkBook_16_G6_ABP/ThinkBook_16_G6_ABP_Spec.PDF), [16 G7 ARP](https://psref.lenovo.com/syspool/Sys/PDF/ThinkBook/ThinkBook_16_G7_ARP/ThinkBook_16_G7_ARP_Spec.PDF), [16 G7+ ASP](https://psref.lenovo.com/syspool/Sys/PDF/ThinkBook/ThinkBook_16_G7plus_ASP/ThinkBook_16_G7plus_ASP_Spec.PDF), [16 G9 AHP](https://psref.lenovo.com/syspool/Sys/PDF/ThinkBook/ThinkBook_16_G9_AHP/ThinkBook_16_G9_AHP_Spec.PDF), [16p G6 ADR](https://psref.lenovo.com/syspool/Sys/PDF/ThinkBook/ThinkBook_16p_G6_ADR/ThinkBook_16p_G6_ADR_Spec.PDF).
- IdeaPad:
  - Slim 3: [15ABR8](https://psref.lenovo.com/syspool/Sys/PDF/IdeaPad/IdeaPad_Slim_3_15ABR8/IdeaPad_Slim_3_15ABR8_Spec.PDF), [15AMN8](https://psref.lenovo.com/syspool/Sys/PDF/IdeaPad/IdeaPad_Slim_3_15AMN8/IdeaPad_Slim_3_15AMN8_Spec.PDF), [15ARP10](https://psref.lenovo.com/syspool/Sys/PDF/IdeaPad/IdeaPad_Slim_3_15ARP10/IdeaPad_Slim_3_15ARP10_Spec.PDF), [16ARP10](https://psref.lenovo.com/syspool/Sys/PDF/IdeaPad/IdeaPad_Slim_3_16ARP10/IdeaPad_Slim_3_16ARP10_Spec.PDF), [15AHP10](https://psref.lenovo.com/syspool/Sys/PDF/IdeaPad/IdeaPad_Slim_3_15AHP10/IdeaPad_Slim_3_15AHP10_Spec.PDF), [16AHP10](https://psref.lenovo.com/syspool/Sys/PDF/IdeaPad/IdeaPad_Slim_3_16AHP10/IdeaPad_Slim_3_16AHP10_Spec.PDF);
  - Slim 5: [15ARP10](https://psref.lenovo.com/syspool/Sys/PDF/IdeaPad/IdeaPad_Slim_5_15ARP10/IdeaPad_Slim_5_15ARP10_Spec.PDF), [16ARP10](https://psref.lenovo.com/syspool/Sys/PDF/IdeaPad/IdeaPad_Slim_5_16ARP10/IdeaPad_Slim_5_16ARP10_Spec.PDF), [16AKP10](https://psref.lenovo.com/syspool/Sys/PDF/IdeaPad/IdeaPad_Slim_5_16AKP10/IdeaPad_Slim_5_16AKP10_Spec.PDF), [16AHP11](https://psref.lenovo.com/syspool/Sys/PDF/IdeaPad/IdeaPad_Slim_5_16AHP11/IdeaPad_Slim_5_16AHP11_Spec.PDF), [16AGP11](https://psref.lenovo.com/syspool/Sys/PDF/IdeaPad/IdeaPad_Slim_5_16AGP11/IdeaPad_Slim_5_16AGP11_Spec.PDF);
  - Pro 5: [16AHP9](https://psref.lenovo.com/syspool/Sys/PDF/IdeaPad/IdeaPad_Pro_5_16AHP9/IdeaPad_Pro_5_16AHP9_Spec.PDF), [16AKP10](https://psref.lenovo.com/syspool/Sys/PDF/IdeaPad/IdeaPad_Pro_5_16AKP10/IdeaPad_Pro_5_16AKP10_Spec.PDF), [16ASP10](https://psref.lenovo.com/syspool/Sys/PDF/IdeaPad/IdeaPad_Pro_5_16ASP10/IdeaPad_Pro_5_16ASP10_Spec.PDF), [16AGP11](https://psref.lenovo.com/syspool/Sys/PDF/IdeaPad/IdeaPad_Pro_5_16AGP11/IdeaPad_Pro_5_16AGP11_Spec.PDF);
  - прочие: [Vibe 15AKP12](https://psref.lenovo.com/syspool/Sys/PDF/IdeaPad/IdeaPad_Vibe_15AKP12/IdeaPad_Vibe_15AKP12_Spec.PDF), [IdeaPad 5 2-in-1 16AKP10](https://psref.lenovo.com/syspool/Sys/PDF/IdeaPad/IdeaPad_5_2_in_1_16AKP10/IdeaPad_5_2_in_1_16AKP10_Spec.PDF).
- V: [V15 G4 AMN](https://psref.lenovo.com/syspool/Sys/PDF/Lenovo/Lenovo_V15_G4_AMN/Lenovo_V15_G4_AMN_Spec.PDF), [V15 G4 ABP](https://psref.lenovo.com/syspool/Sys/PDF/Lenovo/Lenovo_V15_G4_ABP/Lenovo_V15_G4_ABP_Spec.PDF), [V15 G6 ARP](https://psref.lenovo.com/syspool/Sys/PDF/Lenovo/Lenovo_V15_G6_ARP/Lenovo_V15_G6_ARP_Spec.PDF), [V15 G6 AMN](https://psref.lenovo.com/syspool/Sys/PDF/Lenovo/Lenovo_V15_G6_AMN/Lenovo_V15_G6_AMN_Spec.PDF).
- Yoga: [7 2-in-1 16AKP10](https://psref.lenovo.com/syspool/Sys/PDF/Yoga/Yoga_7_2_in_1_16AKP10/Yoga_7_2_in_1_16AKP10_Spec.PDF), [7 2-in-1 16AGP11](https://psref.lenovo.com/syspool/Sys/PDF/Yoga/Yoga_7_2_in_1_16AGP11/Yoga_7_2_in_1_16AGP11_Spec.PDF), [Pro 7 15ASH11](https://psref.lenovo.com/syspool/Sys/PDF/Yoga/Yoga_Pro_7_15ASH11/Yoga_Pro_7_15ASH11_Spec.PDF).
- LOQ / Legion:
  - LOQ: [15ARP9](https://psref.lenovo.com/syspool/Sys/PDF/LOQ/LOQ_15ARP9/LOQ_15ARP9_Spec.PDF), [15AHP9](https://psref.lenovo.com/syspool/Sys/PDF/LOQ/LOQ_15AHP9/LOQ_15AHP9_Spec.PDF), [15AHP10](https://psref.lenovo.com/syspool/Sys/PDF/LOQ/LOQ_15AHP10/LOQ_15AHP10_Spec.PDF), [15ARP10E](https://psref.lenovo.com/syspool/Sys/PDF/LOQ/LOQ_15ARP10E/LOQ_15ARP10E_Spec.PDF), [15AHP11](https://psref.lenovo.com/syspool/Sys/PDF/LOQ/LOQ_15AHP11/LOQ_15AHP11_Spec.PDF);
  - Legion 5: [15AHP10](https://psref.lenovo.com/syspool/Sys/PDF/Legion/Legion_5_15AHP10/Legion_5_15AHP10_Spec.PDF), [15AKP10](https://psref.lenovo.com/syspool/Sys/PDF/Legion/Legion_5_15AKP10/Legion_5_15AKP10_Spec.PDF), [15AHP11](https://psref.lenovo.com/syspool/Sys/PDF/Legion/Legion_5_15AHP11/Legion_5_15AHP11_Spec.PDF), [15AGP11](https://psref.lenovo.com/syspool/Sys/PDF/Legion/Legion_5_15AGP11/Legion_5_15AGP11_Spec.PDF).
- Список моделей PSREF — через `https://psref.lenovo.com/api/search/DefinitionFilterAndSearch/Suggest?kw=…` (30.09.2026).

**HP:**
- QuickSpecs: [ProBook 465 G11](https://www8.hp.com/h20195/V2/GetPDF.aspx/c08908497), [EliteBook 665 G11](https://www8.hp.com/h20195/V2/GetPDF.aspx/c08927104), [ProBook 4 G1a 16](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09111176), [EliteBook 6 G1a 16](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09111179), [EliteBook 8 G1a 16](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09120200), [EliteBook 8 G1a 16 Next Gen](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09120201), [HP 255 G10](https://www8.hp.com/h20195/V2/GetPDF.aspx/c08479497), [HP 255R G10](https://www8.hp.com/h20195/V2/GetPDF.aspx/c09053765).
- MSG: [OmniBook 3 16](https://kaas.hpcloud.hp.com/pdf-public/pdf_13159558_en-US-1.pdf), [OmniBook 5 16 Next Gen](https://kaas.hpcloud.hp.com/pdf-public/pdf_13052194_en-US-1.pdf), [Victus 16](https://kaas.hpcloud.hp.com/pdf-public/pdf_7911438_en-US-1.pdf).

**Dell** (dl.dell.com):
- [Dell 16 DC16255 Setup & Specs](https://dl.dell.com/content/manual20191269-dell-16-dc16255-p-setup-and-specifications.pdf?language=en-us)
- [Dell 15 DC15255](https://dl.dell.com/content/manual20023858-dell-15-dc15255-owner-s-manual.pdf?language=en-us)
- [Dell 16 Plus DB16255](https://dl.dell.com/content/manual23366300-dell-16-plus-db16255-owner-s-manual.pdf?language=en-us)
- [Dell Pro 16 PC16255](https://dl.dell.com/content/manual33305221-dell-pro-16-pc16255-owner-s-manual.pdf?language=en-us)
- [Dell Pro 15 Essential PV15255](https://dl.dell.com/content/manual33819502-dell-pro-15-essential-pv15255-owner-s-manual.pdf?language=en-us)
- [Inspiron 16 5645](https://dl.dell.com/content/manual18275235-inspiron-16-5645-owner-s-manual.pdf?language=en-us)
- [Inspiron 15 3535](https://dl.dell.com/content/manual32008171-inspiron-15-3535-owner-s-manual.pdf?language=en-us)
- Список документов: [DC16255](https://www.dell.com/support/product-details/de-de/product/dell-dc16255-laptop/resources/manuals), [PV15255](https://www.dell.com/support/product-details/de-de/product/dell-pro-pv15255-laptop/resources/manuals).

**ASUS** (techspec):
- Vivobook: [15 M1502](https://www.asus.com/Laptops/For-Home/Vivobook/vivobook-15-m1502/techspec/), [15 OLED M1505](https://www.asus.com/Laptops/For-Home/Vivobook/ASUS-Vivobook-15-OLED-M1505/techspec/), [16 M1605](https://www.asus.com/Laptops/For-Home/Vivobook/ASUS-Vivobook-16-OLED-M1605/techspec/), [16 M1607](https://www.asus.com/Laptops/For-Home/Vivobook/ASUS-Vivobook-16-M1607/techspec/), [S16 M3607](https://www.asus.com/Laptops/For-Home/Vivobook/ASUS-Vivobook-S16-M3607/techspec/), [S16 OLED M5606](https://www.asus.com/Laptops/For-Home/Vivobook/ASUS-Vivobook-S-16-OLED-M5606/techspec/), [15X M3504](https://www.asus.com/Laptops/For-Home/Vivobook/ASUS-Vivobook-15X-OLED-M3504/techspec/), [16X M3604](https://www.asus.com/Laptops/For-Home/Vivobook/ASUS-Vivobook-16X-OLED-M3604/techspec/), [Go 15 E1504F](https://www.asus.com/Laptops/For-Home/Vivobook/Vivobook-Go-15-OLED-E1504F/techspec/).
- ExpertBook: [P1 PM1503](https://www.asus.com/Laptops/For-Work/ExpertBook/ASUS-ExpertBook-P1-PM1503/techspec/), [BM1 BM1503](https://www.asus.com/Laptops/For-Work/ExpertBook/ASUS-ExpertBook-BM1-BM1503/techspec/), [P3 PM3606](https://www.asus.com/Laptops/For-Work/ExpertBook/ASUS-ExpertBook-P3-PM3606/techspec/), [P3 G2 16 AMD](https://www.asus.com/Laptops/For-Work/ExpertBook/ASUS-ExpertBook-P3-G2-16-AMD/techspec/), [B3 G2 16 AMD](https://www.asus.com/Laptops/For-Work/ExpertBook/ASUS-ExpertBook-B3-G2-16-AMD/techspec/), [P5 G2 16 AMD](https://www.asus.com/Laptops/For-Work/ExpertBook/ASUS-ExpertBook-P5-G2-16-AMD/techspec/).
- TUF: [A15 2024](https://www.asus.com/Laptops/For-Gaming/TUF-Gaming/ASUS-TUF-Gaming-A15-2024/techspec/), [A16 2025](https://www.asus.com/Laptops/For-Gaming/TUF-Gaming/ASUS-TUF-Gaming-A16-2025/techspec/), [A16 2024 FA608](https://www.asus.com/Laptops/For-Gaming/TUF-Gaming/ASUS-TUF-Gaming-A16-2024-FA608/techspec/).
- Поиск моделей — `odinapi.asus.com/recent-data/apiv2/SearchSuggestion`.

**amd.com** (Former Codename):
- Mendocino: [7520U](https://www.amd.com/en/products/processors/laptop/ryzen/7000-series/amd-ryzen-5-7520u.html), [Ryzen 5 40](https://www.amd.com/en/products/processors/laptop/ryzen/10-series/amd-ryzen-5-40.html), [Ryzen 3 30](https://www.amd.com/en/products/processors/laptop/ryzen/10-series/amd-ryzen-3-30.html).
- Barcelo R: [7430U](https://www.amd.com/en/products/processors/laptop/ryzen/7000-series/amd-ryzen-5-7430u.html), [7530U](https://www.amd.com/en/products/processors/laptop/ryzen/7000-series/amd-ryzen-5-7530u.html), [7730U](https://www.amd.com/en/products/processors/laptop/ryzen/7000-series/amd-ryzen-7-7730u.html).
- Rembrandt R: [7535HS](https://www.amd.com/en/products/processors/laptop/ryzen/7000-series/amd-ryzen-5-7535hs.html), [7735HS](https://www.amd.com/en/products/processors/laptop/ryzen/7000-series/amd-ryzen-7-7735hs.html).
- Rembrandt: [130](https://www.amd.com/en/products/processors/laptop/ryzen/100-series/amd-ryzen-5-130.html), [150](https://www.amd.com/en/products/processors/laptop/ryzen/100-series/amd-ryzen-5-150.html), [160](https://www.amd.com/en/products/processors/laptop/ryzen/100-series/amd-ryzen-7-160.html), [170](https://www.amd.com/en/products/processors/laptop/ryzen/100-series/amd-ryzen-7-170.html).
- Hawk Point: [210](https://www.amd.com/en/products/processors/laptop/ryzen/200-series/amd-ryzen-3-210.html), [220](https://www.amd.com/en/products/processors/laptop/ryzen/200-series/amd-ryzen-5-220.html), [230](https://www.amd.com/en/products/processors/laptop/ryzen/200-series/amd-ryzen-5-230.html), [240](https://www.amd.com/en/products/processors/laptop/ryzen/200-series/amd-ryzen-5-240.html), [250](https://www.amd.com/en/products/processors/laptop/ryzen/200-series/amd-ryzen-7-250.html), [260](https://www.amd.com/en/products/processors/laptop/ryzen/200-series/amd-ryzen-7-260.html), [8540U](https://www.amd.com/en/products/processors/laptop/ryzen/8000-series/amd-ryzen-5-8540u.html).
- Krackan Point: [AI 5 330](https://www.amd.com/en/products/processors/laptop/ryzen/ai-300-series/amd-ryzen-ai-5-330.html), [AI 5 340](https://www.amd.com/en/products/processors/laptop/ryzen/ai-300-series/amd-ryzen-ai-5-340.html), [AI 7 350](https://www.amd.com/en/products/processors/laptop/ryzen/ai-300-series/amd-ryzen-ai-7-350.html).
- Gorgon Point: [AI 5 430](https://www.amd.com/en/products/processors/laptop/ryzen/ai-400-series/amd-ryzen-ai-5-430.html), [AI 7 445](https://www.amd.com/en/products/processors/laptop/ryzen/ai-400-series/amd-ryzen-ai-7-445.html), [AI 7 450](https://www.amd.com/en/products/processors/laptop/ryzen/ai-400-series/amd-ryzen-ai-7-450.html).

**Icecat** (open, `live.icecat.biz/api?UserName=openIcecat-live&Language=de&…`):
- Lenovo: [21MW00AYGE](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Lenovo&ProductCode=21MW00AYGE), [21MW007VGE](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Lenovo&ProductCode=21MW007VGE), [21UT004QGE](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Lenovo&ProductCode=21UT004QGE), [21UT000RGE](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Lenovo&ProductCode=21UT000RGE), [21ST004GGE](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Lenovo&ProductCode=21ST004GGE), [21ST001YGE](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&Brand=Lenovo&ProductCode=21ST001YGE).
- По EAN: [IdeaPad Slim 5 83S2003GGE](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&GTIN=0199274450946), [83S2000BGE](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&GTIN=0199273885022), [Slim 3 83K800CGGE](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&GTIN=0199274450397), [Acer A16-61M-R2R1](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&GTIN=4711474850324), [A16-61M-R8T1](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&GTIN=4711474665621), [Swift Air 16](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&GTIN=4711474856227), [Swift Go 16](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&GTIN=4711474416001), [Aspire Go 15](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&GTIN=4711474910431), [Nitro V 16 AI](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&GTIN=4711474531131), [MSI Venture A16](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&GTIN=4711377358880), [Medion Avantum 15 E1](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&GTIN=4061275237580), [Gigabyte A16 3VH](https://live.icecat.biz/api?UserName=openIcecat-live&Language=de&GTIN=4719331766764).

**notebookcheck** (тесты, даты публикации — из списка NBC):
- Список AMD 15–16": [Laptop-Search, cpu_manu=AMD, 15–16,1"](https://www.notebookcheck.net/Laptop-Search.8223.0.html?&cpu_manu=4&inch_from=15&inch_to=16.1&orderby=0&search=1).
- Lenovo:
  - ThinkPad: [E16 G2 AMD](https://www.notebookcheck.net/Lenovo-ThinkPad-E16-Gen-2-AMD-laptop-review-Cuts-corners-mostly-in-the-right-places.899320.0.html), [L16 G1 AMD](https://www.notebookcheck.net/Lenovo-ThinkPad-L16-Gen-1-AMD-laptop-review-Powerful-hardware-in-a-modest-guise.901298.0.html), [L16 G2 AMD](https://www.notebookcheck.net/This-affordable-laptop-has-32-GB-RAM-for-cheap-Lenovo-ThinkPad-L16-Gen-2-AMD-review.1144661.0.html), [T16 G4 AMD](https://www.notebookcheck.net/Large-business-laptop-with-AMD-Ryzen-Pro-impresses-Lenovo-ThinkPad-T16-Gen-4-review.1167534.0.html), [T16 G5 AMD](https://www.notebookcheck.net/Premium-business-laptop-with-a-budget-display-Lenovo-ThinkPad-T16-Gen-5-AMD-Review.1307940.0.html), [P16s G4 AMD](https://www.notebookcheck.net/This-is-the-most-powerful-16-inch-AMD-ThinkPad-laptop-Lenovo-ThinkPad-P16s-Gen-4-review-with-Ryzen-AI-9-HX.1135080.0.html);
  - ThinkBook и IdeaPad: [ThinkBook 16 G6](https://www.notebookcheck.net/Lenovo-ThinkBook-16-G6-review-The-inexpensive-multimedia-laptop-with-a-Ryzen-7000.774481.0.html), [IdeaPad Slim 5 16AKP10](https://www.notebookcheck.net/Dual-debut-in-the-Lenovo-IdeaPad-Slim-5-16-Ryzen-AI-5-330-and-Radeon-820M-in-review.1166676.0.html), [IdeaPad Slim 5 15ARP10](https://www.notebookcheck.net/Lenovo-IdeaPad-Slim-5-15-laptop-review-Great-value-for-money-with-an-AMD-SoC-and-an-aluminum-case.945877.0.html), [IdeaPad 5 2-in-1 15AGP11](https://www.notebookcheck.net/Lenovo-IdeaPad-5-2-in-1-15-review-Ryzen-AI-5-430-performance-debut.1270312.0.html), [Yoga 7 2-in-1 16AGP11](https://www.notebookcheck.net/Lenovo-Yoga-7-2-in-1-16AGP11-review-Latest-AMD-Ryzen-AI-7-refresh-lags-behind-Intel.1257880.0.html);
  - LOQ и Legion: [LOQ 15AHP10](https://www.notebookcheck.net/Lenovo-LOQ-15-laptop-review-The-mobile-RTX-5060-celebrates-its-debut.1050248.0.html), [LOQ 15AHP11](https://www.notebookcheck.net/Eyesore-or-eye-catcher-Lenovo-LOQ-15-gaming-laptop-review.1338691.0.html), [Legion 5 15AHP10](https://www.notebookcheck.net/The-best-mainstream-gamer-in-2025-Lenovo-Legion-5-15-Laptop-Review.1047975.0.html), [Legion 5 15AGP11](https://www.notebookcheck.net/OLED-AMD-gamer-with-32-GB-RAM-Lenovo-Legion-5-15AGP11-laptop-review.1333407.0.html).
- HP: [EliteBook 8 G1a 16](https://www.notebookcheck.net/HP-EliteBook-8-G1a-16-AI-laptop-review-Redesigned-inside-and-out.1103659.0.html), [EliteBook 8 G2a 16](https://www.notebookcheck.net/Surprisingly-fast-with-32-GB-RAM-and-Ryzen-7-HP-EliteBook-8-G2a-16-laptop-review.1358548.0.html), [EliteBook 865 G10](https://www.notebookcheck.net/HP-EliteBook-865-G10-laptop-review-Capable-business-laptop-ruined-by-Sure-View.809651.0.html), [HP 255 G10](https://www.notebookcheck.net/HP-255-G10-with-7120U-review-Small-budget-low-performance.1293092.0.html), [Pavilion 16](https://www.notebookcheck.net/HP-Pavilion-16-review-Budget-AMD-CPU-in-a-stylish-laptop.959151.0.html), [Envy x360 16](https://www.notebookcheck.net/HP-Envy-x360-2-in-1-16-review-Ryzen-7-8840HS-beats-Core-Ultra-7-155U.837856.0.html), [Omen 16](https://www.notebookcheck.net/The-best-budget-gamer-HP-Omen-16-laptop-review.1135455.0.html), [Victus 15 (Intel)](https://www.notebookcheck.net/A-budget-gamer-for-1-200-HP-Victus-15-RTX-5050-laptop-review.1147790.0.html).
- Dell и Dynabook: [Dell Pro 5 16](https://www.notebookcheck.net/Dell-Pro-5-16-P516265-review-Traditional-and-reliable.1342884.0.html), [Dynabook Tecra A65-M](https://www.notebookcheck.net/Dynabook-Tecra-A65-M-laptop-review-Suitable-ThinkPad-E-or-EliteBook-alternative.1202807.0.html).
- ASUS: [Vivobook 16 M1606K](https://www.notebookcheck.net/Asus-Vivobook-16-laptop-review-AI-features-at-the-forefront-genuine-productivity-boost-or-marketing-hype.971144.0.html), [ExpertBook B1](https://www.notebookcheck.net/Asus-ExpertBook-B1-review-The-business-laptop-with-Win-11-Pro-and-a-3-year-warranty-for-750.975913.0.html), [ExpertBook PM3](https://www.notebookcheck.net/Asus-ExpertBook-PM3-Review-Office-laptop-with-AMD-long-battery-life-and-Copilot.1200511.0.html), [ExpertBook PM5 G2](https://www.notebookcheck.net/AMD-business-laptop-with-a-great-144-Hz-IPS-display-Asus-ExpertBook-PM5-G2-review.1368549.0.html), [TUF A16 FA608UP](https://www.notebookcheck.net/Asus-TUF-Gaming-A16-Laptop-Review-A-EUR2-200-gamble-for-Zen-4-Hawk-Point-RTX-5070.1122766.0.html), [TUF A15 2024](https://www.notebookcheck.net/Asus-TUF-Gaming-A15-2024-review-RTX-4060-power-moderate-price-long-battery-life.864614.0.html), [Zenbook S16](https://www.notebookcheck.net/The-perfect-everyday-laptop-with-AMD-Ryzen-400-Asus-Zenbook-S16-OLED-review.1221965.0.html), [ProArt P16](https://www.notebookcheck.net/4K-OLED-is-replaced-by-120-Hz-2-8K-OLED-Asus-ProArt-P16-with-RTX-5070-Laptop-review.1026301.0.html).
- Acer: [Swift Go 16 AI](https://www.notebookcheck.net/Solid-performance-and-colorful-OLED-Acer-Swift-Go-16-AI-review.1168834.0.html), [Nitro V 16 AI](https://www.notebookcheck.net/Acer-Nitro-V-16-AI-Review-Affordable-gaming-laptop-with-great-battery-life.1156010.0.html), [Nitro V 16 ANV16-41](https://www.notebookcheck.net/Acer-Nitro-V-16-ANV16-41-review-An-affordable-gaming-laptop-with-a-hitch.928048.0.html), [Aspire 3 A315-24P](https://www.notebookcheck.net/Acer-Aspire-3-Laptop-Review-An-affordable-Mendocino-offering-with-excellent-battery-life-and-a-sub-par-screen.704064.0.html).
- MSI и Gigabyte: [MSI Katana A15 AI](https://www.notebookcheck.net/MSI-Katana-A15-AI-laptop-review-RTX-4070-gamer-hurt-by-cost-saving-measures.936689.0.html), [MSI Prestige A16 AI+](https://www.notebookcheck.net/MSI-Prestige-A16-AI-review-Multimedia-laptop-with-powerful-Ryzen-9-365.949210.0.html), [Gigabyte Aero X16](https://www.notebookcheck.net/Gigabyte-Aero-X16-Review-Sleek-AMD-Zen-5-gaming-machine-with-Nvidia-RTX-5070-Laptop-and-upgradeable-RAM.1022304.0.html), [Gigabyte Gaming A16 (Intel)](https://www.notebookcheck.net/An-affordable-RTX-5070-laptop-Gigabyte-Gaming-A16-review.1072350.0.html).
- XMG: [Core 15 M25](https://www.notebookcheck.net/German-competitor-to-the-Legion-5-XMG-Core-15-M25-gaming-laptop-review.1126351.0.html), [Core 16 M25](https://www.notebookcheck.net/XMG-Core-16-M25-review-AMD-gaming-laptop-with-300-Hz-display-and-RTX-5070.1132775.0.html), [Core 16 VE M25](https://www.notebookcheck.net/Challenge-to-the-Lenovo-Legion-XMG-Core-16-VE-M25-gaming-laptop-review.1202743.0.html), [Core 15 M24](https://www.notebookcheck.net/SCHENKER-XMG-Core-15-M24-laptop-review-A-premium-metal-cased-gaming-machine-from-Germany.848771.0.html), [Apex 16 Max](https://www.notebookcheck.net/AMD-Ryzen-9-9955HX-RTX-5070-Ti-and-mini-LED-XMG-Apex-16-Max-gaming-laptop-review.1206725.0.html).
- Аналитика: [Gorgon Point](https://www.notebookcheck.net/AMD-Ryzen-AI-400-Performance-Analysis-Gorgon-Point-debuts-with-only-minor-improvements.1211982.0.html).

**Производители (прочие):** [Framework Laptop 16](https://frame.work/de/en/laptop16), [Framework 16 DIY AI 300](https://frame.work/de/en/products/laptop16-diy-amd-ai300), [Tuxedo InfinityBook Pro 15 Gen10 AMD](https://www.tuxedocomputers.com/de/TUXEDO-InfinityBook-Pro-15-Gen10-AMD.tuxedo), [Tuxedo InfinityBook Max 15 Gen10 AMD](https://www.tuxedocomputers.com/de/TUXEDO-InfinityBook-Max-15-Gen10-AMD.tuxedo), [Tuxedo Aura 15 Gen1 (архив)](https://www.tuxedocomputers.com/en/Linux-Hardware/Linux-Notebooks/15-16-inch/TUXEDO-Aura-15-Gen1.tuxedo).

**Цены** (billiger.de, 30.09.2026): ссылки в таблице «Кандидаты» и в разделах брендов. Поиск — `billiger.de/search?searchstring=Ryzen&filter=f_category_2303,f_4266_32000000000x32000000000,f_5198_1000000000000x1000000000000,f_162_15x16&order=s_price`.

**Внутренние заметки:** [`../../Intel/notes/brands.md`](../../Intel/notes/brands.md), [`hevc-audit.md`](../../Intel/notes/hevc-audit.md), [`intel-cpu.md`](../../Intel/notes/intel-cpu.md), [`sweep-16gb-plus-stick.md`](../../Intel/notes/sweep-16gb-plus-stick.md), [`../../Intel/REPORT.md`](../../Intel/REPORT.md).
