# Generated by Django 4.1.7 on 2023-03-26 05:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0006_profile_events_volunteered"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="lastname",
            field=models.CharField(blank=True, default="", max_length=30, null=True),
        ),
    ]
