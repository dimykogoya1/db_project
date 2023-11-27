# Generated by Django 4.2.7 on 2023-11-27 15:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("coop", "0007_questionaire"),
    ]

    operations = [
        migrations.AlterField(
            model_name="questionaire",
            name="institution",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="questionnaires",
                to="coop.institution",
            ),
        ),
        migrations.AlterField(
            model_name="questionaire",
            name="question",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="questionnaires",
                to="coop.question",
            ),
        ),
        migrations.CreateModel(
            name="Tasks",
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
                ("answer", models.BooleanField()),
                (
                    "institution_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tasks",
                        to="coop.institution",
                        verbose_name="Institution Name",
                    ),
                ),
                (
                    "items",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="operating_procedures",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tasks",
                        to="coop.question",
                    ),
                ),
            ],
        ),
    ]
