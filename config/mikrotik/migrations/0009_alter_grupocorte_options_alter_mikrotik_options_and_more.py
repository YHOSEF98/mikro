# Generated by Django 4.2.5 on 2023-09-09 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mikrotik", "0008_planvelocidad_alter_grupocorte_hora"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="grupocorte",
            options={
                "verbose_name": "Grupo de corte",
                "verbose_name_plural": "Grupos de corte",
            },
        ),
        migrations.AlterModelOptions(
            name="mikrotik",
            options={
                "verbose_name": "Mikrotik",
                "verbose_name_plural": "Servidores mikrotik",
            },
        ),
        migrations.AlterModelOptions(
            name="planvelocidad",
            options={
                "verbose_name": "Plan de Velocidad",
                "verbose_name_plural": "Planes de Velocidad",
            },
        ),
        migrations.AlterModelOptions(
            name="segmentos",
            options={
                "verbose_name": "Segmento",
                "verbose_name_plural": "Segmentos de red",
            },
        ),
        migrations.AlterModelOptions(
            name="servicio",
            options={"verbose_name": "Servicio", "verbose_name_plural": "Servicios"},
        ),
    ]