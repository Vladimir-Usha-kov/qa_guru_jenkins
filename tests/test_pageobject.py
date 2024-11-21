import os

from pages.registration_page import RegisteationPage
import allure


@allure.story("Форма регистрации")
def test_student_registration_form(setup_browser):
    registration_page = RegisteationPage(browser=setup_browser)


    with allure.step("Открытие страницы demoqa"):
        registration_page.open()


    with allure.step("Заполнение формы"):
        (
            registration_page
            .fill_first_name('Vladimir')
            .fill_last_name('Ushakov')
            .fill_mail('test@mail.ru')
            .fill_gender('Male')
            .fill_phone('89937777777')
            .fill_birthday('1998', 'July', '27')
            .fill_subject('Computer Science')
            .fill_hobbies('Music')
            .fill_photo(os.path.abspath(f'resources/photo.jpg'))
            .fill_adress('street test 12')
            .fill_state('Haryana')
            .fill_city('Karnal')
            .submit()

        )

    with allure.step("Валидация формы"):
        registration_page.should_registred_user_info(
            'Vladimir Ushakov',
            'test@mail.ru',
            'Male',
            '8993777777',
            '27 July,1998',
            'Computer Science',
            'Music',
            'photo.jpg',
            'street test 12',
            'Haryana Karnal'

        )
