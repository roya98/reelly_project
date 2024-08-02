from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ConnectCompany(Page):
    CONNECT_COMPANY = (By.CSS_SELECTOR, "a[href*='/book-presentation']")
    PAGE = "https://soft.reelly.io/book-presentation"

    def click_connect_company(self):
        self.click(self.CONNECT_COMPANY)

    def switch_window(self):
        original_window = self.driver.current_window_handle
        self.driver.wait.until(EC.new_window_is_opened)
        current_windows = self.driver.window_handles
        self.driver.switch_to.window(current_windows[1])

    def verify_page(self):
        self.verify_right_page(self.PAGE)
