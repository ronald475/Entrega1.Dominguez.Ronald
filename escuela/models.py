from django.db import models


class Clase(models.Model):
    titulo = models.CharField(max_length=40)
    tema = models.CharField(max_length=40)
    contenido = models.TextField()
    fecha = models.DateField()

    def __str__(self):
        return f"[{self.tema}] {self.titulo}"
