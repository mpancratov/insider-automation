import allure
from pages.home_page import HomePage
from utils.common_utils import CommonUtils

class HomeActions:
    def __init__(self, driver):
        self.driver = driver
        self.home_page = HomePage(driver)
        self.utils = CommonUtils(driver)

    @allure.step("Opening the Home page")
    def open_home_page(self):
        print("Action: Opening the Home page")
        self.home_page.load()
        assert "Insider" in self.driver.title, "Home page did not open as expected"
        self.utils.accept_cookies_if_present()
