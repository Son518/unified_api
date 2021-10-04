from dataclasses import dataclass


@dataclass
class SmartsheetComment:
    comment_id: str = None
    discussion_id: str = None
    comment: str = None
    created_by: str = None
