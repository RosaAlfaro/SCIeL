from django.db import models

class Cultivo(models.Model):
    id_cultivo = models.AutoField(
        primary_key=True
    )
    nombre_cultivo = models.CharField(
        max_length=45,
        null=False,
        verbose_name='Nombre del cultivo'
    )
    periodo_cosecha = models.IntegerField(
        verbose_name='Periódo de Cosecha',
    )

    def __str__(self):
        return self.nombre_cultivo

    class Meta:
        ordering = ['nombre_cultivo']
        verbose_name = 'Cultivo'
        verbose_name_plural = 'Cultivos'


class Etapa(models.Model):
    id_etapa = models.AutoField(
        primary_key=True
    )
    id_cultivo = models.ForeignKey(
        Cultivo,
        on_delete=models.CASCADE
    )
    numero_etapa = models.IntegerField(
        verbose_name='Número de etapa',
        blank=False,
        null=False
    )
    nombre_etapa = models.CharField(
        max_length=45,
        verbose_name='Nombre de etapa',
        blank=False
    )
    duracion = models.IntegerField(
        verbose_name='Duración de la etapa',
        null=False
    )
    descripcion_etapa = models.CharField(
        max_length=150
    )

    def __str__(self):
        return self.nombre_etapa

    class Meta:
        ordering = ["id_cultivo", "numero_etapa"]
        verbose_name = "Etapa"
        verbose_name_plural = "Etapas"


class Parametro(models.Model):
    id_parametro = models.AutoField(
        primary_key=True
    )
    nombre_parametro = models.CharField(
        max_length=45
    )
    id_cultivo = models.ForeignKey(
        Cultivo,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.nombre_parametro

    class Meta:
        ordering = ["id_cultivo","nombre_parametro"]
        verbose_name = "Parámetro"
        verbose_name_plural = "Parámetros"


class Invernadero(models.Model):
    id_invernadero = models.AutoField(
        primary_key=True
    )
    id_cultivo = models.ForeignKey(
        Cultivo,
        on_delete=models.CASCADE
    )
    nombre_invernadero = models.CharField(
        max_length=45
    )
    ubicacion = models.CharField(
        max_length=15
    )

    def __str__(self):
        return self.nombre_invernadero

    class Meta:
        ordering = ["id_cultivo", "nombre_invernadero"]
        verbose_name = "Invernadero"
        verbose_name_plural = "Invernaderos"


class Dispositivo(models.Model):
    id_dispositivo = models.AutoField(
        primary_key=True
    )
    id_invernadero = models.OneToOneField(
        Invernadero,
        on_delete=models.CASCADE
    )
    nombre_dispositivo = models.CharField(
        max_length=45
    )
    estado_dispositivo = models.CharField(
        max_length=45
    )

    def __str__(self):
        return self.nombre_dispositivo

    class Meta:
        ordering = ["id_invernadero"]
        verbose_name = "Dispositivo"
        verbose_name_plural = "Dispositivos"

class Actuador(models.Model):
    id_actuador = models.AutoField(
        primary_key=True
    )
    id_dispositivo = models.ForeignKey(
        Dispositivo,
        on_delete=models.CASCADE
    )
    nombre_actuador = models.CharField(
        max_length=45
    )
    is_activo = models.BooleanField(
        default=False
    )

    def __str___(self):
        return self.nombre_actuador

    class Meta:
        ordering = ["id_dispositivo","nombre_actuador"]
        verbose_name = "Actuador"
        verbose_name_plural = "Actuadores"


class Sensor(models.Model):
    id_sensor = models.AutoField(
        primary_key=True
    )
    id_dispositivo = models.ForeignKey(
        Dispositivo,
        on_delete=models.CASCADE
    )
    nombre_sensor = models.CharField(
        max_length=45
    )

    def __str__(self):
        return self.nombre_sensor

    class Meta:
        ordering = ["id_dispositivo", "nombre_sensor"]
        verbose_name = "Sensor"
        verbose_name_plural = "Sensores"


class Medicion(models.Model):
    id_medicion = models.AutoField(
        primary_key=True
    )
    id_cultivo = models.ForeignKey(
        Cultivo,
        on_delete=models.DO_NOTHING
    )
    id_parametro = models.ForeignKey(
        Parametro,
        on_delete=models.DO_NOTHING
    )
    id_sensor = models.ForeignKey(
        Sensor,
        on_delete=models.DO_NOTHING
    )
    id_actuador = models.ForeignKey(
        Actuador,
        on_delete=models.DO_NOTHING,
        null=True
    )
    magnitud_medicion = models.DecimalField(
        verbose_name='Magnitud',
        decimal_places=2,
        max_digits=5
    )
    fecha_medicion = models.DateTimeField(
        verbose_name='Fecha de lectura',
        auto_now_add=True
    )

    def __str__(self):
        return self.magnitud_medicion

    class Meta:
        ordering = ["fecha_medicion","id_cultivo", "id_sensor", "id_parametro", "id_actuador"]
        verbose_name = "Medicion"
        verbose_name_plural = "Mediciones"
