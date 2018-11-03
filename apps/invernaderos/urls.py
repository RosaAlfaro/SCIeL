from django.urls import path
from apps.invernaderos.views import CultivosShow
from . import views

urlpatterns = [
    path('', views.InicioView.as_view(), name='index'),
    path('invernaderos/', views.index, name='invernaderos'),
    path('sign-in/', views.SignInView.as_view(), name='sign-in'),
    path('sign-out/', views.SignOutView.as_view(), name='sign-out'),
    path('cultivos/', CultivosShow.as_view(), name='cultivos'),
]