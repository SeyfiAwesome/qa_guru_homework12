import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import browser
from selene.support.shared import config


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

    browser.quit()