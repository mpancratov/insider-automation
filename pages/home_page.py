from constants import BASE_URL
from selenium.webdriver.common.by import By

class HomePage:
    URL = BASE_URL
    TITLE = "Insider"
    COMPANY_MENU = (By.LINK_TEXT, "Company")
    COMPANY_DROPDOWN = (By.XPATH, "//a[contains(@id, 'navbarDropdownMenuLink') and contains(text(),'Company')]")
    CAREERS_LINK = (By.XPATH, "//a[@class='dropdown-sub' and text()='Careers']")
    
    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def get_company_menu(self):
        return self.driver.find_element(*self.COMPANY_MENU)

    def get_company_dropdown(self):
        return self.driver.find_element(*self.COMPANY_DROPDOWN)    
