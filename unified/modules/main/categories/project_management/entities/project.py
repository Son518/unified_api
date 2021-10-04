from dataclasses import dataclass, field


@dataclass
class Project:
    id: str = None
    project_name: str = None
    project_description: str = None
    status: str = None
    created_date: str = None
    updated_date: str = None
    
    # def __repr__(self):
    #     return f'{{"id":"{self.id}","project_name":"{self.project_name}","project_description":"{self.project_description}","status":"{self.status}","created_date":"{self.created_date}","updated_date":"{self.updated_date}"}}'