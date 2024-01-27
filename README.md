# 🔥 Consumir una API con Django y Python 🐍 😯

###### 1. Crear un entorno virtual, hay muchas formas

    Opción 1: Crear entorno virtual con el paquete virtualenv,
    puedes instalarlo de forma global en el sistema atraves de https://pypi.org/project/virtualenv/

    `pip install virtualenv` #Instalar paquete virtualenv
    `virtualenv --version` #Version
    `virtualenv env` #Crear entorno con el paquete virtualenv

    Opción 2: Crear un entorno virtual con el paquete que ya viene por defecto en las ultimas versiones de Python
    `python -m venv env` o `python3 -m venv env`

###### 2. Activar ambiente virtual

    . env/Script/activate #Activar ambiente desde Windows
    . env/bin/activate  #Activar desde la Mac
    deactivate #Desactivar mi entorno virtual

###### 3. Instalar Django desde el manejador de paquete de Python Pip

    `pip install Django`
     Nota: para instalar Django en una version especifica
    `pip install Django==4.2.4`
    `python3 -m django --version`  #Vrsion instalada de Django

###### 4. Instalar el paquete `requests` para hacer solicitudes HTTP

     https://pypi.org/project/requests/
     `pip install requests`
     Verificar todos los paquetes instalados en el proyecto
     `pip freeze`

###### 5. Crear el proyecto con Djando

    `django-admin startproject api_django .`
     El punto . es crucial le dice al script que instale Django en el directorio actual

     Ya en este punto se puede correr el proyecto que a creado Django,
     python manage.py runserver

###### 6. Correr el proyecto creado con Django

     `python manage.py runserver`
     👉Revisar la consola y visitar la URL http://127.0.0.1:8000
     Si deseas cambiar el puerto por donde se esta desplegando el proyecto
     `python manage.py runserver 8080`

### Nota: si no deseas hacer ninguno de los pasos anteriores puedes instalar todas las dependencias del proyecto solo ejecutando el archivo requirements.txt

`pip install -r requirements.txt`

###### 7. Crear mi primera aplicación en Django

`python manage.py startapp api`

###### 8. Instalar nuestra aplicación (MyAPI) ya creada en el proyecto

archivo settings.py

INSTALLED_APPS = [
----,
'MyAPI',
]

##### 9. Define la vista en el views.py

    # Importando Libreria Requests para hacer solicitudes HTTP
    import requests

    def obtener_productos(request):
    	# URL de productos
    	URL_API = "https://fakestoreapi.com/products"

    	# Realizar la solicitud GET a la API
    	response = requests.get(URL_API)

    	if response.status_code == 200:
    		productos = response.json()
    			for producto in productos:
    				print(producto)
    	else:
    		# Lista vacia
    		productos = []

##### 10. Configurar el archivo urls.py de la aplicación

    from django.urls import path
    # Importando desde views.py la funcion obtener_productos
    from .views import obtener_productos

    urlpatterns = [
    	path('productos/', obtener_productos, name='obtener_productos'),
    ]

##### 11. Incluimos el archivo urls.py de nuestra aplicación en nuestro proyecto api_django

    from django.urls import path, include
    urlpatterns = [
    	path('admin/', admin.site.urls),
    	# Incluyendo mi aplicacion api_django
    	path('', include('api_django.urls')),
    ]

##### 12. Creamos la carpeta templates y dentro un index.html para pintar la data que responde la API

##### Codigo del index.html

    {% for producto in productos %}
        <div class="product-card">
        <div class="product-tumb">
          <img src="{{ producto.image}}" alt="{{ producto.title }}" />
        </div>
        <div class="product-details">
          <h4>{{ producto.title }}</h4>
          <div class="product-bottom-details">
          <div class="product-price">Precio: ${{ producto.price }}</div>
          </div>
          <p>{{ producto.description }}</p>
        </div>
        </div>
    {% endfor %}

##### Para finalizar solo debemos correr el proyecto de nuevo con:

    `python manage.py runserver`

El resultado final seria esto:

![](https://raw.githubusercontent.com/urian121/imagenes-proyectos-github/master/consumir-api-con-Django-Urian-viera.png)

![](https://raw.githubusercontent.com/urian121/imagenes-proyectos-github/master/creando-solicitud-api-con-djando.png)

### Expresiones de Gratitud 🎁

    ¡Comparte este emocionante proyecto con los demás! 📢
    Apóyanos con una cerveza 🍺 o un reconfortante café ☕
    Contribuye a través de PayPal: iamdeveloper86@gmail.com
    Expresa tus agradecimientos en público 🤓 ¡Te lo agradeceremos enormemente!

## ¡No dejes pasar la oportunidad de SUSCRIBIRTE! 👍
