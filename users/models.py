from django.db import models
from django.contrib.auth.models import User
from allauth.account.models import EmailAddress
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.utils.text import slugify
from django.db.models.signals import post_save
from allauth.account.signals import email_confirmed
from django.utils import timezone
from research.models import ResearchProject
from startup.models import StartupProject
from am.models import Event

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=30, blank=False, null=False)
    lastname = models.CharField(max_length=30, blank=True, null=True, default='')
    email = models.EmailField(blank=False, null=False)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    slug = models.SlugField(null=True)
    research_projects = models.ManyToManyField(ResearchProject, blank=True, related_name='research_member')
    startup_projects = models.ManyToManyField(StartupProject, blank=True, related_name='startup_member')
    profile_picture = models.ImageField(blank=True, upload_to='members_profile_pics')
    events_volunteered = models.ManyToManyField(Event, blank=True, related_name='event_member')

    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    )
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse("show_profile_page", args=(self.user.username,))

@receiver(post_save, sender=get_user_model())
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, email=instance.email, slug=instance.username)

@receiver(post_save, sender=get_user_model())
def save_profile(sender, instance, created, **kwargs):
    instance.profile.slug = slugify(instance.username)
    instance.profile.email = instance.email
    instance.profile.save()

@receiver(email_confirmed)
def update_user_email(sender, request, email_address, **kwargs):
    email_address.set_as_primary()
    stale_addresses = EmailAddress.objects.filter(
        user=email_address.user).exclude(primary=True).delete()

User._meta.get_field('email')._unique = True