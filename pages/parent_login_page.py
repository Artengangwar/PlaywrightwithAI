import re
from playwright.sync_api import Page

class ParentLoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.login_register_btn = 'button:has-text("Login/Register")'
        self.english_option = "div:has-text('English')"
        self.continue_btn = 'button:has-text("Continue")'
        self.parent_student_btn = 'button:has-text("Parent/Student")'
        self.mobile_input = 'input[placeholder="Enter your number"]'
        self.password_input = 'input[placeholder="Enter Password"]'
        self.eye_icon = '.styles_eye-icon__GJmGS > path'

    def goto(self, url):
        self.page.goto(url)

    def login_flow(self, mobile, password):
        self.page.click(self.login_register_btn)
        # English option: use nth(1) to match your script
        self.page.locator(self.english_option).nth(1).click()
        self.page.click(self.continue_btn)
        self.page.click(self.parent_student_btn)
        self.page.click(self.continue_btn)
        self.page.click(self.mobile_input)
        self.page.fill(self.mobile_input, mobile)
        self.page.click(self.continue_btn)
        self.page.fill(self.password_input, password)
        self.page.click(self.continue_btn)

    def toggle_password_eye(self):
        self.page.locator(self.eye_icon).click()

    def clear_and_fill_password(self, password):
        self.page.click(self.password_input)
        for _ in range(9):
            self.page.press(self.password_input, "ArrowLeft")
        self.page.fill(self.password_input, password)
        self.page.click(self.continue_btn)

    def is_login_successful(self):
        # You can update this selector to match a dashboard/profile element
        return self.page.is_visible('text=Dashboard') or self.page.is_visible('text=Profile')

    def is_error_displayed(self):
        return self.page.is_visible('.error-message, .MuiFormHelperText-root, .alert, .ant-form-explain')

