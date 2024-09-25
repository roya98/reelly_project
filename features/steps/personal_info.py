from selenium.webdriver.common.by import By
from behave import given, when, then


@when('Enter some test information in the input fields')
def enter_some_test_info(context):
    context.app.personal_page.enter_test_info()


@then('Check the right information is present in the input fields')
def verify_input_fields(context):
    context.app.personal_page.verify_input_fields()


@then('Check Close and Save Changes buttons are available and clickable')
def check_buttons_visible(context):
    context.app.personal_page.check_button_are_visible()
