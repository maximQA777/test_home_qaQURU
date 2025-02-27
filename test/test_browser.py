import os

from selene import browser, be, by, have

from mid_level_step_objects.pages import RegistrationPage
from test_home_qaQURU.conditions import match  # чтоб писать match вместо be , have





def test_register_form():
    registration_form = RegistrationPage()


    registration_form.open()
    registration_form.first_name('Maxim')
    registration_form.second_name('Lerich')
    registration_form.mail_name('alab@mail.me')
    registration_form.gender_name()
    registration_form.number_name('3123213131')
    registration_form.birthday_data('8' ,'1999' , '15')
    registration_form.subject_name('Math', 'English')
    registration_form.hobbis_name()
    registration_form.picture_png()
    registration_form.addres_name('Kabanina Polina')

    registration_form.ready()

    registration_form.assert_filled_labels('Label Values')
    registration_form.assert_filled_names('Student Name Maxim Lerich')
    registration_form.assert_filled_emaily('Student Email alab@mail.me')
    registration_form.assert_filled_gender('Gender Female')
    registration_form.assert_filled_mobile('Mobile 3123213131')
    registration_form.assert_filled_birt('Date of Birth 15 September,1999')
    registration_form.assert_filled_subject('Subjects Maths, English')
    registration_form.assert_filled_hobbies('Hobbies Sports')
    registration_form.assert_filled_picrure('Picture picture.png')
    registration_form.assert_filled_Adress('Address Kabanina Polina')
    registration_form.assert_filled_state('State and City NCR Delhi')





