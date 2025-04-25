from django.db import models
from django.conf import settings
# Create your models here.

class Form(models.Model):
    """
    store metadata and structure of a form created via drag and drop builder
    """
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    schema = models.JSONField() 
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
