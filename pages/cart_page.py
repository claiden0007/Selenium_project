
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.settings import DEFAULT_TIMEOUT


class CartPage:

    page_title = (By.CLASS_NAME, "title")
    cart_item_names = (By.CLASS_NAME, "inventory_item_name")
    cart_items = (By.CLASS_NAME, "cart_item")
    checkout_button = (By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, DEFAULT_TIMEOUT)

    def get_page_title(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.page_title)
        ).text

    def get_cart_product_names(self):
        items = self.driver.find_elements(*self.cart_item_names)
        return [item.text for item in items]

    def get_cart_item_count(self):
        return len(self.driver.find_elements(*self.cart_items))

    def remove_product(self, product_name):
        item_locator = (
            By.XPATH,
            f"//div[@class='cart_item'][.//div[@class='inventory_item_name' and text()='{product_name}']]"
        )

        item = self.wait.until(
            EC.visibility_of_element_located(item_locator)
        )

        item.find_element(By.TAG_NAME, "button").click()

    def click_checkout(self):
        self.wait.until(
            EC.element_to_be_clickable(self.checkout_button)
        ).click()
