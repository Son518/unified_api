from dataclasses import dataclass


@dataclass
class DropboxSharedLink:
    path: str = None
    audience: str = "public"
    access: str = "viewer"
    allow_download: bool = False
    requested_visibility: str = "public"
    link_password: str = None
    expires_at: str = None
