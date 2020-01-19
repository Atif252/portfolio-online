from django.contrib import admin
from home.models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'detail', 'date_published', 'lang')

admin.site.register(Project, ProjectAdmin)