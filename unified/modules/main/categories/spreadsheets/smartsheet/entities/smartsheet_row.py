from dataclasses import dataclass


@dataclass
class SmartsheetRow:
    row_number: str = None
    row_id: str = None
    sheet_id: str = None
    comment: str = None
    to_top: bool = False
    to_bottom: bool = False
    cells: list = None
