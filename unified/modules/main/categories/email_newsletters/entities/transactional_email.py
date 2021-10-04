from dataclasses import dataclass


@dataclass
class Transactionalemail:
    subject: str = None
    reply_to: str = None
    to: str = None
    cc: str = None
    bcc: str = None
    email_text_body: str = None
    email_body: str = None
    from_email: str = None
