# utils/base_page.py

class BasePage:
    def __init__(self, page):
        self.page = page

    def navigate(self, url):
        self.page.goto(url)

    def type(self, locator_type, locator_value, text):
        locator = self._get_locator(locator_type, locator_value)
        locator.fill(text)


    def press(self, locator_type, locator_value, text):
        locator = self._get_locator(locator_type, locator_value)
        locator.press(text)

    def click(self, locator_type, locator_value):
        locator = self._get_locator(locator_type, locator_value)
        locator.click()

    def verifytext(self, text):
        assert text.lower() in self.page.content().lower()

    def verifyloc(self, locator_type, locator_value, text):
        locator = self._get_locator(locator_type, locator_value)
        assert text.lower() in self.page.content().lower()

    def wait(self, seconds):
        self.page.wait_for_timeout(seconds * 1000)

    def _get_locator(self, locator_type, locator_value):
        if locator_type.lower() == 'xpath':
            return self.page.locator(locator_value)
        elif locator_type.lower() == 'css':
            return self.page.locator(locator_value)
        elif locator_type.lower() == 'text':
            return self.page.get_by_text(locator_value)
        else:
            raise ValueError(f"Unsupported locator type: {locator_type}")
