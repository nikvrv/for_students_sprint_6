import allure

from src.base_page import BasePage
from selenium.webdriver.common.by import By


class SignUpPage(BasePage):

    _EMAIL_FIELD = By.XPATH, "//*[@id='email']"
    _PASSWORD_FIELD = By.XPATH, "//*[@id='password']"
    _SUBMIT_BUTTON = By.XPATH, "//button[contains(@class, 'auth')]"

    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self, url):
        with allure.step("Open page"):
            self.navigate(f"{url}/signup")

    def enter_email(self, email):
        with allure.step(f"Enter email {email}"):
            self.enter_text(self._EMAIL_FIELD, email)

    def enter_password(self, password):
        with allure.step(f"Enter password {password}"):
            self.enter_text(self._PASSWORD_FIELD, password)

    def submit_button_click(self):
        with allure.step("Click submit button"):
            self.click_element(self._SUBMIT_BUTTON)
