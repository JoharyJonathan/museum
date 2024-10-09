from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Role(models.Model):
    role_name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.role_name}"

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, max_length=255)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    
    # Modifications pour utiliser l'email comme champ d'authentification
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  # Rendre 'username' optionnel si besoin
    
    def __str__(self):
        return self.email  # Afficher l'email au lieu du username

class AdminLogs(models.Model):
    action = models.CharField(max_length=255)
    entity = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.action

class Permissions(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    entity = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.action