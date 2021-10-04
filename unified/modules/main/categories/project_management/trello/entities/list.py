from dataclasses import dataclass

@dataclass
class TrelloList:
    board_id:str=None
    name:str=None
    list_id:str=None
