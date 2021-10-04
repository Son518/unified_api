from dataclasses import dataclass
from marketing_automation.getresponse import util


@dataclass
class GetresponseNewsletter():

    name: str = None
    subject: str = None
    list_id: str = None
    from_field: str = None
    content_html: str = None
    flags: str = None
    content_plain: str = None
    type: str = None
    contact_id: str = None
    send_on: str = None


    def __post_init__(self):
        self.send_on_epoch()

    def send_on_epoch(self):
        if not(self.send_on is None or "-" in self.send_on):
            format = "%Y-%m-%dT%H:%M:%S+00:00"
            self.send_on = util.epoch_to_format(
                format, self.send_on)