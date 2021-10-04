from dataclasses import dataclass

@dataclass
class LinkedinShare():
    comment:str = None
    visible_to:str = None
    title:str = None
    description:str = None
    content_image_url:str = None
    url:str = None