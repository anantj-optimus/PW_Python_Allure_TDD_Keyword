# utils/keyword_engine.py

from utils.base_page import BasePage

class KeywordEngine(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def execute(self, keyword, locator_type=None, locator_value=None, test_data=None):
        method = getattr(self, keyword.lower(), None)
        if not method:
            raise Exception(f"Unknown keyword: {keyword}")
        if locator_type and locator_value and test_data:
            method(locator_type, locator_value, test_data)
        elif locator_type and locator_value:
            method(locator_type, locator_value)
        elif test_data:
            method(test_data)
        else:
            method()
            return method(locator_type, locator_value, test_data)
