from dataclasses import dataclass

@dataclass
class FreshdeskContact():
    name: str = None
    email: str = None
    address: str = None
    description: str = None
    phone: str = None
    job_title: str = None
    tags: str = None
    contact_id: str = None