# Login page - Used during the login/registration process


class LoginPage:
	def __init__(self, page):
		self.page = page
    
	def click_header_container(self):
		"""Click the header container (if needed)"""
		self.page.locator(".styles_header-container__Dv7Ye").click()
    
	def click_main(self):
		"""Click the main area"""
		self.page.get_by_role("main").click()
    
	def click_continue(self):
		"""Click Continue button"""
		self.page.get_by_role("button", name="Continue").click()
    
	def click_parent_student(self):
		"""Click Parent/Student button"""
		self.page.get_by_role("button", name="Parent/Student").click()
    
	def enter_phone_number(self, phone_number):
		"""Enter phone number in the textbox"""
		self.page.get_by_role("textbox", name="Enter your number").click()
		self.page.get_by_role("textbox", name="Enter your number").fill(phone_number)
    
	def enter_password(self, password):
		"""Enter password in the textbox"""
		self.page.get_by_role("textbox", name="Enter Password").click()
		self.page.get_by_role("textbox", name="Enter Password").fill(password)


