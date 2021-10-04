from dataclasses import dataclass
from crm.entities.contact import Contact


@dataclass
class CoppercrmContact(Contact):
    full_name: str = None
    middle_name: str = None
    name_suffix: str = None
    name_prefix: str = None
    assignee: str = None
    status: str = None
    company: str = None
    title: str = None
    descrption: str = None
    contact_type: str = None
    phone_number: str = None
    social_profiles: str = None
    website: str = None
    street: str = None
    city: str = None
    state: str = None
    zipcode: str = None
    country: str = None
    tags: str = None
    match_by_type: str = None
    match_by_value: str = None
    replace_or_append_tags: str = None
    mailing_stree: str = None
    subscription_id: str = None
    event: str = None
    type: str = None
    ids: str = None
    updated_attributes: str = None
