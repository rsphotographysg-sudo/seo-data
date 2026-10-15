# 答案型文章 — 上线指南

5 篇英文文章，给 rsphotographysg.com 的 /insights 栏目。每篇都有：开头的直接回答、常见问题、Article + FAQPage 结构化数据（已用 `structured-data-fix/fix_structured_data.py` 检查，0 错误）、配图建议。

## 建议上线顺序（每周一篇）

| 周 | 文章 | 网址 | 上线前要确认 |
|---|---|---|---|
| 10 月 20 日那周 | 企业活动摄影报价指南 | /insights/corporate-event-photography-cost-singapore | 价格区间；交付时间；“当天回复报价”承诺；是否保留 Airtasker 行情对比 |
| 10 月 27 日那周 | 政府活动摄影：GeBIZ、bizSAFE、PDPA | /insights/government-event-photography-singapore | 已在 GeBIZ 注册；配图要有机构同意 |
| 11 月 3 日那周 | 会议摄影清单 | /insights/conference-photography-checklist | “回复报价时附上草拟拍摄清单”承诺 |
| 11 月 10 日那周 | 当天交付是怎么做到的 | /insights/same-day-event-photo-delivery-singapore | EXPRESS 24 名称和“1 小时内首批照片”；表格里的照片数量（10–30 张、50–150 张）是否符合你的做法 |
| 11 月 17 日那周 | 如何挑选新加坡企业活动摄影师 | /insights/how-to-choose-corporate-event-photographer-singapore | “回复报价时书面回答 10 个问题并附完整相册”承诺；第 10 题提到公众责任险，上线前最好先买好保险 |

四篇都要确认：联系页的真实网址（文章里先写成 `/contact`）。

## 每篇上线步骤

1. 把 `[INTERNAL LINK: /路径 "文字"]` 换成真的链接，把 `[EXTERNAL LINK: …]` 换成对应网站的链接（不想放可以删掉）。
2. 页面 `<title>` 和 meta description 用文章最上面的 title 和 description。
3. 把 “Schema Markup” 里的两段 JSON 放进页面 `<head>`，用 `<script type="application/ld+json">` 包起来。
4. 发布后用 Google Rich Results Test 测一次，再在 Search Console 用“网址检查”请求编入索引。
5. 在 LinkedIn 分享一次（拍摄清单和价格表很适合做成图片）。

## 文章之间的链接

四篇互相链接，也链接到现有的 /rates、/insights/event-videography-rates-singapore 和 /insights/pdpa-event-photography-consent-guide。先上线的文章里指向还没上线文章的链接，可以先删掉，等那篇上线后再加回去。
