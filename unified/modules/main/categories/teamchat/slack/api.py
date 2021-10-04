import json
from teamchat.slack import util
from teamchat.slack.search import search_user_by


class SlackApi:

    def message(self, context, params):
        """ Finds a messages using the Search feature. """

        token = util.get_access_token(context['headers'], type="user")
        url = util.get_url() + f"search.messages?query={params['search_query']}&" \
                f"sort={params['sort_by']}&sort_dit={params['sort_direction']}"
        response = util.rest("GET", url, token)

        if response.status_code > 400:
            raise Exception("Error: ", response.text)

        res = json.loads(response.text)

        if not res['ok']:
            return res

        msg_lst = json.loads(response.text)['messages']['matches']

        return json.dumps(msg_lst)

    def user_by_email(self, context, params):
        """ Finds a user by matching against their email instead of their username. """

        token = util.get_access_token(context['headers'])
        url = util.get_url() + f"users.lookupByEmail?email={params['email']}"
        response = util.rest("GET", url, token)

        if response.status_code > 400:
            raise Exception("Error: ", response.text)

        res = json.loads(response.text)

        if not res['ok']:
            return res

        return json.dumps(res['user'])

    def user_by_id(self, context, params):
        """ Finds user by provided ID """

        token = util.get_access_token(context['headers'])
        url = util.get_url() + f"users.info?user={params['user_id']}"
        response = util.rest("GET", url, token)
        res = json.loads(response.text)

        if not res['ok']:
            return res

        return json.dumps(res['user'])

    def user_by_name(self, context, params):
        """ Finds a user by matching against their real name instead of their username. """

        return search_user_by("real_name", context['headers'], params['full_name'])

    def user_by_username(self, context, params):
        """ Finds a user by its username """

        return search_user_by("name", context['headers'], params['username'])
