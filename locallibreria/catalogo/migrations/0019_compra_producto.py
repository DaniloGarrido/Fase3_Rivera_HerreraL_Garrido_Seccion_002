# Generated by Django 3.1.2 on 2020-11-29 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0018_auto_20201129_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='producto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogo.producto'),
        ),
    ]
