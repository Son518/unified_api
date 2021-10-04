from emails.microsoft_office_365_email import util
from emails.entities.email_entities import Email
from emails.microsoft_office_365_email.entities.microsoft_office_attachment import Microsoftoffice365emailattachment

import json


class Microsoftoffice365emailApi:

    def email(self, context, params):
        '''Get an  Email data'''
        access_token = util.get_access_token(context['headers'])
        url = f"https://graph.microsoft.com/v1.0/me/messages/{params['conversation_id']}"
        response = util.rest("GET", url, access_token)

        if response.status_code > 400:
            raise Exception("Error ", response.text)

        email_obj = json.loads(response.text)
        email = Email(
            email_id = email_obj.get('id'),
            to = email_obj.get('toRecipients'),
            subject = email_obj.get('subject'),
            body = email_obj.get('bodyPreview'),
            cc = email_obj.get('ccRecipients'),
            bcc = email_obj.get('bccRecipients')
        )
        return email.__dict__

    def attachments(self, context, params):
        '''Get email attachments'''
        access_token = util.get_access_token(context['headers'])
        url = f"https://graph.microsoft.com/v1.0/me/messages/{params['message_id']}/attachments"
        response = util.rest("GET", url, access_token)
        attachment_list = json.loads(response.text)['value']
        attachments = []
        for attachment in attachment_list:
            att_obj = Microsoftoffice365emailattachment(
                attachment_id = attachment.get('id'),
                attachment_name = attachment.get('name'),
                content_type = attachment.get('contentType'),
                size = attachment.get('size')
            )
            attachments.append(att_obj.__dict__)

        return json.dumps(attachments)

    def profile(self, context, params):
        '''Details of authenticated user'''

        access_token = util.get_access_token(context['headers'])
        url = 'https://graph.microsoft.com/v1.0/me'
        response_data = util.rest("GET", url, access_token)
        response = response_data.json()
        profile = {
            'id':response['id'],
            'email':response['userPrincipalName'],
            'name':response['displayName']
        }
        return profile