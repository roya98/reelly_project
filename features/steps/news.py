from selenium.webdriver.common.by import By
from behave import given, when, then

@then('Verify the news page opens')
def verify_news_page_opens(context):
    context.app.news_page.verify_news_page()
