from django.db import models
from ckeditor.fields import RichTextField 
from django.contrib.auth.models import User

class researchproject(models.Model):

    STATUS_CHOICES = [
        ('Completed', 'Completed'),
        ('In Progress', 'In Progress'),
    ]

    name = models.CharField(max_length=100)
    description = RichTextField()
    incharge = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)
    domain = models.CharField(max_length=100)
    project_cover_picture_url = models.ImageField(blank=True, upload_to='researchproject_pics')

    def __str__(self):
        return self.name