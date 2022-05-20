from django.shortcuts import render, redirect
from escuela.models import Clase
from .forms import FormClase


def clases(request):
    clases = Clase.objects.all()
    return render(request, "escuela/clases.html", {"clases": clases})


def ver_clase(request, id):
    clase = Clase.objects.get(id=id)
    return render(request, "escuela/ver_clase.html", {"clase": clase})


def editar_clase(request, id):
    clase = Clase.objects.get(id=id)

    if request.method == "POST":
        mi_form = FormClase(request.POST)
        if mi_form.is_valid():
            info = mi_form.cleaned_data

            clase.titulo = info["titulo"],
            clase.tema = info["tema"],
            clase.contenido = info["contenido"],
            clase.fecha = info["fecha"],

            clase.save()
            return redirect("Clases")

    mi_form = FormClase(initial={
        "titulo": clase.titulo,
        "tema": clase.tema,
        "contenido": clase.contenido,
        "fecha": clase.fecha,
    })

    return render(request, "escuela/formCla.html", {"form": mi_form})


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


def eliminar_clase(request, id):
    clase = Clase.objects.get(id=id)
    clase.delete()

    return redirect("Clases")


def buscar_tema(request, tema):
    if request.GET.get("titulo"):
        titulo = request.GET.get("titulo")
        clases = Clase.objects.filter(titulo__icontains=titulo, tema=tema)
        return render(request, "escuela/resultado_buscar.html", {"clases": clases})

    return render(request, "escuela/buscar.html")


def resultados_esc(request):
    return render(request, "escuela/resultado_buscar.html")