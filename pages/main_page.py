from selenium.webdriver import ActionChains

from pages.base_page import Page
from selenium.webdriver.common.by import By


class MainPage(Page):
    EMAIL_FIELD = (By.ID, "email-2")
    PASSWORD_FIELD = (By.ID, "field")
    CONTINUE = (By.CSS_SELECTOR, "a.login-button")
    MAIN_MENU = (By.CSS_SELECTOR, ".w-layout-grid a[href*='main-menu']")
    LANGUAGE_SELECTION = (By.CSS_SELECTOR, ".wg-element-wrapper.sw5")
    RUSSIAN_LANGUAGE = (By.CSS_SELECTOR, "a[lang='ru']")
    RUSSIAN_TITLE = (By.XPATH, "//h1[@class='h1-menu' and text()='Главное меню']")
    SETTING = (By.XPATH, "//a[contains(@href, '/settings') and @class='menu-button-block w-inline-block']")

    def __init__(self, driver):
        super().__init__(driver)

    def open_main_page(self):
        self.driver.get('https://soft.reelly.io/')

    def login(self):
        email_account = "royatest9@gmail.com"
        password_account = "Test1234!"
        self.input_text(email_account, self.EMAIL_FIELD)
        self.input_text(password_account, self.PASSWORD_FIELD)
        self.click(self.CONTINUE)

    def click_main_menu(self):
        self.click(self.MAIN_MENU)

    def change_language_to_russian(self):
        language = self.driver.find_element(*self.LANGUAGE_SELECTION)
        actions = ActionChains(self.driver)
        actions.move_to_element(language).perform()
        self.click(self.RUSSIAN_LANGUAGE)

    def click_setting(self):
        self.click(self.SETTING)

    def verify_russian(self):
        expected = "Главное меню"
        self.verify_text(expected, self.RUSSIAN_TITLE)
