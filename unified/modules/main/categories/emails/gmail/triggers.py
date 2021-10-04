from emails.gmail import util
from unified.core.triggers import Triggers
from emails.gmail.apis import GmailApi
from emails.gmail.actions import GmailActions

import json


class GmailTriggers(Triggers):

    def new_attachment(self, context, payload):
        """ Triggers when you receive a new attachment. """

        message_id = payload['id']
        parts = payload['payload']['parts']

        for part in parts:
            if part['mimeType'] == "application/octet-stream" and part['filename']:
                att_id = part['body']['attachmentId']

        data = {
            "message_id": message_id,
            "attachment_id": att_id
        }

        return GmailApi.attachment(context, data)

    def new_email(self, context, payload):
        """ Triggers when a new e-mail appears in the mailbox. """

        access_token = util.get_access_token(context['headers'])
        url = util.get_url(context) + f"messages/{payload['id']}"
        response = util.rest("GET", url, access_token)

        if response.status_code > 400:
            raise Exception("Error ", response.text)

        email_obj = json.loads(response.text)

        return GmailApi.get_email_data(email_obj)

    def new_label(self, context, payload):
        """ Triggers when you add a new label. """

        labels = GmailActions.labels(context)['labels']
        label_id = ""

        for label in labels:
            if label['name'] == payload['name']:
                label_id = label['id']
                break

        access_token = util.get_access_token(context['headers'])
        url = util.get_url(context) + f"labels/{label_id}"
        response = util.rest("GET", url, access_token)

        if response.status_code > 400:
            raise Exception("Error ", response.text)

        return json.loads(response.text)

    def new_labeled_email(self, context, payload):
        """ Triggers when you label an email """

        access_token = util.get_access_token(context['headers'])
        url = util.get_url(context) + f"messages/{payload['id']}"
        response = util.rest("GET", url, access_token)

        return GmailApi.get_email_data(json.loads(response.text))

    def new_thread(self, context, payload):
        """ Triggers when a new thread starts """

        access_token = util.get_access_token(context['headers'])
        url = util.get_url(context) + f"threads/{payload['threadId']}"
        response = util.rest("GET", url, access_token)

        return json.loads(response.text)
