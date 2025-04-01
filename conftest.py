import tempfile

import allure
import pytest
from selenium import webdriver
from src.config import URL, RESOLUTION


def browser_settings():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless=new')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument(f'--user-data-dir={tempfile.mkdtemp()}')
    # chrome_options.add_argument(f'--window-size={RESOLUTION[0]},{RESOLUTION[1]}')
    return chrome_options


@pytest.fixture
def driver():
    chrome = webdriver.Chrome(options=browser_settings())
    chrome.get(URL)
    yield chrome
    chrome.quit()


@pytest.fixture
def login(driver):
    login_page = LoginPage(driver)
    login_page.navigate()
    login_page.enter_email()
    login_page.enter_password()
    login_page.click_submit()
