import os
import tests
from selene import browser, be, have, command


# Preconditions
def test_for_registration_form_demoqa():
    browser.open('/automation-practice-form')
    browser.element('footer').execute_script('element.remove()')

    # Test steps
    browser.should(have.title('DEMOQA'))
    browser.element('#firstName').type('Angelina')
    browser.element('#lastName').type('Jolie')
    browser.element('#userEmail').type('AngelinaJolie@email.ru')
    browser.all('[name=gender]').element_by(have.value('Female')).element('..').click()
    browser.element('#userNumber').type('1234567890')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').type('1975')
    browser.element('.react-datepicker__month-select').type('June')
    browser.element(f'.react-datepicker__day--00{4}').click()
    browser.element('#subjectsInput').type('Biology').press_enter()
    browser.all('.custom-checkbox').element_by(have.text('Sports')).click()
    browser.element('#uploadPicture').set_value(os.path.abspath(
        os.path.join(os.path.dirname(tests.__file__), 'resources/Angelina_Jolie.jpg')))
    browser.element('#currentAddress').should(be.blank).type(
        'Los Angeles, Borogodskaya, 15')
    browser.element('#state').click()
    browser.all('[id^=react-select][id*=option]').element_by(
        have.exact_text("NCR")).click()
    browser.element('#city').click()
    browser.all('[id^=react-select][id*=option]').element_by(
        have.exact_text("Delhi")).click()
    browser.element('#submit').perform(command.js.click)

    # Expected Result
    browser.element('.modal-header').should(
        have.exact_text('Thanks for submitting the form'))
    browser.all('.modal-body tr td')[1].should(have.exact_text('Angelina Jolie'))
    browser.all('.modal-body tr td')[3].should(
        have.exact_text('AngelinaJolie@email.ru'))
    browser.all('.modal-body tr td')[5].should(have.exact_text('Female'))
    browser.all('.modal-body tr td')[7].should(have.exact_text('1234567890'))
    browser.all('.modal-body tr td')[9].should(have.exact_text('04 June,1975'))
    browser.all('.modal-body tr td')[11].should(have.exact_text('Biology'))
    browser.all('.modal-body tr td')[13].should(have.exact_text('Sports'))
    browser.all('.modal-body tr td')[15].should(have.exact_text('Angelina_Jolie.jpg'))
    browser.all('.modal-body tr td')[17].should(
        have.exact_text('Los Angeles, Borogodskaya, 15'))
    browser.all('.modal-body tr td')[19].should(have.exact_text('NCR Delhi'))

    # Completing the test
    browser.element('#closeLargeModal').click()
    browser.element('.modal-dialog').should(be.absent)
    browser.element('#firstName').should(be.blank)
