---
name: accountant-website-builder
description: Build a cinematic, conversion-led homepage for a UK accountancy, bookkeeping, tax or payroll firm that ranks for "[service] in [town]" and turns visitors into enquiries. Use when someone asks for a website, homepage, landing page or website redesign for an accountant, bookkeeper, tax adviser or payroll bureau.
---

# Accountant Website Builder (HandL Agency)

Most accountancy websites look the same and say "Welcome to Smith & Co". The design is rarely why they don't bring in clients. The real reasons are an H1 that doesn't say the service and town, no prices, no face, and no way to get in touch where the visitor is reading. This skill builds a page that looks expensive **and** does the job.

Follow the steps in order.

## 1. Get the brief (ask once, then decide)
Ask for anything below you can't infer, in one short message. Fill in the rest yourself and say what you chose.
- Firm name, the **service** (e.g. "Accountants", "Bookkeeping", "Contractor accountants") and the **town or area**.
- Who they help (one niche beats "all businesses"), and what makes them different (fixed fees, same accountant every call, response time).
- The one action a visitor should take (e.g. "Get a fixed quote"). One main button, used everywhere.
- Mood in three words, brand colours, and their own photos or video if they have them.

## 2. Write the brief file
Write `brief.json` using `references/brief.md`. Copy the closest file in `examples/` and change it; don't start from blank. Rules:
- `h1` must contain the service and the town. Make it human, not a keyword dump: "Accountants in Bristol, finally on your side."
- `sub` is 120 to 165 characters, so it doubles as the meta description.
- `stats` are things the firm actually promises (reply time, check-ins a year). **Never invent client results, reviews or awards.**
- Pick the layout with `references/layouts.md`.

## 3. Media
In order of preference:
1. The firm's own photos or video. Faces of the real team beat anything else (see `references/finance-rules.md`).
2. Video or images the user has the rights to use (their own stock licence, or a generator they've used).
3. None: set `video` to `null` and the page uses an animated gradient built from `glow`. It's designed to look finished, not empty.

Never hotlink media you don't have the rights to, and never use stock photos of handshakes or calculators.

## 4. Build
Run `python3 scripts/build.py brief.json site/`. It writes `site/index.html` (one file, no build step, opens anywhere) and prints the SEO checks. Fix every failed check in the brief and build again.

## 5. Look and fix (don't skip this)
Run `python3 scripts/shoot.py site/index.html shots/` (it needs Playwright: `pip install playwright && python -m playwright install chromium`). Open the screenshots, look at them and score the page with `references/review.md`. Fix the three weakest points and shoot again. Stop when everything scores 4 or more, or after three rounds.

## 6. Hand over
Give the user:
- The `index.html` file and how to open it.
- The final desktop screenshot.
- The page title and H1, so they can see they say the service and the town.
- What to swap before going live: real photos, real prices, the booking or contact link, and the firm's regulatory wording (e.g. ICAEW/ACCA/AAT practising details) in the footer.

## Files
- `references/brief.md`: every field in `brief.json`.
- `references/layouts.md`: the three layouts and when to use each.
- `references/finance-rules.md`: the SEO and conversion rules for finance firm websites.
- `references/review.md`: the scoring rubric for step 5.
- `examples/*.json`: six finished briefs (accountants, bookkeepers, contractor accountants, e-commerce bookkeeping, tax returns, payroll).
- `scripts/build.py`: renders the page and runs the SEO checks.
- `scripts/shoot.py`: desktop and mobile screenshots for the review.
