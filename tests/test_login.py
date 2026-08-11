from pages.login_page import LoginPage
from utils.config_reader import URL

def test_login(driver):
    driver.get(URL)

    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

