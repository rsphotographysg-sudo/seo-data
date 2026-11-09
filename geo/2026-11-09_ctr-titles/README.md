# 点击率改写：首页和 PDPA 指南（2026 年 11 月 9 日）

10 月点击率从 1.95% 降到 1.36%。展示最多的两页是首页和 PDPA 指南，先改这两页的 `<title>` 和 meta description。

规则：不写任何价格数字；只写能核实的事实（2013 年成立、bizSAFE Level 3、可通过 GeBIZ 聘用、nett 报价、Express 24）。

---

## 1. 首页 `/`

现在的问题：品牌词以外，很少有人从首页点进来。标题要包含买家会搜的词。

```html
<title>Corporate Event Photographer Singapore | RS Photography</title>
<meta name="description" content="Corporate, MICE &amp; government event photography and video in Singapore since 2013. bizSAFE Level 3, engageable via GeBIZ, nett quotes, Express 24 delivery.">
<meta property="og:title" content="Corporate Event Photographer Singapore | RS Photography">
<meta property="og:description" content="Corporate, MICE &amp; government event photography and video in Singapore since 2013. bizSAFE Level 3, engageable via GeBIZ, nett quotes, Express 24 delivery.">
```

- 标题 55 个字符，描述 154 个字符（代码里的 `&amp;` 在页面上显示为 `&`），Google 一般能完整显示。
- 页面上的 H1 不用改。

## 2. PDPA 指南 `/insights/pdpa-event-photography-consent-guide`

现在的问题：这页展示很多，但标题没有回答"要不要征得同意"这个问题。

```html
<title>Do You Need Consent for Event Photos? PDPA Guide Singapore</title>
<meta name="description" content="What Singapore's PDPA means for event photography: when you need consent, how to tell guests, opt-outs, and how to handle and share photos safely.">
<meta property="og:title" content="Do You Need Consent for Event Photos? PDPA Guide Singapore">
<meta property="og:description" content="What Singapore's PDPA means for event photography: when you need consent, how to tell guests, opt-outs, and how to handle and share photos safely.">
```

- 标题 58 个字符，描述 146 个字符。
- 上线前请确认：页面正文确实讲了"告知来宾、不拍的选择、照片的保存和分享"。如果有哪一项没讲，把描述里那一项删掉。

---

## 交给 Mac 上的 Claude 会话的指令（一次做完）

Ricky 已同意直接上线：部署前不用再问，但网站检查、Codex 和 Antigravity 审核、失败回滚照常执行。

> 从 seo-data 仓库拉取 ctr-title-rewrite 分支（合并后就用 main），按 geo/2026-11-09_ctr-titles/README.md 做完下面三步，部署前不用问我。
>
> **第 1 步：首页和 PDPA 指南。** 把 title、meta description、og:title、og:description 换成文件里的文字。每种标签只能有一个。确认 PDPA 页正文讲到了描述里的每一项，没讲到的就从描述里删掉，不要补写新内容。
>
> **第 2 步：其余 8 页。** 在 Chrome 打开 Search Console，进入“效果”>“网页”，选最近 3 个月，按展示次数排序。除首页和 PDPA 指南外，选出展示次数最多、点击率低于 1% 的 8 页，按下面的规则改写它们的 title、meta description 和 og 标签：
> - 标题不超过 60 个字符，用这一页在 Search Console 里展示最多的搜索词开头或包含它，结尾加 \| RS Photography（放不下就省掉）。
> - 描述不超过 155 个字符，先直接回答这一页要回答的问题，再写一个事实。
> - 只用这些事实：2013 年成立、bizSAFE Level 3、可通过 GeBIZ 聘用、nett 报价、Express 24 交付、企业 / MICE / 政府活动摄影和视频。
> - 不写价格，不写网站上没有的服务或说法，不写客户名，不写“自有无人机执照”（只能说 licensed partner operator），不写评价或得奖。
> - 不改正文和结构化数据。
>
> **第 3 步：上线和记录。** 跑网站检查和结构化数据检查，Codex 和 Antigravity 都 PASS 才部署，任何一关不过就回滚并发 Telegram。部署后打开 10 个线上网址确认新标题生效，提交 IndexNow，并在 Search Console 为 10 个网址各请求一次编入索引。然后在 seo-data 仓库新建 geo/ctr-log.md，每页记一行：网址、上线日期、旧标题、新标题，以及改之前 3 个月的展示次数、点击和点击率（从 Search Console 抄）。提交到新分支并开 PR。最后用 Telegram 把这 10 页的新旧标题发给我。

## 怎么看效果

- Google 一般要 1–3 周才会显示新标题。
- 12 月 6 日的自动检查会读 geo/ctr-log.md，用 11 月月报比较这 10 页的点击率。比较准确的结果要等 1 月初的 12 月月报。
- 哪种写法点击率涨得多，就把它用到下一批页面。
