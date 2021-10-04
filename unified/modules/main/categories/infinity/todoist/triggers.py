import json
from requests.models import Response
from core.triggers import Triggers
from infinity.todoist.entities.todoist_new_project import TodoistNewProject
from infinity.todoist.entities.todoist_new_complete_task import TodoistNewCompleteTask
from infinity.todoist.entities.todoist_new_incomplete_task import TodoistNewInCompleteTask
class TodoistTriggers(Triggers):

    def new_project(self,context,payload):
        """
        triggers when new_project created 
        context holds the headers 
        payload holds the request.body
        """
        data = TodoistNewProject(
                    event_data=payload["event_data"],
                    child_order=payload["event_data"]["child_order"],
                    collapsed=payload["event_data"]["collapsed"],
                    color=payload["event_data"]["color"],
                    id=payload["event_data"]["id"],
                    is_archived=payload["event_data"]["is_archived"],
                    is_deleted=payload["event_data"]["is_deleted"],
                    is_favorite=payload["event_data"]["is_favorite"],
                    parent_id=payload["event_data"]["parent_id"],
                    shared=payload["event_data"]["shared"],
                    sync_id=payload["event_data"]["sync_id"],
                    event_name=payload["event_name"],
                    initiator=payload["initiator"],
                    email=payload["initiator"]["email"],
                    full_name=payload["initiator"]["full_name"],
                    image_id=payload["initiator"]["image_id"],
                    user_id=payload["user_id"],
                    version=payload["version"]
                )
        return data.__dict__
    
    def new_completed_task(self,context,payload):
        """
        triggers when new completed task created 
        context holds the headers 
        payload holds the request.body
        """
        data = TodoistNewCompleteTask(
                    event_data=payload["event_data"],
                    child_order=payload["event_data"]["child_order"],
                    collapsed=payload["event_data"]["collapsed"],
                    id=payload["event_data"]["id"],
                    is_deleted=payload["event_data"]["is_deleted"],
                    parent_id=payload["event_data"]["parent_id"],
                    sync_id=payload["event_data"]["sync_id"],
                    url=payload["event_data"]["url"],
                    in_history=payload["event_data"]["in_history"],
                    priority=payload["event_data"]["priority"],
                    event_name=payload["event_name"],
                    initiator=payload["initiator"],
                    email=payload["initiator"]["email"],
                    full_name=payload["initiator"]["full_name"],
                    image_id=payload["initiator"]["image_id"],
                    user_id=payload["user_id"],
                    version=payload["version"]
                )
        return data.__dict__
            
    def new_incomplete_task(self,context,payload):
        """
        triggers when new incomplete task created 
        context holds the headers 
        payload holds the request.body
        """
        data = TodoistNewInCompleteTask(
                    event_data=payload["event_data"],
                    child_order=payload["event_data"]["child_order"],
                    collapsed=payload["event_data"]["collapsed"],
                    id=payload["event_data"]["id"],
                    is_deleted=payload["event_data"]["is_deleted"],
                    parent_id=payload["event_data"]["parent_id"],
                    sync_id=payload["event_data"]["sync_id"],
                    url=payload["event_data"]["url"],
                    in_history=payload["event_data"]["in_history"],
                    priority=payload["event_data"]["priority"],
                    event_name=payload["event_name"],
                    initiator=payload["initiator"],
                    email=payload["initiator"]["email"],
                    full_name=payload["initiator"]["full_name"],
                    image_id=payload["initiator"]["image_id"],
                    user_id=payload["user_id"],
                    version=payload["version"]
                )
        return data.__dict__
            