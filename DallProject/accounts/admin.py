from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'birth_date', 'phone_number', 'major', 'degree', 'university_name')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'major', 'degree', 'university_name')

admin.site.register(UserProfile, UserProfileAdmin)