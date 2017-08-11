import pytest
from selenium import webdriver

from tests.test_auth import login


@pytest.fixture(scope='session')
def auth_driver(variables):
    driver = webdriver.Chrome()
    login(driver, variables)
    yield driver
    driver.quit()


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
