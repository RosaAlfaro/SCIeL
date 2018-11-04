from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response as RFResponse

from django.views.generic import CreateView, TemplateView 
from django.views.generic.edit import FormView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import render, redirect, get_object_or_404
from django.forms.models import model_to_dict
from django.urls import reverse_lazy
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.utils import timezone

from .forms import LoginForm, UserUpdate, InvernaderoForm
from .models import *
from .serializer import *

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
        user = self.request.user
        context = Invernadero.objects.all().filter(id_usuario=user.id)
        return context
    
    def get_context_data(self, **kwargs):
        context = super(InvernaderosListView, self).get_context_data(**kwargs)
        return context


class CultivosListView(LoginRequiredMixin, ListView):
    model = Cultivo
    template_name = 'invernaderos/gestionarCultivos.html'
    context_object_name = 'cultivos'


    def get_queryset(self):
        user = self.request.user
        context = Cultivos.objects.all().filter(id_usuario=user.id)
        return context
    
    def get_context_data(self, **kwargs):
        context = super(CultivosListView, self).get_context_data(**kwargs)
        return context

def editar_invernadero(request):
    id_invernadero = request.GET['id_invernadero']
    invernadero = get_object_or_404(Invernadero, id_invernadero=id_invernadero)
    if request.method == 'POST':
        form =InvernaderoForm(request.POST, instance=invernadero)
        if form.is_valid():
            invernadero = form.save(commit=False)
            invernadero.id_usuario = request.POST['id_usuario']
            invernadero.save()
            message = 'Los cambios fueron guardados exitosamente'
        else:
            message = 'Algunos campos son inválidos'
        data = {
                'message': message
            }
        return JsonResponse(data)
    else:
        form = InvernaderoForm(instance=invernadero)
    data = {
        'form': form.as_p
    }
    return HttpResponse(data)

@api_view(['GET', 'PUT', 'DELETE'])
@login_required(login_url='/sign-in/')
def invernadero(request):
    
    if request.method == 'GET':

        id_invernadero = request.GET['id']

        invernadero = Invernadero.objects.get(id_invernadero=id_invernadero)

        invernadero_serializer = InvernaderoSerializer(invernadero, many=False)
        
        """dispositivo = Dispositivo.objects.filter(id_dispositivo=invernadero.id_dispositivo)
        dispositivo_serializer = DispositivoSerializer(dispositivo, many=False)

        cultivos = Cultivo.objects.filter(id_invernadero=dispositivo.id_invernadero).order_by('nombre_cultivo')
        cultivos_serializer = SensorSerializer(cultivos, many=True)
        
        data = {
            'invernadero': invernadero_serializer,
            'dispositivo': dispositivo_serializer,
            'cultivos': cultivos_serializer
        }"""
        message = 'Los datos han sido desplegados'
        data = {
            'invernadero': invernadero_serializer.data,
            'message': message
        }
        return RFResponse(data=data)
    
    elif request.method == 'PUT':
        id_invernadero = request.POST['id']

        invernadero = Invernadero.objects.get(id_invernadero=id_invernadero)

        invernadero_serializer = InvernaderoSerializer(invernadero, data=request.data['invernadero'])

        if invernadero_serializer.is_valid():
            result = invernadero_serializer.save()
            
            message = None

            if result:
                message = "El invernadero fue modificado exitosamente"
            else:
                message = "El invernadero no pudo ser modificado"
            data = {
                'message': message
            }
            return RFResponse(
                data={
                    'invernadero': invernadero_serializer.data,
                    'data':data
                }
            )
        message = "El formulario no es válido"
        data = {
            'message': message
        }
        return RFResponsedata(
            data={
                'errors': invernadero_serializer.errors,
                'data': data
            }, 
            status=status.HTTP_400_BAD_REQUEST
        )

    elif request.method == 'DELETE':
        id_invernadero = request.POST['id']

        invernadero = Invernadero.objects.get(id_invernadero=id_invernadero)

        message = None

        result = invernadero.delete()
        if result:
            message = "El invernadero fue borrado exitosamente"
        else:
            message = "El invernadero no pudo ser borrado"
        return RFResponse(data=message, status=status.HTTP_204_NO_CONTENT)

        

def borrar_invernadero(request):
    if request.method == 'POST':
        id_invernadero = request.POST['id_invernadero']
        result = Invernadero.objects.filter(id_invernadero=id_invernadero).delete()
        if result:
            message = "El invernadero fue borrado exitosamente"
        else:
            message = "El invernadero no pudo ser borrado"
        data = {
            'message': message
        }
        return JsonResponse(data)



        
