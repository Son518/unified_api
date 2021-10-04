from dataclasses import dataclass


@dataclass
class HelpscoutConversation():

    subject: str = None
    mailbox_id: str = None
    customer_id: str = None
    customer_email: str = None
    from_user_id: str = None
    thread_type: str = None
    text: str = None
    status: str = None
    assigned_user_id: str = None
    tag: str = None
    cc: str = None
    import_only: bool = False
    trigger_auto_reply: bool = False
    user_id: str = None
    conversation_id: str = None
    create_as_draft: bool = False
