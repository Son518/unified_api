from unified.core.actions import Actions
from file_management_storage.onedrive import util
from os import path
import json
import urllib.parse


class OnedriveActions(Actions):

    def upload_file(self, context, payload):
        """ Copies an existing file from another service to Drive. """

        token = util.get_access_token(context['headers'])
        url = util.get_url() + "drive/items/root/children"
        name = path.basename(payload['file_url'])

        if payload.get('name'):
            name = name.replace(name.split('.')[0], payload['name'])

        data = {
            "@microsoft.graph.sourceUrl": payload['file_url'],
            "name": name,
            "file": { }
        }
        headers = {
            "Prefer": "respond-async"
        }
        response = util.rest("POST", url, token, data, headers)

        if response.status_code > 400:
            raise Exception("Error ", response.text)

        url = response.headers["Location"]
        response = util.rest("GET", url)

        return json.loads(response.text)

    def create_new_text_file(self, context, payload):
        """ Create a new file from plain text. """

        token = util.get_access_token(context['headers'])
        name = urllib.parse.quote(payload['name'], safe='')
        url = util.get_url() + f"drive/items/root:/{name}.txt:/content"
        data = payload['file_content']
        response = util.rest("PUT", url, token, data, c_type="text/plain")

        if response.status_code > 400:
            raise Exception("Error ", response.text)

        return json.loads(response.text)

    def create_folder(self, context, payload):
        """ Create a new, empty folder. """

        token = util.get_access_token(context['headers'])
        url = util.get_url() + "drive/root/children"
        data = {
            "name": payload['name'],
            "folder": { },
            "@microsoft.graph.conflictBehavior": "rename"
        }
        response = util.rest("POST", url, token, data)

        if response.status_code > 400:
            raise Exception("Error ", response.text)

        return json.loads(response.text)
