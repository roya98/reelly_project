from selenium.webdriver.common.by import By
from behave import given, when, then

@then('Verify Payment Page Opens')
def verify_correct_payment_page(context):
    context.app.payments_page.verify_payment_page()

@then("Verify title 'Subscription & payments' is visible")
def verify_title_subscription_visible(context):
    context.app.payments_page.payment_title_visibility()

@then("Verify 'back' and 'upgrade plan' buttons are available")
def back_and_upgrade(context):
    context.app.payments_page.back_and_upgrade_buttons()


