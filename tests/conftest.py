import pytest
from selenium import webdriver
from config import URL, RESOLUTION

def browser_settings():
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument(f'--window-size={RESOLUTION[0]},{RESOLUTION[1]}')
    return chrome_options


@pytest.fixture
def driver():
    chrome = webdriver.Chrome(options=browser_settings())
    chrome.get(URL)

    yield chrome

    chrome.quit()
