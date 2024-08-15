from pages.main_page import MainPage
from pages.add_project_page import AddProject
from pages.community_page import CommunityPage
from pages.connect_company_page import ConnectCompany
from pages.settings_page import Settings
from pages.contact_us_page import CONTACT
from pages.user_guide_page import UserGuide



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








