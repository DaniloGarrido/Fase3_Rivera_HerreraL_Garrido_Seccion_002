# Generated by Django 3.1.2 on 2020-11-13 01:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0013_auto_20201112_2207'),
    ]

    operations = [
        migrations.AddField(
            model_name='marca',
            name='disponible',
            field=models.BooleanField(null=True),
        ),
        migrations.RemoveField(
            model_name='producto',
            name='marca',
        ),
        migrations.AddField(
            model_name='producto',
            name='marca',
            field=models.ForeignKey(blank=True, help_text='Seleccione una marca para este producto', null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogo.marca'),
        ),
    ]
