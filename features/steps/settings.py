from selenium.webdriver.common.by import By
from behave import given, when, then


@when('Click on Contact us option')
def contact_us(context):
    context.app.settings_page.click_contact_us()