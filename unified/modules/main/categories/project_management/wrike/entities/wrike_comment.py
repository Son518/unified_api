from dataclasses import dataclass
from project_management.entities.comment import Comment


@dataclass
class WrikeComment(Comment):
    
    eventAuthorId: str = None
    eventType: str = None
    lastUpdatedDate: str = None
    folder_id: str = None
    comment_text: str = None
    attachment_url: str = None
