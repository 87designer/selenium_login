from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from config import username, run_method
from getpass import getpass


def main():
    """

    :return:
    """
    password = getpass(prompt='Password: ', stream=None)
    if run_method == "headless":
        def set_chrome_options():
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_prefs = {}
            chrome_options.experimental_options["prefs"] = chrome_prefs
            chrome_prefs["profile.default_content_settings"] = {"images": 2}
            #chrome_prefs["download.default_directory"] = r"C:\tmp\\"
            #chrome_prefs["directory_upgrade"] = True

            return chrome_options
    else:
        def set_chrome_options():
            chrome_options = Options()
            chrome_options.add_argument("start-maximized")
            chrome_options.add_argument("disable-infobars")
            chrome_options.add_argument("--disable-extensions")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_prefs = {}
            chrome_options.experimental_options["prefs"] = chrome_prefs
            # chrome_prefs["download.default_directory"] = r"C:\tmp\\"
            # chrome_prefs["directory_upgrade"] = True

            return chrome_options

        chrome_options = set_chrome_options()
        driver = webdriver.Chrome(options=chrome_options)

if __name__ == '__main__':
    main()