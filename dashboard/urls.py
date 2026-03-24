from django.urls import path
from .views import *

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('profile/', admin_profile, name='admin_profile'),
]