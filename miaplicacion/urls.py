from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('aprendiz/', views.aprendices, name='aprendiz'),
    path('materia/', views.materias, name='materia'),
    path('formulario/', views.formulario, name='formulario'),
    path('formulario2/', views.formulariodos, name='formulario2'),
    path('eliminar/<int:idaprendiz>/', views.eliminar, name='eliminar'),
    path('modificar/<int:idaprendiz>/', views.modificar, name='modificar'),
    path('eliminarmat/<int:idmateria>/', views.eliminarmat, name='eliminarmat'),
    path('modificarmat/<int:idmateria>/', views.modificarmat, name='modificarmat'),
]
