from dataclasses import dataclass


@dataclass
class Basecamp3Document:
    id: str = None
    title: str = None
    content: str = None
    type: str = None
    folder_id: str = None
    project_id: str = None
    uploaded_by: str = None
    created_date: str = None
    account_id: str = None
    status: str = "active"
