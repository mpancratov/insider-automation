import pytest
from actions.quality_assurance_actions import QualityAssuranceActions
from utils.base_test import BaseTest

@pytest.mark.usefixtures("setup_class")
class TestQualityAssurance(BaseTest):
    def setup_method(self):
        self.actions = QualityAssuranceActions(self.driver)

    def test_validate_insider_qa_page_opens(self):
        self.actions.open_qa_page()

    def test_validate_qa_jobs(self):
        self.actions.open_qa_page()
        self.actions.validate_qa_jobs()
        self.actions.validate_lever_app_page_opens()
        
