from dataclasses import dataclass
from project_management.entities.project import Project


@dataclass
class WrikeProject(Project):

    project_title: str = None
    event_author_id: str = None
    event_type: str = None
    updated_date: str = None
    folder_name: str = None
    folder_description: str = None
    parent_folder_id: str = None
