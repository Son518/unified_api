from dataclasses import dataclass


@dataclass
class SurveymonkeyContact():
    first_name: str = None
    last_name: str = None
    email: str = None
    contact_list_id: str = None
    phone_number: str = None