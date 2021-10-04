import json
from core.actions import Actions
from customer_support.zendesk import util
from customer_support.zendesk.entities.zendesk_ticket import ZendeskTicket
from customer_support.zendesk.entities.zendesk_user import ZendeskUser
from customer_support.zendesk.entities.zendesk_organization import ZendeskOrganization
from customer_support.zendesk.entities.zendesk_attachment import ZendeskAttachment
from zenpy.lib.api_objects import Ticket, User, Organization, Comment, Tag, Attachment


class ZendeskActions(Actions):

    def create_ticket(self, context, ticket_entity):
        """
        creates a ticket 
        context holds the headers 
        ticket_entity holds the request.body
        """
        client = util.get_zendesk_client(context["headers"])
        ticket_schema = ZendeskTicket(**ticket_entity)
        response = client.tickets.create(Ticket(subject=ticket_schema.subject,
                                                description=ticket_schema.description,
                                                assignee_id=ticket_schema.assignee,
                                                collaborator_ids=ticket_schema.collaborators,
                                                collaborator_emails=ticket_schema.collaborator_emails,
                                                group_id=ticket_schema.group,
                                                recipient=ticket_schema.requester_name,
                                                requester_email=ticket_schema.requester_email,
                                                tags=ticket_schema.tags,
                                                status=ticket_schema.status,
                                                type=ticket_schema.type,
                                                due_at=ticket_schema.due_at,
                                                priority=ticket_schema.priority
                                                ))
        return response.to_dict()

    def create_user(self, context, user_entity):
        """
        creates a user 
        context holds the headers 
        user_entity holds the request.bdoy  
        """
        client = util.get_zendesk_client(context["headers"])
        user_schema = ZendeskUser(**user_entity)
        response = client.users.create(User(details=user_schema.details,
                                            email=user_schema.email,
                                            external_id=user_schema.external_id,
                                            name=user_schema.name,
                                            notes=user_schema.notes,
                                            organization_id=user_schema.organization_id,
                                            phone=user_schema.phone,
                                            role=user_schema.role,
                                            tags=user_schema.tags,
                                            ))
        return response.to_dict()

    def create_organization(self, context, organization_entity):
        """
        creates an organization 
        context holds the headers 
        organization_entity holds the request.body
        """
        client = util.get_zendesk_client(context["headers"])
        organization_schema = ZendeskOrganization(**organization_entity)
        response = client.organizations.create(Organization(name=organization_schema.name,
                                                            details=organization_schema.details,
                                                            notes=organization_schema.notes,
                                                            tags=organization_schema.tags,
                                                            domain_names=organization_schema.domain_names,
                                                            external_id=organization_schema.external_id,
                                                            shared_tickets=organization_schema.shared_tickets,
                                                            shared_comments=organization_schema.shared_comments,
                                                            ))
        return response.to_dict()

    def add_comment_to_ticket(self, context, comment_entity):
        """
        adds a comments to ticket 
        context holds the headers 
        comment_entity holds the request.body
        """
        client = util.get_zendesk_client(context["headers"])
        comment_schema = ZendeskTicket(**comment_entity)
        ticket = client.tickets(id=comment_schema.ticket_id)
        ticket.comment = Comment(body=comment_schema.new_comment, public=False)
        response = client.tickets.update(ticket)
        return response.to_dict()

    def add_tag_to_ticket(self, context, tag_entity):
        """
        adds a tag to ticket 
        context holds the headers 
        tag_entity holds the request.body
        """
        client = util.get_zendesk_client(context["headers"])
        tag_schema = ZendeskTicket(**tag_entity)

        ticket = client.tickets(id=tag_schema.ticket_id)
        ticket.tags.extend([tag_schema.tags])
        response = client.tickets.update(ticket)
        return response.to_dict()

    def update_ticket(self, context, ticket_entity):
        """
        updates existing ticket 
        context holds the headers 
        ticket_entity holds the request.body
        """
        client = util.get_zendesk_client(context["headers"])
        ticket_schema = ZendeskTicket(**ticket_entity)
        ticket = client.tickets(id=ticket_schema.ticket_id)
        client.tickets.create(Ticket(subject=ticket_schema.subject,
                                     description=ticket_schema.description if ticket_schema.description else " ",
                                     assignee_id=ticket_schema.assignee,
                                     collaborator_ids=ticket_schema.collaborators,
                                     collaborator_emails=ticket_schema.collaborator_emails,
                                     group_id=ticket_schema.group,
                                     recipient=ticket_schema.requester_name,
                                     requester_email=ticket_schema.requester_email,
                                     tags=ticket_schema.tags,
                                     status=ticket_schema.status,
                                     type=ticket_schema.type,
                                     due_at=ticket_schema.due_at,
                                     priority=ticket_schema.priority
                                     ))
        response = client.tickets.update(ticket)
        return response.to_dict()

    def update_organization(self, context, organization_entity):
        """
        updates existing organization
        context holds the headers 
        organization_entity holds the request.body
        """
        client = util.get_zendesk_client(context["headers"])
        organization_schema = ZendeskOrganization(**organization_entity)
        organization = client.organizations(
            id=organization_schema.organization_id)
        client.organizations.create(Organization(name=organization_schema.name,
                                                 details=organization_schema.details,
                                                 notes=organization_schema.notes,
                                                 tags=organization_schema.tags,
                                                 domain_names=organization_schema.domain_names,
                                                 external_id=organization_schema.external_id,
                                                 shared_tickets=organization_schema.shared_tickets,
                                                 shared_comments=organization_schema.shared_comments,
                                                 ))
        response = client.organizations.update(organization)
        return response.to_dict()

    def update_user(self, context, user_entity):
        """
        updates existing user 
        context holds the headers 
        user_entity holds the request.body
        """
        client = util.get_zendesk_client(context["headers"])
        user_schema = ZendeskUser(**user_entity)
        user = client.users(id=user_schema.user_id)
        client.users.create(User(details=user_schema.details,
                                 email=user_schema.email,
                                 external_id=user_schema.external_id,
                                 name=user_schema.name,
                                 notes=user_schema.notes,
                                 organization_id=user_schema.organization_id,
                                 phone=user_schema.phone,
                                 role=user_schema.role,
                                 tags=user_schema.tags,
                                 ))
        response = client.users.update(user)
        return response.to_dict()

    def attach_file_to_ticket(self, context, attachment_entity):
        """
        uploads file 
        context holds the headers 
        attachement_entity holds the request.body
        """
        client = util.get_zendesk_client(context["headers"])
        attachment_schema = ZendeskAttachment(**attachment_entity)
        response = client.attachments.upload(
            attachment_schema.comment, target_name=attachment_schema.file, content_type="image/jpeg/png/jpg")
        return response.to_dict()
