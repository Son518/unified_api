from spreadsheets.google_sheets import util
from spreadsheets.google_sheets.actions import GooglesheetsActions


class GooglesheetsApi:

    @staticmethod
    def get_vertical_range(response, worksheet_id, letter):
        """ utility function for getting vertical range """

        sheets = response.get('sheets') or \
            response.get('updatedSpreadsheet').get('sheets')

        if sheets:
            for sheet in sheets:
                sheet_prop = sheet['properties']
                if sheet_prop['sheetId'] == int(worksheet_id):
                    last_row = sheet_prop['gridProperties']['rowCount']
                    letter = letter.upper()
                    range_str = sheet_prop['title'] + \
                        f"!{letter}1:{letter}{last_row}"
                    return range_str

        return None

    def lookup_spreadsheet_row(self, context, params):
        """ Finds a row by a column and value.
        Returns the entire row if one is found """

        token = util.get_access_token(context)
        url = util.get_url() + f"/{params['spreadsheet_id']}"
        response = util.rest("GET", url, token)  # get the whole spreadsheet
        letter = params['lookup_column_id']

        if letter.find("COL$", 0) != -1:
            letter = letter[4:]

        # get the vertical range values
        range = self.get_vertical_range(
            response, params['worksheet_id'], letter)
        resp = util.rest("GET", url + f"/values/{range}", token)
        values = resp['values']
        row_index = 0
        query = params['lookup_value']

        for index, value in enumerate(values):
            if query in value:
                row_index = int(index) + 1
                break

        #  get the horizontal range values
        range = GooglesheetsActions.get_range(
            response, params['worksheet_id'], row_index, 1)
        resp = util.rest("GET", url + f"/values/{range}", token)

        return resp
