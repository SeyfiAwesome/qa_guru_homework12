from pages.registration_page import RegistrationPage
from pages.left_panel import LeftPanel

class ApplicationManager:
    def __init__(self):
        self.registration_page = RegistrationPage()
        self.left_panel = LeftPanel()
