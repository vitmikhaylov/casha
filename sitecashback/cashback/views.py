from typing import Any
from django.db.models.base import Model
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView

from .models import Article, Category, Tag

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
        "title": post.title,
        "menu": menu,
        "post": post,
    }
    return render(request, "cashback/post.html", data)


class ShowPost(DetailView):
    model = Article
    template_name = "cashback/post.html"
    slug_url_kwarg = "post_slug"
    context_object_name = "post"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = context["post"].title
        context["menu"] = menu
        return context

    def get_object(self, queryset: QuerySet[Any] | None = ...) -> Model:
        return get_object_or_404(
            Article, is_published=True, slug=self.kwargs[self.slug_url_kwarg]
        )
    
def show_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    posts = Article.objects.filter(category_id=category.pk)
    data = {
        'title': f'Category: {category.name}',
        'menu': menu,
        'posts': posts,
    }
    return render(request, 'cashback/index.html', data)


def show_tag_postlist(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    posts = tag.tags.filter(is_published=True)
    data = {
        'title': f'Tag: {tag.tag}',
        'menu': menu,
        'posts': posts,
    }
    return render(request, 'cashback/index.html', data)
