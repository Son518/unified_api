from dataclasses import dataclass


@dataclass
class Email:
    email_id: str = None
    to: str = None
    subject: str = None
    body: str = None
    body_format: str = None
    cc: list = None
    bcc: list = None
