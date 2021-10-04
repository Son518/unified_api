from dataclasses import dataclass


@dataclass
class GithubRelease():
    repo_name: str = None
    id: str = None
    author: str = None
    tag_name: str = None
    name: str = None
    body: str = None