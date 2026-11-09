# 点击率改写：首页和 PDPA 指南（2026 年 11 月 9 日）

10 月点击率从 1.95% 降到 1.36%。展示最多的两页是首页和 PDPA 指南，先改这两页的 `<title>` 和 meta description。

规则：不写任何价格数字；只写能核实的事实（2013 年成立、bizSAFE Level 3、可通过 GeBIZ 聘用、nett 报价、Express 24）。

---

## 1. 首页 `/`

现在的问题：品牌词以外，很少有人从首页点进来。标题要包含买家会搜的词。

```html
<title>Corporate Event Photographer Singapore | RS Photography</title>
<meta name="description" content="Corporate, MICE and government event photography and video in Singapore since 2013. bizSAFE Level 3, engageable via GeBIZ, nett quotes, Express 24 delivery.">
<meta property="og:title" content="Corporate Event Photographer Singapore | RS Photography">
<meta property="og:description" content="Corporate, MICE and government event photography and video in Singapore since 2013. bizSAFE Level 3, engageable via GeBIZ, nett quotes, Express 24 delivery.">
```

- 标题 55 个字符，描述 154 个字符，Google 一般能完整显示。
- 页面上的 H1 不用改。

## 2. PDPA 指南 `/insights/pdpa-event-photography-consent-guide`

现在的问题：这页展示很多，但标题没有回答"要不要征得同意"这个问题。

```html
<title>Do You Need Consent for Event Photos? PDPA Guide Singapore</title>
<meta name="description" content="What Singapore's PDPA means for event photography: when you need consent, how to tell guests, opt-outs, and how to handle and share photos safely.">
<meta property="og:title" content="Do You Need Consent for Event Photos? PDPA Guide Singapore">
<meta property="og:description" content="What Singapore's PDPA means for event photography: when you need consent, how to tell guests, opt-outs, and how to handle and share photos safely.">
```

- 标题 58 个字符，描述 148 个字符。
- 上线前请确认：页面正文确实讲了"告知来宾、不拍的选择、照片的保存和分享"。如果有哪一项没讲，把描述里那一项删掉。

---

## 交给 Mac 上的 Claude 会话的指令

> 从 seo-data 仓库拉取最新 main，按 geo/2026-11-09_ctr-titles/README.md，把首页和 /insights/pdpa-event-photography-consent-guide 的 title、meta description、og:title、og:description 换成文件里的文字。只改这几个标签，不改正文和结构化数据。确认 PDPA 页面正文确实讲了描述里提到的内容；跑网站检查后部署，部署前先问我。部署后在 Search Console 为这两个网址请求编入索引。

## 怎么看效果

Google 一般要 1–3 周才会显示新标题。12 月 6 日的自动检查会看 11 月的点击率；要比较准确，要等 1 月初的 12 月月报。
