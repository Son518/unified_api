import json
import monday
from project_management.mondaydotcom import util
from project_management.mondaydotcom.entities.monday_item import MondaydotcomItem
from project_management.mondaydotcom.entities.monday_board import MondaydotcomBoard
from project_management.mondaydotcom.entities.monday_column import MondaydotcomColumn
from project_management.entities.task import Task


class MondaydotcomAPI():

    def boards(self, context, params):
        ''' gets all boards data '''

        access_token = context["headers"]["access_token"]
        monday_client = monday.MondayClient(access_token)
        boards = monday_client.boards.fetch_boards().get('data').get('boards')
        board_value = []
        for board in boards:
            board_obj = MondaydotcomBoard(id=board["id"],
                                          project_id=board["id"],
                                          name=board["name"],
                                          project_name=board["name"],
                                          board_tags=board["tags"],
                                          groups=board["groups"],
                                          columns=board["columns"]
                                          )
            board_value.append(board_obj.__dict__)

        return json.dumps(board_value)

    def column_values(self, context, params):
        ''' get specified column values'''

        payload = '{items  {column_values {id value }}}'
        headers = context["headers"]
        columns = (json.loads(util.rest("GET", headers, payload).text)).get(
            'data').get('items')

        column_values = []
        for column in columns:
            for column_value in column['column_values']:
                if params["column_id"] == column_value["id"]:
                    column_obj = MondaydotcomColumn(column_id=column_value['id'],
                                                    column_value=column_value['value'])
                    column_values.append(column_obj.__dict__)

        return json.dumps(columns)

    def item_updates(self, context, params):
        ''' gets items updates'''

        update_schema = MondaydotcomItem(**params)
        access_token = context["headers"]["access_token"]
        monday_client = monday.MondayClient(access_token)
        item_updates = monday_client.updates.fetch_updates_for_item(
            update_schema.board_id, update_schema.item_id)

        return item_updates

    def items(self, context, params):
        ''' gets all items from boards'''

        payload = '{items { id name board {id}}}'
        headers = context["headers"]
        items = (json.loads(util.rest("GET", headers, payload).text)).get(
            'data').get('items')
        item_value = []
        for item in items:
            item_obj = MondaydotcomItem(board_id=item["board"]["id"],
                                        item_id=item["id"],
                                        name=item["name"])
            item_value.append(item_obj.__dict__)

        return json.dumps(item_value)


    def verify(self,context,params):
        """
        get call to verify user authenticated information
        """
        payload = 'query { me { name }}'
        headers = context["headers"]
        response = util.rest("GET", headers, payload)
        return response.json()
    
    def profile(self,context,params):
        """
        get call to show user authenticated information
        """
        payload = 'query { me { is_guest created_at name id email}}'
        headers = context["headers"]
        response = util.rest("GET", headers, payload)
        result = (response.json())['data']['me']
        profile = {
            'id':result['id'],
            'name':result['name'],
            'email':result['email']
        }
        return profile
        
    def projects(self,context,params):
        return self.boards(context,params)
    
    def tasks_by_project_id(self,context,params):
        payload = '{boards(ids:[%s]) { id name items {id name}}}'%(params["project_id"])
        headers = context["headers"]
        tasks = json.loads(util.rest("GET", headers, payload).text).get('data').get('boards')
        task_value = []      
        for task in tasks[0]["items"]:
            task_obj = Task(
                project_id=tasks[0]['id'],
                task_id=task['id'],
                name=task['name']
            )
            task_value.append(task_obj.__dict__)              
        return json.dumps(task_value)


