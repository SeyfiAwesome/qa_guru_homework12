import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import browser

from utils import attaches


@pytest.fixture(autouse=True)
def browser_management():
    options = Options()
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-notifications")

    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "128.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser.config.driver = driver
    browser.config.timeout = 10

    yield

    attaches.add_screenshot(driver)
    attaches.add_page_source(driver)
    attaches.add_logs(driver)
    attaches.add_video(driver)

    browser.quit()
