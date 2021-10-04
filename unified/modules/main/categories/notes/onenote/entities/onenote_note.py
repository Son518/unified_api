from dataclasses import dataclass

@dataclass
class OnenoteNote():
    
    content_type: str = None
    content: str = None
    title: str = None
    body: str = None