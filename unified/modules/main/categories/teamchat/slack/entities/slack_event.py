from dataclasses import dataclass


@dataclass
class SlackEvent:

    event_id: str = None
    bot_id: str = None
    bot_profile: dict = None
    client_msg_id: str = None
    type: str = None
    text: str = None
    ts: str = None
    team: str = None
    blocks: list = None
    channel: str = None
    channel_id: str = None
    channel_type: str = None
    event_ts: str = None
    subtype: str = None
    name: str = None
    value: str = None
    file_id: str = None
    user_id: str = None
    user: str = None
    file: dict = None
    item: dict = None
    item_user: str = None
    pin_count: int = 0
    pinned_info: dict = None
    reaction: str = None

