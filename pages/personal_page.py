from pages.base_page import Page
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class Personal(Page):
    YEAR_JOINED = (By.ID, "When-joined-company-2")
    LANGUAGE = (By.ID, "Languages")
    year = "2020"
    language = "English"

    CLOSE_BUTTON = (By.CSS_SELECTOR, "div.profile-button-block a[href*='/settings'].close-button.w-button")
    SAVE_CHANGES = (By.XPATH, "//div[@class='profile-button-block']//div[@class='save-changes-button']")

    def enter_test_info(self):
        sleep(1)
        self.input_text(self.year, self.YEAR_JOINED)
        self.input_text(self.language, self.LANGUAGE)

    def verify_input_fields(self):
        variable_year = self.get_variable_text(self.YEAR_JOINED)
        variable_language = self.get_variable_text(self.LANGUAGE)
        assert variable_year == self.year, f'expected {self.year} but got {variable_year}'
        assert variable_language == self.language, f'expected {self.language} but got {variable_language}'

    def check_button_are_visible(self):
        self.driver.wait.until(EC.element_to_be_clickable(self.CLOSE_BUTTON))
        self.driver.wait.until(EC.element_to_be_clickable(self.SAVE_CHANGES))
