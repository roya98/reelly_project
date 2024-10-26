from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver import ActionChains

from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class Secondary(Page):
    SECONDARY = (By.CSS_SELECTOR, "a[href*='/secondary']")
    SECONDARY_URL = "https://soft.reelly.io/secondary-listings"
    FORWARD = (By.CSS_SELECTOR, "a.pagination__button.w-inline-block")
    TOTAL = (By.CSS_SELECTOR, "div.page-count[wized='totalPageProperties'][w-el-text='1']")
    CURRENT = (By.CSS_SELECTOR, "div.page-count[wized='currentPageProperties'][w-el-text='1']")
    BACK = (By.CSS_SELECTOR, "div.pagination__button")

    FILTER_BUTTON = (By.CSS_SELECTOR, "div.filter-text")
    SELL = (By.CSS_SELECTOR, "div[wized='ListingTypeSell']")
    APPLY_FILTER = (By.CSS_SELECTOR, "a.button-filter.w-button")
    LISTING = (By.CSS_SELECTOR, "div.listing-card")
    LIST_SALE = (By.CSS_SELECTOR, "div[w-el-text='For sale']")
    BUY = (By.CSS_SELECTOR, "div[wized='ListingTypeBuy']")
    LIST_BUY = (By.CSS_SELECTOR, "div.for-sale-tag")
    FROM_PRICE = (
    By.CSS_SELECTOR, "div.filters-block-1.mls.hidden div.select-block._8px input[wized='unitPriceFromFilter']")
    TO_PRICE = (By.CSS_SELECTOR, "input[wized='unitPriceToFilter']")
    PRODUCT_PRICES = (By.CSS_SELECTOR, "div.number-price-text")

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
        filter_button = self.driver.find_element(*self.FILTER_BUTTON)
        filter_button.click()
        sleep(5)
        self.driver.execute_script("document.querySelector('div.filter-button').style.display = 'block';")
        self.driver.execute_script("document.querySelector('div.filter-button').style.visibility = 'visible';")
        sell = self.driver.find_element(*self.SELL)
        self.driver.execute_script("arguments[0].click()", sell)
        apply = self.driver.find_element(*self.APPLY_FILTER)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", apply)

    def click_on_filters_buy_apply(self):
        filter_button = self.driver.find_element(*self.FILTER_BUTTON)
        filter_button.click()
        sleep(5)
        self.driver.execute_script("document.querySelector('div.filter-button').style.display = 'block';")
        buy = self.driver.find_element(*self.BUY)
        self.driver.execute_script("arguments[0].click()", buy)
        apply = self.driver.find_element(*self.APPLY_FILTER)
        self.driver.execute_script("arguments[0].click()", apply)

    def verify_for_sale_listing(self):
        listing = self.driver.find_elements(*self.LISTING)
        for_sale_lists = self.driver.find_elements(*self.LIST_SALE)
        assert len(listing) == len(for_sale_lists), f'expected {len(listing)} == {len(for_sale_lists)} but they are not'
        print(len(listing))

    def verify_tag_buy_listing(self):
        listing = self.driver.find_elements(*self.LISTING)
        list_buy = self.driver.find_elements(*self.LIST_BUY)
        assert len(listing) == len(list_buy), f'expected {len(listing)} == {len(list_buy)} but they are not'

    def click_on_filter_price_range(self):
        self.click(self.FILTER_BUTTON)
        element = self.driver.find_element(*self.APPLY_FILTER)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.FROM_PRICE)).send_keys("1200000")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.TO_PRICE)).send_keys("2000000")
        self.click(self.APPLY_FILTER)

    def verify_product_price(self):
        prices = self.driver.find_elements(*self.PRODUCT_PRICES)
        numbers = [int(price.replace("AED ", "")) for price in prices]
        for num in numbers:
            assert 2000000 >= num >= 1200000, f'prices is not whithin the range'
