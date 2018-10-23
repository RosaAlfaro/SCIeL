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
        max_lenght=45,  
        null=False,
    )
    periodo_cosecha = models.IntegerField(
        verbose_name='Periódo de Cosecha',
        max_length=3,
        null=False,
        blank=False
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
        max_length=3, 
        null=False, 
        blank=False
    )
    nombre = models.CharField(
        max_lenght=45, 
        null=False,
    )
    duracion = models.IntegerField(
        verbose_name='Duración de la etapa', 
        max_length=5, 
        null=False, 
        blank=False
    )
    descripcion = models.CharField(
        max=150,
        null=False
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
        max_lenght=45, 
        null=False,
    )

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['nombre']
        verbose_name = 'Parámetro'
        verbose_name_plural = 'Parámetros'


class Sensor(models.Model):
    nombre = models.CharField(
        max_lenght=45, 
        null=False
    )

class Medicion(models.Model):
    magnitud = models.DecimalField(
        verbose_name='Magnitud',
        decimal_places=2
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
    nombre = models.CharField(max_lenght=45,  null=False)
    ubicacion = models.CharField(max_lenght=15,  null=False)

