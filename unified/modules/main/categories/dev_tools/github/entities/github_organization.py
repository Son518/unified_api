from dataclasses import dataclass


@dataclass
class GithubOrganization():
    name: str = None
    id: str = None
    type: str = None
    created_at: str = None
    description: str = None
    email: str = None
    is_verified: str = None