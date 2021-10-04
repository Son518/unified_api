
from project_management.trello import util
from unified.core.actions import Actions

from project_management.trello.entities.boards import TrelloBoard
from project_management.trello.entities.card import TrelloCard
from project_management.trello.entities.labels import TrelloLable
from project_management.trello.entities.comments import TrelloComment
from project_management.trello.entities.member import TrelloMember

import json


class TrelloActions(Actions):

    def create_board(self, context, payload):
        '''Creates a new board.'''

        headers = context['headers']
        board_entity = TrelloBoard(**payload)
        url = "https://api.trello.com/1/boards"

        bodard_body = {
            "desc": board_entity.description,
            "name": board_entity.name,
            "idOrganization": board_entity.organization_id,
            "prefs_permissionLevel": board_entity.permission_level,
            "prefs_canInvite": board_entity.teammember_joined
        }
        response = util.rest("POST", url, headers, bodard_body)
        
        return (response.text), response.status_code

    def create_card(self, context, payload):
        '''Adds a new card on a specific board and list.'''

        headers = context['headers']
        card_entites = TrelloCard(**payload)
        url = "https://api.trello.com/1/cards"

        card_body = {
            "urlSource": card_entites.attachment_url,
            "idLabels": [card_entites.label_id],
            "desc": card_entites.description,
            "due": card_entites.due_date,
            "idList": card_entites.list_id,
            "idMembers": card_entites.assigned_to,
            "name": card_entites.name
        }
        response = util.rest("POST", url, headers, card_body)
        return response.text, response.status_code

    def update_card(self, context, payload):
        '''Update a card's name, description, due date'''

        headers = context['headers']
        card_entites = TrelloCard(**payload)
        url = f"https://api.trello.com/1/cards/{card_entites.card_id}"

        card_body = {
            "desc": card_entites.description,
            "due": card_entites.due_date,
            "name": card_entites.name
        }
        response = util.rest("PUT", url, headers, card_body)
        return json.dumps(response.text)

    def create_comment(self, context, payload):
        '''Writes a new comment on a specific card.'''

        headers = context['headers']
        comment = TrelloComment(**payload)
        url = f"https://api.trello.com/1/cards/{comment.card_id}/actions/comments"

        comment_body = {
            "text": comment.comment_description,
            "task_id": comment.card_id
        }
        response = util.rest("POST", url, headers, comment_body)
        return json.dumps(response.text), response.status_code

    def create_label(self, context, payload):
        '''Adds a new label on a specific board.'''

        headers = context['headers']

        label = TrelloLable(**payload)

        url = f'https://api.trello.com/1/boards/{label.board_id}/labels'

        label_body = {
            "name": label.name,
            "color": label.color
        }

        response = util.rest("POST", url, headers, label_body)
        return response.text, response.status_code

    def add_label_to_card(self, context, payload):
        '''Adds an existing label to a specific card.'''

        headers = context['headers']
        label = TrelloLable(**payload)

        url = f'https://api.trello.com/1/cards/{label.card_id}/idLabels'

        label_body = {
            "value": label.label_id
        }

        response = util.rest("POST", url, headers, label_body)
        return response.text, response.status_code

    def add_members_to_card(self, context, payload):
        '''Adds one or more members to a specific card.'''

        headers = context['headers']
        members = TrelloMember(**payload)

        url = f'https://trello.com/1/cards/{members.card_id}/idMembers'

        member_body = {
            "value": members.user_id
        }

        response = util.rest("POST", url, headers, member_body)
        return response.text, response.status_code

    def move_card_to_list(self, context, payload):
        '''Moves a specific card to a list on a specific board.'''

        headers = context['headers']

        card = TrelloCard(**payload)

        url = f'https://trello.com/1/cards/{card.card_id}'

        card_body = {
            "idList": card.list_id
        }

        response = util.rest("PUT", url, headers, card_body)

        return response.text, response.status_code

    def add_attachment_to_card(self, context, payload):
        '''Adds one or more attachments to a specific card.'''

        headers = context['headers']
        card = TrelloCard(**payload)

        url = f'https://trello.com/1/cards/{card.card_id}/attachments'

        card_body = {
            "url": card.attachment_url,
            "name": card.attachment_name
        }

        response = util.rest("POST", url, headers, card_body)

        return response.text, response.status_code
