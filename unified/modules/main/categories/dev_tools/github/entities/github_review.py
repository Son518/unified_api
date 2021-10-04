from dataclasses import dataclass


@dataclass
class GithubReview():
    repo_name: str = None
    pull_request_id: str = None
    comment: str = None
    action: str = None
    branch_name: str = None
