from unified.core.triggers import Triggers
from . import util
class TypeformTriggers(Triggers):
    def new_entry(self, context, payload):
        resp = {
            'entry_id': payload['event_id'],
            'submitted_at': payload['form_response']['submitted_at'],
            'title': payload['form_response']['definition']['title']
        }

        fields = payload['form_response']['definition']['fields']

        for field in fields:
            title = field['title']
            value = util.get_typeform_answer(payload['form_response']['answers'], field['id'])

            resp[title] = value

        return resp
