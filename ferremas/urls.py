from django.urls import path
from . import views

urlpatterns = [
    path('inicio', views.inicio, name='inicio'),
    path('crud_herramientas/', views.crud_herramientas, name='crud_herramientas'),
    path('', views.iniciar_sesion, name='iniciar_sesion'),
    path('registro/', views.registro, name='registro'),  # Asumiendo que ya tienes login
]
