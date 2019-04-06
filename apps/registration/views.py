from django.contrib.auth.models import User
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy

from .forms import RegisterForm


class RegisterUser(CreateView):
    model = User
    template_name = "registration/register.html"
    form_class = RegisterForm
    success_url = reverse_lazy("registration:welcome")


class WelcomeUser(TemplateView):
    template_name = "registration/welcome.html"
