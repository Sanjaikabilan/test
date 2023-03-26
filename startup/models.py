from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Team(models.Model):
    name = models.CharField(max_length=100)
    description = RichTextField()
    origin_story = RichTextField()

    def __str__(self):
        return self.name

class StartupProject(models.Model):

    STATUS_CHOICES = [
        ('Completed', 'Completed'),
        ('In Progress', 'In Progress'),
    ]

    name = models.CharField(max_length=100)
    description = RichTextField()
    incharge = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='In Progress')
    domain = models.CharField(max_length=100)
    project_cover_picture = models.ImageField(blank=True, upload_to='startup_project_pics')
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.name