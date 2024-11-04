from django.http import HttpResponse
from django.shortcuts import render

from .models import Article


def index(request):
    posts = Article.objects.all()
    data = {
        'title': 'Home',
        'posts': posts,
    }
    return render(request, 'cashback/index.html', data)
