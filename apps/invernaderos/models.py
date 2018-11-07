from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from django.dispatch import receiver


class Cultivo(models.Model):
    id_cultivo = models.AutoField(
        primary_key=True,
        verbose_name='Codigo del cultivo',
        help_text='Identificador genérico del cultivo',
        error_messages={
            'exist': 'El indentificador ya existe'
        }
    )
    nombre_cultivo = models.CharField(
        max_length=45,
        null=True, 
        blank=True,
        verbose_name='Nombre del cultivo',
        help_text='Nombre de la planta a cultivar',
        error_messages={
            'empty': 'Este campo no debe quedar vacío'
        }
    )
    periodo_cosecha = models.IntegerField(
        verbose_name='Periódo de Cosecha',
        help_text="Debe ingresar el tiempo que tarda el cultivo en dar frutos",
        error_messages={
            'value':'Debe ser un dato entero positivo'
        },
        validators=[
            MinValueValidator(0),
            MaxValueValidator(1000)
        ],
        null=True, 
        blank=True,
    )

    def __str__(self):
        return self.nombre_cultivo

    class Meta:
        ordering = ['nombre_cultivo']
        verbose_name = 'Cultivo'
        verbose_name_plural = 'Cultivos'


class Etapa(models.Model):
    id_etapa = models.AutoField(
        primary_key=True,
        verbose_name='Codigo de la etapa',
        help_text='Identificador genérico de la Etapa',
        error_messages={
            'exist': 'El indentificador ya existe',
        }
    )
    id_cultivo = models.ForeignKey(
        Cultivo,
        on_delete=models.CASCADE,
        verbose_name='Cultivo',
        help_text='Cultivo al que pertenece esta etapa',
        error_messages={
            'select': 'Debe seleccionar uno de la lista'
        },
        null=True, 
        blank=True
    )
    numero_etapa = models.IntegerField(
        verbose_name='Número de etapa',
        null=True, 
        blank=True,
        help_text="Debe ingresar la cantidad de etapas durante el tiempo de vida del cultivo",
        error_messages={
            'value':'Debe ser un dato entero positivo'
        },
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10)
        ]
    )
    nombre_etapa = models.CharField(
        max_length=45,
        verbose_name='Nombre de etapa',
        help_text='Ingrese el nombre de la etapa. Ejemplo: Floración',
        error_messages={
            'empty': 'Este campo no debe quedar vacío'
        },
        null=True, 
        blank=True
    )
    duracion = models.IntegerField(
        verbose_name='Duración de la etapa',
        null=True, 
        blank=True,
        help_text="Debe ingresar el tiempo que dura esta etapa",
        error_messages={
            'value':'Debe ser un dato entero positivo'
        },
        validators=[
            MinValueValidator(0)
        ]
    )
    descripcion_etapa = models.CharField(
        max_length=150,
        verbose_name='Descripcion de la etapa',
        help_text='Ingrese una breve descripción de la etapa',
        error_messages={
            'empty': 'Este campo no debe quedar vacío'
        },
        null=True, 
        blank=True
    )

    def __str__(self):
        return self.nombre_etapa

    class Meta:
        ordering = ["id_cultivo", "numero_etapa"]
        verbose_name = "Etapa"
        verbose_name_plural = "Etapas"


class Dispositivo(models.Model):
    id_dispositivo = models.AutoField(
        primary_key=True,
        verbose_name='Codigo del dispositivo',
        help_text='Identificador genérico del dispositivo',
        error_messages={
            'exist': 'El indentificador ya existe'
        }
    )
    nombre_dispositivo = models.CharField(
        max_length=45,
        verbose_name='Nombre del dispositivo',
        help_text='Dele un nombre al dispositivo a usar en sus invernaderos',
        error_messages={
            'empty': 'Este campo no debe quedar vacío'
        },
        null=True, 
        blank=True
    )

    def __str__(self):
        return self.nombre_dispositivo

    class Meta:
        ordering = ["id_dispositivo"]
        verbose_name = "Dispositivo"
        verbose_name_plural = "Dispositivos"


class Invernadero(models.Model):
    id_invernadero = models.AutoField(
        primary_key=True,
        verbose_name='Codigo del invernadero',
        help_text='Identificador genérico del invernadero',
        error_messages={
            'exist': 'El indentificador ya existe'
        }
    )
    id_dispositivo = models.ForeignKey(
        Dispositivo,
        on_delete=models.DO_NOTHING,
        verbose_name='Dispositivo',
        help_text='Dispositivo que controla este invernadero',
        error_messages={
            'select': 'Debe seleccionar uno de la lista'
        },
        null=True, 
        blank=True
    )
    id_usuario = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        verbose_name='Usuario',
        help_text='Usuario al que pertenece este invernadero',
        error_messages={
            'select': 'Debe seleccionar uno de la lista'
        },
        null=True, 
        blank=True
    )
    id_cultivo = models.ManyToManyField(
        Cultivo,
        verbose_name='Cultivo',
        help_text='Cultivo que se cosechará en este invernadero',
        error_messages={
            'select': 'Debe seleccionar uno de la lista'
        },
    )
    nombre_invernadero = models.CharField(
        max_length=45,
        verbose_name='Nombre del invernadero',
        help_text='Asignele un nombre cualquiera al invernadero',
        error_messages={
            'empty': 'Este campo no debe quedar vacío'
        },
        null=True, 
        blank=True
    )
    ubicacion = models.CharField(
        max_length=23,
        verbose_name='Ubicacion del invernadero',
        help_text='Ingrese la ubicación del invernadero',
        error_messages={
            'empty': 'Este campo no debe quedar vacío'
        },
        null=True, 
        blank=True
    )

    def __str__(self):
        return self.nombre_invernadero

    class Meta:
        ordering = ["id_invernadero", "nombre_invernadero"]
        verbose_name = "Invernadero"
        verbose_name_plural = "Invernaderos"


class Parametro(models.Model):
    id_parametro = models.AutoField(
        primary_key=True,
        verbose_name='Codigo del parámetro',
        help_text='Identificador genérico del parámetro que servirá de estándar',
        error_messages={
            'exist': 'El indentificador ya existe'
        }
    )
    id_invernadero = models.ForeignKey(
        Invernadero,
        on_delete=models.CASCADE,
        verbose_name='Invernadero',
        help_text='Invernadero al que se asignará este parámetro',
        error_messages={
            'select': 'Debe seleccionar uno de la lista'
        },
        null=True, 
        blank=True
    )
    nombre_parametro = models.CharField(
        max_length=45,
        verbose_name='Nombre del parámetro',
        help_text='Ingrese el nombre del parámetro a medir',
        error_messages={
            'empty': 'Este campo no debe quedar vacío'
        },
        null=True, 
        blank=True
    )
    magnitud_referencia = models.DecimalField(
        verbose_name='Magnitud del Parámetro Base',
        max_digits=10,
        decimal_places=2,
        help_text='Ingrese el valor de la magnitud de referencia para este parámetro',
        error_messages={
            'value': 'Ese valor debe ser positivo'
        },
        validators=[
            MinValueValidator(0)
        ],
        null=True, 
        blank=True
    )

    def __str__(self):
        return self.nombre_parametro

    class Meta:
        ordering = ["id_invernadero","nombre_parametro"]
        verbose_name = "Parámetro"
        verbose_name_plural = "Parámetros"


class Actuador(models.Model):
    id_actuador = models.AutoField(
        primary_key=True,
        verbose_name='Codigo del Actuador',
        help_text='Identificador genérico del actuador',
        error_messages={
            'exist': 'El indentificador ya existe'
        }
    )
    id_dispositivo = models.ForeignKey(
        Dispositivo,
        on_delete=models.CASCADE,
        verbose_name='Dispositivo',
        help_text='Dispositivo que se asociará a este actuador',
        error_messages={
            'select': 'Debe seleccionar uno de la lista'
        },
        null=True, 
        blank=True
    )
    id_invernadero = models.ForeignKey(
        Invernadero,
        on_delete=models.CASCADE,
        verbose_name='Invernadero',
        help_text='Invernadero al que se asignará este parámetro',
        error_messages={
            'select': 'Debe seleccionar uno de la lista'
        },
        null=True, 
        blank=True
    )
    nombre_actuador = models.CharField(
        max_length=45,
        verbose_name='Nombre del Actuador',
        help_text='Ingrese el nombre del actuador a usar',
        error_messages={
            'empty': 'Este campo no debe quedar vacío'
        },
        null=True, 
        blank=True
    )

    def __str___(self):
        return self.nombre_actuador

    class Meta:
        ordering = ["id_dispositivo","nombre_actuador"]
        verbose_name = "Actuador"
        verbose_name_plural = "Actuadores"


class Sensor(models.Model):
    id_sensor = models.AutoField(
        primary_key=True,
        verbose_name='Codigo del sensor',
        help_text='Identificador genérico del sensor',
        error_messages={
            'exist': 'El indentificador ya existe'
        }
    )
    id_dispositivo = models.ForeignKey(
        Dispositivo,
        on_delete=models.CASCADE,
        verbose_name='Dispositivo',
        help_text='Dispositivo asociado a este sensor',
        error_messages={
            'select': 'Debe seleccionar uno de la lista'
        },
        null=True, 
        blank=True
    )
    id_invernadero = models.ForeignKey(
        Invernadero,
        on_delete=models.CASCADE,
        verbose_name='Invernadero',
        help_text='Invernadero al que se asignará este parámetro',
        error_messages={
            'select': 'Debe seleccionar uno de la lista'
        },
        null=True, 
        blank=True
    )
    nombre_sensor = models.CharField(
        max_length=45,
        verbose_name='Nombre del sensor',
        help_text='Ingrese un nombre para este sensor',
        error_messages={
            'empty': 'Este campo no debe quedar vacío'
        },
        null=True, 
        blank=True
    )

    def __str__(self):
        return self.nombre_sensor

    class Meta:
        ordering = ["id_dispositivo", "nombre_sensor"]
        verbose_name = "Sensor"
        verbose_name_plural = "Sensores"


class Medicion(models.Model):
    id_medicion = models.AutoField(
        primary_key=True,
        verbose_name='Codigo de la medición',
        help_text='Identificador genérico de la medición',
        error_messages={
            'exist': 'El indentificador ya existe'
        }
    )
    id_invernadero = models.ForeignKey(
        Invernadero,
        on_delete=models.DO_NOTHING,
        verbose_name='Invernadero',
        help_text='Invernadero al que se le realizó la medición',
        error_messages={
            'select': 'Debe seleccionar uno de la lista'
        },
        null=True, 
        blank=True
    )
    id_parametro = models.ForeignKey(
        Parametro,
        on_delete=models.DO_NOTHING,
        verbose_name='Parámetro',
        help_text='Parámetro con el que se comparará esta medición',
        error_messages={
            'select': 'Debe seleccionar uno de la lista'
        },
        null=True, 
        blank=True
    )
    id_sensor = models.ForeignKey(
        Sensor,
        on_delete=models.DO_NOTHING,
        verbose_name='Sensor',
        help_text='Sensor con el que se realizó esta medición',
        error_messages={
            'select': 'Debe seleccionar uno de la lista'
        },
        null=True, 
        blank=True
    )
    id_actuador = models.ForeignKey(
        Actuador,
        on_delete=models.DO_NOTHING,
        verbose_name='Actuador',
        help_text='Actuador que responderá a dicha medición',
        error_messages={
            'select': 'Debe seleccionar uno de la lista'
        },
        null=True, 
        blank=True
    )
    magnitud_medicion = models.DecimalField(
        decimal_places=2,
        max_digits=5,
        verbose_name='Magnitud de la medición',
        help_text='Magnitud de la medición realizada',
        error_messages={
            'value': 'Debe ser un valor positivo'
        },
        validators=[
            MinValueValidator(0)
        ],
        null=True, 
        blank=True
    )
    fecha_medicion = models.DateTimeField(
        verbose_name='Fecha de lectura',
        auto_now=True,
        help_text='Momento en el que se realizó la medición',
        error_messages={
            'value': 'La fecha por defecto es la de hoy'
        },
        null=True, 
        blank=True
    )
    is_activo = models.BooleanField(
        default=False,
        verbose_name='¿Está activo?',
        help_text='Respuesta del dispositivo',
        error_messages={
            'value': 'Debe ser un atributo boleano'
        },
        null=True, 
        blank=True
    )

    def take(self):
        self.fecha_medicion = timezone.now()
        self.save()

    def __str__(self):
        return self.magnitud_medicion

    class Meta:
        ordering = ["fecha_medicion","id_invernadero", "id_sensor", "id_parametro", "id_actuador"]
        verbose_name = "Medicion"
        verbose_name_plural = "Mediciones"
