# Generated by Django 4.2.7 on 2023-11-27 15:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("coop", "0008_alter_questionaire_institution_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="WeeklyOpening",
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
                    "day_of_week",
                    models.PositiveIntegerField(
                        choices=[
                            (1, "Monday"),
                            (2, "Tuesday"),
                            (3, "Wednesday"),
                            (4, "Thursday"),
                            (5, "Friday"),
                            (6, "Saturday"),
                            (7, "Sunday"),
                        ],
                        unique=True,
                    ),
                ),
                (
                    "backup_staff",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="backup_opening_staff",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "primary_staff",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="primary_opening_staff",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Weekly Opening Staff Schedules",
            },
        ),
    ]