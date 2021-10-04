from dataclasses import dataclass
from os import name


@dataclass
class JiraSoftwareCloudIssue:
    issue_id: str = None
    project_id: str = None
    assignee_id: str = None
    priority_id: str = None
    issuetype_id: str = None
    description: str = None
    site_id: str = None
    user_id: str = None
    issue_name: str = None
    issuetype: str = None
    task_id: str = None
    reporter: str = None
    comment: str = None
    issue_title: str = None
    summary: str = None
    assignee: str = None
    desc: str = None
    priority: str = None
    label: str = None
    reporter_id: str = None
    attachment_url: str = None
    labels: str = None
    sprint_id: str = None
    epic_link: str = None
    linked_issues: str = None
