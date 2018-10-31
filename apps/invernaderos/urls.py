from django.urls import path
from . import views

urlpatterns = [
    path('sign-in/', views.SignInView.as_view(), name='sign-in'),
    path('sign-out/', views.SignOutView.as_view(), name='sign-out'),
    path('', views.InicioView.as_view(), name='invernaderos')
]