from dataclasses import dataclass

@dataclass
class HarvestTask:
    task_id: str = None
    project_id: str = None
    task_name: str = None