import pytest
from utils.custom_webdriver_manager import WebDriverManager

class BaseTest:
    @pytest.fixture(scope="class", autouse=True)
    def setup_class(self, request):
        driver_instance = WebDriverManager().get_driver()
        request.cls.driver = driver_instance  
        yield
        driver_instance.quit()  
