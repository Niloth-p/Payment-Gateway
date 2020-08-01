from django.db import models
from django.conf import settings
from django.utils import timezone
import json
import time
from django.core.serializers.json import DjangoJSONEncoder


class RazorpayHistory(models.Model):
    '''payment details of each razorpay transaction'''
    name = models.CharField(max_length=16, null=True, blank=True)
    card_type = models.CharField(max_length=16, null=True, blank=True)
    card_id = models.CharField(max_length=16, null=True, blank=True)
    txn_amount = models.IntegerField()
    currency = models.CharField(max_length=4, null=True, blank=True)
    status = models.CharField(max_length=12)
    authcode = models.IntegerField(null=True)
    txn_date = models.IntegerField(default=timezone.now)


    def stored_data(self):
        '''returns a string summarising the transaction'''
        if self.status == 'captured':
            output_string = self.name + ' : ' + self.card_id + '\n' + str(self.currency) + ' ' + str(int(self.txn_amount/100)) + '.'
            if(self.txn_amount%100==0):
                output_string += '00 '
            else:
                output_string += str(self.txn_amount%100) + ' '
            output_string +=  'was transfered by ' + self.card_type + ' card at ' 
            output_string += str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(self.txn_date)))
            output_string += ' \nAuth code: ' + str(self.authcode)
            return output_string
        return 'Payment failed'

    def create_json(self):
        if self.status == 'captured':
            card_dict = { "id": self.card_id }
            obj = {
                    "amount": self.txn_amount,
                    "currency": self.currency,
                    "cardtype": self.card_type,
                    "card": card_dict,
                    "status": self.status,
                    "authorization_code": self.authcode,
                    "time": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(self.txn_date)),
                }
            obj_string = json.dumps(obj, indent = 4, cls=DjangoJSONEncoder) 
            return obj_string
        return {}

