# Generated by Django 5.0.6 on 2024-07-27 07:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Posts",
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
                ("title", models.CharField(max_length=100)),
                ("body", models.CharField(max_length=10000)),
                (
                    "created_at",
                    models.DateTimeField(blank=True, default=datetime.datetime.now),
                ),
            ],
        ),
    ]
