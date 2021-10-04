from dataclasses import dataclass


@dataclass
class GithubIssue():
    repo_name: str = None
    title: str = None
    body: str = None
    assignee: str = None
    milestone_id: str = None
    labels: str = None
    issue_id: str = None