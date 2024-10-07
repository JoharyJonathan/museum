from django.contrib import admin
from .models import Exhibition, ExhibitionArtWorks

# Register your models here.
class ExhibitionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'start_date', 'end_date', 'location')
    search_fields = ('title', 'description')
    
admin.site.register(Exhibition, ExhibitionAdmin)
admin.site.register(ExhibitionArtWorks)