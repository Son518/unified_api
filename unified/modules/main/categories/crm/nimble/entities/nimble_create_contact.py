from dataclasses import dataclass
from crm.nimble import util

@dataclass
class NimbleContact():
    
    record_type : str = None
    first_name : str = None
    last_name : str = None
    birthday : str = None
    company_name: str = None
    title: str = None
    email_personal: str = None
    phone_mobile: str = None
    skype_id: str = None
    address_street_home: str = None
    address_city_home: str = None
    address_state_home: str = None
    address_zip_home: str = None
    address_country_home: str = None
    url_work: str = None
    description_other: str = None
    facebook: str = None
    linkedin: str = None
    twitter: str = None
    record_type: str = None
    modifier: str = None
    value: str = None
    tags: str = None
    fields: str = None

    def __post_init__(self):
        if not (self.birthday is None or "-" in self.birthday):
            format = "%Y-%m-%dT%H:%M:%S"
            self.birthday = util.epoch_to_format(format, self.birthday)
