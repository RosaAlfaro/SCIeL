from django.db import models


class Actuador(models.Model):
    nombre = models.CharField(
        max_length=45
    )
    activado = models.BooleanField(
        verbose_name='Activado',
        name='Activado',
        null=False
    )

    def __str___(self):
        return self.nombre

    class Meta:
        ordering = ["nombre"]
        verbose_name = "Actuador"
        verbose_name_plural = "Actuadores"


class Cultivo(models.Model):
    nombre = models.CharField(
        max_length=45
    )
    periodo_cosecha = models.IntegerField(
        verbose_name='Periódo de Cosecha',
    )

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['nombre']
        verbose_name = 'Cultivo'
        verbose_name_plural = 'Cultivo'


class Etapa(models.Model):
    numero = models.IntegerField(
        verbose_name='Número',
        blank=False
    )
    nombre = models.CharField(
        max_length=45
    )
    duracion = models.IntegerField(
        verbose_name='Duración de la etapa',
        null=False
    )
    descripcion = models.CharField(
        max_length=150
    )
    cultivo = models.ForeignKey(
        Cultivo,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ["cultivo", "numero", "nombre"]
        verbose_name = "Etapa"
        verbose_name_plural = "Etapas"


class Parametro(models.Model):
    nombre = models.CharField(
        max_length=45
    )

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['nombre']
        verbose_name = 'Parámetro'
        verbose_name_plural = 'Parámetros'


class Sensor(models.Model):
    nombre = models.CharField(
        max_length=45
    )


class Medicion(models.Model):
    magnitud = models.DecimalField(
        verbose_name='Magnitud',
        decimal_places=2,
        max_digits=5
    )
    referencia = models.BooleanField(
        verbose_name='¿Es la referencia?',
        blank=False,
        default=False
    )
    fecha = models.DateTimeField(
        verbose_name='Fecha de lectura',
        auto_now_add=True
    )


class Invernadero(models.Model):
    nombre = models.CharField(max_length=45)
    ubicacion = models.CharField(max_length=15)
