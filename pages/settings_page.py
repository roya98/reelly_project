from pages.base_page import Page
from selenium.webdriver.common.by import By


class Settings(Page):
    CONTACT_US = (By.CSS_SELECTOR, "a[href*='/contact-us'].page-setting-block.w-inline-block")
    USER_GUIDE = (By.CSS_SELECTOR, "a[href*='/user-guide'].page-setting-block")
    CHANGE_PASSWORD = (By.CSS_SELECTOR, "a[href*='/set-new-password']")

    def click_contact_us(self):
        self.click(self.CONTACT_US)

    def click_on_user_guide(self):
        self.click(self.USER_GUIDE)

    def click_password_change(self):
        self.click(self.CHANGE_PASSWORD)

