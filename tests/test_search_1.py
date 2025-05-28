import pytest, allure
from pages.google_search_page import GoogleSearchPage
from utils.excel_reader import get_test_cases
from config import file_path

@allure.feature("Search Functionality")
@allure.story("Google Search Automation")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("testcase_id, term, expected", get_test_cases(file_path))
def test_google_search(page, testcase_id, term, expected):
    # Dynamically set test title and description in Allure
    allure.dynamic.title(f"[{testcase_id}] Search for: '{term}' and expect: '{expected}'")
    allure.dynamic.description(
        f"""Test Case ID: {testcase_id}
        - Search Term: {term}
        - Expected Result: {expected}
        """
    )

    search_page = GoogleSearchPage(page)

    with allure.step(f"[{testcase_id}] Navigate to Google"):
        search_page.navigate()

    with allure.step(f"[{testcase_id}] Search for term: '{term}'"):
        search_page.search(term)

    with allure.step(f"[{testcase_id}] Verify result contains: '{expected}'"):
        assert search_page.verify_result(expected), f"'{expected}' not found in search results"
