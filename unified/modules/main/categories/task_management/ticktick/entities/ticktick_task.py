from dataclasses import dataclass
from task_management.ticktick import util

@dataclass
class TicktickTask():
    
    list_id: str = None
    name: str = None
    content: str = None
    start_date: str = None
    due_date: str = None
    priority: str = None
    file_url: str = None
    task_id: str = None
    file: str = None
    timezone: str = None