from pom.home_page_elements import HomePage
from playwright.sync_api import Playwright, sync_playwright, expect
import pytest

@pytest.mark.integration
#@pytest.mark.regression
def test_run_b(login_set_up) -> None:
   # browser = playwright.chromium.launch(headless=False, slow_mo=500)
    #context = browser.new_context()
    #page = context.new_page()
    #page.goto("https://symonstorozhenko.wixsite.com/website-1")
    #page.set_default_timeout(3000)
    page = login_set_up
    #   home_page=HomePage()

    assert page.is_visible(HomePage.celebrate_beauty_header)
    assert page.is_visible(HomePage.celebrate_beauty_body)


    #expect(home_page.celebrate_beauty_header).to_be_visible()
    #expect(home_page.celebrate_beauty_body).to_be_visible()

#    context.close()
 #   browser.close()



#with sync_playwright() as playwright:
 #   run_b(playwright)

@pytest.mark.regression
def test_run_b_2(login_set_up) -> None:
   # browser = playwright.chromium.launch(headless=False, slow_mo=500)
    #context = browser.new_context()
    #page = context.new_page()
    #page.goto("https://symonstorozhenko.wixsite.com/website-1")
    #page.set_default_timeout(3000)
    page =login_set_up

    # home_page=HomePage()
#    assert page.is_visible("text=Shop")
    assert page.is_visible(HomePage.celebrate_beauty_header)
    assert page.is_visible(HomePage.celebrate_beauty_body)

    # expect(home_page.celebrate_beauty_header).to_be_visible()
    # expect(home_page.celebrate_beauty_body).to_be_visible()

    #context.close()
    #browser.close()

# with sync_playwright() as playwright:
#   run_b(playwright)