# Home page - First page when you visit the website


class HomePage:
    def __init__(self, page):
        self.page = page
        self.url = "https://mla.rupantar.in/"
    
    def open(self):
        """Open the home page"""
        self.page.goto(self.url)
    
    def click_login_button(self):
        """Click the Login/Register button"""
        self.page.get_by_role("button", name="Login/Register").click()
    
    def get_title(self):
        """Get the page title"""
        try:
            return self.page.title()
        except Exception:
            return ""

