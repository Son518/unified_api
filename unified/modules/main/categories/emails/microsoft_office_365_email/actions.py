from unified.core.actions import Actions
from emails.microsoft_office_365_email import util
from emails.entities.email_entities import Email
from emails.microsoft_office_365_email.entities.microsoft_office_attachment import Microsoftoffice365emailattachment

import base64
import requests


class Microsoftoffice365emailActions(Actions):

    def send_email(self, context, payload):
        '''Create and send a new email message.'''
        access_token = util.get_access_token(context['headers'])
        email = Email(**payload)
        url = "https://graph.microsoft.com/v1.0/me/sendMail"
        mail_body = {
            "message": {
                "subject": email.subject,
                "body": {
                    "contentType": email.body_format,
                    "content": email.body
                },
                "toRecipients": [
                    {
                        "emailAddress": {
                            "address": email.to
                        }
                    }
                ],
                "toRecipients": [
                    {
                        "emailAddress": {
                            "address": email.to
                        }
                    }
                ],
            },
            "saveToSentItems": "true"
        }
        if email.cc:
            mail_body["ccRecipients"] = [{'emailAddress': {'address': em}} for em in email.cc] if email.cc else None
        if email.bcc:
            mail_body["bccRecipients"]: [{'emailAddress': {'address': em}} for em in email.bcc] if email.bcc else None
        response = util.rest("POST", url, access_token, mail_body)
        return response.text, response.status_code

    def create_draft(self, context, payload):
        '''Create (but do not send) a new email message'''
        access_token = util.get_access_token(context['headers'])
        email = Email(**payload)
        url = "https://graph.microsoft.com/v1.0/me/messages"
        mail_body = {
            "subject": email.subject,
            "importance": "Low",
            "body": {
                "contentType": email.body_format,
                "content": email.body
            },
            "toRecipients": [
                {
                    "emailAddress": {
                        "address": email.to
                    }
                }
            ],
            "hasAttachments": True,
            "ccRecipients": [{'emailAddress': {'address': em}} for em in email.cc] if email.cc else None,
            "bccRecipients": [{'emailAddress': {'address': em}} for em in email.bcc] if email.bcc else None
        }
        response = util.rest("POST", url, access_token, mail_body)
        return response.text, response.status_code

    def get_as_base64(self, url):
        return base64.b64encode(requests.get(url).content).decode("utf-8")

    def add_attachment(self, context, payload):
        '''Add  an attachment to message'''
        access_token = util.get_access_token(context['headers'])
        attachment = Microsoftoffice365emailattachment(**payload)
        url = f"https://graph.microsoft.com/v1.0/me/messages/{attachment.message_id}/attachments"

        attachment_body = {
            "@odata.type": "#microsoft.graph.fileAttachment",
            "name": attachment.attachment_name,
            "contentBytes": self.get_as_base64(attachment.attachment_url)
        }
        response = util.rest("POST", url, access_token, attachment_body)
        return response.text, response.status_code
