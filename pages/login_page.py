from locators.login_locators import USERNAME, PASSWORD, LOGIN_BUTTON
from pages.base_page import BasePage    

class LoginPage(BasePage):

    def __init__(self, driver):
         super().__init__(driver)

    def enter_username(self, username):
        self.send_keys(USERNAME, username)

    def enter_password(self, password):
        self.send_keys(PASSWORD, password)

    def click_login(self):
        self.click(LOGIN_BUTTON)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()