from dataclasses import dataclass

@dataclass
class TodoistCommentTask():

     task_id: str = None
     comment: str = None