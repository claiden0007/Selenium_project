
import logging
import os
from datetime import datetime

import pytest
from selenium import webdriver

from config.settings import BROWSER, LOGS_DIR, SCREENSHOTS_DIR, REPORTS_DIR

os.makedirs(LOGS_DIR, exist_ok=True)
os.makedirs(SCREENSHOTS_DIR, exist_ok=True)
os.makedirs(REPORTS_DIR, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(LOGS_DIR, "test_execution.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True,
)


@pytest.fixture
def driver(request):
    logging.info("Starting browser for test: %s", request.node.name)

    if BROWSER.lower() == "chrome":
        options = webdriver.ChromeOptions()
        if os.getenv("CI") == "true":
            options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--start-maximized")
        options.add_experimental_option(
            "prefs",
            {
                "credentials_enable_service": False,
                "profile.password_manager_enabled": False,
            },
        )
        browser = webdriver.Chrome(options=options)
    else:
        raise ValueError(f"Unsupported browser: {BROWSER}")

    yield browser

    report = getattr(request.node, "rep_call", None)

    if report and report.failed:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_name = f"{request.node.name}_{timestamp}.png"
        screenshot_path = os.path.join(
            SCREENSHOTS_DIR, screenshot_name
        )

        try:
            browser.save_screenshot(screenshot_path)
            logging.error(
                "Test failed. Screenshot saved: %s",
                screenshot_path,
            )
        except Exception:
            logging.exception("Could not save failure screenshot")

    browser.quit()
    logging.info("Browser closed for test: %s", request.node.name)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)
