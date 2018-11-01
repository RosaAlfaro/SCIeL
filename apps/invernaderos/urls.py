from django.urls import path
from . import views

urlpatterns = [
    path('', views.InicioView.as_view(), name='index'),
    path('invernaderos/', views.index, name='invernaderos'),
    path('sign-in/', views.SignInView.as_view(), name='sign-in'),
    path('sign-out/', views.SignOutView.as_view(), name='sign-out'),
]