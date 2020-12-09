from django.urls import path
from core.views import FeedView
from django.contrib.auth.decorators import login_required

urlpatterns = [
   path('', login_required(FeedView.as_view()), name="feed_view"),
]