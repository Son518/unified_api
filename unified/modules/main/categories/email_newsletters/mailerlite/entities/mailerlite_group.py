from email_newsletters.entities.group import Group
from dataclasses import dataclass


@dataclass
class MalierliteGroup(Group):

    email: str =  None
    subscriber_id: str = None
    group_name: str = None
    remove_member_from_group: str = None
    subscriber_group: str = None
    subscriber_group_id: str = None
    last_name: str = None
    state: str = None
    pin_code: str = None
    company: str = None
    country: str = None
    city: str = None
    phone: str = None
    date_created: str = None
    date_updated: str = None