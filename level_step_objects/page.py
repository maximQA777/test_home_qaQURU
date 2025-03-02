import os

from selene import browser, by, have

from level_step_objects.users import User


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

    def set_gender(self , gender):
        browser.element(f'[for="gender-radio-1"]').click()

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

    def set_hobby(self , hobby):
        browser.element(f'[for="hobbies-checkbox-1"]').click()

    def upload_picture(self , picture):
        browser.element('#uploadPicture').send_keys(os.path.abspath("../resources\picture.png"))

    def set_address(self, address, state, city):
        browser.element('#currentAddress').type(address)
        browser.element('#state').click().element(by.text(state)).click()
        browser.element('#city').click().element(by.text(city)).click()

    def click_submit_button(self):
        browser.element('#submit').click()

    def register(self, user: User):
        self.set_firstname(user.firstName)
        self.set_lastname(user.lastName)
        self.set_email(user.email)
        self.set_gender(user.gender)
        self.set_phone(user.mobile)
        self.set_birthday(user.birth_month, user.birth_year, user.birth_day)
        self.scroll_page()
        self.set_subjects(user.subjects)
        self.set_hobby(user.hobby)
        self.upload_picture(user.picture)
        self.set_address(user.address, user.state, user.city)

        self.click_submit_button()

    def assert_form_registration(self, user):
        browser.element('.table-responsive').should(have.text(f'Student Name {user.firstName} {user.lastName}'))
        browser.element('.table-responsive').should(have.text(f'Student Email {user.email}'))
        browser.element('.table-responsive').should(have.text(f'Gender {user.gender}'))
        browser.element('.table-responsive').should(have.text(f'Mobile {user.mobile}'))
        browser.element('.table-responsive').should(have.text(f'Date of Birth {user.birth_day} {user.text_birth_month},{user.birth_year}'))
        browser.element('.table-responsive').should(have.text(f'Subjects {user.subjects}'))
        browser.element('.table-responsive').should(have.text(f'Hobbies {user.hobby}'))
        browser.element('.table-responsive').should(have.text(f'Picture {user.picture}'))
        browser.element('.table-responsive').should(have.text(f'Address {user.address}'))
        browser.element('.table-responsive').should(have.text(f'State and City {user.state} {user.city}'))






