# conftest.py
import os
import shutil
import allure
import pytest
from playwright.sync_api import Page

# Clean Allure reports after every 3rd run
RUN_HISTORY = []
MAX_RUNS = 3

def pytest_sessionstart(session):
    global RUN_HISTORY
    RUN_HISTORY.append(1)
    
    if len(RUN_HISTORY) > MAX_RUNS:
        if os.path.exists("allure-results"):
            shutil.rmtree("allure-results")
        RUN_HISTORY.clear()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    
    # Log every test case
    with allure.step(f"Test: {item.nodeid}"):
        if report.when == 'call':
            # Capture screenshot only on failure
            if report.failed:
                page = item.funcargs.get('page')
                if page:
                    allure.attach(
                        page.screenshot(full_page=True),
                        name="failure_screenshot",
                        attachment_type=allure.attachment_type.PNG
                    )
            # Log final status
            allure.dynamic.title(f"{item.nodeid} ({report.outcome})")

