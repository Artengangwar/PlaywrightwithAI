# pages Object for the choose role (user type) page
from playwright.sync_api import Page

class ChooseRolePage:
    def __init__(self, page: Page):
        self.page = page
        self.heading = 'text=Select User Type'
        self.teacher_radio = 'text=Teacher'
        self.parent_student_radio = 'text=Parent/Student'
        self.continue_button = 'text=Continue'

    def is_heading_visible(self):
        return self.page.is_visible(self.heading)

    def select_teacher(self):
        self.page.click(self.teacher_radio)

    def select_parent_student(self):
        self.page.click(self.parent_student_radio)

    def click_continue(self):
        self.page.click(self.continue_button)

