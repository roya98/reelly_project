from selenium.webdriver.common.by import By
from behave import given, when, then


@when('Click on Community option')
def click_on_community_option(context):
    context.app.community_page.click_community()


@then('Verify the community page opens')
def verify_community_page_opens(context):
    context.app.community_page.verify_community()


@then("Verify 'Contact support' button is available and clickable")
def verify_contact_support_button(context):
    context.app.community_page.button_available_clickable()
