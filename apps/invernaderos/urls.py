from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('logut/', views.SignOutView.as_view(), name='logout'),
    path('invernaderos/', views.InicioView.as_view(), name='invernaderos')
]