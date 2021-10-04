import json
from transactional_email.postmark.actions import PostmarkActions
from transactional_email.postmark.triggers import PostmarkTriggers
from unified.core.app import App, AuthInfo


class PostmarkApp(App,PostmarkActions,PostmarkTriggers):

    def __init__(self):
        super().__init__(
            name="Postmark",
            description="Postmark helps deliver and track application email.",
            category="transactional_email",
            logo="https://logo.500apps.com/postmark",
            auth_info=None,
            auth_type='oauth2')
