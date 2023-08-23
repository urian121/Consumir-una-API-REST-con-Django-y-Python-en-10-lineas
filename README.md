# 🔥 Consumir una API con Django y Python 🐍 😯

#### Paso a paso:

Crear un entorno virtual

    `virtualenv env`
      https://pypi.org/project/virtualenv/

- Activar el entorno virtual

  En windows: `. env/Script/activate`
  En Mac: `. env/bin/activate`

- Listar Paquetes
  `pip freeze`

- Instalar Django en mi entorno virtual
  `pip install django`

Verificar la instalacion con
`pip freeze`

- Crear un projecto en Django
  `django-admin startproject  project_core .`
  el punto al final le indica que cree el proyecto en el directorio actual

-     Correr el proyecto creado

  `python manage.py runserver`
  👉Revisar la consola y visitar la URL http://127.0.0.1:8000
  Si deseas cambiar el puerto por donde se esta desplegando el proyecto
  `python manage.py runserver 8080`

- Creamos una aplicacion en el proyecto de Django
  `python manage.py startapp api_django`

- Instalar el paquete `requests` para hacer solicitudes HTTP
  `pip install requests`
  `https://pypi.org/project/requests/`
  Volvemos a listar los paquete de nuestro proyecto para verificar que si este instalado el paquete requests `pip list`

### Nota: si no quieres hacer ninguno de los pasos anteriores puedes instalar todas las dependencias del proyecto solo ejecutando el archivo requirement.txt `pip install -r requirements.txt`

-

Ahora instalar la aplicacion ya creada en nuestro proyecto `project_core` para esto debemos ir al archivo settings.py y en la parte de `INSTALLED_APPS` en esa lista agregar la aplicacion.

    INSTALLED_APPS = [
    '-------',
    'api',
    ]

Ir al archivo views.py de para definir la funcion que realizara la consulta a la API
`

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
        `

Creamos el archivo urls.py en nuestra aplicacion, donde importamos desde view la funcion creada para hacer la solicitud a dicha API
`

    from django.urls import path
    # Importando desde views.py la funcion obtener_productos
    from .views import obtener_productos

    urlpatterns = [
    	path('productos/', obtener_productos, name='obtener_productos'),
    ]`

Ahora vamos a el archivo urls.py de nuestro proyecto para incluir en el archivo urls.py de nuestra aplicacion
`

    from django.urls import path, include
    urlpatterns = [
    	path('admin/', admin.site.urls),
    	# Incluyendo mi aplicacion api_django
    	path('', include('api_django.urls')),
    ]`

Por ultimo creamos una carpeta en nuestra aplicacion que se llame `templates` alli creamos un archivo `index.html` y recorremos toda la data que esta llegando, asi:

`

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
    {% endfor %}`

Para finalizar solo devemos correr el proyecto de nuevo con:
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
