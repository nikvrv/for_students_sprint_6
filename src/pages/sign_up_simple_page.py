import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from src.locators.signup_page_locators import SignUpPageLocators


class SignUpPageSimple:

    _EMAIL_FIELD = By.XPATH, "//*[@id='email']"
    _PASSWORD_FIELD = By.XPATH, "//*[@id='password']"
    _SUBMIT_BUTTON = By.XPATH, "//button[contains(@class, 'auth')]"
    _EMAIL_HEADER = By.XPATH, "//p[contains(@class, 'user')]"
    _LOGOUT_BUTTON = By.XPATH, "//button[contains(@class, 'logout')]"


    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(f"{url}/signup")

    def enter_email(self, email):
        self.driver.find_element(*self._EMAIL_FIELD).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self._PASSWORD_FIELD).send_keys(password)

    def submit_button_click(self):
        self.driver.find_element(*self._SUBMIT_BUTTON).click()
