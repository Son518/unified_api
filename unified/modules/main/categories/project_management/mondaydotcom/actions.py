import monday
import json
import requests
from flask import request, Response
from unified.core.actions import Actions
from project_management.mondaydotcom.entities.monday_item import MondaydotcomItem
from project_management.mondaydotcom.entities.monday_column import MondaydotcomColumn
from project_management.mondaydotcom.entities.monday_updateitem import MondaydotcomUpdateItem
from project_management.mondaydotcom.entities.monday_group import MondaydotcomGroup
from project_management.mondaydotcom.entities.monday_board import MondaydotcomBoard
from project_management.mondaydotcom import util


class MondaydotcomActions(Actions):

    def create_board(self, context, board_entities):
        ''' creates board '''

        board_schema = MondaydotcomBoard(**board_entities)
        query = 'mutation {create_board (board_name: "%s", board_kind: %s) {id}}' % (
            board_schema.board_name, board_schema.board_kind)
        headers = context["headers"]
        response = util.rest("POST", headers, query)

        return json.loads(response.text)

    def create_column(self, context, column_entity):
        ''' creates column''' 

        column_schema = MondaydotcomColumn(**column_entity)

        query = 'mutation{create_column (board_id: %s,title: %s,column_type: %s) {id}}' % (
            column_schema.board_id, column_schema.title, column_schema.type)
        headers = context["headers"]
        response = util.rest("POST", headers, query)

        return json.loads(response.text)

    def create_group(self, context, group_entity):
        ''' create group '''

        monday_client = monday.MondayClient(
            context["headers"]["access_token"])
        group_schema = MondaydotcomGroup(**group_entity)
        result = monday_client.groups.create_group(
            group_schema.board_id, group_schema.name)

        return result

    def create_item(self,   context, item_entity):
        ''' creates item '''

        monday_client = monday.MondayClient(
            context["headers"]["access_token"])
        item_schema = MondaydotcomItem(**item_entity)
        result = monday_client.items.create_item(item_schema.board_id, item_schema.group_id,
                                                 item_schema.name, item_schema.column_values, item_schema.create_labels_if_missing)
        return result

    def update_item_column_value(self, context, item_entity):
        ''' updates item column value'''

        item_schema = MondaydotcomUpdateItem(**item_entity)
        query = 'mutation{change_simple_column_value (board_id: %s,item_id: %s,column_id: %s,value: "%s") {id}}' % (
            item_schema.board_id, item_schema.item_id, item_schema.column_id, item_schema.new_value)
        headers = context["headers"]
        response = util.rest("POST", headers, query)

        return json.loads(response.text)

    def update_item_date_column_value(self, context, item_entity):
        ''' updates item date column value'''

        monday_client = monday.MondayClient(
            context["headers"]["access_token"])
        item_schema = MondaydotcomUpdateItem(**item_entity)
        item_data = {'date': item_schema.new_date_value,
                     'time': item_schema.new_time_value}
        response = monday_client.items.change_item_value(
            item_schema.board_id, item_schema.item_id, item_schema.column_id, item_data)
        
        #if dropdown column not created number column will be created and gets updated    
        if "error_code" in response:
            query = 'mutation{create_column (board_id: %s,title: %s,column_type: %s) {id}}' % (
                item_schema.board_id, "Date", "date")
            headers = context["headers"]
            result = json.loads(util.rest("POST", headers, query).text)
            response = monday_client.items.change_item_value(
                item_schema.board_id, item_schema.item_id, result["data"]["create_column"]["id"], item_data)

        return response

    def update_item_dropdown_column_value(self, context, item_entity):
        ''' updates item dropdown column value'''

        monday_client = monday.MondayClient(
            context["headers"]["access_token"])
        item_schema = MondaydotcomUpdateItem(**item_entity)
        dropdown_data = {"ids": [item_schema.ids]}
        response = monday_client.items.change_item_value(
            item_schema.board_id, item_schema.item_id, item_schema.column_id, dropdown_data)

        #if dropdown column not created dropdown column will be created and gets updated
        if "error_code" in response:
            query = 'mutation{create_column (board_id: %s,title: %s,column_type: %s) {id}}' % (
                item_schema.board_id, "Dropdown", "dropdown")
            headers = context["headers"]
            result = json.loads(util.rest("POST", headers, query).text)
            response = monday_client.items.change_item_value(
                item_schema.board_id, item_schema.item_id, result["data"]["create_column"]["id"], dropdown_data)

        return response

    def update_item_email_column_value(self, context, item_entity):
        ''' updates item email column value'''

        monday_client = monday.MondayClient(
            context["headers"]["access_token"])
        item_schema = MondaydotcomUpdateItem(**item_entity)
        email_data = {'email': item_schema.email,
                      'text': item_schema.email_label}
        response = monday_client.items.change_item_value(
            item_schema.board_id, item_schema.item_id, item_schema.column_id, email_data)

        #if dropdown column not created email column will be created and gets updated
        if "error_code" in response:
            query = 'mutation{create_column (board_id: %s,title: %s,column_type: %s) {id}}' % (
                item_schema.board_id, "Email", "email")
            headers = context["headers"]
            result = json.loads(util.rest("POST", headers, query).text)
            response = monday_client.items.change_item_value(
                item_schema.board_id, item_schema.item_id, result["data"]["create_column"]["id"], email_data)

        return response

    def update_item_status_column_value(self, context, item_entity):
        ''' updates item status column value'''

        monday_client = monday.MondayClient(
            context["headers"]["access_token"])
        item_schema = MondaydotcomUpdateItem(**item_entity)
        status_data = {'index': item_schema.index_value}
        response = monday_client.items.change_item_value(
            item_schema.board_id, item_schema.item_id, item_schema.column_id, status_data)

        #if dropdown column not created status column will be created and gets updated
        if "error_code" in response:
            query = 'mutation{create_column (board_id: %s,title: %s,column_type: %s) {id}}' % (
                item_schema.board_id, "status", "status")
            headers = context["headers"]
            result = json.loads(util.rest("POST", headers, query).text)
            response = monday_client.items.change_item_value(
                item_schema.board_id, item_schema.item_id, result["data"]["create_column"]["id"], status_data)

        return response

    def update_item_number_column_value(self, context, item_entity):
        ''' updates item number column value'''

        monday_client = monday.MondayClient(
            context["headers"]["access_token"])
        item_schema = MondaydotcomUpdateItem(**item_entity)
        response = monday_client.items.change_item_value(
            item_schema.board_id, item_schema.item_id, item_schema.column_id, item_schema.new_value)

        #if dropdown column not created number column will be created and gets updated    
        if "error_code" in response:
            query = 'mutation{create_column (board_id: %s,title: %s,column_type: %s) {id}}' % (
                item_schema.board_id, "Number", "number")
            headers = context["headers"]
            result = json.loads(util.rest("POST", headers, query).text)
            response = monday_client.items.change_item_value(
                item_schema.board_id, item_schema.item_id, result["data"]["create_column"]["id"], text_data)

        return response

    def update_item_people_column_value(self, context, item_entity):
        ''' updates item people column value'''

        monday_client = monday.MondayClient(
            context["headers"]["access_token"])
        item_schema = MondaydotcomUpdateItem(**item_entity)
        person_data = {'personsAndTeams': [{'id':
                                            item_schema.creator_id, 'kind': 'person'}]}
        response = monday_client.items.change_item_value(
            item_schema.board_id, item_schema.item_id, item_schema.column_id, person_data)

        return response

    def update_item_name(self, context, item_entity):
        ''' updates item name'''

        monday_client = monday.MondayClient(
            context["headers"]["access_token"])
        item_schema = MondaydotcomUpdateItem(**item_entity)
        response = monday_client.updates.create_update(
            item_schema.item_id, item_schema.new_item_new_value)

        return response

    def update_item_text_column_value(self, context, item_entity):
        ''' updates item text column value'''

        monday_client = monday.MondayClient(
            context["headers"]["access_token"])
        item_schema = MondaydotcomUpdateItem(**item_entity)
        text_data = {'text': item_schema.new_text_value}
        response = monday_client.items.change_item_value(
            item_schema.board_id, item_schema.item_id, item_schema.column_id, text_data)

        if "error_code" in response:
            query = 'mutation{create_column (board_id: %s,title: %s,column_type: %s) {id}}' % (
                item_schema.board_id, "Text", "text")
            headers = context["headers"]
            result = json.loads(util.rest("POST", headers, query).text)
            response = monday_client.items.change_item_value(
                item_schema.board_id, item_schema.item_id, result["data"]["create_column"]["id"], text_data)

        return response

    def update_item_phone_column_value(self, context, item_entity):
        ''' updates item phone column value'''

        monday_client = monday.MondayClient(
            context["headers"]["access_token"])
        item_schema = MondaydotcomUpdateItem(**item_entity)
        phone_data = {'phone_number': item_schema.phone_number,
                      'country_flag': item_schema.country_flag}
        response = monday_client.items.change_item_value(
            item_schema.board_id, item_schema.item_id, item_schema.column_id, phone_data)
        

        if "error_code" in response:
            query = 'mutation{create_column (board_id: %s,title: %s,column_type: %s) {id}}' % (
                item_schema.board_id, "Phone", "phone")
            headers = context["headers"]
            result = json.loads(util.rest("POST", headers, query).text)
            response = monday_client.items.change_item_value(
                item_schema.board_id, item_schema.item_id, result["data"]["create_column"]["id"], phone_data)

        return response

