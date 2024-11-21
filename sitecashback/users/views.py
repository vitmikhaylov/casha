from django.http import HttpResponse
from django.shortcuts import render


def login_check(request):
    return HttpResponse('Login')
