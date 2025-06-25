from django.urls import path
from .views import CreateCheckoutSessionView,create_checkout_session1 , success_url

urlpatterns = [
    path('create-checkout-session/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path("create_checkout_session1/", create_checkout_session1, name="create-payment"),
    path('api/success/' , success_url, name='success')
]

