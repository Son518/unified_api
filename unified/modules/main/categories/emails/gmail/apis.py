from emails.gmail import util
from emails.gmail.entities.gmail_entity import Gmail
import json
import base64

class GmailApi:

    @staticmethod
    def get_email_body(email_obj):
        """ utility function for parsing email body (text) from payload """

        payload = email_obj['payload']
        body = ""

        if payload['body']['size'] > 0:
            data = payload['body']['data']
            body = base64.urlsafe_b64decode(data.encode('ASCII'))
        else:
            parts = payload['parts']
            for part in parts:
                if part['mimeType'] in ["text/plain", "text/html"]:
                    if part['body']['size'] > 0:
                        data = part['body']['data']
                        body = base64.urlsafe_b64decode(data.encode('ASCII'))
                        break

        if body == "":
            body = email_obj['snippet']
        else:
            body = body.decode()

        return body

    @staticmethod
    def get_email_body_type(email_obj):
        """ utility function for parsing email body-type from payload """

        payload = email_obj['payload']

        if payload['body']['size'] > 0:
            headers = GmailApi.get_values_from(payload['headers'])
        else:
            parts = payload['parts']
            for part in parts:
                if part['mimeType'] in ["text/plain", "text/html"]:
                    headers = GmailApi.get_values_from(part['headers'])
                    break

        return headers.get('content-type')

    @staticmethod
    def get_email_data(email_obj):
        """ utility function for parsing email obj from payload and return as dict """

        email_headers = GmailApi.get_values_from(email_obj['payload']['headers'])
        email_from_str = email_headers.get('from')
        email_from = GmailApi.parse_from(email_from_str)
        email = Gmail(
            email_id = email_obj.get('id'),
            thread_id = email_obj.get('threadId'),
            to = email_headers.get('to'),
            subject = email_headers.get('subject'),
            body = GmailApi.get_email_body(email_obj),
            body_type = GmailApi.get_email_body_type(email_obj),
            cc = email_headers.get('cc'),
            bcc = email_headers.get('bcc'),
            from_email = email_from[1],
            from_name = email_from[0],
            signature = email_headers.get('sender'),
            label = email_obj['labelIds']
        )

        return email.__dict__

    def email(self, context, params):
        """ Get an email data """

        if params['id'] == "":
            return {
                "error": "Empty email id provided"
            }

        access_token = util.get_access_token(context['headers'])
        url = util.get_url(context) + f"messages/{params['id']}"
        response = util.rest("GET", url, access_token)
        res = json.loads(response.text)

        if response.status_code > 400:
            return res

        return GmailApi.get_email_data(res)

    def draft(self, context, params):
        """ Get an draft message data """

        access_token = util.get_access_token(context['headers'])
        url = util.get_url(context) + f"drafts/{params['id']}"
        response = util.rest("GET", url, access_token)

        if response.status_code > 400:
            raise Exception("Error ", response.text)

        data = json.loads(response.text)

        return GmailApi.get_email_data(data['message'])

    @staticmethod
    def get_values_from(headers):
        """ Utility function for parsing headers """

        values = {}
        for header in headers:
            values[header['name'].lower()] = header['value']

        return values

    @staticmethod
    def parse_from(from_str: str):
        """ Utility function for parsing 'From' header """

        if from_str is None:
            return ['', '']

        if from_str.find('<') > 0:
            strs = from_str.split(' ')
            strs[1] = strs[1].lstrip('<').rstrip('>')
        else:
            strs = ['', from_str]

        return strs

    @staticmethod
    def attachment(context, params):
        """ Get an attachment """

        access_token = util.get_access_token(context['headers'])
        url = util.get_url(context) + f"messages/{params['message_id']}" \
                f"/attachments/{params['attachment_id']}"
        response = util.rest("GET", url, access_token)

        return json.loads(response.text)
