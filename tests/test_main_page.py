from manager.browser_manager import get_browser
from pages.main_page import MainPage
from config.config import BASE_URL
from utils.report import log_step

def test_main_page_heading_and_login_button():
    browser, playwright = get_browser()
    page = browser.new_page()
    main_page = MainPage(page)
    log_step(f"Opening {BASE_URL}")
    main_page.goto(BASE_URL)
    assert main_page.is_main_heading_visible(), "Main heading is not visible!"
    log_step("Main heading is visible")
    main_page.click_login_register()
    log_step("Clicked Login/Register button")
    page.wait_for_timeout(1000)
    browser.close()
    playwright.stop()

