from django.contrib import admin
from django.urls import path
from authentication.views import SignUpView,home
urlpatterns = [
    path('', SignUpView.as_view(), name='signup_view'),
    path('',home,name='home')
]