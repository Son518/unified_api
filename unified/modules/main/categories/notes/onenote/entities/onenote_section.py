from dataclasses import dataclass

@dataclass
class OnenoteSection():
    
    content_type: str = None
    content: str = None
    title: str = None
    body: str = None
    notebook_id: str = None
    section_id: str = None