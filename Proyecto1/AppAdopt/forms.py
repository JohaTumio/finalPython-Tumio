from django import forms
from .models import Adopcion

class BuscaAnimalForm(forms.Form):
    OPCIONES_BUSQUEDA = (
        ('nombre', 'Nombre'),
        ('especie', 'Especie'),
    )
    animal = forms.CharField(label='Buscar', max_length=100)
    opcion = forms.ChoiceField(label='Opción de búsqueda', choices=OPCIONES_BUSQUEDA)

class BuscaProfesionalForm(forms.Form):
    OPCIONES_BUSQUEDA = (
        ('nombre', 'Nombre'),
        ('especialidad', 'Especialidad'),
    )
    profesional = forms.CharField(label='Buscar', max_length=100)
    opcion = forms.ChoiceField(label='Opción de búsqueda', choices=OPCIONES_BUSQUEDA)

class AdopcionForm(forms.ModelForm):
    class Meta:
        model = Adopcion
        fields = ["animal", "nombre", "apellido", "edad", "direccion", "telefono", "email"]
