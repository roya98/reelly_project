from pages.base_page import Page
from selenium.webdriver.common.by import By


class Settings(Page):
    CONTACT_US = (By.CSS_SELECTOR, "a[href*='/contact-us'].page-setting-block.w-inline-block")

    def click_contact_us(self):
        self.click(self.CONTACT_US)
