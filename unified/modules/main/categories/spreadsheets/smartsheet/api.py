from spreadsheets.smartsheet.entities.smartsheet_row import SmartsheetRow
from spreadsheets.smartsheet.entities.smartsheet_commet import SmartsheetComment
from spreadsheets.smartsheet.entities.smartsheet_attachment import SmartsmartAttachment
from spreadsheets.smartsheet import util
import json


class SmartsheetApi:
    def row(self, context, payload):
        '''Get details of single row '''

        api_key = context['headers'].get('api_key')

        if not api_key:
            raise Exception('Provide required api-key in headers')

        url = f"sheets/{payload['sheet_id']}/rows/{payload['row_id']}"
        response = util.rest("GET", url, api_key)
        response_obj = json.loads(response.text)
        row = SmartsheetRow(
            sheet_id=response_obj['sheetId'],
            row_id=response_obj['id'],
            cells=response_obj.get('cells'),
            row_number=response_obj.get('rowNumber')
        )
        return row.__dict__

    def attachment(self, context, payload):
        '''Get details of attachment'''

        api_key = context['headers'].get('api_key')

        if not api_key:
            raise Exception('Provide required api-key in headers')

        url = f"sheets/{payload['sheet_id']}/attachments/{payload['attachment_id']}"
        response = util.rest("GET", url, api_key)
        response_obj = json.loads(response.text)

        attachement = SmartsmartAttachment(
            attachment_id=response_obj['id'],
            name=response_obj.get('name'),
            attachment_url=response_obj.get('url'),
            attachment_type=response_obj.get('attachmentType'),
            mime_type=response_obj.get('mimeType')
        )

        return attachement.__dict__

    def comment(self, context, payload):
        '''Get details of comments'''

        api_key = context['headers'].get('api_key')

        if not api_key:
            raise Exception('Provide required api-key in headers')

        url = f"sheets/{payload['sheet_id']}/comments/{payload['comment_id']}"

        response = util.rest("GET", url, api_key)
        response_obj = json.loads(response.text)
        comment = SmartsheetComment(
            comment_id=response_obj['id'],
            discussion_id=response_obj.get('discussionId'),
            comment=response_obj.get('text'),
            created_by=response_obj.get('createdBy').get('email')
        )
        return comment.__dict__
    
    def profile(self, context, payload):
        '''Details of authenticated user'''

        api_key = context['headers'].get('api_key')
        if not api_key:
            raise Exception('Provide required api-key in headers')

        url = "users/me"
        response_data = util.rest("GET", url, api_key)
        if response_data.ok:
            response = response_data.json()
            profile = {
                'id':response['id'],
                'email':response['email'],
                'name':response['firstName']
            }
            return profile
        else:
            return {'response':'invalid details'}
    
    def verify(self, context, payload):
        return self.profile(context, payload)