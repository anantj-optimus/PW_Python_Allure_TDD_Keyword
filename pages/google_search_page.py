from config import base_url
from playwright.sync_api import expect
import allure

class GoogleSearchPage:
    def __init__(self, page):
        self.page = page
        self.search_input = page.locator('//*[@id="sb_form_q"]')
    
    #@allure.step("Navigating to Google")
    def navigate(self):
        self.page.goto(base_url)
        print(">>> Using updated locator")

    #@allure.step("Searching for term: {text}")
    def search(self, text):
        self.search_input.fill(text)
        self.page.wait_for_timeout(1000)
        self.search_input.press("Enter")
        print(f">>> Searched for: {text}")
       
    #    self.page.pause()  # 🔍 Inspector opens here
    #   import pdb; pdb.set_trace()

    #@allure.step("Verifying if results contain text: {expected}")
    def verify_result(self, expected):
        self.page.wait_for_timeout(3000)
        self.page.wait_for_selector("text=" + expected)
        print(f">>> Verifying result for: {expected}")
        return expected.lower() in self.page.content().lower()
    

