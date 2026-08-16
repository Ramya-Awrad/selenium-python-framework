from pages.login_page import LoginPage
from utils.config_reader import URL

from utils.logger import logger
from utils.json_reader import read_json

def test_login(driver):
    logger.info("Starting login test")
    driver.get(URL)
    login_data = read_json("testdata/login_data.json")
    logger.info("Opened SauceDemo application")


    login_page = LoginPage(driver)
    logger.info("LoginPage object created")
    
    login_page.login(login_data["username"], login_data["password"])
    logger.info("Login completed successfully")

