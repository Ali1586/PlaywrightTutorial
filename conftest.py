import playwright
import pytest
from playwright.sync_api import Playwright
import pytest

@pytest.fixture(scope="function")
def set_up(browser) :
    #browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)

    yield page


@pytest.fixture(scope="function")
def login_set_up(set_up) :
   # browser = playwright.chromium.launch(headless=False, slow_mo=500)
    #context = browser.new_context()
    #page = context.new_page()
    #page.goto("https://symonstorozhenko.wixsite.com/website-1")
    #page.set_default_timeout(3000)


    yield page
