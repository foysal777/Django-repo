import striped
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from django.shortcuts import render ,redirect

striped.api_key = settings.STRIPE_SECRET_KEY

class CreateCheckoutSessionView(APIView):
    def post(self, request):
        try:
            checkout_session = striped.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[
                    {
                        'price_data': {
                            'currency': 'usd',
                            'unit_amount': 2000, 
                            'product_data': {
                                'name': 'T-shirt',
                            },
                        },
                        'quantity': 1,
                    },
                ],
                mode='payment',
                success_url='http://localhost:8000/success',
                cancel_url='http://localhost:8000/cancel',
            )
            return Response({'id': checkout_session.id})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)




        
        
    # 1st
import stripe
from django.conf import settings
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

stripe.api_key = settings.STRIPE_SECRET_KEY

def create_checkout_session1(request):
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price': 'price_1RdiTU4Ft3OiftBENmAiWovw',
            'quantity': 1,
        }],
        mode='subscription',
        success_url='http://localhost:8000/stripe/api/success/',
        cancel_url='http://localhost:8000/api/cancel/',
     
    )
    return redirect( session.url)


def success_url(request):
    return render(request,'success.html')
    # HttpResponse("payment successfully completed, Thank you")