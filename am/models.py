from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


class Event(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    description = RichTextField()
    short_description = RichTextField(max_length=400)
    start_date = models.DateField()
    start_time = models.TimeField(blank=True, null=True)
    end_date = models.DateField()
    end_time = models.TimeField(blank=True, null=True)
    venue = RichTextField(max_length=200)
    cover_picture = models.ImageField(upload_to='events_cover_pics', blank=True, null=True)
    poster = models.ImageField(upload_to='events_posters', blank=True, null=True)
    is_this_a_colab = models.BooleanField(default=False)
    colab_with = models.CharField(max_length=100, blank=True, null=True)
    linkedin_post_url = models.URLField(max_length=200, blank=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    overall_coordinator = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    event_domain = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name + " : " + str(self.start_date)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Event, self).save(*args, **kwargs)