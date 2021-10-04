from dataclasses import dataclass
from project_management.entities.comment import Comment


@dataclass
class PodioComment(Comment):

    comment_text: str = None
    task_id: str = None
    file_url: str = None
    weblink_url: str = None
    answer: str = None
