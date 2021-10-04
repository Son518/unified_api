import string
from unified.core.actions import Actions
from spreadsheets.google_sheets import util


class GooglesheetsActions(Actions):

    @staticmethod
    def get_last_column_index(response, worksheet_id):
        """ utility function for parsing last column index for appending """

        sheets = response.get('sheets') or response.get(
            'updatedSpreadsheet').get('sheets')
        if sheets:
            for sheet in sheets:
                if sheet['properties']['sheetId'] == int(worksheet_id):
                    return sheet['properties']['gridProperties']['columnCount']
        else:
            return 0

    @staticmethod
    def get_last_row_index(response, worksheet_id):
        """ utility function for parsing last row index for appending """

        sheets = response.get('sheets') or response.get(
            'updatedSpreadsheet').get('sheets')
        if sheets:
            for sheet in sheets:
                if sheet['properties']['sheetId'] == int(worksheet_id):
                    return sheet['properties']['gridProperties']['rowCount']
        else:
            return 0

    @staticmethod
    def get_range(response, worksheet_id, row, count):
        """ utility function for getting range based on counts """

        sheets = response.get('sheets') or response.get(
            'updatedSpreadsheet').get('sheets')
        if sheets:
            for sheet in sheets:
                sheet_prop = sheet['properties']
                if sheet_prop['sheetId'] == int(worksheet_id):
                    last_column = sheet_prop['gridProperties']['columnCount'] - 1
                    letter = string.ascii_uppercase[last_column]
                    range_str = sheet_prop['title'] + f"!A{row}:" \
                        f"{letter}{int(row) + count - 1}"
                    return range_str

        return None

    def create_spreadsheet(self, context, payload):
        """ Create a blank spreadsheet or duplicate an existing spreadsheet. """

        token = util.get_access_token(context)
        url = util.get_url()
        data = {
            "properties": {
                "title": payload['title']
            }
        }
        resp = util.rest("POST", url, token, data)

        if payload.get('spreadsheet_to_copy'):
            body = {
                "destinationSpreadsheetId": resp['spreadsheetId']
            }
            spreadsheet_id = payload['spreadsheet_to_copy']
            resp = util.rest("GET", url + f"/{spreadsheet_id}", token)
            sheets = resp['sheets']

            for sheet in sheets:
                sheet_id = sheet['properties']['sheetId']
                url = util.get_url() + \
                    f"/{spreadsheet_id}/sheets/{sheet_id}:copyTo"
                resp = util.rest("POST", url, token, body)

            data = {
                "requests": [
                    {
                        "deleteSheet": {
                            "sheetId": "0"
                        }
                    }
                ]
            }
            url = util.get_url() + \
                f"/{body['destinationSpreadsheetId']}:batchUpdate"
            resp = util.rest("POST", url, token, data)
            url = util.get_url() + f"/{body['destinationSpreadsheetId']}"
            resp = util.rest("GET", url, token)

        return resp

    def copy_worksheet(self, context, payload):
        """ Create a new worksheet by copying an existing worksheet """

        token = util.get_access_token(context)
        url = util.get_url() + f"/{payload['spreadsheet_id']}/sheets/" \
            f"{payload['worksheet_id']}:copyTo"
        data = {
            "destinationSpreadsheetId": payload['copy_to_spreadsheet_id']
        }
        resp = util.rest("POST", url, token, data)

        return resp

    def create_worksheet(self, context, payload):
        """ Create a blank worksheet with a title. Optionally, provide headers. """

        token = util.get_access_token(context)
        url = util.get_url() + f"/{payload['spreadsheet_id']}:batchUpdate"
        data = {
            "requests": [
                {
                    "addSheet": {
                        "properties": {
                            "title": payload['title']
                        }
                    }
                }
            ]
        }

        resp = util.rest("POST", url, token, data)

        return resp

    def create_spreadsheet_row(self, context, payload):
        """ Create a new row in a specific spreadsheet """

        token = util.get_access_token(context)
        spreadsheet_id = payload['spreadsheet_id']
        worksheet_id = payload['worksheet_id']
        url = util.get_url() + f"/{spreadsheet_id}"
        response = util.rest("GET", url, token)
        last_row = self.get_last_row_index(response, worksheet_id)
        range = self.get_range(response, worksheet_id, 1, last_row)
        values = util.rest(
            "GET", url + f"/values/{range}", token)['values']
        count = len(values)
        url = util.get_url() + f"/{spreadsheet_id}:batchUpdate"
        data = {
            "includeSpreadsheetInResponse": True
        }
        pasted_data = payload.copy()
        del pasted_data['spreadsheet_id']
        del pasted_data['worksheet_id']
        values = list(pasted_data.values())
        data['requests'] = [
            {
                "pasteData": {
                    "data": ",".join(values),
                    "type": "PASTE_NORMAL",
                    "delimiter": ",",
                    "coordinate": {
                        "sheetId": payload['worksheet_id'],
                        "rowIndex": count
                    }
                }
            }
        ]

        resp = util.rest("POST", url, token, data)

        return resp

    def create_spreadsheet_column(self, context, payload):
        """ Create a new column in a specific spreadsheet. """

        token = util.get_access_token(context)
        url = util.get_url() + f"/{payload['spreadsheet_id']}:batchUpdate"
        data = {
            "includeSpreadsheetInResponse": True
        }
        index = payload.get('index')

        if not index:
            data['requests'] = [
                {
                    "appendDimension": {
                        "sheetId": payload['worksheet_id'],
                        "dimension": "COLUMNS",
                        "length": 1
                    }
                }
            ]
            resp = util.rest("POST", url, token, data)
            index = str(self.get_last_column_index(
                resp, payload['worksheet_id']) - 1)

        data['requests'] = [
            {
                "insertRange": {
                    "range": {
                        "sheetId": payload['worksheet_id'],
                        "startColumnIndex": index,
                        "endColumnIndex": int(index) + 1
                    },
                    "shiftDimension": "COLUMNS"
                }
            },
            {
                "pasteData": {
                    "data": payload['name'],
                    "type": "PASTE_NORMAL",
                    "delimiter": ",",
                    "coordinate": {
                        "sheetId": payload['worksheet_id'],
                        "columnIndex": index
                    }
                }
            }
        ]

        resp = util.rest("POST", url, token, data)

        return resp

    def delete_spreadsheet_row(self, context, payload):
        """ Deletes a row in a specific spreadsheet. """

        token = util.get_access_token(context)
        url = util.get_url() + f"/{payload['spreadsheet_id']}"
        resp = util.rest("GET", url, token)
        index = payload['row']
        delete_range = self.get_range(resp, payload['worksheet_id'], index, 1)
        url += f"/values/{delete_range}:clear"
        resp = util.rest("POST", url, token)

        return resp

    def update_spreadsheet_row(self, context, payload):
        """ Updates a row in a specific spreadsheet. """

        if len(payload) == 3:
            return self.delete_spreadsheet_row(context, payload)
        else:
            token = util.get_access_token(context)
            url = util.get_url() + \
                f"/{payload['spreadsheet_id']}/values:batchUpdate"
            data = {
                "includeValuesInResponse": True
            }
            index = payload['row']
            resp = util.rest("GET", url[:-19], token)
            update_range = self.get_range(
                resp, payload['worksheet_id'], index, 2)
            pasted_data = payload.copy()
            del pasted_data['spreadsheet_id']
            del pasted_data['worksheet_id']
            del pasted_data['row']
            keys = [value.replace(".", ". ").replace("_", " ").title()
                    for value in pasted_data.keys()]
            values = list(pasted_data.values())
            data['valueInputOption'] = "USER_ENTERED"
            data['data'] = [
                {
                    "range": update_range,
                    "majorDimension": "ROWS",
                    "values": [
                        keys,
                        values
                    ]
                }
            ]

            resp = util.rest("POST", url, token, data)

            return resp
