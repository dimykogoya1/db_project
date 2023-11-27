# Generated by Django 4.2.7 on 2023-11-27 17:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("coop", "0023_buildingplan_overallsalvagepriority_collection"),
    ]

    operations = [
        migrations.CreateModel(
            name="InsuranceInformation",
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
                    "policy_number",
                    models.CharField(max_length=50, verbose_name="Policy Number"),
                ),
                (
                    "policy_inception_date",
                    models.DateField(verbose_name="Policy Inception Date"),
                ),
                (
                    "policy_expiration_date",
                    models.DateField(verbose_name="Policy Expiration Date"),
                ),
                (
                    "property_covered",
                    models.CharField(
                        choices=[
                            ("Building", "Building"),
                            ("Machinery", "Machinery"),
                            ("Equipment", "Equipment"),
                        ],
                        max_length=20,
                        verbose_name="Property Covered",
                    ),
                ),
                (
                    "amount_of_coverage",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=50,
                        verbose_name="Amount of Coverage",
                    ),
                ),
                (
                    "deductible",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=50,
                        null=True,
                        verbose_name="Amount of Deductible",
                    ),
                ),
            ],
        ),
    ]
