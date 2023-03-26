# Generated by Django 4.1.7 on 2023-03-26 04:53

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Event",
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
                ("name", models.CharField(max_length=100)),
                ("description", ckeditor.fields.RichTextField()),
                ("short_description", ckeditor.fields.RichTextField(max_length=200)),
                ("start_date", models.DateField()),
                ("start_time", models.TimeField()),
                ("end_date", models.DateField()),
                ("end_time", models.TimeField()),
                ("venue", models.CharField(max_length=200)),
                (
                    "cover_image",
                    models.ImageField(
                        blank=True, null=True, upload_to="events_cover_pics"
                    ),
                ),
                ("is_this_a_colab", models.BooleanField(default=False)),
                ("colab_with", models.CharField(blank=True, max_length=100, null=True)),
                ("linkedin_post_url", models.URLField(blank=True)),
                (
                    "slug",
                    models.SlugField(
                        blank=True, max_length=100, null=True, unique=True
                    ),
                ),
                (
                    "overall_coordinator",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
