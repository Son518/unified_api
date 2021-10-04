import json
from dev_tools.github import util
from dev_tools.github.entities.github_comments import GithubComments
from dev_tools.github.entities.github_gist import GithubGist
from dev_tools.github.entities.github_issue import GithubIssue
from dev_tools.github.entities.github_pullrequest import GithubPullRequest
from dev_tools.github.entities.github_branch import GithubBranch
from dev_tools.github.entities.github_review import GithubReview
from dev_tools.github.entities.github_organization import GithubOrganization
from dev_tools.github.entities.github_repository import GithubRepository
from dev_tools.github.entities.github_user import GithubUser


class GithubAPI():

    def issue_by_number(self, context, params):
        """Get issue by number"""

        access_token = context["headers"]["token"]
        response = util.rest(
            "GET", f"repos/{params.get('repo_name')}/issues/{params.get('search_value')}", access_token)
        response = json.loads(response.text)
        label = []
        if len(response["labels"]) > 0:
            for label_obj in response["labels"]:
                label.append(label_obj["name"])

        data = GithubIssue(
            repo_name=params.get('repo_name'),
            title=response["title"],
            body=response["body"],
            assignee=response["assignee"]["login"],
            milestone_id=response["milestone"]["number"],
            labels=label,
            issue_id=params.get('search_value')
        )
        return data.__dict__

    def organization_by_name(self, context, params):
        """Get Organization by name"""

        access_token = context["headers"]["token"]
        response = util.rest("GET", f"orgs/{params.get('name')}", access_token)
        response = json.loads(response.text)
        data = GithubOrganization(
            name=response["login"],
            id=response["id"],
            type=response["type"],
            created_at=response["created_at"],
            description=response["description"],
            email=response["billing_email"],
            is_verified=response["is_verified"]
        )
        return data.__dict__

    def organization_membership(self, context, params):
        """Check organization membership"""

        access_token = context["headers"]["token"]
        response = util.rest(
            "GET", f"orgs/{params.get('organization_name')}/members/{params.get('user_name')}", access_token)
        if response.status_code == 204:
            return {"message": f"{params.get('user_name')} organization member"}
        return {"message": f"{params.get('user_name')} not an organization member"}

    def pull_request_by_number(self, context, params):
        """Get Pull request by number"""

        access_token = context["headers"]["token"]
        response = util.rest(
            "GET", f"repos/{params.get('repo_name')}/pulls/{params.get('search_value')}", access_token)
        response = json.loads(response.text)
        data = GithubPullRequest(
            repo_name=params.get('repo_name'),
            title=response["title"],
            body=response["body"],
            head=response["head"]["ref"],
            base=response["base"]["ref"],
            instant_merge=response["auto_merge"],
            pull_request_id=params.get('search_value'),
            state=response["state"]
        )
        return data.__dict__

    def repository_by_name(self, context, params):
        """Get repository by name"""

        access_token = context["headers"]["token"]
        response = util.rest(
            "GET", f"repos/{params.get('name')}", access_token)
        response = json.loads(response.text)
        data = GithubRepository(
            description=response["description"],
            id=response["id"],
            repo_name=response["name"],
            created_at=response["created_at"],
            default_branch=response["default_branch"],
            owner_name=response["owner"]["login"]
        )
        return data.__dict__

    def user_by_name(self, context, params):
        """Get user by name"""

        access_token = context["headers"]["token"]
        response = util.rest(
            "GET", f"users/{params.get('name')}", access_token)
        response = json.loads(response.text)
        data = GithubUser(
            id=response["id"],
            name=params.get('name'),
            type=response["type"],
            created_at=response["created_at"],
            email=response["email"],
            followers=response["followers"]
        )
        return data.__dict__

    def profile(self, context, params):
        """Get issue by number"""

        access_token = context["headers"]["token"]
        response = util.rest("GET", f"user", access_token)
        response = json.loads(response.text)
        data = {
            "id": response["id"],
            "email": response["email"],
            "name": response["login"]
        }
        return data
