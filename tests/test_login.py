from pages.login_page import LoginPage
from utils.config_reader import URL

from utils.logger import logger

def test_login(driver):
    logger.info("Starting login test")
    driver.get(URL)
    logger.info("Opened SauceDemo application")


    login_page = LoginPage(driver)
    logger.info("LoginPage object created")
    
    login_page.login("standard_user", "secret_sauce")
    logger.info("Login completed successfully")

