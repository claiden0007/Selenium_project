
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage

from test_data.test_users import VALID_PASSWORD, VALID_USERNAME


def login_and_add_product(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.enter_username(VALID_USERNAME)
    login_page.enter_password(VALID_PASSWORD)
    login_page.click_login()

    inventory_page = InventoryPage(driver)
    inventory_page.add_product_to_cart("Sauce Labs Backpack")
    inventory_page.open_cart()


def test_cart_displays_added_product(driver):
    login_and_add_product(driver)
    cart_page = CartPage(driver)

    assert cart_page.get_page_title() == "Your Cart"
    assert "Sauce Labs Backpack" in cart_page.get_cart_product_names()
    assert cart_page.get_cart_item_count() == 1


def test_remove_product_from_cart(driver):
    login_and_add_product(driver)
    cart_page = CartPage(driver)

    cart_page.remove_product("Sauce Labs Backpack")

    assert cart_page.get_cart_item_count() == 0
    assert cart_page.get_cart_product_names() == []
