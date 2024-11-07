from django.urls import path

from .views import ArticleCategory, CashbackHome, ShowPost, about, index, contact, login, show_category, show_post, show_tag_postlist

urlpatterns = [
    path('', CashbackHome.as_view(), name='home'),
    # path('', index, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    # path('post/<slug:post_slug>/', show_post, name='post'),
    path('category/<slug:category_slug>/', ArticleCategory.as_view(), name='category'),
    # path('category/<slug:category_slug>/', show_category, name='category'),
    path('tag/<slug:tag_slug>/', show_tag_postlist, name='tag'),
]
