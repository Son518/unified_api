from dataclasses import dataclass


@dataclass
class SlackMessage():

    channel_id: str = None
    user_id: str = None
    to_username: str = None
    message_text: str = None
    send_multi_message: bool = False
    send_as_a_bot: bool = True
    bot_name: str = None
    bot_icon: str = None
    include_a_link_to_this_zap: bool = False
    attach_image_by_url: str = None
    auto_expand_links: bool = False
    link_usernames_and_channel_names: bool = False
    schedule_at: str = None
    file: str = None
    thread: str = None
    broadcast_to_channel: bool = False
