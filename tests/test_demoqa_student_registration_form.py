import datetime

from demoqa.data.users import User
from demoqa.pages.registration_page import RegistrationPage

def test_for_registration_form_demoqa():
    registration_page = RegistrationPage()

    Angelina = User(
        first_name='Angelina',
        last_name='Jolie',
        email='AngelinaJolie@email.ru',
        gender='Female',
        mobile_number='1234567890',
        date_of_birth=datetime.date(year=1975, month=5, day=4),
        subjects='Biology',
        hobbies='Sports',
        picture='Angelina_Jolie.jpg',
        address='Los Angeles, Borogodskaya, 17',
        state="NCR",
        city="Delhi"
    )

    registration_page.open()
    registration_page.register(Angelina)
    registration_page.should_have_registered(Angelina)

    registration_page.close_modal()

