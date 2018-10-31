# Generated by Django 2.1.2 on 2018-10-30 06:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invernaderos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dispositivo',
            fields=[
                ('id_dispositivo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_dispositivo', models.CharField(max_length=45)),
                ('estado_dispositivo', models.CharField(max_length=45)),
            ],
            options={
                'verbose_name': 'Dispositivo',
                'verbose_name_plural': 'Dispositivos',
                'ordering': ['id_invernadero'],
            },
        ),
        migrations.AlterModelOptions(
            name='actuador',
            options={'ordering': ['id_dispositivo', 'nombre_actuador'], 'verbose_name': 'Actuador', 'verbose_name_plural': 'Actuadores'},
        ),
        migrations.AlterModelOptions(
            name='cultivo',
            options={'ordering': ['nombre_cultivo'], 'verbose_name': 'Cultivo', 'verbose_name_plural': 'Cultivos'},
        ),
        migrations.AlterModelOptions(
            name='etapa',
            options={'ordering': ['id_cultivo', 'numero_etapa'], 'verbose_name': 'Etapa', 'verbose_name_plural': 'Etapas'},
        ),
        migrations.AlterModelOptions(
            name='invernadero',
            options={'ordering': ['id_cultivo', 'nombre_invernadero'], 'verbose_name': 'Invernadero', 'verbose_name_plural': 'Invernaderos'},
        ),
        migrations.AlterModelOptions(
            name='medicion',
            options={'ordering': ['fecha_medicion', 'id_cultivo', 'id_sensor', 'id_parametro', 'id_actuador'], 'verbose_name': 'Medicion', 'verbose_name_plural': 'Mediciones'},
        ),
        migrations.AlterModelOptions(
            name='parametro',
            options={'ordering': ['id_cultivo', 'nombre_parametro'], 'verbose_name': 'Parámetro', 'verbose_name_plural': 'Parámetros'},
        ),
        migrations.AlterModelOptions(
            name='sensor',
            options={'ordering': ['id_dispositivo', 'nombre_sensor'], 'verbose_name': 'Sensor', 'verbose_name_plural': 'Sensores'},
        ),
        migrations.RenameField(
            model_name='actuador',
            old_name='nombre',
            new_name='nombre_actuador',
        ),
        migrations.RenameField(
            model_name='etapa',
            old_name='descripcion',
            new_name='descripcion_etapa',
        ),
        migrations.RenameField(
            model_name='etapa',
            old_name='cultivo',
            new_name='id_cultivo',
        ),
        migrations.RenameField(
            model_name='invernadero',
            old_name='nombre',
            new_name='nombre_invernadero',
        ),
        migrations.RenameField(
            model_name='medicion',
            old_name='fecha',
            new_name='fecha_medicion',
        ),
        migrations.RenameField(
            model_name='medicion',
            old_name='magnitud',
            new_name='magnitud_medicion',
        ),
        migrations.RenameField(
            model_name='parametro',
            old_name='nombre',
            new_name='nombre_parametro',
        ),
        migrations.RenameField(
            model_name='sensor',
            old_name='nombre',
            new_name='nombre_sensor',
        ),
        migrations.RemoveField(
            model_name='actuador',
            name='Activado',
        ),
        migrations.RemoveField(
            model_name='actuador',
            name='id',
        ),
        migrations.RemoveField(
            model_name='cultivo',
            name='id',
        ),
        migrations.RemoveField(
            model_name='cultivo',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='etapa',
            name='id',
        ),
        migrations.RemoveField(
            model_name='etapa',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='etapa',
            name='numero',
        ),
        migrations.RemoveField(
            model_name='invernadero',
            name='id',
        ),
        migrations.RemoveField(
            model_name='medicion',
            name='id',
        ),
        migrations.RemoveField(
            model_name='medicion',
            name='referencia',
        ),
        migrations.RemoveField(
            model_name='parametro',
            name='id',
        ),
        migrations.RemoveField(
            model_name='sensor',
            name='id',
        ),
        migrations.AddField(
            model_name='actuador',
            name='id_actuador',
            field=models.AutoField(default=None, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='actuador',
            name='is_activo',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cultivo',
            name='id_cultivo',
            field=models.AutoField(default=None, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cultivo',
            name='nombre_cultivo',
            field=models.CharField(default=None, max_length=45, verbose_name='Nombre del cultivo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='etapa',
            name='id_etapa',
            field=models.AutoField(default=None, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='etapa',
            name='nombre_etapa',
            field=models.CharField(default=None, max_length=45, verbose_name='Nombre de etapa'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='etapa',
            name='numero_etapa',
            field=models.IntegerField(default=None, verbose_name='Número de etapa'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='invernadero',
            name='id_cultivo',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='invernaderos.Cultivo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='invernadero',
            name='id_invernadero',
            field=models.AutoField(default=None, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='medicion',
            name='id_actuador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='invernaderos.Actuador'),
        ),
        migrations.AddField(
            model_name='medicion',
            name='id_cultivo',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='invernaderos.Cultivo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='medicion',
            name='id_medicion',
            field=models.AutoField(default=None, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='medicion',
            name='id_parametro',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='invernaderos.Parametro'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='medicion',
            name='id_sensor',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='invernaderos.Sensor'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parametro',
            name='id_cultivo',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='invernaderos.Cultivo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parametro',
            name='id_parametro',
            field=models.AutoField(default=None, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sensor',
            name='id_sensor',
            field=models.AutoField(default=None, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dispositivo',
            name='id_invernadero',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='invernaderos.Invernadero'),
        ),
        migrations.AddField(
            model_name='actuador',
            name='id_dispositivo',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='invernaderos.Dispositivo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sensor',
            name='id_dispositivo',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='invernaderos.Dispositivo'),
            preserve_default=False,
        ),
    ]