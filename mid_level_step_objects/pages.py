import os

from selene import browser, by, have


class RegistrationPage:
    def open(self):
        browser.config.base_url = 'https://demoqa.com/automation-practice-form'
        browser.open('/')


    def first_name(self , value):
        browser.element('#firstName').type(value)


    def second_name(self , value):
         browser.element('#lastName').type(value)


    def mail_name(self , email):
        browser.element('#userEmail').type(email)


    def gender_name(self ):
        browser.element('[for="gender-radio-2"]').click()

    def number_name(self , phone):
        browser.element('#userNumber').type(phone)

    def birthday_data(self, mouth, years, day):
        browser.element('#dateOfBirthInput').click()
        browser.element(f'.react-datepicker__month-select option[value="{mouth}"]').click()
        browser.element(f'.react-datepicker__year-select option[value="{years}"]').click()
        browser.element(f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)').click()

    def subject_name(self , Value1 , Value2 ):
        browser.execute_script('window.scrollBy(0, 400);')   #cкролл чтоб не убирать рекламу
        browser.element('#subjectsInput').type(Value1).press_enter()
        browser.element('#subjectsInput').type(Value2).press_enter()

    def hobbis_name(self ):
        browser.element('[for="hobbies-checkbox-1"]').click()

    def picture_png(self  ):
        browser.element('#uploadPicture').send_keys(os.path.abspath("../resources\picture.png"))

    def addres_name(self , Value):
        browser.element('#currentAddress').type(Value).click()
        browser.element('#state').click().element(by.text('NCR')).click()
        browser.element('#city').click().element(by.text('Delhi')).click()

    def ready(self):
        browser.element('#submit').click()

    def assert_filled_names(self, Names):
        browser.element('.table-responsive').should(have.text(Names))


    def assert_filled_labels(self, labels):
        browser.element('.table-responsive').should(have.text(labels))

    def assert_filled_emaily(self, Mail):
        browser.element('.table-responsive').should(have.text(Mail))

    def assert_filled_gender(self, Gender):
        browser.element('.table-responsive').should(have.text(Gender))

    def assert_filled_mobile(self, Mobile):
        browser.element('.table-responsive').should(have.text(Mobile))

    def assert_filled_subject(self, Subjest):
        browser.element('.table-responsive').should(have.text(Subjest))

    def assert_filled_hobbies(self, Hobbies):
        browser.element('.table-responsive').should(have.text(Hobbies))

    def assert_filled_picrure(self, picture):
        browser.element('.table-responsive').should(have.text(picture))

    def assert_filled_Adress(self, Addres):
        browser.element('.table-responsive').should(have.text(Addres))

    def assert_filled_state(self , state):
          browser.element('.table-responsive').should(have.text(state))

    def assert_filled_birt(self , day):
        browser.element('.table-responsive').should(have.text(day))
