from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver import ActionChains

from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class Secondary(Page):
    SECONDARY = (By.CSS_SELECTOR, "a[href*='/secondary']")
    SECONDARY_URL = "https://soft.reelly.io/secondary-listings"
    FORWARD = (By.CSS_SELECTOR, "a.pagination__button.w-inline-block")
    TOTAL = (By.CSS_SELECTOR, "div.page-count[wized='totalPageProperties'][w-el-text='1']")
    CURRENT = (By.CSS_SELECTOR, "div.page-count[wized='currentPageProperties'][w-el-text='1']")
    BACK = (By.CSS_SELECTOR, "div.pagination__button")

    FILTER_BUTTON = (By.CSS_SELECTOR, "div.filter-button")
    SELL = (By.CSS_SELECTOR, "div.switcher-button.active")
    APPLY_FILTER = (By.CSS_SELECTOR, "a.button-filter.w-button")
    LISTING = (By.CSS_SELECTOR, "div.listing-card")
    LIST_SALE = (By.CSS_SELECTOR, "div[w-el-text='For sale']")

    def go_through_pages(self, number, navigation):
        for i in range(number):
            self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*navigation))
            self.driver.wait.until(EC.element_to_be_clickable(navigation))
            self.driver.wait.until(EC.element_to_be_clickable(navigation))
            self.driver.wait.until(EC.text_to_be_present_in_element(self.TOTAL, str(number)))
            self.click(navigation)

    def click_secondary_option(self):
        self.click(self.SECONDARY)

    def go_to_final_page(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.TOTAL))
        total_pages = self.driver.find_element(*self.TOTAL).text
        print(f'number of pages: {total_pages}')
        total_pages = int(total_pages)

        print(f'number of pages: {total_pages}')
        self.driver.wait.until(EC.element_to_be_clickable(self.FORWARD))

        self.go_through_pages(total_pages, self.FORWARD)
        sleep(3)
        self.driver.wait.until(EC.text_to_be_present_in_element(self.CURRENT, str(total_pages)))
        current_pages = self.driver.find_element(*self.CURRENT).text
        current_pages = int(current_pages)
        assert current_pages == total_pages, f'expected {total_pages} but got {current_pages}'

    def go_to_first(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.TOTAL))
        total_pages = self.driver.find_element(*self.TOTAL).text
        total_pages = int(total_pages)

        self.go_through_pages(total_pages, self.BACK)
        sleep(3)
        self.driver.wait.until(EC.text_to_be_present_in_element(self.CURRENT, "1"))
        current_pages = self.driver.find_element(*self.CURRENT).text
        current_pages = int(current_pages)
        assert current_pages == 1, f'expected {1} but got {current_pages}'

    def verify_secondary_page(self):
        self.verify_right_page(self.SECONDARY_URL)

    def click_on_filters_select_sells(self):
        # filter_button = self.driver.find_element(*self.FILTER_BUTTON)
        # self.driver.execute_script("arguments[0].click();", filter_button)
        element = self.driver.find_element(*self.FILTER_BUTTON)
        print(element)
        element.click()
        self.click(self.SELL)
        apply_filter = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.APPLY_FILTER))
        ActionChains(self.driver).move_to_element(apply_filter).click().perform()

    def verify_for_sale_listing(self):
        listing = self.driver.find_elements(*self.LISTING)
        for_sale_lists = self.driver.find_elements(*self.LIST_SALE)
        assert len(listing) == len(for_sale_lists), f'expected {len(listing)} == {len(for_sale_lists)} but they are not'

