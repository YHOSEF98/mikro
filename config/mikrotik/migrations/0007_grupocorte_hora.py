# Generated by Django 4.2.5 on 2023-09-08 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mikrotik", "0006_grupocorte"),
    ]

    operations = [
        migrations.AddField(
            model_name="grupocorte",
            name="hora",
            field=models.TimeField(default="12:00"),
        ),
    ]
