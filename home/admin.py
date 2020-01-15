from django.contrib import admin
from home.models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'detail', 'date_published', 'lang')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Project, ProjectAdmin)