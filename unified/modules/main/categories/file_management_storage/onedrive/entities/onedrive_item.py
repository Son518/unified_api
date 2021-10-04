from dataclasses import dataclass


@dataclass
class OnedriveItem:

    id: str = None
    name: str = None
    web_url: str = None
    created_by: dict = None