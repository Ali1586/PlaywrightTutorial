import re
from playwright.sync_api import Playwright, sync_playwright, expect
import pytest

@pytest.mark.smoke
@pytest.mark.regression
def test_logged_user_can_view_my_orders_menu(login_set_up):
   # browser = playwright.chromium.launch(headless=False, slow_mo=2000)
    #context = browser.new_context()
    #page.goto("https://symonstorozhenko.wixsite.com/website-1")
    #page.set_default_timeout(12000)
    #page.get_by_test_id("handle-button").click()
    #page.get_by_test_id("signUp.switchToSignUp").click()
    #page.get_by_role("button", name="Log in with Email").click()
    #page.get_by_test_id("emailAuth").get_by_role("textbox", name="Email").fill("https://symonstorozhenko.wixsite.com/website-1%20@")
    #page.get_by_test_id("emailAuth").get_by_role("textbox", name="Email").press("ArrowLeft")
    #page.get_by_test_id("emailAuth").get_by_role("textbox", name="Email").fill("keepitnice1990@")
    #page.get_by_test_id("emailAuth").get_by_role("textbox", name="Email").press("ArrowRight")
    #page.get_by_test_id("emailAuth").get_by_role("textbox", name="Email").fill("keepitnice1990@gamil.com")
    #page.get_by_role("textbox", name="Password").click()
    #page.get_by_role("textbox", name="Password").fill("Asdfg12345!")
    #page.get_by_test_id("submit").get_by_test_id("buttonElement").click()
    #page.get_by_role("textbox", name="Password").dblclick()
    #page.get_by_role("textbox", name="Password").fill("Asdfg12345!")
    #page.get_by_test_id("emailAuth").get_by_role("textbox", name="Email").click()
    #page.get_by_test_id("emailAuth").get_by_role("textbox", name="Email").fill("keepitnice1990@gmail.com")
    #page.get_by_test_id("submit").get_by_test_id("buttonElement").click()
    page=login_set_up
    assert page.is_visiable("text=Contact Us")

    # ---------------------
    #context.close()
    #browser.close()


#with sync_playwright() as playwright:
 #   run(playwright)
