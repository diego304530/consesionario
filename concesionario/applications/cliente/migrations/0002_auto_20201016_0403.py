# Generated by Django 3.1.2 on 2020-10-16 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='fecha_nacimiento',
            field=models.DateField(),
        ),
    ]
