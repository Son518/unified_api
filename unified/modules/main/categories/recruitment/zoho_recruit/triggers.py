from unified.core.triggers import Triggers
from recruitment.zoho_recruit.api import ZohorecruitApi


class ZohorecruitTriggers(Triggers):

    def new_record(self, context, payload):
        '''trigger when new record is created '''

        params = {
            "record_id": payload['id']
        }
        return ZohorecruitApi().record(context, params)

    def updated_record(self, context, payload):
        '''trigger when new record is updated '''

        params = {
            "record_id": payload['id']
        }
        return ZohorecruitApi().record(context, params)