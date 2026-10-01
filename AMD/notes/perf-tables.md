# Производительность процессоров и видеоядер для монтажа 4K

_Снято 30.09.2026. Страницы notebookcheck.net скачаны через curl (открылись без защиты), числа вынуты скриптом из таблиц на каждой странице. Ссылка на страницу NBC — в имени процессора или видеоядра._
_Оплата и экран в этой заметке не учитываются — только скорость и кодеки._
_Разделы: 1 — процессоры; 2 — видеоядра (3DMark); 3 — Puget Bench (Resolve, Premiere); 4 — кодеки; 5 — одна планка против двух; 6 — разброс по ноутбукам; 7 — итог. Puget — curl по страницам сравнения; поиск статей NBC про одноканал — Google в Chrome (google.de), страницы NBC — curl._

## Как читать

- **Медиана NBC** — поле «median» на странице процессора. В скобках — сколько ноутбуков NBC протестировал (n).
  n = 1–2 — это один-два ноутбука, а не медиана: такие числа сильно зависят от лимита мощности конкретной модели.
- **У видеоядер** на странице NBC поля «median» нет (там ошибка «could not paint bar»). Медиану я посчитал сам по списку тестов на странице
  и сверил с таблицей [Mobile Graphics Cards — Benchmark List](https://www.notebookcheck.net/Mobile-Graphics-Cards-Benchmark-List.844.0.html): все Time Spy и Fire Strike совпали до единицы.
- У процессоров посчитанная медиана тоже совпала с полем NBC, кроме Ryzen 7 7840HS: там расхождение 0,1–0,5 % (16 156 у NBC, 16 123 по списку). В таблице — число NBC.
- **Blender 3.3 Classroom CPU** — время рендера в секундах: меньше — лучше.
- **HandBrake NBC не тестирует.** Ближе всего — HWBOT x265 4K: программное кодирование HEVC 4K на процессоре, кадр/с (больше — лучше).
- **TDP** — базовое значение со страницы NBC. Реальная мощность в ноутбуке другая: у одного процессора бывает от 15 до 80 Вт (раздел 6).
- **Geekbench 6** — группа «Geekbench 6.7» на NBC: в ней больше всего тестов. Старые группы (6.0–6.5) в таблицу не брал.

## 1. Процессоры

| CPU (страница NBC) | Кодовое имя (NBC) | Ядра/потоки | TDP | iGPU | CB R23 Multi | CB R23 Single | CB 2024 Multi | CB 2024 Single | GB6 Multi | GB6 Single | Blender, с ↓ | x265 4K, fps |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [Core i5-13420H](https://www.notebookcheck.net/Intel-Core-i5-13420H-Processor-Benchmarks-and-Specs.677510.0.html) | Raptor Lake-H | 8/12 (4P+4E) | 45 Вт | UHD Xe G4 48EUs | 11 084 (5) | 1 689 (5) | 502 (4) | 98 (4) | 8 444 (5) | 2 254 (5) | 528 (4) | 12,1 (5) |
| [Core i7-13620H](https://www.notebookcheck.net/Intel-Core-i7-13620H-Processor-Benchmarks-and-Specs.677505.0.html) | Raptor Lake-H | 10/16 (6P+4E) | 45 Вт | UHD 64EUs | 15 176 (7) | 1 833 (7) | 696 (3) | 110 (3) | 11 723 (6) | 2 568 (6) | 391 (7) | 16,6 (7) |
| [Core i9-13900H](https://www.notebookcheck.net/Intel-Core-i9-13900H-Processor-Benchmarks-and-Specs.677396.0.html) | Raptor Lake-H | 14/20 (6P+8E) | 45 Вт | Iris Xe G7 96EUs | 17 471 (28) | 1 964 (26) | 760 (4) | 104 (4) | 12 644 (14) | 2 654 (14) | 338 (24) | 18,9 (25) |
| [Core 5 210H](https://www.notebookcheck.net/Intel-Core-5-210H-Processor-Benchmarks-and-Specs.936302.0.html) | Raptor Lake-H Refresh | 8/12 (4P+4E) | 45 Вт | UHD Xe G4 48EUs | 11 830 (3) | 1 771 (3) | 686 (3) | 105 (3) | 9 616 (4) | 2 416 (4) | 520 (3) | 13,4 (3) |
| [Core 5 220H](https://www.notebookcheck.net/Intel-Core-5-220H-Processor-Benchmarks-and-Specs.936297.0.html) | Raptor Lake-H Refresh | 12/16 (4P+8E) | 45 Вт | Iris Xe G7 80EUs | 11 198 (1) | 1 853 (1) | 655 (1) | 108 (1) | 11 280 (1) | 2 501 (1) | 505 (1) | 12,5 (1) |
| [Core 7 240H](https://www.notebookcheck.net/Intel-Core-7-240H-Processor-Benchmarks-and-Specs.936272.0.html) | Raptor Lake-H Refresh | 10/16 (6P+4E) | 45 Вт | UHD 64EUs | 15 225 (4) | 1 715 (4) | 832 (4) | 107 (4) | 12 302 (5) | 2 394 (5) | 372 (4) | 17,0 (4) |
| [Core 7 250H](https://www.notebookcheck.net/Intel-Core-7-250H-Processor-Benchmarks-and-Specs.936248.0.html) | Raptor Lake-H Refresh | 14/20 (6P+8E) | 45 Вт | Iris Xe G7 96EUs | 16 561 (1) | 1 931 (1) | 1 113 (1) | 122 (1) | 12 521 (2) | 2 792 (2) | 306 (1) | 21,2 (1) |
| [Core Ultra 5 125H](https://www.notebookcheck.net/Intel-Core-Ultra-5-125H-Processor-Benchmarks-and-Specs.783325.0.html) | Meteor Lake-H | 14/18 (4P+8E+2LPE) | 28 Вт | Arc 7-Core | 12 804 (8) | 1 648 (8) | 616 (6) | 100 (6) | 11 268 (7) | 2 279 (7) | 479 (8) | 13,8 (8) |
| [Core Ultra 5 135H](https://www.notebookcheck.net/Intel-Core-Ultra-5-135H-Processor-Benchmarks-and-Specs.783324.0.html) | Meteor Lake-H | 14/18 (4P+8E+2LPE) | 28 Вт | Arc 8-Core | 11 876 (2) | 1 700 (2) | 575 (1) | 99 (1) | 10 368 (2) | 2 278 (2) | 542 (1) | 12,5 (1) |
| [Core Ultra 7 155H](https://www.notebookcheck.net/Intel-Core-Ultra-7-155H-Processor-Benchmarks-and-Specs.783323.0.html) | Meteor Lake-H | 16/22 (6P+8E+2LPE) | 28 Вт | Arc 8-Core | 15 028 (52) | 1 743 (52) | 789 (33) | 102 (24) | 12 385 (55) | 2 409 (52) | 380 (51) | 16,6 (50) |
| [Core Ultra 5 125U](https://www.notebookcheck.net/Intel-Core-Ultra-5-125U-Processor-Benchmarks-and-Specs.783351.0.html) | Meteor Lake-P | 12/14 (2P+8E+2LPE) | 15 Вт | Graphics 4-Core | 9 799 (9) | 1 561 (9) | 508 (5) | 92 (4) | 9 351 (9) | 2 150 (9) | 652 (9) | 11,1 (9) |
| [Core Ultra 5 225U](https://www.notebookcheck.net/Intel-Core-Ultra-5-225U-Processor-Benchmarks-and-Specs.943067.0.html) | Arrow Lake-U | 12/14 (2P+8E+2LPE) | 15 Вт | Graphics 4-Core | 11 844 (2) | 1 731 (2) | 621 (1) | 102 (1) | 9 886 (2) | 2 372 (2) | 520 (2) | 13,0 (2) |
| [Core Ultra 5 225H](https://www.notebookcheck.net/Intel-Core-Ultra-5-225H-Processor-Benchmarks-and-Specs.944682.0.html) | Arrow Lake-H | 14/14 (4P+8E+2LPE) | 28 Вт | Arc 130T | 14 630 (2) | 1 969 (2) | 720 (2) | 119 (2) | 12 099 (3) | 2 733 (3) | 435 (2) | 16,0 (2) |
| [Core Ultra 5 235H](https://www.notebookcheck.net/Intel-Core-Ultra-5-235H-Processor-Benchmarks-and-Specs.944681.0.html) | Arrow Lake-H | 14/14 (4P+8E+2LPE) | 28 Вт | Arc 140T | нет | нет | нет | нет | 14 451 (1) | 2 743 (1) | нет | нет |
| [Core Ultra 7 255H](https://www.notebookcheck.net/Intel-Core-Ultra-7-255H-Processor-Benchmarks-and-Specs.944139.0.html) | Arrow Lake-H | 16/16 (6P+8E+2LPE) | 28 Вт | Arc 140T | 17 845 (20) | 2 061 (20) | 1 053 (13) | 124 (15) | 15 223 (20) | 2 866 (20) | 326 (18) | 21,4 (19) |
| [Core Ultra 5 226V](https://www.notebookcheck.net/Intel-Core-Ultra-5-226V-Processor-Benchmarks-and-Specs.893266.0.html) | Lunar Lake | 8/8 (4P+4E) | 17 Вт | Arc 130V | 9 850 (8) | 1 746 (8) | 539 (7) | 113 (7) | 9 965 (8) | 2 584 (9) | 584 (8) | 12,4 (8) |
| [Core Ultra 5 228V](https://www.notebookcheck.net/Intel-Core-Ultra-5-228V-Processor-Benchmarks-and-Specs.893277.0.html) | Lunar Lake | 8/8 (4P+4E) | 17 Вт | Arc 130V | 9 932 (2) | 1 758 (2) | 494 (2) | 105 (2) | 10 313 (3) | 2 585 (3) | 689 (2) | 11,2 (2) |
| [Core Ultra 7 256V](https://www.notebookcheck.net/Intel-Core-Ultra-7-256V-Processor-Benchmarks-and-Specs.892554.0.html) | Lunar Lake | 8/8 (4P+4E) | 17 Вт | Arc 140V | 10 407 (9) | 1 880 (9) | 584 (8) | 120 (8) | 10 962 (10) | 2 756 (10) | 557 (8) | 13,1 (8) |
| [Core Ultra 7 258V](https://www.notebookcheck.net/Intel-Core-Ultra-7-258V-Processor-Benchmarks-and-Specs.892883.0.html) | Lunar Lake | 8/8 (4P+4E) | 17 Вт | Arc 140V | 10 301 (25) | 1 872 (25) | 573 (24) | 120 (18) | 10 966 (24) | 2 754 (24) | 584 (23) | 12,4 (24) |
| [Core Ultra 5 325](https://www.notebookcheck.net/Intel-Core-Ultra-5-325-Processor-Benchmarks-and-Specs.1196417.0.html) | Panther Lake | 8/8 (4P+4LPE) | 25 Вт | Graphics 4 Xe3 Panther Lake | 10 984 (4) | 1 894 (4) | 637 (2) | 114 (2) | 11 033 (5) | 2 576 (5) | 529 (4) | 14,1 (4) |
| [Core Ultra 5 336H](https://www.notebookcheck.net/Intel-Core-Ultra-5-336H-Processor-Benchmarks-and-Specs.1196625.0.html) | Panther Lake | 12/12 (4P+4E+4LPE) | 25 Вт | Graphics 4 Xe3 Panther Lake | нет | нет | нет | нет | 13 882 (1) | 2 752 (1) | нет | нет |
| [Core Ultra 7 356H](https://www.notebookcheck.net/Intel-Core-Ultra-7-356H-Processor-Benchmarks-and-Specs.1196617.0.html) | Panther Lake | 16/16 (4P+8E+4LPE) | 25 Вт | Graphics 4 Xe3 Panther Lake | 18 395 (5) | 2 040 (5) | 1 044 (5) | 117 (5) | 16 012 (6) | 2 775 (6) | 309 (5) | 20,7 (5) |
| [Ryzen 5 7535HS](https://www.notebookcheck.net/AMD-Ryzen-5-7535HS-Processor-Benchmarks-and-Specs.681414.0.html) | Rembrandt R | 6/12 (6×Zen 3+) | 35 Вт | Radeon 660M | 8 613 (3) | 1 445 (3) | 459 (1) | 83 (1) | 8 094 (3) | 1 988 (3) | 643 (3) | 11,3 (3) |
| [Ryzen 7 7735HS](https://www.notebookcheck.net/AMD-Ryzen-7-7735HS-Processor-Benchmarks-and-Specs.681410.0.html) | Rembrandt-HS Refresh | 8/16 (8×Zen 3+) | 35 Вт | Radeon 680M | 13 106 (15) | 1 546 (15) | 620 (5) | 90 (5) | 9 970 (9) | 2 098 (9) | 394 (16) | 16,0 (15) |
| [Ryzen 5 220](https://www.notebookcheck.net/AMD-Ryzen-5-220-Processor-Benchmarks-and-Specs.946309.0.html) | Hawk Point-U (Zen 4 + Zen 4c) | 6/12 (2×Zen 4+4×Zen 4c) | 28 Вт | Radeon 740M | нет | нет | нет | нет | 8 065 (1) | 2 476 (1) | нет | нет |
| [Ryzen 5 230](https://www.notebookcheck.net/AMD-Ryzen-5-230-Processor-Benchmarks-and-Specs.946303.0.html) | Hawk Point-U (Zen 4) | 6/12 (6×Zen 4) | 28 Вт | Radeon 760M | нет | нет | нет | нет | 8 437 (1) | 2 448 (1) | нет | нет |
| [Ryzen 5 240](https://www.notebookcheck.net/AMD-Ryzen-5-240-Processor-Benchmarks-and-Specs.946292.0.html) | Hawk Point-HS (Zen 4) | 6/12 (6×Zen 4) | 45 Вт | Radeon 760M | 13 013 (1) | 1 742 (1) | 654 (1) | 104 (1) | 10 870 (2) | 2 582 (2) | 396 (1) | 16,6 (1) |
| [Ryzen 7 250](https://www.notebookcheck.net/AMD-Ryzen-7-250-Processor-Benchmarks-and-Specs.945901.0.html) | Hawk Point-U (Zen 4) | 8/16 (8×Zen 4) | 28 Вт | Radeon 780M | 14 676 (5) | 1 715 (5) | 831 (3) | 101 (3) | 9 956 (5) | 2 585 (5) | 371 (5) | 15,9 (5) |
| [Ryzen 7 260](https://www.notebookcheck.net/AMD-Ryzen-7-260-Processor-Benchmarks-and-Specs.945912.0.html) | Hawk Point-HS (Zen 4) | 8/16 (8×Zen 4) | 45 Вт | Radeon 780M | 17 212 (6) | 1 770 (6) | 962 (4) | 104 (4) | 12 795 (6) | 2 668 (6) | 298 (6) | 21,2 (6) |
| [Ryzen 7 7840HS](https://www.notebookcheck.net/AMD-Ryzen-7-7840HS-Processor-Benchmarks-and-Specs.680876.0.html) | Phoenix-HS (Zen 4) | 8/16 (8×Zen 4) | 35 Вт | Radeon 780M | 16 156 (19) | 1 775 (19) | 900 (6) | 106 (6) | 13 066 (21) | 2 664 (21) | 320 (20) | 20,4 (20) |
| [Ryzen 7 8845HS](https://www.notebookcheck.net/AMD-Ryzen-7-8845HS-Processor-Benchmarks-and-Specs.780991.0.html) | Hawk Point-HS (Zen 4) | 8/16 (8×Zen 4) | 45 Вт | Radeon 780M | 16 192 (13) | 1 769 (13) | 902 (11) | 104 (8) | 12 998 (18) | 2 630 (16) | 318 (13) | 20,4 (13) |
| [Ryzen 5 8645HS](https://www.notebookcheck.net/AMD-Ryzen-5-8645HS-Processor-Benchmarks-and-Specs.780989.0.html) | Hawk Point-HS (Zen 4) | 6/12 (6×Zen 4) | 45 Вт | Radeon 760M | 13 220 (1) | 1 714 (1) | 727 (1) | 100 (1) | 10 882 (1) | 2 570 (1) | 389 (1) | 17,2 (1) |
| [Ryzen AI 5 330](https://www.notebookcheck.net/AMD-Ryzen-AI-5-330-Processor-Benchmarks-and-Specs.1049553.0.html) | Krackan Point 2 (Zen 5) | 4/8 (1×Zen 5+3×Zen 5c) | 28 Вт | Radeon 820M | 7 840 (1) | 1 812 (1) | нет | нет | 7 600 (2) | 2 466 (2) | 657 (1) | 10,3 (1) |
| [Ryzen AI 5 340](https://www.notebookcheck.net/AMD-Ryzen-AI-5-340-Processor-Benchmarks-and-Specs.950403.0.html) | Krackan Point (Zen 5) | 6/12 (3×Zen 5+3×Zen 5c) | 28 Вт | Radeon 840M | 12 532 (2) | 1 916 (2) | 668 (2) | 112 (2) | 10 765 (2) | 2 782 (2) | 410 (2) | 15,0 (2) |
| [Ryzen AI 7 350](https://www.notebookcheck.net/AMD-Ryzen-AI-7-350-Processor-Benchmarks-and-Specs.949825.0.html) | Krackan Point (Zen 5) | 8/16 (4×Zen 5+4×Zen 5c) | 28 Вт | Radeon 860M | 16 014 (18) | 1 958 (18) | 901 (15) | 116 (15) | 12 835 (17) | 2 853 (17) | 322 (17) | 20,6 (16) |
| [Ryzen AI 7 445](https://www.notebookcheck.net/AMD-Ryzen-AI-7-445-Processor-Benchmarks-and-Specs.1197764.0.html) | Gorgon Point | 6/12 (2×Zen 5+4×Zen 5c) | 28 Вт | Radeon 840M | 10 590 (2) | 1 806 (2) | 600 (2) | 106 (2) | 10 324 (2) | 2 608 (2) | 488 (2) | 14,3 (2) |
| [Ryzen AI 7 450](https://www.notebookcheck.net/AMD-Ryzen-AI-7-450-Processor-Benchmarks-and-Specs.1197762.0.html) | Gorgon Point | 8/16 (4×Zen 5+4×Zen 5c) | 28 Вт | Radeon 860M | 17 302 (4) | 2 034 (4) | 921 (2) | 118 (2) | 13 789 (5) | 2 914 (5) | 294 (4) | 22,3 (4) |
| [Ryzen AI 9 365](https://www.notebookcheck.net/AMD-Ryzen-AI-9-365-Processor-Benchmarks-and-Specs.843618.0.html) | Strix Point (Zen 5) | 10/20 (4×Zen 5+6×Zen 5c) | 28 Вт | Radeon 880M | 18 698 (7) | 1 992 (7) | 992 (8) | 114 (5) | 14 262 (7) | 2 815 (7) | 270 (7) | 22,4 (7) |
| [Ryzen AI 9 HX 370](https://www.notebookcheck.net/AMD-Ryzen-AI-9-HX-370-Processor-Benchmarks-and-Specs.836729.0.html) | Strix Point-HX (Zen 5/5c) | 12/24 (4×Zen 5+8×Zen 5c) | 28 Вт | Radeon 890M | 21 761 (32) | 2 018 (25) | 1 139 (33) | 117 (23) | 14 996 (26) | 2 880 (26) | 221 (24) | 26,2 (24) |

Нет в таблице — значит, на странице NBC у процессора нет ни одного теста этого вида («на NBC нет данных»). У Core Ultra 5 235H, Core Ultra 5 336H, Ryzen 5 220 и Ryzen 5 230 есть только Geekbench одного ноутбука.

## 2. Видеоядра: 3DMark (медианы NBC)

- Формат ячейки: **медиана (n ноутбуков; минимум–максимум)**. Медиану я посчитал по списку тестов на странице GPU; для Time Spy и Fire Strike она совпала до единицы
  с [Mobile Graphics Cards — Benchmark List](https://www.notebookcheck.net/Mobile-Graphics-Cards-Benchmark-List.844.0.html) у всех 31 видеоядра (сверка скриптом 30.09.2026).
- **Steel Nomad Light** — общий балл теста (у NBC отдельного «Graphics» для него нет). Это DirectX 12 без трассировки, ближе всего к современной нагрузке на GPU.
- «Где стоит» — процессоры из раздела 1 с этим iGPU (поле GPU на странице процессора NBC). Pipelines — поле NBC (у Intel это EU/векторные блоки, у AMD и NVIDIA — шейдерные ALU); между брендами не сравнивать.
- \* У **Arc 7-Core** (Core Ultra 5 125H) на странице GPU таблиц тестов нет. Числа взяты из [Benchmark List](https://www.notebookcheck.net/Mobile-Graphics-Cards-Benchmark-List.844.0.html) (запрос со столбцами Time Spy Graphics, Fire Strike Graphics и Steel Nomad Light, 30.09.2026): 2940,5 (n8), 7612,5 (n8), 2617 (n2).
- **RTX 3050 A Laptop** (Ada, 64 бит): страница есть, тестов нет — «на NBC нет данных». В таблице ещё обычная RTX 3050 Laptop (4 ГБ) и RTX 3050 6GB Laptop: в продаже встречаются все три.
- Разброс min–max у iGPU — это в основном лимит мощности и одноканальная память (раздел 6). У NVIDIA — TGP: RTX 4060 даёт 7 484 в MSI Cyborg 15 A12VF (45 Вт) и 11 451 в XMG Core 15 M24 (140 Вт) (строки теста на странице RTX 4060).
  В списки NBC входят и мини-ПК (Beelink, Geekom, BOSGAME): у iGPU максимумы часто от них.

| GPU (страница NBC) | Где стоит (CPU из раздела 1) | Архитектура, блоки, TGP | Time Spy Graphics | Steel Nomad Light | Fire Strike Graphics |
|---|---|---|---|---|---|
| [Intel UHD Graphics Xe G4 48EUs](https://www.notebookcheck.net/Intel-Tiger-Lake-U-Xe-Graphics-G4-48-EUs-GPU-Benchmarks-and-Specs.466210.0.html) | i5-13420H, Core 5 210H | Tiger Lake Xe, 48 pipelines | 801 (14; 634–1 028) | 754 (1) | 2 469 (16; 1 602–3 588) |
| [Intel UHD Graphics 64EUs](https://www.notebookcheck.net/Intel-UHD-Graphics-64EUs-Alder-Lake-GPU-Benchmarks-and-Specs.589905.0.html) | i7-13620H, Core 7 240H | Alder Lake Xe, 64 pipelines | 1 110 (12; 830–1 336) | 976 (2; 882–1 071) | 3 894 (12; 2 592–4 567) |
| [Intel Iris Xe Graphics G7 80EUs](https://www.notebookcheck.net/Intel-Tiger-Lake-U-Xe-Graphics-G7-80EUs-GPU-Benchmarks-and-Specs.466209.0.html) | Core 5 220H | Tiger Lake Xe, 80 pipelines | 1 181 (111; 561–1 576) | 1 184 (3; 1 019–1 201) | 4 048 (114; 1 560–5 398) |
| [Intel Iris Xe Graphics G7 96EUs](https://www.notebookcheck.net/Intel-Tiger-Lake-U-Xe-Graphics-G7-96EUs-GPU-Benchmarks-and-Specs.462145.0.html) | i9-13900H, Core 7 250H | Tiger Lake Xe, 96 pipelines | 1 560 (218; 707–1 890) | 1 280 (2; 1 276–1 283) | 5 160 (222; 2 286–6 624) |
| [Intel Arc 7-Cores (Meteor Lake)](https://www.notebookcheck.net/Intel-Arc-7-Cores-iGPU-Benchmarks-and-Specs.782931.0.html) | Ultra 5 125H | Meteor Lake iGPU, Xe LPG, 7 Xe-ядер | 2 940,5 (8)* | 2 617 (2)* | 7 612,5 (8)* |
| [Intel Arc 8-Cores (Meteor Lake)](https://www.notebookcheck.net/Intel-Arc-8-Cores-iGPU-Benchmarks-and-Specs.782930.0.html) | Ultra 5 135H, Ultra 7 155H | Meteor Lake iGPU, Xe LPG, 8 pipelines | 3 270 (48; 2 018–3 770) | 2 971 (12; 2 356–3 248) | 8 477 (45; 5 568–9 692) |
| [Intel Graphics 4-Cores (Meteor/Arrow Lake-U)](https://www.notebookcheck.net/Intel-Graphics-4-Cores-iGPU-Arc-Benchmarks-and-Specs.782932.0.html) | Ultra 5 125U, Ultra 5 225U | Meteor Lake iGPU, Xe LPG, 64 pipelines | 1 902 (33; 1 530–2 144) | 1 626 (6; 1 434–1 749) | 4 973 (33; 3 838–5 554) |
| [Intel Arc 130T](https://www.notebookcheck.net/Intel-Arc-130T-Benchmarks-and-Specs.942051.0.html) | Ultra 5 225H | Xe+, 112 pipelines | 2 378 (2; 2 354–2 402) | 2 161 (2; 2 115–2 207) | 5 300 (2; 5 173–5 426) |
| [Intel Arc 140T](https://www.notebookcheck.net/Intel-Arc-140T-Benchmarks-and-Specs.942050.0.html) | Ultra 5 235H, Ultra 7 255H | Xe+, 128 pipelines | 3 843 (20; 2 466–4 387) | 3 546 (6; 2 278–3 692) | 8 664 (20; 5 433–10 742) |
| [Intel Arc 130V](https://www.notebookcheck.net/Intel-Arc-Graphics-130V-Benchmarks-and-Specs.854992.0.html) | Ultra 5 226V/228V | Lunar Lake iGPU, Xe² Battlemage, 7 pipelines | 3 401 (10; 3 148–3 543) | 2 670 (5; 2 413–2 877) | 8 478 (10; 7 536–8 755) |
| [Intel Arc 140V](https://www.notebookcheck.net/Intel-Arc-Graphics-140V-Benchmarks-and-Specs.854991.0.html) | Ultra 7 256V/258V | Lunar Lake iGPU, Xe² Battlemage, 8 pipelines | 4 044 (42; 2 754–4 415) | 3 275 (19; 2 596–3 555) | 9 819 (39; 6 209–10 476) |
| [Intel Arc B370 (10 Xe3)](https://www.notebookcheck.net/Intel-Arc-B370-10-Xe3-Panther-Lake-iGPU-Benchmarks-and-Specs.1193672.0.html) | (Ultra 5 338H — нет в списке CPU) | Panther Lake iGPU, Xe3, 80 pipelines | 6 050 (2; 5 933–6 167) | 5 376 (2; 5 354–5 398) | 14 832 (2; 14 699–14 966) |
| [Intel Arc B390 (12 Xe3)](https://www.notebookcheck.net/Intel-Arc-B390-12-Xe3-Panther-Lake-iGPU-Benchmarks-and-Specs.1169503.0.html) | (Ultra X7 358H, X9 388H — нет в списке) | Panther Lake iGPU, 96 pipelines | 6 653 (22; 4 567–7 257) | 5 897 (7; 5 562–6 338) | 17 018 (15; 13 410–18 327) |
| [Intel Graphics 4 Xe3 (Panther Lake)](https://www.notebookcheck.net/Intel-Graphics-4-Xe3-Panther-Lake-Benchmarks-and-Specs.1193658.0.html) | Ultra 5 325, 336H, Ultra 7 356H | Panther Lake, 32 pipelines | 2 903 (20; 2 117–3 136) | 2 343 (4; 2 213–2 501) | 7 028 (20; 5 127–7 415) |
| [AMD Radeon 660M](https://www.notebookcheck.net/AMD-Radeon-660M-GPU-Benchmarks-and-Specs.589879.0.html) | R5 7535HS | RDNA 2 Rembrandt, RDNA 2, 384 pipelines | 1 535 (13; 1 016–1 588) | нет | 4 881 (13; 3 447–4 993) |
| [AMD Radeon 680M](https://www.notebookcheck.net/AMD-Radeon-680M-GPU-Benchmarks-and-Specs.589860.0.html) | R7 7735HS | RDNA 2 Rembrandt, RDNA 2, 768 pipelines | 2 303 (41; 1 359–2 607) | 2 119 (3; 2 045–2 355) | 6 848 (41; 3 791–7 706) |
| [AMD Radeon 740M](https://www.notebookcheck.net/AMD-Radeon-740M-GPU-Benchmarks-and-Specs.716455.0.html) | Ryzen 5 220 | Phoenix, RDNA 3, 256 pipelines | 1 527 (5; 1 136–1 699) | 1 175 (1) | 4 625 (5; 3 421–5 135) |
| [AMD Radeon 760M](https://www.notebookcheck.net/AMD-Radeon-760M-GPU-Benchmarks-and-Specs.680920.0.html) | Ryzen 5 230/240, R5 8645HS | Phoenix, RDNA 3, 512 pipelines | 2 281 (5; 1 997–2 495) | нет | 6 558 (5; 6 121–7 004) |
| [AMD Radeon 780M](https://www.notebookcheck.net/AMD-Radeon-780M-GPU-Benchmarks-and-Specs.680539.0.html) | Ryzen 7 250/260, 7840HS, 8845HS | Phoenix, RDNA 3, 768 pipelines | 2 808 (81; 1 496–3 196) | 2 775 (12; 2 447–2 972) | 7 985 (81; 4 550–8 904) |
| [AMD Radeon 820M](https://www.notebookcheck.net/AMD-Radeon-820M-Benchmarks-and-Specs.1059782.0.html) | Ryzen AI 5 330 | Krackan Point, RDNA 3+, 128 pipelines | 786 (1) | нет | 3 155 (1) |
| [AMD Radeon 840M](https://www.notebookcheck.net/AMD-Radeon-840M-Benchmarks-and-Specs.950405.0.html) | Ryzen AI 5 340, AI 7 445 | Krackan Point, RDNA 3+, 256 pipelines | 1 415 (7; 1 335–1 705) | нет | 4 536 (7; 3 706–5 606) |
| [AMD Radeon 860M](https://www.notebookcheck.net/AMD-Radeon-860M-Benchmarks-and-Specs.949852.0.html) | Ryzen AI 7 350/450 | Krackan Point, RDNA 3+, 512 pipelines | 2 565 (23; 1 656–2 987) | 2 380 (11; 1 491–2 605) | 7 131 (23; 4 376–7 935) |
| [AMD Radeon 880M](https://www.notebookcheck.net/AMD-Radeon-880M-iGPU-Benchmarks-and-Specs.843543.0.html) | Ryzen AI 9 365 | Strix Point, RDNA 3+, 768 pipelines | 3 335 (8; 2 300–3 688) | 3 325 (3; 3 281–3 421) | 9 408 (8; 7 404–9 651) |
| [AMD Radeon 890M](https://www.notebookcheck.net/AMD-Radeon-890M-Benchmarks-and-Specs.843536.0.html) | Ryzen AI 9 HX 370 | Strix Point, RDNA 3+, 1024 pipelines | 3 331 (33; 1 918–3 753) | 3 283 (10; 2 082–3 511) | 8 933 (32; 5 173–10 037) |
| [NVIDIA RTX 3050 Laptop](https://www.notebookcheck.net/NVIDIA-GeForce-RTX-3050-Laptop-GPU-Benchmarks-and-Specs.513790.0.html) | дискретная | GN20-P0, Ampere, 2048 pipelines, TGP 35–80 Вт, GDDR6 | 4 497 (23; 3 281–5 295) | 3 858 (4; 3 766–3 940) | 11 949 (22; 9 138–14 157) |
| [NVIDIA RTX 3050 6GB Laptop](https://www.notebookcheck.net/NVIDIA-GeForce-RTX-3050-6GB-Laptop-GPU-GPU-Benchmarks-and-Specs.692276.0.html) | дискретная | GN20-P0-R 6GB, Ampere, 2560 pipelines, TGP 35–80 Вт, GDDR6 | 4 571 (3; 4 501–4 820) | нет | 11 973 (4; 11 887–12 618) |
| [NVIDIA RTX 3050 A Laptop](https://www.notebookcheck.net/NVIDIA-GeForce-RTX-3050-A-Laptop-GPU-Benchmarks-and-Specs.867762.0.html) | дискретная | Ada Lovelace, 1792 pipelines, TGP 35–80 Вт, GDDR6 | нет | нет | нет |
| [NVIDIA RTX 4050 Laptop](https://www.notebookcheck.net/NVIDIA-GeForce-RTX-4050-Laptop-GPU-Benchmarks-and-Specs.675695.0.html) | дискретная | GN21-X2, Ada Lovelace, 2560 pipelines, TGP 35–115 Вт, GDDR6 | 8 125 (41; 5 107–9 040) | 6 206 (2; 5 157–7 254) | 21 949 (41; 13 591–24 007) |
| [NVIDIA RTX 4060 Laptop](https://www.notebookcheck.net/NVIDIA-GeForce-RTX-4060-Laptop-GPU-Benchmarks-and-Specs.675692.0.html) | дискретная | GN21-X4, Ada Lovelace, 3072 pipelines, TGP 35–115 Вт, GDDR6 | 10 338 (56; 7 484–11 451) | 9 584 (2; 9 201–9 967) | 26 530 (54; 20 533–29 656) |
| [NVIDIA RTX 5050 Laptop](https://www.notebookcheck.net/Nvidia-GeForce-RTX-5050-Laptop-Benchmarks-and-Specs.934804.0.html) | дискретная | GN22-X2, Blackwell, 2560 pipelines, TGP 35–100 Вт, GDDR6 | 9 122 (9; 7 166–9 828) | 7 470 (2; 7 369–7 571) | 24 926 (10; 20 726–28 040) |
| [NVIDIA RTX 5060 Laptop](https://www.notebookcheck.net/Nvidia-GeForce-RTX-5060-Laptop-Benchmarks-and-Specs.934941.0.html) | дискретная | GN22-X4, Blackwell, 3328 pipelines, TGP 45–100 Вт, GDDR7 | 11 937 (22; 9 090–12 719) | 11 804 (5; 11 026–12 307) | 31 366 (21; 26 022–34 197) |
| [NVIDIA RTX 5070 Laptop](https://www.notebookcheck.net/Nvidia-GeForce-RTX-5070-Laptop-Benchmarks-and-Specs.934942.0.html) | дискретная | GN22-X6, Blackwell, 4608 pipelines, TGP 50–100 Вт, GDDR7 | 13 564 (35; 10 851–14 771) | 13 574 (12; 11 847–14 954) | 36 212 (35; 28 759–38 954) |

## 3. Puget Bench: DaVinci Resolve Studio и Premiere Pro

**Откуда числа.** Публичная база Puget Systems, страницы сравнения `pugetsystems.com/pugetbench/results/compare/…` (группа версий → GPU → два GPU рядом), сняты curl 30.09.2026 около 22:00.
Ссылка — в имени GPU (это страница пары; число в строке — для того GPU, что в строке). NBC PugetBench не публикует — других сводных чисел по iGPU нет.

**Как читать:**
- Это загрузки пользователей, а не лабораторные тесты: результат — весь ноутбук (процессор, память, лимит мощности, драйвер).
  Puget пишет, что показывает GPU только от 10 результатов, «to smooth out these outliers». Медиана это или среднее, на странице не сказано.
- **† — меньше 10 прогонов.** В выпадающем списке сайта такого GPU нет, число открывается только по прямой ссылке. Выбросы там явные:
  у «AMD Radeon 680M» в Premiere 25.1 GPU Effects = 161 (у RTX 5070 — 58). Это машина с дискретной картой, которая записалась под именем iGPU. Такие строки — только для ориентира.
- **Шкалы групп разные** (PB 2.x против 1.x, Basic против Standard): сравнивать только внутри одной таблицы.
- Столбцы: общий балл (Standard; для Resolve ещё Basic — у многих iGPU есть только он), LongGOP (H.264/HEVC), Intraframe (ProRes/DNxHR), GPU Effects, RAW (BRAW/RED и т. п.).
- **Имена — как их отдаёт Windows.** Как они ложатся на наш список:
  - «Intel UHD Graphics» — все UHD Xe‑LP 11–14‑го поколения (48 и 64 EU вместе). «Intel Iris Xe Graphics» — 80 и 96 EU вместе;
  - «Intel Arc Graphics» — iGPU Meteor Lake‑H (Arc 7/8‑Core: 125H/135H/155H). Это вывод по имени устройства, у Puget не расписано;
  - «Intel Graphics» — **смесь**: Graphics 4‑Core (125U/225U), Graphics 4 Xe3 (Panther Lake), десктопный Arrow Lake‑S и любой Arc с одной планкой.
    При одноканальной памяти Arc работает «nur als Intel Grafikmarke» ([даташит HP CU7G6EA](https://gzhls.at/blob/ldb/1/b/f/e/80d2945b99127777febcb5714b2521ae2d8c.pdf); у Intel — «at least 16GB of system memory in a dual-channel configuration», [ARK 155H](https://www.intel.com/content/www/us/en/products/sku/236847/intel-core-ultra-7-processor-155h-24m-cache-up-to-4-80-ghz/specifications.html));
  - «(8GB)» / «(16GB)» у Arc 130V/140V/130T/140T — сколько общей памяти Windows отдаёт графике (обычно половина ОЗУ). Значит, (8GB) — ноутбуки с 16 ГБ, (16GB) — с 32 ГБ. Это мой вывод, не проверено;
  - «AMD Radeon Graphics» — **смесь, не сопоставимо**: так называются и Rembrandt (660M/680M), и Vega в Barcelo, и десктопные Ryzen;
  - «AMD Radeon 780M» и «AMD Radeon 780M Graphics» — одно ядро под двумя именами (разные драйверы).
- Системы с двумя GPU (например, «RTX 5060 Laptop | Arc 140T») Puget ведёт отдельными строками — в таблицы не брал.
- Нет Puget‑данных вовсе: Radeon 660M (только в Resolve 20.0–20.3: одно число Basic, †), 820M (нигде), RTX 3050 A (нигде), Arc 7‑Core и 8‑Core отдельно (только общим «Intel Arc Graphics»), Graphics 4‑Core и Graphics 4 Xe3 отдельно (только в смеси «Intel Graphics»).

#### Resolve Studio 20.0–21.1, Puget Bench for DR 2.0–2.1 — новая шкала, со старыми группами не сравнивать

| GPU (сравнение Puget) | Прогонов | Общий (Standard) | Общий (Basic) | LongGOP | Intraframe | GPU Effects | RAW |
|---|---|---|---|---|---|---|---|
| [Intel UHD Graphics](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/33/GPU/Intel%20UHD%20Graphics/Intel%20Iris%20Xe%20Graphics/) | < 10 † | — | 10 493 | — | — | — | — |
| [Intel Iris Xe Graphics](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/33/GPU/Intel%20UHD%20Graphics/Intel%20Iris%20Xe%20Graphics/) | < 10 † | 9 014 | 16 662 | 10,7 | 10,3 | 8,0 | 6,5 |
| [Intel Arc Graphics](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/33/GPU/Intel%20Arc%20Graphics/Intel%20Graphics/) | 11 | 17 924 | 28 430 | 18,5 | 20,8 | 14,6 | 15,1 |
| [Intel Graphics](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/33/GPU/Intel%20Arc%20Graphics/Intel%20Graphics/) | 29 | 20 381 | 30 161 | 23,7 | 25,9 | 15,0 | 14,6 |
| [Intel Arc 130T(16GB)](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/33/GPU/Intel%20Arc%20130T%20GPU%20%2816GB%29/Intel%20Arc%20140T%20GPU%20%2816GB%29/) | < 10 † | — | 18 060 | — | — | — | — |
| [Intel Arc 140T(16GB)](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/33/GPU/Intel%20Arc%20130T%20GPU%20%2816GB%29/Intel%20Arc%20140T%20GPU%20%2816GB%29/) | < 10 † | 26 670 | 47 097 | 23,5 | 30,1 | 19,1 | 23,7 |
| [Intel Arc 140V(8GB)](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/33/GPU/Intel%20Arc%20140V%20GPU%20%2816GB%29/Intel%20Arc%20140V%20GPU%20%288GB%29/) | < 10 † | — | 32 256 | — | — | — | — |
| [Intel Arc 140V(16GB)](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/33/GPU/Intel%20Arc%20140V%20GPU%20%2816GB%29/Intel%20Arc%20140V%20GPU%20%288GB%29/) | 12 | 21 202 | 32 231 | 22,4 | 20,8 | 18,4 | 15,2 |
| [Intel Arc B370](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/33/GPU/Intel%20Arc%20B370%20GPU/Intel%20Arc%20B390%20GPU/) | < 10 † | 32 201 | 54 841 | 36,4 | 37,3 | 23,1 | 25,3 |
| [Intel Arc B390](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/33/GPU/Intel%20Arc%20B370%20GPU/Intel%20Arc%20B390%20GPU/) | 64 | 31 825 | 50 677 | 35,4 | 36,8 | 24,0 | 25,1 |
| [AMD Radeon Graphics](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/33/GPU/AMD%20Radeon%20Graphics/AMD%20Radeon%20660M/) | 17 | 10 254 | 20 883 | 11,2 | 10,8 | 8,7 | 8,8 |
| [AMD Radeon 680M](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/33/GPU/AMD%20Radeon%20680M/AMD%20Radeon%20740M%20Graphics/) | < 10 † | — | 26 886 | — | — | — | — |
| [AMD Radeon 760M Graphics](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/33/GPU/AMD%20Radeon%20760M%20Graphics/AMD%20Radeon%20780M%20Graphics/) | < 10 † | — | 24 738 | — | — | — | — |
| [AMD Radeon 780M Graphics](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/33/GPU/AMD%20Radeon%20760M%20Graphics/AMD%20Radeon%20780M%20Graphics/) | 17 | — | 30 680 | — | — | — | — |
| [AMD Radeon 780M](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/33/GPU/AMD%20Radeon%20780M/AMD%20Radeon%20820M%20Graphics/) | < 10 † | — | 40 103 | — | — | — | — |
| [AMD Radeon 840M Graphics](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/33/GPU/AMD%20Radeon%20840M%20Graphics/AMD%20Radeon%20860M%20Graphics/) | < 10 † | — | 22 913 | — | — | — | — |
| [AMD Radeon 860M Graphics](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/33/GPU/AMD%20Radeon%20840M%20Graphics/AMD%20Radeon%20860M%20Graphics/) | 11 | — | 31 695 | — | — | — | — |
| [AMD Radeon 880M Graphics](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/33/GPU/AMD%20Radeon%20880M%20Graphics/AMD%20Radeon%20890M%20Graphics/) | < 10 † | 22 812 | 41 604 | 22,1 | 24,6 | 14,4 | 17,6 |
| [AMD Radeon 890M Graphics](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/33/GPU/AMD%20Radeon%20880M%20Graphics/AMD%20Radeon%20890M%20Graphics/) | < 10 † | 19 644 | 42 373 | 22,1 | 14,0 | 15,7 | 18,3 |
| [RTX 3050 Laptop](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/33/GPU/NVIDIA%20GeForce%20RTX%203050%20Laptop%20GPU/NVIDIA%20GeForce%20RTX%203050%206GB%20Laptop%20GPU/) | < 10 † | — | 44 609 | — | — | — | — |
| [RTX 3050 6GB Laptop](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/33/GPU/NVIDIA%20GeForce%20RTX%203050%20Laptop%20GPU/NVIDIA%20GeForce%20RTX%203050%206GB%20Laptop%20GPU/) | < 10 † | — | 52 801 | — | — | — | — |
| [RTX 4050 Laptop](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/33/GPU/NVIDIA%20GeForce%20RTX%203050%20A%20Laptop%20GPU/NVIDIA%20GeForce%20RTX%204050%20Laptop%20GPU/) | 24 | 48 807 | 62 890 | 41,1 | 43,8 | 38,5 | 47,5 |
| [RTX 4060 Laptop](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/33/GPU/NVIDIA%20GeForce%20RTX%204060%20Laptop%20GPU/NVIDIA%20GeForce%20RTX%205050%20Laptop%20GPU/) | 15 | 55 612 | 72 418 | 46,8 | 43,3 | 47,5 | 50,2 |
| [RTX 5050 Laptop](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/33/GPU/NVIDIA%20GeForce%20RTX%204060%20Laptop%20GPU/NVIDIA%20GeForce%20RTX%205050%20Laptop%20GPU/) | < 10 † | 61 171 | 76 252 | 55,6 | 52,4 | 54,8 | 54,0 |
| [RTX 5060 Laptop](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/33/GPU/NVIDIA%20GeForce%20RTX%205060%20Laptop%20GPU/NVIDIA%20GeForce%20RTX%205070%20Laptop%20GPU/) | 29 | 71 352 | 98 078 | 59,3 | 62,6 | 64,5 | 69,8 |
| [RTX 5070 Laptop](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/33/GPU/NVIDIA%20GeForce%20RTX%205060%20Laptop%20GPU/NVIDIA%20GeForce%20RTX%205070%20Laptop%20GPU/) | 56 | 67 790 | 95 924 | 55,2 | 55,9 | 63,4 | 66,9 |

Нет в этой группе: Intel Arc 130V(8GB), Intel Arc 130V(16GB), AMD Radeon 660M, AMD Radeon 740M Graphics, AMD Radeon 820M Graphics.

#### Resolve Studio 20.0–20.3, Puget Bench for DR 1.2

| GPU (сравнение Puget) | Прогонов | Общий (Standard) | Общий (Basic) | LongGOP | Intraframe | GPU Effects | RAW |
|---|---|---|---|---|---|---|---|
| [Intel UHD Graphics](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/27/GPU/Intel%20UHD%20Graphics/Intel%20Iris%20Xe%20Graphics/) | < 10 † | — | 1 049 | — | — | — | — |
| [Intel Iris Xe Graphics](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/27/GPU/Intel%20UHD%20Graphics/Intel%20Iris%20Xe%20Graphics/) | 10 | — | 1 571 | — | — | — | — |
| [Intel Arc Graphics](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/27/GPU/Intel%20Arc%20Graphics/Intel%20Graphics/) | 16 | 2 150 | 2 546 | 48,1 | 26,6 | 10,0 | 16,3 |
| [Intel Graphics](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/27/GPU/Intel%20Arc%20Graphics/Intel%20Graphics/) | 30 | 2 366 | 2 445 | 55,4 | 27,8 | 9,2 | 15,1 |
| [Intel Arc 130T(16GB)](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/27/GPU/Intel%20Arc%20130T%20GPU%20%2816GB%29/Intel%20Arc%20140T%20GPU%20%2816GB%29/) | < 10 † | — | 3 502 | — | — | — | — |
| [Intel Arc 140T(16GB)](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/27/GPU/Intel%20Arc%20130T%20GPU%20%2816GB%29/Intel%20Arc%20140T%20GPU%20%2816GB%29/) | 27 | 2 489 | 3 211 | 55,0 | 28,2 | 10,7 | 18,8 |
| [Intel Arc 130V(8GB)](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/27/GPU/Intel%20Arc%20130V%20GPU%20%2816GB%29/Intel%20Arc%20130V%20GPU%20%288GB%29/) | < 10 † | 2 304 | 2 862 | 59,6 | 26,1 | 11,6 | 16,0 |
| [Intel Arc 140V(8GB)](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/27/GPU/Intel%20Arc%20140V%20GPU%20%2816GB%29/Intel%20Arc%20140V%20GPU%20%288GB%29/) | < 10 † | 1 597 | 2 170 | 35,8 | 17,7 | 9,2 | 11,5 |
| [Intel Arc 140V(16GB)](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/27/GPU/Intel%20Arc%20140V%20GPU%20%2816GB%29/Intel%20Arc%20140V%20GPU%20%288GB%29/) | 32 | 2 451 | 3 075 | 63,3 | 24,6 | 12,7 | 16,8 |
| [Intel Arc B390](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/27/GPU/Intel%20Arc%20B370%20GPU/Intel%20Arc%20B390%20GPU/) | 21 | 3 381 | 4 164 | 81,3 | 43,0 | 17,0 | 23,3 |
| [AMD Radeon Graphics](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/27/GPU/AMD%20Radeon%20Graphics/AMD%20Radeon%20660M/) | 13 | 1 059 | 1 599 | 24,1 | 12,4 | 4,2 | 8,2 |
| [AMD Radeon 660M](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/27/GPU/AMD%20Radeon%20Graphics/AMD%20Radeon%20660M/) | < 10 † | — | 1 278 | — | — | — | — |
| [AMD Radeon 760M Graphics](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/27/GPU/AMD%20Radeon%20760M%20Graphics/AMD%20Radeon%20780M%20Graphics/) | < 10 † | — | 2 900 | — | — | — | — |
| [AMD Radeon 780M Graphics](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/27/GPU/AMD%20Radeon%20760M%20Graphics/AMD%20Radeon%20780M%20Graphics/) | 27 | — | 2 513 | — | — | — | — |
| [AMD Radeon 840M Graphics](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/27/GPU/AMD%20Radeon%20840M%20Graphics/AMD%20Radeon%20860M%20Graphics/) | < 10 † | 1 262 | 1 559 | 32,6 | 14,2 | 4,8 | 7,8 |
| [AMD Radeon 860M Graphics](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/27/GPU/AMD%20Radeon%20840M%20Graphics/AMD%20Radeon%20860M%20Graphics/) | 19 | 2 402 | 2 754 | 55,8 | 26,3 | 10,4 | 16,2 |
| [AMD Radeon 880M Graphics](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/27/GPU/AMD%20Radeon%20880M%20Graphics/AMD%20Radeon%20890M%20Graphics/) | < 10 † | — | 2 585 | — | — | — | — |
| [AMD Radeon 890M Graphics](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/27/GPU/AMD%20Radeon%20880M%20Graphics/AMD%20Radeon%20890M%20Graphics/) | 18 | 2 872 | 3 473 | 61,9 | 33,7 | 12,1 | 20,6 |
| [RTX 3050 Laptop](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/27/GPU/NVIDIA%20GeForce%20RTX%203050%20Laptop%20GPU/NVIDIA%20GeForce%20RTX%203050%206GB%20Laptop%20GPU/) | 16 | 3 487 | 3 661 | 63,0 | 39,6 | 20,3 | 28,0 |
| [RTX 3050 6GB Laptop](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/27/GPU/NVIDIA%20GeForce%20RTX%203050%20Laptop%20GPU/NVIDIA%20GeForce%20RTX%203050%206GB%20Laptop%20GPU/) | < 10 † | 4 343 | 5 027 | 91,5 | 40,2 | 23,7 | 38,1 |
| [RTX 4050 Laptop](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/27/GPU/NVIDIA%20GeForce%20RTX%203050%20A%20Laptop%20GPU/NVIDIA%20GeForce%20RTX%204050%20Laptop%20GPU/) | 15 | 4 458 | 5 073 | 90,7 | 38,0 | 27,6 | 39,4 |
| [RTX 4060 Laptop](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/27/GPU/NVIDIA%20GeForce%20RTX%204060%20Laptop%20GPU/NVIDIA%20GeForce%20RTX%205050%20Laptop%20GPU/) | 42 | 5 486 | 6 624 | 97,8 | 49,8 | 35,6 | 51,6 |
| [RTX 5050 Laptop](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/27/GPU/NVIDIA%20GeForce%20RTX%204060%20Laptop%20GPU/NVIDIA%20GeForce%20RTX%205050%20Laptop%20GPU/) | 12 | 6 279 | 6 381 | 145,3 | 50,5 | 42,5 | 55,0 |
| [RTX 5060 Laptop](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/27/GPU/NVIDIA%20GeForce%20RTX%205060%20Laptop%20GPU/NVIDIA%20GeForce%20RTX%205070%20Laptop%20GPU/) | 90 | 7 324 | 7 586 | 139,6 | 73,4 | 47,2 | 69,8 |
| [RTX 5070 Laptop](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/27/GPU/NVIDIA%20GeForce%20RTX%205060%20Laptop%20GPU/NVIDIA%20GeForce%20RTX%205070%20Laptop%20GPU/) | 97 | 7 232 | 8 879 | 125,1 | 71,9 | 50,8 | 69,5 |

Нет в этой группе: Intel Arc 130V(16GB), Intel Arc B370, AMD Radeon 680M, AMD Radeon 740M Graphics, AMD Radeon 780M, AMD Radeon 820M Graphics.

#### Resolve Studio 18.6–19.1, Puget Bench for DR 1.0–1.2

| GPU (сравнение Puget) | Прогонов | Общий (Standard) | Общий (Basic) | LongGOP | Intraframe | GPU Effects | RAW |
|---|---|---|---|---|---|---|---|
| [Intel UHD Graphics](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/17/GPU/Intel%20UHD%20Graphics/Intel%20Iris%20Xe%20Graphics/) | < 10 † | — | 693 | — | — | — | — |
| [Intel Iris Xe Graphics](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/17/GPU/Intel%20UHD%20Graphics/Intel%20Iris%20Xe%20Graphics/) | 10 | 860 | 1 279 | 17,9 | 9,4 | 3,7 | 6,7 |
| [Intel Arc Graphics](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/17/GPU/Intel%20Arc%20Graphics/Intel%20Graphics/) | 44 | 1 990 | 2 458 | 46,8 | 26,2 | 9,6 | 14,6 |
| [Intel Graphics](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/17/GPU/Intel%20Arc%20Graphics/Intel%20Graphics/) | 52 | 2 266 | 2 501 | 53,4 | 31,7 | 9,1 | 14,9 |
| [Intel Arc 130T(16GB)](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/17/GPU/Intel%20Arc%20130T%20GPU%20%2816GB%29/Intel%20Arc%20140T%20GPU%20%2816GB%29/) | < 10 † | — | 3 481 | — | — | — | — |
| [Intel Arc 140T(16GB)](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/17/GPU/Intel%20Arc%20130T%20GPU%20%2816GB%29/Intel%20Arc%20140T%20GPU%20%2816GB%29/) | 32 | 2 701 | 3 385 | 58,9 | 33,3 | 12,4 | 20,1 |
| [Intel Arc 130V(8GB)](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/17/GPU/Intel%20Arc%20130V%20GPU%20%2816GB%29/Intel%20Arc%20130V%20GPU%20%288GB%29/) | < 10 † | 1 662 | 2 128 | 36,0 | 14,8 | 10,1 | 10,4 |
| [Intel Arc 130V(16GB)](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/17/GPU/Intel%20Arc%20130V%20GPU%20%2816GB%29/Intel%20Arc%20130V%20GPU%20%288GB%29/) | < 10 † | 2 124 | 2 540 | 63,5 | 19,5 | 11,1 | 14,8 |
| [Intel Arc 140V(8GB)](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/17/GPU/Intel%20Arc%20140V%20GPU%20%2816GB%29/Intel%20Arc%20140V%20GPU%20%288GB%29/) | < 10 † | 1 763 | 2 990 | 38,2 | 15,7 | 11,6 | 10,7 |
| [Intel Arc 140V(16GB)](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/17/GPU/Intel%20Arc%20140V%20GPU%20%2816GB%29/Intel%20Arc%20140V%20GPU%20%288GB%29/) | 42 | 2 321 | 2 781 | 56,4 | 27,1 | 11,7 | 15,9 |
| [Intel Arc B390](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/17/GPU/Intel%20Arc%20B370%20GPU/Intel%20Arc%20B390%20GPU/) | 12 | 4 232 | 4 416 | 103,0 | 54,6 | 19,6 | 29,2 |
| [AMD Radeon Graphics](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/17/GPU/AMD%20Radeon%20Graphics/AMD%20Radeon%20660M/) | 25 | 4 893 | 2 785 | 100,0 | 62,0 | 26,0 | 47,0 |
| [AMD Radeon 740M Graphics](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/17/GPU/AMD%20Radeon%20680M/AMD%20Radeon%20740M%20Graphics/) | < 10 † | — | 2 308 | — | — | — | — |
| [AMD Radeon 760M Graphics](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/17/GPU/AMD%20Radeon%20760M%20Graphics/AMD%20Radeon%20780M%20Graphics/) | < 10 † | — | 1 888 | — | — | — | — |
| [AMD Radeon 780M Graphics](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/17/GPU/AMD%20Radeon%20760M%20Graphics/AMD%20Radeon%20780M%20Graphics/) | 45 | 2 245 | 2 648 | 52,1 | 27,2 | 9,7 | 14,9 |
| [AMD Radeon 780M](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/17/GPU/AMD%20Radeon%20780M/AMD%20Radeon%20820M%20Graphics/) | < 10 † | — | 2 482 | — | — | — | — |
| [AMD Radeon 860M Graphics](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/17/GPU/AMD%20Radeon%20840M%20Graphics/AMD%20Radeon%20860M%20Graphics/) | < 10 † | 1 348 | 1 982 | 33,9 | 16,0 | 5,6 | 7,5 |
| [AMD Radeon 880M Graphics](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/17/GPU/AMD%20Radeon%20880M%20Graphics/AMD%20Radeon%20890M%20Graphics/) | < 10 † | 2 354 | 2 859 | 60,1 | 26,9 | 10,6 | 16,8 |
| [AMD Radeon 890M Graphics](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/17/GPU/AMD%20Radeon%20880M%20Graphics/AMD%20Radeon%20890M%20Graphics/) | 50 | 2 500 | 3 001 | 58,0 | 29,1 | 11,5 | 15,3 |
| [RTX 3050 Laptop](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/17/GPU/NVIDIA%20GeForce%20RTX%203050%20Laptop%20GPU/NVIDIA%20GeForce%20RTX%203050%206GB%20Laptop%20GPU/) | 24 | 3 468 | 4 098 | 73,4 | 41,0 | 21,3 | 31,7 |
| [RTX 3050 6GB Laptop](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/17/GPU/NVIDIA%20GeForce%20RTX%203050%20Laptop%20GPU/NVIDIA%20GeForce%20RTX%203050%206GB%20Laptop%20GPU/) | < 10 † | — | 4 406 | — | — | — | — |
| [RTX 4050 Laptop](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/17/GPU/NVIDIA%20GeForce%20RTX%203050%20A%20Laptop%20GPU/NVIDIA%20GeForce%20RTX%204050%20Laptop%20GPU/) | 22 | 3 891 | 4 720 | 76,6 | 35,6 | 26,6 | 38,7 |
| [RTX 4060 Laptop](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/17/GPU/NVIDIA%20GeForce%20RTX%204060%20Laptop%20GPU/NVIDIA%20GeForce%20RTX%205050%20Laptop%20GPU/) | 96 | 5 066 | 6 005 | 92,0 | 50,9 | 34,8 | 45,4 |
| [RTX 5050 Laptop](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/17/GPU/NVIDIA%20GeForce%20RTX%204060%20Laptop%20GPU/NVIDIA%20GeForce%20RTX%205050%20Laptop%20GPU/) | 11 | 5 762 | 6 188 | 115,5 | 48,4 | 42,9 | 51,6 |
| [RTX 5060 Laptop](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/17/GPU/NVIDIA%20GeForce%20RTX%205060%20Laptop%20GPU/NVIDIA%20GeForce%20RTX%205070%20Laptop%20GPU/) | 75 | 7 135 | 8 123 | 118,8 | 65,5 | 48,8 | 74,7 |
| [RTX 5070 Laptop](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20DaVinci%20Resolve/17/GPU/NVIDIA%20GeForce%20RTX%205060%20Laptop%20GPU/NVIDIA%20GeForce%20RTX%205070%20Laptop%20GPU/) | 14 | 7 243 | 8 237 | 120,2 | 70,9 | 53,5 | 76,6 |

Нет в этой группе: Intel Arc B370, AMD Radeon 660M, AMD Radeon 680M, AMD Radeon 820M Graphics, AMD Radeon 840M Graphics.

#### Premiere Pro 25.6–26.5, Puget Bench for Pr 2.0 — новая шкала, со старыми группами не сравнивать

| GPU (сравнение Puget) | Прогонов | Общий (Standard) | LongGOP | Intraframe | GPU Effects | RAW |
|---|---|---|---|---|---|---|
| [Intel Iris Xe Graphics](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/32/GPU/Intel%20UHD%20Graphics/Intel%20Iris%20Xe%20Graphics/) | < 10 † | 32 768 | 46,7 | 26,3 | — | — |
| [Intel Arc Graphics](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/32/GPU/Intel%20Arc%20Graphics/Intel%20Graphics/) | < 10 † | 28 988 | 33,6 | 33,6 | 7,9 | 13,0 |
| [Intel Graphics](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/32/GPU/Intel%20Arc%20Graphics/Intel%20Graphics/) | 46 | 30 790 | 36,8 | 44,2 | 6,5 | 12,7 |
| [Intel Arc 140T(16GB)](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/32/GPU/Intel%20Arc%20130T%20GPU%20%2816GB%29/Intel%20Arc%20140T%20GPU%20%2816GB%29/) | < 10 † | 28 724 | 34,9 | 66,8 | 11,9 | 24,5 |
| [Intel Arc 130V(8GB)](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/32/GPU/Intel%20Arc%20130V%20GPU%20%2816GB%29/Intel%20Arc%20130V%20GPU%20%288GB%29/) | < 10 † | 21 749 | 30,7 | 51,8 | 10,0 | 14,1 |
| [Intel Arc 130V(16GB)](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/32/GPU/Intel%20Arc%20130V%20GPU%20%2816GB%29/Intel%20Arc%20130V%20GPU%20%288GB%29/) | < 10 † | 61 088 | 64,9 | 50,6 | — | — |
| [Intel Arc 140V(8GB)](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/32/GPU/Intel%20Arc%20140V%20GPU%20%2816GB%29/Intel%20Arc%20140V%20GPU%20%288GB%29/) | < 10 † | 42 340 | 65,5 | 28,6 | — | — |
| [Intel Arc 140V(16GB)](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/32/GPU/Intel%20Arc%20140V%20GPU%20%2816GB%29/Intel%20Arc%20140V%20GPU%20%288GB%29/) | < 10 † | 36 842 | 62,8 | 47,5 | 11,7 | 15,6 |
| [Intel Arc B370](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/32/GPU/Intel%20Arc%20B370%20GPU/Intel%20Arc%20B390%20GPU/) | < 10 † | 33 994 | 47,4 | 78,5 | 16,8 | 21,4 |
| [Intel Arc B390](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/32/GPU/Intel%20Arc%20B370%20GPU/Intel%20Arc%20B390%20GPU/) | 70 | 38 532 | 47,2 | 82,2 | 19,8 | 24,2 |
| [AMD Radeon Graphics](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/32/GPU/AMD%20Radeon%20Graphics/AMD%20Radeon%20660M/) | 62 | 18 882 | 23,5 | 34,5 | 15,9 | 10,3 |
| [AMD Radeon 760M Graphics](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/32/GPU/AMD%20Radeon%20760M%20Graphics/AMD%20Radeon%20780M%20Graphics/) | < 10 † | 15 674 | 18,3 | 26,4 | 12,3 | 10,3 |
| [AMD Radeon 780M Graphics](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/32/GPU/AMD%20Radeon%20760M%20Graphics/AMD%20Radeon%20780M%20Graphics/) | 10 | 26 436 | 37,1 | 38,0 | 17,1 | 13,3 |
| [AMD Radeon 840M Graphics](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/32/GPU/AMD%20Radeon%20840M%20Graphics/AMD%20Radeon%20860M%20Graphics/) | < 10 † | 19 105 | 32,4 | 28,8 | 11,6 | 10,2 |
| [AMD Radeon 860M Graphics](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/32/GPU/AMD%20Radeon%20840M%20Graphics/AMD%20Radeon%20860M%20Graphics/) | 29 | 28 863 | 36,1 | 42,0 | 18,0 | 18,2 |
| [AMD Radeon 880M Graphics](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/32/GPU/AMD%20Radeon%20880M%20Graphics/AMD%20Radeon%20890M%20Graphics/) | 11 | 31 000 | 43,4 | 39,6 | 19,0 | 19,4 |
| [AMD Radeon 890M Graphics](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/32/GPU/AMD%20Radeon%20880M%20Graphics/AMD%20Radeon%20890M%20Graphics/) | 31 | 28 888 | 31,1 | 55,5 | 22,3 | 18,6 |
| [RTX 3050 Laptop](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/32/GPU/NVIDIA%20GeForce%20RTX%203050%20Laptop%20GPU/NVIDIA%20GeForce%20RTX%203050%206GB%20Laptop%20GPU/) | < 10 † | 48 788 | 52,5 | 56,3 | 19,9 | 64,0 |
| [RTX 3050 6GB Laptop](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/32/GPU/NVIDIA%20GeForce%20RTX%203050%20Laptop%20GPU/NVIDIA%20GeForce%20RTX%203050%206GB%20Laptop%20GPU/) | 10 | 44 651 | 45,7 | 48,8 | 21,6 | 81,3 |
| [RTX 4050 Laptop](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/32/GPU/NVIDIA%20GeForce%20RTX%203050%20A%20Laptop%20GPU/NVIDIA%20GeForce%20RTX%204050%20Laptop%20GPU/) | 13 | 51 338 | 49,4 | 57,8 | 27,8 | 89,0 |
| [RTX 4060 Laptop](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/32/GPU/NVIDIA%20GeForce%20RTX%204060%20Laptop%20GPU/NVIDIA%20GeForce%20RTX%205050%20Laptop%20GPU/) | 12 | 62 666 | 59,7 | 67,5 | 35,9 | 107,8 |
| [RTX 5050 Laptop](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/32/GPU/NVIDIA%20GeForce%20RTX%204060%20Laptop%20GPU/NVIDIA%20GeForce%20RTX%205050%20Laptop%20GPU/) | 16 | 66 837 | 69,3 | 79,3 | 32,8 | 113,9 |
| [RTX 5060 Laptop](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/32/GPU/NVIDIA%20GeForce%20RTX%205060%20Laptop%20GPU/NVIDIA%20GeForce%20RTX%205070%20Laptop%20GPU/) | 59 | 78 745 | 79,5 | 81,4 | 45,1 | 132,6 |
| [RTX 5070 Laptop](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/32/GPU/NVIDIA%20GeForce%20RTX%205060%20Laptop%20GPU/NVIDIA%20GeForce%20RTX%205070%20Laptop%20GPU/) | 28 | 83 121 | 81,1 | 85,4 | 50,4 | 132,7 |

Нет в этой группе: Intel UHD Graphics, Intel Arc 130T(16GB), AMD Radeon 660M, AMD Radeon 680M, AMD Radeon 740M Graphics, AMD Radeon 780M, AMD Radeon 820M Graphics.

#### Premiere Pro 25.1–25.2, Puget Bench for Pr 1.0–1.1

| GPU (сравнение Puget) | Прогонов | Общий (Standard) | LongGOP | Intraframe | GPU Effects | RAW |
|---|---|---|---|---|---|---|
| [Intel UHD Graphics](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/23/GPU/Intel%20UHD%20Graphics/Intel%20Iris%20Xe%20Graphics/) | 11 | 1 599 | 17,8 | 17,9 | 5,5 | 40,4 |
| [Intel Iris Xe Graphics](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/23/GPU/Intel%20UHD%20Graphics/Intel%20Iris%20Xe%20Graphics/) | 29 | 1 651 | 20,1 | 19,3 | 6,3 | 31,6 |
| [Intel Arc Graphics](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/23/GPU/Intel%20Arc%20Graphics/Intel%20Graphics/) | 26 | 2 694 | 33,6 | 34,2 | 10,9 | 44,1 |
| [Intel Graphics](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/23/GPU/Intel%20Arc%20Graphics/Intel%20Graphics/) | 102 | 2 380 | 27,6 | 28,7 | 8,8 | 44,4 |
| [Intel Arc 130T(16GB)](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/23/GPU/Intel%20Arc%20130T%20GPU%20%2816GB%29/Intel%20Arc%20140T%20GPU%20%2816GB%29/) | 24 | 3 591 | 47,1 | 45,5 | 14,2 | 57,3 |
| [Intel Arc 140T(16GB)](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/23/GPU/Intel%20Arc%20130T%20GPU%20%2816GB%29/Intel%20Arc%20140T%20GPU%20%2816GB%29/) | 70 | 3 661 | 47,5 | 47,0 | 13,9 | 57,5 |
| [Intel Arc 130V(8GB)](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/23/GPU/Intel%20Arc%20130V%20GPU%20%2816GB%29/Intel%20Arc%20130V%20GPU%20%288GB%29/) | 20 | 2 809 | 36,0 | 37,0 | 13,7 | 35,8 |
| [Intel Arc 130V(16GB)](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/23/GPU/Intel%20Arc%20130V%20GPU%20%2816GB%29/Intel%20Arc%20130V%20GPU%20%288GB%29/) | 11 | 2 433 | 30,8 | 30,7 | 11,7 | 32,6 |
| [Intel Arc 140V(8GB)](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/23/GPU/Intel%20Arc%20140V%20GPU%20%2816GB%29/Intel%20Arc%20140V%20GPU%20%288GB%29/) | 17 | 2 994 | 40,6 | 39,0 | 14,2 | 36,8 |
| [Intel Arc 140V(16GB)](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/23/GPU/Intel%20Arc%20140V%20GPU%20%2816GB%29/Intel%20Arc%20140V%20GPU%20%288GB%29/) | 102 | 2 834 | 37,8 | 35,9 | 13,8 | 35,8 |
| [Intel Arc B370](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/23/GPU/Intel%20Arc%20B370%20GPU/Intel%20Arc%20B390%20GPU/) | < 10 † | 4 630 | 58,3 | 66,2 | 20,6 | 60,3 |
| [Intel Arc B390](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/23/GPU/Intel%20Arc%20B370%20GPU/Intel%20Arc%20B390%20GPU/) | 56 | 5 025 | 64,8 | 70,2 | 21,8 | 64,9 |
| [AMD Radeon Graphics](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/23/GPU/AMD%20Radeon%20Graphics/AMD%20Radeon%20660M/) | 44 | 2 084 | 26,8 | 23,3 | 7,5 | 42,7 |
| [AMD Radeon 680M](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/23/GPU/AMD%20Radeon%20680M/AMD%20Radeon%20740M%20Graphics/) | < 10 † | 10 463 | 91,9 | 116,3 | 161,3 | 70,1 |
| [AMD Radeon 740M Graphics](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/23/GPU/AMD%20Radeon%20680M/AMD%20Radeon%20740M%20Graphics/) | < 10 † | 2 572 | 35,3 | 28,3 | 6,9 | 63,7 |
| [AMD Radeon 760M Graphics](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/23/GPU/AMD%20Radeon%20760M%20Graphics/AMD%20Radeon%20780M%20Graphics/) | < 10 † | 2 855 | 38,1 | 32,8 | 8,3 | 63,8 |
| [AMD Radeon 780M Graphics](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/23/GPU/AMD%20Radeon%20760M%20Graphics/AMD%20Radeon%20780M%20Graphics/) | 68 | 3 038 | 41,7 | 37,1 | 9,4 | 59,2 |
| [AMD Radeon 780M](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/23/GPU/AMD%20Radeon%20780M/AMD%20Radeon%20820M%20Graphics/) | < 10 † | 2 807 | 38,0 | 32,7 | 10,6 | 48,3 |
| [AMD Radeon 840M Graphics](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/23/GPU/AMD%20Radeon%20840M%20Graphics/AMD%20Radeon%20860M%20Graphics/) | 11 | 2 051 | 28,1 | 24,2 | 7,5 | 39,8 |
| [AMD Radeon 860M Graphics](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/23/GPU/AMD%20Radeon%20840M%20Graphics/AMD%20Radeon%20860M%20Graphics/) | 27 | 2 882 | 39,1 | 35,0 | 10,2 | 50,4 |
| [AMD Radeon 880M Graphics](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/23/GPU/AMD%20Radeon%20880M%20Graphics/AMD%20Radeon%20890M%20Graphics/) | 21 | 5 065 | 50,6 | 47,8 | 63,8 | 71,5 |
| [AMD Radeon 890M Graphics](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/23/GPU/AMD%20Radeon%20880M%20Graphics/AMD%20Radeon%20890M%20Graphics/) | 59 | 4 326 | 51,8 | 47,4 | 32,5 | 68,1 |
| [RTX 3050 Laptop](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/23/GPU/NVIDIA%20GeForce%20RTX%203050%20Laptop%20GPU/NVIDIA%20GeForce%20RTX%203050%206GB%20Laptop%20GPU/) | 26 | 4 396 | 53,3 | 49,1 | 27,1 | 51,7 |
| [RTX 3050 6GB Laptop](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/23/GPU/NVIDIA%20GeForce%20RTX%203050%20Laptop%20GPU/NVIDIA%20GeForce%20RTX%203050%206GB%20Laptop%20GPU/) | 29 | 5 242 | 51,4 | 54,5 | 24,1 | 113,3 |
| [RTX 4050 Laptop](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/23/GPU/NVIDIA%20GeForce%20RTX%203050%20A%20Laptop%20GPU/NVIDIA%20GeForce%20RTX%204050%20Laptop%20GPU/) | 53 | 6 548 | 63,5 | 64,5 | 30,2 | 152,2 |
| [RTX 4060 Laptop](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/23/GPU/NVIDIA%20GeForce%20RTX%204060%20Laptop%20GPU/NVIDIA%20GeForce%20RTX%205050%20Laptop%20GPU/) | 70 | 7 850 | 70,6 | 75,5 | 42,5 | 167,1 |
| [RTX 5050 Laptop](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/23/GPU/NVIDIA%20GeForce%20RTX%204060%20Laptop%20GPU/NVIDIA%20GeForce%20RTX%205050%20Laptop%20GPU/) | 30 | 8 183 | 73,7 | 68,8 | 51,8 | 182,9 |
| [RTX 5060 Laptop](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/23/GPU/NVIDIA%20GeForce%20RTX%205060%20Laptop%20GPU/NVIDIA%20GeForce%20RTX%205070%20Laptop%20GPU/) | 169 | 9 894 | 90,3 | 94,6 | 58,3 | 197,8 |
| [RTX 5070 Laptop](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/23/GPU/NVIDIA%20GeForce%20RTX%205060%20Laptop%20GPU/NVIDIA%20GeForce%20RTX%205070%20Laptop%20GPU/) | 49 | 10 033 | 89,3 | 102,1 | 58,2 | 198,6 |

Нет в этой группе: AMD Radeon 660M, AMD Radeon 820M Graphics.

#### Premiere Pro 23.0–25.0, Puget Bench for Pr 1.0–1.1

| GPU (сравнение Puget) | Прогонов | Общий (Standard) | LongGOP | Intraframe | GPU Effects | RAW |
|---|---|---|---|---|---|---|
| [Intel UHD Graphics](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/14/GPU/Intel%20UHD%20Graphics/Intel%20Iris%20Xe%20Graphics/) | 90 | 1 271 | 13,6 | 13,6 | 4,5 | 28,9 |
| [Intel Iris Xe Graphics](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/14/GPU/Intel%20UHD%20Graphics/Intel%20Iris%20Xe%20Graphics/) | 154 | 1 907 | 21,8 | 21,5 | 6,9 | 40,4 |
| [Intel Arc Graphics](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/14/GPU/Intel%20Arc%20Graphics/Intel%20Graphics/) | 196 | 2 961 | 37,5 | 37,4 | 11,5 | 51,1 |
| [Intel Graphics](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/14/GPU/Intel%20Arc%20Graphics/Intel%20Graphics/) | 96 | 2 364 | 26,6 | 27,9 | 9,1 | 50,5 |
| [Intel Arc 130T(16GB)](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/14/GPU/Intel%20Arc%20130T%20GPU%20%2816GB%29/Intel%20Arc%20140T%20GPU%20%2816GB%29/) | < 10 † | 4 114 | 50,8 | 51,5 | 14,7 | 75,4 |
| [Intel Arc 140T(16GB)](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/14/GPU/Intel%20Arc%20130T%20GPU%20%2816GB%29/Intel%20Arc%20140T%20GPU%20%2816GB%29/) | 23 | 4 044 | 51,2 | 49,8 | 15,1 | 66,3 |
| [Intel Arc 130V(8GB)](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/14/GPU/Intel%20Arc%20130V%20GPU%20%2816GB%29/Intel%20Arc%20130V%20GPU%20%288GB%29/) | < 10 † | 3 522 | 40,5 | 34,9 | 13,7 | 27,0 |
| [Intel Arc 130V(16GB)](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/14/GPU/Intel%20Arc%20130V%20GPU%20%2816GB%29/Intel%20Arc%20130V%20GPU%20%288GB%29/) | < 10 † | 3 016 | 38,0 | 39,5 | 15,4 | 35,8 |
| [Intel Arc 140V(8GB)](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/14/GPU/Intel%20Arc%20140V%20GPU%20%2816GB%29/Intel%20Arc%20140V%20GPU%20%288GB%29/) | < 10 † | 3 050 | 37,4 | 40,3 | 14,7 | 38,5 |
| [Intel Arc 140V(16GB)](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/14/GPU/Intel%20Arc%20140V%20GPU%20%2816GB%29/Intel%20Arc%20140V%20GPU%20%288GB%29/) | 53 | 3 063 | 40,1 | 39,4 | 15,5 | 37,5 |
| [Intel Arc B370](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/14/GPU/Intel%20Arc%20B370%20GPU/Intel%20Arc%20B390%20GPU/) | 12 | 4 305 | 53,6 | 57,8 | 18,3 | 61,8 |
| [Intel Arc B390](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/14/GPU/Intel%20Arc%20B370%20GPU/Intel%20Arc%20B390%20GPU/) | < 10 † | 5 202 | 66,2 | 71,6 | 21,8 | 75,9 |
| [AMD Radeon Graphics](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/14/GPU/AMD%20Radeon%20Graphics/AMD%20Radeon%20660M/) | 178 | 2 461 | 27,6 | 25,7 | 8,1 | 53,1 |
| [AMD Radeon 740M Graphics](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/14/GPU/AMD%20Radeon%20680M/AMD%20Radeon%20740M%20Graphics/) | < 10 † | 2 882 | 39,4 | 33,9 | 9,9 | 53,6 |
| [AMD Radeon 760M Graphics](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/14/GPU/AMD%20Radeon%20760M%20Graphics/AMD%20Radeon%20780M%20Graphics/) | 16 | 3 150 | 40,8 | 36,2 | 10,8 | 63,1 |
| [AMD Radeon 780M Graphics](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/14/GPU/AMD%20Radeon%20760M%20Graphics/AMD%20Radeon%20780M%20Graphics/) | 168 | 3 019 | 38,8 | 36,0 | 9,1 | 57,1 |
| [AMD Radeon 780M](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/14/GPU/AMD%20Radeon%20780M/AMD%20Radeon%20820M%20Graphics/) | 23 | 3 078 | 42,5 | 38,7 | 9,2 | 63,4 |
| [AMD Radeon 860M Graphics](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/14/GPU/AMD%20Radeon%20840M%20Graphics/AMD%20Radeon%20860M%20Graphics/) | 17 | 2 876 | 36,4 | 33,6 | 9,0 | 63,3 |
| [AMD Radeon 880M Graphics](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/14/GPU/AMD%20Radeon%20880M%20Graphics/AMD%20Radeon%20890M%20Graphics/) | < 10 † | 2 996 | 43,9 | 40,3 | 11,2 | 42,0 |
| [AMD Radeon 890M Graphics](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/14/GPU/AMD%20Radeon%20880M%20Graphics/AMD%20Radeon%20890M%20Graphics/) | 81 | 3 450 | 46,3 | 41,9 | 13,2 | 60,5 |
| [RTX 3050 Laptop](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/14/GPU/NVIDIA%20GeForce%20RTX%203050%20Laptop%20GPU/NVIDIA%20GeForce%20RTX%203050%206GB%20Laptop%20GPU/) | 36 | 3 804 | 45,1 | 45,1 | 19,7 | 56,4 |
| [RTX 3050 6GB Laptop](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/14/GPU/NVIDIA%20GeForce%20RTX%203050%20Laptop%20GPU/NVIDIA%20GeForce%20RTX%203050%206GB%20Laptop%20GPU/) | 46 | 5 307 | 60,5 | 52,5 | 25,6 | 113,9 |
| [RTX 4050 Laptop](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/14/GPU/NVIDIA%20GeForce%20RTX%203050%20A%20Laptop%20GPU/NVIDIA%20GeForce%20RTX%204050%20Laptop%20GPU/) | 117 | 6 209 | 63,7 | 58,2 | 28,8 | 143,1 |
| [RTX 4060 Laptop](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/14/GPU/NVIDIA%20GeForce%20RTX%204060%20Laptop%20GPU/NVIDIA%20GeForce%20RTX%205050%20Laptop%20GPU/) | 233 | 7 435 | 76,1 | 69,1 | 40,8 | 153,6 |
| [RTX 5050 Laptop](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/14/GPU/NVIDIA%20GeForce%20RTX%204060%20Laptop%20GPU/NVIDIA%20GeForce%20RTX%205050%20Laptop%20GPU/) | 15 | 8 501 | 75,6 | 72,7 | 52,8 | 184,6 |
| [RTX 5060 Laptop](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/14/GPU/NVIDIA%20GeForce%20RTX%205060%20Laptop%20GPU/NVIDIA%20GeForce%20RTX%205070%20Laptop%20GPU/) | 51 | 9 508 | 89,5 | 86,9 | 57,7 | 198,6 |
| [RTX 5070 Laptop](https://www.pugetsystems.com/pugetbench/results/compare/Puget%20Bench%20for%20Premiere%20Pro/14/GPU/NVIDIA%20GeForce%20RTX%205060%20Laptop%20GPU/NVIDIA%20GeForce%20RTX%205070%20Laptop%20GPU/) | 19 | 9 730 | 86,7 | 90,0 | 56,6 | 202,5 |

Нет в этой группе: AMD Radeon 660M, AMD Radeon 680M, AMD Radeon 820M Graphics, AMD Radeon 840M Graphics.

### 3.1. Ключевые подтесты (кадр/с, больше — лучше)

Те же страницы сравнения, что в таблицах выше (ссылки там). Только GPU с ≥ 10 прогонами; «—» — у этой группы машин подтест не прогнан (он входит только в пресет Extended).

#### Resolve Studio 20.0–20.3 (PB 1.2), кадр/с, только GPU с ≥ 10 прогонами

| GPU | Прогонов | 4K H.264 4:2:0 8 бит | 4K HEVC 4:2:2 10 бит | Экспорт HEVC 10 бит UHD | Color Node ×30 |
|---|---|---|---|---|---|
| Intel Iris Xe Graphics | 10 | 51,87 | — | — | — |
| Intel Arc Graphics | 16 | 75,66 | 41,74 | 48,9 | 7,82 |
| Intel Graphics | 30 | 74,23 | 51,01 | 50,41 | 9,92 |
| Intel Arc 140T(16GB) | 27 | 94,74 | 56,29 | 52,43 | 8,77 |
| Intel Arc 140V(16GB) | 32 | 108,53 | 67,05 | 63,37 | 12,63 |
| Intel Arc B390 | 21 | 147,93 | 84,79 | — | 15,01 |
| AMD Radeon Graphics | 13 | 48,33 | 21,83 | — | 4,25 |
| AMD Radeon 780M Graphics | 27 | 76,48 | — | — | — |
| AMD Radeon 860M Graphics | 19 | 88,29 | 43,35 | 64,96 | 13,64 |
| AMD Radeon 890M Graphics | 18 | 106,73 | 41,93 | 70,89 | 10,38 |
| RTX 3050 Laptop | 16 | 96,83 | 44,53 | — | 24,14 |
| RTX 4050 Laptop | 15 | 127,66 | 104,96 | — | 24,9 |
| RTX 4060 Laptop | 42 | 142,06 | 111,13 | — | 32,67 |
| RTX 5050 Laptop | 12 | 207,09 | 221,99 | — | 44,81 |
| RTX 5060 Laptop | 90 | 226,49 | 190,84 | 114,6 | 46,93 |
| RTX 5070 Laptop | 97 | 234,32 | 134,83 | 111,76 | 46,63 |

#### Premiere Pro 25.1–25.2 (PB 1.x), кадр/с, только GPU с ≥ 10 прогонами

| GPU | Прогонов | 4K H.264 4:2:0 8 бит | 4K HEVC 4:2:2 10 бит | Экспорт HEVC 8 бит UHD | Lumetri ×40 |
|---|---|---|---|---|---|
| Intel UHD Graphics | 11 | 20,8 | — | 21,73 | 6,26 |
| Intel Iris Xe Graphics | 29 | 24,75 | — | 27,21 | 7,19 |
| Intel Arc Graphics | 26 | 42,88 | — | 43,53 | 13,73 |
| Intel Graphics | 102 | 31,46 | 32 | 35,8 | 10,45 |
| Intel Arc 130T(16GB) | 24 | 58,81 | — | 59,63 | 18,85 |
| Intel Arc 140T(16GB) | 70 | 60,78 | — | 59,03 | 18,15 |
| Intel Arc 130V(8GB) | 20 | 44,88 | — | 55,54 | 16,89 |
| Intel Arc 130V(16GB) | 11 | 40,07 | — | 41,69 | 14,14 |
| Intel Arc 140V(8GB) | 17 | 53,18 | — | 64,81 | 17,42 |
| Intel Arc 140V(16GB) | 102 | 47,84 | — | 60,39 | 16,8 |
| Intel Arc B390 | 56 | 86,89 | — | 85,9 | 27,88 |
| AMD Radeon Graphics | 44 | 29,45 | 28,63 | 39,21 | 8,35 |
| AMD Radeon 780M Graphics | 68 | 47,74 | 29,1 | 60,1 | 11,02 |
| AMD Radeon 840M Graphics | 11 | 31,18 | — | 41,18 | 7,86 |
| AMD Radeon 860M Graphics | 27 | 44,95 | — | 55,92 | 11,9 |
| AMD Radeon 880M Graphics | 21 | 58,05 | 40,63 | 77,68 | 35,77 |
| AMD Radeon 890M Graphics | 59 | 57,51 | 44,1 | 77,16 | 17,79 |
| RTX 3050 Laptop | 26 | 79,38 | — | 64,57 | 33,67 |
| RTX 3050 6GB Laptop | 29 | 80,62 | 41,83 | 63,84 | 31,76 |
| RTX 4050 Laptop | 53 | 91,8 | — | 83,6 | 38,75 |
| RTX 4060 Laptop | 70 | 98,37 | — | 84,75 | 51,07 |
| RTX 5050 Laptop | 30 | 122,62 | — | 102 | 62,34 |
| RTX 5060 Laptop | 169 | 141,83 | — | 107,51 | 73,57 |
| RTX 5070 Laptop | 49 | 133,94 | — | 106,1 | 72,57 |

### 3.2. Что видно по Puget

- **Resolve 20.0–20.3, общий балл (Standard):** iGPU 2 150–2 872 (Meteor Lake Arc → 890M), Arc B390 3 381; RTX 3050 3 487, RTX 4050 4 458, RTX 4060 5 486, RTX 5050 6 279, RTX 5060 7 324, RTX 5070 7 232.
  RTX 4050…5070 быстрее iGPU до 890M включительно в 1,5–2,5 раза, быстрее Arc B390 — в 1,3–2,2 раза. На **GPU Effects** разрыв больше: iGPU 10,0–12,7, B390 17,0, RTX 4050 27,6, RTX 5060 47,2 (×2,2–4,7 к iGPU до 890M).
- **Среди iGPU (Resolve 20.0–20.3):** 890M 2 872 > Arc 140T 2 489 ≈ Arc 140V (32 ГБ) 2 451 ≈ 860M 2 402 > «Intel Graphics» 2 366 > Arc Meteor Lake 2 150. Разница между ними 10–35 %, между iGPU и RTX — в разы.
- **Premiere 25.1–25.2, общий балл:** Arc 140T 3 661, Arc 130T 3 591, 780M 3 038, 140V (32 ГБ) 2 834, 860M 2 882, Arc Meteor Lake 2 694, Iris Xe 1 651, UHD 1 599, 840M 2 051;
  RTX 4050 6 548, RTX 4060 7 850, RTX 5060 9 894.
  У 890M (4 326) и 880M (5 065) в этой группе GPU Effects 32,6 и 63,8 — в 3–6 раз выше любого другого iGPU (Lumetri ×40: 880M 35,8 при 11–19 у остальных).
  Скорее всего, в выборку попали машины с дискретной картой — не проверено. В Premiere 23.0–25.0 у 890M 3 450 и GPU Effects 13,3 — это ближе к правде.
- **4K HEVC 4:2:2 10 бит в Resolve:** Arc 140T 56, Arc 140V 67, B390 85 кадр/с — против 860M 43 и 890M 42 (AMD декодирует 4:2:2 процессором, раздел 4). RTX 5050/5060 — 222/191 (NVDEC 6‑го поколения).
- **UHD 48/64 EU** (i5‑13420H, i7‑13620H, Core 5 210H, Core 7 240H) — в Premiere 1 599 против 2 834–3 661 у Arc: вдвое медленнее на монтаже без дискретной карты.

## 4. Аппаратный декод и кодирование

Сводка из [`amd-codecs.md`](amd-codecs.md) (разделы 1–2) и [`../../Intel/notes/intel-cpu.md`](../../Intel/notes/intel-cpu.md) (раздел 2); строки NVIDIA сверены с матрицей NVIDIA 30.09.2026 (curl).
Обозначения: **Д** — аппаратный декод, **К** — аппаратное кодирование, «нет» — только процессором. Первая строка ячейки — что умеет железо; оговорки про программы — под таблицей.

| Видеоядро (из списка) | Медиаблок | H.264 8 бит 4:2:0 | H.264 10 бит 4:2:0 | H.264 4:2:2 | HEVC 4:2:0 8/10 бит | HEVC 4:2:2 10 бит | HEVC 4:4:4 | AV1 |
|---|---|---|---|---|---|---|---|---|
| UHD 48/64 EU, Iris Xe 80/96 EU (i5‑13420H, i7‑13620H, i9‑13900H, Core 5/7 2xxH) | Intel Raptor Lake (TGLx) | Д/К | нет | нет | Д/К | **Д** (К — через шейдеры) | Д/К | Д, **К нет** |
| Arc 7/8‑Core, Graphics 4‑Core, Arc 130T/140T (Core Ultra 1xxH/U, 2xxH/U) | Intel Meteor/Arrow Lake (MTLx) | Д/К | нет | нет | Д/К | **Д/К** | Д/К | Д/К |
| Arc 130V/140V (Core Ultra 2xxV) | Intel Lunar Lake (LNL) | Д/К | нет | нет | Д/К | **Д/К** | Д/К | Д/К (+ VVC Д) |
| Graphics 4 Xe3, Arc B370/B390 (Core Ultra 3xx) | Intel Panther Lake (PTL) | Д/К | **Д/К** | **Д 10 бит** | Д/К | **Д/К** | Д/К | Д/К (+ VVC Д) |
| Radeon 660M/680M (R5 7535HS, R7 7735HS) | AMD VCN 3.1.1 (Rembrandt) | Д/К | нет | нет | Д/К | нет | нет | Д, **К нет** |
| Radeon 740M/760M/780M (Ryzen 5 220/230/240, Ryzen 7 250/260, 7840HS, 8645HS/8845HS) | AMD VCN 4.0.2 | Д/К | нет | нет | Д/К | нет | нет | Д/К |
| Radeon 820M/840M/860M/880M/890M (Ryzen AI 300/400) | AMD VCN 4.0.5 | Д/К | нет | нет | Д/К | нет | нет | Д/К |
| RTX 3050 / 3050 6GB Laptop | NVIDIA Ampere: NVDEC 5, NVENC 7 | Д/К | нет | нет | Д/К | нет | Д/К | Д, **К нет** |
| RTX 4050/4060 Laptop (и RTX 3050 A — Ada, в матрице нет) | NVIDIA Ada: NVDEC 5, NVENC 8 | Д/К | нет | нет | Д/К | нет | Д/К | Д/К |
| RTX 5050/5060/5070 Laptop | NVIDIA Blackwell: NVDEC 6, NVENC 9 | Д/К | **Д** | **Д/К** | Д/К | **Д/К** | Д/К | Д/К |

Источники и оговорки:
- **Intel, железо:** таблица media-driver ([media_features.md](https://raw.githubusercontent.com/intel/media-driver/master/docs/media_features.md)): H.264 — только NV12 (8 бит 4:2:0) на TGLx, MTLx, LNL; AV1‑кодирование — с MTLx.
  Даташиты Intel: Raptor Lake — AVC только 4:2:0 8 бит, HEVC до 4:2:2/4:4:4, AV1 только декод ([декод](https://edc.intel.com/content/www/us/en/design/products/platforms/details/raptor-lake-s/13th-generation-core-processors-datasheet-volume-1-of-2/hardware-accelerated-video-decode/), [кодирование](https://edc.intel.com/content/www/us/en/design/products/platforms/details/raptor-lake-s/13th-generation-core-processors-datasheet-volume-1-of-2/hardware-accelerated-video-encode/));
  Meteor Lake — HEVC Main10 4:2:2 кодирование до 4K@60 ([Intel EDC](https://edc.intel.com/content/www/us/en/design/products/platforms/details/meteor-lake-u-p/core-ultra-processor-datasheet-volume-1-of-2/hardware-accelerated-video-encode/)).
- **Panther Lake:** даташит Intel Core Ultra Series 3 (872188, табл. 77) — декод H.264 4:2:0 8/10 бит и 4:2:2 10 бит ([cdrdv2.intel.com](https://cdrdv2.intel.com/v1/dl/getContent/872188?fileName=872188-002.pdf));
  Resolve Studio 21 — «Intel QuickSync H.264 10-bit 4:2:0 and 4:2:2 decode support» ([readme Blackmagic](https://www.blackmagicdesign.com/support/readme/2cda7ec076ea4b25aaa007fc68a5cbfc)); Premiere и бесплатный Resolve — нет; независимых тестов нет (проверка 5.13 в [`browser-todo.md`](../../Intel/notes/browser-todo.md)).
- **AMD:** AMF‑вики — «All codecs are 4:2:0», AVC‑декод «8b» у VCN 2.0–5.0 ([GPUOpen AMF Wiki](https://github.com/GPUOpen-LibrariesAndSDKs/AMF/wiki/GPU%20and%20APU%20HW%20Features%20and%20Support)); версии VCN — таблица ядра Linux ([amdgpu CSV](https://raw.githubusercontent.com/torvalds/linux/master/Documentation/gpu/amdgpu/apu-asic-info-table.csv)).
  Живая проверка VA‑API на Radeon 780M пользователя: H.264 — только 4:2:0 8 бит, HEVC — только 4:2:0 ([`amd-codecs.md`](amd-codecs.md), [LV1]).
- **NVIDIA:** [матрица NVDEC/NVENC](https://developer.nvidia.com/video-encode-and-decode-gpu-support-matrix-new): RTX 3050 Laptop — NVDEC 5: H.264 10 бит и 4:2:2 NO, HEVC 4:2:2 NO, HEVC 4:4:4 и AV1 YES; NVENC 7: AV1 NO.
  RTX 4060 Laptop — то же, NVENC 8: AV1 YES. RTX 5070 Laptop — всё YES, включая H.264 4:2:2 и HEVC 4:2:2 (декод и кодирование).
  **RTX 5050/5060 Laptop в матрице нет**; у них NVDEC 6‑го поколения ([NVIDIA, сравнение ноутбучных GPU](https://www.nvidia.com/en-us/geforce/laptops/compare/)), который по [whitepaper Blackwell](https://images.nvidia.com/aem-dam/Solutions/geforce/blackwell/nvidia-rtx-blackwell-gpu-architecture.pdf) даёт «4:2:2 H.264 and HEVC decode». RTX 3050 A в матрице нет — возможности по архитектуре Ada, **не проверено**.
- **В программах (тесты Puget, [Resolve Studio](https://www.pugetsystems.com/labs/articles/what-h-264-and-h-265-hardware-decoding-is-supported-in-davinci-resolve-studio-2122/), [Premiere](https://www.pugetsystems.com/labs/articles/what-h-264-and-h-265-hardware-decoding-is-supported-in-premiere-pro-2120/), июнь 2025):**
  - HEVC 4:2:2 10 бит: Intel 11–14 и Core Ultra 200 — да в обеих; Radeon и iGPU Ryzen — нет; RTX 20/30/40 — нет; RTX 50 — да (Resolve 20+, Premiere 25.3+).
  - H.264 10 бит и H.264 4:2:2: нет ни у кого, кроме RTX 50 (и Panther Lake в Resolve Studio 21 — см. выше).
  - HEVC 4:4:4 и 12 бит: Intel и RTX — да в Resolve; в Premiere — нет ни у кого.
  - Lunar Lake и Panther Lake Puget в этих статьях не тестировал. Косвенно: в Puget Bench у Arc 140V «4K HEVC 4:2:2 10 бит» в Resolve — 67 кадр/с против 42–43 у 860M/890M (раздел 3.1).
  - Бесплатный Resolve под Windows GPU‑декод не использует — только Studio ([Blackmagic, кодеки Resolve 21](https://documents.blackmagicdesign.com/SupportNotes/DaVinci_Resolve_21_Supported_Codec_List.pdf)).
- **Отключённый HEVC:** HP, Dell и часть Acer отключают аппаратный HEVC на отдельных моделях — медиаблок тот же, но декода нет ([`hevc-amd.md`](hevc-amd.md), [`../../Intel/notes/hevc-audit.md`](../../Intel/notes/hevc-audit.md)).

## 5. Одноканальная память режет iGPU (замеры NBC)

У iGPU нет своей видеопамяти: одна планка вместо двух — вдвое меньше пропускной способности. Имя видеоядра у AMD при этом не меняется; у Intel Arc работает «nur als Intel Grafikmarke» ([даташит HP CU7G6EA](https://gzhls.at/blob/ldb/1/b/f/e/80d2945b99127777febcb5714b2521ae2d8c.pdf)), а Iris Xe — как UHD ([Intel](https://www.intel.com/content/www/us/en/support/articles/000094617/graphics.html)).

| Замер NBC | Чип | Тест | 1 планка | 2 планки | Потеря |
|---|---|---|---|---|---|
| [HP EliteBook 845 G10, та же машина с 1 и 2 планками (11.08.2023)](https://www.notebookcheck.net/Testing-the-performance-of-AMD-Radeon-780M-760M-iGPUs-with-new-drivers.740311.0.html) | R9 PRO 7940HS, Radeon 780M | Time Spy Graphics | 1 496 | 2 659 | **−44 %** |
| | | Fire Strike Graphics | 4 550 | 7 800 | −42 % |
| | | 3DMark 11 GPU | 7 868 | 11 811 | −33 % |
| [Minisforum AI X1 Pro (мини‑ПК), 1×32 → 2×32 ГБ DDR5 (12.05.2026)](https://www.notebookcheck.com/Minisforum-AI-X1-Pro-Einfaches-RAM-Upgrade-sorgt-fuer-spuerbar-mehr-Leistung-und-entfesselt-die-Radeon-890M.1293916.0.html) | Ryzen AI 9 HX 470, Radeon 890M | Time Spy Graphics | 1 950 | 3 658 | **−47 %** |
| | | Fire Strike Graphics | 5 173 | 9 192 | −44 % |
| | | Steel Nomad (DX12) | 367 | 695 | −47 % |
| | | 3DMark 11 GPU | 8 947 | 15 546 | −42 % |
| | | *процессор:* Geekbench 6.7 Multi | 11 437 | 15 605 | −27 % |
| | | *процессор:* HWBOT x265 4K, кадр/с | 24,9 | 28,5 | −13 % |
| | | *процессор:* Cinebench 2024 Multi | 1 118 | 1 247 | −10 % |
| | | *процессор:* Cinebench R23 Multi | 23 208 | 23 775 | −2 % |
| | | *процессор:* Blender 3.3 Classroom, с ↓ | 214 | 211 | ≈ 0 |
| [ThinkPad E14 G7 21SYS00H00: 1×16, «Single-Channel» (28.07.2025)](https://www.notebookcheck.com/Lenovo-ThinkPad-E14-G7-im-Test-Guenstiges-Office-Notebook-hebt-sich-mit-120-Hz-Display-von-der-Konkurrenz-ab.1066977.0.html) против [ThinkBook 14 G8 21SJ007SGE: 2×16 SO‑DIMM (27.07.2025)](https://www.notebookcheck.com/Dieser-erschwingliche-Lenovo-Laptop-ist-aufruestbarer-als-die-meisten-ThinkPads-ThinkBook-14-Gen-8-IAL-Test.1069611.0.html) | Core Ultra 7 255H, Arc 140T | Time Spy Graphics | 2 466 | 3 629 | **−32 %** |
| | | Fire Strike Graphics | 5 433 | 9 870 | −45 % |
| | | 3DMark 11 GPU | 9 684 | 13 661 | −29 % |

- Minisforum: числа «1 планка / 2 планки» — пары из графиков статьи (конфигурации 32768 и 65536 МБ). NBC: у iGPU «Leistungssteigerungen von bis über 100 Prozent», у процессора — «um etwa 5 bis 15 Prozent».
- ThinkPad E14 G7 и ThinkBook 14 G8 — **разные ноутбуки** с разным лимитом (E14: 28/45 Вт; ThinkBook в «Beste Leistung»: 38/50 Вт), так что не вся разница — от памяти.
  NBC о E14: iGPU «aufgrund der Single-Channel-RAM-Konfiguration nicht das volle Potenzial» и минус «Testgerät mit Single-Channel-RAM». Его 2 466 — минимум Arc 140T во всей базе NBC (раздел 2).
- **Ещё одноканальные тестовые ноутбуки** (сравнение с медианой NBC из раздела 2, разные машины):
  - Asus ExpertBook PM3406 (Ryzen AI 7 350, 860M) — Time Spy Graphics 1 698 против медианы 2 565 (−34 %); NBC: «only with single-channel RAM in the test device» ([обзор](https://www.notebookcheck.net/Asus-ExpertBook-PM3-Review-Office-laptop-with-AMD-long-battery-life-and-Copilot.1200511.0.html));
  - Dynabook Tecra A65‑M (Ryzen 7 250, 780M, 16 ГБ single‑channel) — 1 587 против 2 808 (−43 %) ([обзор](https://www.notebookcheck.net/Dynabook-Tecra-A65-M-laptop-review-Suitable-ThinkPad-E-or-EliteBook-alternative.1202807.0.html)).
- **Вывод:** одна планка отнимает у iGPU 30–47 % в 3DMark — это больше, чем разница между 780M и 890M (≈ 19 % по медианам Time Spy). Для 4K‑монтажа на iGPU двухканал обязателен, что и записано в жёстких критериях.
  Замера «одна планка против двух» прямо в Resolve или Premiere у NBC нет — **не проверено**.

## 6. Разброс одного чипа между ноутбуками (лимит мощности)

По строкам тестов на страницах NBC из разделов 1–2 (мини‑ПК, приставки и игровые консоли отброшены). В скобках — PL2/PL1 процессора или TGP видеокарты, как их записал NBC.

**Процессоры, Cinebench R23 Multi:**

| CPU | Медиана NBC | Самый медленный ноутбук | Самый быстрый ноутбук | Разброс |
|---|---|---|---|---|
| [Core Ultra 7 155H](https://www.notebookcheck.net/Intel-Core-Ultra-7-155H-Processor-Benchmarks-and-Specs.783323.0.html) | 15 028 (52) | MSI Prestige 13 AI Evo — 9 769 (лимит не указан); LG Gram 17 (44/22 Вт) — 9 977 | Honor MagicBook Pro 16 2024 (90/60 Вт) — 19 007 | ×1,95 |
| [Core Ultra 7 255H](https://www.notebookcheck.net/Intel-Core-Ultra-7-255H-Processor-Benchmarks-and-Specs.944139.0.html) | 17 845 (20) | Honor MagicBook Art 14 2025 (40/26 Вт) — 16 105 | Lenovo Yoga Pro 9 16IAH10 (115/80 Вт) — 22 578 | ×1,40 |
| [Core i9-13900H](https://www.notebookcheck.net/Intel-Core-i9-13900H-Processor-Benchmarks-and-Specs.677396.0.html) | 17 471 (28) | Samsung Galaxy Book3 Ultra 16 (75/70 Вт) — 13 177 | MSI Stealth 17 Studio (135/115 Вт) — 20 385 | ×1,55 |
| [Core Ultra 7 258V](https://www.notebookcheck.net/Intel-Core-Ultra-7-258V-Processor-Benchmarks-and-Specs.892883.0.html) | 10 301 (25) | Dynabook Portégé Z40L‑N (32/17 Вт) — 7 920 | MSI Prestige 13 AI+ Evo (40/27 Вт) — 11 097 | ×1,40 |
| [Ryzen 7 7840HS](https://www.notebookcheck.net/AMD-Ryzen-7-7840HS-Processor-Benchmarks-and-Specs.680876.0.html) | 16 156 (19) | Tuxedo Pulse 14 Gen3 (65/45 Вт) — 15 515 | XMG Core 16 L23 — 17 205 | ×1,11 |
| [Ryzen 7 8845HS](https://www.notebookcheck.net/AMD-Ryzen-7-8845HS-Processor-Benchmarks-and-Specs.780991.0.html) | 16 192 (13) | Lenovo IdeaPad 5 2‑in‑1 14AHP9 (60/36 Вт) — 14 895 | XMG Core 15 M24 (90/80 Вт) — 18 037 | ×1,21 |
| [Ryzen 7 260](https://www.notebookcheck.net/AMD-Ryzen-7-260-Processor-Benchmarks-and-Specs.945912.0.html) | 17 212 (6) | Asus Vivobook 18 M1807HA (60/54 Вт) — 15 864 | Lenovo Legion 5 15AHP10 (85/80 Вт) — 17 712 | ×1,12 |
| [Ryzen AI 7 350](https://www.notebookcheck.net/AMD-Ryzen-AI-7-350-Processor-Benchmarks-and-Specs.949825.0.html) | 16 014 (18) | Asus Zenbook 14 OLED UM3406K (45/32 Вт) — 12 647 | Acer Nitro 18 AI (125/75 Вт) — 18 243 | ×1,44 |
| [Ryzen AI 9 HX 370](https://www.notebookcheck.net/AMD-Ryzen-AI-9-HX-370-Processor-Benchmarks-and-Specs.836729.0.html) | 21 761 (32) | Asus ProArt P16 H7606WI — 10 435 / 12 627 / 15 849 (три строки одного ноутбука; скорее всего, разные режимы питания) | Asus ROG Zephyrus G14 2025 (80/80 Вт) — 23 902 | ×2,29 |

**Видеоядра, Time Spy Graphics:**

| GPU | Медиана NBC | Самый медленный ноутбук | Самый быстрый ноутбук | Разброс |
|---|---|---|---|---|
| [Radeon 780M](https://www.notebookcheck.net/AMD-Radeon-780M-GPU-Benchmarks-and-Specs.680539.0.html) | 2 808 (81) | HP EliteBook 845 G10 — 1 496 (**одна планка**, раздел 5) | Tuxedo Pulse 14 Gen3 (7840HS 65/45 Вт) — 3 027 | ×2,02 |
| [Radeon 680M](https://www.notebookcheck.net/AMD-Radeon-680M-GPU-Benchmarks-and-Specs.589860.0.html) | 2 303 (41) | HP EliteBook 845 G9 (6950HS 50/40 Вт) — 1 359 | HP Dragonfly Pro 2023 (7736U 51/40 Вт) — 2 607 | ×1,92 |
| [Radeon 860M](https://www.notebookcheck.net/AMD-Radeon-860M-Benchmarks-and-Specs.949852.0.html) | 2 565 (23) | Asus Vivobook 16 M1606K (50/40 Вт, 16 ГБ) — 1 656 | Lenovo Yoga Pro 7 14AKP10 (85/70 Вт) — 2 987 | ×1,80 |
| [Radeon 890M](https://www.notebookcheck.net/AMD-Radeon-890M-Benchmarks-and-Specs.843536.0.html) | 3 331 (33) | Asus ExpertBook PM5 G2 (HX 470 52/48 Вт, 16 ГБ, одна планка — [обзор NBC](https://www.notebookcheck.net/AMD-business-laptop-with-a-great-144-Hz-IPS-display-Asus-ExpertBook-PM5-G2-review.1368549.0.html)) — 2 062 | Asus Vivobook S 14 OLED M5406WA (HX 370 65/54 Вт) — 3 676 | ×1,78 |
| [Arc 8‑Core (155H)](https://www.notebookcheck.net/Intel-Arc-8-Cores-iGPU-Benchmarks-and-Specs.782930.0.html) | 3 270 (48) | MSI Prestige 13 AI Evo — 2 018 | Lenovo IdeaPad Pro 5 16IMH9 (70/50 Вт) — 3 770 | ×1,87 |
| [Arc 140T](https://www.notebookcheck.net/Intel-Arc-140T-Benchmarks-and-Specs.942050.0.html) | 3 843 (20) | ThinkPad E14 G7 (45/28 Вт, **одна планка**) — 2 466 | Lenovo Yoga Pro 7 14IAH10 (285H 115/75 Вт) — 4 387 | ×1,78 |
| [Arc 140V](https://www.notebookcheck.net/Intel-Arc-Graphics-140V-Benchmarks-and-Specs.854991.0.html) | 4 044 (42) | Asus Zenbook S 14 UX5406 — 2 955 | Microsoft Surface Laptop 7 15 (268V 37/30 Вт) — 4 415 | ×1,49 |
| [Iris Xe 96 EU](https://www.notebookcheck.net/Intel-Tiger-Lake-U-Xe-Graphics-G7-96EUs-GPU-Benchmarks-and-Specs.462145.0.html) | 1 560 (218) | Samsung Galaxy Book2 Pro 360 (режим «Still») — 707 | Lenovo Yoga Slim 9 14IAP7 (52/35 Вт) — 1 871 | ×2,65 |
| [RTX 4050 Laptop](https://www.notebookcheck.net/NVIDIA-GeForce-RTX-4050-Laptop-GPU-Benchmarks-and-Specs.675695.0.html) | 8 125 (41) | Dell XPS 14 2024 (TGP 30 Вт) — 5 107 | Lenovo LOQ 15APH8 (95 Вт) — 9 040 | ×1,77 |
| [RTX 4060 Laptop](https://www.notebookcheck.net/NVIDIA-GeForce-RTX-4060-Laptop-GPU-Benchmarks-and-Specs.675692.0.html) | 10 338 (56) | MSI Cyborg 15 A12VF (45 Вт) — 7 484 | XMG Core 15 M24 (140 Вт) — 11 451 | ×1,53 |
| [RTX 5050 Laptop](https://www.notebookcheck.net/Nvidia-GeForce-RTX-5050-Laptop-Benchmarks-and-Specs.934804.0.html) | 9 122 (9) | MSI Cyborg 15 B2RWEKG (45 Вт) — 7 166 | Schenker Fusion 15 L25 (115 Вт) — 9 828 | ×1,37 |
| [RTX 5060 Laptop](https://www.notebookcheck.net/Nvidia-GeForce-RTX-5060-Laptop-Benchmarks-and-Specs.934941.0.html) | 11 937 (22) | MSI Cyborg 17 B13WFKG (55 Вт) — 9 090 | Lenovo LOQ 15AHP11 (105 Вт) — 12 719 | ×1,40 |
| [RTX 5070 Laptop](https://www.notebookcheck.net/Nvidia-GeForce-RTX-5070-Laptop-Benchmarks-and-Specs.934942.0.html) | 13 564 (35) | Dell 16 Premium DA16250 (60 Вт) — 10 851 | Asus TUF Gaming A16 FA608UP (115 Вт) — 14 771 | ×1,36 |

Что из этого следует:
- **Процессор в тонком ноутбуке теряет 20–35 % многопотока против медианы** (155H −35 %, i9‑13900H −25 %, AI 7 350 −21 %), а против самого быстрого корпуса — 30–50 %. У HX 370 в ProArt P16 — вдвое (вероятно, тихий режим). У Hawk Point (7840HS/8845HS/260) разброс меньше — ×1,1–1,2: он почти везде стоит в толстых корпусах с 45+ Вт.
- **iGPU разбегается почти вдвое** (×1,5–2,0), и самые медленные строки — часто одноканальные машины (780M, 140T, 890M). По медиане не выбрать: смотреть обзор конкретной модели или хотя бы лимит мощности и раскладку памяти.
- **RTX одного имени** отличается в 1,4–1,8 раза по TGP. RTX 4060 на 45 Вт (7 484) медленнее RTX 4050 на 95 Вт (9 040); RTX 5070 на 60 Вт (10 851) лишь на 10 % быстрее RTX 5050 на 115 Вт (9 828). TGP смотреть в спецификации ноутбука.
- Строки NBC сняты в разных режимах питания и с разными драйверами; одна и та же модель может встречаться несколько раз.

## 7. Итог для выбора (по таблицам)

- **Процессор для 4K‑монтажа:** по многопотоку (Cinebench R23/2024, x265, Blender) верх списка — Ryzen AI 9 HX 370 (21 761), Ryzen AI 9 365 (18 698), Core Ultra 7 356H (18 395), Ultra 7 255H (17 845), i9‑13900H (17 471), Ryzen AI 7 450 (17 302), Ryzen 7 260 (17 212).
  Середина — Ryzen AI 7 350, 7840HS/8845HS, Core 7 250H (1 ноутбук), Ultra 7 155H, i7‑13620H/Core 7 240H (15–16 тыс.). Низ — 4‑ядерный Ryzen AI 5 330 (7 840), Ryzen 5 7535HS (8 613), Lunar Lake (~10 000), Ultra 5 125U (9 799).
- **iGPU (Time Spy Graphics):** Arc B390 (6 653) > B370 (6 050, 2 ноутбука) ≫ Arc 140V (4 044) ≈ Arc 140T (3 843) > Arc 130V (3 401) ≈ 880M/890M (~3 330) ≈ Arc 8‑Core (3 270) > Graphics 4 Xe3 (2 903) ≈ 780M (2 808) > 860M (2 565) > Arc 130T (2 378) ≈ 680M/760M (~2 300) ≫ Graphics 4‑Core (1 902), Iris Xe, UHD, 740M/840M (800–1 560), 820M (786).
  В Puget‑монтаже (раздел 3) iGPU ближе друг к другу (±15–35 %), а RTX 4050+ быстрее в 1,5–2,5 раза и в 2–4,7 раза на эффектах.
- **Кодеки:** для неизвестной камеры шире всех RTX 50 (всё, включая H.264/HEVC 4:2:2) и Panther Lake (H.264 4:2:2 10 бит — только Resolve Studio 21); затем любой Intel с 11‑го поколения (HEVC 4:2:2); у AMD 4:2:2 нет ни в одном поколении (раздел 4).
- **Две оговорки к любым медианам:** одна планка режет iGPU на 30–47 % (раздел 5), лимит мощности меняет результат в 1,1–2,3 раза (раздел 6).
