# Generated by Django 4.2.5 on 2023-09-12 22:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mikrotik", "0003_remove_servicio_max_limit_servicio_plan"),
    ]

    operations = [
        migrations.RenameField(
            model_name="planvelocidad",
            old_name="velociadad",
            new_name="velocidad",
        ),
    ]