from django.test import TestCase, Client
from django.urls import reverse
from django.core.serializers.json import DjangoJSONEncoder
import unittest
import razorpay
import json
import time

from ..models import RazorpayHistory
from ..views import capture_payment


class RazorPayHistoryTests(TestCase):
    '''Testing model and stored_data() method'''


    def setUp(self):
        '''setting up the razorpayhistory objects'''
        RazorpayHistory.objects.create(
            name = 'Imay', card_type = 'debit', card_id = 'card_FKZbewMiiPThQX', txn_amount=10475, currency='INR', status='captured', authcode='428568', txn_date=int(time.mktime(time.strptime('2020-07-31 22:38:11', '%Y-%m-%d %H:%M:%S'))))
        RazorpayHistory.objects.create(
            name = 'Imayavalli', card_type = 'credit', card_id = 'card_FKZbewMghyutdS', txn_amount=40800, currency='USD', status='captured', authcode='428569', txn_date=int(time.mktime(time.strptime('2020-07-31 22:38:14', '%Y-%m-%d %H:%M:%S'))))


    def test_stored_data(self):
        '''testing the functionality of stored_data() method''' 
        razorpayment1 = RazorpayHistory.objects.get(card_id='card_FKZbewMiiPThQX') 
        razorpayment2 = RazorpayHistory.objects.get(card_id='card_FKZbewMghyutdS')
        self.assertEqual(razorpayment1.stored_data(), "Imay : card_FKZbewMiiPThQX\nINR 104.75 was transfered by debit card at 2020-07-31 22:38:11 \nAuth code: 428568")
        self.assertEqual(razorpayment2.stored_data(), "Imayavalli : card_FKZbewMghyutdS\nUSD 408.00 was transfered by credit card at 2020-07-31 22:38:14 \nAuth code: 428569")


    def test_create_json(self):
        '''testing the functionality of create_json_object() method'''
        razorpayment1 = RazorpayHistory.objects.get(card_id='card_FKZbewMiiPThQX') 
        razorpayment2 = RazorpayHistory.objects.get(card_id='card_FKZbewMghyutdS')
        output1 = {
                    "amount": 10475,
                    "currency": "INR",
                    "cardtype": "debit",
                    "card": {
                        "id": "card_FKZbewMiiPThQX"
                    },
                    "status": "captured",
                    "authorization_code": 428568,
                    "time": "2020-07-31 22:38:11"
                  }
        output1_string = json.dumps(output1, indent = 4, cls=DjangoJSONEncoder)
        output2 = {
                    "amount": 40800,
                    "currency": "USD",
                    "cardtype": "credit",
                    "card": {
                        "id": "card_FKZbewMghyutdS"
                    },
                    "status": "captured",
                    "authorization_code": 428569,
                    "time": "2020-07-31 22:38:14"
                  }
        output2_string = json.dumps(output2, indent = 4, cls=DjangoJSONEncoder)
        self.assertEqual(razorpayment1.create_json(), output1_string)
        self.assertEqual(razorpayment2.create_json(), output2_string)



class RazorPayHistoryCreationTests(TestCase):
    '''Testing model creation'''


    def create_model(self, title="only a test", body="yes, this is only a test"):
        '''creates a model object'''
        return RazorpayHistory.objects.create(name = 'Imay', card_type = 'debit', card_id = 'card_FKZbewMiiPThQX', txn_amount=10475, currency='INR', status='captured', authcode='428568', txn_date=int(time.mktime(time.strptime('2020-07-31 22:38:11', '%Y-%m-%d %H:%M:%S'))))

    
    def test_modelcreation(self):
        '''tests creation of model object'''
        model_obj = self.create_model()
        self.assertTrue(isinstance(model_obj, RazorpayHistory))
        
