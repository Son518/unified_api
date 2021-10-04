from dataclasses import dataclass


@dataclass
class ZohodeskComment:

    comment_id: str = None
    organization_id: str = None
    ticket_id: str = None
    content: str = None
    public: str = None
    attachment_ids: list = None
    content_type: str = None
    commenter: dict = None

    def get_as_data(self, include_none=True):

        data = {
            "id": self.comment_id,
            "content": self.content,
            "isPublic": self.public,
            "attachmentIds": self.attachment_ids,
            "contentType": self.content_type
        }

        if not include_none:
            data = { key : value for key, value in data.items() if value is not None }

        return data