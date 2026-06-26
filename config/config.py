# Configuration for all tests
# Change these values to customize test behavior


class Config:
    # The website we are testing
    APP_URL = "https://mla.rupantar.in/"
    
    # Browser type: "chromium", "firefox", or "webkit"
    BROWSER = "chromium"
    
    # Run browser in headless mode (True = hidden, False = visible window)
    # Set to False to see the browser UI for debugging
    HEADLESS = True
    
    # How long to wait for elements before timing out (in milliseconds)
    TIMEOUT = 5000
    
    # Test credentials (ONLY for testing - never use real credentials in code!)
    TEST_PHONE = "9650167989"
    TEST_PASSWORD = "Password@123"



