"""Screenshot a built page at desktop and mobile sizes for the review step.

Usage: python3 shoot.py site/index.html shots/
Needs Playwright: pip install playwright && python -m playwright install chromium
HandL Agency, MIT licence.
"""
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

SIZES = {"desktop": (1440, 900), "mobile": (390, 844)}


def main():
    page_path, out = Path(sys.argv[1]).resolve(), Path(sys.argv[2])
    out.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for name, (w, h) in SIZES.items():
            page = browser.new_page(viewport={"width": w, "height": h})
            errors = []
            page.on("pageerror", lambda e: errors.append(str(e)))
            page.goto(page_path.as_uri(), wait_until="networkidle")
            page.wait_for_timeout(2000)
            page.screenshot(path=str(out / f"{name}-hero.png"))
            height = page.evaluate("document.body.scrollHeight")
            for i, y in enumerate(range(h, height, h), start=1):
                page.evaluate(f"window.scrollTo(0, {y})")
                page.wait_for_timeout(1200)
                page.screenshot(path=str(out / f"{name}-{i:02d}.png"))
            overflow = page.evaluate("document.documentElement.scrollWidth > window.innerWidth")
            print(f"{name}: {height}px tall, horizontal overflow: {'YES, fix it' if overflow else 'no'}, JS errors: {len(errors)}")
            for e in errors:
                print("  ", e)
            page.close()
        browser.close()
    print("screenshots in", out)


if __name__ == "__main__":
    main()
