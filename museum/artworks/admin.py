from django.contrib import admin
from .models import Artist, Artwork, Categories, Multimedia

# Register your models here.
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'biography', 'birthdate', 'deathdate', 'nationality', 'picture')
    search_fields = ('name', 'biography', 'birthdate')
    
class ArtworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'year_created', 'image', 'media_type')
    search_fields = ('title', 'description')
    
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    
class MultiMediaAdmin(admin.ModelAdmin):
    list_display = ('type', 'url', 'description')
    search_fields = ('type',)
    
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Artwork, ArtworkAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Multimedia, MultiMediaAdmin)