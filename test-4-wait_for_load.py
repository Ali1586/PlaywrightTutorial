import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.get_by_test_id("handle-button").click()
    page.get_by_test_id("signUp.switchToSignUp").click()
    page.get_by_test_id("siteMembersDialogLayout").press("Tab")
    page.get_by_test_id("switchToSignUp").press("Tab")
    page.get_by_test_id("googlenew").get_by_test_id("buttonElement").press("Tab")
    page.get_by_test_id("fbnew").get_by_test_id("buttonElement").press("Tab")
    page.get_by_role("button", name="Log in with Email").press("Tab")


    page.get_by_test_id("xButton").press("Tab")
    page.wait_for_selector("name=Log in with Email")
    assert page.is_visible("name=Log in with Email")
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
