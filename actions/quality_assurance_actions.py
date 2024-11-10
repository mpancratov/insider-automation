import allure
from selenium.webdriver.common.action_chains import ActionChains
from pages.quality_assurance_page import QualityAssurancePage
from utils.common_utils import CommonUtils

class QualityAssuranceActions:
    def __init__(self, driver):
        self.driver = driver
        self.qa_page = QualityAssurancePage(driver)
        self.utils = CommonUtils(driver)
        self.actions_hv = ActionChains(driver)

    @allure.step("Opening Quality Assurance Page")    
    def open_qa_page(self):
        print("Action: Opening Quality Assurance Page")
        self.qa_page.load()
        assert "Insider quality assurance" in self.driver.title, "Quality Assurance page did not open as expected"
        self.utils.accept_cookies_if_present()

    @allure.step("Validating QA Jobs")
    def validate_qa_jobs(self):
        print("Action: CLicking on 'See All QA Jobs'")
        all_qa_button = self.utils.wait_for_element_to_be_visible(*self.qa_page.SEE_ALL_QA_JOBS)
        all_qa_button.click()
        self.utils.accept_cookies_if_present()

        print("Action: Select 'Turkey' Filter Location")
        self.utils.poll_click_until_options_loaded(self.qa_page.get_filter_by_location(), *self.qa_page.TURKEY_LOCATION_OPTION)
        turkey_option = self.utils.wait_for_element_to_be_visible(*self.qa_page.TURKEY_LOCATION_OPTION)
        turkey_option.click()

        #quality assurance department is selected by default
        assert self.utils.wait_for_element_to_be_visible(*self.qa_page.QA_POSITION) is not None, "Expected QA Position element to be visible, but it was not found."

        
        print("Action: Validate Jobs Title, Department, Location")
        for job in self.qa_page.get_job_positions():
            assert "Quality Assurance" in self.qa_page.get_job_title(job), f"Expected 'Quality Assurance' in title, but got '{self.qa_page.get_job_title(job)}'"
            assert "Quality Assurance" in self.qa_page.get_job_department(job), f"Expected 'Quality Assurance' in department, but got '{self.qa_page.get_job_department(job)}'"
            assert "Istanbul, Turkey" in self.qa_page.get_job_location(job), f"Expected 'Istanbul, Turkey' in location, but got '{self.qa_page.get_job_location(job)}'"
   
    @allure.step("Validating Lever Application form page")
    def validate_lever_app_page_opens(self):
        print("Action: CLicking on 'View Role'")
        self.actions_hv.move_to_element(self.qa_page.get_view_role()).perform()
        self.utils.js_click(self.qa_page.get_view_role())


        print("Action: Validating Lever Application form page")
        all_tabs = self.driver.window_handles
        self.driver.switch_to.window(all_tabs[-1])
        self.utils.wait_for_element_to_be_visible(*self.qa_page.APPLY_FOR_JOB)
        assert "Senior Software Quality Assurance Engineer" in self.driver.title, "Application form  page did not open as expected"
        






 
