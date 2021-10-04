from unified.core.triggers import Triggers
import json
from dev_tools.github.entities.github_comments import GithubComments
from dev_tools.github.entities.github_gist import GithubGist
from dev_tools.github.entities.github_issue import GithubIssue
from dev_tools.github.entities.github_pullrequest import GithubPullRequest
from dev_tools.github.entities.github_branch import GithubBranch
from dev_tools.github.entities.github_review import GithubReview
from dev_tools.github.entities.github_repository import GithubRepository
from dev_tools.github.entities.github_milestone import GithubMilestone
from dev_tools.github.entities.github_label import Githublabel
from dev_tools.github.entities.github_release import GithubRelease


class GithubTriggers(Triggers):

    def new_branch(self, contact, payload):
        """New branch"""

        data = GithubBranch(
            branch_name=payload["ref"],
            repo_name=payload["repository"]["full_name"],
            description=payload["description"],
            master_branch=payload["master_branch"],
            default_branch=payload["repository"]["default_branch"]
        )
        return data.__dict__

    def new_review_request(self, contact, payload):
        """New review request"""

        data = GithubReview(
            repo_name= payload["repository"]["full_name"],
            pull_request_id= payload["pull_request"]["number"],
            comment= payload["pull_request"]["body"],
            action= payload["action"],
            branch_name= payload["pull_request"]["head"]["ref"]
        )
        return data.__dict__

    def new_issue(self, contact, payload):
        """New issue"""

        label = []
        if len(payload["issue"]["labels"]) > 0:
            for label_obj in payload["issue"]["labels"]:
                label.append(label_obj["name"])

        data = GithubIssue(
            repo_name=payload["repository"]["full_name"],
            title=payload["issue"]["title"],
            body=payload["issue"]["body"],
            assignee=payload["issue"]["assignee"]["login"],
            milestone_id=payload["issue"]["milestone"],
            labels=label,
            issue_id=payload["issue"]["number"]
        )
        return data.__dict__

    def new_label(self, contact, payload):
        """New label"""

        data = Githublabel(
            repo_name=payload["repository"]["full_name"],
            label_name=payload["label"]["name"],
            id=payload["label"]["id"],
            description=payload["label"]["description"],
            color=payload["label"]["color"]
        )
        return data.__dict__

    def new_milestone(self, contact, payload):
        """New milestone"""

        data = GithubMilestone(
            id=payload["milestone"]["id"],
            milestone_number=payload["milestone"]["number"],
            title=payload["milestone"]["title"],
            description=payload["milestone"]["description"],
            repo_name=payload["repository"]["full_name"]
        )
        return data.__dict__

    def new_pull_request(self, contact, payload):
        """New Pull request"""

        data = GithubPullRequest(
            repo_name=payload["repository"]["full_name"],
            title=payload["pull_request"]["title"],
            body=payload["pull_request"]["body"],
            head=payload["pull_request"]["head"]["ref"],
            base=payload["pull_request"]["base"]["ref"],
            instant_merge=payload["pull_request"]["auto_merge"],
            pull_request_id=payload["pull_request"]["number"],
            state=payload["pull_request"]["state"]
        )
        return data.__dict__

    def new_release(self, contact, payload):
        """New Release"""

        data = GithubRelease(
            repo_name=payload["repository"]["full_name"],
            id=payload["release"]["id"],
            author=payload["release"]["author"]["login"],
            tag_name=payload["release"]["tag_name"],
            name=payload["release"]["name"],
            body=payload["release"]["body"]
        )
        return data.__dict__

    def new_repository(self, contact, payload):
        """New Repository"""

        data = GithubRepository(
            repo_name=payload["repository"]["full_name"],
            id=payload["repository"]["id"],
            description=payload["repository"]["description"],
            default_branch=payload["repository"]["default_branch"],
            owner_name=payload["repository"]["owner"]["login"],
            created_at=payload["repository"]["created_at"]
        )
        return data.__dict__

    def new_commit_comment(self, contact, payload):
        """New commit comment"""

        data = GithubComments(
            repo_name= payload["repository"]["full_name"],
            body= payload["comment"]["body"],
            issue_or_pull_request_id= payload["issue"]["number"]
        )
        return data.__dict__