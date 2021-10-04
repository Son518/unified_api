import json

from unified.core.actions import Actions
from phone_sms.clicksend_sms import util
from phone_sms.clicksend_sms.entities.clicksend_contact import ClickSend_Contact
from phone_sms.clicksend_sms.entities.clicksend_send_voice import ClickSend_Send_Voice
from phone_sms.clicksend_sms.entities.clicksend_send_sms import ClickSend_Send_SMS
from phone_sms.clicksend_sms.entities.clicksend_letter import ClickSend_Letter
from phone_sms.clicksend_sms.entities.clicksend_send_mms import ClickSend_Send_MMS
from phone_sms.clicksend_sms.entities.clicksend_send_fax import ClickSend_Send_Fax

import clicksend_client

class ClickSendActions(Actions):
    def create_contact(self, context, task_entity):
        '''Create a contact'''

        configuration = util.get_clicksend_configuration(context['headers'])
        api_instance = clicksend_client.ContactApi(clicksend_client.ApiClient(configuration))
        task_schema = ClickSend_Contact(**task_entity)

        contact = clicksend_client.Contact(
          phone_number=task_schema.phone_number,
          first_name=task_schema.full_name,
          last_name=task_schema.last_name,
          custom_1=task_schema.custom_1,
          fax_number=task_schema.fax_number,
          organization_name=task_schema.organization_name,
          email=task_schema.email,
          address_city=task_schema.city,
          address_state=task_schema.state,
          address_postal_code=task_schema.postal_code,
          address_country=task_schema.country)
        list_id = task_schema.contact_list

        api_response = api_instance.lists_contacts_by_list_id_post(contact, list_id)
        api_response = api_response.replace("\'", "\"")
        return json.loads(api_response)

    def delete_contact(self, context, task_entity):
        '''Delete a contact'''

        configuration = util.get_clicksend_configuration(context['headers'])
        api_instance = clicksend_client.ContactApi(clicksend_client.ApiClient(configuration))
        task_schema = ClickSend_Contact(**task_entity)

        list_id = task_schema.contact_list
        contact_id = task_schema.contact_id

        api_response = api_instance.lists_contacts_by_list_id_and_contact_id_delete(list_id, contact_id)
        api_response = api_response.replace("\'", "\"")
        api_response = json.dumps(api_response).replace("None", "null")
        return json.loads(api_response)

    def create_contact_list(self, context, task_entity):
        '''Create a contact list'''

        configuration = util.get_clicksend_configuration(context['headers'])
        api_instance = clicksend_client.ContactListApi(clicksend_client.ApiClient(configuration))
        task_schema = ClickSend_Contact(**task_entity)

        list = clicksend_client.ContactList(list_name=task_schema.list_name)

        api_response = api_instance.lists_post(list)
        api_response = api_response.replace("\'", "\"")
        return json.loads(api_response)

    def delete_contact_list(self, context, task_entity):
        '''Delete a contact list'''

        configuration = util.get_clicksend_configuration(context['headers'])
        api_instance = clicksend_client.ContactListApi(clicksend_client.ApiClient(configuration))
        task_schema = ClickSend_Contact(**task_entity)

        list_id = task_schema.contact_list

        api_response = api_instance.lists_by_list_id_delete(list_id)
        api_response = api_response.replace("\'", "\"")
        api_response = json.dumps(api_response).replace("None", "null")
        return json.loads(api_response)

    def send_postcard(self, context, task_entity):
        '''Send a postcard'''

        configuration = util.get_clicksend_configuration(context['headers'])
        api_instance = clicksend_client.PostPostcardApi(clicksend_client.ApiClient(configuration))
        task_schema = ClickSend_Letter(**task_entity)

        #File not found. Need to replace task_schema.pdf_file_url with a valid file
        file_url_list = [task_schema.pdf_file_url]
        recipient = clicksend_client.PostRecipient(
            address_name=task_schema.address_name,
            address_line_1=task_schema.line_1,
            address_city=task_schema.city,
            address_state=task_schema.state,
            address_postal_code=task_schema.postal_code,
            address_country=task_schema.country,
            return_address_id=task_schema.return_address)
        post_postcards = clicksend_client.PostPostcard(file_urls=file_url_list,recipients=[recipient])

        api_response = api_instance.post_postcards_send_post(post_postcards)
        api_response = api_response.replace("\'", "\"")
        return json.loads(api_response)

    def send_fax(self, context, task_entity):
        '''Send a fax'''

        configuration = util.get_clicksend_configuration(context['headers'])
        api_instance = clicksend_client.FAXApi(clicksend_client.ApiClient(configuration))
        task_schema = ClickSend_Send_Fax(**task_entity)

        #File not found. Need to replace task_schema.pdf_file_url with a valid file
        file_url = task_schema.pdf_file_url
        fax_message_list = [clicksend_client.FaxMessage(
            to=task_schema.to,
            _from=task_schema.sent_from)]
        fax_message = clicksend_client.FaxMessageCollection(file_url=file_url, messages=fax_message_list)

        api_response = api_instance.fax_send_post(fax_message)
        api_response = api_response.replace("\'", "\"")
        return json.loads(api_response)

    def send_mms(self, context, task_entity):
        '''Send a new MMS'''

        configuration = util.get_clicksend_configuration(context['headers'])
        api_instance = clicksend_client.MMSApi(clicksend_client.ApiClient(configuration))
        task_schema = ClickSend_Send_MMS(**task_entity)

        mms_message = clicksend_client.MmsMessage(
            body=task_schema.body,
            to=task_schema.to,
            subject=task_schema.subject,
            schedule=task_schema.schedule)
        mms_messages = clicksend_client.MmsMessageCollection(
            #File not found. Need to replace task_schema.pdf_file_url with a valid file
            media_file=task_schema.media_url,
            messages=[mms_message])

        api_response = api_instance.mms_send_post(mms_messages)
        api_response = api_response.replace("\'", "\"")
        return json.loads(api_response)

    def send_letter(self, context, task_entity):
        '''Send a PDF letter'''

        configuration = util.get_clicksend_configuration(context['headers'])
        api_instance = clicksend_client.PostLetterApi(clicksend_client.ApiClient(configuration))
        task_schema = ClickSend_Letter(**task_entity)

        post_recipient = clicksend_client.PostRecipient(
            address_name=task_schema.address_name,
            address_line_1=task_schema.line_1,
            address_city=task_schema.city,
            address_state=task_schema.state,
            address_postal_code=task_schema.postal_code,
            address_country=task_schema.country,
            return_address_id=task_schema.return_address)
        post_letter = clicksend_client.PostLetter(
            #File not found. Need to replace task_schema.pdf_file_url with a valid file
            file_url=task_schema.pdf_file_url,
            template_used=task_schema.template_used,
            colour=task_schema.colour,
            duplex=task_schema.duplex,
            recipients=[post_recipient])

        api_response = api_instance.post_letters_send_post(post_letter)
        api_response = api_response.replace("\'", "\"")
        return json.loads(api_response)

    def create_sms_to_contact_list(self, context, task_entity):
        '''Send a new SMS to contact list'''

        configuration = util.get_clicksend_configuration(context['headers'])
        api_instance = clicksend_client.SMSApi(clicksend_client.ApiClient(configuration))
        task_schema = ClickSend_Send_SMS(**task_entity)

        sms_message = clicksend_client.SmsMessage(
            body=task_schema.message,
            list_id=task_schema.contact_list_name,
            _from=task_schema.sent_from,
            schedule=task_schema.schedule)
        sms_messages = clicksend_client.SmsMessageCollection(messages=[sms_message])

        api_response = api_instance.sms_send_post(sms_messages)
        api_response = api_response.replace("\'", "\"")
        return json.loads(api_response)

    def send_voice(self, context, task_entity):
        '''Send a Voice Text-to-Speech message'''

        configuration = util.get_clicksend_configuration(context['headers'])
        api_instance = clicksend_client.VoiceApi(clicksend_client.ApiClient(configuration))
        task_schema = ClickSend_Send_Voice(**task_entity)

        voice_message = clicksend_client.VoiceMessage(
            to=task_schema.to,
            lang=task_schema.language,
            body=task_schema.message,
            voice=task_schema.voice,
            schedule=task_schema.schedule,
            custom_string=task_schema.custom_string,
            country=task_schema.country)
        voice_messages = clicksend_client.VoiceMessageCollection(messages=[voice_message])

        api_response = api_instance.voice_send_post(voice_messages)
        api_response = api_response.replace("\'", "\"")
        return json.loads(api_response)
