from django.shortcuts import render, redirect
from voluntariado.models import Facilitador, Voluntario
from .forms import FormFacilitador, FormRegistrarse, FormVoluntario
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import login, authenticate, logout


def inicio(request):
    return render(request, "voluntariado/inicio.html")


def about(request):
    return render(request, "voluntariado/about.html")


def es_admin_o_facilitador(user):
    if not user.is_authenticated:
        return False

    if user.is_staff:
        return True

    try:
        facilitador = Facilitador.objects.count(usuario=user.id)
    except ObjectDoesNotExist:
        facilitador = None

    return facilitador is not None


def es_admin_o_voluntario(user):
    if not user.is_authenticated:
        return False

    if user.is_authenticated:
        return True

    try:
        voluntario = Voluntario.objects.count(usuario=user.id)
    except ObjectDoesNotExist:
        voluntario = None

    return voluntario is not None


def es_admin(user):
    return user.is_authenticated and user.is_staff


# Facilitafores
def facilitadores(request):
    facilitadores = Facilitador.objects.all()
    return render(request, "voluntariado/facilitadores.html", {"facilitadores": facilitadores})


@user_passes_test(es_admin)
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
            username = nombre + apellido
            data = {
                "username": username,
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
                    usuario=User.objects.get(username=username)
                )
                facilitador.save()

                return redirect("Facilitadores")
            else:
                print(form_registro.errors)

    mi_form = FormFacilitador()

    return render(request, "voluntariado/formFac.html", {"form": mi_form})


def ver_facilitador(request, id):
    facilitador = Facilitador.objects.get(id=id)
    return render(request, "voluntariado/ver_facilitador.html", {"facilitador": facilitador})


@user_passes_test(es_admin_o_facilitador)
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


@user_passes_test(es_admin_o_facilitador)
def eliminar_facilitador(request, id):
    if request.user.is_staff or request.user.id == id:
        facilitador = Facilitador.objects.get(id=id)
        facilitador.delete()

        return redirect("Facilitadores")
    else:
        redirect("Inicio")


# Voluntarios
def voluntarios(request):
    voluntarios = Voluntario.objects.all()
    return render(request, "voluntariado/voluntarios.html", {"voluntarios": voluntarios})


def nuevo_voluntario(request):
    if request.method == "POST":
        mi_form = FormVoluntario(request.POST)
        if mi_form.is_valid():
            info = mi_form.cleaned_data

            pass1 = info.get("password1")
            pass2 = info.get("password2")
            nombre = info.get("nombre")
            apellido = info.get("apellido")
            email = info.get("email")
            username = nombre + apellido
            data = {
                "username": username,
                "password1": pass1,
                "password2": pass2,
                "email": email,
            }

            form_registro = FormRegistrarse(data)
            if form_registro.is_valid():
                form_registro.save()

                voluntario = Voluntario(
                    nombre=nombre,
                    apellido=apellido,
                    email=email,
                    usuario=User.objects.get(username=username)
                )
                voluntario.save()

                return redirect("Voluntarios")
            else:
                print(form_registro.errors)

    mi_form = FormVoluntario()

    return render(request, "voluntariado/formVol.html", {"form": mi_form})


def ver_voluntario(request, id):
    voluntario = Voluntario.objects.get(id=id)
    return render(request, "voluntariado/ver_voluntario.html", {"voluntario": voluntario})


@user_passes_test(es_admin_o_voluntario)
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


@user_passes_test(es_admin_o_voluntario)
def eliminar_voluntario(request, id):
    voluntario = Voluntario.objects.get(id=id)
    voluntario.delete()

    return redirect("Voluntarios")


def login_request(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect("Inicio")

    return render(request, "voluntariado/login.html")


@login_required
def logout_request(request):
    logout(request)
    return redirect("Inicio")
