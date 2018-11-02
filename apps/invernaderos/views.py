from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import render, redirect
from django.forms.models import model_to_dict
from django.urls import reverse_lazy
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.utils import timezone

from django.views.generic import CreateView, TemplateView 

from .forms import LoginForm, UserUpdate
from .models import *

import json

class SignUpView(LoginRequiredMixin, CreateView):
    model = User
    form_class = LoginForm


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


class PerfilDetailView(LoginRequiredMixin, DetailView):
    template_name = 'invernaderos/editarPerfil.html'
    model = User
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super(PerfilDetailView, self).get_context_data(**kwargs)
        return context


class InvernaderosListView(LoginRequiredMixin, ListView):
    model = Invernadero
    template_name = 'invernaderos/gestionarInvernaderos.html'
    context_object_name = 'invernaderos'


    def get_queryset(self):
        context = Invernadero.objects.all()
        return context
    
    def get_context_data(self, **kwargs):
        context = super(InvernaderosListView, self).get_context_data(**kwargs)
        return context

class InicioView(LoginRequiredMixin, TemplateView):
    template_name = 'invernaderos/gestionarInvernaderos.html'


def index(request):
    return redirect('/')

"""def invernadero_ajax(request):
    id_invernadero = request.POST['id_invernadero']
    invernadero = Invernadero.objects.filter(id_invernadero=id_invernadero)
    dispositivo = Dispositivo.objects.filter(id_dispositivo=invernadero.id_dispositivo)
    sensores = Sensores.objects.filter(id_dispositivo=dispositivo.id_dispositivo).order_by('nombre_dispositivo')
    objetos = []
    lista_sensores = []
    if request.POST['action'] == 'ver' or request.POST['action'] == 'editar':
        for sensor in sensores:
            lista_sensores.append({
                'id_sensor': sensor.id_sensor,
                'nombre_sensor': sensor.nombre_sensor
            })
        objetos.append({
            'id_invernadero': invernadero.id_invernadero,
            'nombre_invernadero': invernadero.nombre_invernadero,
            'ubicacion': invernadero.ubicacion,
            'id_dispositivo': dispositivo.id_dispositivo,
            'nombre_dispositivo': dispositivo.nombre_dispositivo,
            'lista_sensores': lista_sensores
        })
    elif request.POST['action'] == 'borrar':
        objetos.append({
            'id_invernadero': invernadero.id_invernadero,
            'nombre_invernadero': invernadero.nombre_invernadero
        })
    return HttpResponse(json.dumps(objetos), content_type='application/json')"""

def borrar_invernadero(request, id_invernadero):
    if request.method == 'POST':
        print(request)
        data = {
        'is_done': Invernadero.objects.filter(id_invernadero=id_invernadero).delete()
        }
        return JsonResponse(data)



        
