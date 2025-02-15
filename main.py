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
    time.sleep(4)  # Allow page elements to fully render
    page.locator(".components-home-assets-__sign-guide_---guide-close---2VvmzE").click()  # Dismiss initial guide overlay
    time.sleep(1)  # Brief pause to ensure dialog is fully closed
    # Click on the active day element to initiate the daily action
    page.evaluate("document.querySelector('div.components-home-assets-__sign-content-test_---actived-day---34r3rb').click()")
    time.sleep(4)  # Wait for action to complete and any animations to finish

    def click_days(SITE_URL):
        """
        Performs a sequence of clicks on daily elements for a given site URL.
        This function handles the repetitive task of clicking day-related elements.
        
        Args:
            SITE_URL (str): The URL of the website to perform actions on
        """
        # Navigate to the specified URL
        page.goto(SITE_URL)
        time.sleep(4)  # Allow page and all dynamic content to load completely
        # Close the modal dialog that appears on initial page load
        page.locator(".components-pc-assets-__dialog_---dialog-close---3G9gO2").click()
        time.sleep(1)  # Ensure dialog is dismissed before proceeding
        # Click on the 9th day element to initiate the daily action
        page.locator("div").filter(has_text=re.compile(r"Day 1")).nth(8).locator("img").click()
        time.sleep(4)  # Final wait to ensure all actions are processed

    # Process additional sites using the click_days function
    click_days(SITE_URL_TWO)
    click_days(SITE_URL_THREE)
    
    # Save the updated session cookies for future use
    cookies = context.cookies()
    with open("cookies.json", "w") as f:
        json.dump(cookies, f)
        
    # Clean up by closing the browser instance
    browser.close()