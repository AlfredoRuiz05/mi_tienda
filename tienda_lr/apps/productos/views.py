from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto  # si ya lo tenés creado
from django.contrib.auth.decorators import login_required, user_passes_test

from decimal import Decimal

def home(request): 
    productos = Producto.objects.all()

    for p in productos:
        descuento_decimal = Decimal(p.descuento) / Decimal('100')
        p.precio_final = p.precio * (Decimal('1.0') - descuento_decimal)

    return render(request, 'home.html', {'productos': productos})



def es_admin(user):
    return user.is_superuser  # o user.is_staff si preferís

@login_required
@user_passes_test(es_admin)
def panel_admin(request):
    return render(request, 'admin_panel.html')


def es_admin(user):
    return user.is_superuser

@login_required
@user_passes_test(es_admin)
def agregar_producto(request):
    if request.method == 'POST':
        nombre = request.POST.get('productName')
        precio = request.POST.get('productPrice')
        descuento = request.POST.get('discountAmount') or 0
        imagen = request.FILES.get('productImage')

        producto = Producto(nombre=nombre, precio=precio, descuento=descuento, imagen=imagen)
        producto.save()
        return redirect('productos:panel_admin')

    return render(request, 'agregar_producto.html')

@login_required
def modificar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    errores = []

    if request.method == 'POST':
        nombre = request.POST.get('productName', '').strip()
        precio = request.POST.get('productPrice')
        descuento = request.POST.get('discountAmount') or '0'
        imagen = request.FILES.get('productImage')

        # Validaciones
        if not nombre:
            errores.append("El nombre del producto no puede estar vacío.")
        
        try:
            precio = float(precio)
            if precio <= 0:
                errores.append("El precio debe ser mayor a cero.")
        except ValueError:
            errores.append("El precio no es un número válido.")
        
        try:
            descuento = float(descuento)
            if descuento < 0 or descuento > 100:
                errores.append("El descuento debe estar entre 0 y 100.")
        except ValueError:
            errores.append("El descuento no es un número válido.")

        # Si no hay errores, guardar
        if not errores:
            producto.nombre = nombre
            producto.precio = precio
            producto.descuento = descuento
            if imagen:
                producto.imagen = imagen
            producto.save()
            return redirect('productos:panel_admin')

    return render(request, 'modificar_producto.html', {
        'producto': producto,
        'errores': errores
    })

@login_required
def panel_modificar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'panel_modificar_productos.html', {'productos': productos})

@login_required
def panel_eliminar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'panel_eliminar_productos.html', {'productos': productos})

@login_required
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    producto.delete()
    return redirect('productos:panel_eliminar_productos')
