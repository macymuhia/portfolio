from django.contrib import admin
from django.apps import apps
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


class MenuAdmin(admin.ModelAdmin):
    model = Menu
    list_display = ("name", "weight")


# model registered with custom admin
admin.site.register(Project, ProjectAdmin)
admin.site.register(Profile)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Quote)


# all other models
# models = apps.get_models()

# for model in models:
#     try:
#         admin.site.register(model)
#     except admin.sites.AlreadyRegistered:
#         pass

