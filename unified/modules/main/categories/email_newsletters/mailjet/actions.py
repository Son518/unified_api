import json
from email_newsletters.mailjet import util
from unified.core.actions import Actions
from email_newsletters.mailjet.entities.mailjet_subscriber import MailjetSubscriber
from email_newsletters.mailjet.entities.mailjet_transactionalemail import MailjetTransactionalemail
from email_newsletters.mailjet.entities.mailjet_campaign import MailjetCampaign


class MailjetActions(Actions):

    def add_subscriber(self, context, subscriber_entity):
        """ Add or create subscriber"""

        mailjet_client = util.mailjet_client(context['headers'])
        subscriber_schema = MailjetSubscriber(**subscriber_entity)
        data = {
            'IsExcludedFromCampaigns': "true",
            'Name': subscriber_schema.name,
            'Email': subscriber_schema.email
        }
        result = mailjet_client.contact.create(data=data).text
        return json.loads(result)


    def send_plain_text_email(self, context, plaintext_entity):
        """ Send a plain text content email"""

        mailjet_client = util.mailjet_client(context['headers'])
        plaintext_schema = MailjetTransactionalemail(**plaintext_entity)

        plaintext_data = data = {
            'FromEmail': plaintext_schema.from_address,
            'FromName': plaintext_schema.from_name,
            'Subject': plaintext_schema.subject,
            'Text-part': plaintext_schema.email_text_body,
            'to': plaintext_schema.to,
            'cc': plaintext_schema.cc,
            'bcc': plaintext_schema.bcc
        }
        result = mailjet_client.send.create(data=plaintext_data).text
        return json.loads((result))


    def send_html_email(self, context, html_entity):
        """ Send HTML content email"""

        mailjet_client = util.mailjet_client(context['headers'])
        html_schema = MailjetTransactionalemail(**html_entity)

        html_data = data = {
            'FromEmail': html_schema.from_address,
            'FromName': html_schema.from_name,
            'Subject': html_schema.subject,
            'Html-part': html_schema.email_body,
            'to': html_schema.to,
            'cc': html_schema.cc,
            'bcc': html_schema.bcc
        }
        result = mailjet_client.send.create(data=html_data).text
        return json.loads(result)


    def send_a_sms(self, context, sms_entity):
        """ Send SMS 
         Note: To complete send SMS functionality we need to purchase the account"""

        mailjet_client = util.mailjet_client(context['headers'])
        sms_schema = MailjetTransactionalemail(**sms_entity)
        sms_data = {
            "From": sms_schema.from_address,
            "To": sms_schema.to,
            "Text": sms_schema.text
        }


    def send_email_using_template(self, context, template_entity):
        """ Send email using template"""

        mailjet_client = util.mailjet_client(context['headers'])

        # there is no specific entity for template so fields from transactionalemails are binded
        template_schema = MailjetTransactionalemail(**template_entity)
        template_data = {
            'FromEmail': template_schema.from_address,
            'FromName': template_schema.from_name,
            'Subject': template_schema.subject,
            'MJ-TemplateID': template_schema.template,
            'MJ-TemplateLanguage': template_schema.template_language,
            'to': template_schema.to,
            'cc': template_schema.cc,
            'bcc': template_schema.bcc
        }
        result = mailjet_client.send.create(data=template_data).text
        return json.loads(result)


    def send_an_email_campaign_to_list(self, context, campaign_entity):
        """ Send an email campaingn to list"""

        mailjet_client = util.mailjet_client(context['headers'])

        # Mj-deduplicatecampaign set to 1 to stop contacts being emailed several times in the same campaign
        campaign_schema = MailjetCampaign(**campaign_entity)
        campaign_data = {
            'FromEmail': campaign_schema.from_address,
            'FromName': campaign_schema.from_name,
            'Subject': campaign_schema.subject,
            'Text-part': campaign_schema.email_body,
            'to': campaign_schema.reply_to,
            'Mj-campaign': campaign_schema.campaign_title,
            'Mj-deduplicatecampaign': '1'
        }

        result = mailjet_client.send.create(data=campaign_data).text
        return json.loads(result)


    def unsubscribe_email(self, context, unsubscriber_entity):
        """  Unsubscribe email"""

        mailjet_client = util.mailjet_client(context['headers'])

        # Mj-deduplicatecampaign set to 1 to stop contacts being emailed several times in the same campaign
        unsubscribe_schema = MailjetSubscriber(**unsubscriber_entity)
        unsubscribe_data = {
            'ContactsLists': [
                {
                    "Action": "unsub",
                    "ListID": unsubscribe_schema.list_id
                }
            ]
        }

        result = mailjet_client.contact_managecontactslists.create(
            id=unsubscribe_schema.contact_id, data=unsubscribe_data).text
        return json.loads(result)