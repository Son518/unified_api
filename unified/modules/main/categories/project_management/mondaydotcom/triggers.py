from flask import request, Response
from project_management.mondaydotcom import util
from project_management.mondaydotcom.entities.monday_board import MondaydotcomBoard
from project_management.mondaydotcom.entities.monday_item import MondaydotcomItem
from unified.core.triggers import Triggers
import requests


class MondaydotcomTriggers(Triggers):

    def column_value_changed_in_board(self, context, payload):
        ''' triggers when column value changed in board'''

        user = MondaydotcomItem(
            board_id=payload["event"]["boardId"]
        )

        return user.__dict__

    def new_item(self, context, payload):
        ''' triggers when new item created'''

        item = MondaydotcomItem(
            id=payload["event"]["userId"],
            board_id=payload["event"]["boardId"],
            name=payload["event"]["pulseName"],
            item_id=payload["event"]["pulseId"],
            group_id=payload["event"]["groupId"],
            group_name=payload["event"]["groupName"],
            column_values=payload["event"]["columnValues"],
            group_color=payload["event"]["groupColor"]
        )

        return item.__dict__

    def new_update_in_board(self, context, payload):
        ''' triggers when new update created in boards'''

        board = MondaydotcomBoard(
            board_id=payload["event"]["boardId"],
            group_id=payload["event"]["groupId"],
            item_id=payload["event"]["pulseId"],
            column_id=payload["event"]["columnId"],
            column_title=payload["event"]["columnTitle"]
        )

        return board.__dict__

    def specific_column_value_changed_in_board(self, context, payload):
        ''' triggers when specific column value changed in board''' 

        board = MondaydotcomBoard(
            board_id=payload["event"]["boardId"],
            group_id=payload["event"]["groupId"],
            item_id=payload["event"]["pulseId"],
            column_id=payload["event"]["columnId"],
            column_title=payload["event"]["columnTitle"]
        )

        return board.__dict__


