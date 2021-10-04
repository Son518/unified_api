import json
from unified.core.triggers import Triggers
from customer_support.livechat.entities.livechat_ticket import  LivechatTicket

class LivechatTriggers(Triggers):
    
    def new_ticket(self, context, payload):
        ''' triggers when new ticket created'''
        response = payload['ticket']['events'][0]
        group = payload["ticket"]["groups"][0]
        assignee = payload['ticket']['assignee']
        author = response['author']
        requester = payload['ticket']['requester']
        ticket_obj = LivechatTicket(
                                    event_type=payload['event_type'],
                                    token=payload['token'],
                                    license_id=payload['license_id'],
                                    ticket=payload['ticket'],
                                    assignee_id=assignee['id'],
                                    assignee_name=assignee['name'],
                                    author_id=author['id'],
                                    author_name=author['name'],
                                    author_type=author['type'],
                                    date=response['date'],
                                    is_private=response['is_private'],
                                    message=response['message'],
                                    type=response['type'],
                                    source_type=response['source']['type'],
                                    source_url=response['source']['url'],
                                    groups_id=group['id'],
                                    groups_name=group['name'],
                                    groups_inherited=group['inherited'],
                                    id= payload['ticket']['id'],
                                    requester_mail=requester['mail'],
                                    requester_name=requester['name'],
                                    requester_ip=requester['ip'],
                                    status=payload['ticket']['status'],
                                    subject=payload['ticket']['subject'],
                                    tags=payload['ticket']['tags'],
                                    source_type1=payload['ticket']['source']['type'],
                                    source_url1=payload['ticket']['source']['type'],
                                    source_id=payload['ticket']['source']['id']
                                )                          
        return ticket_obj.__dict__