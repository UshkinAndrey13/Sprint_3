import pytest
from selenium import webdriver

url = 'https://stellarburgers.nomoreparties.site'


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    yield driver
    driver.quit()