from selenium.webdriver.common.by import By


class MestoLocators:
    EMAIL_FIELD = By.XPATH, "//*[@id='email']"
    PASSWORD_FIELD = By.XPATH, "//*[@id='password']"
    SUBMIT_BUTTON = By.XPATH, "//button[contains(@class, 'auth')]"
    EMAIL_HEADER = By.XPATH, "//p[contains(@class, 'user')]"
    LOGOUT_BUTTON = By.XPATH, "//button[contains(@class, 'logout')]"
