from selenium.webdriver.common.by import By
from behave import given, when, then


@then('Verify the support page opens')
def verify_support_page(context):
    context.app.support_page = context.app.support_page.verify_support()
