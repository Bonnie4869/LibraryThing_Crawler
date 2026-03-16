from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class BrowserDriver:

    def __init__(self):

        options = webdriver.ChromeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--start-maximized")

        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()), options=options
        )

    def get_page(self, url):

        self.driver.get(url)

    def current_page(self):

        return self.driver.page_source

    def close(self):

        self.driver.quit()
