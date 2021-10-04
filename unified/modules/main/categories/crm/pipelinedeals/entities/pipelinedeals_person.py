from crm.entities.contact import Contact
from dataclasses import dataclass

@dataclass
class PipelinedealsPerson(Contact):

    person_id: str = None
    first_name: str = None
    mobile: str = None
    last_name: str = None
    phone: str = None
    position: str = None
    website: str = None
    email: str = None
    company: str = None
    type: str = None
    work_address: str = None
    work_city: str = None
    work_state: str = None
    work_postal_code: str = None
    work_country: str = None
    home_address: str = None
    home_city: str = None
    home_state: str = None
    home_country: str = None
    home_postal_code: str = None
    status_id: str = None
    source_id: str = None
    summary: str = None
    image_url: str = None
    facebook_url: str = None
    linkedin_url: str = None
    twitter_username: str = None