from mid_level_step_objects.page import RegistrationPage


def test_register_form():
    registration_form = RegistrationPage()

    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.set_firstname("Maxim")
    registration_page.set_lastname("Lerich")
    registration_page.set_email("alab@mail.me")
    registration_page.set_gender(2)
    registration_page.set_phone("3123213131")
    registration_page.set_birthday("5", "1990", "15")
    registration_page.scroll_page()
    registration_page.set_subjects("Maths", "English")
    registration_page.set_hobby(1)
    registration_page.upload_picture("../resources/picture.png")
    registration_page.set_address("Kabanina Polina", "NCR", "Delhi")

    registration_form.click_submit_button()

    registration_form.assert_filled_label('Label Values')
    registration_form.assert_filled_names('Student Name Maxim Lerich')
    registration_form.assert_filled_email('Student Email alab@mail.me')
    registration_form.assert_filled_gender('Gender Female')
    registration_form.assert_filled_mobile('Mobile 3123213131')
    registration_form.assert_filled_birth('Date of Birth 15 June,1990')
    registration_form.assert_filled_subject('Subjects Maths, English')
    registration_form.assert_filled_hobbies('Hobbies Sports')
    registration_form.assert_filled_picture('Picture picture.png')
    registration_form.assert_filled_address('Address Kabanina Polina')
    registration_form.assert_filled_state('State and City NCR Delhi')
