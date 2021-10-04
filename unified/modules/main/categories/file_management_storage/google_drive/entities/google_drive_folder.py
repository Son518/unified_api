from dataclasses import dataclass


@dataclass
class GoogledriveFolder:
    parent_folder_id: str = None
    folder_name: str = None
    folder_id: str = None
    permission: str = None
    media_mime_type: str = None
