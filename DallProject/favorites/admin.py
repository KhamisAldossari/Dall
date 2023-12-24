from django.contrib import admin
from .models import Favorite

# Define the admin class
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'major', 'created_at')
    search_fields = ('user__username', 'major__name')
    list_filter = ('major', 'user')
    raw_id_fields = ('user', 'major')

# Register the admin class with the associated model
admin.site.register(Favorite, FavoriteAdmin)
