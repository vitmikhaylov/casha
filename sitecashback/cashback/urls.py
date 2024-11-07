from django.urls import path

from .views import CashbackHome, ShowPost, about, index, contact, login, show_post

urlpatterns = [
    path('', CashbackHome.as_view(), name='name'),
    # path('', index, name='name'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    # path('post/<slug:post_slug>/', show_post, name='post'),
]
