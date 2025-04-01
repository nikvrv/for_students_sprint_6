import time


from selenium.webdriver.common.by import By


from src.locators.metro_page_locators import MetroLocators


class TestMetro:

    def test_metro(self, driver):

        driver.get(f"https://qa-scooter.praktikum-services.ru/order")

        driver.find_element(
            By.XPATH, "(//*[contains(@class, 'Order')]//input[@type='text'])[1]"
        ).send_keys("Джон")
        driver.find_element(
            By.XPATH, "(//*[contains(@class, 'Order')]//input[@type='text'])[2]"
        ).send_keys("Марстон")
        driver.find_element(
            By.XPATH, "(//*[contains(@class, 'Order')]//input[@type='text'])[3]"
        ).send_keys("Ленина 10")
        driver.find_element(
            By.XPATH, "(//*[contains(@class, 'Order')]//input[@type='text'])[4]"
        ).send_keys("+79314001212")
        metro_name = "Войковская"

        driver.find_element(*MetroLocators.METRO_INPUT).send_keys(metro_name)
        driver.find_element(
            *MetroLocators.get_metro_station_locator(metro_name)
        ).click()

        driver.find_element(By.XPATH, "//button[text()='Далее']").click()
        time.sleep(10)
