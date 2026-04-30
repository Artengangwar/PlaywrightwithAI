from manager.browser_manager import get_browser
from pages.main_page import MainPage
from pages.signup_page import SignupPage
from pages.choose_role_page import ChooseRolePage
from config.config import BASE_URL
from utils.report import log_step

def test_login_page_elements_after_parent_student():
    browser, playwright = get_browser()
    page = browser.new_page()
    main_page = MainPage(page)
    main_page.goto(BASE_URL)
    main_page.click_login_register()
    signup_page = SignupPage(page)
    signup_page.select_english()
    signup_page.click_continue()
    choose_role_page = ChooseRolePage(page)
    choose_role_page.select_parent_student()
    choose_role_page.click_continue()
    assert page.is_visible('text=Welcome!'), "Welcome heading not visible on login page!"
    assert page.is_visible('input[placeholder="Enter your number"]'), "Mobile number input not visible!"
    log_step("Login page loaded and verified")
    page.wait_for_timeout(2000)
    page.close()
    browser.close()
    playwright.stop()
