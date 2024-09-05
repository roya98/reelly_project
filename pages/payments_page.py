from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Payment(Page):
    PAYMENT_URL = 'https://soft.reelly.io/subscription'
    PAYMENT_TITLE = (By.CSS_SELECTOR, "div.lotion-your-h3--price.size")
    UPGRADE_BUTTON = (By.CSS_SELECTOR, "a[wized='upgradePlanButton']")
    BACK_BUTTON = (By.CSS_SELECTOR, "a.button-verify.margin-top-8.white.w-inline-block")

    def verify_payment_page(self):
        self.verify_right_page(self.PAYMENT_URL)

    def payment_title_visibility(self):
        self.driver.wait.until(EC.presence_of_element_located(self.PAYMENT_TITLE))

    def back_and_upgrade_buttons(self):
        self.driver.wait.until(EC.presence_of_element_located(self.UPGRADE_BUTTON))
        self.driver.wait.until(EC.presence_of_all_elements_located(self.BACK_BUTTON))
