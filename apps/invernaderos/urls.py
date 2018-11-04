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
        'perfil/<slug:pk>/',
        views.PerfilUpdateView.as_view(),
        name='perfil'
    ),
    path(
        'sign-out/',
        views.SignOutView.as_view(),
        name='sign-out'
    ),
    path(
        'monitorear/',
        views.MonitorearView.as_view(),
        name = 'monitorear'
    )
]

urlpatterns = format_suffix_patterns(urlpatterns)