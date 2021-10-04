from unified.core.actions import Actions
from dev_tools.github import util
import json
from dev_tools.github.entities.github_comments import GithubComments
from dev_tools.github.entities.github_gist import GithubGist
from dev_tools.github.entities.github_issue import GithubIssue
from dev_tools.github.entities.github_pullrequest import GithubPullRequest
from dev_tools.github.entities.github_branch import GithubBranch
from dev_tools.github.entities.github_review import GithubReview


class GithubActions(Actions):

    def create_comment(self, context, payload):
        """Create a comment on pull request"""

        access_token = context["headers"]["token"]
        payload_data = GithubComments(**payload)
        data = {
            "body": payload_data.body
        }
        response = util.rest(
            "POST", f"repos/{payload_data.repo_name}/issues/{payload_data.issue_or_pull_request_id}/comments", access_token, data)
        return json.loads(response.text)

    def create_gist(self, context, payload):
        """Create Gist"""

        access_token = context["headers"]["token"]
        payload_data = GithubGist(**payload)
        data = {
            "files": {
                payload_data.gist_filename: {
                    "content": payload_data.content_of_the_gist
                }
            }
        }

        if payload_data.description is not None:
            data["description"] = payload_data.description

        if payload_data.make_gist_public is not None:
            data["public"] = payload_data.make_gist_public
        response = util.rest("POST", f"gists", access_token, data)
        return json.loads(response.text)

    def create_issue(self, context, payload):
        """Create issue"""

        access_token = context["headers"]["token"]
        payload_data = GithubIssue(**payload)
        data = {
            "title": payload_data.title
        }

        if payload_data.body is not None:
            data["body"] = payload_data.body

        if payload_data.assignee is not None:
            data["assignee"] = payload_data.assignee

        if payload_data.milestone_id is not None:
            data["milestone"] = payload_data.milestone_id

        if payload_data.labels is not None:
            data["labels"] = payload_data.labels.split(',')

        response = util.rest("POST", f"repos/{payload_data.repo_name}/issues", access_token, data)
        return json.loads(response.text)

    def create_pull_request(self, context, payload):
        """Create Pull Request"""

        access_token = context["headers"]["token"]
        payload_data = GithubPullRequest(**payload)
        data = {
            "head": payload_data.head,
            "base": payload_data.base
        }

        if payload_data.title is not None:
            data["title"] = payload_data.title

        if payload_data.instant_merge is not None:
            data["merge"] = payload_data.instant_merge

        if payload_data.body is not None:
            data["body"] = payload_data.body
        
        response = util.rest("POST", f"repos/{payload_data.repo_name}/pulls", access_token, data)
        return json.loads(response.text)

    def delete_branch(self, context, payload):
        """Delete Branch"""

        access_token = context["headers"]["token"]
        payload_data = GithubBranch(**payload)       
        response = util.rest("DELETE", f"repos/{payload_data.repo_name}/git/refs/heads/{payload_data.branch_name}", access_token)

        if response.status_code == 204:
            return {"message": "Deleted successfully"}
        return json.loads(response.text)

    def submit_review(self, context, payload):
        """Submit review"""

        access_token = context["headers"]["token"]
        payload_data = GithubReview(**payload)
        data = {
            "body":payload_data.comment,
            "event":payload_data.action.upper()
        }     
        response = util.rest("POST", f"repos/{payload_data.repo_name}/pulls/{payload_data.pull_request_id}/reviews", access_token, data)
        return json.loads(response.text)

    def update_issue(self, context, payload):
        """Submit review"""

        access_token = context["headers"]["token"]
        payload_data = GithubIssue(**payload)
        data = {
            "title": payload_data.title
        }

        if payload_data.body is not None:
            data["body"] = payload_data.body

        if payload_data.assignee is not None:
            data["assignee"] = payload_data.assignee

        if payload_data.milestone_id is not None:
            data["milestone"] = payload_data.milestone_id

        if payload_data.labels is not None:
            data["labels"] = payload_data.labels.split(',')    
        response = util.rest("PATCH", f"repos/{payload_data.repo_name}/issues/{payload_data.issue_id}", access_token, data)
        return json.loads(response.text)

    def update_pull_request(self, context, payload):
        """Create Pull Request"""

        access_token = context["headers"]["token"]
        payload_data = GithubPullRequest(**payload)
        data = {
            "head": payload_data.head,
            "base": payload_data.base
        }

        if payload_data.title is not None:
            data["title"] = payload_data.title

        if payload_data.instant_merge is not None:
            data["merge"] = payload_data.instant_merge

        if payload_data.body is not None:
            data["body"] = payload_data.body
        
        response = util.rest("PATCH", f"repos/{payload_data.repo_name}/pulls/{payload_data.pull_request_id}", access_token, data)
        return json.loads(response.text)
