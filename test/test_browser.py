import os

from selene import browser, be

from test_home_qaQURU.conditions import match   #чтоб писать match вместо be , have



def test_register_form():
    browser.open('https://demoqa.com/automation-practice-form') #открыть бразуер



    browser.element('[id="firstName"]').type('John') #имя
    browser.element('[id="lastName"]').type('Doe')  #фамилия
    browser.element('[id="userEmail"]').type('john.doe@example.com') #майл


    browser.execute_script('window.scrollBy(0, 400);')     #прокрутка вниз


    browser.element('[for="gender-radio-1"]').should(be.visible).click()   #выбрать пол

    browser.element('[id="userNumber"]').should(be.visible).type('1234567890') #написать номер

    browser.element('[id="dateOfBirthInput"]').click()  #открыть календарь
    browser.element('.react-datepicker__month-select option[value="1"]').should(be.visible).click() #выбрать месяц

    browser.element('.react-datepicker__year-select [value="1999"]').click() # выбрать год
    browser.element('[class="react-datepicker__day react-datepicker__day--023"]').click()  # выбрать день



    browser.element('[id="subjectsInput"]').type("Math").press_enter()  #написать предмет

    browser.element('[for="hobbies-checkbox-1"]').click()  #выбрать хобби

    browser.element('#uploadPicture').send_keys(os.path.abspath("resources\picture.png")) #вставить файл фотку

    browser.element('[id = "currentAddress"]').should(be.visible).type('Aviacionno') # написать адрес

    browser.element('[id="state"]').should(be.visible).click()  #выбрать штат
    browser.element('#react-select-3-option-0').click()

    browser.element('[id = "city"]').should(be.visible).click()    # выбрать город
    browser.element('#react-select-4-input').type('Delhi').press_enter()


    browser.element('#submit').click()  #отправить данные














