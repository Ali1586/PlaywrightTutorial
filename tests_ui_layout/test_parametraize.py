import time

import pytest
from playwright.sync_api import Playwright, sync_playwright, expect


@pytest.mark.parametrize("email", ["Keepitnice1990@gmail.com",
                                             pytest.param("fakeemail", marks=pytest.mark.xfail),
                                             pytest.param("Keepitnice1990@gmail", marks=pytest.mark.xfail)])
@pytest.mark.parametrize("password", ["Asdfg12345!",
                                             pytest.param("fakepassword", marks=pytest.mark.xfail),
                                             "Asdfg12345!"])
def test_login_para(page, email, password) -> None:
        #browser = playwright.chromium.launch(headless=False, slow_mo=1000)
        #context = browser.new_context()
        #page= login_set_up
        #page = context.new_page()
        page.goto("https://symonstorozhenko.wixsite.com/website-1")
        page.set_default_timeout(2000)
        login_issue = True
        while login_issue:
            if not page.is_visible("[data-testid=\"signUp.switchToSignUp\"]"):
                page.click("button:has-text(\"Log In\")")
            else:
                login_issue = False
            time.sleep(0.1)
      #  page.get_by_test_id("handle-button").click()
       # page.get_by_test_id("signUp.switchToSignUp").click(timeout=2000)
       # page.wait_for_selector('[data-testid="signUp.switchToSignUp"]', timeout=10000)

        #page.get_by_test_id("emailAuth").get_by_role("textbox", name="Email").fill("Keepitnice1990@")
        #page.get_by_test_id("emailAuth").get_by_role("textbox", name="Email").press("ArrowRight")
        #page.get_by_test_id("emailAuth").get_by_role("textbox", name="Email").fill("Keepitnice1990@gmail")
        #page.get_by_role("textbox", name="Password").click()
        #page.get_by_role("textbox", name="Password").fill("Asdfg12345")
        #page.get_by_role("textbox", name="Password").press("CapsLock")
        #page.get_by_role("textbox", name="Password").fill("Asdfg123451")
        #page.get_by_test_id("emailAuth").get_by_role("textbox", name="Email").click()
        #page.get_by_test_id("emailAuth").get_by_role("textbox", name="Email").press("ArrowRight")
        #page.get_by_test_id("emailAuth").get_by_role("textbox", name="Email").press("ArrowRight")
        #page.get_by_test_id("emailAuth").get_by_role("textbox", name="Email").fill("Keepitnice1990@gmail.com")
        #page.get_by_test_id("submit").get_by_test_id("buttonElement").click()
        #page.get_by_role("textbox", name="Password").click()
        #page.get_by_role("textbox", name="Password").dblclick()
        #page.get_by_role("textbox", name="Password").fill("Asdfg12345!")
        #page.get_by_test_id("submit").get_by_test_id("buttonElement").click()
        page.click("[data-testid=\"signUp.switchToSignUp\"]", timeout=2000)
        # page.click(":nth-match(:text('Log In'), 2)", timeout=2000)
        page.click("[data-testid='switchToEmailLink'] >> [data-testid='buttonElement']")
        # page.click("[data-testid='siteMembers.container'] input[type='email']")
        # page.fill("[data-testid='siteMembers.container'] input[type='email']", "symon.storozhenko@gmail.com")
        page.fill('input:below(:text("Email"))', email)
        page.press("[data-testid='siteMembers.container'] >> input[type='email']", "Tab")
        page.fill("input[type='password']", password)
        page.click("[data-testid='submit'] >> [data-testid='buttonElement']")
        page.wait_for_load_state()
        page.expect_navigation(url="https://symonstorozhenko.wixsite.com/website-1",
                               wait_until="domcontentloaded",
                               timeout=5000)
        page.wait_for_selector("[aria-label=\"symon.storozhenkoaccount menu\"]")
        assert not page.is_visible("text=Log In")