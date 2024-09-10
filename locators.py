from selenium.webdriver.common.by import By


class MestoLocators:
    EMAIL_FIELD = By.XPATH, "//*[@id='email']"
    PASSWORD_FIELD = By.XPATH, "//*[@id='password']"
    SUBMIT_BUTTON = By.XPATH, "//button[contains(@class, 'auth')]"
    EMAIL_HEADER = By.XPATH, "//p[contains(@class, 'user')]"
    LOGOUT_BUTTON = By.XPATH, "//button[contains(@class, 'logout')]"


class MetroLocators:
    METRO_INPUT = By.XPATH, "//input[@class='select-search__input']"

    @staticmethod
    def get_metro_station_locator(metro_name):
        return By.XPATH, f"//*[@class='select-search__select']//*[text()='{metro_name}']"

