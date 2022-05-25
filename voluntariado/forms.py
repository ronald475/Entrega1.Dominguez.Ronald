from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class FormFacilitador(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)

    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Repita la contraseña", widget=forms.PasswordInput
    )

    email = forms.EmailField()
    presentacion = forms.CharField(widget=forms.Textarea, required=False)


class FormRegistrarse(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Repita la contraseña", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class FormVoluntario(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()
