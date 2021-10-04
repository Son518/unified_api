from dataclasses import dataclass


@dataclass
class SmartsheetCopyRow:
    source_sheet_id: str = None
    destination_sheet_id: str = None
    row_id: str = None
