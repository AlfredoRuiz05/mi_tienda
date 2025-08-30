from django.urls import path
from . import views
app_name = 'productos'
urlpatterns = [
    path('admin-panel/', views.panel_admin, name='panel_admin'),
    # Acá podés agregar más rutas después: crear_producto, editar, eliminar, etc.
    path('admin-panel/agregar-producto/', views.agregar_producto, name='agregar_producto'),
    path('admin-panel/modificar-productos/', views.panel_modificar_productos, name='panel_modificar_productos'),
    path('modificar/<int:producto_id>/', views.modificar_producto, name='modificar_producto'),
    path('admin-panel/eliminar-productos/', views.panel_eliminar_productos, name='panel_eliminar_productos'),
    path('admin-panel/eliminar-producto/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),

]
