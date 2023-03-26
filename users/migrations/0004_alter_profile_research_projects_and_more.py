# Generated by Django 4.1.7 on 2023-03-26 01:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("startup", "0003_remove_startupproject_project_cover_picture_url_and_more"),
        ("research", "0005_alter_researchproject_short_description"),
        ("users", "0003_alter_profile_research_projects_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="research_projects",
            field=models.ManyToManyField(
                blank=True,
                related_name="research_member",
                to="research.researchproject",
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="startup_projects",
            field=models.ManyToManyField(
                blank=True, related_name="startup_member", to="startup.startupproject"
            ),
        ),
    ]
