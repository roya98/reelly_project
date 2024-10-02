from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException

from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class Secondary(Page):
    SECONDARY = (By.CSS_SELECTOR, "a[href*='/secondary']")
    SECONDARY_URL = "https://soft.reelly.io/secondary-listings"
    FORWARD = (By.CSS_SELECTOR, "a.pagination__button.w-inline-block")
    TOTAL = (By.CSS_SELECTOR, "div.page-count[wized='totalPageProperties'][w-el-text='1']")
    CURRENT = (By.CSS_SELECTOR, "div.page-count[wized='currentPageProperties'][w-el-text='1']")
    BACK = (By.CSS_SELECTOR, "div.pagination__button")

    def click_secondary_option(self):
        self.click(self.SECONDARY)

    def go_to_final_page(self):

        self.driver.wait.until(EC.text_to_be_present_in_element(self.TOTAL, "97"))
        total_pages = self.driver.find_element(*self.TOTAL).text
        total_pages = int(total_pages)
        print(f'number of pages: {total_pages}')
        self.driver.wait.until(EC.element_to_be_clickable(self.FORWARD))
        for i in range(total_pages):
            self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*self.FORWARD))
            self.driver.wait.until(EC.element_to_be_clickable(self.FORWARD))
            self.driver.wait.until(EC.element_to_be_clickable(self.FORWARD))
            self.driver.wait.until(EC.text_to_be_present_in_element(self.TOTAL, "97"))
            self.click(self.FORWARD)
        sleep(10)
        self.driver.wait.until(EC.text_to_be_present_in_element(self.CURRENT, "97"))
        current_pages = self.driver.find_element(*self.CURRENT).text
        current_pages = int(current_pages)
        assert current_pages == total_pages, f'expected {total_pages} but got {current_pages}'

    def go_to_first(self):
     self.driver.wait.until(EC.text_to_be_present_in_element(self.TOTAL, "97"))
     self.driver.wait.until(EC.element_to_be_clickable(self.BACK))
     for i in range(97):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*self.BACK))
        self.driver.wait.until(EC.element_to_be_clickable(self.BACK))
        self.driver.wait.until(EC.element_to_be_clickable(self.BACK))
        self.driver.wait.until(EC.text_to_be_present_in_element(self.TOTAL, "97"))
        self.click(self.BACK)
     sleep(10)
     self.driver.wait.until(EC.text_to_be_present_in_element(self.CURRENT, "1"))
     current_pages = self.driver.find_element(*self.CURRENT).text
     current_pages = int(current_pages)
     assert current_pages == 1, f'expected {1} but got {current_pages}'

    def verify_secondary_page(self):
        self.verify_right_page(self.SECONDARY_URL)
