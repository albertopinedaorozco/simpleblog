from django.db import models

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    picture = models.ImageField(upload_to='media/',null=True, blank=True)



