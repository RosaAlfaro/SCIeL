from django.db import models

class Cultivo(models.Model):
    idCultivo = models.Autofield(
        primary_key=True
    )
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
    idEtapa = models.Autofield(
        primary_key=True
    )
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
    idCultivo = models.ForeignKey(
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
    idParametro = models.Autofield(
        primary_key=True
    )
    nombre = models.CharField(
        max_length=45
    )
    idCultivo = models.ForeignKey(
        Cultivo,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ["cultivo","nombre"]
        verbose_name = "Parámetro"
        verbose_name_plural = "Parámetros"


class Invernadero(models.Model):
    idInvernadero = models.Autofield(
        primary_key=True
    )
    nombre = models.CharField(
        max_length=45
    )
    ubicacion = models.CharField(
        max_length=15
    )
    idCultivo = models.ForeignKey(
        Cultivo,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ["cultivo", "nombre"]
        verbose_name = "Invernadero"
        verbose_name_plural = "Invernaderos"


class Dispositivo(models.Model):
    idDispositivo = models.Autofield(
        primary_key=True
    )
    nombre = models.CharField(
        max_length=45
    )
    estado = models.CharField(
        max_length=45
    )
    idInvernadero = models.ForeignKey(
        Invernadero,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ["invernadero", "nombre", "estado"]
        verbose_name = "Dispositivo"
        verbose_name_plural = "Dispositivos"

class Actuador(models.Model):
    idActuador = models.Autofield(
        primary_key=True
    )
    nombre = models.CharField(
        max_length=45
    )
    activado = models.BooleanField(
        verbose_name='Activado',
        name='Activado',
        null=False
    )
    idDispositivo = models.ForeignKey(
        Dispositivo,
        on_delete=models.CASCADE
    )

    def __str___(self):
        return self.nombre

    class Meta:
        ordering = ["dispositivo","nombre"]
        verbose_name = "Actuador"
        verbose_name_plural = "Actuadores"


class Sensor(models.Model):
    idSensor = models.Autofield(
        primary_key=True
    )
    nombre = models.CharField(
        max_length=45
    )
    idDispositivo = models.ForeignKey(
        Dispositivo,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ["dispositivo", "nombre"]
        verbose_name = "Sensor"
        verbose_name_plural = "Sensores"


class Medicion(models.Model):
    idMedicion = models.Autofield(
        primary_key=True
    )
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
    idCultivo = models.ForeignKey(
        Cultivo,
        on_delete=models.CASCADE
    )
    idParametro = models.ForeignKey(
        Parametro,
        on_delete=models.CASCADE
    )
    idSensor = models.ForeignKey(
        Sensor,
        on_delete=models.CASCADE
    )
    idActuador = models.ForeignKey(
        Actuador,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ["cultivo", "sensor", "parametro", "actuador", "numero", "nombre"]
        verbose_name = "Medicion"
        verbose_name_plural = "Mediciones"
