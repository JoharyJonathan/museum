from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=255)
    biography = models.TextField()
    birthdate = models.DateField()
    deathdate = models.DateField()
    nationality = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='artist_pics', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class Categories(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class Artwork(models.Model):
    title = models.CharField(max_length=255)
    artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE)
    description = models.TextField()
    year_created = models.DateField()
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='art_pics', blank=True, null=True)
    media_type = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
class Multimedia(models.Model):
    artwork_id = models.ForeignKey(Artwork, on_delete=models.CASCADE)
    type = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.type