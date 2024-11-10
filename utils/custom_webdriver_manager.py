from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

class WebDriverManager:
    def get_driver(self):
        chrome_options = Options()
        chrome_options.add_argument("start-maximized")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")

        selenium_grid_url = os.getenv("SELENIUM_GRID_URL", "http://selenium-hub:4444")

        self.driver = webdriver.Remote(
            command_executor=selenium_grid_url,
            options=chrome_options  
        )
        return self.driver

    def quit_driver(self):
        if self.driver:
            self.driver.quit()
            self.driver = None
