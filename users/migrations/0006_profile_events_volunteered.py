# Generated by Django 4.1.7 on 2023-03-26 04:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("am", "__first__"),
        ("users", "0005_profile_profile_picture"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="events_volunteered",
            field=models.ManyToManyField(
                blank=True, related_name="event_member", to="am.event"
            ),
        ),
    ]
