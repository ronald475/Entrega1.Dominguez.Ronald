from django.urls import path
from . import views


urlpatterns = [
    path("nueva_clase/", views.nueva_clase, name="NuevaClase"),
    path('buscar/<tema>/', views.buscar_tema, name="BuscarClase"),
    path('buscar/resultados', views.resultados_esc, name="BuscarResultados2"),
]
