from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from src.config import URL
from src.helpers import get_sign_up_data
from src.locators.signup_page_locators import SignUpPageLocators
from src.pages.main_page import MainPage
from src.pages.sign_up_simple_page import SignUpPageSimple
from src.pages.signup_page import SignUpPage

from src.pages.successful_signup_popup import SuccessfulSignupPopup
from allure import title, step, suite

@suite("Registration")
class TestMestoRegistration:

    def test_signup(self, driver, login):
        driver.get(f"{URL}/signup")
        email_data, password_data = get_sign_up_data()

        driver.find_element(*SignUpPageLocators.EMAIL_FIELD).send_keys(email_data)

        driver.find_element(*SignUpPageLocators.PASSWORD_FIELD).send_keys(password_data)

        driver.find_element(*SignUpPageLocators.SUBMIT_BUTTON).click()

        logout_button = WebDriverWait(driver, 15).until(
            expected_conditions.visibility_of_element_located(
                SignUpPageLocators.LOGOUT_BUTTON
            )
        )
        assert logout_button.is_displayed()
        assert logout_button.is_enabled()

    def test_sign_pom_simple(self, driver):
        email, password = get_sign_up_data()
        sign_up_page = SignUpPageSimple(driver)
        sign_up_page.open_page(URL)
        sign_up_page.enter_email(email)
        sign_up_page.enter_password(password)
        sign_up_page.submit_button_click()

        main_page = MainPage(driver)
        assert main_page.logout_button_is_displayed() is True, "Button is not shown"

    @title("Sign up")
    def test_signup_pom(self, driver):
        email_data, password_data = get_sign_up_data()
        sign_up_page = SignUpPage(driver)
        sign_up_page.open_page(URL)
        sign_up_page.enter_email(email_data)
        sign_up_page.enter_password(password_data)
        sign_up_page.submit_button_click()

        modal = SuccessfulSignupPopup(driver)
        assert modal.get_label_text() == modal.SIGNUP_TEXT
