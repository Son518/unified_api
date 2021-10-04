from dataclasses import dataclass

@dataclass
class TeamworkNotebook():

    id: str = None
    name: str = None
    description: str = None
    tags: str = None
    category_id: str = None
    project_id: str = None
    created_date: str = None
    version: str = None
    version_id: str = None