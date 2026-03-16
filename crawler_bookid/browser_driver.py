from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class BrowserDriver:

    def __init__(self, headless=False):

        options = webdriver.ChromeOptions()

        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--log-level=3")
        options.add_experimental_option("excludeSwitches", ["enable-logging"])

        if headless:
            options.add_argument("--headless=new")

        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()), options=options
        )

    def get_page(self, url):
        """get the HTML of the given url"""
        self.driver.get(url)
        return self.driver.page_source

    def close(self):
        self.driver.quit()
