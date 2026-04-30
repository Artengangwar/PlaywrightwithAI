# pages Object for the signup (language selection) page
from playwright.sync_api import Page

class SignupPage:
    def __init__(self, page: Page):
        self.page = page
        self.heading = 'text=Choose Your Language'
        self.english_option = 'text=English'
        self.continue_button = 'text=Continue'

    def is_heading_visible(self):
        return self.page.is_visible(self.heading)

    def select_english(self):
        self.page.click(self.english_option)

    def click_continue(self):
        self.page.click(self.continue_button)

