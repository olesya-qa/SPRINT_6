import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from data import BASE_URL


@pytest.fixture
def driver():
    options = Options()
    options.add_argument('--width=1920')
    options.add_argument('--height=1080')
    browser = webdriver.Firefox(options=options)
    browser.maximize_window()
    browser.get(BASE_URL)
    yield browser
    browser.quit()
