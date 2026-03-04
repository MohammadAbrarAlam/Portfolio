from django.contrib import admin
from .models import Project
admin.site.register(Project)
class ProjectAdmin(admin.ModelAdmin):
  list_display=['title','description','tech_stack','github_link','image']
