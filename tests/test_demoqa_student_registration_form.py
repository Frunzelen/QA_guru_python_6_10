from selene import browser, be, have, command

from demoqa.pages.registration_page import RegistrationPage


def test_for_registration_form_demoqa():
    # GIVEN
    registration_page = RegistrationPage()
    registration_page.open()

    # WHEN
    (registration_page
    .fill_first_name('Angelina')
    .fill_last_name('Jolie')
    .fill_email('AngelinaJolie@email.ru')
    .fill_gender('Female')
    .fill_mobile_number('1234567890')
    .fill_date_of_birth('4', 'June', '1975')
    .fill_subjects('Biology')
    .fill_hobbies('Sports')
    .select_picture('Angelina_Jolie.jpg')
    .fill_address('Los Angeles, Borogodskaya, 17')
    .fill_state("NCR")
    .fill_city("Delhi")
    .submit_form()
     )

    # THEN
    registration_page.should_have_text('Thanks for submitting the form')
    registration_page.registered_user_data.should(
        have.exact_texts(
            'Angelina Jolie',
            'AngelinaJolie@email.ru',
            'Female',
            '1234567890',
            '04 June,1975',
            'Biology',
            'Sports',
            'Angelina_Jolie.jpg',
            'Los Angeles, Borogodskaya, 17',
            'NCR Delhi')
    )

    # WHEN
    registration_page.close()

    # THEN
    registration_page.cleared_registration_form()