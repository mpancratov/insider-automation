import allure
from selenium.common.exceptions import TimeoutException
from pages.careers_page import CareersPage, EXPECTED_JOB_TITLES, EXPECTED_LOCATIONS
from pages.home_page import HomePage
from utils.common_utils import CommonUtils
from selenium.webdriver.common.by import By

class CareersActions:
    def __init__(self, driver):
        self.driver = driver
        self.careers_page = CareersPage(driver)
        self.home_page = HomePage(driver)
        self.utils = CommonUtils(driver)
    
    @allure.step("Opening the Careers page")
    def open_careers_page(self):
        print("Action: Opening the Careers page")
        company_dropdown = self.utils.wait_for_element_to_be_visible(*self.home_page.COMPANY_DROPDOWN)
        company_dropdown.click()
        careers_option = self.utils.wait_for_element_to_be_visible(*self.home_page.CAREERS_LINK)
        careers_option.click()
        assert "Insider Careers" in self.driver.title, "Home page did not open as expected"

    @allure.step("Validating the presence of Teams, Locations, Life at Insider sections")
    def validate_sections_present(self):
        print("Action: Validating the presence of Teams section")
        all_teams_button = self.utils.wait_for_element_to_be_visible(*self.careers_page.ALL_TEAMS_BUTTON)
        self.utils.scroll_to(self.careers_page.get_see_all_teams_button())
        self.utils.js_click(self.careers_page.get_see_all_teams_button())
        assert self.careers_page.get_all_teams_section().is_displayed(), "Teams section is not displayed"

        #compare expected job titles with received list of job titles
        self.utils.wait_for_element_to_be_visible(*self.careers_page.PEOPLE_AND_CULTURE)
        job_titles = {job.text for job in self.careers_page.get_job_items()}
        expected_titles_set = set(EXPECTED_JOB_TITLES)
        assert expected_titles_set.issubset(job_titles), (
            f"Missing job titles: {expected_titles_set - job_titles}"
        )     

        print("Action: Validating the presence of Locations section")
        self.utils.scroll_to(self.careers_page.get_back_arrow_culture()) 
        back_arrow_button = self.utils.wait_for_element_to_be_visible(*self.careers_page.BACK_ARROW_CULTURE)
        
        #compare expected locations with received list of locations
        self.utils.click_till_visibility(self.careers_page.get_back_arrow_culture(), *self.careers_page.MEXICO_CITY_LOCATION)
        all_locations = {location.get_attribute('alt') for location in self.careers_page.get_all_locations()} 
        expected_locations_set = set(EXPECTED_LOCATIONS)
        assert expected_locations_set.issubset(all_locations), (
            f"Missing locations: {expected_locations_set - all_locations}"
        ) 

        print("Action: Validating the presence of Life at Insider section")
        self.utils.scroll_to(self.careers_page.get_life_of_insider_section()) 
        assert self.utils.wait_for_element_to_be_visible(*self.careers_page.LIFE_AT_INSIDER_SECTION) is not None, "Expected 'Life at Insider' section to be visible, but it was not found."



   