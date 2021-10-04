from dataclasses import dataclass


@dataclass
class GoogledocsDocument:
    template_id: str = None
    name: str = None
    content: str = None
    text_to_append: str = None
    folder_id: str = None
    document_id: str = None
    media_mime_type: str = None
    permission: str = None
    document_size: str = None
