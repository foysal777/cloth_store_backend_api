
from sslcommerz_lib import SSLCOMMERZ 
import random, string
from django.http import HttpResponse, HttpResponseRedirect

def unique_transaction_id_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def payment(request):
    settings = { 'store_id': 'foysa671dabfd11ca2', 'store_pass': 'foysa671dabfd11ca2@ssl', 'issandbox': True }
        
    sslcz = SSLCOMMERZ(settings)
    
    post_body = {}
    post_body['total_amount'] = 5600.26 
    post_body['currency'] = "BDT"
    post_body['tran_id'] = unique_transaction_id_generator()
    post_body['success_url'] = "http://127.0.0.1:5500/index.html"
    post_body['fail_url'] = "http://127.0.0.1:5500/index.html"
    post_body['cancel_url'] = "hhttp://127.0.0.1:5500/index.htm"
    post_body['emi_option'] = 0
    post_body['cus_name'] = "test"
    post_body['cus_email'] = "test@test.com"
    post_body['cus_phone'] = "01700000000"
    post_body['cus_add1'] = "Cantonment"
    post_body['cus_city'] = "Dhaka"
    post_body['cus_country'] = "Bangladesh"
    post_body['shipping_method'] = "NO"
    post_body['multi_card_name'] = ""
    post_body['num_of_item'] = 1
    post_body['product_name'] = "Test"
    post_body['product_category'] = "Test Category"
    post_body['product_profile'] = "general"


    response = sslcz.createSession(post_body) # API response
    # print(response)
    if response['status'] == 'SUCCESS':
        return HttpResponseRedirect(response['GatewayPageURL'])
    else:
        return HttpResponse("Payment initiation failed. Please try again later.")
    # Need to redirect user to response['GatewayPageURL']
    
    
    
# # views.py
# from sslcommerz_lib import SSLCOMMERZ
# import random, string
# from django.http import HttpResponse, HttpResponseRedirect
# from django.shortcuts import render
# from django.urls import reverse

# # Function to generate a unique transaction ID
# def unique_transaction_id_generator(size=10, chars=string.ascii_uppercase + string.digits):
#     return ''.join(random.choice(chars) for _ in range(size))

# # Payment initiation view
# def payment(request):
#     settings = { 
#         'store_id': 'foysa671dabfd11ca2', 
#         'store_pass': 'foysa671dabfd11ca2@ssl', 
#         'issandbox': True 
#     }
#     sslcz = SSLCOMMERZ(settings)
    
#     transaction_id = unique_transaction_id_generator()
#     post_body = {
#         'total_amount': 5600.26,
#         'currency': "BDT",
#         'tran_id': transaction_id,
#         'success_url': request.build_absolute_uri(reverse('payment_success', args=[transaction_id])),
#         'fail_url': request.build_absolute_uri(reverse('payment_fail')),
#         'cancel_url': request.build_absolute_uri(reverse('payment_cancel')),
#         'emi_option': 0,
#         'cus_name': "test",
#         'cus_email': "test@test.com",
#         'cus_phone': "01700000000",
#         'cus_add1': "Cantonment",
#         'cus_city': "Dhaka",
#         'cus_country': "Bangladesh",
#         'shipping_method': "NO",
#         'multi_card_name': "",
#         'num_of_item': 1,
#         'product_name': "Test",
#         'product_category': "Test Category",
#         'product_profile': "general"
#     }

#     response = sslcz.createSession(post_body)
    
#     if response['status'] == 'SUCCESS':
#         return HttpResponseRedirect(response['GatewayPageURL'])
#     else:
#         return HttpResponse("Payment initiation failed. Please try again later.")

# # Success view
# def payment_success(request, transaction_id):
#     context = {'transaction_id': transaction_id}
#     return render(request, 'payment_success.html', context)

# # Failure view
# def payment_fail(request):
#     return HttpResponse("Payment failed. Please try again.")

# # Cancel view
# def payment_cancel(request):
#     return HttpResponse("Payment was cancelled.")
