from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_request, name="Login"),
    path("logout/", views.logout_request, name="Logout"),
    # Voluntarios
    path("voluntarios/", views.voluntarios, name="Voluntarios"),
    path("nuevo_voluntario/", views.nuevo_voluntario, name="NuevoVoluntario"),
    path("voluntario/<id>", views.ver_voluntario, name="VerVoluntario"),
    path("voluntario/editar/<id>", views.editar_voluntario, name="EditarVoluntario"),  
    path("voluntario/eliminar/<id>", views.eliminar_voluntario, name="EliminarVoluntario"),
    # Facilitadores
    path("facilitadores/", views.facilitadores, name="Facilitadores"),
    path("nuevo_facilitador/", views.nuevo_facilitador, name="NuevoFacilitador"),
    path("facilitador/<id>", views.ver_facilitador, name="VerFacilitador"),
    path("facilitador/editar/<id>", views.editar_facilitador, name="EditarFacilitador"),  
    path("facilitador/eliminar/<id>", views.eliminar_facilitador, name="EliminarFacilitador"),
]
