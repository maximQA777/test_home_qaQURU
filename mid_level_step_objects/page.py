import os

from selene import browser, by, have


class RegistrationPage:
    def open(self):
        browser.config.base_url = 'https://demoqa.com/automation-practice-form'
        browser.open('/')

    def set_firstname(self, value):
        browser.element('#firstName').type(value)

    def set_lastname(self, value):
        browser.element('#lastName').type(value)

    def set_email(self, email):
        browser.element('#userEmail').type(email)

    def set_gender(self, gender_value):
        browser.element(f'[for="gender-radio-{gender_value}"]').click()

    def set_phone(self, phone):
        browser.element('#userNumber').type(phone)

    def set_birthday(self, month, year, day):
        browser.element('#dateOfBirthInput').click()
        browser.element(f'.react-datepicker__month-select option[value="{month}"]').click()
        browser.element(f'.react-datepicker__year-select option[value="{year}"]').click()
        browser.element(f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)').click()

    def scroll_page(self):
        browser.execute_script('window.scrollBy(0, 400);')  # Скролл, чтобы не убирать рекламу

    def set_subjects(self, *subjects):
        for subject in subjects:
            browser.element('#subjectsInput').type(subject).press_enter()

    def set_hobby(self, hobby_value):
        browser.element(f'[for="hobbies-checkbox-{hobby_value}"]').click()

    def upload_picture(self, file_path):
        browser.element('#uploadPicture').send_keys(os.path.abspath(file_path))

    def set_address(self, address, state, city):
        browser.element('#currentAddress').type(address)
        browser.element('#state').click().element(by.text(state)).click()
        browser.element('#city').click().element(by.text(city)).click()

    def click_submit_button(self):
        browser.element('#submit').click()

    def assert_filled_names(self, Names):
        browser.element('.table-responsive').should(have.text(Names))

    def assert_text_present(self, text):
        browser.element('.table-responsive').should(have.text(text))

    def assert_filled_name(self, name):
        self.assert_text_present(name)

    def assert_filled_label(self, label):
        self.assert_text_present(label)

    def assert_filled_email(self, email):
        self.assert_text_present(email)

    def assert_filled_gender(self, gender):
        self.assert_text_present(gender)

    def assert_filled_mobile(self, mobile):
        self.assert_text_present(mobile)

    def assert_filled_subject(self, subject):
        self.assert_text_present(subject)

    def assert_filled_hobbies(self, hobbies):
        self.assert_text_present(hobbies)

    def assert_filled_picture(self, picture):
        self.assert_text_present(picture)

    def assert_filled_address(self, address):
        self.assert_text_present(address)

    def assert_filled_state(self, state):
        self.assert_text_present(state)

    def assert_filled_birth(self, day):
        self.assert_text_present(day)
