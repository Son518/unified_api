from dataclasses import dataclass
from project_management.entities.project import Project


@dataclass
class Basecamp3Project(Project):
    message_board_id: str = None
    todoset_id: str = None
    file_id: str = None
    chat_id: str = None
    schedule_id: str = None
    questionnaire_id: str = None
