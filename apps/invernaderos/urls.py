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
        'ajax/invernadero/',
        views.invernadero,
        name='ajax-invernadero'
    ),
    path(
        'perfil/<slug:pk>/',
        views.PerfilDetailView.as_view(),
        name='perfil'
    ),
    path(
        'sign-out/',
        views.SignOutView.as_view(),
        name='sign-out'
    ),
    path(
        'cultivos/',
        views.CultivosListView.as_view(),
        name='cultivos'
    )
]

urlpatterns = format_suffix_patterns(urlpatterns)