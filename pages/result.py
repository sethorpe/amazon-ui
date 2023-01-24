from selenium.webdriver.common.by import By

class AmazonResultPage:
    SEARCH_INPUT = (By.ID, "twotabsearchtextbox")

    def __init__(self, browser):
        self.browser = browser
    
    def search_input_value(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        return search_input.get_attribute('value')
    
    def select_choice_item(self):
        try:
            choice_item = self.browser.find_element_by_xpath("//span[contains(@class, 'a-badge-label') and contains(@id, 'amazons-choice-label')]")
            if choice_item.is_displayed():
                self.browser.execute_script("arguments[0].scrollIntoView();", choice_item)
                return choice_item.click()
            else:
                return print("Amazon Choice label not available for this product!")
        except Exception as e:
            return str(e)
            # print ("An exception occurred: " + str(e))
            # print ("Amazon's Choice label not available for this product")

