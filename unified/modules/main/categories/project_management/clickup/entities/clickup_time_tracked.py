from dataclasses import dataclass

@dataclass
class ClikupTimeTracked:
    start_date: str = None
    due_date: str = None
    task_id: str = None
