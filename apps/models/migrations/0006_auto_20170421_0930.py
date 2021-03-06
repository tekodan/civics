# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-21 09:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import djgeojson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0005_auto_20170419_1115'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='¿Cuál es el título del evento que quieres organiza?', max_length=200, null=True, verbose_name='Título del evento')),
                ('date', models.DateField(help_text='¿Qué día se celebra la actividad?', verbose_name='Fecha del evento')),
                ('time', models.TimeField(help_text='¿A qué hora se celebra la actividad?', verbose_name='Hora del evento')),
                ('position', djgeojson.fields.PointField(help_text='Añade la ubicación de la actividad. Si lo dejas en blanco se usará la ubicación de la iniciativa asociada.', null=True, verbose_name='Ubicación')),
                ('topic', models.CharField(choices=[('DC', 'Desarrollo comunitario'), ('AU', 'Arte urbano'), ('CL', 'Cultura libre'), ('DS', 'Deporte / Salud / Cuidados'), ('ID', 'Igualdad / Derechos / Memoria'), ('EC', 'Ecología / Consumo'), ('OE', 'Otras economías'), ('EE', 'Educación expandida'), ('CT', 'Ciencia / Tecnología'), ('MS', 'Movilidad sostenible'), ('PG', 'Política y gobernanza'), ('UP', 'Urbanismo / Patrimonio'), ('PC', 'Periodismo comunitario')], default='DC', help_text='El tema de la actividad', max_length=2, verbose_name='Temática de la actividad')),
                ('agent', models.CharField(choices=[('IM', 'Iniciativas municipales / Gobierno'), ('UO', 'Universidades / ONG / Fundaciones'), ('OI', 'Organismos internacionales'), ('ES', 'Empresa social / Startup'), ('IC', 'Iniciativa ciudadana'), ('JA', 'Juntas / Asociaciones de vecinos')], default='IM', help_text='El tipo de agente involucrado en la actividad', max_length=2, verbose_name='tipo de agente')),
                ('category', models.CharField(choices=[('AU', 'Audiovisual'), ('CU', 'Curso / Convocatoria'), ('DI', 'Digital'), ('EN', 'Encuentro'), ('EV', 'Evento'), ('EX', 'Exposicion'), ('FI', 'Fiesta / Concierto'), ('PU', 'Publicación'), ('TA', 'Taller')], default='AU', help_text='El tipo de actividad que quieres organizar', max_length=2, verbose_name='tipo de actividad')),
                ('description', models.TextField(help_text='Describe la actividad.', null=True, verbose_name='Descripción de la iniciativa')),
            ],
            options={
                'verbose_name': 'Actividad',
                'verbose_name_plural': 'Actividades',
            },
        ),
        migrations.AlterField(
            model_name='initiative',
            name='city',
            field=models.ForeignKey(help_text='Ciudad donde se encuentra la iniciativa. Si no la encuentras en la lista puedes añadir una nueva.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='models.City', verbose_name='Ciudad'),
        ),
        migrations.AlterField(
            model_name='initiative',
            name='facebook',
            field=models.URLField(blank=True, help_text='Si tienes un perfil de Facebook pon aquí su enlace.', null=True, verbose_name='Facebook'),
        ),
        migrations.AlterField(
            model_name='initiative',
            name='twitter',
            field=models.CharField(blank=True, help_text='Si tienes una cuenta de Twitter, pon aquí el nombre de usuario.', max_length=128, null=True, verbose_name='Twitter'),
        ),
        migrations.AddField(
            model_name='event',
            name='initiative',
            field=models.ForeignKey(default=False, help_text='¿Qué iniciativa organiza el evento?', null=True, on_delete=django.db.models.deletion.CASCADE, to='models.Initiative', verbose_name='Iniciativa que organiza la actividad'),
        ),
    ]
