import time

from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class OffPlan(Page):
    OFF_PLAN = (By.CSS_SELECTOR, ".menu-twobutton")
    OFF_PLAN_TITLE = (By.CSS_SELECTOR, ".menu-text-link-leaderboard.w--current")
    PICTURES = (By.CSS_SELECTOR, ".project-image")
    TITLES = (By.CSS_SELECTOR, ".project-name")

    def click_on_off_plan(self):
        self.click(self.OFF_PLAN)

    def verify_off_plan_page_opens(self):
        title = self.get_text(self.OFF_PLAN_TITLE)
        assert title == 'Off-plan', f'expecting Off-plan but got {title}'

    def verify_element_picture_title(self):
        time.sleep(3)
        images = self.driver.find_elements(*self.PICTURES)
        titles = self.driver.find_elements(*self.TITLES)
        assert len(images) == len(titles), f'found {len(images)} images and {len(titles)} titles'


