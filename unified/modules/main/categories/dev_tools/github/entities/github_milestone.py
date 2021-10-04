from dataclasses import dataclass


@dataclass
class GithubMilestone():
    id: str = None
    milestone_number: str = None
    title: str = None
    description: str = None
    repo_name: str = None