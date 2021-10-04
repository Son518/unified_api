from dataclasses import dataclass


@dataclass
class Githublabel():
    repo_name: str = None
    label_name: str = None
    id: str = None
    description: str = None
    color: str = None
