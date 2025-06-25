from django.urls import path
from .views import (
    UserAPIView, 
    RegisterAPIView, VerifyOTPApiView,ResendOTPApiView,
     LoginAPIView,
     LogoutAPIView, 
     StudentApi ,
     payment_success
)
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
   
    path('student/', StudentApi.as_view(), name='student'),  
    path('user_all/', UserAPIView.as_view(), name='user-list'),  
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('verify_otp/', VerifyOTPApiView.as_view(), name='verify-otp'),
    path('resend_otp/', ResendOTPApiView.as_view(), name='resend-otp'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/payment/success/', payment_success, name='payment_success'),


]