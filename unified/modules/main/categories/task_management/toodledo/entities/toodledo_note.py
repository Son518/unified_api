from dataclasses import dataclass
from task_management.toodledo import util

@dataclass
class ToodledoNote():

    folder_id: str = None
    note_title: str = None
    private: str = None
    note_text: str = None