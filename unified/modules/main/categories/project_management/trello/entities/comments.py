from dataclasses import dataclass


@dataclass
class TrelloComment:
    card_id: str = None
    comment_description: str = None
    board_id: str = None
    created_date: str = None
    comment_id: str = None
    list_id: str = None
