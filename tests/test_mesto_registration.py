from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from config import URL
from locators import MestoLocators
from helpers import get_sign_up_data
from src.signup_page import SignUpPage
from src.successful_signup_popup import SuccessfulSignupPopup
import allure


class TestMestoRegistration:

    def test_signup(self, driver):
        driver.get(f'{URL}/signup')
        email_data, password_data = get_sign_up_data()

        driver.find_element(*MestoLocators.EMAIL_FIELD).send_keys(email_data)

        driver.find_element(*MestoLocators.PASSWORD_FIELD).send_keys(password_data)

        driver.find_element(*MestoLocators.SUBMIT_BUTTON).click()

        logout_button = WebDriverWait(driver, 15).until(
            expected_conditions.visibility_of_element_located(MestoLocators.LOGOUT_BUTTON))
        assert logout_button.is_displayed()
        assert logout_button.is_enabled()

    @allure.title('Signup')
    def test_signup_pom(self, driver):
        email_data, password_data = get_sign_up_data()
        sign_up_page = SignUpPage(driver)
        sign_up_page.open_page(URL)
        sign_up_page.enter_email(email_data)
        sign_up_page.enter_password(password_data)
        sign_up_page.submit_button_click()

        modal = SuccessfulSignupPopup(driver)

        assert modal.get_text() == modal.SIGNUP_TEXT
