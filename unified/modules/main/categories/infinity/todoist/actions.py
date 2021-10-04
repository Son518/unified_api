import json
from requests.models import Response
from infinity.todoist.entities.todoist_create_project import TodoistProject
from core.actions import Actions
from infinity.todoist.entities.todoist_create_task import TodoistTask
from infinity.todoist.entities.todoist_add_comment_to_project import TodoistCommentProject
from infinity.todoist.entities.todoist_add_comment_to_task import TodoistCommentTask
from infinity.todoist.entities.todoist_update_task import TodoistUpdateTask
from infinity.todoist.entities.todoist_mark_task_as_complete import TodoistTaskComplete
from infinity.todoist import util

class TodoistActions(Actions):

    def create_project(self, context, project_payload):
        """ 
        Creates project
        context holds the headers 
        project_entity holds the request.body
        """
        project_entity = TodoistProject(**project_payload)
        data ={
            "name": project_entity.name
        }     
        response = util.rest("POST","projects",data,context["headers"]["api_key"])
        return response.text
    
    def create_task(self, context, task_payload):
        """ 
        Creates task
        context holds the headers 
        task_entity holds the request.body
        """
        task_entity = TodoistTask(**task_payload)
        data ={

            "content": task_entity.title,
            "description": task_entity.note
        }
        if task_entity.project_id:
            data["project_id"] = int(task_entity.project_id)
        if task_entity.project_id:
            data["section_id"] = int(task_entity.section_id)
        if task_entity.assigned_to:
            data["assignee"] = int(task_entity.assigned_to)
        
        # for task priority we taking in descending as per api documentation
        if task_entity.priority:
            if (task_entity.priority) == 1:
                data["priority"] =  4
            elif task_entity.priority == 2:
                data["priority"] =  3
            elif task_entity.priority == 3:
                data["priority"] =  2
            elif task_entity.priority == 4:
                data["priority"] =  1
            else:
                return {"error":"please enter the value between 1-4"}
                
        if task_entity.label_id:
            data["label_ids"] = [int(task_entity.label_id)]
        if task_entity.due_date:
            data["due_date"] = (task_entity.due_date)
        response = util.rest("POST","task",data,context["headers"]["api_key"])
        return response.text

    def add_comment_to_project(self, context, project_payload):
        """ 
        Comment to project
        context holds the headers 
        project_entity holds the request.body
        """
        project_entity = TodoistCommentProject(**project_payload)
        data ={
            "project_id": int(project_entity.project_id),
            "content": project_entity.comment
        }     
        response = util.rest("POST","comments",data,context["headers"]["api_key"])
        return response.text
    
    def add_comment_to_task(self, context, task_payload):
        """ 
        Comment to task
        context holds the headers 
        task_entity holds the request.body
        """
        task_entity = TodoistCommentTask(**task_payload)
        data ={
            "task_id": int(task_entity.task_id),
            "content": task_entity.comment
        }     
        response = util.rest("POST","comments",data,context["headers"]["api_key"])
        return response.text

    def update_task(self, context, task_payload):
        """ 
        Update task
        context holds the headers 
        task_entity holds the request.body
        """
        task_entity = TodoistUpdateTask(**task_payload)
        data ={
            "content": task_entity.title
            }
        response = util.rest("POST","tasks",data,context["headers"]["api_key"], task_entity.task_id)
        if response.status_code == 204:
            return {"status":"completed"}
        return response.text

    def mark_task_as_complete(self, context, task_payload):
        """ 
        mark task as complete
        context holds the headers 
        task_entity holds the request.body
        """
        task_entity = TodoistTaskComplete(**task_payload)
       
        response = util.rest("POST","close",{},context["headers"]["api_key"],int(task_entity.task_id))
        if response.status_code == 204:
            return {"status":"completed"}
        return response.text
    