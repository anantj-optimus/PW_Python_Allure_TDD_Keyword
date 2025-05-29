# utils/keyword_engine.py

from config import base_url
from playwright.sync_api import expect
import allure

class KeywordEngine:
    def __init__(self, page):
        self.page = page

    def execute(self, keyword, locator_type=None, locator_value=None, test_data=None):
        locator = None
        if locator_type and locator_value:
            if locator_type.lower() == "xpath":
                locator = self.page.locator(locator_value)
            elif locator_type.lower() == "css":
                locator = self.page.locator(locator_value)
            elif locator_type.lower() == "id":
                locator = self.page.locator(f"#{locator_value}")
            elif locator_type.lower() == "text":
                locator = self.page.get_by_text(locator_value)

        keyword = keyword.lower()

        if keyword == "navigate":
            self.page.goto(test_data or base_url)

        elif keyword == "type" and locator:
            locator.fill(test_data)

        elif keyword == "press" and locator:
            locator.press(test_data)

        elif keyword == "click" and locator:
            locator.click()

        elif keyword == "verifytext":
            locator = self.page.locator(locator_value)
            expect(locator).to_have_text(test_data)

        elif keyword == "verifyelement" and locator:
            expect(locator).to_be_visible()

        elif keyword == "wait":
            self.page.wait_for_timeout(int(test_data))

        else:
            raise ValueError(f"Unsupported keyword: {keyword}")
