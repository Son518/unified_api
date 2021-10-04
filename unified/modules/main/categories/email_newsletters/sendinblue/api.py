import json
import sib_api_v3_sdk
from email_newsletters.sendinblue import util
from email_newsletters.sendinblue.entities.sendinblue_subscriber import SendinblueSubscriber
from email_newsletters.sendinblue.entities.sendinblue_list import SendinblueList
from email_newsletters.sendinblue.entities.sendinblue_campaign import SendinblueCampaign


class SendinblueApi():

    def contact(self, context, params):
        ''' returns a single contact '''

        sendinblue_configuration = util.sendinblue_configuration(
            context['headers'])
        # create an instance of the API class
        contact_instance = sib_api_v3_sdk.ContactsApi(
            sib_api_v3_sdk.ApiClient(sendinblue_configuration))
        contact = contact_instance.get_contact_info(params['contact_id'])
        contact = contact.to_dict()
        contact_obj = SendinblueSubscriber(
            first_name=contact.get("attributes").get("FIRSTNAME") or None,
            last_name=contact.get("attributes").get("LASTNAME") or None,
            sms=contact.get("attributes").get("SMS") or None,
            email=contact.get("email") or None,
            created_date=contact.get("created_at") or None,
            updated_date=contact.get("modified_at") or None,
            list_id=contact.get("list_ids") or None,
            contact_id=contact.get("id") or None,
        )

        return contact_obj.__dict__

    def contacts(self, context, params):
        ''' returns all contacts'''

        sendinblue_configuration = util.sendinblue_configuration(
            context['headers'])
        # create an instance of the API class
        contact_instance = sib_api_v3_sdk.ContactsApi(
            sib_api_v3_sdk.ApiClient(sendinblue_configuration))
        contacts = contact_instance.get_contacts()
        contacts = (contacts.to_dict())["contacts"]
        contact_value = []
        for contact in contacts:
            contact_obj = SendinblueSubscriber(
                first_name=contact.get("attributes").get("FIRSTNAME") or None,
                last_name=contact.get("attributes").get("LASTNAME") or None,
                sms=contact.get("attributes").get("SMS") or None,
                email=contact.get("email") or None,
                created_date=contact.get("createdAt") or None,
                updated_date=contact.get("modifiedAt") or None,
                list_id=contact.get("listIds") or None,
                contact_id=contact.get("id") or None,
            )
            contact_value.append(contact_obj.__dict__)

        return json.dumps(contact_value)

    def lists(self, context, params):
        ''' returns all lists'''

        sendinblue_configuration = util.sendinblue_configuration(
            context['headers'])
        # create an instance of the API class
        contact_instance = sib_api_v3_sdk.ContactsApi(
            sib_api_v3_sdk.ApiClient(sendinblue_configuration))
        lists = contact_instance.get_lists()
        lists = (lists.to_dict())["lists"]
        list_value = []
        for list in lists:
            list_obj = SendinblueList(
                list_id=list.get("id") or None,
                name=list.get("name") or None,
                created_date=list.get("created_at") or None,
                dynamic_list=list.get("dynamic_list") or False,
                folder_id=list.get("folderId") or None,
                total_subscribers=list.get("totalSubscribers") or None,
                unique_subscribers=list.get("uniqueSubscribers") or None
            )
            list_value.append(list_obj.__dict__)

        return json.dumps(list_value)

    def list(self, context, params):
        ''' returns a single list'''

        sendinblue_configuration = util.sendinblue_configuration(
            context['headers'])
        # create an instance of the API class
        contact_instance = sib_api_v3_sdk.ContactsApi(
            sib_api_v3_sdk.ApiClient(sendinblue_configuration))
        list = contact_instance.get_list(params["list_id"])
        list = list.to_dict()
        list_obj = SendinblueList(
            list_id=list.get("id") or None,
            name=list.get("name") or None,
            created_date=list.get("created_at") or None,
            dynamic_list=list.get("dynamic_list") or False,
            folder_id=list.get("folder_id") or None,
            total_subscribers=list.get("total_subscribers") or None,
            unique_subscribers=list.get("unique_subscribers") or None
        )
        return list_obj.__dict__

    def folders(self, context, params):
        ''' returns all folders'''

        sendinblue_configuration = util.sendinblue_configuration(
            context['headers'])
        # create an instance of the API class
        contact_instance = sib_api_v3_sdk.ContactsApi(
            sib_api_v3_sdk.ApiClient(sendinblue_configuration))
        folders = contact_instance.get_folders(10, 0)
        folders = (folders.to_dict())["folders"]
        folder_value = []
        for folder in folders:
            folder_obj = SendinblueList(
                folder_id=folder.get("id") or None,
                name=folder.get("name") or None,
                total_subscribers=folder.get("totalSubscribers") or None,
                unique_subscribers=folder.get("uniqueSubscribers") or None
            )
            folder_value.append(folder_obj.__dict__)
        return json.dumps(folder_value)

    def folder(self, context, params):
        ''' returns a single folder'''

        sendinblue_configuration = util.sendinblue_configuration(
            context['headers'])
        # create an instance of the API class
        contact_instance = sib_api_v3_sdk.ContactsApi(
            sib_api_v3_sdk.ApiClient(sendinblue_configuration))
        folder = contact_instance.get_folder(params['folder_id'])
        folder = folder.to_dict()
        folder_obj = SendinblueList(
            folder_id=folder.get("id") or None,
            name=folder.get("name") or None,
            total_subscribers=folder.get("total_subscribers") or None,
            unique_subscribers=folder.get("unique_subscribers") or None
        )

        return folder_obj.__dict__

    def list_contacts(self, context, params):
        ''' returns all contacts from a  list'''

        sendinblue_configuration = util.sendinblue_configuration(
            context['headers'])
        # create an instance of the API class
        contact_instance = sib_api_v3_sdk.ContactsApi(
            sib_api_v3_sdk.ApiClient(sendinblue_configuration))
        lists = contact_instance.get_contacts_from_list(params["list_id"])
        contacts = (lists.to_dict())["contacts"]
        contact_value = []
        for contact in contacts:
            contact_obj = SendinblueSubscriber(
                first_name=contact.get("attributes").get("FIRSTNAME") or None,
                last_name=contact.get("attributes").get("LASTNAME") or None,
                sms=contact.get("attributes").get("SMS") or None,
                email=contact.get("email") or None,
                created_date=contact.get("createdAt") or None,
                updated_date=contact.get("modifiedAt") or None,
                list_id=contact.get("listIds") or None,
                contact_id=contact.get("id") or None,
            )
            contact_value.append(contact_obj.__dict__)

        return json.dumps(contact_value)

    def email_campaigns(self, context, contact_entity):
        ''' returns all emailcampaigns'''

        sendinblue_configuration = util.sendinblue_configuration(
            context['headers'])
        # create an instance of the API class
        contact_instance = sib_api_v3_sdk.EmailCampaignsApi(
            sib_api_v3_sdk.ApiClient(sendinblue_configuration))
        campaigns = contact_instance.get_email_campaigns()
        campaigns = (campaigns.to_dict())["campaigns"]
        campaign_value = []
        for campaign in campaigns:
            campaign_obj = SendinblueCampaign(
                campaign_id=campaign.get("id") or None,
                campaign_name=campaign.get("name") or None,
                ab_testing=campaign.get("abTesting") or None,
                html_url=campaign.get("shareLink") or None,
                html_content=campaign.get("htmlContent") or None,
                reply_email=campaign.get("replyTo") or None,
                from_email=campaign.get("sender").get("email") or None,
                from_name=campaign.get("sender").get("name") or None,
                subject=campaign.get("subject") or None,
                list_id=campaign.get("recipients").get("lists") or None,
            )
            campaign_value.append(campaign_obj.__dict__)
        return json.dumps(campaign_value)
    
    def profile(self,context,params):
        """
        get call to show user authenticated information
        """
        sendinblue_configuration = util.sendinblue_configuration(
            context['headers'])
        api_instance = sib_api_v3_sdk.AccountApi(sib_api_v3_sdk.ApiClient(sendinblue_configuration))
        response = api_instance.get_account().to_dict()
        profile = {
            'name':response['first_name'],
            'email':response['email']
        }
        return profile
    
    def verify(self,context,params):
        """
        get call to verify user authenticated information
        """
        sendinblue_configuration = util.sendinblue_configuration(
            context['headers'])
        api_instance = sib_api_v3_sdk.AccountApi(sib_api_v3_sdk.ApiClient(sendinblue_configuration))
        response = api_instance.get_account().to_dict()
        return response