from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class CommunityPage(Page):
    COMMUNITY = (By.CSS_SELECTOR, "a[href*='/community'].page-setting-block.w-inline-block")
    SUPPORT = (By.CSS_SELECTOR, ".support-fixed-button.w-inline-block")

    def click_community(self):
        self.click(self.COMMUNITY)

    def verify_community(self, str1):
        self.verify_right_page(str1)

    def button_available_clickable(self):
        self.driver.wait.until(EC.presence_of_element_located(self.SUPPORT))
        self.driver.wait.until(EC.element_to_be_clickable(self.SUPPORT))




