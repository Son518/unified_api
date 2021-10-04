from dataclasses import dataclass
from project_management.pivotal_tracker import util

@dataclass
class PivotaltrackerActivity:

    kind: str = None
    guid: str = None
    project_version: str = None
    message: str = None
    highlight: str = None
    changes: str = None
    change_type: str = None
    id: str = None
    new_values: str = None
    story_id: str = None
    text: str = None
    person_id: str = None
    created_at: str = None
    updated_at: str = None
    file_attachment_ids: str = None
    google_attachment_ids: str = None
    attachment_ids: str = None
    file_attachments: str = None
    google_attachments: str = None
    filename: str = None
    uploader_id: str = None
    thumbnailable: str = None
    height: str = None
    width: str = None
    size: str = None
    download_url: str = None
    content_type: str = None
    uploaded: str = None
    big_url: str = None
    thumbnail_url: str = None
    original_values: str = None
    name: str = None
    story_type: str = None
    primary_resources: str = None
    url: str = None
    secondary_resources: str = None
    project: str = None
    performed_by: str = None
    initials: str = None
    occurred_at: str = None