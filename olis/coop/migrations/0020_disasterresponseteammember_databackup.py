# Generated by Django 4.2.7 on 2023-11-27 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("coop", "0019_teamname_teamresponsibility"),
    ]

    operations = [
        migrations.CreateModel(
            name="DisasterResponseTeamMember",
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
                ("name", models.CharField(max_length=150, verbose_name="Name")),
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("Leader", "Leader"),
                            ("Coordinator", "Coordinator"),
                            ("Member", "Member"),
                        ],
                        max_length=20,
                        verbose_name="Role",
                    ),
                ),
                (
                    "contact_phone",
                    models.CharField(max_length=30, verbose_name="Phone"),
                ),
                (
                    "contact_cell_phone",
                    models.CharField(
                        blank=True, max_length=20, verbose_name="Cell Phone"
                    ),
                ),
                (
                    "contact_after_hours_phone",
                    models.CharField(
                        blank=True, max_length=20, verbose_name="After Hours Phone"
                    ),
                ),
                (
                    "contact_email",
                    models.EmailField(blank=True, max_length=254, verbose_name="Email"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DataBackup",
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
                    "type_of_data",
                    models.CharField(
                        choices=[
                            ("Collection Records", "Collection Records"),
                            ("In-house Databases", "In-house Databases"),
                            ("Financial Information", "Financial Information"),
                            ("Digital Collections", "Digital Collections"),
                        ],
                        max_length=150,
                        verbose_name="Type of Data",
                    ),
                ),
                (
                    "location_of_data",
                    models.CharField(max_length=150, verbose_name="Location of Data"),
                ),
                (
                    "on_site_backup",
                    models.CharField(
                        blank=True,
                        max_length=150,
                        verbose_name="On-site Location of Backup",
                    ),
                ),
                (
                    "off_site_location",
                    models.CharField(
                        blank=True,
                        max_length=150,
                        verbose_name="Off-site Location of Backup",
                    ),
                ),
                (
                    "frequency",
                    models.CharField(
                        blank=True, max_length=50, verbose_name="Frequency of Backup"
                    ),
                ),
                (
                    "person_backup",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="data_backups",
                        to="coop.disasterresponseteammember",
                    ),
                ),
            ],
        ),
    ]
