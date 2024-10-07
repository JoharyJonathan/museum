from django.contrib import admin
from .models import Comments, Reports

# Register your models here.
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('user', 'artwork', 'content', 'rating')
    search_fields = ('user', 'content')
    
admin.site.register(Comments, CommentsAdmin)
admin.site.register(Reports)