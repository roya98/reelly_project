from selenium.webdriver.common.by import By
from behave import given, when, then


@when("Click on 'off plan' at the left side menu")
def click_off_plan(context):
    context.app.off_plan_page.click_on_off_plan()


@then('Verify the off plan page opens')
def verify_off_plan_page(context):
    context.app.off_plan_page.verify_off_plan_page_opens()


@then('Verify each product on this page contains a title and picture visible')
def verify_each_product_on_off_plan(context):
    context.app.off_plan_page.verify_element_picture_title()
