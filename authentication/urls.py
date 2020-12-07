from django.contrib import admin
from django.urls import path
from authentication.views import SignUpView,home,SignInView
urlpatterns = [
    path('', SignUpView.as_view(), name='signup_view'),
    path('signin/', SignInView.as_view(), name='signin_view'),
    path('home/',home,name='home')
]