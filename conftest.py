import pytest
import allure
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

@pytest.fixture(scope="function")
def driver():
    options = Options()
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    yield driver
    if hasattr(driver, 'failed'):
        allure.attach(driver.get_screenshot_as_png(), name="screenshot on failure", attachment_type=allure.attachment_type.PNG)
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        if 'driver' in item.fixturenames:
            driver = item.funcargs['driver']
            driver.failed = True