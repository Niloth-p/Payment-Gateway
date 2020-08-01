from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import get_language
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import JsonResponse

import json
import time
import razorpay
from .models import RazorpayHistory


def index(request):
    return render(request, 'payments/index.html')


@csrf_exempt
def charge(request):
    if request.method == "POST":
        output_string = capture_payment(request)
        return HttpResponse(output_string, content_type="text/plain")
    return HttpResponse(status=200)


def capture_payment(request):
    '''capturing the payment using razorpay client then fetching the payment details'''
    razorpay_client = razorpay.Client(auth=("rzp_test_lXnX8botLYip9x", "ILz3LievuVZ6IDZzBMwjWn9f"))
    razorpay_client.set_app_details({"title" : "Title", "version" : "1.0"})
    amount = settings.AMOUNT # in paise //to check if capture paid matches the reqd amount - otherwise Error
    payment_id = request.POST.get('razorpay_payment_id','')
    razorpay_client.payment.capture(payment_id, amount)
    data = razorpay_client.payment.fetch(payment_id)
    card_data = razorpay_client.card.fetch(card_id=data['card_id'])
    output_string = store_to_db(data, card_data) 
    return output_string


def store_to_db(data, card_data):   
    '''stores tha payment details to the database'''
    razorpay_history = RazorpayHistory()
    razorpay_history.name = card_data['name']
    razorpay_history.card_type = card_data['type']
    razorpay_history.card_id = card_data['id']
    razorpay_history.txn_amount = data['amount']
    razorpay_history.payment_mode = data['method']
    razorpay_history.currency = data['currency']
    razorpay_history.status = data['status']
    try:
        razorpay_history.authcode = data['acquirer_data']['auth_code']
    except:
        print()
    txn_time = data['created_at']
    razorpay_history.txn_date = txn_time
    razorpay_history.save()
    output_string = razorpay_history.stored_data() + '\n'
    output_string += razorpay_history.create_json()
    return output_string
