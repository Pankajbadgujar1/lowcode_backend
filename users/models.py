from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin' , 'Admin'),
        ('user' , 'User'),
        ('developer', 'Developer'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')
    organization = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.username