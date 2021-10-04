from dataclasses import dataclass


@dataclass
class SmartsheetSendRow:
    email_address: str = None
    row_id: str = None
    sheet_id: str = None
    subject: str = None
    message: str = None
    include_attachments: str = None
    include_discussions: str = None
    cc_me: str = None
    access_level: str = None
    notify_via_email: str = 'no'
    format: str = 'pdf'
    paper_size: str = 'a4'
    workspace_id:str=None
