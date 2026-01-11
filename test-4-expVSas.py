import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")

   # assert page.is_hidden("name=Log in with Email")

    expect(page.locator("name=Log in with Email")).to_be_hidden()

with sync_playwright() as playwright:
    run(playwright)
