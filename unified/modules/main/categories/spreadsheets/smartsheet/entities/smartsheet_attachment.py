from dataclasses import dataclass


@dataclass
class SmartsmartAttachment:
    name: str = None
    description: str = None
    attachment_url: str = None
    row_id: str = None
    sheet_id: str = None
    attachment_type: str = None
    mime_type: str = None
    attachment_id: str = None
