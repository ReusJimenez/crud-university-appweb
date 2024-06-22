from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar, name='listar'),
    path('agregar/', views.agregar, name='agregar'),
    path('editar/<str:codigo_alumno>/', views.editar, name='editar'),
    path('eliminar/<str:codigo_alumno>/', views.eliminar, name='eliminar'),
]