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


@when('Click on Subscription & payments option')
def click_on_payments(context):
    context.app.settings_page.click_on_subscription_payment()


@when('Click on support option')
def click_on_support_option(context):
    context.app.settings_page.click_on_support()


@when('Switch to support window')
def switch_to_support_window(context):
    context.app.settings_page.switch_to_support_window()


@when('Switch to settings window')
def switch_to_settings(context):
    context.app.settings_page.go_back_to_settings_page()


@when('Click on news option')
def click_on_news(context):
    context.app.settings_page.click_on_news_option()


@when('Click on Edit profile option')
def click_on_edit_profile(context):
    context.app.settings_page.click_edit_profile()
