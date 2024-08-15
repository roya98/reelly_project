from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class UserGuide(Page):
    USER_GUIDE_URL = "https://soft.reelly.io/user-guide"
    VIDEOS = (By.CSS_SELECTOR, ".ytp-large-play-button-red-bg")
    LESSON_TITLES = (By.CSS_SELECTOR, "a.ytp-title-link.yt-uix-sessionlink")
    VIDEO_BLOCK = (By.CSS_SELECTOR, "div.video-block")
    IFRAME = (By.CSS_SELECTOR, "div.video-2.w-video.w-embed iframe.embedly-embed")
    SECOND_IFRAME = (By.ID, "player")

    def verify_user_guide_opens(self):
        self.verify_right_page(self.USER_GUIDE_URL)

    def verify_lesson_titles(self):
        iframe = self.driver.find_element(*self.IFRAME)
        self.driver.switch_to.frame(iframe)
        second_iframe = self.driver.find_element(*self.SECOND_IFRAME)
        self.driver.switch_to.frame(second_iframe)
        titles = self.driver.find_elements(*self.LESSON_TITLES)
        for title in titles:
            element_text = title.text
            print(element_text)
            assert element_text != "", f'No text is given {element_text}'

