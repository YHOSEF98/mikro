# Generated by Django 4.2.3 on 2023-08-25 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mikrotik", "0004_remove_servicio_bajada_remove_servicio_subida_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="servicio",
            name="ip",
            field=models.CharField(max_length=15),
        ),
    ]
