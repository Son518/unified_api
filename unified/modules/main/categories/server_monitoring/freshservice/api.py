from server_monitoring.freshservice import util
from server_monitoring.freshservice.entities.freshservice_ticket import FreshserviceTicket
from server_monitoring.freshservice.entities.freshservice_requester import FreshserviceRequester


class FreshserviceApi:

    @staticmethod
    def get_ticket_data(payload):
        """utility function for getting ticket data from payload"""

        return FreshserviceTicket(
            ticket_id=payload.get('ticket_id'),
            subject=payload.get('ticket_subject'),
            email=payload.get('ticket_requester_email'),
            description=payload.get('ticket_description'),
            priority=payload.get('ticket_priority'),
            status=payload.get('ticket_status')
        ).__dict__
