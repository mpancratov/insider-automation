import pytest
import time
from utils.base_test import BaseTest
from actions.careers_actions import CareersActions
from actions.home_actions import HomeActions

@pytest.mark.usefixtures("setup_class")
class TestCareers(BaseTest):
    def setup_method(self):
        self.home_actions = HomeActions(self.driver)
        self.careers_actions = CareersActions(self.driver)

    def test_validate_careers_page_opens(self):
        self.home_actions.open_home_page()
        self.careers_actions.open_careers_page()

    def test_validate_careers_page_sections(self):
        self.home_actions.open_home_page()
        self.careers_actions.open_careers_page()
        self.careers_actions.validate_sections_present()

