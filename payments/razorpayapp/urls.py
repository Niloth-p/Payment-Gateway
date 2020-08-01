from django.urls import path

from razorpayapp.views import index, charge, capture_payment

urlpatterns = [
    path('', index, name='index'),
    path('charge', charge, name='charge'),
    path('capture_payment', capture_payment, name='capture_payment')
]