from dataclasses import dataclass


@dataclass
class SmartsheetCopyFolder:
    source_folder_id: str = None
    new_folder_name: str = None
    destination_folder_id: str = None
    what_to_include: list = None
    skip_remap: list = None
