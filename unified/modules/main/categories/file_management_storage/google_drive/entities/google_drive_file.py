from dataclasses import dataclass


@dataclass
class GoogledriveFile:
    file_id: str = None
    folder_id: str = None
    file_name: str = None
    file_content: str = None
    permission: str = None
    file_size: str = None
    media_mime_type: str = None
    file_url: str = None
