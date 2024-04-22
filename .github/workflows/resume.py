from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType, PATTERN
from webdriver_manager.core.utils import read_version_from_cmd
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from os import getcwd, remove
from os.path import exists, join
from json import dumps
from base64 import b64decode
from time import sleep

if exists(join(getcwd(), 'resume.pdf')):
    remove(join(getcwd(), 'resume.pdf'))

if exists("/usr/bin/chromium"):
    chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM, driver_version=read_version_from_cmd(
        "/usr/bin/chromium --version", PATTERN[ChromeType.CHROMIUM])).install())
    print(f"""/usr/bin/chromium: {read_version_from_cmd(
        '/usr/bin/chromium --version', PATTERN[ChromeType.CHROMIUM])}""")
elif exists("/usr/bin/chromium-browser"):
    chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM, driver_version=read_version_from_cmd(
        "/usr/bin/chromium-browser --version", PATTERN[ChromeType.CHROMIUM])).install())
    print(f"""/usr/bin/chromium-browser: {read_version_from_cmd(
        '/usr/bin/chromium-browser --version', PATTERN[ChromeType.CHROMIUM])}""")
else:
    chrome_service = Service(ChromeDriverManager(
        chrome_type=ChromeType.CHROMIUM).install())
    print(f"detected: {chrome_service.path.split('/')[7]}")

chrome_options = Options()
options = [
    "--headless",
    "--disable-gpu",
    "--window-size=1920,1200",
    "--ignore-certificate-errors",
    "--disable-extensions",
    "--no-sandbox",
    "--disable-dev-shm-usage"
]
for option in options:
    chrome_options.add_argument(option)

print_settings = {
    "recentDestinations": [{
        "id": "Save as PDF",
        "origin": "local",
        "account": "",
    }],
    "selectedDestinationId": "Save as PDF",
    "version": 2,
    "isHeaderFooterEnabled": False,
    "isLandscapeEnabled": True
}

chrome_options.add_experimental_option("prefs", {
    "printing.print_preview_sticky_settings.appState": dumps(print_settings),
    "savefile.default_directory": getcwd(),
    "download.default_directory": getcwd(),
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "profile.default_content_setting_values.automatic_downloads": 1,
    "safebrowsing.enabled": True
})

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

driver.get('https://resume.creddle.io/resume/awnsqrb764w')

sleep(10)

pdf_data = driver.execute_cdp_cmd("Page.printToPDF", print_settings)
with open('resume.pdf', 'wb') as file:
    file.write(b64decode(pdf_data['data']))
