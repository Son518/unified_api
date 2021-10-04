from dataclasses import dataclass


@dataclass
class GithubRepository():
    repo_name: str = None
    id: str = None
    created_at: str = None
    description: str = None
    default_branch: str = None
    owner_name: str = None