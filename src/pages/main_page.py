
from src.locators.signup_page_locators import SignUpPageLocators
from src.pages.base_page import BasePage


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def logout_button_is_displayed(self):
        logout_button = self.find_element(SignUpPageLocators.LOGOUT_BUTTON)
        return logout_button.is_displayed()
