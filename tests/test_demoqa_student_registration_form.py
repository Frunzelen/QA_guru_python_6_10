import os

from selene import browser, be, have


# Preconditions
def test_for_registration_form_demoqa():
    browser.open('/automation-practice-form')

    # Test steps
    browser.should(have.title('DEMOQA'))
    browser.element('#firstName').type('Angelina')
    browser.element('#lastName').type('Jolie')
    browser.element('#userEmail').type('AngelinaJolie@email.ru')
    browser.all('#genterWrapper .custom-control').element_by(have.exact_text('Female')).click()
    browser.element('#userNumber').type('1234567890')
    browser.element('#dateOfBirthInput').click()
    browser.element('[value="1975"]').click()
    browser.element('[value="5"]').click()
    browser.element('[class="react-datepicker__day react-datepicker__day--004"]').click()
    browser.element('#subjectsInput').type('Biology').press_enter()
    browser.all('#hobbiesWrapper .custom-control')[0].click()
    browser.element('#uploadPicture').send_keys(os.getcwd() + '/resources/Angelina_Jolie.jpg')
    browser.element('#currentAddress').should(be.blank).type('Los Angeles')
    browser.element('#state').click()
    browser.all("#state div").element_by(have.exact_text("NCR")).click()
    browser.element('#city').click()
    browser.all("#city div").element_by(have.exact_text("Delhi")).click()
    browser.element('#submit').click()

    # Expected Result
    browser.element('.modal-header').should(have.exact_text('Thanks for submitting the form'))
    browser.all('.modal-body tr td')[1].should(have.exact_text('Angelina Jolie'))
    browser.all('.modal-body tr td')[3].should(have.exact_text('AngelinaJolie@email.ru'))
    browser.all('.modal-body tr td')[5].should(have.exact_text('Female'))
    browser.all('.modal-body tr td')[7].should(have.exact_text('1234567890'))
    browser.all('.modal-body tr td')[9].should(have.exact_text('04 June,1975'))
    browser.all('.modal-body tr td')[11].should(have.exact_text('Biology'))
    browser.all('.modal-body tr td')[13].should(have.exact_text('Sports'))
    browser.all('.modal-body tr td')[15].should(have.exact_text('Angelina_Jolie.jpg'))
    browser.all('.modal-body tr td')[17].should(have.exact_text('Los Angeles'))
    browser.all('.modal-body tr td')[19].should(have.exact_text('NCR Delhi'))

    # Completing the test
    browser.element('#closeLargeModal').click()
    browser.element('.modal-dialog').should(be.absent)
    browser.element('#firstName').should(be.blank)
