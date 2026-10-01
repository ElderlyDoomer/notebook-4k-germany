# Как снимать данные с idealo.de в Chrome пользователя

Проверено 30.09.2026. idealo и geizhals не отдают страницы в curl и WebFetch (403), а в Chrome пользователя (расширение Claude in Chrome) открываются.

## Инструменты

Загрузить одним запросом ToolSearch:
`select:mcp__claude-in-chrome__tabs_context_mcp,mcp__claude-in-chrome__tabs_create_mcp,mcp__claude-in-chrome__tabs_close_mcp,mcp__claude-in-chrome__navigate,mcp__claude-in-chrome__get_page_text,mcp__claude-in-chrome__javascript_tool,mcp__claude-in-chrome__find,mcp__claude-in-chrome__computer,mcp__claude-in-chrome__browser_batch`

- `tabs_context_mcp` (createIfEmpty: true) → `tabs_create_mcp` → работать только в своей вкладке → в конце `tabs_close_mcp`. Параллельные агенты — каждый в своей вкладке.
- Данные снимать через `javascript_tool` (компактно), а не скриншотами и не полным `get_page_text`: так дешевле по токенам.
- Одна загрузка страницы за раз. Капча — не проходить: остановиться и попросить пользователя.

## Поиск в интернете — Google в Chrome пользователя

Встроенный WebSearch ищет по американскому индексу и делит лимит между агентами; curl к Google получает капчу, поэтому агенты уходили в html.duckduckgo.com — там меньше данных.
Для немецких магазинов, даташитов, форумов, P/N — **Google в своей вкладке Chrome** (проверено 30.09.2026: без капчи, выдача немецкая — idealo, geizhals, магазины, Campus):

`https://www.google.de/search?q=<запрос>&hl=de&gl=de&num=20`

```js
[...document.querySelectorAll('a h3')].slice(0,20).map(h=>({t:h.innerText.slice(0,100), u:(h.closest('a')||{}).href}))
```

- Англоязычные первоисточники (Puget, NVIDIA, Intel, AMD, notebookcheck.net) — можно и через WebSearch.
- Не частить: один запрос → прочитать результаты → следующий. Появилась капча «ungewöhnlicher Datenverkehr» — остановиться, попросить пользователя, пока — Bing (`https://www.bing.com/search?q=…&cc=de`).
- DuckDuckGo — только если Google и Bing недоступны.

## Поиск по парт-номеру

`https://www.idealo.de/preisvergleich/MainSearchProductCategory.html?q=<P/N>`

Ссылки на карточки: `[...new Set([...document.querySelectorAll('a[href*="OffersOfProduct"]')].map(a=>a.href))].slice(0,10)`

Карточка товара — `https://www.idealo.de/preisvergleich/OffersOfProduct/<pid>_-<slug>.html`. Эту ссылку и давать в отчёте.
В блоке «Variante:» — родственные P/N той же модели с ценами «ab».

## Карточка: предложения, характеристики, история цен

```js
const pid = location.pathname.match(/OffersOfProduct\/(\d+)/)[1];
const j = await fetch('/price-chart/sites/1/products/'+pid+'/history?period=1Y').then(r=>r.json());
const d = j.data||[]; const last182 = d.slice(-182);
const min = d.reduce((m,p)=>p.y<m.y?p:m, d[0]||{y:0});
const le = last182.filter(p=>p.y<=110000);
const offers=[...document.querySelectorAll('li.productOffers-listItem')].map(li=>{const t=li.innerText.replace(/\s+/g,' ');return {shop:(li.querySelector('img[alt]')||{}).alt||(t.match(/Verkauf durch: (\S+)/)||[])[1], title:t.slice(0,120), total:(t.match(/([\d.]+,\d{2}) € inkl\. Versand/)||[])[1], marketplace:/Marktplatz/.test(t), conditional:/Preis nur mit|Gutschein/.test(t), ret:(t.match(/Rücksendung \d+ Tage/)||[])[0]}});
const details=[...document.querySelectorAll('.datasheet-listItem, [class*="datasheet"] li, table tr')].map(e=>e.innerText.replace(/\s+/g,' ').trim()).filter(Boolean).slice(0,80);
({pid, title:document.title, stats:j.statistics, min1y:min, daysLe1100_182:le.length, lastLe1100:(le[le.length-1]||{}).x, offers, details})
```

- История: `period=3M | 6M | 1Y`; `y` — дневной минимум в центах (114900 = 1149,00 €); `statistics` — средняя, минимальная, максимальная цена за период.
- В `details` есть «Prozessor Codename» (Hawk Point, Raptor Lake-H, Arrow Lake-H…) — удобно ловить старые процессоры под новыми именами.
- Цена кандидата — самая низкая цена нового товара с доставкой у любого продавца, **маркетплейсы (Kaufland, Amazon Marketplace, eBay) включительно** (правило пользователя, корневой `CLAUDE.md`). Срок возврата и рейтинг продавца — справка.
- Условные цены («Preis nur mit …»-подписка, «Gutschein») за минимум не брать — записывать отдельно. Б/у, B-Ware, refurbished — не считаются.
- **Оплата наличными (жёсткий критерий, корневой `CLAUDE.md`).** Способы оплаты видны в строке предложения — добавь в сниппет:
  `pay:(t.match(/Vorkasse|Nachnahme|Rechnung|Lastschrift|PayPal|Kreditkarte|Barzahlung|Abholung|Klarna|Sofort|eps|Apple Pay|Google Pay/g)||[])`.
  В строке idealo видны не все способы — у финалистов проверь на сайте магазина («Zahlungsarten», «Abholung im Markt / in der Filiale»).
  Наличными можно: Nachnahme (сбор прибавить к цене), самовывоз с оплатой на месте, покупка в магазине сети.

## Скан категории «Notebooks» (3751)

`https://www.idealo.de/preisvergleich/ProductCategory/3751F<id1>-<id2>-<id3>.html?sortKey=minPrice` — фильтры через дефис, сортировка по цене.
Проверять по `document.title`: в нём перечислены применённые фильтры.

| Фильтр | id |
|---|---|
| Intel | 107335535 |
| AMD | 848110 |
| RAM 32 GB | 7612877 |
| SSD 1 TB | 2682401 |
| ohne Betriebssystem | 1059385 |
| RTX 5050 / 5060 / 4060 | 106843055 / 106745465 / 104023766 (проверить по title) |

| 16 Zoll / 15 Zoll | 1568565 / 699493 |

Остальные id (RAM 16/24 GB, кодовое имя CPU) — ссылками `a[href*="ProductCategory/3751"]` с текстом фильтра на странице категории.

- **Пагинация:** в путь добавляется `I16-<15×(N−1)>`, т. е. страница 2 — `3751I16-15F….html`, страница 3 — `3751I16-30F….html`.
- **Фильтр производителя CPU теряет товары:** у части карточек нет поля «Prozessorhersteller» (так выпали 83HS00BLGE, MD600023, 22AY004XGE, 21UR005AGE).
  Всегда делай второй проход без фильтра Intel/AMD (только RAM + SSD + размер) и отбирай по названию CPU вручную.
- **API истории** днём 30.09.2026 временами отвечал 404 на все товары (и график на странице пропадал); через какое-то время снова 200. Если 404 — повтори позже, не долби.
- **Даташит idealo ошибается** (размер экрана, Гц, SSD, «DDR5» вместо распаянной LPDDR5) — раскладку памяти и SSD подтверждай даташитом производителя.
