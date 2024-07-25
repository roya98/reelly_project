from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

EMAIL_FIELD= (By.ID, "email-2")
PASSWORD_FIELD = (By.ID, "field")
CONTINUE = (By.CSS_SELECTOR, "a.login-button")
MAIN_MENU = (By.CSS_SELECTOR, ".w-layout-grid a[href*='main-menu']")
LANGUAGE_SELECTION = (By.CSS_SELECTOR, ".wg-element-wrapper.sw5")
RUSSIAN_LANGUAGE = (By.CSS_SELECTOR, "a[lang='ru']")
RUSSIAN_TITLE = (By.XPATH, "//h1[@class='h1-menu' and text()='Главное меню']")
SETTING = (By.XPATH, "//a[contains(@href, '/settings') and @class='menu-button-block w-inline-block']")


@given('Open the main page')
def open_main_page(context):
    context.driver.get('https://soft.reelly.io/')
    sleep(4)

@when('Log in to the page')
def login_page(context):
    email_account = "jasmine.test0011@gmail.com"
    password_account = "Jasmine1234"
    email = context.driver.find_element(*EMAIL_FIELD)
    email.send_keys(email_account)
    password = context.driver.find_element(*PASSWORD_FIELD)
    password.send_keys(password_account)
    context.driver.find_element(*CONTINUE).click()



@when('Click on the main menu option')
def main_menu(context):
    main = context.driver.find_element(*MAIN_MENU).click()

@when('Change the language of the page to Russian')
def change_language(context):
    language = context.driver.find_element(*LANGUAGE_SELECTION)
    actions = ActionChains(context.driver)
    actions.move_to_element(language).perform()
    context.driver.find_element(*RUSSIAN_LANGUAGE).click()


@when('Click on setting options')
def click_on_setting(context):
    context.driver.find_element(*SETTING).click()


@then('Verify the language has changed')
def verify_russian_language_change(context):
    actual = context.driver.find_element(*RUSSIAN_TITLE).text
    expected = "Главное меню"
    assert expected == actual, f'The language did not change expected {expected} but got {actual}'











