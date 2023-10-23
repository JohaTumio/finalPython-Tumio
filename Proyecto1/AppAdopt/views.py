from django.shortcuts import render
from django.views.generic import ListView 
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from AppAdopt.models import Animal, Cuidador, Profesional, Adopcion
from .forms import BuscaAnimalForm, BuscaProfesionalForm, AdopcionForm
from django.contrib.auth.mixins import LoginRequiredMixin


class InicioView(TemplateView):
    template_name = "AppAdopt/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["animalForm"] = BuscaAnimalForm()
        context["profesionalForm"] = BuscaProfesionalForm()
        return context

    def post(self, request, *args, **kwargs):
        animales = []
        profesionales = []

        animalForm = BuscaAnimalForm(request.POST)
        if animalForm.is_valid():
            informacion_animal = animalForm.cleaned_data
            opcion = informacion_animal.get('opcion')
            if opcion == 'nombre':
                animales = Animal.objects.filter(nombre__icontains=informacion_animal["animal"])
            elif opcion == 'especie':
                animales = Animal.objects.filter(especie__icontains=informacion_animal["animal"])

        profesionalForm = BuscaProfesionalForm(request.POST)
        if profesionalForm.is_valid():
            informacion_profesional = profesionalForm.cleaned_data
            opcion = informacion_profesional.get('opcion')
            if opcion == 'nombre':
                profesionales = Profesional.objects.filter(nombre__icontains=informacion_profesional["profesional"])
            elif opcion == 'especialidad':
                profesionales = Profesional.objects.filter(especialidad__icontains=informacion_profesional["profesional"])

        return render(request, "AppAdopt/resBusForm.html", {"animales": animales, "profesionales": profesionales, "animalForm": animalForm, "profesionalForm": profesionalForm})


#Animal
class AnimalView(ListView):
    model = Animal
    template_name = "AppAdopt/animal_list.html"

class AnimalDetView(DetailView):
    model = Animal
    template_name = "AppAdopt/animal_detalle.html"

class AnimalNuevoView(LoginRequiredMixin,CreateView):
    model = Animal
    template_name = "AppAdopt/formulario.html"
    success_url = reverse_lazy("AnimalList")
    fields = ["nombre", "sexo", "edad", "tamaño", "raza", "caracteristicas", "cuidados_especiales", "especie", "imagen"]

    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super(AnimalNuevoView, self).get(request, *args, **kwargs)
        else:
            return render(request, "AppAdopt/acceso_restringido.html")

class AnimalEditView(LoginRequiredMixin,UpdateView):
    model = Animal
    template_name = "AppAdopt/form_edit.html"
    success_url = reverse_lazy("AnimalList")
    fields = ["nombre", "sexo", "edad", "tamaño", "raza", "caracteristicas", "cuidados_especiales", "especie"]

    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super(AnimalEditView, self).get(request, *args, **kwargs)
        else:
            return render(request, "AppAdopt/acceso_restringido.html")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["return_url"] = reverse_lazy("AnimalList")
        return context

class AnimalElimView(LoginRequiredMixin,DeleteView):
    model = Animal
    success_url = reverse_lazy("AnimalList")
    template_name = "AppAdopt/animal_confirm_delete.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super(AnimalElimView, self).get(request, *args, **kwargs)
        else:
            return render(request, "AppAdopt/acceso_restringido.html")

#Profesional

class ProfesionalView(ListView):
    model = Profesional
    template_name = "AppAdopt/prof_list.html"

class ProfesionalDetView(DetailView):
    model = Profesional
    template_name = "AppAdopt/prof_detalle.html"    

class ProfesionalNuevoView(LoginRequiredMixin,CreateView):
    model = Profesional
    template_name = "AppAdopt/formulario.html"
    success_url = reverse_lazy("ProfList")
    fields = ["nombre", "apellido", "edad", "email", "especialidad"]  

    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super(ProfesionalNuevoView, self).get(request, *args, **kwargs)
        else:
            return render(request, "AppAdopt/acceso_restringido.html")

class ProfesionalEditView(LoginRequiredMixin,UpdateView):
    model = Profesional
    template_name = "AppAdopt/form_edit.html"
    success_url = reverse_lazy("ProfList")
    fields = ["nombre", "apellido", "edad", "email", "especialidad"]

    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super(ProfesionalEditView, self).get(request, *args, **kwargs)
        else:
            return render(request, "AppAdopt/acceso_restringido.html")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["return_url"] = reverse_lazy("ProfList")
        return context

class ProfesionalElimView(LoginRequiredMixin,DeleteView):
    model = Profesional
    success_url = reverse_lazy("ProfList")
    template_name = "AppAdopt/profesional_confirm_delete.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super(ProfesionalElimView, self).get(request, *args, **kwargs)
        else:
            return render(request, "AppAdopt/acceso_restringido.html")

#Cuidador
class CuidadorView(ListView):
    model = Cuidador
    template_name = "AppAdopt/cuidador_list.html"

class CuidadorDetView(DetailView):
    model = Cuidador
    template_name = "AppAdopt/cuidador_detalle.html"

class CuidadorNuevoView(LoginRequiredMixin,CreateView):
    model = Cuidador
    template_name = "AppAdopt/formulario.html"
    success_url = reverse_lazy("CuidadorList")
    fields = ["nombre", "apellido", "edad", "email", "direccion"]

    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super(CuidadorNuevoView, self).get(request, *args, **kwargs)
        else:
            return render(request, "AppAdopt/acceso_restringido.html")

class CuidadorEditView(LoginRequiredMixin,UpdateView):
    model = Cuidador
    template_name = "AppAdopt/form_edit.html"
    success_url = reverse_lazy("CuidadorList")
    fields = ["nombre", "apellido", "edad", "email", "direccion"]

    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super(CuidadorEditView, self).get(request, *args, **kwargs)
        else:
            return render(request, "AppAdopt/acceso_restringido.html")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["return_url"] = reverse_lazy("CuidadorList")
        return context

class CuidadorElimView(LoginRequiredMixin,DeleteView):
    model = Cuidador
    success_url = reverse_lazy("CuidadorList")
    template_name = "AppAdopt/cuidador_confirm_delete.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super(CuidadorElimView, self).get(request, *args, **kwargs)
        else:
            return render(request, "AppAdopt/acceso_restringido.html")    


class AdoptaView(LoginRequiredMixin, CreateView):
    template_name = "AppAdopt/formulario.html"
    model = Adopcion
    form_class = AdopcionForm
    success_url = reverse_lazy("Confirm_adop")

    def form_valid(self, form):
        adopcion = form.save(commit=False)
        adopcion.save()
        animal_nombre = adopcion.animal.nombre
        return render(self.request, 'AppAdopt/confirmacion_adopcion.html', {'animal_nombre': animal_nombre})


