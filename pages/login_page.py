
from selenium.webdriver.common.by import By
from config.settings import BASE_URL

class LoginPage:


    username_input = (By.ID, "user-name")
    password_input = (By.ID, "password")
    login_button = (By.ID, "login-button")
    error_message = (By.CSS_SELECTOR, "[data-test='error']")


    def __init__(self, driver):
            self.driver = driver

    def open(self):
        self.driver.get(BASE_URL)

    def enter_username(self, username):
        self.driver.find_element(*self.username_input).clear()
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).clear()
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def get_error_message(self):
        return self.driver.find_element(*self.error_message).text

    def is_login_page_displayed(self):
         return self.driver.find_element(*self.login_button).is_displayed()


        

