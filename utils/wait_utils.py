from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WaitUtils:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    def wait_for_element_visible(self, locator):
        return WebDriverWait(
            self.driver,
            self.timeout
        ).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_element_clickable(self, locator):
        return WebDriverWait(
            self.driver,
            self.timeout
        ).until(
            EC.element_to_be_clickable(locator)
        )

    def wait_for_element_present(self, locator):
        return WebDriverWait(
            self.driver,
            self.timeout
        ).until(
            EC.presence_of_element_located(locator)
        )