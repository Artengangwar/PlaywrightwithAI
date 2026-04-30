# Test cases for the signup flow: home -> language -> role -> login
from manager.browser_manager import get_browser
from pages.main_page import MainPage
from pages.signup_page import SignupPage
from pages.choose_role_page import ChooseRolePage
from config.config import BASE_URL
from utils.report import log_step


def test_signup_parent_student_flow():
    browser, playwright = get_browser()
    page = browser.new_page()
    main_page = MainPage(page)
    log_step(f"Opening {BASE_URL}")
    main_page.goto(BASE_URL)
    assert main_page.is_main_heading_visible(), "Main heading is not visible!"
    log_step("Main heading is visible")
    main_page.click_login_register()
    log_step("Clicked Login/Register button")
    signup_page = SignupPage(page)
    assert signup_page.is_heading_visible(), "Choose Your Language heading is not visible!"
    log_step("Choose Your Language heading is visible")
    signup_page.select_english()
    log_step("Selected English language")
    signup_page.click_continue()
    log_step("Clicked Continue button on language selection")
    choose_role_page = ChooseRolePage(page)
    assert choose_role_page.is_heading_visible(), "Select User Type heading is not visible!"
    log_step("Select User Type heading is visible")
    choose_role_page.select_parent_student()
    log_step("Selected Parent/Student role")
    choose_role_page.click_continue()
    log_step("Clicked Continue button on role selection")
    # Assert login page elements
    assert page.is_visible('text=Welcome!'), "Welcome heading not visible on login page!"
    assert page.is_visible('input[placeholder="Enter your number"]'), "Mobile number input not visible!"
    log_step("Login page loaded and verified")
    page.wait_for_timeout(2000)
    browser.close()
    playwright.stop()


def test_signup_teacher_flow():
    browser, playwright = get_browser()
    page = browser.new_page()
    main_page = MainPage(page)
    log_step(f"Opening {BASE_URL}")
    main_page.goto(BASE_URL)
    assert main_page.is_main_heading_visible(), "Main heading is not visible!"
    log_step("Main heading is visible")
    main_page.click_login_register()
    log_step("Clicked Login/Register button")
    signup_page = SignupPage(page)
    assert signup_page.is_heading_visible(), "Choose Your Language heading is not visible!"
    log_step("Choose Your Language heading is visible")
    signup_page.select_english()
    log_step("Selected English language")
    signup_page.click_continue()
    log_step("Clicked Continue button on language selection")
    choose_role_page = ChooseRolePage(page)
    assert choose_role_page.is_heading_visible(), "Select User Type heading is not visible!"
    log_step("Select User Type heading is visible")
    choose_role_page.select_teacher()
    log_step("Selected Teacher role")
    choose_role_page.click_continue()
    log_step("Clicked Continue button on role selection")
    # Assert login page elements
    assert page.is_visible('text=Welcome!'), "Welcome heading not visible on login page!"
    assert page.is_visible('input[placeholder="Enter your number"]'), "Mobile number input not visible!"
    log_step("Login page loaded and verified")
    page.wait_for_timeout(2000)
    browser.close()
    playwright.stop()
