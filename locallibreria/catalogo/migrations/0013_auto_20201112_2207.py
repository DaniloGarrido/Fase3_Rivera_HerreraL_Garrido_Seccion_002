# Generated by Django 3.1.2 on 2020-11-13 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0012_auto_20201102_0317'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='img1',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='producto',
            name='img2',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='producto',
            name='img3',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='producto',
            name='img4',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='producto',
            name='alto',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Alto del producto(puede quedar en blanco)', max_digits=4, null=True),
        ),
    ]