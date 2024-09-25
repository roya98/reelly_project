from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
class Page:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        self.driver.find_element(*locator).click()

    def input_text(self, text, locator):
        self.driver.find_element(*locator).send_keys(text)

    def get_text(self, locator):
        locator_text = self.driver.find_element(*locator).text
        return locator_text

    def get_variable_text(self, locator):
        element = self.driver.find_element(*locator)
        element_text = element.get_attribute('value')
        return element_text

    def verify_text(self, expected_result, locator):
        actual_text = self.get_text(locator)
        assert str(actual_text) == str(expected_result), f'Error expected {expected_result} but got {actual_text}'

    def verify_right_page(self, string):
        self.driver.wait.until(EC.url_contains(string))








