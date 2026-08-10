class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        self.driver.find_element(*locator).click()

    def send_keys(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)