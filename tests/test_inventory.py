from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from test_data.test_users import VALID_USERNAME, VALID_PASSWORD


def login_as_valid_user(driver):
    login_page = LoginPage(driver)

    login_page.open()
    login_page.enter_username(VALID_USERNAME)
    login_page.enter_password(VALID_PASSWORD)
    login_page.click_login()

def test_products_are_displayed(driver):
    login_as_valid_user(driver)
    inventory_page = InventoryPage(driver)

    assert inventory_page.get_page_title() == "Products"
    assert inventory_page.get_product_count() > 0
    assert len(inventory_page.get_product_names()) > 0

def test_sort_products_by_name_ascending(driver):
    login_as_valid_user(driver)
    inventory_page = InventoryPage(driver)

    inventory_page.sort_products("az")
    product_names = inventory_page.get_product_names()

    assert product_names == sorted(product_names)

def test_add_product_to_cart(driver):
    login_as_valid_user(driver)
    inventory_page = InventoryPage(driver)

    inventory_page.add_product_to_cart("Sauce Labs Backpack")

    assert inventory_page.get_cart_count() == 1






