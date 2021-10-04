from dataclasses import dataclass


@dataclass
class TrelloLable:
    board_id: str = None
    name: str = None
    color: str = None
    card_id: str = None
    label_id: str = None
