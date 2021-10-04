from os import access
from unified.core.actions import Actions
from emails.gmail import util
from emails.gmail.entities.gmail_entity import Gmail

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import base64
import json
from requests import get
from os.path import basename


class GmailActions(Actions):

    @staticmethod
    def labels(context):
        """ List all labels """

        access_token = util.get_access_token(context['headers'])
        url = util.get_url(context) + "labels"
        response = util.rest("GET", url, access_token)

        if response.status_code > 400:
            raise Exception("Error ", response.text)

        return json.loads(response.text)

    def email_helper(self, context, payload):
        """ Utility function for parsing from email headers """

        access_token = util.get_access_token(context['headers'])
        url = util.get_url(context) + f"threads/{payload['thread_id']}/?format=metadata"
        response = util.rest("GET", url, access_token)

        if response.status_code > 400:
            raise Exception("Error ", response.text)

        response_obj = json.loads(response.text)
        message = response_obj['messages'].pop()
        headers = message['payload']['headers']

        from_str = ""
        message_id = ""
        subject = ""

        for header in headers:
            if header['name'].lower() == "from":
                from_str = header['value']
            if header['name'].lower() == "message-id":
                message_id = header['value']
            if header['name'].lower() == "subject":
                subject = header['value']

        res = {
            "from" : from_str.rstrip('>').split('<').pop(),
            "message_id": message_id,
            "subject": subject
            }

        return res

    def get_raw(self, email: Gmail):
        """ Utility function for generating raw body for email """

        msg = MIMEMultipart()
        subtype = "plain"

        if email.body_type:
            subtype = email.body_type

        msg.attach(MIMEText(email.body, _subtype=subtype))
        if email.attachments:
            msg.attach(MIMEApplication(
                get(email.attachments).content,
                Name=basename(email.attachments)
            ))

        if email.from_email and email.from_name:
            msg['From'] = email.from_name + f" <{email.from_email}>"

        msg['To'] = email.to
        if email.cc: msg['Cc'] = email.cc
        if email.bcc: msg['Bcc'] = email.bcc
        msg['Subject'] = email.subject
        if email.signature: msg['Sender'] = email.signature
        if email.in_reply_to:
            msg['In-Reply-To'] = email.in_reply_to
            msg['References'] = email.in_reply_to

        return base64.b64encode(msg.as_bytes()).decode()

    def send_email(self, context, payload):
        """ Create and send a new email message. """

        access_token = util.get_access_token(context['headers'])
        email = Gmail(**payload)
        url = util.get_url(context) + "messages/send"
        data = { "raw": self.get_raw(email) }
        if email.thread_id: data["threadId"] = email.thread_id
        response = util.rest("POST", url, access_token, data)

        if response.status_code > 400:
            raise Exception("Error ", response.text)

        if email.label:
            response_obj = json.loads(response.text)
            data = {
                "label": email.label,
                "message_id": response_obj['id']
            }
            return self.add_label_to_email(context, data)

        return json.loads(response.text)

    def create_label(self, context, payload):
        """ Creates a new label. """

        access_token = util.get_access_token(context['headers'])
        url = util.get_url(context) + "labels"
        response = util.rest("POST", url, access_token, payload)

        if response.status_code > 400:
            raise Exception("Error ", response.text)

        return json.loads(response.text)

    def reply_to_email(self, context, payload):
        """ Send a reply to an email message """

        email = Gmail(**payload)
        msg_data = self.email_helper(context, payload)
        email.subject = msg_data["subject"]

        if not email.to:
            email.to = msg_data['from']

        email.in_reply_to = msg_data['message_id']
        data = {
            "threadId": email.thread_id,
            "raw": self.get_raw(email)
            }

        access_token = util.get_access_token(context['headers'])
        url = util.get_url(context) + "messages/send"
        response = util.rest("POST", url, access_token, data)

        if response.status_code > 400:
            raise Exception("Error ", response.text)

        return json.loads(response.text)
        # return None

    def remove_label_from_email(self, context, payload):
        """ Remove a label from an email message """

        labels = GmailActions.labels(context)['labels']
        label_id = ""

        for i in range(len(labels)):
            if labels[i]['name'] == payload['label']:
                label_id = labels[i]['id']
                break

        data = {
            "removeLabelIds": [
                label_id
            ]
        }

        access_token = util.get_access_token(context['headers'])
        url = util.get_url(context) + f"messages/{payload['message_id']}/modify"
        response = util.rest("POST", url, access_token, data)

        if response.status_code > 400:
            raise Exception("Error ", response.text)

        return json.loads(response.text)

    def add_label_to_email(self, context, payload):
        """ Add a label to an email message """

        labels = GmailActions.labels(context)['labels']
        label_id = ""

        for i in range(len(labels)):
            if labels[i]['name'] == payload['label']:
                label_id = labels[i]['id']
                break

        data = {
            "addLabelIds": [
                label_id
            ]
        }
        access_token = util.get_access_token(context['headers'])
        url = util.get_url(context) + f"messages/{payload['message_id']}/modify"
        response = util.rest("POST", url, access_token, data)

        if response.status_code > 400:
            raise Exception("Error ", response.text)

        return json.loads(response.text)

    def create_draft(self, context, payload):
        """ Create (but do not send) a new email message """

        access_token = util.get_access_token(context['headers'])
        url = util.get_url(context) + "drafts"
        email = Gmail(**payload)
        data = {
            "message": {
                "raw": self.get_raw(email)
            }
        }
        response = util.rest("POST", url, access_token, data)

        if response.status_code > 400:
            raise Exception("Error ", response.text)

        return json.loads(response.text)

    def make_email_read(self, context, payload):
        """ Marks an email or a draft in a selected directory as read by setting the "Read" flag. """

        data = {
            "message_id": payload["message_id"],
            "label": "UNREAD"
        }

        return self.remove_label_from_email(context, data)
