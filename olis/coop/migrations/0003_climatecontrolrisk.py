# Generated by Django 4.2.7 on 2023-11-27 15:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("coop", "0002_responsibilities"),
    ]

    operations = [
        migrations.CreateModel(
            name="ClimateControlRisk",
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
                (
                    "heating_system",
                    models.IntegerField(
                        choices=[
                            (1, "Must be addressed"),
                            (2, "Should be addressed"),
                            (3, "Could be addressed"),
                            (4, "Not applicable/no action needed"),
                        ],
                        verbose_name="Heating System",
                    ),
                ),
                (
                    "cooling_system",
                    models.IntegerField(
                        choices=[
                            (1, "Must be addressed"),
                            (2, "Should be addressed"),
                            (3, "Could be addressed"),
                            (4, "Not applicable/no action needed"),
                        ],
                        verbose_name="Cooling System",
                    ),
                ),
                (
                    "humidification_system",
                    models.IntegerField(
                        choices=[
                            (1, "Must be addressed"),
                            (2, "Should be addressed"),
                            (3, "Could be addressed"),
                            (4, "Not applicable/no action needed"),
                        ],
                        verbose_name="Humidification System",
                    ),
                ),
                (
                    "air_circulation",
                    models.IntegerField(
                        choices=[
                            (1, "Must be addressed"),
                            (2, "Should be addressed"),
                            (3, "Could be addressed"),
                            (4, "Not applicable/no action needed"),
                        ],
                        verbose_name="Air Circulation",
                    ),
                ),
                (
                    "building_closed",
                    models.IntegerField(
                        choices=[
                            (1, "Must be addressed"),
                            (2, "Should be addressed"),
                            (3, "Could be addressed"),
                            (4, "Not applicable/no action needed"),
                        ],
                        verbose_name="Building Closed in Winter",
                    ),
                ),
                (
                    "temperature_extremes",
                    models.IntegerField(
                        choices=[
                            (1, "Must be addressed"),
                            (2, "Should be addressed"),
                            (3, "Could be addressed"),
                            (4, "Not applicable/no action needed"),
                        ],
                        verbose_name="Temperature Extremes",
                    ),
                ),
                (
                    "humidity_extremes",
                    models.IntegerField(
                        choices=[
                            (1, "Must be addressed"),
                            (2, "Should be addressed"),
                            (3, "Could be addressed"),
                            (4, "Not applicable/no action needed"),
                        ],
                        verbose_name="Humidity Extremes",
                    ),
                ),
                (
                    "mold_infestation",
                    models.IntegerField(
                        choices=[
                            (1, "Must be addressed"),
                            (2, "Should be addressed"),
                            (3, "Could be addressed"),
                            (4, "Not applicable/no action needed"),
                        ],
                        verbose_name="Mold Infestation",
                    ),
                ),
                (
                    "collections",
                    models.IntegerField(
                        choices=[
                            (1, "Must be addressed"),
                            (2, "Should be addressed"),
                            (3, "Could be addressed"),
                            (4, "Not applicable/no action needed"),
                        ],
                        verbose_name="Collections in Uncontrolled Areas",
                    ),
                ),
            ],
        ),
    ]