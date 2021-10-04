from dataclasses import dataclass


@dataclass
class JiraSoftwareCloudUsers:
    user_id: str = None
    email: str = None
    name: str = None
    is_active: bool = False
