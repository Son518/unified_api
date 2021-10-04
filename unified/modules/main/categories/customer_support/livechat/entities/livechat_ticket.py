from dataclasses import dataclass
from customer_support.livechat import util

@dataclass
class LivechatTicket():

	event_type: str = None,
	token: str = None,
	license_id: str = None,
	ticket: str = None,
	assignee_id: str = None,
	assignee_name: str = None,
	events: str = None,
	author_id: str = None,
	author_name: str = None,
	author_type: str = None,
	date: str = None,
	is_private: bool = False,
	message: str = None,
	type: str = None,
	source_type: str = None,
	source_url: str = None,
	groups_id: str = None,
	groups_name: str = None,
	groups_inherited: bool = True,
	id: str = None,
	requester_mail: str = None,
	requester_name: str = None,
	requester_ip: str = None,
	status: str = None,
	subject: str = None,
	tags: str = None,
	source_type1: bool = True,
	source_url1: str = None,
	source_id: str = None

	def __post_init__(self):
		if not(self.date is None or "-" in self.date):
			format = '%Y-%m-%d'
			self.date = util.epoch_to_format(format, self.date)