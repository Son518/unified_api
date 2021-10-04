from dataclasses import dataclass
from crm.entities.lead import Lead


@dataclass
class CoppercrmLead(Lead):

    full_name: str = None
    middle_name: str = None
    name_prefix: str = None
    name_suffix: str = None
    assignee: str = None
    status: str = None
    company: str = None
    descrption: str = None
    monetary_value: str = None
    currency: str = None
    customer_source: str = None
    phone_number: str = None
    social_profiles: str = None
    zipcode: str = None
    country: str = None
    tags: str = None
    match_by_type: str = None
    match_by_value: str = None
    replace_or_append_tags: str = None
    value: str = None
    subscription_id: str = None
    event: str = None
    type: str = None
    ids: str = None
    updated_attributes: str = None