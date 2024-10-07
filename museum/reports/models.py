from django.db import models
from artworks.models import Artwork
from django.conf import settings

# Create your models here.
class Comments(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.content
    
class Reports(models.Model):
    type = models.CharField(max_length=255)
    admin = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    generated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.type