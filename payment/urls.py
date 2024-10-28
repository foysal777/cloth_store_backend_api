from django.urls import path
from payment import views

urlpatterns = [
    path('pay/', views.payment, name='payment'),
]
