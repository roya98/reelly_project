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




