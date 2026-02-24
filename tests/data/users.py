from enum import Enum
from dataclasses import dataclass
from datetime import date


class Gender(Enum):
    MALE = 'Male'
    FEMALE = 'Female'
    OTHER = 'Other'

class Hobbies(Enum):
    SPORTS = 'Sports'
    READING = 'Reading'
    MUSIC = 'Music'

@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: Gender
    mobile_phone: str
    date_of_birth: date
    subject: str
    hobbies: list[Hobbies]
    picture: str
    address: str
    state: str
    city: str

student = User(
    first_name='Seyfi',
    last_name='Ismailov',
    email='seyfullahismailly@gmail.com',
    gender=Gender.MALE,
    mobile_phone='9219212121',
    date_of_birth=date(1993, 8, 21),
    subject='English',
    hobbies=[Hobbies.SPORTS],
    picture='foto.jpg',
    address='Ushinskogo street, 3',
    state='NCR',
    city='Delhi'
)
