from constants import QUALITY_ASSURANCE_URL
from selenium.webdriver.common.by import By

class QualityAssurancePage:
    URL = QUALITY_ASSURANCE_URL
    TITLE = "Insider quality assurance"
    SEE_ALL_QA_JOBS = (By.XPATH, "//a[contains(text(), 'See all QA jobs')]")
    FILTER_BY_LOCATION = (By.ID, "select2-filter-by-location-container")
    FILTER_BY_DEPARTMENT = (By.ID, "select2-filter-by-department-container")
    TURKEY_LOCATION_OPTION = (By.XPATH, " //li[@class='select2-results__option' and text()='Istanbul, Turkey']")
    QUALITY_ASSURANCE_OPTION = (By.ID, "select2-filter-by-department-result-mmcz-Quality Assurance")
    POSITION_WRAPPER = (By.XPATH, "//div[@class='position-list-item-wrapper bg-light']")
    ALL_JOB_POSITIONS = (By.XPATH, ".//div[contains(@class, 'position-list-item-wrapper')]")
    QA_POSITION = (By.XPATH, "//div[@id='jobs-list']//span[text()='Quality Assurance']")
    VIEW_ROLE = (By.XPATH, "//div[contains(@class, 'position-list-item-wrapper')]//a[text()='View Role']")   
    APPLY_FOR_JOB = (By.XPATH, "//a[@class='postings-btn template-btn-submit shamrock']")  
    PAGE_COUNT = (By.XPATH, "//span[@class='currentResult' and text()='1 - 12']")  

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def get_qa_link(self):
        return self.driver.find_element(*self.URL)
    
    def get_all_qa_jobs(self):
        return self.driver.find_element(*self.SEE_ALL_QA_JOBS)

    def get_filter_by_location(self):
        return self.driver.find_element(*self.FILTER_BY_LOCATION)

    def get_turkey_location_option(self):
        return self.driver.find_element(*self.TURKEY_LOCATION_OPTION)
    
    def get_position_wrapper(self):
        return self.driver.find_element(*self.POSITION_WRAPPER)
    
    def get_job_positions(self):
        return self.driver.find_elements(*self.ALL_JOB_POSITIONS)

    def get_filter_by_department(self):
        return self.driver.find_element(*self.FILTER_BY_DEPARTMENT)
    
    def get_quality_assurance_option(self):
        return self.driver.find_element(*self.QUALITY_ASSURANCE_OPTION)

    def get_view_role(self):
        return self.driver.find_element(*self.VIEW_ROLE)

    def get_apply_for_job(self):
        return self.driver.find_element(*self.APPLY_FOR_JOB)
    
    def get_job_title(self, job):
        return job.find_element(By.XPATH, ".//p[contains(@class, 'position-title')]").text

    def get_job_department(self, job):
        return job.find_element(By.XPATH, ".//span[contains(@class, 'position-department')]").text

    def get_job_location(self, job):
        return job.find_element(By.XPATH, ".//div[contains(@class, 'position-location')]").text
