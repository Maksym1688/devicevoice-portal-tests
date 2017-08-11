import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def driver():
    return webdriver.Chrome()
