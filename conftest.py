import pytest
from selenium import webdriver
from utils.config_reader import BROWSER

@pytest.fixture
def driver():
    if BROWSER.lower() == "chrome":
        driver = webdriver.Chrome()
    elif BROWSER.lower() == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {BROWSER}")
    driver.maximize_window()
    yield driver
    driver.quit()

