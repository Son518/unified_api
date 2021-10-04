import json
from anydo_api import user
from anydo_api.client import Client
from anydo_api.task import Task
from core.actions import Actions
from task_management.any_do import util
from task_management.any_do.entities.any_do_task import AnydoTask
from flask import jsonify

class AnydoActions(Actions):

    def create_task(self,context,payload):
        """
        creates a new task
        context holds the headers 
        payload holds the request.body
        """
        user = util.anydo_client(context["headers"])
        task_entity = AnydoTask(**payload)
        task = Task.create(
                            user=user,
                            title=task_entity.name,
                            priority=task_entity.priority,
                            category=task_entity.category
                        )
        if task_entity.notes:
            task.add_note(task_entity.notes)
        return {
            'title':task.title,
            'priority':task.priority,
            'id':task.id
        }