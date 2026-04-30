import pytest
from playwright.async_api import async_playwright
from config.config import BASE_URL
from config.credentials import PARENT_MOBILE, PARENT_PASSWORD

VALID_PASSWORD = "Password@123"
INVALID_PASSWORD = "1234566"
BLANK_PASSWORD = ""
BLANK_MOBILE = ""

async def setup_login_page(page):
    await page.goto(BASE_URL)
    await page.click('text=Login/Register')
    await page.click('text=English')
    await page.click('text=Continue')
    await page.click('text=Parent/Student')
    await page.click('text=Continue')

@pytest.mark.asyncio
async def test_valid_password():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await setup_login_page(page)
        await page.fill('input[placeholder="Enter your number"]', PARENT_MOBILE)
        await page.click('button:has-text("Continue")')
        if await page.is_visible('input[placeholder="Enter your password"]'):
            await page.fill('input[placeholder="Enter your password"]', VALID_PASSWORD)
            await page.click('button:has-text("Continue")')
        assert await page.is_visible('text=Dashboard') or await page.is_visible('text=Profile'), "Login failed with valid password!"
        await page.wait_for_timeout(2000)
        await page.close()
        await browser.close()

@pytest.mark.asyncio
async def test_invalid_password():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await setup_login_page(page)
        await page.fill('input[placeholder="Enter your number"]', PARENT_MOBILE)
        await page.click('button:has-text("Continue")')
        if await page.is_visible('input[placeholder="Enter your password"]'):
            await page.fill('input[placeholder="Enter your password"]', INVALID_PASSWORD)
            await page.click('button:has-text("Continue")')
        assert not (await page.is_visible('text=Dashboard') or await page.is_visible('text=Profile')), "Login succeeded with invalid password!"
        await page.wait_for_timeout(2000)
        await page.close()
        await browser.close()

@pytest.mark.asyncio
async def test_blank_password():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await setup_login_page(page)
        await page.fill('input[placeholder="Enter your number"]', PARENT_MOBILE)
        await page.click('button:has-text("Continue")')
        if await page.is_visible('input[placeholder="Enter your password"]'):
            await page.fill('input[placeholder="Enter your password"]', BLANK_PASSWORD)
            await page.click('button:has-text("Continue")')
        assert not (await page.is_visible('text=Dashboard') or await page.is_visible('text=Profile')), "Login succeeded with blank password!"
        await page.wait_for_timeout(2000)
        await page.close()
        await browser.close()

@pytest.mark.asyncio
async def test_blank_username_and_password():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await setup_login_page(page)
        await page.fill('input[placeholder="Enter your number"]', BLANK_MOBILE)
        await page.click('button:has-text("Continue")')
        if await page.is_visible('input[placeholder="Enter your password"]'):
            await page.fill('input[placeholder="Enter your password"]', BLANK_PASSWORD)
            await page.click('button:has-text("Continue")')
        assert not (await page.is_visible('text=Dashboard') or await page.is_visible('text=Profile')), "Login succeeded with blank username and password!"
        await page.wait_for_timeout(2000)
        await page.close()
        await browser.close()

