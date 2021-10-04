import json
from requests.models import Response
from transactional_email.postmark.entities.postmark_send_email import PostmarkSendEmail
from core.actions import Actions
from transactional_email.postmark.entities.postmark_send_email_with_template import PostmarkTemplate
from transactional_email.postmark import util

class PostmarkActions(Actions):

    def send_email(self, context, email_payload):
        """ 
        Send new email 
        context holds the headers 
        email_entity holds the request.body
        """
        email_entity = PostmarkSendEmail(**email_payload)
        data ={
            "From":email_entity.from_email_address,
            "To":email_entity.to_email_address,
            "Subject":email_entity.email_subject,
            "CC":email_entity.cc_email_address,
            "BCC":email_entity.bcc_email_address
        }
        if email_entity.text_email_body:
            data["TextBody"] = email_entity.text_email_body
        if email_entity.html_email_body:
            data["HtmlBody"] = email_entity.html_email_body
        response = util.rest("POST","email",data,context["headers"]["server_token"])
        return json.loads(response)

    def send_email_with_template(self, context, template_payload):
        """ 
        Send new email with template
        context holds the headers 
        template_entity holds the request.body

        """
        template_entity = PostmarkTemplate(**template_payload)
        template = {}
        if "user_email" in template_entity.template_model.keys():
            template["email"] = template_entity.template_model["user_email"]
        elif "user_name" in template_entity.template_model.keys():
            template["name"] = template_entity.template_model["user_name"]
        elif "user_phone" in template_entity.template_model.keys():
            template["phone"] = template_entity.template_model["user_phone"]
        data ={
          "From":template_entity.from_address ,
          "To":template_entity.to_recipients ,
          "TemplateId":template_entity.template_id ,
          "TemplateModel":template_entity.template_model
        }
        response = util.rest("POST","template",data,context["headers"]["server_token"])
        return json.loads(response)

    