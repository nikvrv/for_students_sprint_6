from selenium.webdriver.common.by import By


class MetroLocators:
    METRO_INPUT = By.XPATH, "//input[@class='select-search__input']"

    @staticmethod
    def get_metro_station_locator(metro_name):
        return (
            By.XPATH,
            f"//*[@class='select-search__select']//*[text()='{metro_name}']",
        )
