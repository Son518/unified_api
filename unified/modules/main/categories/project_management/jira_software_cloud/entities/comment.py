from dataclasses import dataclass


@dataclass
class JiraSoftwareCloudComment:
    issue_id: str = None
    comment_id: str = None
    comment_description: str = None
    site_id: str = None
    author_id: str = None
    issue_name: str = None
    comment: str = None
