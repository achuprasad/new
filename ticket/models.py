from django.db import models

# Create your models here.
from django.db import models
from django.utils.crypto import get_random_string

class Ticket(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    ticket_number = models.CharField(max_length=10, unique=True)
    social_media_platform = models.CharField(max_length=20,null=True,blank=True)
    interests = models.TextField(blank=True,null=True)

    def save(self, *args, **kwargs):
        if not self.ticket_number:
            self.ticket_number = get_random_string(length=5, allowed_chars='0123456789')
        super().save(*args, **kwargs)
