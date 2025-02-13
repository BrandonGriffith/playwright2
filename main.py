"""
Web Automation Script using Playwright
This script automates browser interactions across multiple websites using saved cookies for authentication.
It performs a series of clicks and navigations with appropriate wait times between actions.
"""

import os
import time
import json
import re
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

# Load environment variables from a .env file for secure configuration
load_dotenv()

# Retrieve configuration from environment variables
BROWERS_EXECUTABLE_PATH = os.getenv("BROWERS_EXECUTABLE_PATH")  # Path to browser executable
SITE_URL_ONE = os.getenv("SITE_URL_ONE")      # First target website URL
SITE_URL_TWO = os.getenv("SITE_URL_TWO")      # Second target website URL
SITE_URL_THREE = os.getenv("SITE_URL_THREE")   # Third target website URL

# Initialize Playwright and start the automation process
with sync_playwright() as p:
    # Launch a non-headless Chrome browser with specified executable path
    # headless=False allows visual observation of the automation
    browser = p.chromium.launch(executable_path=BROWERS_EXECUTABLE_PATH, headless=False)
    context = browser.new_context()

    # Load previously saved cookies to maintain session state
    with open("cookies.json", "r") as f:
        cookies = json.load(f)
        context.add_cookies(cookies)

    # Create a new page and start the automation sequence
    page = context.new_page()
    
    # Site One interactions
    page.goto(SITE_URL_ONE)
    time.sleep(2)  # Wait for page load
    page.locator(".components-home-assets-__sign-guide_---guide-close---2VvmzE").click()  # Close guide popup
    time.sleep(1)
    page.evaluate("document.querySelector('div.components-home-assets-__sign-content-test_---actived-day---34r3rb').click()")  # Select active day
    time.sleep(2)

    # Site Two interactions
    page.goto(SITE_URL_TWO)
    time.sleep(2)  # Wait for page load
    page.locator(".components-pc-assets-__dialog_---dialog-close---3G9gO2").click()  # Close dialog
    time.sleep(1)
    page.locator("div").filter(has_text=re.compile(r"^×2Day 1$")).locator("img").click()  # Click specific day element
    time.sleep(2)

    # Site Three interactions
    page.goto(SITE_URL_THREE)
    time.sleep(2)  # Wait for page load
    page.locator(".components-pc-assets-__dialog_---dialog-close---3G9gO2").click()  # Close dialog
    time.sleep(1)
    page.locator("div").filter(has_text=re.compile(r"^×2Day")).locator("img").nth(1).click()  # Click second day element
    time.sleep(5)

    # Save updated cookies for future sessions
    cookies = context.cookies()
    with open("cookies.json", "w") as f:
        json.dump(cookies, f)

    # Clean up by closing the browser
    browser.close()