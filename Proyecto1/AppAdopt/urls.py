from django.urls import path
from AppAdopt import views

urlpatterns = [
    path('', views.InicioView.as_view(), name="Inicio"),
    path('adopta/', views.AdoptaView.as_view(), name="Adopta"),
]

#Animal
urlpatterns += [
    path('animal_list/', views.AnimalView.as_view(), name="AnimalList"),
    path('animal_detalle/<int:pk>/', views.AnimalDetView.as_view(), name='AnimalDetalle'),
    path('animal_nuevo/', views.AnimalNuevoView.as_view(), name='AnimalNuevo'),
    path('animal_editar/<int:pk>', views.AnimalEditView.as_view(), name='AnimalEdit'),
    path('animal_eliminar/<int:pk>', views.AnimalElimView.as_view(), name='AnimalEliminar'),
]

#Profesional
urlpatterns += [
    path('prof_list/', views.ProfesionalView.as_view(), name="ProfList"),
    path('prof_detalle/<int:pk>/', views.ProfesionalDetView.as_view(), name='ProfDetalle'),
    path('prof_nuevo/', views.ProfesionalNuevoView.as_view(), name='ProfNuevo'),
    path('prof_editar/<int:pk>', views.ProfesionalEditView.as_view(), name='ProfEdit'),
    path('prof_eliminar/<int:pk>', views.ProfesionalElimView.as_view(), name='ProfEliminar'),    
]

#Cuidador
urlpatterns += [
    path('cuidador_list/', views.CuidadorView.as_view(), name="CuidadorList"),
    path('cuidador_detalle/<int:pk>/', views.CuidadorDetView.as_view(), name='CuidadorDetalle'),
    path('cuidador_nuevo/', views.CuidadorNuevoView.as_view(), name='CuidadorNuevo'),
    path('cuidador_editar/<int:pk>', views.CuidadorEditView.as_view(), name='CuidadorEdit'),
    path('cuidador_eliminar/<int:pk>', views.CuidadorElimView.as_view(), name='CuidadorEliminar'),    
]
