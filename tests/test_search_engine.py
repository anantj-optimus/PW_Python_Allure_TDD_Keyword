# test_google_search.py for Keyword-Driven Framework

import os
import allure
import pytest
from utils.keyword_engine import KeywordEngine
from utils.excel_reader import get_test_steps_by_testcase
from config import file_path
from utils.html_reporter import generate_html_summary  # Add this


@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("testcase_id, steps", get_test_steps_by_testcase(file_path))
def test_keyword_driven(page, testcase_id, steps):
    engine = KeywordEngine(page)
    step_results = []

    # Generate dynamic title
    search_terms = [step['Test Data'] for step in steps if step['Keyword'].lower() == 'type']
    term_summary = f"Search for '{search_terms[0]}'" if search_terms else "Execute Steps"
    allure.dynamic.title(f"{testcase_id} - {term_summary}")

    test_failed = False

    for step in steps:
        with allure.step(f"[{testcase_id}] {step['Step']}"):
            try:
                engine.execute(
                    keyword=step['Keyword'],
                    locator_type=step.get('Locator Type'),
                    locator_value=step.get('Locator Value'),
                    test_data=step.get('Test Data')
                )
                step_results.append("Pass")
            except AssertionError as e:
                step_results.append("Fail")
                test_failed = True

                os.makedirs("screenshots", exist_ok=True)
                screenshot_path = f"screenshots/{testcase_id}_failure.png"
                page.screenshot(path=screenshot_path, full_page=True)
                allure.attach.file(
                    screenshot_path,
                    name=f"Failure Screenshot for {testcase_id}",
                    attachment_type=allure.attachment_type.PNG
                )
                break  # stop further steps if one fails

    # Always generate table, even if test failed
    html_table = generate_html_summary(testcase_id, steps, step_results)
    allure.dynamic.description_html(html_table)

    # Take final screenshot only if no failure
    if not test_failed:
        os.makedirs("screenshots", exist_ok=True)
        screenshot_path = f"screenshots/{testcase_id}_success.png"
        page.screenshot(path=screenshot_path, full_page=True)
        allure.attach.file(
            screenshot_path,
            name=f"Search result for {testcase_id}",
            attachment_type=allure.attachment_type.PNG
        )

    if test_failed:
        pytest.fail(f"Testcase {testcase_id} failed. See steps above.")
