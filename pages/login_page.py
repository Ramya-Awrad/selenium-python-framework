from locators.login_locators import USERNAME, PASSWORD, LOGIN_BUTTON    

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(*USERNAME).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(*PASSWORD).send_keys(password)

    def click_login(self):
        self.driver.find_element(*LOGIN_BUTTON).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()