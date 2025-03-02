

from level_step_objects.page import RegistrationPage
from level_step_objects.users import test_user


def test_registration_form():
    registration_page = RegistrationPage()
    registration_page.open()

    registration_page.register(test_user)

    registration_page.assert_form_registration(test_user)
