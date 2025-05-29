# test_google_search.py for Keyword-Driven Framework

import os
import allure
import pytest
from utils.keyword_engine import KeywordEngine
from utils.excel_reader import get_test_steps_by_testcase
from config import file_path

# @allure.feature("Search Functionality")
# @allure.story("Google Search Automation")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("testcase_id, steps", get_test_steps_by_testcase(file_path))

def test_keyword_driven(page, testcase_id, steps):
    engine = KeywordEngine(page)

    for step in steps:
        with allure.step(f"[{testcase_id}] {step['Step']}"):
            try:
                engine.execute(
                    keyword=step['Keyword'],
                    locator_type=step.get('Locator Type'),
                    locator_value=step.get('Locator Value'),
                    test_data=step.get('Test Data')
                )
            except AssertionError as e:
                os.makedirs("screenshots", exist_ok=True)
                screenshot_path = f"screenshots/{testcase_id}_failure.png"
                page.screenshot(path=screenshot_path, full_page=True)
                allure.attach.file(
                    screenshot_path,
                    name=f"Failure Screenshot for {testcase_id}",
                    attachment_type=allure.attachment_type.PNG
                )
                raise e

    os.makedirs("screenshots", exist_ok=True)
    screenshot_path = f"screenshots/{testcase_id}_success.png"
    page.screenshot(path=screenshot_path, full_page=True)
    allure.attach.file(
        screenshot_path,
        name=f"Search result for {testcase_id}",
        attachment_type=allure.attachment_type.PNG
    )
