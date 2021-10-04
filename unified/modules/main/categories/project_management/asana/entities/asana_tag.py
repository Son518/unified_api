from dataclasses import dataclass, field
from project_management.entities.tag import Tag


@dataclass
class AsanaTag(Tag):
    color: str = None
    followers: str = None
    workspace_id: str = None
    workspace_name: str = None