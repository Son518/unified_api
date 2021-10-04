
from unified.core.triggers import Triggers
from project_management.trello.entities.card import TrelloCard
from project_management.trello.entities.list import TrelloList
from project_management.trello.entities.comments import TrelloComment
from project_management.trello.entities.checklist import TrelloChecklist
from project_management.trello.entities.labels import TrelloLable
from project_management.trello.entities.member import TrelloMember
from project_management.trello.entities.activity import TrelloActivity


class TrelloTriggers(Triggers):

    def new_card(self, context, payload):
        '''Triggers when a new card is added.'''

        card = TrelloCard(
            card_id=payload['action']['data']['card']['id'],
            name=payload['action']['data']['card']['name'],
            list_id=payload['action']['data']['list']['id'],
            assigned_to=payload['action']['memberCreator']['id']
        )
        return card.__dict__

    def new_list(self, context, payload):
        '''Triggers when a new list is added.'''

        list = TrelloList(
            list_id=payload['action']['data']['list']['id'],
            name=payload['action']['data']['list']['name'],
            board_id=payload['action']['data']['board']['id'],
        )
        return list.__dict__

    def new_comment(self, context, payload):
        '''Triggers when a new comment is added.'''

        comment = TrelloComment(
            comment_id=payload['action']['id'],
            card_id=payload['action']['data']['card']['id'],
            board_id=payload['action']['data']['board']['id'],
            list_id=payload['action']['data']['list']['id'],
            comment_description=payload['action']['data']['text'],
            created_date=payload['action']['date']
        )
        return comment.__dict__

    def card_archived(self, context, payload):
        '''Triggers when a  card is archived is added.'''

        card = TrelloCard(
            card_id=payload['action']['data']['card']['id'],
            closed=payload['action']['data']['card']['closed'],
            name=payload['action']['data']['card']['name'],
            list_id=payload['action']['data']['list']['id'],
            assigned_to=payload['action']['memberCreator']['id']
        )
        return card.__dict__

    def card_due(self, context, payload):
        '''Triggers at a specified time before a card is due.'''

        card = TrelloCard(
            card_id=payload['action']['data']['card']['id'],
            name=payload['action']['data']['card']['name'],
            list_id=payload['action']['data']['list']['id'],
            assigned_to=payload['action']['memberCreator']['id'],
            due_date=payload['action']['data']['card']['due']
        )
        
        return card.__dict__

    def card_updated(self, context, payload):
        '''Triggers when a Card is updated in Trello.'''

        card = TrelloCard(
            card_id=payload['action']['data']['card']['id'],
            name=payload['action']['data']['card']['name'],
            list_id=payload['action']['data']['list']['id'],
            assigned_to=payload['action']['memberCreator']['id']
        )
        return card.__dict__

    def new_checklist(self, context, payload):
        '''Triggers when a new checklist is created in Trello.'''

        cheklist = TrelloChecklist(
            checklist_id=payload['action']['data']['checklist']['id'],
            name=payload['action']['data']['checklist']['name'],
            card_id=payload['action']['data']['card']['id'],
            board_id=payload['action']['data']['board']['id'],
        )
        return cheklist.__dict__

    def new_label(self, context, payload):
        '''Triggers when a new label is created in Trello.'''

        label = TrelloLable(
            label_id=payload['action']['data']['label']['id'],
            name=payload['action']['data']['label']['name'],
            board_id=payload['action']['data']['board']['id'],
            color=payload['action']['data']['label']['color']
        )
        return label.__dict__

    def new_label_added_to_card(self, context, payload):
        '''Triggers when a  label is added to card in Trello.'''

        label = TrelloLable(
            label_id=payload['action']['data']['label']['id'],
            name=payload['action']['data']['label']['name'],
            board_id=payload['action']['data']['board']['id'],
            card_id=payload['action']['data']['card']['id'],
            color=payload['action']['data']['label']['color']
        )
        return label.__dict__

    def card_moved_to_list(self, context, payload):
        '''Triggers when a Card is moved to a List in Trello, inside the same Board.'''

        card = TrelloCard(
            card_id=payload['action']['data']['card']['id'],
            name=payload['action']['data']['card']['name'],
            list_id=payload['action']['data']['listAfter']['id'],
            assigned_to=payload['action']['memberCreator']['id']
        )
        return card.__dict__

    def new_member(self, context, payload):
        '''Triggers when this Trello account joins a card.'''

        member = TrelloMember(
            user_id=payload['action']['data']['member']['id'],
            card_id=payload['action']['data']['card']['id'],
            board_id=payload['action']['data']['board']['id'],
            name=payload['action']['data']['member']['name']
        )
        return member.__dict__

    def new_activity(self, context, payload):
        '''Activiy of checklist  or Attachment'''

        activity = TrelloActivity(
            card_id=payload['action']['data']['card']['id'],
            board_id=payload['action']['data']['board']['id'],
            card_name=payload['action']['data']['card']['name'],
            board_name=payload['action']['data']['board']['name'],
            checklist_id=payload['action']['data']['checklist']['id'] if payload.get(
                'action').get('type') == 'createCheckItem' else None,
            checklist_item=payload['action']['data']['checkItem']['id'] if payload.get(
                'action').get('type') == 'createCheckItem' else None,
            attachment_name=payload['action'].get('data').get('attachment').get(
                'name') if payload.get('action').get('type') == 'addAttachmentToCard' else None,
            attachment_url=payload['action']['data'].get('attachment').get(
                'url') if payload.get('action').get('type') == 'addAttachmentToCard' else None
        )
        return activity.__dict__