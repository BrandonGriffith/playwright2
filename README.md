# Web Automation Script

This project uses Playwright with Python to automate interactions across multiple websites. It handles cookie management for maintaining session states and performs automated clicks and navigations.

## Prerequisites

- Python 3.7 or higher
- Playwright for Python
- python-dotenv

## Installation

1. Install the required packages:
```bash
pip install playwright python-dotenv
```

2. Install Playwright browsers:
```bash
playwright install
```

## Configuration

1. Create a `.env` file in the project root with the following variables:
```
BROWERS_EXECUTABLE_PATH=path/to/your/browser/executable
SITE_URL_ONE=your_first_site_url
SITE_URL_TWO=your_second_site_url
SITE_URL_THREE=your_third_site_url
```

2. Ensure you have a `cookies.json` file in the project root. This file will be used to store and load browser cookies.

## Usage

Run the script using:
```bash
python main.py
```

The script will:
1. Load saved cookies from cookies.json
2. Navigate through three different websites
3. Perform automated interactions on each site
4. Save updated cookies back to cookies.json
5. Close the browser automatically

## File Structure

- `main.py` - The main automation script
- `cookies.json` - Stores browser cookies for session management
- `.env` - Environment variables configuration
- `README.md` - Project documentation

## Notes

- The script runs in non-headless mode for visual observation
- Includes appropriate wait times between actions to ensure page loading
- Automatically handles cookie persistence between sessions
