from teamchat.slack import util
from unified.core.actions import Actions
from teamchat.slack.entities.slack_reminder import SlackReminder
from teamchat.slack.entities.slack_message import SlackMessage
import json


class SlackActions(Actions):

    def create_channel(self, context, payload):
        """ Creates a new channel. """

        token = util.get_access_token(context['headers'])
        url = util.get_url() + "conversations.create"
        data = {
            "name": str.replace(payload['channel_name'], " ", "_")
        }
        response = util.rest("POST", url, token, data)

        if response.status_code > 400:
            raise Exception("Error: ", response.text)

        return json.loads(response.text)

    def add_reminder(self, context, payload):
        """ Adds a reminder for yourself or a teammate,
        just like the /remind slash command. """

        token = util.get_access_token(context['headers'], "user")
        url = util.get_url() + "reminders.add"
        reminder = SlackReminder(**payload)
        data = {
            "text": reminder.text,
            "time": reminder.remind_when,
        }
        if reminder.team_id: data["team_id"] = reminder.team_id
        if reminder.remind_who: data["user"] = reminder.remind_who
        response = util.rest("POST", url, token, data)

        if response.status_code > 400:
            raise Exception("Error: ", response.text)

        return json.loads(response.text)

    def send_channel_message(self, context, payload):
        """ Post a new message to a specific #channel you choose.
        Can also schedule a message for later. """

        token = util.get_access_token(context['headers'])
        message = SlackMessage(**payload)
        data = {
            "text": message.message_text,
            "unfurl_links": message.auto_expand_links,
            "link_names": message.link_usernames_and_channel_names,
            "reply_broadcast": message.broadcast_to_channel,
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "plain_text",
                        "text": message.message_text
                    }
                }
            ]
        }

        if message.channel_id:
            data['channel'] = message.channel_id
        elif message.user_id:
            data['channel'] = message.user_id
        else:
            data['channel'] = message.to_username

        if message.attach_image_by_url:
            url = message.attach_image_by_url
            data["blocks"].append(
                {
                    "type": "image",
                    "image_url": url,
                    "alt_text": url
                }
            )

        if message.file:
            data["blocks"].append(
                {
                    "type": "file",
                    "external_id": message.file,
                    "source": "remote"
                }
            )

        if message.thread:
            data["thread_ts"] = message.thread

        if not message.send_as_a_bot:
            data["as_user"] = True
        else:
            data["username"] = message.bot_name
            data["icon_url"] = message.bot_icon

        if message.schedule_at:
            url = util.get_url() + "chat.scheduleMessage"
            data["post_at"] = message.schedule_at
        else:
            url = util.get_url() + "chat.postMessage"

        response = util.rest("POST", url, token, data)

        if response.status_code > 400:
            raise Exception("Error: ", response.text)

        return json.loads(response.text)

    def send_direct_message(self, context, payload):
        """ Send a direct message to a user or yourself. """

        return self.send_channel_message(context, payload)

    def invite_user_to_channel(self, context, payload):
        """ Invite an existing User to an existing Channel.
        You must be a member of the channel to invite someone to it. """

        token = util.get_access_token(context['headers'])
        url = util.get_url() + "conversations.invite"
        data = {
            "channel": payload['channel_id'],
            "users": payload['user_id']
        }
        response = util.rest("POST", url, token, data)

        if response.status_code > 400:
            raise Exception("Error: ", response.text)

        return json.loads(response.text)

    def send_private_channel_message(self, context, payload):
        """ Post a new message to a private channel you choose.
        Can also schedule a message for later. """

        return self.send_channel_message(context, payload)

    def set_channel_topic(self, context, payload):
        """ Sets the topic on a selected channel. """

        token = util.get_access_token(context['headers'])
        url = util.get_url() + "conversations.setTopic"
        data = {
            "channel": payload['channel_id'],
            "topic": payload['topic']
        }
        response = util.rest("POST", url, token, data)

        if response.status_code > 400:
            raise Exception("Error: ", response.text)

        return json.loads(response.text)

    def update_profile(self, context, payload):
        """ Update basic profile fields such as name or title """

        token = util.get_access_token(context['headers'], type="user")
        url = util.get_url() + "users.profile.set"
        profile = payload
        # user_id = profile.pop('user')
        data = {
            "user": profile.pop('user_id'),
            "profile": profile
        }
        response = util.rest("POST", url, token, data)

        if response.status_code > 400:
            raise Exception("Error: ", response.text)

        return json.loads(response.text)

    def set_status(self, context, payload):
        """ Sets your status to the given text and emoji. """

        token = util.get_access_token(context['headers'], type="user")
        url = util.get_url() + "users.profile.set"
        data = {
            "profile": payload
        }
        response = util.rest("POST", url, token, data)

        if response.status_code > 400:
            raise Exception("Error: ", response.text)

        return json.loads(response.text)
