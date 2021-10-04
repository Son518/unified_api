from dataclasses import dataclass

@dataclass
class PostmarkBounce():
    
    record_type: str = None
    id: str = None
    type: str = None
    type_code: str = None
    name: str = None
    tag: str = None
    message_id: str = None
    server_id: str = None
    message_stream: str = None
    description: str = None
    details: str = None
    content: str = None
    email: str = None
    From: str = None
    bounced_at: str = None
    dump_available: str = None
    inactive: str = None
    canActivate: str = None
    subject: str = None
    metadata: str = None