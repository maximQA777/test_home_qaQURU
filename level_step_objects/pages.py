import os

from selene import browser, by, have

from level_step_objects.users import User


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


    def floor_name(self , gender ):
        browser.element('[for="gender-radio-2"]').click()

    def number_name(self , phone):
        browser.element('#userNumber').type(phone)

    def birthday_data(self, mouth, years, day):
        browser.element('#dateOfBirthInput').click()
        browser.element(f'.react-datepicker__month-select option[value="{mouth}"]').click()
        browser.element(f'.react-datepicker__year-select option[value="{years}"]').click()
        browser.element(f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)').click()


    def scroll_web(self):
        browser.execute_script('window.scrollBy(0, 400);') #cкролл чтоб не убирать рекламу

    def subject_name(self , subjects ):
        browser.element('#subjectsInput').type(subjects).press_enter()


    def hobbis_name(self, hobby):
        browser.element('[for="hobbies-checkbox-1"]').click()

    def picture_png(self , picrture ):
        browser.element('#uploadPicture').send_keys(os.path.abspath("../resources\picture.png"))

    def addres_name(self , Value , state , city):
        browser.element('#currentAddress').type(Value).click()
        browser.element('#state').click().element(by.text('NCR')).click()
        browser.element('#city').click().element(by.text('Delhi')).click()

    def ready(self):
        browser.element('#submit').click()

    def register(self, user: User):
        self.first_name(user.firstName)
        self.second_name(user.lastName)
        self.mail_name(user.email)
        self.floor_name(user.gender)
        self.number_name(user.mobile)
        self.birthday_data(user.birth_month, user.birth_year, user.birth_day)
        self.scroll_web()
        self.subject_name(user.subjects)
        self.hobbis_name(user.hobby)
        self.picture_png(user.picture)
        self.addres_name(user.address , user.state , user.city)

        self.ready()

    def  assert_form_registration(self):
        browser.element('.table-responsive').should(have.text('Label Values'))
        browser.element('.table-responsive').should(have.text('Values'))
        browser.element('.table-responsive').should(have.text('Student Name Maxim Lerich'))
        browser.element('.table-responsive').should(have.text('Student Email alab@mail.me'))
        browser.element('.table-responsive').should(have.text('Gender Female'))
        browser.element('.table-responsive').should(have.text('Mobile 3123213131'))
        browser.element('.table-responsive').should(have.text('Date of Birth 15 September,1999'))
        browser.element('.table-responsive').should(have.text('Subjects Maths'))
        browser.element('.table-responsive').should(have.text('Hobbies Sports'))
        browser.element('.table-responsive').should(have.text('Picture picture.png'))
        browser.element('.table-responsive').should(have.text('Address Kabanina Polina'))
        browser.element('.table-responsive').should(have.text('State and City NCR Delhi'))






