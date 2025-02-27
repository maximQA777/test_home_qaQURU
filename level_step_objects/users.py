from dataclasses import dataclass
import os


@dataclass
class User:
    firstName: str
    lastName: str
    email: str
    gender: str
    mobile: str
    birth_day: str
    birth_month: str
    birth_year: str
    subjects: str
    hobby: str
    picture: str
    address: str
    state: str
    city: str


test_user = User(firstName='Maxim', lastName='Lerich', email='alab@mail.me', gender='Female', mobile='3123213131',
                 birth_day='15', birth_month='8', birth_year='1999', subjects= 'Math', hobby='Sports',
                 picture='picture.png', address='Kabanina Polina', state=' NCR', city='Delhi')