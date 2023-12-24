from django.contrib import admin
from .models import Certificate

# Define the admin class
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

# Register the admin class with the associated model
admin.site.register(Certificate, CertificateAdmin)
