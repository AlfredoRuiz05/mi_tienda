# tienda_lr/urls.py
from django.contrib import admin
from django.urls import path, include
from apps.productos.views import home
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='pagina_principal'),  # Página principal
    path('usuarios/', include('apps.usuarios.urls')),  # Ahora con prefijo
    path('productos/', include('apps.productos.urls')),  # También con prefijo
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




