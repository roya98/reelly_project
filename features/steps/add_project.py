from selenium.webdriver.common.by import By
from behave import given, when, then


@when('Click on Add a project')
def click_on_add_project(context):
    context.app.add_project.click_add_project()


@when('Add some test information to the input fields')
def add_information(context):
    context.app.add_project.add_info()


@then('Verify the right information is present in the input field')
def verify_right_information(context):
    context.app.add_project.verify_info()


@then("Verify 'Send an application' button is available and clickable")
def send_application_button(context):
    context.app.add_project.verify_send_application_button()
