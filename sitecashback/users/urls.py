from django.urls import path
from .views import login_check


urlpatterns = [
    path('login_check/', login_check, name='login_check'),
]
