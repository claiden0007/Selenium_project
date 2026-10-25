
from pages.login_page import LoginPage
from test_data.test_users import (
    VALID_PASSWORD,
    VALID_USERNAME,
    INVALID_PASSWORD,
    INVALID_USERNAME,
    LOCKED_PASSWORD,
    LOCKED_USERNAME,
)


def test_invalid_username(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.enter_username(INVALID_USERNAME)
    login_page.enter_password(INVALID_PASSWORD)
    login_page.click_login()

    assert "Username and password do not match" in login_page.get_error_message()


def test_invalid_password(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.enter_username(VALID_USERNAME)
    login_page.enter_password(INVALID_PASSWORD)
    login_page.click_login()

    assert "Username and password do not match" in login_page.get_error_message()


def test_locked_out_user(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.enter_username(LOCKED_USERNAME)
    login_page.enter_password(LOCKED_PASSWORD)
    login_page.click_login()

    assert "locked out" in login_page.get_error_message().lower()
