from django.urls import path

from .views import about, index, contact, login

urlpatterns = [
    path('', index, name='name'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
]
