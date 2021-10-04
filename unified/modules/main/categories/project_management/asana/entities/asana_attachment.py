from dataclasses import dataclass
from project_management.entities.attachment import Attachment

@dataclass
class AsanaAttachment(Attachment):
    download_url: str = None
    task_id: str = None
    task_name: str = None
    permanent_url: str = None
