from project_management.podio import util
from project_management.podio.entities.podio_app import PodioApp
from project_management.podio.entities.podio_item import PodioItem
from project_management.podio.entities.podio_org import PodioOrg
from project_management.podio.entities.podio_comment import PodioComment
from project_management.podio.entities.podio_task import PodioTask
from project_management.podio.entities.podio_user import PodioUser
import json


class PodioTriggers():

    def new_item(self, context, payload):
        ''' triggers when new item created'''

        item_id = payload["item_id"]
        podio_item = util.podio_oauth(context["headers"])
        item_response = podio_item.Item.find(int(payload["item_id"]))

        item = PodioItem(app_name=item_response["app"]["item_name"],
                      application_id=item_response["app"]["app_id"],
                      item_id=item_response["item_id"],
                      workspace_id=item_response["app"]["space_id"],
                      organization_id=item_response["app"]["item_accounting_info"]["org_id"],
                      link=item_response["link"],
                      url=item_response["app"]["url"],
                      tag=item_response["tags"],
                      description=item_response["fields"][0]["config"]["description"],
                      title=item_response["fields"][0]["label"],
                      priority=item_response["priority"])
        
        return item.__dict__

    def new_application(self, context, payload):
        ''' triggers when new application created'''
        
        app_id = payload["app_id"]
        podio_app = util.podio_oauth(context["headers"])
        app_response = podio_app.Application.find(int(payload["app_id"]))

        app = PodioApp(
            status=app_response["status"],
            space_id=app_response["space_id"],
            link_add=app_response["url_add"],
            type=app_response["config"]["type"],
            name=app_response["config"]["name"],
            item_name=app_response["config"]["item_name"],
            description=app_response["config"]["description"],
            usage=app_response["config"]["usage"],
            external_id=app_response["config"]["external_id"],
            link=app_response["link"])

        return app.__dict__

    def new_organization(self, context, payload):
        ''' triggers when new origanization created'''

        podio_app = util.podio_oauth(context["headers"])
        org_response = podio_app.Org.get_all()

        organization = PodioOrg(
            name=org_response[0]["name"],
            org_id=org_response[0]["org_id"],
            url=org_response[0]["url"],
            url_label=org_response[0]["url_label"],
            status=org_response[0]["status"],
            logo=org_response[0]["logo"],
            segment=org_response[0]["segment"],
            tier=org_response[0]["tier"],
            sales_agent_id=org_response[0]["sales_agent_id"],
            domains=org_response[0]["domains"],
            role=org_response[0]["role"],
            type=org_response[0]["type"]
        )

        return organization.__dict__
    
    def new_comment(self, context, payload):
        ''' triggers when new comment created'''

        access_token = util.get_access_token(context["headers"])
        url = f"https://api.podio.com/comment/{payload['comment_id']}"
        comment = json.loads(util.rest("GET", url, {}, access_token).text)

        comment_obj = PodioComment(id = comment["comment_id"],
                                task_id=comment["ref"]["id"],
                                comment_text=comment["value"],
                                file_url=comment["user"]["image"]["link"],
                                weblink_url=comment["user"]["image"]["thumbnail_link"])   

        return comment_obj.__dict__
    
    def new_task(self, context, payload):
        ''' triggers when new task created'''

        access_token = util.get_access_token(context["headers"])
        url = f"https://api.podio.com/task/{payload['task_id']}"
        task = json.loads(util.rest("GET", url, {}, access_token).text)

        task_obj = PodioTask(task_id=task["task_id"],
                            organization_id=task["ref"]["data"]["org_id"],
                            responsible_user=task["responsible"]["name"],
                            workspace_id=task["space_id"],
                            labels=task["labels"],
                            task_description=task["description"],
                            due_on=task["due_date"],
                            task_name=task["text"])

        return task_obj.__dict__
    
    def new_user(self, context, payload):
        ''' triggers when new user created'''

        access_token = util.get_access_token(context["headers"])
        url = f"https://api.podio.com/user"
        user = json.loads(util.rest("GET", url, {}, access_token).text)

        user_obj = PodioUser(id=user["user_id"],
                            email=user["mail"],
                            created_on=user["created_on"])

        return user_obj.__dict__

    def updated_item(self, context, payload):
        ''' triggers when item updated'''

        item_id = payload["item_id"]
        podio_item = util.podio_oauth(context["headers"])
        item_response = podio_item.Item.find(int(payload["item_id"]))

        item = PodioItem(app_name=item_response["app"]["item_name"],
                      application_id=item_response["app"]["app_id"],
                      item_id=item_response["item_id"],
                      workspace_id=item_response["app"]["space_id"],
                      organization_id=item_response["app"]["item_accounting_info"]["org_id"],
                      link=item_response["link"],
                      url=item_response["app"]["url"],
                      tag=item_response["tags"],
                      description=item_response["fields"][0]["config"]["description"],
                      title=item_response["fields"][0]["label"],
                      priority=item_response["priority"])
        
        return item.__dict__
