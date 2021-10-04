from dataclasses import dataclass

@dataclass
class FreshdeskForum():
    forum_category: str = None
    name: str = None
    type: str = None
    visibility: str = None
    description: str = None
    forum: str = None
    title: str = None
    topic_description: str = None
    sticky: bool = False
    locked: bool = False