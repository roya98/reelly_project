from selenium.webdriver.common.by import By
from behave import given, when, then


@when("Click on 'Connect the company'")
def connect_company(context):
    context.app.connect_company_page.click_connect_company()


@when('Switch the new tab')
def switch_tab(context):
    context.app.connect_company_page.switch_window()


@then('Verify the connect company page opens')
def verify_connect_company_opens(context):
    context.app.connect_company_page.verify_page()
