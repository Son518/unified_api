from dataclasses import dataclass

@dataclass
class InstagramPublishPhoto:
    instagram_account_id: str = None
    photo_url: str = None
    caption: str = None
    tagged_users: str = None
    location: str = None
