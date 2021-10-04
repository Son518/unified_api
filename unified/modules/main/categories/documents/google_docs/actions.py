import json
from unified.core.actions import Actions
from documents.google_docs import util
from documents.google_docs.entities.google_docs_document import GoogledocsDocument


class GoogledocsAction(Actions):

    def create_document_from_text(self, context, payload):
        '''Create a  file with text.'''

        access_token = util.get_access_token(context["headers"])
        url = "https://docs.googleapis.com/v1/documents"
        file = GoogledocsDocument(**payload)
        create_file = {
            "title": file.name
        }
        response = util.rest("post", url, access_token, create_file)

        if response.ok:
            file_id = json.loads(response.text)['documentId']
            # updating content in docs
            update_content_response = self.create_content_in_file(file_id, file.content, access_token)

            if update_content_response.ok:
                # move file to given folder id
                if file.folder_id:
                    move_file = self.move_file(access_token, file_id, file.folder_id)
                update_content_obj = json.loads(update_content_response.text)
                update_content_obj['id'] = file_id

                return json.loads(update_content_obj), update_content_response.status_code

        return json.loads(response.text), response.status_code

    def create_content_in_file(self, file_id, file_content, access_token):
        '''create a file content'''

        url = f"https://docs.googleapis.com/v1/documents/{file_id}:batchUpdate"
        request_body = {
            "requests": [{"insertText": {
                "text": file_content,
                "endOfSegmentLocation": {"segmentId": ""}}}]}
        return util.rest("POST", url, access_token, request_body)

    def move_file(self, access_token, file_id, folder_id):
        '''Move a file from one folder to another.'''

        url = f"https://www.googleapis.com/drive/v2/files/{file_id}/parents"
        request_body = {
            "id": folder_id
        }
        response = util.rest("POST", url, access_token, request_body)

        return response

    def create_document_from_template(self, context, payload):
        '''Creates a new doc based on an existing one'''

        access_token = util.get_access_token(context["headers"])
        file = GoogledocsDocument(**payload)
        url = f"https://www.googleapis.com/drive/v2/files/{file.template_id}/copy"
        file_body = {
            "title": file.name
        }

        response = util.rest("POST", url, access_token, file_body)

        if response.ok:
            templete = json.loads(response.text)
            file_id = templete.get('id')
            # Moving file to given folder
            if file.folder_id:
                move_file_response = self.move_file(access_token, file_id, file.folder_id)
                if not move_file_response.ok:
                    return json.loads(move_file_response.text), move_file_response.status_code 

            return json.loads(response.text), response.status_code

    def append_text_to_document(self, context, payload):
        '''Appends text to an existing document.'''

        file = GoogledocsDocument(**payload)
        access_token = util.get_access_token(context["headers"])
        data = self.create_content_in_file(file.document_id, file.text_to_append, access_token)
        return json.loads(data.text), data.status_code
