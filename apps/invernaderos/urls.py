from django.urls import path
from . import views

urlpatterns = [
    path('sign-in/', views.SignInView.as_view(), name='sign-in'),
    path('', views.InvernaderosListView.as_view(), name='invernaderos'),
    path('ajax/borrar/invernadero/', views.borrar_invernadero, name='ajax-borrar-invernadero'),
    path('ajax/ver/invernadero', views.editar_invernadero, name='ajax-ver-invernadero'),
    path('perfil/<slug:pk>/', views.PerfilDetailView.as_view(), name='perfil'),
    path('sign-out/', views.SignOutView.as_view(), name='sign-out')
]