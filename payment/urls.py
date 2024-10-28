
from django.urls import path
from . import views

urlpatterns = [
    path('pay/', views.payment, name='payment'),
    # path('transaction/payment/success/<str:transaction_id>/', views.payment_success, name='payment_success'),
    # path('transaction/payment/fail/', views.payment_fail, name='payment_fail'),
    # path('transaction/payment/cancel/', views.payment_cancel, name='payment_cancel'),
]
