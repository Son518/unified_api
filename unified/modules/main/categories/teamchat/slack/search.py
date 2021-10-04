import json
from teamchat.slack import util


def search_user_by(field, headers, param):
    """ Searching function of a user by specific field """

    token = util.get_access_token(headers)
    url = util.get_url() + "users.list"
    response = util.rest("GET", url, token)

    if response.status_code > 400:
        raise Exception("Error: ", response.text)

    res = json.loads(response.text)

    if not res['ok']:
        return res

    usr_lst = res['members']
    user_id = ""

    for user in usr_lst:
        if user[field] == param:
            user_id = user['id']
            break

    url = util.get_url() + f"users.info?user={user_id}"
    response = util.rest("GET", url, token)
    res = json.loads(response.text)

    if not res['ok']:
        return res

    return json.dumps(res['user'])
