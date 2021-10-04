from dataclasses import dataclass


@dataclass
class Basecamp3FileUpload:
    id: str = None
    title: str = None
    notes: str = None
    type: str = None
    doc_file_id: str = None
    project_id: str = None
    uploaded_by: str = None
    created_date: str = None
