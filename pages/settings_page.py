from pages.base_page import Page
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC


class Settings(Page):
    CONTACT_US = (By.CSS_SELECTOR, "a[href*='/contact-us'].page-setting-block.w-inline-block")
    USER_GUIDE = (By.CSS_SELECTOR, "a[href*='/user-guide'].page-setting-block")
    CHANGE_PASSWORD = (By.CSS_SELECTOR, "a[href*='/set-new-password']")
    PAYMENTS = (By.CSS_SELECTOR, "a[href*='/subscription']")
    SUPPORT = (By.CSS_SELECTOR, "a[href*='https://api.whatsapp.com/send?phone=9715680983']")
    NEWS = (By.CSS_SELECTOR, "a[href*='https://t.me/reellydxb'].page-setting-block.w-inline-block")

    def click_contact_us(self):
        self.click(self.CONTACT_US)

    def click_on_user_guide(self):
        self.click(self.USER_GUIDE)

    def click_password_change(self):
        self.click(self.CHANGE_PASSWORD)

    def click_on_subscription_payment(self):
        self.click(self.PAYMENTS)

    def click_on_support(self):
        self.click(self.SUPPORT)

    def switch_to_support_window(self):
        current_window = self.driver.current_window_handle
        windows = self.driver.window_handles
        self.driver.wait.until(EC.new_window_is_opened)
        self.driver.switch_to.window(windows[1])

    def go_back_to_settings_page(self):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[0])

    def click_on_news_option(self):
        self.click(self.NEWS)
        self.driver.wait.until(EC.new_window_is_opened)
