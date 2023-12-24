from django.contrib import admin
from .models import Course

# Define the admin class
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'duration', 'provider')
    search_fields = ('name', 'provider')

# Register the admin class with the associated model
admin.site.register(Course, CourseAdmin)
