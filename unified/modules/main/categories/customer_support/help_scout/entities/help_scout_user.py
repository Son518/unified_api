from dataclasses import dataclass


@dataclass
class HelpscoutUser():

    email: str = None
    first_name: str = None
    user_id: str = None
    initials: str = None
    job_title: str = None
    last_name: str = None
    phone: str = None
    role: str = None
