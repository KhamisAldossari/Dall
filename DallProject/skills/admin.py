from django.contrib import admin
from .models import Skill

# Define the admin class
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

# Register the admin class with the associated model
admin.site.register(Skill, SkillAdmin)
