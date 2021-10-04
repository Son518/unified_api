import json
from project_management.trello import util
from project_management.trello.entities.boards import TrelloBoard
from project_management.trello.entities.card import TrelloCard
from project_management.trello.entities.member import TrelloMember
from project_management.trello.entities.labels import TrelloLable
from project_management.trello.entities.comments import TrelloComment
from project_management.trello.entities.attachment import TrelloAttachment
from project_management.entities.project import Project
from project_management.trello.entities.trello_task import TrelloTask


class TrelloApi:
    def board_by_name(self, context, params):
        '''Get List of Boards by Name'''

        url = f"https://trello.com/1/search?query={params['name']}&boards_limit=10&modelTypes=boards&partial=true&board_fields=all"

        headers = context['headers']

        response = util.rest("GET", url, headers)

        boards_list = json.loads(response.text)["boards"]
        boards = []
        for board in boards_list:
            board_obj = TrelloBoard(
                name=board['name'],
                description=board['desc'],
                is_closed=board['closed'],
                id=board['id']
            )
            boards.append(board_obj.__dict__)

        return json.dumps(boards)
    
    def list_of_boards(self, context):
        url = "https://trello.com/1/Members/me?boards=open"

        headers = context['headers']

        response = util.rest("GET", url, headers)

        boards_list = json.loads(response.text)["boards"]
        
        return boards_list
        
    def boards(self, context, params):
        '''Get List of Boards'''
        boards_list = self.list_of_boards(context)
        boards = []
        for board in boards_list:
            board_obj = TrelloBoard(
                name=board['name'],
                is_closed=board['closed'],
                id=board['id']
            )
            boards.append(board_obj.__dict__)

        return json.dumps(boards)

    def list_of_cards(self,context,params):
        if params.get("board_id") or params.get('project_id'):
            board_id = params.get("board_id") or params.get('project_id')
            url = f"https://api.trello.com/1/boards/{board_id}/cards"
        else:
            url = f"https://api.trello.com/1/lists/{params['card_id']}/cards"
        headers = context['headers']

        response = util.rest("GET", url, headers)
        card_list = json.loads(response.text)

        return card_list
        


    def cards(self, context, params):
        '''Get List of cards in board or list'''

        card_list = self.list_of_cards(context, params)
        cards = []
        for card in card_list:
            card_obj = TrelloCard(
                card_id=card['id'],
                description=card['desc'],
                name=card['name'],
                due_date=card['due'],
                label_id=card['labels'],
                list_id=card['idList'],
            )
            cards.append(card_obj.__dict__)

        return json.dumps(cards)

    def user_by_name(self, context, parmas):
        '''user Details by name'''

        url = f"https://trello.com/1/search?query={parmas['name']}&board_fields=closed%2Cid%2CidOrganization%2Cname%2Cprefs%2Curl&boards_limit=8&card_attachments=cover&card_board=true&card_list=true&card_members=true&card_stickers=true&cards_limit=9&cards_page=0&members_limit=8&modelTypes=cards%2Cboards%2Corganizations%2Cmembers&organization_fields=all&organizations_limit=6&partial=true"
        headers = context['headers']
        response = util.rest("GET", url, headers)
        users_list = json.loads(response.text)['members']
        users = []

        for user in users_list:
            user_obj = TrelloMember(
                user_id=user['id'],
                name=user['fullName'],
                confirmed=user['confirmed']
            )
            users.append(user_obj.__dict__)
        return json.dumps(users)

    def labels(self, context, params):
        '''Get list of labels from a board'''

        url = f'https://api.trello.com/1/boards/{params["board_id"]}/labels'

        headers = context['headers']

        labels_list = json.loads((util.rest("GET", url, headers)).text)
        labels = []
        for label in labels_list:
            label_obj = TrelloLable(
                label_id=label['id'],
                name=label['name'],
                color=label['color'],
                board_id=label['idBoard']
            )
            labels.append(label_obj.__dict__)

        return json.dumps(labels)

    def card_comments(self, context, params):
        '''Get list of comments from a card'''
        
        url = f'https://api.trello.com/1/cards/{params["card_id"]}/actions'
        headers = context['headers']
        comment_list = json.loads((util.rest("GET", url, headers)).text)
        comments = []

        for comment in comment_list:
            comment_obj = TrelloComment(
                comment_id=comment['id'],
                card_id=comment['data']['card']['id'],
                board_id=comment['data']['board']['id'],
                list_id=comment['data']['list']['id'],
                comment_description=comment['data']['text'],
                created_date=comment['date']
            )
            comments.append(comment_obj.__dict__)
        return json.dumps(comments)
    
    def card_attachments(self, context, params):
        '''Get list of attachements from a card'''
        
        url = f'https://api.trello.com/1/cards/{params["card_id"]}/attachments'
        headers = context['headers']
        attachment_list = json.loads((util.rest("GET", url, headers)).text)
        attachments = []

        for attachment in attachment_list:
            attachment_obj = TrelloAttachment(
               attachment_id = attachment['id'],
               name=attachment['name'],
               user_id=attachment['idMember'],
               mimetype=attachment['mimeType'],
               attachment_url=attachment['url']
            )
            attachments.append(attachment_obj.__dict__)
        return json.dumps(attachments)
    
    def projects(self,context,params):
        '''Get List of projects or Boards'''

        boards_list = self.list_of_boards(context)
        boards = []
        for board in boards_list:
            board_obj = Project(
                project_name=board['name'],
                id=board['id']
            )
            boards.append(board_obj.__dict__)

        return json.dumps(boards)

    def tasks_by_project_id(self,context,params):

        card_list = self.list_of_cards(context, params)
        cards = []
        for card in card_list:
            card_obj = TrelloTask(
                id=card['id'],
                description=card['desc'],
                name=card['name'],
                due_date=card['due'],
                tasklist_id=card['idList'],
            )
            cards.append(card_obj.__dict__)

        return json.dumps(cards)
    
    def profile(self, context, params):
        url = "https://api.trello.com/1/members/me"
        headers = context['headers']
        response = util.rest("GET", url, headers).json()
        profile = {
            'id':response['id'],
            'email':response['email'],
            'name':response['fullName']
        }
        return profile