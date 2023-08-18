from django.urls import path
# Importando desde views.py la funcion obtener_productos
from .views import obtener_productos

urlpatterns = [
    path('productos/', obtener_productos, name='obtener_productos'),
]
