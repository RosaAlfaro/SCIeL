from django.urls import path
from . import views

urlpatterns = [
    path('', views.InvernaderosListView.as_view(), name='index'),
    path('invernaderos/', views.index, name='invernaderos'),
    path('perfil/<slug:pk>/', views.PerfilDetailView.as_view(), name='perfil'),
    path('sign-in/', views.SignInView.as_view(), name='sign-in'),
    path('sign-out/', views.SignOutView.as_view(), name='sign-out'),
    path('ajax/borrar-invernadero/', views.borrar_invernadero, name='ajax-borrar-invernadero')
]