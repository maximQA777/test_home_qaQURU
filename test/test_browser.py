import os
from selene import browser, be, by, have

from level_step_objects.pages import RegistrationPage
from level_step_objects.users import test_user
from test_home_qaQURU.conditions import match  # чтоб писать match вместо be , have




def test_registration_form():
        registration_form = RegistrationPage()
        registration_form.open()
        registration_form.register(test_user)


        registration_form.assert_form_registration()





