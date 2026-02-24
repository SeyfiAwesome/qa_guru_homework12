from pages.simple_registration_page import SimpleUserRegistrationPage

class LeftPanel:

    def __init__(self):
        self.simple_registration_page = SimpleUserRegistrationPage()

    def open_simple_registration_form(self):
        self.simple_registration_page.open()
        return self