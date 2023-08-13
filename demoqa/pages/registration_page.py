from selene import browser, be, have, command
from demoqa.data.users import User
from demoqa.resources import path


class RegistrationPage:

    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.email = browser.element('#userEmail')
        self.gender = browser.all('[name=gender]')
        self.mobile_number = browser.element('#userNumber')
        self.subjects = browser.element('#subjectsInput')
        self.hobbies = browser.all('#hobbiesWrapper label')
        self.picture = browser.element('#uploadPicture')
        self.address = browser.element('#currentAddress')
        self.submit = browser.element('#submit')

    def open(self):
        browser.open('https://demoqa.com/automation-practice-form/')
        browser.execute_script('document.querySelector("#fixedban").remove()')
        browser.element('footer').execute_script('element.remove()')
        return self

    def register(self, user: User):
        self.first_name.type(user.first_name)
        self.last_name.type(user.last_name)
        self.email.type(user.email)
        self.gender.element_by(have.value(user.gender)).element('..').click()
        self.mobile_number.type(user.mobile_number)
        self.fill_date_of_birth(user.date_of_birth)
        self.subjects.type(user.subjects).press_enter()
        self.hobbies.element_by(have.text(user.hobbies)).click()
        self.picture.send_keys(path(user.picture))
        self.address.type(user.address)
        self.fill_state(user.state)
        self.fill_city(user.city)
        self.submit_form()
        return self

    def fill_date_of_birth(self, date):
        year = date.year
        month = date.month - 1
        day = date.strftime('%d')
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element(
            f'.react-datepicker__year-select option[value="{year}"]').click()
        browser.element('.react-datepicker__month-select').click()
        browser.element(
            f'.react-datepicker__month-select option[value="{month}"]').click()
        browser.element(f'.react-datepicker__day--0{day}').click()
        return self

    def fill_state(self, value):
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(value)).click()
        return self

    def fill_city(self, value):
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(value)).click()
        return self

    def submit_form(self):
        browser.element('#submit').perform(command.js.click)
        return self

    def should_have_registered(self, user):
        browser.element('.table').all('td').even.should(have.exact_texts(
            f'{user.first_name} {user.last_name}',
            f'{user.email}',
            f'{user.gender}',
            f'{user.mobile_number}',
            '{0} {1},{2}'.format(user.date_of_birth.strftime("%d"),
                                 user.date_of_birth.strftime("%B"),
                                 user.date_of_birth.year),
            f'{user.subjects}',
            f'{user.hobbies}',
            f'{user.picture}',
            f'{user.address}',
            f'{user.state} {user.city}'
        ))

    def close_modal(self):
        browser.element('#closeLargeModal').should(have.exact_text('Close')).click()
        browser.element('.modal-dialog').should(be.absent)
        browser.element('#firstName').should(be.blank)
