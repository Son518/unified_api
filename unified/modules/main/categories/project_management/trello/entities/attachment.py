from dataclasses import dataclass


@dataclass
class TrelloAttachment:
    attachment_id: str = None
    user_id: str = None
    mimetype: str = None
    name: str = None
    attachment_url: str = None
