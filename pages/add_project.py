from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



class AddProject(Page):
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

    name = "Jasmine"
    company_name = "Careerist"
    role = "QA"
    age_company = "9"
    country = "USA"
    project_name = "Reelly"
    phone = "1234"
    email = "email@email"

    def click_add_project(self):
        self.click(self.ADD_PROJECT)

    def add_info(self):

        self.input_text(self.name, self.NAME_INPUT)
        self.input_text(self.company_name, self.COMPANY_NAME_INPUT)
        self.input_text(self.role, self.ROLE_INPUT)
        self.input_text(self.age_company, self.AGE_INPUT)
        self.input_text(self.country, self.COUNTRY_INPUT)
        self.input_text(self.project_name, self.NAME_PROJECT_INPUT)
        self.input_text(self.phone, self.PHONE_INPUT)
        self.input_text(self.email, self.EMAIL_INPUT)

    def verify_info(self):

        expected_inputs = [self.name, self.company_name, self.role, self.age_company, self.country,
                           self.project_name, self.phone, self.email]
        fields = [self.NAME_INPUT, self.COMPANY_NAME_INPUT, self.ROLE_INPUT, self.AGE_INPUT, self.COUNTRY_INPUT, self.NAME_PROJECT_INPUT, self.PHONE_INPUT,
                  self.EMAIL_INPUT]
        actual_inputs = []

        for field in fields:
            try:
                element = self.driver.find_element(*field)
                element_text = element.get_attribute('value')
                actual_inputs.append(element_text)
            except Exception as e:
                print(f"Error finding element {field}: {e}")
        assert actual_inputs == expected_inputs, f'expected {expected_inputs} got {actual_inputs}'


    def verify_send_application_button(self):
        self.driver.wait.until(EC.presence_of_element_located(self.SUBMIT_BUTTON))
        self.driver.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON))








