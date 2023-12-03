from django.urls import path
# Importando desde views.py la funcion obtener_productos()
from .views import getAPI, obtener_productos

urlpatterns = [
    path('', obtener_productos, name='obtener_productos'),
    path('api/', getAPI, name='getAPI'),
]
