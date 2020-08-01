## Payment Gateway API

This is a wrapper integration for the Razorpay API in Python and Django.
The public and secret keys are set for dev and must be newly generated for actual money transactions.
This project uses Razorpay to handle credit and debit card transactions, and stores the payment_details in a local SQL database.

### Razorpay API security abstraction

Payments can be made only through Razorpay's embedded UI in the integrated API for security reasons.
Payment details like cvv of a card, etc are abstracted from the vendor i.e this program. 
Hence, a payment cannot be made through an API method call.
But payment details like the amount, card type, transaction time, etc can be fetched after the transaction has been successfully captured by Razorpay.

### Setup Instructions:

(Optional) Create a free profile in razorpayapp.com and generate your own public key and secret key. Replace in index.html, views.py, tests_views.py.
Creating an account enables the user to view all the order details and payment details through Razorpay's interactive dashboard.

#### Running the Project Locally

Install the requirements:
`pip install -r requirements.txt`
Setup the local configurations:
`cp .env.example .env`
Create the database:
`python manage.py migrate`
Finally, run the development server:
`python manage.py runserver`
The project will be available at 127.0.0.1:8000/razorpayapp/

### Usage:

(Note) Only works with internet access - since it calls the Razorpay API
* Go to 127.0.0.1:8000/razorpayapp/
* Click the button
* Use the UI to edit the user details
* Choose Pay by Card 
* Skip Saved Cards
* Type any one of these card numbers `{4111 1111 1111 1111, 5104 0155 5555 5558, 5104 0600 0000 0008}`
* Type any date past the current date as the expiry date
* Type any random 3 digits for CVV
* Unselect Remember card
* Click Pay button
* Choose Select/Failure and view both the outputs separately

##### Editing the amount:
Change amount in index.html and settings.py. 
The required amount and the paid amount must match for a successful transaction.
Note: amount is in paise (if INR) or cent (if USD), and so on.

### Assumptions:
* No user authentication is required to proceed with the payment
* The user enters their card details in Razorpay's embedded UI which pops on the screen when the user clicks on the 'Pay Now' button. We, the merchants cannot see their card details.
* Only credit card and debit card options has been integrated in this project

### References:
https://razorpay.com/docs/payment-gateway/
https://razorpay.com/docs/payment-gateway/server-integration/python/







Payment details example:

self.valid_response = {
                    'id': 'pay_FLCRGTOndXQoqj', 
                    'entity': 'payment', 
                    'amount': 10020, 
                    'currency': 'INR', 
                    'status': 'captured', 
                    'order_id': None, 
                    'invoice_id': None, 
                    'international': False, 
                    'method': 'card', 
                    'amount_refunded': 0, 
                    'refund_status': None, 
                    'captured': True, 
                    'description': 'Purchase Description', 
                    'card_id': 'card_FKZbewMiiPThQX', 
                    'card': {
                        'id': 'card_FKZbewMiiPThQX', 
                        'entity': 'card', 
                        'name': 'Harshil Mathur', 
                        'last4': '1111', 
                        'network': 'Visa', 
                        'type': 'debit', 
                        'issuer': None, 
                        'international': False, 
                        'emi': False, 
                        'global_fingerprint': '6a045f295a17379c5e0cb38bbfb29cf7', 
                        'sub_type': 'consumer'}, 
                    'bank': None, 
                    'wallet': None, 
                    'vpa': None, 
                    'email': 'imayn9@gmail.com', 
                    'contact': '+919999999999', 
                    'notes': {'shopping_order_id': '21'}, 
                    'fee': 201, 
                    'tax': 0, 
                    'error_code': None, 
                    'error_description': None, 
                    'error_source': None, 
                    'error_step': None, 
                    'error_reason': None, 
                    'acquirer_data': {'auth_code': '253749'}, 
                    'created_at': 1596219648}