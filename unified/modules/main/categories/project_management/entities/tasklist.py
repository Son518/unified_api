from dataclasses import dataclass

@dataclass
class Tasklist:
    id :str = None
    name :str = None
    description:str = None
    project_id:str = None
