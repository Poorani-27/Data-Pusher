# data_pusher_app/urls.py
from django.urls import path
from .views import home, incoming_data
from django.urls import path
from .views import incoming_data

urlpatterns = [
    path('', home, name='home'),
    path('api/', incoming_data, name='incoming_data'),
]
