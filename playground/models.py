from django.db import models
import random
import string


# Create your models here.

class TesTeam(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    hashid = models.CharField(max_length=8, primary_key=True, unique=True, editable=True)

    def save(self, *args, **kwargs):
        if not self.hashid:
            # generate a random 8 character string for hashid
            self.hashid = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name

