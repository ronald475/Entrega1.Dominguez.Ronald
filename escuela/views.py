from django.shortcuts import render, redirect
from escuela.models import Clase
from .forms import FormClase


def nueva_clase(request):
    if request.method == "POST":
        mi_form = FormClase(request.POST)
        if mi_form.is_valid():
            info = mi_form.cleaned_data
            clase = Clase(
                titulo=info["titulo"],
                tema=info["tema"],
                contenido=info["contenido"],
                fecha=info["fecha"],
            )
            clase.save()
            return redirect("Inicio")

    mi_form = FormClase()

    return render(request, "escuela/formCla.html", {"form": mi_form})


def buscar_tema(request, tema):
    if request.GET.get("titulo"):
        titulo = request.GET.get("titulo")
        clases = Clase.objects.filter(titulo__icontains=titulo, tema=tema)
        return render(request, "escuela/resultado_buscar.html", {"clases": clases})

    return render(request, "escuela/buscar.html")


def resultados_esc(request):
    return render(request, "escuela/resultado_buscar.html")
