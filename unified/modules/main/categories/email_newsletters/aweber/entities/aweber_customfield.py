from dataclasses import dataclass


@dataclass
class AweberCustomfield:
    custom_field_id: str = None
    is_subscriber_updateable: bool = False
    name: str = None
