from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView

from .models import Article

from .utils import menu


def index(request):
    posts = Article.objects.all()
    data = {
        "title": "Home",
        "menu": menu,
        "posts": posts,
    }
    return render(request, "cashback/index.html", data)


class CashbackHome(ListView):
    template_name = "cashback/index.html"
    context_object_name = "posts"
    extra_context = {
        "title": "Home page",
        "menu": menu,
    }

    def get_queryset(self) -> QuerySet[Any]:
        return Article.objects.filter(is_published=True).select_related("category")


def about(request):
    data = {
        "title": "Abaut site",
        "menu": menu,
    }
    return render(request, "cashback/about.html", data)


def contact(request):
    data = {
        "title": "Contact",
        "menu": menu,
    }
    return render(request, "cashback/contact.html", data)


def login(request):
    data = {
        "title": "Login",
        "menu": menu,
    }
    return render(request, "cashback/login.html", data)


def page_not_found(request, exception):
    return HttpResponse("The page not found")

def show_post(request, post_slug):
    post = get_object_or_404(Article, slug=post_slug)
    data = {
        'title': post.title,
        'menu': menu,
        'post': post,
    }
    return render(request, 'cashback/show_post.html', data)