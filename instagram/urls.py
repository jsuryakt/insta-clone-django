from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls'), name='authentication'),
    path('feed/',include('core.urls'), name = 'core'),
]
