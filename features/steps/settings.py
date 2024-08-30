from selenium.webdriver.common.by import By
from behave import given, when, then


@when('Click on Contact us option')
def contact_us(context):
    context.app.settings_page.click_contact_us()


@when('Click on User Guide option')
def user_guide(context):
    context.app.settings_page.click_on_user_guide()

@when('Click on Change password option')
def click_on_change_password(context):
    context.app.settings_page.click_password_change()

