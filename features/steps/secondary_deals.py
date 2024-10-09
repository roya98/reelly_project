from selenium.webdriver.common.by import By
from behave import given, when, then


@when('Click on Secondary option at the left side menu')
def click_secondary_option(context):
    context.app.secondary_page.click_secondary_option()


@when("Click on Filters and select 'want to sell' and apply")
def click_filters_and_sell(context):
    context.app.secondary_page.click_on_filters_select_sells()


@then('Go to the final page using the pagination button')
def go_to_final_page(context):
    context.app.secondary_page.go_to_final_page()


@then('Go back to the first page using the pagination button')
def go_to_first_page(context):
    context.app.secondary_page.go_to_first()


@then('Verify the secondary page opens')
def verify_secondary_page_opens(context):
    context.app.secondary_page.verify_secondary_page()


@then("Verify all cards have 'for sale' tag")
def verify_tag(context):
    context.app.secondary_page.verify_for_sale_listing()
