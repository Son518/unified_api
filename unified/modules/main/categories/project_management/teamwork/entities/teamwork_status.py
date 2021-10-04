from dataclasses import dataclass

@dataclass
class TeamworkStatus():

    id: str = None
    user_id: str = None
    date: str = None
    message: str = None