from dataclasses import dataclass

@dataclass
class KeapNote():

    contact_id: str = None
    title: str = None
    description: str = None
    created_by: str = None
