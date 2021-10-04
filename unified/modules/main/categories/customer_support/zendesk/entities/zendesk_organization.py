from dataclasses import dataclass


@dataclass
class ZendeskOrganization():

    name: str = None
    details: str = None
    notes: str = None
    tags: str = None
    domain_names: str = None
    external_id: str = None
    shared_tickets: str = None
    shared_comments: str = None
    organization_id: str = None
    created_date: str = None
