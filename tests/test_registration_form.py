from pages.registration_page import RegistrationPage
from tests.data.users import student
import allure


@allure.title('Successful fill form')
def test_student_registration_from_high_level():
    registration_page = RegistrationPage()

    with allure.step('Open registration form'):
        registration_page.open()

    with allure.step('Fill data'):
        registration_page.register(student)

    with allure.step('Check the data'):
        registration_page.should_registered_user_with(student)
