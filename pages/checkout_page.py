
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.settings import DEFAULT_TIMEOUT


class CheckoutPage:

    first_name_input = (By.ID, "first-name")
    last_name_input = (By.ID, "last-name")
    postal_code_input = (By.ID, "postal-code")
    continue_button = (By.ID, "continue")
    cancel_button = (By.ID, "cancel")
    error_message = (By.CSS_SELECTOR, "[data-test='error']")

    page_title = (By.CLASS_NAME, "title")
    item_total = (By.CLASS_NAME, "summary_subtotal_label")
    tax_total = (By.CLASS_NAME, "summary_tax_label")
    total_price = (By.CLASS_NAME, "summary_total_label")
    finish_button = (By.ID, "finish")

    confirmation_message = (By.CLASS_NAME, "complete-header")
    back_home_button = (By.ID, "back-to-products")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, DEFAULT_TIMEOUT)

    def enter_first_name(self, first_name):
        self.wait.until(
            EC.visibility_of_element_located(self.first_name_input)
        ).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.wait.until(
            EC.visibility_of_element_located(self.last_name_input)
        ).send_keys(last_name)

    def enter_zip_code(self, zip_code):
        self.wait.until(
            EC.visibility_of_element_located(self.postal_code_input)
        ).send_keys(zip_code)

    def fill_checkout_information(self, first_name, last_name, zip_code):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_zip_code(zip_code)

    def click_continue(self):
        self.wait.until(
            EC.element_to_be_clickable(self.continue_button)
        ).click()

    def click_cancel(self):
        self.wait.until(
            EC.element_to_be_clickable(self.cancel_button)
        ).click()

    def get_error_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.error_message)
        ).text

    def get_page_title(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.page_title)
        ).text

    def get_item_total(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.item_total)
        ).text

    def get_tax_total(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.tax_total)
        ).text

    def get_total_price(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.total_price)
        ).text

    def click_finish(self):
        self.wait.until(
            EC.element_to_be_clickable(self.finish_button)
        ).click()

    def get_confirmation_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.confirmation_message)
        ).text

    def click_back_home(self):
        self.wait.until(
            EC.element_to_be_clickable(self.back_home_button)
        ).click()
