# from django.test import TestCase, Client
# from django.urls import reverse
# import unittest
# import razorpay
# from .models import RazorpayHistory
# from .views import capture_payment

# class PaymentTests(TestCase):

#     def setUp(self):
#         '''setting up the razorpay client and the data to be captured'''
#         razorpay_client = razorpay.Client(auth=("rzp_test_1EpF60pesrZQRU", "4udhRNkCqjQYIxuUza28t3N9"))
#         razorpay_history = RazorpayHistory()
        
#         #payment_id = request.POST.get('razorpay_payment_id','')

        

#         #assert resp.status_code == 200
#         #response = self.app.post('https://api.razorpay.com/v1/orders', data=json.dumps(data), headers=self.headers)


#     # def test_amountmismatch(self):
#     #     '''setting required amount different from captured amount to cause a mismatch'''
#     #     amount = 50000 # in paise //to check if capture paid matches the reqd amount - otherwise Error
#     #     c = Client()
#     #     razorpay_client = razorpay.Client(auth=("rzp_test_1EpF60pesrZQRU", "4udhRNkCqjQYIxuUza28t3N9"))
#     #     payment_data = {"amount": 10000,
#     #             "currency": "INR",
#     #             "receipt": "rcptid_11",
#     #             "payment_capture": 1}
#     #     temp = 0
#     #     self.assertEqual(temp, 0)
#     #     resp = c.post(reverse('capture_payment'), data = payment_data)
#     #     #resp = c.post('/razorpayapp/charge', data = payment_data)
#     #     payment_id = resp.get('razorpay_payment_id','')
#     #     razorpay_client.payment.capture(payment_id, amount) #this should cause error
#     #     self.assertEqual(temp, 0)
#     #     data = razorpay_client.payment.fetch(payment_id)
#     #     self.assertEqual(temp, 0)
#     #     print(data) #should be null?


#     def test_capture_payment(self):
#         '''testing the capture payment method'''     
        
#         amount = 10000 # in paise //to check if capture paid matches the reqd amount - otherwise Error
#         c = Client()
#         payment_data = {"amount": 10000,
#                 "currency": "INR",
#                 "receipt": "rcptid_11",
#                 "payment_capture": 1}
#         temp = 0
#         self.assertEqual(temp, 0)
#         resp = c.post(reverse('capture_payment'), data = payment_data)
#         #resp = c.post('/razorpayapp/capture_payment', data = payment_data)
#         payment_id = resp.get('razorpay_payment_id','')
#         razorpay_client.payment.capture(payment_id, amount) #this should cause error
#         self.assertEqual(temp, 0)
#         data = razorpay_client.payment.fetch(payment_id)

#        #data = capture_payment(request)

#         # amount = 10000 # in paise //to check if capture paid matches the reqd amount - otherwise Error
#         # resp = requests.post('https://api.razorpay.com/v1/orders', data = data)
#         # payment_id = resp.get('razorpay_payment_id','')
#         # razorpay_client.payment.capture(payment_id, amount)
#         # data = razorpay_client.payment.fetch(payment_id)

#         self.assertEqual(data['entity'], "payment")
#         self.assertEqual(data['amount'], 10000)
#         self.assertEqual(data['currency'], "INR")
#         self.assertEqual(data['status'], "captured")
#         self.assertEqual(data['method'], "card")
#         self.assertEqual(data['captured'], True)
#         self.assertEqual(data['email'], "imayn9@gmail.com")
#         self.assertEqual(data['contact'], "+919999999999")
#         self.assertEqual(data['error_code'], null)



#     def store_to_db(self):
#         '''checking if the values have been saved to the database'''
#         # amount = 10000 # in paise //to check if capture paid matches the reqd amount - otherwise Error
#         # resp = requests.post('https://api.razorpay.com/v1/orders', data = data)
#         # payment_id = resp.get('razorpay_payment_id','')
#         # razorpay_client.payment.capture(payment_id, amount)
#         # data = razorpay_client.payment.fetch(payment_id)
#         # razorpay_history.txn_amount = data['amount']
#         # razorpay_history.payment_mode = data['method']
#         # razorpay_history.currency = data['currency']
#         # #razorpay_history.card_number = data.???
#         # razorpay_history.status = data['status']
#         # try:
#         #     razorpay_history.authcode = data['acquirer_data']['auth_code']
#         # except:
#         #     print()
#         # txn_time = data['created_at']
#         # razorpay_history.txn_date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(txn_time))
#         # razorpay_history.save()

#         data = capture_payment(request)
#         #now run sql queries to find if it has been updated with the latest entry

    
        

