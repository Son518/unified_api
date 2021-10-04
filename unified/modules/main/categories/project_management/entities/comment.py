from dataclasses import dataclass, field


@dataclass
class Comment:

    id: str = None
    comment_description: str = None
    task_id: str = None
    project_id: str = None
    comment_by:str = None