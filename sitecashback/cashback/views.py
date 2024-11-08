from typing import Any
from django.db.models.base import Model
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView

from .models import Article, Tag

from .utils import DataMixin, menu


class CashbackHome(DataMixin, ListView):
    template_name = "cashback/index.html"
    context_object_name = "posts"
    title_page = "Home"

    def get_queryset(self):
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


class ShowPost(DataMixin, DetailView):
    template_name = "cashback/post.html"
    slug_url_kwarg = "post_slug"
    context_object_name = "post"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title=context["post"].title)

    def get_object(self, queryset: QuerySet[Any] | None = ...) -> Model:
        return get_object_or_404(
            Article, is_published=True, slug=self.kwargs[self.slug_url_kwarg]
        )


class ArticleCategory(DataMixin, ListView):
    template_name = "cashback/index.html"
    context_object_name = "posts"
    allow_empty = False

    def get_queryset(self):
        return Article.objects.filter(
            is_published=True, category__slug=self.kwargs["category_slug"]
        ).select_related("category")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = context["posts"][0].category
        return self.get_mixin_context(
            context, title=f"Category {category.name}", cat_selected=category.pk
        )


class TagPostList(DataMixin, ListView):
    template_name = "cashback/index.html"
    context_object_name = "posts"
    allow_empty = False

    def get_queryset(self) -> QuerySet[Any]:
        return Article.objects.filter(
            is_published=True, tags__slug=self.kwargs["tag_slug"]
        ).select_related("category")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = Tag.objects.get(slug=self.kwargs["tag_slug"])
        return self.get_mixin_context(context, title=f"Tag : {tag.tag}")
