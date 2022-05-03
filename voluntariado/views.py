from django.shortcuts import render, redirect
from voluntariado.models import Facilitador, Voluntario
from .forms import FormFacilitador, FormVoluntario


def inicio_voluntariado(request):
    return render(request, "voluntariado/inicio.html")


def nuevo_voluntario(request):
    if request.method == "POST":
        mi_form = FormVoluntario(request.POST)
        if mi_form.is_valid():
            info = mi_form.cleaned_data
            voluntario = Voluntario(
                nombre=info["nombre"],
                apellido=info["apellido"],
                email=info["email"],
            )
            voluntario.save()
            return redirect("InicioVoluntariado")

    mi_form = FormVoluntario()

    return render(request, "voluntariado/formVol.html", {"form": mi_form})


def nuevo_facilitador(request):
    if request.method == "POST":
        mi_form = FormFacilitador(request.POST)
        if mi_form.is_valid():
            info = mi_form.cleaned_data
            facilitador = Facilitador(
                nombre=info["nombre"],
                apellido=info["apellido"],
                email=info["email"],
                presentacion=info["sobre_ti"],
            )
            facilitador.save()
            return redirect("InicioVoluntariado")

    mi_form = FormFacilitador()

    return render(request, "voluntariado/formFac.html", {"form": mi_form})


def buscar_voluntario(request, nombre):
    if request.GET.get("nombre"):
        nombre = request.GET.get("nombre")
        voluntarios = Voluntario.objects.filter(
            nombre__icontains=nombre, nombre=nombre)
        return render(request, "voluntariado/resultado_buscar.html", {"voluntarios": voluntarios})

    return render(request, "voluntariado/buscar.html")


def resultados_vol(request):
    return render(request, "voluntariado/resultado_buscar.html")
