import time
from re import search

from playwright.sync_api import Playwright, sync_playwright, expect
from pom.contact_us_page import ContactUsPage


def run(playwright: Playwright) -> None:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page= context.new_page()
        contact_us= ContactUsPage(page)
        contact_us.navigate()
        contact_us.submit_form("Ali", "123 UP", "test@gamil.com", "123456789", "test subject", "test message blah")


with sync_playwright() as playwright:
    run(playwright)
    time.sleep(5)
