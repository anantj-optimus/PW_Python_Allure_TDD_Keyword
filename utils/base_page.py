# utils/base_page.py

class BasePage:
    def __init__(self, page):
        self.page = page

    def get_locator(self, locator_type, locator_value):
        if locator_type.lower() == 'xpath':
            return self.page.locator(locator_value)
        elif locator_type.lower() == 'css':
            return self.page.locator(locator_value)
        elif locator_type.lower() == 'text':
            return self.page.get_by_text(locator_value)
        else:
            raise ValueError(f"Unsupported locator type: {locator_type}") 

    def navigate(self, url):
        self.page.goto(url)

    def type(self, locator_type, locator_value, text):
        self.get_locator(locator_type, locator_value).fill(text)
    
    def press(self, locator_type, locator_value, text):
        self.get_locator(locator_type, locator_value).press(text)

    def click(self, locator_type, locator_value):
        locator = self.get_locator(locator_type, locator_value)
        locator.click()

    def verifytext(self, text):
        assert text.lower() in self.page.content().lower()

    def verifyloc(self, locator_type, locator_value, text):
        locator = self.get_locator(locator_type, locator_value)
        assert text.lower() in self.page.content().lower()

    def wait(self, seconds):
        self.page.wait_for_timeout(seconds * 1000)

    def gettext(self, locator_type, locator_value):
        return self.get_locator(locator_type, locator_value).inner_text()
    
    def asserttext(self, locator_type, locator_value, expected_text):
        element = self.get_locator(locator_type, locator_value)
        actual_text = element.text_content()  # <- Get the string text
        assert actual_text and expected_text.lower() in actual_text.lower(), \
        f"Expected '{expected_text}' not found in '{actual_text}'"


 