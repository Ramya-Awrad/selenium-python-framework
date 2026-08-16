import pytest
from pages.login_page import LoginPage
from utils.config_reader import URL

from utils.logger import logger
from utils.json_reader import read_json

test_data = read_json("testdata/login_data.json")

@pytest.mark.parametrize("login_data", test_data)
def test_login(driver, login_data):
    logger.info("Starting login test")
    driver.get(URL)
    logger.info("Opened SauceDemo application")


    login_page = LoginPage(driver)
    logger.info("LoginPage object created")
    
    login_page.login(login_data["username"], login_data["password"])
    logger.info("Login completed successfully")

