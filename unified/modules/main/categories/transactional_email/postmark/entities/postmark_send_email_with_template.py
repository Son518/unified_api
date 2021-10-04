from dataclasses import dataclass

@dataclass
class PostmarkTemplate():
    
    from_address: str = None
    to_recipients: str = None
    cc_recipients: str = None
    bcc_recipients: str = None
    template_id: str = None
    template_model: str = None
    message_stream: str = None
