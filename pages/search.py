import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class AmazonSearchPage:
    URL = 'https://www.amazon.com'

    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)
        self.browser.delete_all_cookies()
    
    def search(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.ENTER)
        time.sleep(5)