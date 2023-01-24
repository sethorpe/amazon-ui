from typing import cast
from selenium.webdriver.common.by import By
import time

class AmazonProductPage:
    ADD_TO_CART = (By.ID, 'add-to-cart-button')
    VIEW_CART = (By.ID, 'hlb-view-cart-announce')
    ATTACH_WARRANTY = (By.ID,"attach-warranty-display")

    def __init__(self, browser):
        self.browser = browser

    def add_to_cart(self, warranty):
        add_to_cart = self.browser.find_element(*self.ADD_TO_CART)
        add_to_cart.click()
        time.sleep(5)
        try:
            add_warranty_pane = self.browser.find_element(*self.ATTACH_WARRANTY)
            if (add_warranty_pane.is_displayed()):
                return self.handle_warranty(warranty)
        except Exception as e:
            print("Add Warranty Pane is not visible. So just click the cart button to view it")
            return self.browser.find_element(*self.VIEW_CART).click()
            # print("End of transaction...for now!")      
        
    def handle_warranty(self, warranty):
        # add_warranty_pane = self.browser.find_element(*self.ATTACH_WARRANTY)
        # print("is warranty pane displayed: " + str(add_warranty_pane.is_displayed()))

        if (warranty == 'Yes'):
            # add_warranty = self.browser.find_element(By.CSS_SELECTOR("#attachSiAddCoverage > span:nth-child(1) > input:nth-child(1)"))
            add_warranty = self.browser.find_element(By.XPATH, "//body/div[@id='a-page']/div[@id='dp']/div[@id='dp-container']/div[@id='rightCol']/div[@id='attachAccessoryModal_feature_div']/div[@id='attach-dss-placeholder']/div[@id='attach-desktop-sideSheet']/div[@id='attach-warranty-pane']/div[@id='attach-warranty']/div[@id='attach-warranty-display']/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/span[1]/span[1]/input[1]")
            add_warranty.click()
            time.sleep(2)
            # cart = self.browser.find_element(By.CSS_SELECTOR("#attach-sidesheet-view-cart-button > span:nth-child(1) > input:nth-child(1)"))
            cart = self.browser.find_element(By.XPATH, "//body/div[@id='a-page']/div[@id='dp']/div[@id='dp-container']/div[@id='rightCol']/div[@id='attachAccessoryModal_feature_div']/div[@id='attach-dss-placeholder']/div[@id='attach-desktop-sideSheet']/div[@id='attach-accessory-pane']/div[1]/div[1]/div[3]/div[1]/div[2]/div[3]/form[1]/span[1]/span[1]/input[1]")
            return cart.click()

        else:
            # (add_warranty_pane.is_displayed() and warranty == 'No')
            # decline_warranty = self.browser.find_element(By.CSS_SELECTOR("#attachSiNoCoverage > span:nth-child(1) > input:nth-child(1)"))
            decline_warranty = self.browser.find_element(By.XPATH, "//body/div[@id='a-page']/div[@id='dp']/div[@id='dp-container']/div[@id='rightCol']/div[@id='attachAccessoryModal_feature_div']/div[@id='attach-dss-placeholder']/div[@id='attach-desktop-sideSheet']/div[@id='attach-warranty-pane']/div[@id='attach-warranty']/div[@id='attach-warranty-display']/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/span[2]/span[1]/input[1]")
            decline_warranty.click()
            time.sleep(2)
            # cart = self.browser.find_element(By.CSS_SELECTOR("#attach-sidesheet-view-cart-button > span:nth-child(1) > input:nth-child(1)")).Click()
            cart = self.browser.find_element(By.XPATH, "//body/div[@id='a-page']/div[@id='dp']/div[@id='dp-container']/div[@id='rightCol']/div[@id='attachAccessoryModal_feature_div']/div[@id='attach-dss-placeholder']/div[@id='attach-desktop-sideSheet']/div[@id='attach-accessory-pane']/div[1]/div[1]/div[3]/div[1]/div[2]/div[3]/form[1]/span[1]/span[1]/input[1]")
            return cart.click()
    