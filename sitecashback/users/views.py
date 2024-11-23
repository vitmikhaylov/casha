from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy

from .forms import LoginUserForm

from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Authotization'}

    # def get_success_url(self) -> str:
    #     return reverse_lazy('home')

# def login_user(request):
#     if request.method == "POST":
#         form = LoginUserForm(request.POST)
#         if form.is_valid():
#             cleaned_data = form.cleaned_data
#             user = authenticate(
#                 request,
#                 username=cleaned_data["username"],
#                 password=cleaned_data["password"],
#             )
#             if user and user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect(reverse("home"))
#     else:
#         form = LoginUserForm()
#     return render(request, "users/login.html", {"form": form})


# def logout_user(request):
#     logout(request)
#     return HttpResponseRedirect(reverse('users:login'))
