from dataclasses import dataclass


@dataclass
class HelpscoutCustomer():

    first_name: str = None
    last_name: str = None
    email: str = None
    phone: str = None
    website: str = None
    organization: str = None
    location: str = None
    job_title: str = None
    address: str = None
    city: str = None
    state: str = None
    pin_code: str = None
    country: str = None
    customer_id: str = None
