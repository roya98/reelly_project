from pages.main_page import MainPage
from pages.add_project_page import AddProject
from pages.community_page import CommunityPage
from pages.connect_company_page import ConnectCompany



class Application:
    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.add_project = AddProject(self.driver)
        self.community_page = CommunityPage(self.driver)
        self.connect_company_page = ConnectCompany(self.driver)








