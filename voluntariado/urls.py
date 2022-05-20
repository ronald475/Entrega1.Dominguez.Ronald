from django.urls import path
from . import views


urlpatterns = [
    path("voluntarios/", views.voluntarios, name="Voluntarios"),
    path("nuevo_voluntario/", views.nuevo_voluntario, name="NuevoVoluntario"),
    path("voluntario/<id>", views.ver_voluntario, name="VerVoluntario"),
    path("voluntario/editar/<id>", views.editar_voluntario, name="EditarVoluntario"),  
    path("voluntario/eliminar/<id>", views.eliminar_voluntario, name="EliminarVoluntario"),

    path("facilitadores/", views.facilitadores, name="Facilitadores"),
    path("nuevo_facilitador/", views.nuevo_facilitador, name="NuevoFacilitador"),
    path("facilitador/<id>", views.ver_facilitador, name="VerFacilitador"),
    path("facilitador/editar/<id>", views.editar_facilitador, name="EditarFacilitador"),  
    path("facilitador/eliminar/<id>", views.eliminar_facilitador, name="EliminarFacilitador"),

    path('buscar/<nombre>/', views.buscar_voluntario, name="BuscarVoluntario"),
    path('buscar/resultados', views.resultados_vol, name="BuscarResultadosVol"),
]
