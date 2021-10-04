from dataclasses import dataclass


@dataclass
class TrelloActivity:
    card_id: str = None
    board_id: str = None
    card_name: str = None
    board_name: str = None
    checklist_id: str = None
    checklist_item: str = None
    attachment_name: str = None
    attachment_url: str = None
