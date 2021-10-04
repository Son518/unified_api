from dataclasses import dataclass

@dataclass
class PostmarkSendEmail():
    
    from_email_address: str = None
    to_email_address: str = None
    cc_email_address: str = None
    bcc_email_address: str = None
    email_subject: str = None
    text_email_body: str = None
    html_email_body: str = None
    message_stream: str = None
    