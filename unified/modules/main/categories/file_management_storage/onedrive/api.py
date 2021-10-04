import json
from file_management_storage.onedrive import util
from file_management_storage.onedrive.entities.onedrive_item import OnedriveItem


class OnedriveApi:

    @staticmethod
    def search(token, query):
        """ utility function for running search queries """

        url = util.get_url() + f"drive/root/search(q='{query}')"
        response = util.rest("GET", url, token)

        if response.status_code > 400:
            raise Exception("Error ", response.text)

        return json.loads(response.text), response.status_code

    @staticmethod
    def get_item_data(item):
        """ utility function for getting drive item dict data """

        return OnedriveItem(
            id=item.get('id'),
            name=item.get('name'),
            web_url=item.get('webUrl'),
            created_by=item.get('createdBy')
        ).__dict__

    def file_by_name(self, context, params):
        """ Search for a specific file by name. """

        token = util.get_access_token(context['headers'])
        response, code = OnedriveApi.search(token, params['name'])

        if code == 400:
            return response

        result = []

        for item in response['value']:
            if item.get('file'):
                item_data = self.get_item_data(item)
                result.append(item_data)

        return result

    def folder_by_name(self, context, params):
        """ Search for a specific file by name. """

        token = util.get_access_token(context['headers'])
        response, code = OnedriveApi.search(token, params['name'])

        if code == 400:
            return response

        result = []

        for item in response['value']:
            if item.get('folder'):
                item_data = self.get_item_data(item)
                result.append(item_data)

        return result
