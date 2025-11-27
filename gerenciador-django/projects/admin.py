from django.contrib import admin
from .models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'usuario')
    search_fields = ('titulo', 'usuario__username')
    list_filter = ('usuario',)

admin.site.register(Project, ProjectAdmin)