# pages Object for the main page
from playwright.sync_api import Page

class MainPage:
    def __init__(self, page: Page):
        self.page = page
        self.login_register_button = 'text=Login/Register'
        self.main_heading = 'text=The First Learning Assessment'

    def goto(self, url):
        self.page.goto(url)

    def click_login_register(self):
        self.page.click(self.login_register_button)

    def is_main_heading_visible(self):
        return self.page.is_visible(self.main_heading)
