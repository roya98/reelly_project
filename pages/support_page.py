from pages.base_page import Page
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC


class Support(Page):

    SUPPORT_URL = "https://api.whatsapp.com/"

    def verify_support(self):
        self.verify_right_page(self.SUPPORT_URL)
