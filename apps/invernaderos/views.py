from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView

from django.views.generic import CreateView, TemplateView

from .models import Usuario

from .forms import LoginForm


"""
class LoginView(CreateView):
    model = Usuario
    form_class = LoginForm

    def form_valid(self, form):
        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_date.get('password1')
        usuario = authenticate(username=usuario, password=password)
        login(self.request, usuario)
        return redirect('/')
"""

class SignInView(LoginView):
    template_name = 'invernaderos/iniciarSesion.html'


class SignOutView(LogoutView):
    pass

class InicioView(TemplateView):
    template_name = 'invernaderos/gestionarInvernaderos.html'
