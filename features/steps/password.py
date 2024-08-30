from selenium.webdriver.common.by import By
from behave import given, when, then


@when('Add some test password to the input fields')
def add_input_data(context):
    context.app.password_page.password_data()


@then('Verify the change password page opens')
def contact_page_opens(context):
    context.app.password_page.verify_password_change_page()


@then("Verify the 'Change password' button is available")
def verify_change_password_button(context):
    context.app.password_page.verify_button()

