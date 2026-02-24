from pages.registration_page import RegistrationPage
from tests.data.users import student


def test_student_registration_from_high_level():
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.register(student)
    registration_page.should_registered_user_with(student)

