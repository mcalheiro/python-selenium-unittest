from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class BasePageElement:
    WAIT_TIMEOUT = 10 # seconds
    def __set__(self, obj, value) -> None:
        driver = obj.driver
        WebDriverWait(driver, self.WAIT_TIMEOUT).until(
            lambda driver: driver.find_element(By.NAME, self.locator))
        driver.find_element(By.NAME, self.locator).clear()
        driver.find_element(By.NAME, self.locator).send_keys(value)

    def __get__(self, obj, owner) -> any:
        driver = obj.driver
        WebDriverWait(driver, self.WAIT_TIMEOUT).until(
            lambda driver: driver.find_element(By.NAME, self.locator))
        element = driver.find_element(By.NAME, self.locator)
        return element.get_attribute('value')
