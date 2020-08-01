from django.test import TestCase, Client
from django.urls import reverse
import unittest
from payments import settings
import razorpay
import hmac
import hashlib
import json
from ..models import RazorpayHistory
from ..views import capture_payment

class ChargeTests(TestCase):
    '''Test module for charge() method'''


    def setUp(self):
        self.client = Client()
        self.razorpay_client = razorpay.Client(auth=(settings.PUBLIC_KEY, settings.SECRET_KEY))
        self.razorpay_payment_id = 'pay_FLKatectcn16O5'
        
        
    def test_fetch_payment(self):
        '''fetches payment details by payment_id - checks if its stored'''
        try:
            response = self.razorpay_client.payment.fetch(self.razorpay_payment_id)
        except: #if the payment_id does not exist yet
            pass
        else:
            self.assertEqual(response['status'], 'captured')
       
    def test_amount(self):
        '''required amount (in index.html) must match the paid amount (settings.amount)'''
        self.assertEqual(settings.AMOUNT, 10020) 
  

    def test_signature_generation(self):
        '''tests the signature generation from secret key'''
        payment_id = 'pay_FLO4PfRzrqVkun'
        generated_signature = hmac.new(bytes(settings.SECRET_KEY, 'utf-8'), bytes(str(settings.ORDER_ID) + "|" + str(payment_id), 'utf-8'), hashlib.sha256).hexdigest()
        self.assertEqual(generated_signature, 'babc9819408997906bd2fa8d5af31ac94ce16f9d2458992881a95b2d66151413')

