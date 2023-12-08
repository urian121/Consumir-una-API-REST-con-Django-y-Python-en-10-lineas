from django.shortcuts import render, HttpResponse
# Importando Libreria Requests para hacer solicitudes HTTP
import requests


def getAPI(request):
    # URL de productos
    URL_API = "https://jsonplaceholder.typicode.com/albums"

    # Realizar la solicitud GET a la API
    response = requests.get(URL_API)

    if response.status_code == 200:
        # se utiliza el método json() para extraer los datos en formato JSON de la respuesta y se almacenan en la variable productos
        productos = response.json()
        """
        for producto in productos:
            print(producto)
        """
        return HttpResponse(productos) or []


def obtener_productos(request):
    URL_API = "https://fakestoreapi.com/products"
    try:
        # Intenta realizar la solicitud GET a la API
        response = requests.get(URL_API)
        if response.status_code == 200:
            # se utiliza el método json() para extraer los datos en formato JSON de la respuesta y se almacenan en la variable productos
            productos = response.json()
        else:
            # En caso de un código de respuesta no exitoso, manejar de acuerdo a tus necesidades
            print(f"Error en la solicitud: {response.status_code}")
            productos = []
    except requests.RequestException as e:
        # Manejar errores de solicitud, por ejemplo, problemas de red
        print(f"Error en la solicitud: {e}")
        productos = []

    return render(request, 'index.html', {'productos': productos})
