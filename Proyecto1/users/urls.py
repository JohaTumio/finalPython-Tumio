from django.urls import path
from users import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', views.login_request, name="Login"),
    path('registro/', views.registro, name="Registro"),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name="Logout"),
    path('editar/', views.EditarUser, name="Editar"),
    path('cambiar-pass/', views.cambiar_pass, name='Cambiar_pass'),
]