from dataclasses import dataclass

@dataclass
class TodoistUpdateTask():

     task_id: str = None
     title: str = None
     assigned_to: str = None
     due_date: str = None
     priority: str = None
     label_id: str = None
     content: str = None