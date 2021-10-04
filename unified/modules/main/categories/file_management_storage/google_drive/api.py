from unified.core.util import google_profile
from file_management_storage.google_drive import util
from file_management_storage.google_drive.entities.google_drive_file import GoogledriveFile
from file_management_storage.google_drive.entities.google_drive_folder import GoogledriveFolder
import json
class GoogledriveApi:

    def find_a_file(self,context,params):
        '''find file by name'''

        access_token = util.get_access_token(context["headers"])
        url = f"https://www.googleapis.com/drive/v2/files?q=title='{params['file_name']}'"
        response = util.rest("GET", url, access_token)
        files_list = json.loads(response.text)['items']
        files = []
        for file in files_list:
            file_obj = GoogledriveFile(
                file_id=file['id'],
                file_name=file.get('title'),
                media_mime_type =  file.get('mimeType'),
                permission= file['userPermission'].get('id'),
                file_size = file.get('fileSize')
            )
            files.append(file_obj.__dict__)
        return json.dumps(files)

    def find_a_folder(self,context,params):
        '''find a folder by name'''
        
        access_token = util.get_access_token(context["headers"])
        url = f"https://www.googleapis.com/drive/v2/files?q=mimeType='application/vnd.google-apps.folder'andtitle='{params['folder_name']}'"
        response = util.rest("GET", url, access_token)
        folder_list = json.loads(response.text)['items']
        folders = []
        for folder in folder_list:
            folder_obj = GoogledriveFolder(
                folder_id=folder['id'],
                folder_name=folder['title'],
                permission=folder['userPermission'].get('id'),
                media_mime_type=folder['mimeType']
            )
            folders.append(folder_obj.__dict__)
        
        return json.dumps(folders)
    
    def profile(self, context, params):
        '''Details of authenticated user'''

        return google_profile(context, params)