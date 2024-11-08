from django.urls import path

from .views import (
    ArticleCategory,
    CashbackHome,
    ShowPost,
    TagPostList,
    about,
    contact,
    login,
)

urlpatterns = [
    path("", CashbackHome.as_view(), name="home"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    path("login/", login, name="login"),
    path("post/<slug:post_slug>/", ShowPost.as_view(), name="post"),
    path("category/<slug:category_slug>/", ArticleCategory.as_view(), name="category"),
    path("tag/<slug:tag_slug>/", TagPostList.as_view(), name="tag"),
]
