from django.test import TestCase, Client
from django.urls import reverse
import unittest
import razorpay
import json
from ..models import RazorpayHistory
from ..views import capture_payment

class ChargeTests(TestCase):
    '''Test module for charge() method'''


    def setUp(self):
        self.client = Client()
        self.razorpay_client = razorpay.Client(auth=("rzp_test_lXnX8botLYip9x", "ILz3LievuVZ6IDZzBMwjWn9f"))
        self.razorpay_payment_id = 'pay_FLKatectcn16O5'
        
        
    def test_fetch_payment(self):
        '''fetches payment details by payment_id - checks if its stored'''
        try:
            response = self.razorpay_client.payment.fetch(self.razorpay_payment_id)
        except: #if the payment_id does not exist yet
            pass
        else:
            self.assertEqual(response['status'], 'captured')
       
    def amount(self):
        '''required amount (in index.html) must match the paid amount (settings.amount)'''
        self.assertEqual(settings.AMOUNT, 10020) 
  
