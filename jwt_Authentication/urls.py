
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('jwt_auth/' , include('jwt_auth.urls')),
    path('stripe/' , include('striped.urls')),
]
