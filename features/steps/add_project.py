from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


ADD_PROJECT = (By.CSS_SELECTOR, "a[href*=add-a-project].page-setting-block")
NAME_INPUT = (By.ID, "Your-name")
COMPANY_NAME_INPUT = (By.ID, "Your-company-name")
ROLE_INPUT = (By.ID, "Role")
AGE_INPUT = (By.ID, "Age-of-the-company")
COUNTRY_INPUT = (By.ID, "Country")
NAME_PROJECT_INPUT = (By.ID, "Name-project")
PHONE_INPUT = (By.ID, "Phone")
EMAIL_INPUT = (By.ID, "Email-add-project")
SUBMIT_BUTTON = (By.CSS_SELECTOR, ".purchase-access.w-button")


@when('Click on Add a project')
def click_on_add_project(context):
    context.driver.find_element(*ADD_PROJECT).click()

@when('Add some test information to the input fields')
def add_information(context):
    context.name = "Jasmine"
    context.company_name = "Careerist"
    context.role = "QA"
    context.age_company = "9"
    context.country = "USA"
    context.project_name = "Reelly"
    context.phone = "1234"
    context.email = "email@email"

    context.driver.find_element(*NAME_INPUT).send_keys(context.name)
    context.driver.find_element(*COMPANY_NAME_INPUT).send_keys(context.company_name)
    context.driver.find_element(*ROLE_INPUT).send_keys(context.role)
    context.driver.find_element(*AGE_INPUT).send_keys(context.age_company)
    context.driver.find_element(*COUNTRY_INPUT).send_keys(context.country)
    context.driver.find_element(*NAME_PROJECT_INPUT).send_keys(context.project_name)
    context.driver.find_element(*PHONE_INPUT).send_keys(context.phone)
    context.driver.find_element(*EMAIL_INPUT).send_keys(context.email)


@then('Verify the right information is present in the input field')
def verify_right_information(context):
    expected_inputs = [context.name, context.company_name, context.role, context.age_company, context.country, context.project_name, context.phone, context.email]
    fields = [NAME_INPUT, COMPANY_NAME_INPUT, ROLE_INPUT, AGE_INPUT, COUNTRY_INPUT, NAME_PROJECT_INPUT, PHONE_INPUT, EMAIL_INPUT ]
    actual_inputs = []

    for field in fields:
        try:
            element = context.driver.find_element(*field)
            element_text = element.get_attribute('value')
            actual_inputs.append(element_text)
        except Exception as e:
            print(f"Error finding element {field}: {e}")
    assert actual_inputs == expected_inputs, f'expected {expected_inputs} got {actual_inputs}'



@then("Verify 'Send an application' button is available and clickable")
def send_application_button(context):
    context.driver.wait.until(EC.presence_of_element_located(SUBMIT_BUTTON))
    context.driver.wait.until(EC.element_to_be_clickable(SUBMIT_BUTTON))


