# Multiple test cases for login flow
# Each test focuses on ONE specific task

from pages.home_page import HomePage
from pages.login_page import LoginPage
from config.config import Config
from playwright.sync_api import expect


# ============================================================================
# Helper functions
# ============================================================================
def _open_home(page):
    home = HomePage(page)
    home.open()
    page.wait_for_load_state("networkidle")
    return home


def _open_and_start_login(page):
    """Open home page and click Login/Register, return LoginPage."""
    home = _open_home(page)
    home.click_login_button()
    return LoginPage(page)


# ============================================================================
# TEST 1: Home Page Loading
# ============================================================================
def test_home_page_loads(page):
    """Test that home page loads successfully.

    Use Config.APP_URL and a relaxed check so the test is not brittle
    if the site redirects or changes trailing slashes.
    """
    home = _open_home(page)
    # Additional wait to ensure page is fully interactive
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_timeout(1000)

    # Verify we're on the home page (use startswith for robustness)
    assert page.url.startswith(Config.APP_URL), f"Failed to load home page: {page.url}"
    
    # Wait for main content to be visible
    expect(page.get_by_role("button", name="Login/Register")).to_be_visible(timeout=5000)
    print("✓ Test 1 PASSED: Home page loads successfully")


# ============================================================================
# TEST 2: Login Button is Visible and Clickable
# ============================================================================
def test_login_button_visible(page):
    """Test that Login/Register button is visible and clickable.

    Instead of relying on navigation, verify that clicking shows the next
    UI element (Continue button) which proves the flow progressed.
    """
    _open_home(page)
    page.wait_for_timeout(500)

    btn = page.get_by_role("button", name="Login/Register")
    expect(btn).to_be_visible(timeout=5000)
    page.wait_for_timeout(300)
    
    btn.click()
    page.wait_for_load_state("networkidle")
    page.wait_for_timeout(500)

    # After click, the Continue button should appear in the flow
    continue_btn = page.get_by_role("button", name="Continue")
    expect(continue_btn).to_be_visible(timeout=5000)
    page.wait_for_timeout(300)
    print("✓ Test 2 PASSED: Login button is visible and works")


# ============================================================================
# TEST 3: User Type Selection (Parent/Student)
# ============================================================================
def test_user_type_selection(page):
    """Test that we can select Parent/Student user type"""
    login = _open_and_start_login(page)
    page.wait_for_load_state("networkidle")
    
    # navigate through initial screens
    login.click_header_container()
    page.wait_for_timeout(500)
    
    login.click_main()
    page.wait_for_timeout(500)
    
    login.click_continue()
    page.wait_for_timeout(500)

    # Click Parent/Student button and ensure it is clickable
    btn = page.get_by_role("button", name="Parent/Student")
    expect(btn).to_be_visible(timeout=5000)
    btn.click()
    page.wait_for_timeout(500)
    print("✓ Test 3 PASSED: Parent/Student selection works")


# ============================================================================
# TEST 4: Phone Number Entry
# ============================================================================
def test_phone_number_entry(page):
    """Test that we can enter a phone number"""
    login = _open_and_start_login(page)
    page.wait_for_load_state("networkidle")
    
    login.click_header_container()
    page.wait_for_timeout(500)
    
    login.click_main()
    page.wait_for_timeout(500)
    
    login.click_continue()
    page.wait_for_timeout(500)
    
    login.click_parent_student()
    page.wait_for_timeout(500)
    
    login.click_continue()
    page.wait_for_timeout(500)
    
    # Wait for phone textbox to be visible before entering number
    phone_input = page.get_by_role("textbox", name="Enter your number")
    expect(phone_input).to_be_visible(timeout=5000)

    # Enter phone number and verify the textbox value
    login.enter_phone_number("9650167989")
    page.wait_for_timeout(500)
    
    phone = page.get_by_role("textbox", name="Enter your number")
    expect(phone).to_have_value("9650167989", timeout=5000)
    print("✓ Test 4 PASSED: Phone number entered successfully")


# ============================================================================
# TEST 5: Password Entry
# ============================================================================
def test_password_entry(page):
    """Test that we can enter a password"""
    login = _open_and_start_login(page)
    page.wait_for_load_state("networkidle")
    
    login.click_header_container()
    page.wait_for_timeout(500)
    
    login.click_main()
    page.wait_for_timeout(500)
    
    login.click_continue()
    page.wait_for_timeout(500)
    
    login.click_parent_student()
    page.wait_for_timeout(500)
    
    login.click_continue()
    page.wait_for_timeout(500)
    
    # Wait for phone textbox and enter phone number
    phone_input = page.get_by_role("textbox", name="Enter your number")
    expect(phone_input).to_be_visible(timeout=5000)
    login.enter_phone_number("9650167989")
    page.wait_for_timeout(500)
    
    login.click_continue()
    page.wait_for_timeout(500)
    
    # Wait for password textbox to be visible before entering password
    pwd_input = page.get_by_role("textbox", name="Enter Password")
    expect(pwd_input).to_be_visible(timeout=5000)

    # Enter password and verify field is filled
    login.enter_password("Password@123")
    page.wait_for_timeout(500)
    
    pwd = page.get_by_role("textbox", name="Enter Password")
    expect(pwd).to_have_value("Password@123", timeout=5000)
    print("✓ Test 5 PASSED: Password entered successfully")


# ============================================================================
# TEST 6: Complete Login Flow (All Steps Together)
# ============================================================================
def test_complete_login_flow(page):
    """Test the COMPLETE login process from start to finish"""
    # Step 1: Open home page and start login
    home = HomePage(page)
    home.open()
    page.wait_for_load_state("networkidle")
    print("  ✓ Home page opened")

    # Wait for login button to be visible before clicking
    login_btn = page.get_by_role("button", name="Login/Register")
    expect(login_btn).to_be_visible(timeout=5000)
    home.click_login_button()
    page.wait_for_load_state("networkidle")
    print("  ✓ Login/Register button clicked")

    login = LoginPage(page)
    
    login.click_header_container()
    page.wait_for_timeout(500)
    
    login.click_main()
    page.wait_for_timeout(500)
    
    login.click_continue()
    page.wait_for_timeout(500)
    
    # Wait for Parent/Student button before clicking
    parent_btn = page.get_by_role("button", name="Parent/Student")
    expect(parent_btn).to_be_visible(timeout=5000)
    login.click_parent_student()
    page.wait_for_timeout(500)
    
    login.click_continue()
    page.wait_for_timeout(500)

    # Wait for phone textbox before entering phone number
    phone_input = page.get_by_role("textbox", name="Enter your number")
    expect(phone_input).to_be_visible(timeout=5000)
    login.enter_phone_number("9650167989")
    page.wait_for_timeout(500)
    
    login.click_continue()
    page.wait_for_timeout(500)
    
    # Wait for password textbox before entering password
    pwd_input = page.get_by_role("textbox", name="Enter Password")
    expect(pwd_input).to_be_visible(timeout=5000)
    login.enter_password("Password@123")
    page.wait_for_timeout(500)
    
    login.click_continue()
    page.wait_for_load_state("networkidle")

    # Verify login was successful by checking URL changed from app URL
    assert not page.url.startswith(Config.APP_URL), "Login failed - still on home page"
    print("✓ Test 6 PASSED: Complete login flow successful!")




