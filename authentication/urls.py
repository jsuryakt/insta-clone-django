from django.contrib import admin
from django.urls import path
from authentication.views import SignUpView,SignInView, SignOutView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup_view'),
    path('', SignInView.as_view(), name='signin_view'),
    path('signout/', SignOutView.as_view(), name='signout_view')
    # path('feed/',feed,name='home_feed')
]                                                                                                                                            