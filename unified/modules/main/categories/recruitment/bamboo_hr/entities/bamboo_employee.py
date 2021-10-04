from dataclasses import dataclass, field
from recruitment.bamboo_hr import util

@dataclass
class BambooEmployee():

    employee_id: str = None
    first_name: str = None
    last_name: str = None
    date_of_birth: str = None
    address1: str = None
    address2: str = None
    city: str = None
    state: str = None
    zip_code: str = None
    country: str = None
    hire_date: str = None
    work_email: str = None

    def __post_init__(self):
        self.date_of_birth = util.date_to_epoch(self.date_of_birth)
        self.hire_date = util.date_to_epoch(self.hire_date)
