from dataclasses import dataclass
from social_media.entities.page import Page


@dataclass
class Facebookpages_page(Page):
    page_data: list = None
    page_id: str = None
    message: str = None
    link_url: str = None
    description: str = None
    photo_url: str = None
    video_url: str = None
    title: str = None
    photo_url: str = None
