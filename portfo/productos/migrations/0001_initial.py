# Generated by Django 4.2.1 on 2023-07-01 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Productos",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("codigo", models.IntegerField()),
                ("nombre", models.CharField(max_length=50)),
                ("descripcion", models.CharField(max_length=200)),
                ("imagen", models.CharField(max_length=1000)),
                ("disponible", models.CharField(max_length=20)),
            ],
        ),
    ]