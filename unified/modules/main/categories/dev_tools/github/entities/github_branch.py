from dataclasses import dataclass


@dataclass
class GithubBranch():
    repo_name: str = None
    branch_name: str = None
    description: str = None
    master_branch: str = None
    default_branch: str = None