from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def navigate(self, url: str):
        self.driver.get(url)

    def find_element(self, locator: tuple, timeout: int = 10):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            print(f"Element with locator {locator} not found within {timeout} seconds.")
            return None

    def find_elements(self, locator: tuple, timeout: int = 10):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
        except TimeoutException:
            print(f"Elements with locator {locator} not found within {timeout} seconds.")
            return []

    def click_element(self, locator: tuple, timeout: int = 10):
        element = self.find_element(locator, timeout)
        if element:
            element.click()
        else:
            print(f"Failed to click on element with locator {locator}.")

    def enter_text(self, locator: tuple, text: str, timeout: int = 10):
        element = self.find_element(locator, timeout)
        if element:
            element.clear()
            element.send_keys(text)
        else:
            print(f"Failed to enter text in element with locator {locator}.")

    def wait_for_element_visible(self, locator: tuple, timeout: int = 10):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            print(f"Element with locator {locator} not visible after {timeout} seconds.")
            return None

    def element_is_present(self, locator: tuple, timeout: int = 10):
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False
