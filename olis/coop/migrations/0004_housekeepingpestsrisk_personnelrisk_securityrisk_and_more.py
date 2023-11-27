# Generated by Django 4.2.7 on 2023-11-27 15:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("coop", "0003_climatecontrolrisk"),
    ]

    operations = [
        migrations.CreateModel(
            name="HousekeepingPestsRisk",
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
                    "pest_infestation",
                    models.CharField(
                        choices=[
                            ("1", "Must be addressed"),
                            ("2", "Should be addressed"),
                            ("3", "Could be addressed"),
                            ("4", "Not applicable/no action needed"),
                        ],
                        max_length=1,
                        verbose_name="Pest Infestation",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="PersonnelRisk",
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
                    "staff_training_emergency_procedures",
                    models.CharField(
                        choices=[
                            ("1", "Must be addressed"),
                            ("2", "Should be addressed"),
                            ("3", "Could be addressed"),
                            ("4", "Not applicable/no action needed"),
                        ],
                        max_length=1,
                        verbose_name="Staff Training",
                    ),
                ),
                (
                    "staff_training_security_procedures",
                    models.CharField(
                        choices=[
                            ("1", "Must be addressed"),
                            ("2", "Should be addressed"),
                            ("3", "Could be addressed"),
                            ("4", "Not applicable/no action needed"),
                        ],
                        max_length=1,
                        verbose_name="Security Procedures",
                    ),
                ),
                (
                    "security_staff_training_recognizing_hazards",
                    models.CharField(
                        choices=[
                            ("1", "Must be addressed"),
                            ("2", "Should be addressed"),
                            ("3", "Could be addressed"),
                            ("4", "Not applicable/no action needed"),
                        ],
                        max_length=1,
                        verbose_name="Recognizing Hazards",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="SecurityRisk",
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
                    "automated_security_system",
                    models.CharField(
                        choices=[
                            ("1", "Must be addressed"),
                            ("2", "Should be addressed"),
                            ("3", "Could be addressed"),
                            ("4", "Not applicable/no action needed"),
                        ],
                        max_length=1,
                        verbose_name="Automated Security System",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="StorageRisk",
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
                    "anchor_shelving",
                    models.CharField(
                        choices=[
                            ("1", "Must be addressed"),
                            ("2", "Should be addressed"),
                            ("3", "Could be addressed"),
                            ("4", "Not applicable/no action needed"),
                        ],
                        max_length=1,
                        verbose_name="Anchor Shelving",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]