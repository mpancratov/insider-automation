import pytest
from actions.home_actions import HomeActions
from utils.base_test import BaseTest

@pytest.mark.usefixtures("setup_class")
class TestHome(BaseTest):
    def setup_method(self):
        self.actions = HomeActions(self.driver)

    def test_validate_insider_home_page_opens(self):
        self.actions.open_home_page()
        
