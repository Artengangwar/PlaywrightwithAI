# My Learning Assessment Test Project

This is a beginner-friendly automation testing project using **Playwright** and **pytest**.

## 📁 Project Folder Structure

```
D:\Netra\PythonProjectAI
├── pages/                    # Page Objects (every page has a class here)
│   ├── home_page.py         # Home page object
│   ├── home_page_new.py     # Updated home page object
│   └── login_page.py        # Login page object
├── tests/                    # Test files (your test scripts go here)
│   ├── test_home_pom.py     # Test for home page
│   └── test_login_flow.py   # Test for login flow
├── config/                   # Configuration files
│   └── config.py            # Settings like URL, browser, credentials
├── utils/                    # Helper functions (optional)
├── conftest.py              # Pytest configuration
├── pytest.ini               # Pytest settings
├── requirements.txt         # Python packages needed
└── README.md                # This file
```

## What Each Folder Does

### 📄 `pages/` - Page Objects
- Contains Python classes that represent each page of the website
- Each class has methods to interact with that page (click buttons, fill forms, etc.)
- Examples:
  - `home_page.py` → Methods like `open()`, `click_login_button()`
  - `login_page.py` → Methods like `enter_phone_number()`, `enter_password()`

### 🧪 `tests/` - Your Tests
- Contains test files (start with `test_`)
- Each test uses the page objects to test the website
- Examples:
  - `test_home_pom.py` → Tests the home page loads correctly
  - `test_login_flow.py` → Tests the complete login process

### ⚙️ `config/` - Configuration
- `config.py` → Settings that all tests use (URL, browser type, credentials)
- Change these values to customize your tests

### 🛠️ `utils/` - Helpers (Optional)
- For helper functions that multiple tests use
- Examples: login helper, screenshot helper, wait helper, etc.

## What This Project Tests

- **Home page**: Checks that the website opens correctly
- **Login flow**: Tests the complete login process (phone → password → continue)

## Files You Need to Know About

- `pages/home_page.py` - This is a helper class that opens the website and gets text from it
- `tests/test_home_pom.py` - This is the test that runs and checks the website

## How to Run the Test (Step by Step)

### Step 1: Open PowerShell

Press `Win + R` and type `powershell`. Press Enter.

### Step 2: Go to Your Project Folder

```powershell
Set-Location "D:\Netra\PythonProjectAI"
```

### Step 3: Create a Virtual Environment (Do This Once)

```powershell
python -m venv .venv
```

### Step 4: Activate the Virtual Environment

```powershell
.\.venv\Scripts\Activate.ps1
```

You should see `(.venv)` at the start of your command line after this.

### Step 5: Install the Required Packages

```powershell
pip install -r requirements.txt
```

### Step 6: Install Playwright Browsers (Do This Once)

```powershell
python -m playwright install
```

This downloads the Chrome browser that Playwright needs.

### Step 7: Run the Test

```powershell
pytest -q tests/test_home_pom.py
```

You should see a message saying the test passed!

## What Happens When You Run the Test

1. Playwright opens a Chrome browser (in the background, you won't see it)
2. The test opens the website: https://mla.rupantar.in
3. The test gets the page title and heading text
4. The test checks that the heading or title contains the word "Learning"
5. If everything is correct, the test passes ✓

## If the Test Fails

If you get an error, here are some things to check:

- **Error about packages**: Make sure you ran `pip install -r requirements.txt`
- **Error about Playwright**: Make sure you ran `python -m playwright install`
- **Error about "Learning" not found**: The website might have changed. Open https://mla.rupantar.in in your browser and check what text is on the page. Update the test to look for different text if needed.

## How to See What the Browser is Doing

If you want to see the browser window when the test runs (instead of it running in the background):

```powershell
# Set this to make tests run with the browser visible
setx PLAYWRIGHT_HEADLESS 0

# Then close PowerShell and open a new one, then run the test again
pytest -q tests/test_home_pom.py
```

## Change the Website URL or Text to Check

If you want to test a different website or look for different text:

1. Open `pages/home_page.py`
2. Change `self.url = "https://mla.rupantar.in"` to your website
3. Open `tests/test_home_pom.py`
4. Change `"Learning"` to the text you want to find on your website
5. Run the test again

## Quick Start - Run Tests Now!

### Option 1: Run just the login test (recommended)

```powershell
Set-Location "D:\Netra\PythonProjectAI"
.venv\Scripts\python.exe -m pytest -q tests/test_login_flow.py
```

### Option 2: Run all tests

```powershell
Set-Location "D:\Netra\PythonProjectAI"
.venv\Scripts\python.exe -m pytest -q tests/
```

### Option 3: Run with the browser visible

```powershell
$env:PLAYWRIGHT_HEADLESS = "0"
.venv\Scripts\python.exe -m pytest -q tests/test_login_flow.py
```

## Quick Reference Commands

```powershell
# Run home page test
pytest -q tests/test_home_pom.py

# Run login flow test
pytest -q tests/test_login_flow.py

# Run all tests
pytest -vv tests/

# Run with verbose output (see more details)
pytest -vv tests/test_login_flow.py

# Run and see browser window (after setting PLAYWRIGHT_HEADLESS=0)
pytest tests/test_login_flow.py
```

## How to Add More Tests

1. Create a new file in the `tests/` folder: `test_my_feature.py`
2. Import the page objects you need: `from pages.login_page import LoginPage`
3. Create a test function: `def test_my_feature(page):`
4. Use the page objects to interact with the website
5. Make assertions to check results
6. Run your test: `pytest -q tests/test_my_feature.py`

## How to Add More Page Objects

If the website has more pages (like a dashboard, profile, etc.):

1. Create a new file in `pages/`: `dashboard_page.py`
2. Define a class with methods for interactions:
   ```python
   class DashboardPage:
       def __init__(self, page):
           self.page = page
       
       def click_my_courses(self):
           self.page.get_by_role("link", name="My Courses").click()
   ```
3. Use it in your tests: `dashboard = DashboardPage(page)`

## Still Have Questions?

If something doesn't work:
1. Make sure you're in the project folder: `D:\Netra\PythonProjectAI`
2. Make sure the virtual environment is activated (you see `(.venv)` in your PowerShell)
3. Check that all packages installed: `pip list` (should show pytest, playwright, etc.)
4. Check the browser is visible: Set `PLAYWRIGHT_HEADLESS=0` to debug
5. Check the config: Open `config/config.py` and verify the URL and credentials are correct

