from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from users.forms import UserLogin, UserRegistroForm,CambiarContraseñaForm, UserEditProfileForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from users.models import Imagen
from django.contrib.auth.decorators import login_required


def login_request(request):
    if request.method == 'POST':
        form = UserLogin(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contrasenia)
            if user is not None:
                login(request, user)
                next_url = request.GET.get('next')
                if next_url:
                    return redirect(next_url)
                else:
                    messages.success(request, f"Bienvenido/a {usuario}")
                    return redirect("Inicio")
        else:
            messages.error(request, "Credenciales incorrectas, intente nuevamente.")
    
    form = UserLogin()
    return render(request, "users/login.html", {"form": form})


def registro(request):
    if request.method == 'POST':
        form = UserRegistroForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            messages.success(request, f"Bienvenido/a {username}. Usuario creado con éxito!")
            return redirect("Inicio")
        else:
            form.errors.clear()
            messages.error(request, "Datos incorrectos o usuario ya en uso intente nuevamente")
    else:
        form = UserRegistroForm()
    return render(request, "users/registro.html", {"form": form})


@login_required
def EditarUser(request):
    usuario = request.user
    if request.method == 'POST':
        miFormulario = UserEditProfileForm(request.POST, request.FILES)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']
            usuario.save()

            try:
                avatar = Imagen.objects.get(user=usuario)
            except Imagen.DoesNotExist:
                avatar = Imagen(user=usuario, imagen=informacion["imagen"])
                avatar.save()
            else:
                avatar.imagen = informacion["imagen"]
                avatar.save()

            return redirect('Inicio')
    else:
        datos = {
            'first_name': usuario.first_name,
            'last_name': usuario.last_name,
            'email': usuario.email
        }
        miFormulario = UserEditProfileForm(initial=datos)
    return render(request, "users/edit.html", {"mi_form": miFormulario, "usuario": usuario})


def cambiar_pass(request):
    if request.method == 'POST':
        form = CambiarContraseñaForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Contraseña actualizada con éxito.')
            return redirect('Inicio')
        else:
            messages.error(request, 'Hubo un error al cambiar la contraseña. Por favor, intenta de nuevo.')

    form = CambiarContraseñaForm(request.user)
    return render(request, 'users/cambiar_contraseña.html', {'form': form})



