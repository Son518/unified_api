from dataclasses import dataclass
from emails.entities.email_entities import Email


@dataclass
class Gmail(Email):

    from_email: str = None
    from_name: str = None
    body_type: str = None
    signature: str = None
    label: str = None
    attachments: str = None
    thread_id: str = None
    message_id: str = None
    references: str = None
    in_reply_to: str = None
