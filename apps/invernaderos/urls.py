from django.urls import path
from apps.invernaderos.views import CultivosShow
from . import views

urlpatterns = [
    path('', views.InvernaderosListView.as_view(), name='index'),
    path('invernaderos/', views.index, name='invernaderos'),
    path('perfil/<slug:pk>/', views.PerfilDetailView.as_view(), name='perfil'),
    path('sign-in/', views.SignInView.as_view(), name='sign-in'),
    path('sign-out/', views.SignOutView.as_view(), name='sign-out'),
<<<<<<< HEAD
    path('cultivos/', CultivosShow.as_view(), name='cultivos'),
=======
    path('ajax/borrar/invernadero/', views.borrar_invernadero, name='ajax-borrar-invernadero')
>>>>>>> 255006ad7352e18441501c90026f1e48720009ba
]