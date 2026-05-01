import pytest
from playwright.sync_api import sync_playwright
from config.config import BASE_URL
from config.credentials import PARENT_MOBILE, PARENT_PASSWORD
from pages.parent_login_page import ParentLoginPage

def test_parent_login_valid():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        parent_login = ParentLoginPage(page)
        parent_login.goto(BASE_URL)
        parent_login.login_flow(PARENT_MOBILE, PARENT_PASSWORD)
        assert parent_login.is_login_successful(), "Valid login failed!"
        page.close()
        browser.close()

def test_parent_login_invalid():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        parent_login = ParentLoginPage(page)
        parent_login.goto(BASE_URL)
        parent_login.login_flow(PARENT_MOBILE, "wrongpassword")
        assert parent_login.is_error_displayed(), "Error not displayed for invalid password!"
        page.close()
        browser.close()

def test_parent_login_blank():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        parent_login = ParentLoginPage(page)
        parent_login.goto(BASE_URL)
        parent_login.login_flow("", "")
        assert parent_login.is_error_displayed(), "Error not displayed for blank credentials!"
        page.close()
        browser.close()

