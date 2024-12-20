from pages.main_page import MainPage
from pages.add_project_page import AddProject
from pages.community_page import CommunityPage
from pages.connect_company_page import ConnectCompany
from pages.settings_page import Settings
from pages.contact_us_page import CONTACT
from pages.user_guide_page import UserGuide
from pages.password_page import Password
from pages.payments_page import Payment
from pages.support_page import Support
from pages.news_page import News
from pages.personal_page import Personal
from pages.secondary_deals_page import Secondary
from pages.off_plan_page import OffPlan



class Application:
    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.add_project = AddProject(self.driver)
        self.community_page = CommunityPage(self.driver)
        self.connect_company_page = ConnectCompany(self.driver)
        self.settings_page = Settings(self.driver)
        self.contact_us_page = CONTACT(self.driver)
        self.user_guide_page = UserGuide(self.driver)
        self.password_page = Password(self.driver)
        self.payments_page = Payment(self.driver)
        self.support_page = Support(self.driver)
        self.news_page = News(self.driver)
        self.personal_page = Personal(self.driver)
        self.secondary_page = Secondary(driver)
        self.off_plan_page = OffPlan(self.driver)








