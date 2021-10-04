import json
from lib import logger
import sib_api_v3_sdk
from email_newsletters.sendinblue import util
from flask_apiexceptions import ApiException
from unified.core.actions import Actions
from email_newsletters.sendinblue.entities.sendinblue_subscriber import SendinblueSubscriber
from email_newsletters.sendinblue.entities.sendinblue_transactionalemail import SendinblueTransactionalemail
from email_newsletters.sendinblue.entities.sendinblue_campaign import SendinblueCampaign


class SendinblueActions(Actions):

    def add_contact(self, context, contact_entity):
        ''' adding contact in sendin blue'''

        sendinblue_configuration = util.sendinblue_configuration(
            context['headers'])

        # create an instance of the API class
        contact_instance = sib_api_v3_sdk.ContactsApi(
            sib_api_v3_sdk.ApiClient(sendinblue_configuration))
        contact_schema = SendinblueSubscriber(**contact_entity)
        create_contact = sib_api_v3_sdk.CreateContact(
            email=contact_schema.email,
            list_ids=[contact_schema.list_id],
            attributes={
                'first_name': contact_schema.first_name,
                'last_name': contact_schema.last_name,
                'sms': contact_schema.sms
            },
        )  # CreateContact | Values to create a contact

        response = contact_instance.create_contact(create_contact)
        return response.to_dict()

    def update_contact(self, context, contact_entity):
        ''' updating contact in sendin blue'''

        sendinblue_configuration = util.sendinblue_configuration(
            context['headers'])

        # create an instance of the API class
        contact_instance = sib_api_v3_sdk.ContactsApi(
            sib_api_v3_sdk.ApiClient(sendinblue_configuration))
        contact_schema = SendinblueSubscriber(**contact_entity)
        update_contact = sib_api_v3_sdk.UpdateContact(
            list_ids=[contact_schema.list_id],
            attributes={
                'firstname': contact_schema.first_name,
                'lastname': contact_schema.last_name,
                'sms': contact_schema.sms
            }
        )  # CreateContact | Values to create a contact

        try:
            # Update a contact
            response = contact_instance.update_contact(
                contact_schema.contact_id, update_contact)
            contact_response = {"status": 200}
            return contact_response

        except ApiException as e:
            logger.error(
                "Exception when calling ContactsApi->update_folder: %s\n" % e)
            contact_response = {
                "error": "Exception when calling ContactsApi->update_folder: %s\n" % e}
            return contact_response

    def delete_contact(self, context, contact_entity):
        ''' deleting contact in sendin blue'''

        sendinblue_configuration = util.sendinblue_configuration(
            context['headers'])

        # create an instance of the API class
        contact_instance = sib_api_v3_sdk.ContactsApi(
            sib_api_v3_sdk.ApiClient(sendinblue_configuration))
        contact_schema = SendinblueSubscriber(**contact_entity)

        try:
            # delete a contact
            response = contact_instance.delete_contact(
                contact_schema.contact_id)
            contact_response = {"status": 200}
            return contact_response

        except ApiException as e:
            logger.error(
                "Exception when calling ContactsApi->update_folder: %s\n" % e)
            contact_response = {
                "error": "Exception when calling ContactsApi->update_folder: %s\n" % e}
            return contact_response

    def create_a_folder(self, context, folder_entity):
        ''' creating folder in sendin blue'''

        sendinblue_configuration = util.sendinblue_configuration(
            context['headers'])

        # create an instance of the API class
        folder_instance = sib_api_v3_sdk.FoldersApi(
            sib_api_v3_sdk.ApiClient(sendinblue_configuration))
        folder_schema = SendinblueSubscriber(**folder_entity)
        create_folder = sib_api_v3_sdk.CreateUpdateFolder(
            name=folder_schema.folder_name)

        response = folder_instance.create_folder(create_folder)
        return response.to_dict()

    def update_a_folder(self, context, folder_entity):
        ''' creating folder in sendin blue'''

        sendinblue_configuration = util.sendinblue_configuration(
            context['headers'])

        # create an instance of the API class
        folder_instance = sib_api_v3_sdk.ContactsApi(
            sib_api_v3_sdk.ApiClient(sendinblue_configuration))
        folder_schema = SendinblueSubscriber(**folder_entity)
        update_folder = sib_api_v3_sdk.CreateUpdateFolder(
            name=folder_schema.folder_name)

        try:
            # Update a folder
            response = folder_instance.update_folder(
                folder_schema.folder_id, update_folder)
            folder_response = {"status": 200}
            return folder_response

        except ApiException as e:
            logger.error(
                "Exception when calling ContactsApi->update_folder: %s\n" % e)
            folder_response = {
                "error": "Exception when calling ContactsApi->update_folder: %s\n" % e}
            return folder_response

    def delete_a_folder(self, context, folder_entity):
        ''' deleting contact in sendin blue'''
        sendinblue_configuration = util.sendinblue_configuration(
            context['headers'])

        # create an instance of the API class
        folder_instance = sib_api_v3_sdk.FoldersApi(
            sib_api_v3_sdk.ApiClient(sendinblue_configuration))
        folder_schema = SendinblueSubscriber(**folder_entity)
        response = folder_instance.delete_folder(folder_schema.folder_id)

        try:
            # delete a folder
            response = folder_instance.delete_folder(folder_schema.folder_id)
            folder_response = {"status": 200}
            return folder_response

        except ApiException as e:
            logger.error(
                "Exception when calling ContactsApi->update_folder: %s\n" % e)
            folder_response = {
                "error": "Exception when calling ContactsApi->update_folder: %s\n" % e}
            return folder_response

    def create_a_list(self, context, list_entity):
        ''' creating folder in sendin blue'''

        sendinblue_configuration = util.sendinblue_configuration(
            context['headers'])

        # create an instance of the API class
        list_instance = sib_api_v3_sdk.ContactsApi(
            sib_api_v3_sdk.ApiClient(sendinblue_configuration))
        list_schema = SendinblueSubscriber(**list_entity)
        create_list = sib_api_v3_sdk.CreateList(
            name=list_schema.list_name,
            folder_id=list_schema.folder_id
        )

        response = list_instance.create_list(create_list)
        return response.to_dict()

    def update_a_list(self, context, list_entity):
        ''' updating contact in sendin blue'''

        sendinblue_configuration = util.sendinblue_configuration(
            context['headers'])

        # create an instance of the API class
        list_instance = sib_api_v3_sdk.ContactsApi(
            sib_api_v3_sdk.ApiClient(sendinblue_configuration))
        list_schema = SendinblueSubscriber(**list_entity)
        update_list = sib_api_v3_sdk.UpdateList(name=list_schema.list_name,)

        try:
            # Update a list
            response = list_instance.update_list(
                list_schema.list_id, update_list)
            list_response = {"status": 200}
            return list_response
        except ApiException as e:
            logger.error(
                "Exception when calling ContactsApi->update_list: %s\n" % e)
            list_response = {
                "error": "Exception when calling ContactsApi->update_list: %s\n" % e}
            return list_response

    def delete_a_list(self, context, list_entity):
        ''' deletes contact in sendin blue'''

        sendinblue_configuration = util.sendinblue_configuration(
            context['headers'])

        # create an instance of the API class
        list_instance = sib_api_v3_sdk.ContactsApi(
            sib_api_v3_sdk.ApiClient(sendinblue_configuration))
        list_schema = SendinblueSubscriber(**list_entity)

        try:
            # delete a list
            response = list_instance.delete_list(list_schema.list_id)
            list_response = {"status": 200}
            return list_response
        except ApiException as e:
            logger.error(
                "Exception when calling ContactsApi->update_list: %s\n" % e)
            list_response = {
                "error": "Exception when calling ContactsApi->update_list: %s\n" % e}
            return list_response

    def create_an_email_campaign(self, context, campaign_entity):
        ''' creates an email campaign in sendin blue'''

        sendinblue_configuration = util.sendinblue_configuration(
            context['headers'])

        # create an instance of the API class
        campaign_instance = sib_api_v3_sdk.EmailCampaignsApi(
            sib_api_v3_sdk.ApiClient(sendinblue_configuration))
        campaign_schema = SendinblueCampaign(**campaign_entity)
        email_campaign = sib_api_v3_sdk.CreateEmailCampaign(
            name=campaign_schema.campaign_name,
            subject=campaign_schema.subject,
            html_content=campaign_schema.html_content,
            reply_to=campaign_schema.from_email,
            sender={
                'name': campaign_schema.sender,
                'id': campaign_schema.sender_id
            },
            params={
                'name': campaign_schema.name
            }
        )  # CreateContact | Values to create a contact

        response = campaign_instance.create_email_campaign(email_campaign)
        return response.to_dict()

    def update_an_email_campaign(self, context, campaign_entity):
        ''' updates an email campaign in sendin blue'''

        sendinblue_configuration = util.sendinblue_configuration(
            context['headers'])

        # create an instance of the API class
        campaign_instance = sib_api_v3_sdk.EmailCampaignsApi(
            sib_api_v3_sdk.ApiClient(sendinblue_configuration))
        campaign_schema = SendinblueCampaign(**campaign_entity)
        email_campaign = sib_api_v3_sdk.UpdateEmailCampaign(
            name=campaign_schema.campaign_name,
            subject=campaign_schema.subject,
            html_content=campaign_schema.html_content,
            reply_to=campaign_schema.from_email,
            sender={
                'name': campaign_schema.sender,
                'id': campaign_schema.sender_id
            },
            params={
                'name': campaign_schema.name
            },
            winner_criteria=campaign_schema.winner_criteria
        )

        try:
            # Update an email campaign
            response = campaign_instance.update_email_campaign(
                campaign_schema.campaign_id, email_campaign)
            campaign_response = {"status": 200}
            return campaign_response
        except ApiException as e:
            logger.error(
                "Exception when calling EmailCampaignsApi->update_email_campaign: %s\n" % e)
            campaign_response = {
                "error": "Exception when calling EmailCampaignsApi->update_email_campaign: %s\n" % e}
            return campaign_response

    def delete_an_email_campaign(self, context, campaign_entity):
        ''' deletes an email campaign in sendin blue'''

        sendinblue_configuration = util.sendinblue_configuration(
            context['headers'])

        # create an instance of the API class
        campaign_instance = sib_api_v3_sdk.EmailCampaignsApi(
            sib_api_v3_sdk.ApiClient(sendinblue_configuration))
        campaign_schema = SendinblueCampaign(**campaign_entity)
        response = campaign_instance.delete_email_campaign(
            campaign_schema.campaign_id)

        try:
            # delete an email campaign
            response = campaign_instance.delete_email_campaign(
                campaign_schema.campaign_id)
            campaign_response = {"status": 200}
            return campaign_response
        except ApiException as e:
            logger.error(
                "Exception when calling EmailCampaignsApi->delete_email_campaign: %s\n" % e)
            campaign_response = {
                "error": "Exception when calling EmailCampaignsApi->delete_email_campaign: %s\n" % e}
            return campaign_response

    def send_a_campaign_report(self, context, campaign_entity):
        ''' sends a campaign report'''

        sendinblue_configuration = util.sendinblue_configuration(
            context['headers'])

        # create an instance of the API class
        campaign_instance = sib_api_v3_sdk.EmailCampaignsApi(
            sib_api_v3_sdk.ApiClient(sendinblue_configuration))
        campaign_schema = SendinblueCampaign(**campaign_entity)
        send_report = sib_api_v3_sdk.SendReport(
            language=campaign_schema.language,
            email={
                'to': [campaign_schema.to],
                'body': campaign_schema.body
            }
        )

        try:
            # Send the report of a campaign
            response = campaign_instance.send_report(
                campaign_schema.campaign_id, send_report)
            report_reponse = {"status": 200}
            return report_reponse
        except ApiException as e:
            logger.error(
                "Exception when calling EmailCampaignsApi->send_report: %s\n" % e)
            report_reponse = {
                "error": "Exception when calling EmailCampaignsApi->send_report: %s\n" % e}
            return report_reponse

    def add_exsiting_contacts_for_a_list(self, context, contact_entity):
        ''' adding contact to list in sendin blue'''

        sendinblue_configuration = util.sendinblue_configuration(
            context['headers'])

        # create an instance of the API class
        contact_instance = sib_api_v3_sdk.ContactsApi(
            sib_api_v3_sdk.ApiClient(sendinblue_configuration))
        contact_schema = SendinblueSubscriber(**contact_entity)
        contact_emails = sib_api_v3_sdk.AddContactToList(
            emails=[contact_schema.email])

        response = contact_instance.add_contact_to_list(
            contact_schema.list_id, contact_emails)
        return response.to_dict()

    def send_transactional_email(self, context, transactionalemail_entity):
        '''sends an transactional email'''

        sendinblue_configuration = util.sendinblue_configuration(
            context['headers'])

        # create an instance of the API class
        email_instance = sib_api_v3_sdk.TransactionalEmailsApi(
            sib_api_v3_sdk.ApiClient(sendinblue_configuration))
        email_schema = SendinblueTransactionalemail(
            **transactionalemail_entity)
        send_email = sib_api_v3_sdk.SendSmtpEmail(
            to=[email_schema.to],
            subject=email_schema.subject,
            reply_to=email_schema.reply_to,
            sender={
                'email': email_schema.email
            }
        )
        response = email_instance.send_transac_email(send_email)
        return response.to_dict()
