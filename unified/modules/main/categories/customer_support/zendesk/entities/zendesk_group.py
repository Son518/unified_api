from dataclasses import dataclass


@dataclass
class ZendeskGroup():

    created_date: str = None
    default: bool = False,
    deleted: bool = False,
    description: str = None
    group_id: str = None
    group_name: str = None
    updated_date: str = None
    url: str = None
