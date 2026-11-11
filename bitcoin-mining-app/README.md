# The Honest Bitcoin Generator

A single-file web app that answers the question *"can an app generate 1 bitcoin a day?"*
with real numbers — and then shows the out-of-the-box path that actually works.

## How to open it

No install, no server. Just open `index.html` in any modern browser
(double-click it, or drag it into Chrome/Safari/Edge). With internet access it
pulls live Bitcoin price and network data from mempool.space and CoinGecko;
offline it falls back to built-in estimates and says so in the banner.

## What's inside

1. **The dream, priced** — enter any target (default 1 BTC/day) and see the real
   requirements: the share of the world's mining power you'd need, thousands of
   ASIC machines, tens of millions of dollars of hardware, megawatts of power,
   and the daily electricity bill at Singapore tariffs. It also shows what a
   normal computer would earn: a fraction of one satoshi per day, with millions
   of years to reach 1 BTC.

2. **Your real generator** — the honest reframe: bitcoin is *earned*, not
   conjured. Plug in your average job price, jobs per month, and the percentage
   you set aside, and see sats stacked per job, BTC per month, and a dated
   milestone plan to your first million sats, 0.1 BTC, 0.5 BTC and 1 whole coin.

3. **Feel the proof-of-work** — a toy miner running real double-SHA256 in your
   browser (WebCrypto). Adjust the difficulty, watch blocks get found, and see
   how many times faster the real network is (spoiler: the wait for a real block
   would be measured in billions of years).

4. **Scam shield** — the red flags of every "bitcoin generator" scam.

## Why 1 BTC/day is impossible

- The Bitcoin protocol mints ~450 new BTC per day **globally** (144 blocks x
  3.125 BTC), shared by all miners in proportion to computing power.
- Earning 1 BTC/day therefore requires ~1/450th of the entire world's hashrate —
  thousands of industrial ASIC machines (~US$30M+), megawatts of electricity.
- No software trick changes this: difficulty adjusts automatically so that more
  total mining power never mints coins faster.
- Consequently, **every** app/site/bot promising free or fast bitcoin generation
  is fraudulent. Never enter a seed phrase or pay a "withdrawal fee".

## Security & privacy

Audited (static analysis + full source-to-sink data-flow review). Posture:

- **Fully client-side.** No server, no accounts, no wallet connections. The app
  never asks for — and has no code paths to receive — seed phrases or keys.
- **No data collection.** No cookies, no localStorage, no analytics, nothing
  transmitted. The only network traffic is two read-only HTTPS GET requests
  (CoinGecko price, mempool.space hashrate/height) with no personal data.
- **Content Security Policy** pins connections to those two hosts and blocks
  all external scripts, styles, images, and form posts.
- **Untrusted-data handling.** API responses are type- and range-validated
  before use, and every value interpolated into HTML is escaped; user inputs
  are parsed as numbers and clamped to sane ranges.
- **Graceful degradation.** Works offline (labeled estimates), without
  WebCrypto (miner disabled with an explanation), and without JavaScript
  (noscript notice).

## Disclaimer

Educational tool only. Not financial advice. Bitcoin is highly volatile — the
savings illustrations assume today's price stays flat, which it will not.
