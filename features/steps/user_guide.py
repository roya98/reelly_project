from selenium.webdriver.common.by import By
from behave import given, when, then


@then('Verify the user guide page opens')
def verify_user_guide(context):
    context.app.user_guide_page.verify_user_guide_opens()


@then('Verify all lesson videos contain titles')
def lesson_titles(context):
    context.app.user_guide_page.verify_lesson_titles()

