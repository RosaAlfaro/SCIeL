from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path(
        'sign-in/',
        views.SignInView.as_view(),
        name='sign-in'
    ),
    path(
        '',
        views.InvernaderosListView.as_view(),
        name='invernaderos'
    ),
    re_path(
        r'^monitorear/(?P<id_invernadero>[0-9]+)/',
        views.monitorear_invernadero,
        name = 'monitorear'
    ),
    path(
        'monitorear/',
        views.monitorear_invernadero,
        name = 'monitorear'
    ),
    path(
        'cultivos/',
        views.CultivosListView.as_view(),
        name='cultivos'
    ),
    path(
        'dispositivos/',
        views.DispositivosListView.as_view(),
        name='dispositivos'
    ),
    path(
        'parametros/',
        views.ParametrosListView.as_view(),
        name='parametros'
    ),
    path(
        'sensores/',
        views.SensoresListView.as_view(),
        name='sensores'
    ),
    path(
        'actuadores/',
        views.ActuadoresListView.as_view(),
        name='actuadores'
    ),
    path(
        'ajax/invernadero/',
        views.invernadero,
        name='ajax-invernadero'
    ),
    path(
        'ajax/dispositivo/',
        views.dispositivo,
        name='ajax-dispositivo'
    ),
    path(
        'perfil/<slug:pk>/',
        views.PerfilUpdateView.as_view(),
        name='perfil'
    ),
    path(
        'sign-out/',
        views.SignOutView.as_view(),
        name='sign-out'
    )
]
