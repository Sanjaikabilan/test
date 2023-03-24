# Generated by Django 4.1.7 on 2023-03-24 18:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ps", "0002_team"),
    ]

    operations = [
        migrations.CreateModel(
            name="Member",
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
                ("name", models.CharField(max_length=50)),
            ],
        ),
    ]
