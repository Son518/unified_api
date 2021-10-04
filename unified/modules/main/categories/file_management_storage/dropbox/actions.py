from unified.core.actions import Actions
from file_management_storage.dropbox import util
from file_management_storage.dropbox.entities.dropbox_file import DropboxFile
from file_management_storage.dropbox.entities.dropbox_folder import DropboxFolder
from file_management_storage.dropbox.entities.dropbox_shared_link import DropboxSharedLink

import requests
import json

class DropboxActions(Actions):

    def create_folder(self, context, payload):
        '''Create a new, empty folder.'''
        access_token = util.get_access_token(context['headers'])
        folder = DropboxFolder(**payload)
        url = "files/create_folder_v2"
        request_body = {
            "autorename": folder.auto_rename,
            "path": f"/{folder.name}"
        }
        response = util.rest("post", url, access_token, request_body)

        return response.text, response.status_code

    def move_file(self, context, payload):
        '''Move a file from one folder to another.'''

        access_token = util.get_access_token(context['headers'])
        file = DropboxFile(**payload)
        url = "files/move_v2"
        request_body = {
            "from_path": file.file,
            "to_path": file.to_location,
            "allow_shared_folder": False,
            "autorename": False,
            "allow_ownership_transfer": False
        }
        response = util.rest("post", url, access_token, request_body)

        return response.text, response.status_code

    def rename_file(self, context, payload):
        '''Rename file Existing file'''
        payload['to_location'] = payload['name']
        payload.pop('name', 'no file found')
        return self.move_file(context, payload)

    def create_shared_link(self, context, payload):
        '''create shared link for file '''

        access_token = util.get_access_token(context['headers'])
        url = 'sharing/create_shared_link_with_settings'
        shared_link = DropboxSharedLink(**payload)
        request_body = {
            "path": shared_link.path,
            "settings": {
                "audience": shared_link.audience,
                "access": shared_link.access,
                "requested_visibility": shared_link.requested_visibility,
                "allow_download": shared_link.allow_download
            }
        }

        response = util.rest("post", url, access_token, request_body)

        return response.text, response.status_code
    
    def create_text_file(self,context,payload):
        '''creates text file '''
        
        access_token = util.get_access_token(context['headers'])
        file = DropboxFile(**payload)
        api_args = json.dumps({"path": f"{file.path}/{file.name}.txt", "mode": "add", "autorename": True, "mute": False, "strict_conflict": False})
        headers = {
            "Authorization":f"Bearer {access_token}",
            "Dropbox-API-Arg":api_args,
            "Content-Type":"application/octet-stream"
        }
        request_body = file.content
        response = requests.post("https://content.dropboxapi.com/2/files/upload", headers=headers, data = request_body)
        return response.text, response.status_code

    def upload_file(self,context, payload):
        '''upload a file'''

        access_token = util.get_access_token(context['headers'])
        file = DropboxFile(**payload)
        if not file.file_extension:
            file.file_extension = file.file_url.split('.')[-1]
        api_args = json.dumps({"path": f"{file.path}/{file.name}.{file.file_extension}", "mode": "add", "autorename": True, "mute": False, "strict_conflict": False})
        headers = {
            "Authorization":f"Bearer {access_token}",
            "Dropbox-API-Arg":api_args,
            "Content-Type":"application/octet-stream"
        }
        file_content = requests.get(file.file_url).content
        request_body = file_content
        response = requests.post("https://content.dropboxapi.com/2/files/upload", headers=headers, data = request_body)
        
        return response.text, response.status_code
