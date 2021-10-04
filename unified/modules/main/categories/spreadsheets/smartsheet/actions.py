import json
import requests
from unified.core.actions import Actions
from spreadsheets.smartsheet import util
from spreadsheets.smartsheet.entities.smartsheet_row import SmartsheetRow
from spreadsheets.smartsheet.entities.smartsheet_sheet import SmartsheetSheet
from spreadsheets.smartsheet.entities.smartsheet_sendrow import SmartsheetSendRow
from spreadsheets.smartsheet.entities.smartsheet_copy_row import SmartsheetCopyRow
from spreadsheets.smartsheet.entities.smartsheet_workspace import SmartsheetWorkspace
from spreadsheets.smartsheet.entities.smartsheet_attachment import SmartsmartAttachment
from spreadsheets.smartsheet.entities.smartsheet_copy_folder import SmartsheetCopyFolder
from spreadsheets.smartsheet.entities.smartsheet_copy_workspace import SmartsheetCopyWorkspace


class SmartsheetActions(Actions):

    def create_workspace(self, context, payload):
        '''Creates a Workspace.'''

        api_key = context['headers'].get('api_key')

        if not api_key:
            raise Exception('Provide required api-key in headers')

        url = "workspaces"
        workspace = SmartsheetWorkspace(**payload)
        request_body = {"name": workspace.workspace_name}
        response = util.rest("post", url, api_key, request_body)

        if not response.ok:
            raise Exception('Something went wrong!', response.text,
                            response.status_code)

        return response.text, response.status_code

    def add_discussion_to_row(self, context, payload):
        '''Adds discussion to row.'''

        api_key = context['headers'].get('api_key')

        if not api_key:
            raise Exception('Provide required api-key in headers')

        discussion = SmartsheetRow(**payload)

        url = f'sheets/{discussion.sheet_id}/rows/{discussion.row_id}/discussions'

        request_body = {"comment": {
            "text": discussion.comment}}

        response = util.rest("post", url, api_key, request_body)

        if not response.ok:
            raise Exception('Something went wrong!', response.text,
                            response.status_code)

        return response.text, response.status_code

    def copy_workspace(self, context, payload):
        '''Creates a copy of the specified Workspace.'''

        api_key = context['headers'].get('api_key')

        if not api_key:
            raise Exception('Provide required api-key in headers')

        copy_workspace = SmartsheetCopyWorkspace(**payload)

        url = self.optional_parameters(
            'workspaces', copy_workspace.workspace_id, copy_workspace.what_to_include, copy_workspace.skip_remap)

        request_body = {
            "newName": copy_workspace.new_workspace_name
        }
        response = util.rest("post", url, api_key, request_body)

        if not response.ok:
            raise Exception('Something went wrong!', response.text,
                            response.status_code)

        return response.text, response.status_code

    def copy_folder(self, context, payload):
        '''Copies folder to another destination.'''

        api_key = context['headers'].get('api_key')

        if not api_key:
            raise Exception('Provide required api-key in headers')
        copy_folder = SmartsheetCopyFolder(**payload)

        url = self.optional_parameters(
            "folders", copy_folder.source_folder_id, copy_folder.what_to_include, copy_folder.skip_remap)
        request_body = {
            "destinationType": "folder",
            "destinationId": copy_folder.destination_folder_id,
            "newName": copy_folder.new_folder_name
        }

        response = util.rest("post", url, api_key, request_body)

        if not response.ok:
            raise Exception('Something went wrong!', response.text,
                            response.status_code)

        return response.text, response.status_code

    def copy_row(self, context, payload):
        '''Copies row to another sheet.'''

        api_key = context['headers'].get('api_key')

        if not api_key:
            raise Exception('Provide required api-key in headers')

        copy_row = SmartsheetCopyRow(**payload)
        url = f"sheets/{copy_row.source_sheet_id}/rows/copy"
        request_body = {"rowIds": [copy_row.row_id], "to": {
            "sheetId": copy_row.destination_sheet_id}}

        response = util.rest("post", url, api_key, request_body)

        if not response.ok:
            raise Exception('Something went wrong!', response.text,
                            response.status_code)

        return response.text, response.status_code

    def optional_parameters(self, activity, activity_id, what_to_include=None, skip_remap=None):
        '''includes optional_parameters in url'''

        url = f"{activity}/{activity_id}/copy"
        include_items = None
        skip_remap_items = None

        if what_to_include:
            include_items = f"include={','.join(what_to_include)}"

        if skip_remap:
            skip_remap_items = f"skipRemap={','.join(skip_remap)}"

        # shoudnt append empty values for what_to_include and skip_remap
        
        if (include_items and skip_remap_items):
            return f'{url}?{include_items}&{skip_remap_items}'
        elif include_items:
            return f'{url}?{include_items}'
        elif skip_remap_items:
            return f'{url}?{skip_remap_items}'
        else:
            return url
        


    def move_row(self, context, payload):
        '''Moves row to another sheet.'''

        api_key = context['headers'].get('api_key')

        if not api_key:
            raise Exception('Provide required api-key in headers')

        move_row = SmartsheetCopyRow(**payload)
        url = f"sheets/{move_row.source_sheet_id}/rows/move"
        request_body = {"rowIds": [move_row.row_id], "to": {
            "sheetId": move_row.destination_sheet_id}}

        response = util.rest("post", url, api_key, request_body)

        if not response.ok:
            raise Exception('Something went wrong!', response.text,
                            response.status_code)

        return response.text, response.status_code

    def new_sheet_from_existing_sheet(self, context, payload):
        '''Create a new sheet from an existing sheet.'''

        api_key = context['headers'].get('api_key')

        if not api_key:
            raise Exception('Provide required api-key in headers')

        sheet = SmartsheetSheet(**payload)
        url = f"sheets/{sheet.source_sheet_id}/copy?include=data"
        request_body = {
            "destinationType": "folder",
            "destinationId": sheet.folder_id,
            "newName": sheet.sheet_name
        }

        if sheet.copy_attachments.lower() == 'yes':
            url = f"{url},attachments"

        if sheet.copy_cells.lower() == 'yes':
            url = f"{url},forms,rules,ruleRecipients"

        if sheet.copy_discussions.lower() == 'yes':
            url = f"{url},discussions,cellLinks"

        response = util.rest("post", url, api_key, request_body)

        if not response.ok:
            raise Exception('Something went wrong!', response.text,
                            response.status_code)

        return response.text, response.status_code

    def new_sheet_from_template(self, context, payload):
        '''Create a new sheet from a template.'''

        api_key = context['headers'].get('api_key')

        if not api_key:
            raise Exception('Provide required api-key in headers')

        url = "sheets?include=data"
        sheet = SmartsheetSheet(**payload)

        if sheet.copy_attachments.lower() == 'yes':
            url = f"{url},attachments"

        if sheet.copy_cells.lower() == 'yes':
            url = f"{url},forms,rules,ruleRecipients"

        if sheet.copy_discussions.lower() == 'yes':
            url = f"{url},discussions,cellLinks"

        request_body = {"name": sheet.sheet_name, "fromId": sheet.template_id}
        response = util.rest("post", url, api_key, request_body)

        if not response.ok:
            raise Exception('Something went wrong!', response.text,
                            response.status_code)

        return response.text, response.status_code

    def send_row(self, context, payload):
        '''Send a row via email.'''

        api_key = context['headers'].get('api_key')

        if not api_key:
            raise Exception('Provide required api-key in headers')

        send_row = SmartsheetSendRow(**payload)
        url = f"sheets/{send_row.sheet_id}/rows/emails"
        request_body = {
            "sendTo": [
                {"email": send_row.email_address}
            ],
            "subject": send_row.subject,
            "message": send_row.message,
            "ccMe": (send_row.cc_me.lower() == 'yes'),
            "rowIds": [
                send_row.row_id
            ],
            "includeAttachments": (send_row.include_attachments.lower() == 'yes'),
            "includeDiscussions": (send_row.include_discussions.lower() == 'yes')
        }
        response = util.rest("post", url, api_key, request_body)

        if not response.ok:
            raise Exception('Something went wrong!', response.text,
                            response.status_code)

        return response.text, response.status_code

    def send_sheet(self, context, payload):
        '''Send a sheet via email (as PDF or Excel).'''

        api_key = context['headers'].get('api_key')

        if not api_key:
            raise Exception('Provide required api-key in headers')

        send_row = SmartsheetSendRow(**payload)
        url = f"sheets/{send_row.sheet_id}/emails"
        request_body = {
            "sendTo": [{
                "email": send_row.email_address
            }],
            "subject": send_row.subject,
            "message": send_row.message,
            "ccMe": True if send_row.cc_me == 'yes' else False,
            "format": send_row.format.upper(),
            "formatDetails": {
                "paperSize": send_row.paper_size.upper()
            }
        }

        response = util.rest("post", url, api_key, request_body)

        if not response.ok:
            raise Exception('Something went wrong!', response.text,
                            response.status_code)

        return response.text, response.status_code

    def share_sheet(self, context, payload):
        '''Share a sheet.'''

        api_key = context['headers'].get('api_key')

        if not api_key:
            raise Exception('Provide required api-key in headers')

        send_row = SmartsheetSendRow(**payload)
        url = f"sheets/{send_row.sheet_id}/shares"
        url = f"{url}?sendEmail=true" if send_row.notify_via_email == 'yes' else ''
        request_body = [{"email": send_row.email_address, "accessLevel": send_row.access_level.upper(
        ), "message": send_row.message, "subject": send_row.subject}]

        response = util.rest("post", url, api_key, request_body)

        if not response.ok:
            raise Exception('Something went wrong!', response.text,
                            response.status_code)

        return response.text, response.status_code

    def share_workspace(self, context, payload):
        '''Share a workspace.'''

        api_key = context['headers'].get('api_key')

        if not api_key:
            raise Exception('Provide required api-key in headers')

        send_row = SmartsheetSendRow(**payload)
        url = f"workspaces/{send_row.workspace_id}/shares"
        url = f"{url}?sendEmail=true" if send_row.notify_via_email == 'yes' else ''
        request_body = [{"email": send_row.email_address, "accessLevel": send_row.access_level.upper(
        ), "message": send_row.message, "subject": send_row.subject}]

        response = util.rest("post", url, api_key, request_body)

        if not response.ok:
            raise Exception('Something went wrong!', response.text,
                            response.status_code)

        return response.text, response.status_code

    def add_row_to_sheet(self, context, payload):
        '''Add a row to a sheet.'''

        api_key = context['headers'].get('api_key')

        if not api_key:
            raise Exception('Provide required api-key in headers')

        row = SmartsheetRow(**payload)
        url = f"sheets/{row.sheet_id}/rows"
        cells = []
        if row.cells:
            for cell in row.cells:
                default_value = {
                    'columnId': cell['column_id'],
                    'value': cell['value'],
                    'strict': False
                }
                cells.append(default_value)

        request_body = [{
            "toTop": row.to_top,
            "cells": cells
        }]
        response = util.rest("post", url, api_key, request_body)

        if not response.ok:
            raise Exception('Something went wrong!', response.text,
                            response.status_code)

        return response.text, response.status_code

    def new_row_update(self, context, payload):
        '''Update an existing row with new values. Requires a row ID.'''

        api_key = context['headers'].get('api_key')

        if not api_key:
            raise Exception('Provide required api-key in headers')

        row = SmartsheetRow(**payload)
        url = f"sheets/{row.sheet_id}/rows"
        cells = []
        if row.cells:
            for cell in row.cells:
                default_value = {
                    'columnId': cell['column_id'],
                    'value': cell['value'],
                    'strict': False
                }
                cells.append(default_value)

        request_body = [{
            'id': row.row_id,
            "toTop": row.to_top,
            "cells": cells
        }]
        response = util.rest("PUT", url, api_key, request_body)

        if not response.ok:
            raise Exception('Something went wrong!', response.text,
                            response.status_code)

        return response.text, response.status_code

    def add_attachment_to_row(self, context, payload):
        '''Adds a file attachment to a row.'''

        api_key = context['headers'].get('api_key')

        if not api_key:
            raise Exception('Provide required api-key in headers')
        
        attachment = SmartsmartAttachment(**payload)
        url = f"sheets/{attachment.sheet_id}/rows/{attachment.row_id}/attachments"
        request_body = {
            "name": attachment.name,
            "description": attachment.description,
            "attachmentType": "LINK",
            "url": attachment.attachment_url
        }

        response = util.rest("POST", url, api_key, request_body)

        if not response.ok:
            raise Exception('Something went wrong!', response.text,
                            response.status_code)

        return response.text, response.status_code
