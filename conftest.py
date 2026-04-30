# Pytest fixtures for Playwright POM framework
import pytest
from manager.browser_manager import get_browser

@pytest.fixture(scope='session')
def browser():
    browser, playwright = get_browser()
    yield browser
    browser.close()
    playwright.stop()

@pytest.fixture
def page(browser):
    page = browser.new_page()
    yield page
    page.close()
