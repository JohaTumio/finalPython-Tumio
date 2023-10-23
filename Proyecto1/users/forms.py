from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm


class UserLogin(AuthenticationForm):
        error_messages = {
        'invalid_login': [],
    }
        username = forms.CharField(
            label="Nombre",
            widget=forms.TextInput(attrs={'placeholder': 'Ingrese su usuario'}),
        )
        password = forms.CharField(
            label="Contraseña",
            widget=forms.PasswordInput(attrs={'placeholder': 'Ingrese su contraseña'}),
        )

class UserRegistroForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Ingrese su email'}))
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'placeholder': 'Ingrese su contraseña'}))
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput(attrs={'placeholder': 'Repetir contraseña'}))
    
    username = forms.CharField(
        label="Nombre",
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese su nombre'}),
        error_messages={'unique': 'Este nombre de usuario ya está en uso.'}
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}


class UserEditProfileForm(forms.Form):
    email = forms.EmailField(label="Ingrese su email:")
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido:")
    imagen = forms.ImageField(required=True)


class CambiarContraseñaForm(PasswordChangeForm):
    class Meta:
        model = User

    def __init__(self, *args, **kwargs):
        super(CambiarContraseñaForm, self).__init__(*args, **kwargs)

        self.fields['old_password'].label = "Contraseña actual"
        self.fields['new_password1'].label = "Nueva contraseña"
        self.fields['new_password2'].label = "Confirmar nueva contraseña"
        
        for field_name in self.fields:
            self.fields[field_name].help_text = ""
        


class CustomAuthenticationForm(AuthenticationForm):
    error_messages = {
        'invalid_login': [],
        'username': {'required': 'Ingrese un nombre de usuario.'},
        'non_field_errors': [],
    }
    username = forms.CharField(
        label="Nombre",
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese su usuario'}),
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={'placeholder': 'Ingrese su contraseña'}),
    ) 