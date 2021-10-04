from dataclasses import dataclass
from social_media.pinterest import util

@dataclass
class PinterestPin():
    
    board_id: str = None
    image_url: str = None
    link: str = None
    title: str = None
    description: str = None
    source_type: str = None