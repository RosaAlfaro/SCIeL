from django.views.generic.edit import FormView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http.response import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView


from django.views.generic import CreateView, TemplateView

from .forms import LoginForm, SignUpForm

class SignUpView(LoginRequiredMixin, CreateView):
    model = User
    form_class = SignUpForm

    def form_valid(self, form):
        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_date.get('password1')
        usuario = authenticate(username=usuario, password=password)
        if(not usuario.is_authenticated):
            context = {
                'mensaje': 'Credenciales erróneas',
                'form': form
                }
            return render(form.request, 'invernaderos/inciarSesion.html', context=context)
        else:
            login(self.request, usuario)
            return redirect('')


class SignInView(LoginView):
    template_name = 'invernaderos/iniciarSesion.html'


"""class Login(FormView):
    form_class = AuthenticationForm
    template_name = 'invernaderos/iniciarSesion.html'
    success_url = reverse_lazy('invernaderos:invernaderos')
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(self, Login).dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(self, Login).form_valid(form)
"""

class SignOutView(LoginRequiredMixin, LogoutView):
    template_name = 'invernaderos/iniciarSesion.html'


class InicioView(LoginRequiredMixin, TemplateView):
    template_name = 'invernaderos/gestionarInvernaderos.html'
