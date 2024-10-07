from django.db import models
from artworks.models import Artwork

# Create your models here.
class Exhibition(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
class ExhibitionArtWorks(models.Model):
    exhibition_id = models.ForeignKey(Exhibition, on_delete=models.CASCADE)
    artwork_id = models.ForeignKey(Artwork, on_delete=models.CASCADE)