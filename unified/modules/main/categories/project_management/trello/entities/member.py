from dataclasses import dataclass


@dataclass
class TrelloMember:
    user_id: str = None
    card_id: str = None
    name: str = None
    confirmed: str = None
    board_id:str=None
