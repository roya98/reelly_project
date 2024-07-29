from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open the main page')
def open_main_page(context):
    context.app.main_page.open_main_page()


@when('Log in to the page')
def login_page(context):
    context.app.main_page.login()


@when('Click on the main menu option')
def main_menu(context):
    context.app.main_page.click_main_menu()


@when('Change the language of the page to Russian')
def change_language(context):
    context.app.main_page.change_language_to_russian()


@when('Click on setting options')
def click_on_setting(context):
    context.app.main_page.click_setting()


@then('Verify the language has changed')
def verify_russian_language_change(context):
    context.app.main_page.verify_russian()
