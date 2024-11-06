from django.http import HttpResponse
from django.shortcuts import render

from .models import Article

from .utils import menu


def index(request):
    posts = Article.objects.all()
    data = {
        'title': 'Home',
        'menu': menu,
        'posts': posts,
    }
    return render(request, 'cashback/index.html', data)

def about(request):
    data = {
        'title': 'Abaut site',
        'menu': menu,
    }
    return render(request, 'cashback/about.html', data)

def contact(request):
    data = {
        'title': 'Contact',
        'menu': menu,
    }
    return render(request, 'cashback/contact.html', data)

def login(request):
    data = {
        'title': 'Login',
        'menu': menu,
    }
    return render(request, 'cashback/login.html', data)

def page_not_found(request, exception):
    return HttpResponse('The page not found')