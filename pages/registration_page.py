import os

from selene import browser, command, have, be


from demoqa_test import resource



class RegisteationPage:

    def __init__(self, browser):
        self.city = browser.element('#city')
        self.state = browser.element('#state')
        self.browser = browser


    def open(self):
        self.browser.open('https://demoqa.com/automation-practice-form')
        return self

    def fill_first_name(self, value):
        browser.element('#firstName').should(be.blank).type(value)
        return self
    def fill_last_name(self, value):
        browser.element('#lastName').should(be.blank).type(value)
        return self

    def fill_mail(self, value):
        browser.element('#userEmail').type(value)
        return self
    def fill_gender(self, value):
        browser.all('[name=gender]').element_by(have.value(value)).element('..').click()
        return self
    def fill_phone(self, nubmer):
        browser.element('#userNumber').type(nubmer)
        return self

    def fill_subject(self, subject):
        browser.element('#subjectsInput').send_keys(subject).press_tab()
        return self

    def fill_hobbies(self, hobbies):
        browser.all('#hobbiesWrapper .custom-control-label').element_by(have.exact_text(hobbies)).click()
        return self

    def fill_photo(self, photo):
        browser.element('#uploadPicture').send_keys(photo)
        return self

    # def path(file_name):
    # return (os.path.abspath(f'resources/{file_name}'))

    def fill_adress(self, adress):
        browser.element('#currentAddress').type(adress)
        return self

    def fill_city(self, city):
        self.city.perform(command.js.scroll_into_view)
        self.city.click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(city)).click()
        return self

    def fill_birthday(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').send_keys(month)
        browser.element('.react-datepicker__year-select').send_keys(year)
        browser.element(f'.react-datepicker__day--0{day}').click()
        return self

    def fill_state(self, state):
        self.state.perform(command.js.scroll_into_view)
        self.state.click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(state)).click()
        return self

    def submit(self):
        browser.element('#submit').click()

    def should_registred_user_info(self, full_name, mail, gender, phone, birth, hob, hobbies, upload, adress, home):
        browser.all('.table-responsive .table td:nth-child(2)').should(have.exact_texts(
            f'{full_name}',
            f'{mail}',
            f'{gender}',
            f'{phone}',
            f'{birth}',
            f'{hob}',
            f'{hobbies}',
            f'{upload}',
            f'{adress}',
            f'{home}'

        )
        )


