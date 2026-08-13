import pytest
from selenium import webdriver
from utils.config_reader import BROWSER

from utils.screenshot import capture_screenshot

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    setattr(item, "rep_" + report.when, report)


@pytest.fixture
def driver(request):
    if BROWSER.lower() == "chrome":
        driver = webdriver.Chrome()
    elif BROWSER.lower() == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {BROWSER}")
    driver.maximize_window()
    yield driver


    if request.node.rep_call.failed:
        capture_screenshot(driver, request.node.name)

    driver.quit()

