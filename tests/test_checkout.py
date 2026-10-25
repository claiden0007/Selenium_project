
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

def test_checkout_information(driver):
    navigate_to_checkout(driver)
    checkout_page = CheckoutPage(driver)

    checkout_page.fill_checkout_information(FIRST_NAME, LAST_NAME, POSTAL_CODE)
    checkout_page.click_continue()

    assert checkout_page.get_page_title() == "Checkout: Overview"
    assert "Item total:" in checkout_page.get_item_total()
    assert "Tax:" in checkout_page.get_tax_total()
    assert "Total:" in checkout_page.get_total_price()

def test_complete_order(driver):
    navigate_to_checkout(driver)
    checkout_page = CheckoutPage(driver)

    checkout_page.fill_checkout_information(FIRST_NAME, LAST_NAME, POSTAL_CODE)
    checkout_page.click_continue()
    checkout_page.click_finish()

    assert checkout_page.get_confirmation_message() == "Thank you for your order!"

    


