import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import browser
from selene.support.shared import config

from utils import attaches


@pytest.fixture(autouse=True)
def browser_management():
    options = Options()
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-notifications")

    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options,
    )

    browser.config.driver = driver
    browser.config.timeout = 10

    yield

    attaches.add_screenshot(driver)
    attaches.add_page_source(driver)
    attaches.add_logs(driver)

    browser.quit()
