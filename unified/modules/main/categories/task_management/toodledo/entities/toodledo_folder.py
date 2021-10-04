from dataclasses import dataclass
from task_management.toodledo import util

@dataclass
class ToodledoFolder():

    name: str = None
    private: bool= None