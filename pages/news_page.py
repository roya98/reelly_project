from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class News(Page):
    NEWS_URL = "https://t.me/reellydxb"

    def verify_news_page(self):
        self.verify_right_page(self.NEWS_URL)
