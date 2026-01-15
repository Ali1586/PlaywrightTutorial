import utils.secret_config
import time

import playwright
import pytest
from playwright.sync_api import Playwright
import pytest



@pytest.fixture(scope="session")
def set_up(browser):
        #browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(10000)

    yield page
    page.close()


@pytest.fixture(scope="session")
def login_set_up(set_up):

    page=set_up
    # page.goto("")
    #page.set_default_timeout(5000)
    login_issue = True
    while login_issue:
        if not page.is_visible("[data-testid=\"signUp.switchToSignUp\"]"):
            page.click("button:has-text(\"Log In\")")
        else:
            login_issue = False
        time.sleep(0.1)
    page.click("[data-testid=\"signUp.switchToSignUp\"]", timeout=2000)
    # page.click(":nth-match(:text('Log In'), 2)", timeout=2000)
    page.click("[data-testid='switchToEmailLink'] >> [data-testid='buttonElement']")
    # page.click("[data-testid='siteMembers.container'] input[type='email']")
    # page.fill("[data-testid='siteMembers.container'] input[type='email']", "symon.storozhenko@gmail.com")
    page.fill('input:below(:text("Email"))', "Keepitnice1990@gmail.com")
    page.press("[data-testid='siteMembers.container'] >> input[type='email']", "Tab")
    page.fill("input[type='password']", utils.secret_config.PASSWORD)
    page.click("[data-testid='submit'] >> [data-testid='buttonElement']")

    yield page


@pytest.fixture(scope="function")
def go_to_new_collections_page(set_up) :
    #browser = playwright.chromium.launch(headless=False, slow_mo=500)
    #context = browser.new_context()
    #page = context.new_page()
    page= set_up
    page.goto("/new-collection")
    page.set_default_timeout(3000)

    yield page



