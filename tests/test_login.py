
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from test_data.test_users import VALID_USERNAME, VALID_PASSWORD

def test_successfull_login(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open()
    login_page.enter_username(VALID_USERNAME)
    login_page.enter_password(VALID_PASSWORD)
    login_page.click_login()

    assert inventory_page.get_page_title() == "Products"
    assert inventory_page.get_product_count() > 0

    
