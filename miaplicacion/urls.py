from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('aprendiz/', views.aprendices, name='aprendiz'),
    path('formulario/', views.formulario, name='formulario'),
    path('eliminar/<int:idaprendiz>/', views.eliminar, name='eliminar'),
    path('modificar/<int:idaprendiz>/', views.modificar, name='modificar'),
]
