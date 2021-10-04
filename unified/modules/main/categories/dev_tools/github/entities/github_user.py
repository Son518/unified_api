from dataclasses import dataclass


@dataclass
class GithubUser():
    name: str = None
    id: str = None
    created_at: str = None
    type: str = None
    email: str = None
    followers: str = None