# Generated by Django 3.1.2 on 2020-11-29 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0017_auto_20201128_2155'),
    ]

    operations = [
        migrations.RenameField(
            model_name='compra',
            old_name='coreo',
            new_name='correo',
        ),
        migrations.RenameField(
            model_name='compra',
            old_name='nom_user',
            new_name='nombre',
        ),
    ]
