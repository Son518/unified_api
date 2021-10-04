# AsanaTriggers.py extends core/triggers/Triggers
import asana
from flask import request, Response
from project_management.asana import util
from project_management.asana.entities.asana_task import AsanaTask
from project_management.asana.api import AsanaApi
from unified.core.triggers import Triggers
import requests


class AsanaTriggers(Triggers):

    def new_task(self, context, payload):
        '''Triggered when you add a new task to a project.'''
        
        # asana handshake
        if resp := util.check_handshake():   # assignment expression
            return resp

        # we get only created task id in webhook response
        task_id = payload['events'][0].get('resource').get('gid')
        params = {
            'task_id': task_id
        }
        response = AsanaApi().task(context, params)

        return response, 200

    def new_project(self, context, payload):
        '''Triggered when you add a new project.'''

        # asana handshake
        if resp := util.check_handshake():   # assignment expression
            return resp

        project_id = payload['events'][0].get('resource').get('gid')
        params = {
            'project_id': project_id
        }
        response = AsanaApi().project(context, params)

        return response

    def new_tag(self, context, payload):
        '''Triggered when you add a new tag'''

        # asana handshake
        if resp := util.check_handshake():   # assignment expression
            return resp

        tag_id = payload['events'][0].get('parent').get('gid')
        params = {
            'tag_id': tag_id
        }
        response = AsanaApi().tag(context, params)

        return response
    
    def new_story(self,context,payload):
        '''Triggered when you add a new story.'''

        return self.new_comment(context, payload)

    def new_comment(self, context, payload):
        '''Triggered when you add a new comment to a project.'''

        # asana handshake
        if resp := util.check_handshake():   # assignment expression
            return resp

        comment_id = payload['events'][0].get('resource').get('gid')
        params = {
            'comment_id': comment_id
        }
        response = AsanaApi().comment(context, params)

        return response

    def tag_added_to_task(self, context, payload):
        '''Triggered when you add a tag to a task.'''
        
        # asana handshake
        if resp := util.check_handshake():   # assignment expression
            return resp

        # we get only created task id in webhook response
        task_id = payload['events'][0].get('resource').get('gid')
        params = {
            'task_id': task_id
        }
        response = AsanaApi().task(context, params)

        return response, 200
