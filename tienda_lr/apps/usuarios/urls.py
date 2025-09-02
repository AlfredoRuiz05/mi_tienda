
# apps/usuarios/urls.py
from django.urls import path
from . import views
app_name = "usuarios"
urlpatterns = [
    path('login/', views.iniciar_sesion, name='iniciar_sesion'),
    path('registrarse/', views.registrar_usuario, name='registrarse'),
]
