from dataclasses import dataclass


@dataclass
class MediumStory():
    title: str = None
    format: str = None
    content: str = None
    subtitle: str = None
    tags: str = None
    canonical_url: str = None
    publish_status: str = None
    license: str = None
    notify_followers: str = None
