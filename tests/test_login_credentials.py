from manager.browser_manager import get_browser
from pages.main_page import MainPage
from pages.signup_page import SignupPage
from pages.choose_role_page import ChooseRolePage
from pages.login_page import LoginPage
from config.config import BASE_URL
from config.credentials import PARENT_MOBILE, PARENT_PASSWORD
from utils.report import log_step

def test_parent_login_flow():
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
    login_page = LoginPage(page)
    login_page.enter_mobile(PARENT_MOBILE)
    login_page.click_continue()
    # If password is required on next step, fill it
    if page.is_visible(login_page.password_input):
        login_page.enter_password(PARENT_PASSWORD)
        login_page.click_continue()
    # Assert login success (customize selector as needed)
    assert login_page.is_logged_in(), "Login failed or dashboard/profile not visible!"
    log_step("Parent login flow completed and verified")
    page.wait_for_timeout(2000)
    page.close()
    browser.close()
    playwright.stop()

