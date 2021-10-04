from unified.core.triggers import Triggers
from spreadsheets.smartsheet.api import SmartsheetApi
from spreadsheets.smartsheet import util


class SmartsheetTriggers(Triggers):
    def new_row(self, context, payload):
        '''Trigger when new row is created in sheet'''
        
        # Handshake
        if resp := util.check_handshake():
            return resp,200

        params = {}
        events = payload['events']
        params['row_id'] = events[-1].get('rowId')
        params['sheet_id'] = payload['scopeObjectId']
        return SmartsheetApi().row(context, params)

    def updated_row(self, context, payload):
        '''Trigger when a row is updated '''

        # Handshake
        if resp := util.check_handshake():
            return resp,200

        return self.new_row(context, payload)

    def new_attachment(self, context, payload):
        '''Trigger when new Attachment is added to row '''

        # Handshake
        if resp := util.check_handshake():
            return resp,200

        params = {}
        events = payload['events']
        params['sheet_id'] = payload['scopeObjectId']
        params['attachment_id'] = events[-1].get('id')
        return SmartsheetApi().attachment(context, params)

    def new_comment(self, context, payload):
        '''Trigger when new comment is added to row'''

        # Handshake
        if resp := util.check_handshake():
            return resp,200

        params = {}
        events = payload['events']
        params['sheet_id'] = payload['scopeObjectId']
        params['comment_id'] = events[-1].get('id')
        return SmartsheetApi().comment(context, params)
