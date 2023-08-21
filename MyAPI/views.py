from django.shortcuts import render
# Importando Libreria Requests para hacer solicitudes HTTP
import requests


def obtener_productos(request):
    # URL de productos
    URL_API = "https://fakestoreapi.com/products"

    # Realizar la solicitud GET a la API
    response = requests.get(URL_API)

    if response.status_code == 200:
        productos = response.json()
        """for producto in productos:
            print(producto)
        """
    else:
        # Lista vacia
        productos = []

    return render(request, 'index.html', {'productos': productos})