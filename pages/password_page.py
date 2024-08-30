from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Password(Page):
    PASSWORD_URL = 'https://soft.reelly.io/set-new-password'
    PASSWORD1 = (By.ID, "Enter-new-password")
    PASSWORD2 = (By.ID, "Repeat-password")
    PASSWORD_BUTTON = (By.CSS_SELECTOR, ".submit-button-2.w-button")

    password_to_enter = "new_pass_test"

    def verify_password_change_page(self):
        self.verify_right_page(self.PASSWORD_URL)

    def password_data(self):
        self.input_text(self.password_to_enter, self.PASSWORD1)
        self.input_text(self.password_to_enter, self.PASSWORD2)

    def verify_button(self):
        self.driver.wait.until(EC.presence_of_element_located(self.PASSWORD_BUTTON))

