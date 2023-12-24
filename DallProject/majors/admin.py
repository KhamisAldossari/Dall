from django.contrib import admin
from .models import Major

# Optional: Define Inline admin classes for the many-to-many relationships
class JobInline(admin.TabularInline):
    model = Major.jobs.through
    extra = 1

class CertificateInline(admin.TabularInline):
    model = Major.certificates.through
    extra = 1

class CompanyInline(admin.TabularInline):
    model = Major.companies.through
    extra = 1

class CourseInline(admin.TabularInline):
    model = Major.courses.through
    extra = 1

class SkillInline(admin.TabularInline):
    model = Major.skills.through
    extra = 1

# Define the admin class
class MajorAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    inlines = [JobInline, CertificateInline, CompanyInline, CourseInline, SkillInline]

# Register the admin class with the associated model
admin.site.register(Major, MajorAdmin)
