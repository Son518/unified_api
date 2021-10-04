from dataclasses import dataclass


@dataclass
class FreshserviceRequester:

    requester_id: str = None
    name: str = None
    email: str = None
    address: str = None
    background_information: str = None
    phone: str = None
    job_title: str = None
