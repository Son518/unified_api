from dataclasses import dataclass

@dataclass
class OnenoteAppend():
    
    content_type: str = None
    content: str = None
    section_id: str = None
    page_id: str = None
    notebook_id: str = None