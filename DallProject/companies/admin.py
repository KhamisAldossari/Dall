from django.contrib import admin
from .models import Company

# Define the admin class
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'industry')
    search_fields = ('name', 'industry')

# Register the admin class with the associated model
admin.site.register(Company, CompanyAdmin)
