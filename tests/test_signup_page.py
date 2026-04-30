from manager.browser_manager import get_browser
from pages.main_page import MainPage
from pages.signup_page import SignupPage
from config.config import BASE_URL
from utils.report import log_step

def test_signup_language_selection():
    browser, playwright = get_browser()
    page = browser.new_page()
    main_page = MainPage(page)
    main_page.goto(BASE_URL)
    main_page.click_login_register()
    signup_page = SignupPage(page)
    assert signup_page.is_heading_visible(), "Choose Your Language heading is not visible!"
    signup_page.select_english()
    signup_page.click_continue()
    log_step("Language selected and continued")
    page.wait_for_timeout(1000)
    browser.close()
    playwright.stop()

