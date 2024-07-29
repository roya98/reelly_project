from pages.main_page import MainPage
from pages.add_project import AddProject


class Application:
    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.add_project = AddProject(self.driver)





