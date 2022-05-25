from django.db import models


class Facilitador(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    presentacion = models.TextField()

    class Meta:
        verbose_name = "Facilitador"
        verbose_name_plural = "Facilitadores"

    def __str__(self):
        return f"[Facilitador] {self.nombre} {self.apellido}"


class Voluntario(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()

    def __str__(self):
        return f"[Voluntario] {self.nombre} {self.apellido}"
