from dataclasses import dataclass


@dataclass
class SmartsheetSheet:
    source_sheet_id: str = None
    folder_id: str = None
    workspace_id: str = None
    template_id: str = None
    copy_cells: str = None
    copy_attachments: str = None
    copy_discussions: str = None
    sheet_name: str = None
