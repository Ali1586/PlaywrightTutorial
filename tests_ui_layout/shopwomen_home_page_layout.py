from playwright.sync_api import Playwright, sync_playwright, expect
from pom.shopwomen_element import Shop_women


def run(playwright: Playwright) -> None:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_context()
        page.goto("https://symonstorozhenko.wixsite.com/website-1")
        shop_women= Shop_women(page)
        expect(shop_women.celebrating_beauty_header).to_be_visible()
        expect(shop_women.celebrating_beauty_body).to_be_visible()

with sync_playwright() as playwright:
    run(playwright)
