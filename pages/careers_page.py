from constants import CAREERS_URL
from selenium.webdriver.common.by import By

EXPECTED_JOB_TITLES = [
    "Partner Support Development",
    "Mobile Business Unit",
    "Product Design",
    "Security Engineering",
    "Quality Assurance"
]

EXPECTED_LOCATIONS = [
    "Bogota",
    "Santiago",
    "Buenos Aires",
    "Lima",
    "Mexico City"
]

class CareersPage:
    URL = CAREERS_URL
    ALL_TEAMS_BUTTON = (By.XPATH, "//section[@id='career-find-our-calling']//a[text()='See all teams']")
    ALL_TEAMS_SECTION = (By.CLASS_NAME, "career-load-more")
    JOB_ITEMS = (By.XPATH, "//div[contains(@class,'job-item')]//h3")
    ALL_LOCATIONS = (By.XPATH, "//ul[@class='glide__slides']//img[@alt]")
    PEOPLE_AND_CULTURE = (By.XPATH, "//div[contains(@class,'job-item')]//h3[ text()='People and Culture']")
    BACK_ARROW_CULTURE = (By.XPATH, "//i[contains(@class, 'icon-arrow-left') and contains(@class, 'location-slider-prev')]")
    MEXICO_CITY_LOCATION = (By.XPATH, "//ul[@class='glide__slides']//img[@alt='Mexico City']")
    LIFE_AT_INSIDER_SECTION = (By.XPATH, "//section[contains(@class, 'elementor-section') and .//h2[text()='Life at Insider']]") 
    LOCATIONS_SECTION = (By.ID, "career-location")
    TEAMS_SECTION = (By.ID, "career-team")
    LIFE_AT_SECTION = (By.ID, "life-at-insider")
    SEE_ALL_QA_JOBS_BUTTON = (By.LINK_TEXT, "See all QA jobs")
    FILTER_LOCATION_DROPDOWN = (By.ID, "filter-location")
    FILTER_DEPARTMENT_DROPDOWN = (By.ID, "filter-department")
    VIEW_ROLE_BUTTON = (By.LINK_TEXT, "View Role")
    
    
    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def get_locations_section(self):
        return self.driver.find_element(*self.LOCATIONS_SECTION)

    def get_teams_section(self):
        return self.driver.find_element(*self.TEAMS_SECTION)

    def get_life_at_section(self):
        return self.driver.find_element(*self.LIFE_AT_SECTION)

    def get_see_all_qa_jobs_button(self):
        return self.driver.find_element(*self.SEE_ALL_QA_JOBS_BUTTON)

    def get_filter_location_dropdown(self):
        return self.driver.find_element(*self.FILTER_LOCATION_DROPDOWN)

    def get_filter_department_dropdown(self):
        return self.driver.find_element(*self.FILTER_DEPARTMENT_DROPDOWN)

    def get_view_role_buttons(self):
        return self.driver.find_elements(*self.VIEW_ROLE_BUTTON)
    
    def get_see_all_teams_button(self):
        return self.driver.find_element(*self.ALL_TEAMS_BUTTON)

    def get_all_teams_section(self):
        return self.driver.find_element(*self.ALL_TEAMS_SECTION)

    def get_people_and_culture(self):
        return self.driver.find_element(*self.PEOPLE_AND_CULTURE)   

    def get_job_items(self):
        return self.driver.find_elements(*self.JOB_ITEMS)

    def get_all_locations(self):
        return self.driver.find_elements(*self.ALL_LOCATIONS)    
    
    def get_back_arrow_culture(self):
        return self.driver.find_element(*self.BACK_ARROW_CULTURE)   

    def get_mexico_city_location(self):
        return self.driver.find_element(*self.MEXICO_CITY_LOCATION)        
    
    def get_life_of_insider_section(self):
        return self.driver.find_element(*self.LIFE_AT_INSIDER_SECTION)  
        
        