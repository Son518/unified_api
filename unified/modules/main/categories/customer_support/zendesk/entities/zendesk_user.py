from dataclasses import dataclass


@dataclass
class ZendeskUser():

    name: str = None
    email: str = None
    details: str = None
    notes: str = None
    phone: str = None
    tags: str = None
    role: str = None
    organization_id: str = None
    external_id: str = None
    user_id: str = None
    created_date: str = None
    updated_date: str = None
