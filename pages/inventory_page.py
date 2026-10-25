
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from config.settings import DEFAULT_TIMEOUT

class InventoryPage:

    page_title = (By.CLASS_NAME, "title")
    inventory_item = (By.CLASS_NAME, "inventory_item")
    sort_dropdown = (By.CLASS_NAME, "product_sort_container")
    cart_link = (By.CLASS_NAME, "shopping_cart_link")
    cart_badge = (By.CSS_SELECTOR, ".shopping_cart_badge")


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, DEFAULT_TIMEOUT)

    def get_page_title(self):
        return self.wait.until(EC.visibility_of_element_located(self.page_title)).text

    def get_product_count(self):
        return len(self.driver.find_elements(*self.inventory_item))

    def get_product_names(self):
        products = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")

        return [product.text for product in products]

    def sort_products(self, option):
        dropdown = self.wait.until(EC.element_to_be_clickable(self.sort_dropdown))
        Select(dropdown).select_by_value(option)

    
    def add_product_to_cart(self, product_name):
        products = self.wait.until(
            EC.presence_of_all_elements_located(self.inventory_item)
        )
    
        for product in products:
            name = product.find_element(
                By.CLASS_NAME, "inventory_item_name"
            ).text
    
            if name == product_name:
                product.find_element(
                    By.CSS_SELECTOR, "button.btn_inventory"
                ).click()
                return
    
        raise AssertionError(
            f"Product not found: {product_name}"
        )

    def get_cart_count(self):
        badges = self.driver.find_elements(*self.cart_badge)
        return int(badges[0].text) if badges else 0

    
    def open_cart(self):
        cart = self.wait.until(
            EC.element_to_be_clickable(self.cart_link)
        )
    
        cart.click()
    
        try:
            self.wait.until(
                EC.url_contains("cart.html")
            )
        except Exception:
            print("URL after cart click:", self.driver.current_url)
            print("Page title after cart click:", self.driver.title)
            print("Page source contains:", self.driver.page_source[:1000])
            raise





    