# Page Object for the login page
from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.mobile_input = 'input[placeholder="Enter your number"]'
        self.password_input = 'input[placeholder="Enter your password"]'
        self.continue_button = 'button:has-text("Continue")'
        self.error_message = '.error-message, .MuiFormHelperText-root, .alert, .ant-form-explain'  # Add selectors for error messages if any

    def enter_mobile(self, mobile):
        self.page.fill(self.mobile_input, mobile)

    def click_continue(self):
        self.page.click(self.continue_button)

    def enter_password(self, password):
        self.page.fill(self.password_input, password)

    def is_logged_in(self):
        # Example: check for a dashboard element or user profile
        return self.page.is_visible('text=Dashboard') or self.page.is_visible('text=Profile')

    def is_error_displayed(self):
        # Returns True if any error message is visible
        return self.page.is_visible(self.error_message)

    def get_error_text(self):
        # Returns the error message text if present
        if self.page.is_visible(self.error_message):
            return self.page.inner_text(self.error_message)
        return None
