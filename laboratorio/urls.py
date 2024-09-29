from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index, name='index'),  # Ruta para la página de inicio
    path('', views.laboratorio_list, name='laboratorio_list'),
    path('crear/', views.laboratorio_create, name='laboratorio_create'),
    path('editar/<int:pk>/', views.laboratorio_update, name='laboratorio_update'),
    path('eliminar/<int:pk>/', views.laboratorio_delete, name='laboratorio_delete'),

      # URLs para Productos
    path('productos/', views.producto_list, name='producto_list'),
    path('productos/nuevo/', views.producto_create, name='producto_create'),
    path('productos/editar/<int:pk>/', views.producto_update, name='producto_update'),
    path('productos/eliminar/<int:pk>/', views.producto_delete, name='producto_delete'),

    # URLs para Directores Generales
    path('directores/', views.directorgeneral_list, name='directorgeneral_list'),
    path('directores/nuevo/', views.directorgeneral_create, name='directorgeneral_create'),
    path('directores/editar/<int:pk>/', views.directorgeneral_update, name='directorgeneral_update'),
    path('directores/eliminar/<int:pk>/', views.directorgeneral_delete, name='directorgeneral_delete'),

]
