from unified.core.actions import Actions
from file_management_storage.google_drive import util
from googleapiclient.discovery import build
from apiclient.http import MediaFileUpload
import requests
import json

from file_management_storage.google_drive.entities.google_drive_folder import GoogledriveFolder
from file_management_storage.google_drive.entities.google_drive_file import GoogledriveFile


class GoogledriveAction(Actions):
    def create_folder(self, context, payload):
        '''Create a new, empty folder'''

        drive_client = util.drive_client_instance(context["headers"])
        folder = GoogledriveFolder(**payload)
        file_metadata = {
            'name': folder.folder_name,
            'mimeType': 'application/vnd.google-apps.folder'
        }

        if folder.parent_folder_id:
            file_metadata["parents"] = [folder.parent_folder_id]
        file = drive_client.files().create(body=file_metadata).execute()

        return file

    def copy_file(self, context, payload):
        '''Create a copy of the specified file.'''

        drive_client = util.drive_client_instance(context["headers"])
        file = GoogledriveFile(**payload)
        file_metadata = {}

        if file.file_name:
            file_metadata['name'] = file.file_name

        if file.folder_id:
            file_metadata['parents'] = [file.folder_id]
        file = drive_client.files().copy(fileId=file.file_id, body=file_metadata).execute()

        return file

    def move_file(self, context, payload):
        '''Move a file from one folder to another.'''

        access_token = util.get_access_token(context["headers"])
        file = GoogledriveFile(**payload)
        url = f"https://www.googleapis.com/drive/v2/files/{file.file_id}/parents"
        request_body = {
            "id": f"{file.folder_id}"
        }
        response = util.rest("POST", url, access_token, request_body)

        return response.text, response.status_code

    def upload_file(self, context, payload):
        '''uploads file to google drive '''

        access_token = util.get_access_token(context["headers"])
        file = GoogledriveFile(**payload)
        metadata = {
            "name": file.file_name
        }

        if file.folder_id:
            metadata["parents"]: [file.folder_id]
        
        files = {
            'data': ('metadata', json.dumps(metadata), 'application/json'),
            'file': (requests.get(file.file_url).content)
        }
        response = requests.post(
            "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
            headers={"Authorization": "Bearer " + access_token},
            files=files
        )

        return response.text, response.status_code

    def create_file_from_text(self, context, payload):
        '''Create a  file with text.'''

        access_token = util.get_access_token(context["headers"])
        url = "https://docs.googleapis.com/v1/documents"
        file = GoogledriveFile(**payload)
        create_file = {
            "title": file.file_name
        }
        response = util.rest("post", url, access_token, create_file)

        if response.ok:
            file_id = json.loads(response.text)['documentId']
            response = self.create_content_in_file(
                file_id, file.file_content, access_token)
            if response.ok:
                response_obj = json.loads(response.text)
                response_obj['id'] = file_id
                return response_obj, response.status_code

        return response.text, response.status_code

    def create_content_in_file(self, file_id, file_content, access_token):
        '''create a file content'''

        url = f"https://docs.googleapis.com/v1/documents/{file_id}:batchUpdate"
        request_body = {
            "requests": [{"insertText": {
                "text": file_content,
                "endOfSegmentLocation": {"segmentId": ""}}}]}
        return util.rest("POST", url, access_token, request_body)
