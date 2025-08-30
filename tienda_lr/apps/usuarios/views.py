from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

def iniciar_sesion(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('pagina_principal')  # o la url que quieras
        else:
            error = "Este usuario no está registrado o la contraseña es incorrecta."

    return render(request, 'login.html', {'error': error})



# Obtener el modelo de usuario personalizado
User = get_user_model()

def registrar_usuario(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Verificar si el usuario ya existe
        if User.objects.filter(username=username).exists():
            messages.error(request, "El nombre de usuario ya existe.")
            return render(request, 'registro.html')

        # Crear el nuevo usuario
        User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, f'Usuario {username} creado con éxito.')
        return redirect('iniciar_sesion')

    return render(request, 'registro.html')

