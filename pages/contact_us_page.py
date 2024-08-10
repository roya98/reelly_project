from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class CONTACT(Page):
    ICONS = (By.CSS_SELECTOR, "div.social-button")
    CONNECT_COMPANY = (By.CSS_SELECTOR, "a[href*='/book-presentation'].button-link-menu._1.w-inline-block")

    def verify_contact_page(self):
        self.verify_right_page('contact-us')

    def verify_social_icons(self):
        icons_list = self.driver.find_elements(*self.ICONS)
        assert len(icons_list) >= 4, f'Needed at list 4 but got {len(icons_list)}'

    def verify_connect_company(self):
        self.driver.wait.until(EC.element_to_be_clickable(self.CONNECT_COMPANY))

