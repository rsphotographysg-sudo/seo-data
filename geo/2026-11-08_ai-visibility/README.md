# AI 答案可见度：修复包（2026 年 11 月 8 日）

对应报告里"AI 答案可见度"那一节的四行。

| 报告里的问题 | 怎么解决 | 用到的文件 | 谁做 |
|---|---|---|---|
| 品牌搜索：靠目录被找到，目录上的价格和资料不一致 | 登录 DesignRush、Sortlist、GoodFirms、TechBehemoths，按同一份文字更新资料；删掉每小时的价格，改成指向 /rates | `directory-profile.md` | Ricky（需要各目录的登录） |
| 非品牌搜索：没有出现 | 在 AI 答案会引用的名单上露面：开 Clutch 免费资料并请客户写评价；向 thebestsingapore.com 和 Medium 榜单作者推荐 | `listing-pitch.md` | Ricky；收费的项目先不做，要你决定 |
| HubSpot AEO：没有权限 | 不必花钱开通。每月 6 日的自动检查会用网页搜索复测，结果写进报告 | — | 已自动化 |
| 网站技术检查：无法访问网站 | 在网站根目录加上 `llms.txt`，并在 `robots.txt` 末尾加上允许 AI 爬虫的几行 | `llms.txt`、`robots-ai-snippet.txt` | Mac 上的发布流程或 Claude 会话 |

## 上线前请确认
- `llms.txt` 里没有写任何价格，只链接 /rates 和 /express-24。
- 成立年份写的是 2013 年，和网站一致。
- 不要把 `robots-ai-snippet.txt` 整个替换掉现有的 robots.txt，只把那几行加到末尾。
