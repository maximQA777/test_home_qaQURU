import os

from selene import browser, be, by, have

from test_home_qaQURU.conditions import match  # чтоб писать match вместо be , have


def test_register_form():
    # открыли браузер
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'
    browser.open('/')
    # ввели имя и фамилию
    browser.element('#firstName').type('Maxim')
    browser.element('#lastName').type('Lerich')
    # майл
    browser.element('#userEmail').type('alab@mail.me')
    # пол
    browser.element('[for="gender-radio-2"]').click()
    # номер телефона
    browser.element('#userNumber').type('3123213131')

    # дата рождения
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select option[value="8"]').click()
    browser.element('.react-datepicker__year-select  option[value="1999"]').click()
    browser.element('.react-datepicker__day--015').click()

    # cкролл так как текст иногда валиться из-за рекламы
    browser.execute_script('window.scrollBy(0, 400);')

    # предменты
    browser.element('#subjectsInput').type('Math').press_enter()
    browser.element('#subjectsInput').type('English').press_enter()

    # хобби
    browser.element('[for="hobbies-checkbox-1"]').click()
    # картинка
    browser.element('#uploadPicture').send_keys(os.path.abspath("resources\picture.png"))

    # адресс
    browser.element('#currentAddress').type('Kabanina Polina').click()
    # штат и город
    browser.element('#state').click().element(by.text('NCR')).click()
    browser.element('#city').click().element(by.text('Delhi')).click()

    # проверка что все поля заполнены
    browser.element('#submit').click()
    browser.element('.table-responsive').should(have.text('Label Values'))
    browser.element('.table-responsive').should(have.text('Values'))
    browser.element('.table-responsive').should(have.text('Student Name Maxim Lerich'))
    browser.element('.table-responsive').should(have.text('Student Email alab@mail.me'))
    browser.element('.table-responsive').should(have.text('Gender Female'))
    browser.element('.table-responsive').should(have.text('Mobile 3123213131'))
    browser.element('.table-responsive').should(have.text('Date of Birth 15 September,1999'))
    browser.element('.table-responsive').should(have.text('Subjects Maths, English'))
    browser.element('.table-responsive').should(have.text('Hobbies Sports'))
    browser.element('.table-responsive').should(have.text('Picture picture.png'))
    browser.element('.table-responsive').should(have.text('Address Kabanina Polina'))
    browser.element('.table-responsive').should(have.text('State and City NCR Delhi'))
