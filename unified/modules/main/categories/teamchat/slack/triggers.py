import json
from teamchat.slack import util
from unified.core.triggers import Triggers
from teamchat.slack.entities.slack_event import SlackEvent


class SlackTriggers(Triggers):

    def event(self, event_data):
        """ utility function for returning event object as dict """

        return SlackEvent(**event_data).__dict__

    def new_channel(self, context, payload):
        """ Triggers whenever a new #channel is created. """

        token = util.get_access_token(context['headers'])
        channel_id = payload['event']['channel']['id']
        url = util.get_url() + f"conversations.info?channel={channel_id}"
        response = util.rest("GET", url, token)
        res = json.loads(response.text)

        if not res['ok']:
            return res

        return json.dumps(res['channel'])

    def new_message(self, context, payload):
        """ Triggers when a new message is posted to any channel. """

        return self.event(payload['event'])

    def new_saved_message(self, context, payload):
        """ Triggers when you save a message. """

        return self.event(payload['event'])

    def new_team_custom_emoji(self, context, payload):
        """ Triggers when a custom emoji has been added to a team. """

        return self.event(payload['event'])

    def new_file(self, context, payload):
        """ Triggers when a new file is uploaded to your workspace. """

        return self.event(payload['event'])

    def new_mention(self, context, payload):
        """ Triggers when an app word is mentioned in a channel. """

        return self.event(payload['event'])

    def new_reaction(self, context, payload):
        """ Triggers when a reaction (aka reactji)
        is added to a message in a public #channel. """

        return self.event(payload['event'])

    def new_user(self, context, payload):
        """ Triggers when a new user is created / first joins your org. """

        token = util.get_access_token(context['headers'])
        user_id = payload['event']['user']['id']
        url = util.get_url() + f"users.info?user={user_id}"
        response = util.rest("GET", url, token)
        res = json.loads(response.text)

        if not res['ok']:
            return res

        return json.dumps(res['user'])
