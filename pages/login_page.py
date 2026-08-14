from locators.login_locators import USERNAME, PASSWORD, LOGIN_BUTTON
from pages.base_page import BasePage 

from utils.wait_utils import WaitUtils

class LoginPage(BasePage):

    def __init__(self, driver):
         super().__init__(driver)
         self.wait = WaitUtils(driver)

    def enter_username(self, username):
        self.wait.wait_for_element_visible(USERNAME).send_keys(username)

    def enter_password(self, password):
        self.wait.wait_for_element_visible(PASSWORD).send_keys(password)

    def click_login(self):
        self.wait.wait_for_element_clickable(LOGIN_BUTTON).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()