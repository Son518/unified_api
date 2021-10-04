import json
from customer_support.zendesk import util
from customer_support.zendesk.entities.zendesk_ticket import ZendeskTicket
from customer_support.zendesk.entities.zendesk_group import ZendeskGroup
from customer_support.zendesk.entities.zendesk_organization import ZendeskOrganization
from customer_support.zendesk.entities.zendesk_user import ZendeskUser


class ZendeskApi():

    def ticket(self, context, params):
        """
        gets a ticket using ticket_id
        context holds the headers 
        params holds ticket_id
        """
        client = util.get_zendesk_client(context["headers"])
        response = client.search._get_ticket(params['ticket_id']).to_dict()
        ticket = ZendeskTicket(subject=response["subject"],
                               description=response["description"],
                               assignee=response["assignee_id"],
                               collaborators=response["collaborator_ids"],
                               group=response["group_id"],
                               tags=response["tags"],
                               status=response["status"],
                               type=response["type"],
                               due_at=response["due_at"],
                               priority=response["priority"],
                               ticket_id=response["id"],
                               )
        return ticket.__dict__

    def organization(self, context, params):
        """
        gets a organization using organization_id
        context holds the headers 
        params holds organization_id
        """
        client = util.get_zendesk_client(context["headers"])
        response = client.search._get_organization(
            params['organization_id']).to_dict()
        organization = ZendeskOrganization(name=response["name"],
                                           details=response["details"],
                                           notes=response["notes"],
                                           tags=response["tags"],
                                           domain_names=response["domain_names"],
                                           external_id=response["external_id"],
                                           shared_tickets=response["shared_tickets"],
                                           shared_comments=response["shared_comments"],
                                           organization_id=response["id"],
                                           created_date=response["created_at"]
                                           )
        return organization.__dict__

    def user(self, context, params):
        """
        gets a user using user_id
        context holds the headers 
        params holds user_id
        """
        client = util.get_zendesk_client(context["headers"])
        response = client.search._get_user(params['user_id']).to_dict()
        user = ZendeskUser(name=response["name"],
                           email=response["email"],
                           details=response["details"],
                           notes=response["notes"],
                           phone=response["phone"],
                           tags=response["tags"],
                           role=response["role"],
                           organization_id=response["organization_id"],
                           external_id=response["external_id"],
                           user_id=response["id"],
                           created_date=response["created_at"],
                           updated_date=response["updated_at"],
                           )
        return user.__dict__

    def group(self, context, params):
        """
        gets a group using group_id
        context holds the headers 
        params holds group_id
        """
        client = util.get_zendesk_client(context["headers"])
        response = client.search._get_group(params['group_id']).to_dict()
        group = ZendeskGroup(created_date=response["created_at"],
                             default=response["default"],
                             deleted=response["deleted"],
                             description=response["description"],
                             group_id=response["id"],
                             group_name=response["name"],
                             updated_date=response["updated_at"],
                             url=response["url"]
                             )
        return group.__dict__