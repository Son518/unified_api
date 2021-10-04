from unified.core.triggers import Triggers
from phone_sms.clicksend_sms import util



class ClickSendTriggers(Triggers):

    def new_sms_sent(self, context, payload):
        '''Triggers when a new sms is sent'''

        pass
