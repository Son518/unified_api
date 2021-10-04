from dataclasses import dataclass


@dataclass
class GithubComments():
    repo_name: str = None
    body: str = None
    issue_or_pull_request_id: str = None