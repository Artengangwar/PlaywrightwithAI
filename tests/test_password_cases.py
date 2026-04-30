from manager.browser_manager import get_browser
from pages.main_page import MainPage
from pages.signup_page import SignupPage
from pages.choose_role_page import ChooseRolePage
from pages.login_page import LoginPage
from config.config import BASE_URL
from config.credentials import PARENT_MOBILE, PARENT_PASSWORD
from utils.report import log_step

VALID_PASSWORD = "Password@123"
INVALID_PASSWORD = "1234566"
BLANK_PASSWORD = ""
BLANK_MOBILE = ""


def setup_login_page():
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
    return browser, playwright, page, login_page


def test_valid_password():
    browser, playwright, page, login_page = setup_login_page()
    login_page.enter_mobile(PARENT_MOBILE)
    login_page.click_continue()
    if page.is_visible(login_page.password_input):
        login_page.enter_password(VALID_PASSWORD)
        login_page.click_continue()
    assert login_page.is_logged_in(), "Login failed with valid password!"
    log_step("Valid password login successful")
    page.wait_for_timeout(2000)
    page.close()
    browser.close()
    playwright.stop()


def test_invalid_password():
    browser, playwright, page, login_page = setup_login_page()
    login_page.enter_mobile(PARENT_MOBILE)
    login_page.click_continue()
    if page.is_visible(login_page.password_input):
        login_page.enter_password(INVALID_PASSWORD)
        login_page.click_continue()
    assert not login_page.is_logged_in(), "Login succeeded with invalid password!"
    log_step("Invalid password login failed as expected")
    page.wait_for_timeout(2000)
    page.close()
    browser.close()
    playwright.stop()


def test_blank_password():
    browser, playwright, page, login_page = setup_login_page()
    login_page.enter_mobile(PARENT_MOBILE)
    login_page.click_continue()
    if page.is_visible(login_page.password_input):
        login_page.enter_password(BLANK_PASSWORD)
        login_page.click_continue()
    assert not login_page.is_logged_in(), "Login succeeded with blank password!"
    log_step("Blank password login failed as expected")
    page.wait_for_timeout(2000)
    page.close()
    browser.close()
    playwright.stop()


def test_blank_username_and_password():
    browser, playwright, page, login_page = setup_login_page()
    login_page.enter_mobile(BLANK_MOBILE)
    login_page.click_continue()
    if page.is_visible(login_page.password_input):
        login_page.enter_password(BLANK_PASSWORD)
        login_page.click_continue()
    assert not login_page.is_logged_in(), "Login succeeded with blank username and password!"
    log_step("Blank username and password login failed as expected")
    page.wait_for_timeout(2000)
    page.close()
    browser.close()
    playwright.stop()

