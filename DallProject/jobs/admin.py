from django.contrib import admin
from .models import Job

# Define the admin class
class JobAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

# Register the admin class with the associated model
admin.site.register(Job, JobAdmin)
