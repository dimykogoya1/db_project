# Generated by Django 4.2.7 on 2023-11-27 17:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("coop", "0021_reconfiguration_datarestoration"),
    ]

    operations = [
        migrations.CreateModel(
            name="AdministrativeRecord",
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
                    "priority_ranking",
                    models.IntegerField(
                        choices=[
                            (1, "Priority 1"),
                            (2, "Priority 2"),
                            (3, "Priority 3"),
                            (4, "Priority 4"),
                            (5, "Priority 5"),
                        ],
                        verbose_name="Priority Ranking",
                    ),
                ),
                (
                    "record_type",
                    models.CharField(
                        max_length=150, verbose_name="Type of Record Group"
                    ),
                ),
            ],
            options={
                "ordering": ["priority_ranking"],
            },
        ),
        migrations.CreateModel(
            name="ComputerOperation",
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
                    "category",
                    models.CharField(
                        choices=[
                            ("OR", "Computer Operation Relocation"),
                            ("ERA", "Emergency Remote Access"),
                            ("P", "Procedures"),
                            ("LW", "Library Website"),
                        ],
                        max_length=3,
                        verbose_name="Category",
                    ),
                ),
                ("procedures", models.TextField(blank=True, verbose_name="Procedures")),
                ("computer", models.CharField(max_length=150)),
                ("intranet", models.TextField(blank=True, verbose_name="Intranet")),
                (
                    "website",
                    models.TextField(blank=True, verbose_name="Library Website"),
                ),
                (
                    "regional_network",
                    models.TextField(
                        blank=True, verbose_name="Regional Library Network"
                    ),
                ),
                (
                    "online_catalog",
                    models.TextField(blank=True, verbose_name="Local Online Catalog"),
                ),
                (
                    "subscription_services",
                    models.TextField(
                        blank=True, verbose_name="Online Subscription Services"
                    ),
                ),
                ("other", models.TextField(blank=True, verbose_name="Other")),
            ],
            options={
                "ordering": ["category"],
            },
        ),
        migrations.CreateModel(
            name="Department",
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
                    "priority_ranking",
                    models.PositiveIntegerField(verbose_name="Priority Ranking"),
                ),
                (
                    "name",
                    models.CharField(max_length=150, verbose_name="Department Name"),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
