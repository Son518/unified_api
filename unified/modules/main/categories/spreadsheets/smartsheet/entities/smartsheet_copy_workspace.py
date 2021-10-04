from dataclasses import dataclass

@dataclass
class SmartsheetCopyWorkspace:
    workspace_id: str = None
    new_workspace_name: str = None
    what_to_include: list = None
    skip_remap: list = None
