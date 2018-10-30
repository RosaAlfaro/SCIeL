from django.shortcuts import render
from django.contrib.auth import authenticate, login

def login(request):
    usuario = request.POST['username']
    contraseña = request.POST['password']
    user = authenticate(request, username=usuario)
