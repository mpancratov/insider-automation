import time
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class CommonUtils:
    def __init__(self, driver):
        self.driver = driver

    def scroll_to(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def js_click(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    def wait_for_element_to_be_clickable(self, by, value, timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((by, value))
        )  

    def wait_for_element_to_be_visible(self, by, value, timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((by, value))
        )    

    def handle_dropdown(self, dropdown_element, value):
        select = Select(dropdown_element)
        select.select_by_visible_text(value)

    def accept_cookies_if_present(self, timeout=5):
        try:
            accept_button = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, "//a[@id='wt-cli-accept-all-btn']"))
            )
            accept_button.click()
            print("Cookie consent accepted.")
        except:
            print("Cookie consent button not present.")

    def click_till_visibility(self, element_to_click, *target_element_locator):   
        start_time = time.time()
        max_wait_time=30

        while True:
            try:
                target_element = self.wait_for_element_to_be_visible(*target_element_locator)
                if target_element:
                    print("Target element is now visible.")
                    return True
            except TimeoutException:
                self.js_click(element_to_click)
                print("Clicked the specified element, waiting for target element...")

            if time.time() - start_time > max_wait_time:
                print("Target element did not become visible within the maximum wait time.")
                return False

    def poll_click_until_options_loaded(self, filter_element, by, value):
        max_attempts = 10
        delay = 10
        attempts = 0

        while attempts < max_attempts:
            try:
                filter_element.click()
                print(f"Attempt {attempts + 1}: Clicked on filter.")
                if attempts % 2 == 1:  
                    print(f"Skipping wait on attempt {attempts + 1}.")
                else:
                    WebDriverWait(self.driver, delay).until(
                        EC.visibility_of_element_located((by, value))
                    )
                    print("Options are loaded.")
                    return True  

            except (TimeoutException, NoSuchElementException):
                print(f"Attempt {attempts + 1}: Options not loaded, retrying...")
            attempts += 1

        print("Failed to load options after multiple attempts.")
        return False