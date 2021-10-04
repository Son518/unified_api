from dataclasses import dataclass
from crm.entities.account import Account


@dataclass
class CoppercrmAccount(Account):
    email_domain: str = None
    assignee: str = None
    contact_type: str = None
    title: str = None
    social_profiles: str = None
    tags: str = None
    match_by_type: str = None
    match_by_value: str = None
    subscription_id: str = None
    replace_or_append_tags: str = None
    event: str = None
    type: str = None
    ids: str = None
    updated_attributes: str = None