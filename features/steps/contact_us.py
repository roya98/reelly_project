from selenium.webdriver.common.by import By
from behave import given, when, then


@then('Verify the contact us page opens')
def verify_contact_us_page(context):
    context.app.contact_us_page.verify_contact_page()


@then('Verify there are at least 4 social media icons')
def verify_icons(context):
    context.app.contact_us_page.verify_social_icons()

@then("Verify 'Connect the company' button is available and clickable")
def verify_connect_company_button(context):
    context.app.contact_us_page.verify_connect_company()

