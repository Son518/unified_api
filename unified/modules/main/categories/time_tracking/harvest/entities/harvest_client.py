from dataclasses import dataclass

@dataclass
class HarvestClient:
    client_id: str = None
    name: str = None
    extra_information: str = None