from unified.core.triggers import Triggers
from server_monitoring.freshservice.api import FreshserviceApi


class FreshserviceTriggers(Triggers):

    def new_ticket(self, context, payload):
        """ Triggered when new ticket is created """

        payload = payload['freshdesk_webhook']

        return FreshserviceApi.get_ticket_data(payload)


    def new_ticket(self, context, payload):
        """ Triggered when ticket was updated """

        payload = payload['freshdesk_webhook']

        return FreshserviceApi.get_ticket_data(payload)
