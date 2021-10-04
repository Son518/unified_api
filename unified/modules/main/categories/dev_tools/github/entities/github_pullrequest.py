from dataclasses import dataclass


@dataclass
class GithubPullRequest():
    repo_name: str = None
    title: str = None
    body: str = None
    head: str = None
    base: str = None
    instant_merge: str = None
    pull_request_id: str = None
    state: str = None