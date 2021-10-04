from dataclasses import dataclass
from project_management.entities.project import Project
@dataclass
class ProjectslyProjects(Project):
    icon:str=None
    color:str=None
    member_id:str=None
    is_public:str=None