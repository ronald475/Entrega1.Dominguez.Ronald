from django.urls import path
from . import views


urlpatterns = [
    path("clases/", views.clases, name="Clases"),
    path("nueva_clase/", views.nueva_clase, name="NuevaClase"),
    path("clase/<id>", views.ver_clase, name="VerClase"),
    path("clase/editar/<id>", views.editar_clase, name="EditarClase"),
    path("clase/eliminar/<id>", views.eliminar_clase, name="EliminarClase"),


    path('buscar/<tema>/', views.buscar_tema, name="BuscarClase"),
    path('buscar/resultados', views.resultados_esc, name="BuscarResultadosCla"),
]
