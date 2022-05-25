from django.shortcuts import render, redirect
from voluntariado.models import Facilitador, Voluntario
from .forms import FormFacilitador, FormRegistrarse, FormVoluntario


def inicio(request):
    return render(request, "voluntariado/inicio.html")


def facilitadores(request):
    facilitadores = Facilitador.objects.all()
    return render(request, "voluntariado/facilitadores.html", {"facilitadores": facilitadores})


def ver_facilitador(request, id):
    facilitador = Facilitador.objects.get(id=id)
    return render(request, "voluntariado/ver_facilitador.html", {"facilitador": facilitador})


def editar_facilitador(request, id):
    facilitador = Facilitador.objects.get(id=id)

    if request.method == "POST":
        mi_form = FormFacilitador(request.POST)
        if mi_form.is_valid():
            info = mi_form.cleaned_data

            facilitador.nombre = info["nombre"],
            facilitador.apellido = info["apellido"],
            facilitador.email = info["email"],
            facilitador.presentacion = info["presentacion"],

            facilitador.save()
            return redirect("Facilitadores")

    mi_form = FormFacilitador(initial={
        "nombre": facilitador.nombre,
        "apellido": facilitador.apellido,
        "email": facilitador.email,
        "presentacion": facilitador.presentacion,
    })

    return render(request, "voluntariado/formFac.html", {"form": mi_form})


def nuevo_facilitador(request):
    if request.method == "POST":
        mi_form = FormFacilitador(request.POST)
        if mi_form.is_valid():
            info = mi_form.cleaned_data

            pass1 = info.get("password1")
            pass2 = info.get("password2")
            nombre = info.get("nombre")
            apellido = info.get("apellido")
            email = info.get("email")
            data = {
                "username": nombre + apellido,
                "password1": pass1,
                "password2": pass2,
                "email": email,
            }

            form_registro = FormRegistrarse(data)
            if form_registro.is_valid():
                form_registro.save()
                
                facilitador = Facilitador(
                    nombre=nombre,
                    apellido=apellido,
                    email=email,
                    presentacion=info.get("presentacion"),
                )
            facilitador.save()
            
            return redirect("Facilitadores")

    mi_form = FormFacilitador()

    return render(request, "voluntariado/formFac.html", {"form": mi_form})


def eliminar_facilitador(request, id):
    facilitador = Facilitador.objects.get(id=id)
    facilitador.delete()

    return redirect("Facilitadores")


def voluntarios(request):
    voluntarios = Voluntario.objects.all()
    return render(request, "voluntariado/voluntarios.html", {"voluntarios": voluntarios})


def ver_voluntario(request, id):
    voluntario = Voluntario.objects.get(id=id)
    return render(request, "voluntariado/ver_voluntario.html", {"voluntario": voluntario})


def editar_voluntario(request, id):
    voluntario = Voluntario.objects.get(id=id)

    if request.method == "POST":
        mi_form = FormVoluntario(request.POST)
        if mi_form.is_valid():
            info = mi_form.cleaned_data

            voluntario.nombre = info["nombre"],
            voluntario.apellido = info["apellido"],
            voluntario.email = info["email"],

            voluntario.save()
            return redirect("Voluntarios")

    mi_form = FormVoluntario(initial={
        "nombre": voluntario.nombre,
        "apellido": voluntario.apellido,
        "email": voluntario.email,
    })

    return render(request, "voluntariado/formVol.html", {"form": mi_form})


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
            return redirect("Inicio")

    mi_form = FormVoluntario()

    return render(request, "voluntariado/formVol.html", {"form": mi_form})


def eliminar_voluntario(request, id):
    voluntario = Voluntario.objects.get(id=id)
    voluntario.delete()

    return redirect("Voluntarios")


def buscar_voluntario(request, nombre):
    if request.GET.get("nombre"):
        nombre = request.GET.get("nombre")
        voluntarios = Voluntario.objects.filter(
            nombre__icontains=nombre, nombre=nombre)
        return render(request, "voluntariado/resultado_buscar.html", {"voluntarios": voluntarios})

    return render(request, "voluntariado/buscar.html")


def resultados_vol(request):
    return render(request, "voluntariado/resultado_buscar.html")
