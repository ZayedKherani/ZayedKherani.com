# Description: This script is used to generate a PDF version of my
# resume using the Chromium WebDriver on GitHub Actions and save it
# to the root directory of the repository for https://zayedkherani.com/resume

# Importing Required Modules

"""
from webdriver_manager.core.os_manager import ChromeType, PATTERN
from webdriver_manager.core.utils import read_version_from_cmd
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
"""
from os.path import exists, join
"""
from selenium import webdriver
"""
from os import getcwd, remove
"""
from base64 import b64decode
"""
from requests import get
"""
from json import dumps
from time import sleep
"""

# Removing the existing resume.pdf file if it exists
remove(
    join(
        getcwd(),
        'resume.pdf'
    )
) if exists(
    join(
        getcwd(),
        'resume.pdf'
    )
) else None


# Temporarily stop Print to PDF and replace with direct save
"""
# Starting the Chrome WebDriver Options Agent
chrome_options = Options()

# Adding Options to the Chrome WebDriver Options Agent
# to Run the Chrome WebDriver in Headless Mode While
# Still Rendering the Page
[chrome_options.add_argument(option) for option in [
    "--headless",
    "--disable-gpu",
    "--window-size=1920,1200",
    "--ignore-certificate-errors",
    "--disable-extensions",
    "--no-sandbox",
    "--disable-dev-shm-usage"
]]

# Adding Experimental Options to the Chrome WebDriver
# Options Agent to Enable the Printing of the Page
# to a PDF File
chrome_options.add_experimental_option(
    "prefs",
    {
        "printing.print_preview_sticky_settings.appState": dumps(
            {
                "recentDestinations": [
                    {
                        "id": "Save as PDF",
                        "origin": "local",
                        "account": "",
                    }
                ],
                "selectedDestinationId": "Save as PDF",
                "version": 2,
                "isHeaderFooterEnabled": False,
                "isLandscapeEnabled": True
            }
        ),
        "savefile.default_directory": getcwd(),
        "download.default_directory": getcwd(),
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "profile.default_content_setting_values.automatic_downloads": 1,
        "safebrowsing.enabled": True
    }
)

# Defining and Starting the Chrome WebDriver Service Dynamically
# Starting Chromium via WebDriver
driver = webdriver.Chrome(
    service=Service(
        ChromeDriverManager(
            chrome_type=ChromeType.CHROMIUM,
            driver_version=read_version_from_cmd(
                "/usr/bin/chromium --version",
                PATTERN[ChromeType.CHROMIUM]
            )
        ).install()
    ) if exists("/usr/bin/chromium") else Service(
        ChromeDriverManager(
            chrome_type=ChromeType.CHROMIUM,
            driver_version=read_version_from_cmd(
                "/usr/bin/chromium-browser --version",
                PATTERN[ChromeType.CHROMIUM]
            )
        ).install()
    ) if exists("/usr/bin/chromium-browser") else Service(
        ChromeDriverManager(
            chrome_type=ChromeType.CHROMIUM
        ).install()
    ),
    options=chrome_options
)

# Navigate to the Resume Page
driver.get(
    'https://resume.creddle.io/resume/awnsqrb764w'
)

# Waiting for the Page to Load
sleep(10)

# Print the Page to a PDF File and Retrieve the PDF Data
pdf_data = driver.execute_cdp_cmd(
    "Page.printToPDF",
    {
        "recentDestinations": [
            {
                "id": "Save as PDF",
                "origin": "local",
                "account": "",
            }
        ],
        "selectedDestinationId": "Save as PDF",
        "version": 2,
        "isHeaderFooterEnabled": False,
        "isLandscapeEnabled": True
    }
)
"""

# Getting the PDF Data
# Writing the PDF Data to a PDF File
with open('resume.pdf', 'wb') as file:
    # file.write(b64decode(pdf_data['data']))
    file.write(get("https://zayedkherani.com/resume.pdf").content)

# Temporarily stop Print to PDF and replace with direct save
"""
# Closing the Chrome WebDriver
driver.quit()
"""

# Closing the PDF File if it is Open
try:
    file.close()
except:
    pass
