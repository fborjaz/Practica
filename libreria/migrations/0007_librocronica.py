# Generated by Django 5.1.2 on 2024-10-27 03:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0006_libro_edicion_ant'),
    ]

    operations = [
        migrations.CreateModel(
            name='LibroCronica',
            fields=[
                ('descripcion_larga', models.TextField(null=True)),
                ('libro', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='libreria.libro')),
            ],
        ),
    ]
