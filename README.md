# 🔥 Consumir una API con Django y Python 🐍 😯

###### La Manera Más Sencilla de Consumir un Servicio Web con Python es con la Biblioteca Requests ( para hacer solicitudes HTT)

    Crear entorno virtual con Python
     `virtualenv env`

    Activar ambiente virtual en windows
    ` . env/scripts/activate`

- Para desactivar dicho entorno virtual
  `deactivate`

  Instalar Djando desde Pip en nuestro entorno virtual.
  `pip install Django`

  Crear el proyecto con Djando
  `django-admin startproject Project_API .`
  El punto . es crucial porque le dice al script que instale Django en el directorio actual,
  para el cual el punto sirve de abreviatura


    Ya en este punto se puede correr el proyecto 'Project_API' que a creado Django,
    `python manage.py runserver`


    Visitar la URL http://127.0.0.1:8000/

    Instalar la Biblioteca (libreria, paquete) Requests
    pip install requests


    Crear mi primera aplicación en Django MyAPI
    `python manage.py startapp MyAPI`

8. Instalar nuestra aplicación (MyAPI) ya creada en nuestro proyecto
   ` archivo settings.py`
   INSTALLED_APPS = [
   ----,
   'MyAPI',
   ]`

   Crear el archivo urls.py en nuestra aplicación creada (MyAPI)
   from django.urls import path

   # Importando desde views.py la funcion obtener_productos

   from .views import obtener_productos

   urlpatterns = [
   path('productos/', obtener_productos, name='obtener_productos'),
   ]

   Conectar nuestra aplicación ir a uls.py este archivo esta en el proyecto
   from django.urls import path, include
   urlpatterns = [
   path('admin/', admin.site.urls),

   # registering MyAPI application's urls in project

   path('MyAPI/', include('MyAPI.urls')),
   ]

   Correr el proyecto creado en Python & Django
   `python manage.py runserver`

👉Revisar la consola y visitar la
URL http://127.0.0.1:8000

### Codigo

![](https://raw.githubusercontent.com/urian121/imagenes-proyectos-github/master/creando-solicitud-api-con-djando.png)

### Resultado Final 😯

![](https://raw.githubusercontent.com/urian121/imagenes-proyectos-github/master/consumir-api-con-Django-Urian-viera.png)

### Expresiones de Gratitud 🎁

    ¡Comparte este emocionante proyecto con los demás! 📢
    Apóyanos con una cerveza 🍺 o un reconfortante café ☕
    Contribuye a través de PayPal: iamdeveloper86@gmail.com
    Expresa tus agradecimientos en público 🤓 ¡Te lo agradeceremos enormemente!

## ¡No dejes pasar la oportunidad de SUSCRIBIRTE! 👍
