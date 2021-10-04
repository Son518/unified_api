from dataclasses import dataclass


@dataclass
class Basecamp3Message:
    project_id: str = None
    message_board_id: str = None
    subject: str = None
    content: str = None
    status: str = None
    created_date:str= None
