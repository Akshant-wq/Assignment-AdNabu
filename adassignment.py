# Import required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class AdNabuTest:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)

# Open the login page
    def open_page(self):
        self.driver.get("https://adnabu-store-assignment1.myshopify.com/password")
        self.driver.maximize_window()

# Enter the password and login
    def enter_password(self, password):
        Enpass = self.wait.until(
            EC.visibility_of_element_located((By.ID, "password"))
        )
        Enpass.send_keys(password)
        Enpass.send_keys(Keys.RETURN)


# Click on the search icon
    def searchBox(self):
        search_box = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "(//*[@aria-hidden='true'])[9]"))
        )
        search_box.click()
    

# Search for a product
    def search_product(self, product_name):
        enter_product = self.wait.until(
            EC.visibility_of_element_located((By.ID, "Search-In-Modal"))
        )
        enter_product.send_keys(product_name)
        enter_product.send_keys(Keys.RETURN)
        


# Scroll and select the product
    def select_first_product(self):
        first_product = self.wait.until(
            
            EC.visibility_of_element_located((By.XPATH, "//a[@aria-labelledby='CardLink--7801364480090 Badge--7801364480090']"))
        )
        self.driver.execute_script("window.scrollBy(0,500)")
        first_product.click()
        
# Add the product to cart
    def add_to_cart(self):
        add_to_cart_btn = self.wait.until(
            EC.element_to_be_clickable((By.ID, "ProductSubmitButton-template--19850788667482__main"))
        )
        add_to_cart_btn.click()
         

     # Test execution
    def run_test(self):
        self.open_page()
        self.enter_password("AdNabuQA")
        self.searchBox()
        self.search_product("snowboard")
        self.select_first_product()
        self.add_to_cart()
    
 # Close browser   
def close_browser(self):
        self.driver.quit()      

    
# Main execution
if __name__ == "__main__":
    test = AdNabuTest()
    test.run_test()