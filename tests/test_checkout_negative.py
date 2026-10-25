from tabnanny import check

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

from test_data.test_users import (
    VALID_PASSWORD, 
    VALID_USERNAME,
    FIRST_NAME,
    LAST_NAME,
    POSTAL_CODE,
    )

def navigate_to_checkout(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.enter_username(VALID_USERNAME)
    login_page.enter_password(VALID_PASSWORD)
    login_page.click_login()

    inventory_page = InventoryPage(driver)
    inventory_page.add_product_to_cart("Sauce Labs Backpack")
    inventory_page.open_cart()

    cart_page = CartPage(driver)
    cart_page.click_checkout()

def test_check_without_first_name(driver):
    navigate_to_checkout(driver)
    checkout_page = CheckoutPage(driver)

    checkout_page.enter_last_name("Tester")
    checkout_page.enter_zip_code("673579")
    checkout_page.click_continue()

    assert "First Name is required" in checkout_page.get_error_message()

def test_checkout_without_lastpage(driver):
    navigate_to_checkout(driver)
    checkout_page = CheckoutPage(driver)

    checkout_page.enter_first_name("Claiden")
    checkout_page.enter_zip_code("675647")
    checkout_page.click_continue()

    assert "Last Name is required" in checkout_page.get_error_message()

def test_checkout_without_postal_code(driver):
    navigate_to_checkout(driver)
    checkout_page = CheckoutPage(driver)

    checkout_page.enter_first_name("Claiden")
    checkout_page.enter_last_name("Tester")
    checkout_page.click_continue()

    assert "Postal Code is required" in checkout_page.get_error_message()



