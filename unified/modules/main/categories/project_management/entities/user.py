from dataclasses import dataclass

@dataclass
class User:
    id: str = None
    first_name: str = None
    last_name: str = None
    email: str = None
    avatar_url: str = None
