from django.conf import settings
from django.db import models

# Create your models here.
# Object

class Post(models.Model):
    text = models.TextField()
    upload = models.FileField(upload_to='uploads/')
    
    def publish(self):
        self.save()