from email_newsletters.entities.subscriber import Subscriber
from dataclasses import dataclass
from email_newsletters import util


@dataclass
class MalierliteSubscriber(Subscriber):

    company: str = None
    group_id: str = None
    group_name: str = None
    subscriber_group_id: str = None
    date_created: str = None
    date_updated: str = None
    date_unsubscribe: str = None
    type: str = None
    send_autoresponder: str = None
    Resubscribe: str = None
    country: str = None
    subscriber_group: str = None
    city: str = None
    phone: str = None
    state: str = None
    pin_code: str = None
    fields: list = None
    

    def __post_init__(self):
        self.date_unsubscribe_epoch()
        self.date_created_epoch()


    def date_unsubscribe_epoch(self):
        if self.date_unsubscribe is None or "-" in self.date_unsubscribe:
            self.date_unsubscribe = self.date_unsubscribe
        else:
            format = "%Y-%m-%d"
            self.date_unsubscribe = util.epoch_to_format(
                format, self.date_unsubscribe).replace("-", "")


    def date_created_epoch(self):
        if self.date_created is None or "-" in self.date_created:
            self.date_created = self.date_created
        else:
            format = "%Y-%m-%d"
            self.date_created = util.epoch_to_format(
                format, self.date_created).replace("-", "")

    def date_update_epoch(self):
        if self.date_updated is None or "-" in self.date_updated:
            self.date_updated = self.date_updated
        else:
            format = "%Y-%m-%d"
            self.date_updated = util.epoch_to_format(
                format, self.date_updated).replace("-", "")