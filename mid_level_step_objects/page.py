import os

from selene import browser, by, have
import allure


class RegistrationPage:
    @allure.step("Открываем страницу регистрации")
    def open(self):
        browser.config.base_url = 'https://demoqa.com/automation-practice-form'
        browser.open('/')

    @allure.step("Вводим имя: {value}")
    def set_firstname(self, value):
        browser.element('#firstName').type(value)

    @allure.step("Вводим фамилию: {value}")
    def set_lastname(self, value):
        browser.element('#lastName').type(value)

    @allure.step("Вводим email: {email}")
    def set_email(self, email):
        browser.element('#userEmail').type(email)

    @allure.step("Выбираем пол: {gender_value}")
    def set_gender(self, gender_value):
        browser.element(f'[for="gender-radio-{gender_value}"]').click()

    @allure.step("Вводим телефон: {phone}")
    def set_phone(self, phone):
        browser.element('#userNumber').type(phone)

    @allure.step("Устанавливаем дату рождения: {day}.{month}.{year}")
    def set_birthday(self, month, year, day):
        browser.element('#dateOfBirthInput').click()
        browser.element(f'.react-datepicker__month-select option[value="{month}"]').click()
        browser.element(f'.react-datepicker__year-select option[value="{year}"]').click()
        browser.element(f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)').click()

    @allure.step("Скроллим страницу")
    def scroll_page(self):
        browser.execute_script('window.scrollBy(0, 400);')

    @allure.step("Вводим предметы: {subjects}")
    def set_subjects(self, *subjects):
        for subject in subjects:
            browser.element('#subjectsInput').type(subject).press_enter()

    @allure.step("Выбираем хобби: {hobby_value}")
    def set_hobby(self, hobby_value):
        browser.element(f'[for="hobbies-checkbox-{hobby_value}"]').click()

    @allure.step("Загружаем изображение ")
    def upload_picture(self, path):
        browser.element("#uploadPicture").send_keys(
            os.path.abspath(os.path.join(os.path.dirname(__file__), f"../resources/{path}")))

    @allure.step("Вводим адрес: {address}, штат: {state}, город: {city}")
    def set_address(self, address, state, city):
        browser.element('#currentAddress').type(address)
        browser.element('#state').click().element(by.text(state)).click()
        browser.element('#city').click().element(by.text(city)).click()

    @allure.step("Нажимаем кнопку отправки формы")
    def click_submit_button(self):
        browser.element('#submit').click()

    @allure.step("Проверяем, что имя и фамилия заполнены: {Names}")
    def assert_filled_names(self, Names):
        browser.element('.table-responsive').should(have.text(Names))

    @allure.step("Проверяем наличие текста: {text}")
    def assert_text_present(self, text):
        browser.element('.table-responsive').should(have.text(text))

    @allure.step("Проверяем, что имя заполнено: {name}")
    def assert_filled_name(self, name):
        self.assert_text_present(name)

    @allure.step("Проверяем, что метка заполнена: {label}")
    def assert_filled_label(self, label):
        self.assert_text_present(label)

    @allure.step("Проверяем, что email заполнен: {email}")
    def assert_filled_email(self, email):
        self.assert_text_present(email)

    @allure.step("Проверяем, что пол заполнен: {gender}")
    def assert_filled_gender(self, gender):
        self.assert_text_present(gender)

    @allure.step("Проверяем, что телефон заполнен: {mobile}")
    def assert_filled_mobile(self, mobile):
        self.assert_text_present(mobile)

    @allure.step("Проверяем, что предмет заполнен: {subject}")
    def assert_filled_subject(self, subject):
        self.assert_text_present(subject)

    @allure.step("Проверяем, что хобби заполнены: {hobbies}")
    def assert_filled_hobbies(self, hobbies):
        self.assert_text_present(hobbies)

    @allure.step("Проверяем, что изображение заполнено: {picture}")
    def assert_filled_picture(self, picture):
        self.assert_text_present(picture)

    @allure.step("Проверяем, что адрес заполнен: {address}")
    def assert_filled_address(self, address):
        self.assert_text_present(address)

    @allure.step("Проверяем, что штат заполнен: {state}")
    def assert_filled_state(self, state):
        self.assert_text_present(state)

    @allure.step("Проверяем, что дата рождения заполнена: {day}")
    def assert_filled_birth(self, day):
        self.assert_text_present(day)
