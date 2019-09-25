from django.contrib import admin
from .models import *

# Register your models here.
class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 3


class ProjectTechInline(admin.TabularInline):
    model = ProjectTech
    extra = 3


class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline, ProjectTechInline]


admin.site.register(Project, ProjectAdmin)
admin.site.register(Profile)
admin.site.register(Menu)
