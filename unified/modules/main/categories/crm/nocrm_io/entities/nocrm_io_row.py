from dataclasses import dataclass


@dataclass
class NoCRMioRow():

    prospecting_list_id: str = None
    name: str = None
    first_name: str = None
    last_name: str = None
    phone: str = None
    email: str = None
