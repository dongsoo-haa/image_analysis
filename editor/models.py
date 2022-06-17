from django.db import models

# Create your models here.
class Post(models.Model):
    text = models.TextField()
    upload = models.FileField()
    
    def publish(self):
        self.save()