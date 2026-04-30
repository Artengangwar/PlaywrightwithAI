from manager.browser_manager import get_browser
from pages.main_page import MainPage
from pages.signup_page import SignupPage
from pages.choose_role_page import ChooseRolePage
from config.config import BASE_URL
from utils.report import log_step

def test_choose_role_parent_student():
    browser, playwright = get_browser()
    page = browser.new_page()
    main_page = MainPage(page)
    main_page.goto(BASE_URL)
    main_page.click_login_register()
    signup_page = SignupPage(page)
    signup_page.select_english()
    signup_page.click_continue()
    choose_role_page = ChooseRolePage(page)
    assert choose_role_page.is_heading_visible(), "Select User Type heading is not visible!"
    choose_role_page.select_parent_student()
    choose_role_page.click_continue()
    log_step("Parent/Student role selected and continued")
    page.wait_for_timeout(1000)
    browser.close()
    playwright.stop()

def test_choose_role_teacher():
    browser, playwright = get_browser()
    page = browser.new_page()
    main_page = MainPage(page)
    main_page.goto(BASE_URL)
    main_page.click_login_register()
    signup_page = SignupPage(page)
    signup_page.select_english()
    signup_page.click_continue()
    choose_role_page = ChooseRolePage(page)
    choose_role_page.select_teacher()
    choose_role_page.click_continue()
    log_step("Teacher role selected and continued")
    page.wait_for_timeout(1000)
    browser.close()
    playwright.stop()

