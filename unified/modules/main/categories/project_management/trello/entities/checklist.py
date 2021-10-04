from dataclasses import dataclass


@dataclass
class TrelloChecklist:
    card_id: str = None
    name: str = None
    checklist_id: str = None
    board_id:str=None

